# AutoWebGLM: A Large Language Model-based Web Navigating Agent

**Authors:** Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, and Jie Tang  
**Venue:** KDD 2024, Barcelona, Spain

## 1. Background and Context

Large language models can understand instructions and generate responses, making them promising foundations for agents that browse websites on a user’s behalf. Such agents could search for information, summarize news, fill forms, navigate online services, and complete multi-step tasks.

However, the authors identify three fundamental obstacles to reliable real-world web navigation:

- **Complex webpage representations:** Raw HTML is long, structurally complicated, and filled with redundant or distracting content.
- **Diverse actions:** A general agent must support clicking, typing, scrolling, selecting options, changing tabs, opening URLs, and many other operations across different sites.
- **Open-domain task difficulty:** Websites differ substantially in design and operating logic. Tasks may require planning, remembering earlier actions, interpreting the current page state, and recovering from errors.

Existing agents also lack a universal action space, struggle with verbose and diverse pages, and often cannot infer correctly or check their own behavior. Once they enter an incorrect action loop, they may repeatedly make the same mistake.

Earlier systems cover only part of the problem. WebGPT and WebGLM primarily use the web for question answering. MindAct filters HTML elements and asks the model multiple-choice questions, sometimes requiring more than ten model calls for one operation. WebAgent performs strongly but relies on a 540-billion-parameter Flan-U-PaLM model, creating deployment difficulties. By contrast, this work seeks strong practical web-navigation performance using a single 6-billion-parameter model.

The paper treats browsing as a **sequential decision problem**. At each step:

- The state \(S\) contains the page’s HTML, URL, and current window position.
- The history \(H_t\) summarizes prior states and actions.
- A policy \(\pi\) selects the next action from the current state and history.
- The webpage transition function \(T\) produces the next state after the action.
- Interaction stops when the model issues `finish` or reaches the maximum allowed sequence length.

In plain terms, the agent repeatedly observes the page, considers what it has already done, selects one browser operation, observes the result, and continues until the task is finished.

## 2. Research Goal and Objectives

The main goal is to build an open, compact, and practically usable language-model agent—**AutoWebGLM**—that can understand webpages, plan multi-step tasks, execute browser operations, learn from its errors, and specialize through practice in particular web environments.

The specific objectives are to:

1. Build the agent on the open **ChatGLM3-6B** model.
2. simplify HTML while retaining the information required for navigation;
3. define unified observation and action spaces for many kinds of websites;
4. construct a large, reliable browsing dataset through a hybrid human–AI process;
5. teach the model progressively through curriculum learning;
6. reduce action hallucinations by having the model learn from correct and incorrect self-generated operations;
7. use rejection sampling finetuning to improve performance in specific interactive environments;
8. create **AutoWebBench**, described as the first bilingual English–Chinese benchmark for real-world webpage browsing; and
9. compare the resulting 6B model against GPT-3.5, GPT-4, Claude 2, open LLMs, and specialized web agents.

## 3. Methods (Approach/Design)

### 3.1 Overall architecture

AutoWebGLM combines an LM agent with an interaction framework.

**Figure 3** divides the system into three connected parts:

1. **Data construction**
   - Source data from real-world environments and open-source training sets
   - Hybrid human–AI construction using manual annotation assisted by LLMs
   - Trace collection from virtual environments

2. **Training**
   - Curriculum learning to understand and manipulate webpages
   - Reinforcement learning to learn from mistakes
   - Rejection sampling finetuning to specialize in particular environments

3. **Interaction**
   - A webpage supplies a screenshot and HTML.
   - Perception uses an element selector.
   - Parsing uses OCR and an HTML parser.
   - The observation given to AutoWebGLM includes parsed HTML, task, and history.
   - AutoWebGLM predicts an action.
   - An automated browser executes it, after which the cycle repeats.

The authors also deployed the system as a Chrome extension.

### 3.2 Observation space

Each model input contains four important forms of information:

- **Task description:** what the user wants accomplished.
- **Simplified HTML:** page structure and content, with operable elements marked.
- **Current position:** viewport position and total page size, helping the agent distinguish the visible area from the scale of the full page.
- **Previous operations:** explicit action history, helping the agent maintain consistency and avoid repeating failed actions.

The actual prompt wraps the simplified content in `<html>` tags, explains the available browser functions, supplies previous commands, open tabs, current versus maximum page position, and the task, and asks for exactly one next command plus a brief explanation.

OCR is used to annotate text encountered during screenshot/image parsing. The paper nevertheless relies primarily on HTML and identifies fuller multimodal processing as future work.

### 3.3 HTML simplification

Raw HTML is pruned so that essential content and page structure remain while redundant or disruptive elements are removed.

**Algorithm 1, the HTML Pruner**, starts from a set of retained or actionable elements. For each such element, it collects a limited number of:

- ancestors,
- descendants, and
- siblings.

It repeats this process for a specified recursion count while progressively reducing the depth, child, and sibling limits. It then walks through the HTML tree in reverse and removes nodes that are not selected or do not carry useful text, attributes, branching structure, or root information.

The result is a shorter tree intended to preserve the context around important elements without overwhelming the model.

### 3.4 Action space

**Table 1** defines ten operation types:

| Instruction | Meaning |
|---|---|
| `click(id)` | Click an element |
| `hover(id)` | Hover over an element |
| `select(id, option)` | Choose an option |
| `type_string(id, text, enter)` | Type into an element, optionally submitting |
| `scroll_page(direction)` | Scroll upward or downward |
| `go(direction)` | Navigate forward or backward |
| `jump_to(url, newtab)` | Open a URL, optionally in a new tab |
| `switch_tab(id)` | Switch to a specified tab |
| `user_input(message)` | Ask the user to interact |
| `finish(answer)` | Stop and return an answer |

### 3.5 Hybrid human–AI data construction

The authors report approximately **10,000 real browsing traces** constructed through model-assisted and manual methods. Their motivation was that direct human collection is costly and privacy-sensitive, while current LLMs cannot reliably generate correct complex trajectories by themselves.

They divide construction into two stages.

#### Stage 1: Web recognition and simple operations

**Web recognition data** teach the model to understand HTML formats, recognize elements such as buttons, text boxes, and images, and explain their interactive roles.

The authors:

- collected URLs from mainstream Chinese and English websites listed by Similarweb;
- used their parser to identify actionable components and record positions and sizes;
- rearranged and simplified the component tree;
- created questions about website and component functions;
- used GPT-3.5-Turbo to paraphrase questions for linguistic variety; and
- used GPT-3.5-Turbo to produce short answers from the simplified HTML and question.

**Simple-operation data** teach single-step behaviors such as clicking, typing, scrolling, and navigating. Data were divided by operation type, with split sizes adjusted to reflect practical operation frequency.

A first attempt asked GPT-3.5-Turbo to generate tasks, intentions, and operations and used Selenium to test executability. This did not reach acceptable accuracy, and the correctness of generated operations was difficult to judge. The final procedure therefore began with actionable webpage elements and valid operations, then used GPT-3.5-Turbo to generate a corresponding task and step intention. Fixed actions such as scrolling and opening a URL were generated with templates; flexible actions such as clicking and typing received LLM assistance.

#### Stage 2: Complex tasks

Each complex sample contains:

- a realistic multi-step browsing task,
- the operation sequence that completes it, and
- the intention behind each step.

The team initially generated **50 candidate complex tasks per website** with an Evol-Instruct-inspired prompting method. Approximately **20 feasible tasks per website** were manually selected and labeled.

Because even advanced LLMs could not reliably execute these tasks, humans performed them using a browser plugin that recorded actions. GPT-4 then inferred the intention associated with every step. The authors first tried inferring intentions one step at a time, but this produced weak connections between steps and high API cost. Their final “global thought-chain” prompt supplied all actions and important HTML segments together and asked GPT-4 to infer every step’s intention, yielding more coherent traces.

The final training collection combined these new data with the Mind2Web and MiniWoB++ training sets.

**Figure 4** illustrates both stages. Its complex-task example asks for the price of the latest MacBook. The trajectory clicks a search field, types “latest Macbook Air,” changes sorting from “Featured” to “Newest Arrival,” and returns a price. The diagram also contrasts a sensible task with an inappropriate generated request (“Equip me with a gun through this website”), showing the role of manual filtering.

**Figure 5** gives the training-data mixture:

- Complex tasks: **60 units, 38.71%**
- Simple tasks: **42, 27.1%**
- Web recognition: **40, 25.81%**
- Mind2Web: **7, 4.51%**
- MiniWoB++: **6, 3.87%**

### 3.6 Human annotation

Twenty annotators worked for one month using Google Chrome with the recording plugin. They checked whether website descriptions matched tasks and judged each task for clarity, relevance, achievability, complexity, and subjectivity. Unsuitable tasks were skipped.

Annotators recorded every step, including login and CAPTCHA steps. They manually edited answer responses when needed and could revise or abandon tasks that proved impossible.

### 3.7 Three-stage training

**Figure 6** summarizes the training sequence.

#### Step I: Curriculum learning with supervised finetuning

The model first learns easier recognition and single-step operations, then advances to complex planning and reasoning. The supervised objective increases the probability of the correct output given each input.

- Stage 1 teaches page structure, component functions, and predefined operations.
- Stage 2 teaches task decomposition and selection of subsequent steps from the current page and action history.

SFT used:

- learning rate: **\(1\times10^{-5}\)**
- batch size: **32**

#### Step II: Self-sampling reinforcement learning

The SFT model could imitate actions but sometimes ignored the page state or action history, producing operational hallucinations.

To address this, the authors sampled the SFT model **20 times** on every complex training sample. Generated outputs were compared with the gold action to form positive–negative preference pairs.

Samples were retained only when the model succeeded between 1 and 19 times:

- Always-correct items lacked useful negative examples.
- Always-wrong items were treated as likely outliers or unsuitable training cases.
- Duplicate incorrect operations were removed.

Filtering produced approximately **13,000 contrastive examples**. The model was optimized with Direct Preference Optimization, which favors the correct action over an incorrect one. Pure DPO was unstable, so the authors combined it with the original SFT objective to preserve language and agent capabilities.

DPO settings were:

- learning rate: **\(1\times10^{-6}\)**
- batch size: **64**
- DPO \(\beta\): **0.15**
- SFT-loss weight: **0.8**

#### Step III: Rejection sampling finetuning

RFT specializes the agent through self-play. The model attempts tasks repeatedly, and only successful trajectories—identified by environmental signals or manually designed rules—are used for further finetuning.

Because live websites have network and policy constraints, this stage used MiniWoB++ and WebArena sandboxes.

- **MiniWoB++:** Queries were generated automatically, with more queries for harder tasks. Environment-verified successful traces were retained. This produced about **15,000 traces comprising 66,000 steps**.
- **WebArena:** To avoid test overlap, the authors manually wrote distinct queries from templates. Each sample was attempted **64 times**. A trajectory was retained if the model completed the task at least once according to manually written rules. This produced about **240 traces comprising 2,000 steps**.

Separate RFT models were trained for the two environments with learning rate **\(1\times10^{-5}\)** and batch size **32**.

### 3.8 AutoWebBench and evaluation design

AutoWebBench is a bilingual English–Chinese benchmark derived from the authors’ complex-task traces.

It contains:

- **in-domain/cross-task splits:** test tasks from websites represented in training;
- **out-of-domain/cross-domain splits:** tasks from websites entirely excluded from training;
- English and Chinese versions of both conditions; and
- **50 human-verified traces per split**.

Evaluation follows Mind2Web and measures **Step Success Rate (SSR)**—whether individual predicted operations are correct. The paper also evaluates:

- Mind2Web under its standard settings and MindAct framework;
- MiniWoB++ on **56 tasks with 100 episodes per task**; and
- WebArena after integrating AutoWebGLM’s parser and execution modules.

## 4. Results and Findings

### 4.1 AutoWebBench

AutoWebGLM substantially outperformed all listed models on all four bilingual splits.

| Model | English cross-task | English cross-domain | Chinese cross-task | Chinese cross-domain |
|---|---:|---:|---:|---:|
| GPT-3.5-Turbo | 12.1 | 6.4 | 13.5 | 10.8 |
| GPT-4 | 38.6 | 39.7 | 36.7 | 36.3 |
| Claude 2 | 13.2 | 8.1 | 13.0 | 7.9 |
| LLaMA2-7B | 3.3 | 2.5 | Not reported | Not reported |
| LLaMA2-70B | 8.3 | 8.9 | Not reported | Not reported |
| Qwen-7B | 9.0 | 7.6 | 9.1 | 7.5 |
| **AutoWebGLM-6B** | **64.8** | **58.6** | **65.4** | **61.8** |

Thus, AutoWebGLM’s lowest score, 58.6, remained far above GPT-4’s best score of 39.7. Its results were also relatively consistent across English and Chinese and declined only moderately on unseen websites.

### 4.2 Mind2Web

| Model | Cross-task | Cross-website | Cross-domain | Average |
|---|---:|---:|---:|---:|
| GPT-3.5-Turbo | 17.4 | 16.2 | 18.6 | 17.4 |
| GPT-4, top-10 candidates | 36.2 | 30.1 | 26.4 | 30.9 |
| Flan-T5-XL, finetuned, 3B | 52.0 | 38.9 | 39.6 | 43.5 |
| HTML-T5-XL, finetuned, reported as 543B | **71.5** | **62.2** | **67.1** | **66.9** |
| LLaMA2-7B, finetuned | 52.7 | 47.1 | 50.3 | 50.1 |
| LLaMA2-70B, finetuned | 55.8 | 51.6 | 55.7 | 54.4 |
| Qwen-VL-9.6B, finetuned | 12.6 | 10.1 | 8.0 | 10.2 |
| SeeClick-9.6B, finetuned | 23.7 | 18.8 | 20.2 | 20.9 |
| **AutoWebGLM-6B** | **66.4** | **56.4** | **55.8** | **59.5** |

AutoWebGLM ranked below HTML-T5-XL but above every other listed baseline on average. It exceeded GPT-4 by 28.6 average SSR points and the finetuned LLaMA2-70B by 5.1 points.

### 4.3 MiniWoB++ and WebArena

| Model | MiniWoB++ | WebArena |
|---|---:|---:|
| GPT-3.5-Turbo | 13.4 | 6.2 |
| GPT-4 | 32.1 | 14.4 |
| Text-Bison-001 | Not reported | 5.1 |
| LLaMA2-7B, finetuned where marked | 42.8 | 1.2 |
| LLaMA2-70B, finetuned where marked | 47.1 | 0.6 |
| HTML-T5-XL, finetuned | 85.6 | Not reported |
| WebN-T5-XL, finetuned | 48.4 | Not reported |
| Lemur-70B | Not reported | 5.3 |
| **AutoWebGLM-6B** | **89.3** | **18.2** |

AutoWebGLM produced the best reported result on both benchmarks: 89.3 on MiniWoB++ and 18.2 on WebArena. It exceeded HTML-T5-XL by 3.7 points on MiniWoB++ and GPT-4 by 3.8 points on WebArena.

### 4.4 MiniWoB++ task-level behavior

Across the 56 tasks in Table 8, average success rates were:

- **AutoWebGLM: 0.893**
- HTML-T5-XL: 0.856
- WebN-T5-XL: 0.484
- GPT-4: 0.321
- GPT-3.5-Turbo: 0.134

AutoWebGLM achieved **1.00 success** on 38 of the 56 listed tasks, including all choose-date variants; many button, dialog, menu, tab, email, form-entry, login, search, navigation, and social-media tasks; `guess-number`; `use-spinner`; and others.

Its weaker tasks were:

- `enter-time`: **0.00**
- `choose-list`: **0.15**
- `click-checkboxes-soft`: **0.37**
- `book-flight`: **0.50**
- `click-scroll-list`: **0.57**
- `login-user-popup`: **0.63**
- `click-shape`: **0.64**
- `count-shape`: **0.65**
- `click-color` and `tic-tac-toe`: **0.74**
- `click-collapsible-2` and `social-media-some`: **0.76**
- `click-checkboxes-large`: **0.83**
- `use-autocomplete`: **0.85**
- `social-media-all`: **0.90**
- `click-test-2`: **0.93**

Some results reveal different strengths between systems. For example, AutoWebGLM scored 1.00 on `choose-date-medium`, `click-shades`, `guess-number`, and `use-spinner`, where HTML-T5-XL scored 0.56, 0.00, 0.13, and 0.07. Conversely, HTML-T5-XL scored 1.00 on `enter-time`, where AutoWebGLM scored 0.00, and substantially outperformed it on `click-checkboxes-soft` and `click-scroll-list`.

### 4.5 Training-data ablation

| Training configuration | AutoWebBench | Mind2Web | MiniWoB++ | WebArena |
|---|---:|---:|---:|---:|
| Only original training set | — | 48.1 | 44.3 | — |
| Add Stage 1 simple/recognition data | 23.5 | 48.4 | 48.3 | 2.5 |
| Add Stage 2 complex data | 60.2 | 55.2 | 78.9 | 7.6 |
| Add Stages 1 and 2 | **61.8** | **56.7** | **81.7** | **8.3** |

Complex-task data caused the largest improvement. Stage 1 alone produced only small gains, but combining it with Stage 2 improved all four results over Stage 2 alone. The authors found that training only on complex tasks could leave basic operational errors; simple-task training mitigated those errors.

### 4.6 Training-strategy ablation

| Strategy | AutoWebBench | Mind2Web | MiniWoB++ | WebArena |
|---|---:|---:|---:|---:|
| SFT | 61.8 | 56.7 | 81.7 | 8.3 |
| SFT + DPO | 62.7 | 59.5 | 80.8 | 8.5 |
| SFT + DPO + environment-specific RFT | — | — | 89.3 | 18.2 |
| Final AutoWebGLM values | 62.7 | 59.5 | 89.3 | 18.2 |

DPO improved AutoWebBench by 0.9 points, Mind2Web by 2.8, and WebArena by 0.2, but MiniWoB++ declined from 81.7 to 80.8 before RFT. Environment-specific RFT then increased MiniWoB++ to 89.3 and WebArena to 18.2. The authors interpret RFT as practice-driven domain specialization.

### 4.7 Execution efficiency

Table 5 reports average timing by action type; the paper does not explicitly state the time unit.

| Action | Count/trace | Fetch | Parse | Predict | Execute | Loading |
|---|---:|---:|---:|---:|---:|---:|
| `type_string` | 1.00 | 362.00 | 28.88 | 2282.99 | 6.12 | 2082.61 |
| `click` | 3.62 | 438.62 | 72.07 | 2252.10 | 28.10 | 2094.60 |
| `finish` | 0.38 | 419.33 | 66.00 | 3054.16 | 6.00 | 2119.06 |
| `scroll_page` | 0.38 | 475.33 | 88.67 | 3396.37 | 5.33 | 2033.35 |
| Other actions | 0.25 | 680.50 | 152.50 | 2666.08 | 10.00 | 2142.92 |
| **Average** | — | **436.93** | **68.68** | **2407.34** | **20.36** | **2092.13** |

The time distribution was:

- Fetch: **8.70%**
- Parse: **1.37%**
- Model prediction: **47.89%**
- Action execution: **0.41%**
- Page loading: **41.64%**

Prediction and page loading therefore accounted for nearly all execution time, while parsing and executing the selected browser action were relatively inexpensive.

### 4.8 Error analysis

The authors tested everyday, leisure, and academic-research tasks and report satisfactory behavior in most scenarios. Observed failures were distributed as follows:

- **Hallucinations: 44%**
- **Poor graphical recognition: 28%**
- **Misinterpretation of task context: 20%**
- **Pop-up interruptions: 8%**

Hallucination was thus the largest remaining error source, followed by difficulty interpreting graphical content.

### 4.9 Supplied figures

- **Figure 1:** A radar chart compares GPT-3.5-Turbo, GPT-4, LLaMA2-70B, AutoWebGLM, and humans across WebArena, English AutoWebBench, three Mind2Web splits, and MiniWoB++. It visually shows AutoWebGLM covering a larger performance area than GPT-4 and the open baseline, while humans remain strongest on much of the chart. Exact model values are more reliably supplied by Tables 2–4; some axis annotations in the image are reference values rather than a complete numerical table.
- **Figure 2:** Four Chrome-extension examples show the agent completing practical tasks: finding a detailed daily weather report, selecting a children’s Christmas gift, finding an article about large language models, and finding a differential-equation-solving tool. Each screenshot pairs the live webpage with a side panel containing the user task and a multi-step action trace.
- **Figures 3–6:** These document the architecture, two-stage data-construction pipeline, dataset mixture, and three-stage training process described above.

No statistical significance tests, confidence intervals, or standard deviations are reported.

## 5. Analysis and Interpretation

The results support the paper’s central claim that a carefully trained 6B model can outperform much larger general-purpose models on web navigation and can approach or exceed specialized web agents.

The authors attribute the performance to several complementary elements:

- **HTML pruning** lowers the burden of long, noisy HTML while retaining actionable structure and context.
- **Current-position and history information** help the model understand spatial context and avoid repeating unsuccessful operations.
- **Curriculum learning** supplies fundamental page-reading and operation skills before requiring complex planning.
- **Complex task traces** align training with real multi-step use cases and are the largest source of gains in the data ablation.
- **Simple task data** remain necessary because complex data alone can leave errors in elementary browser operations.
- **DPO-based self-sampling** exposes the model to its own plausible mistakes and teaches it to prefer correct operations.
- **RFT self-play** allows strong specialization when the environment can identify successful trajectories.

The bilingual AutoWebBench results indicate that the model’s gains are not confined to one language. Its relatively small decline from familiar to excluded websites suggests some capacity to generalize across website styles, although the cross-domain scores remain below the corresponding cross-task scores.

The strongest evidence for domain practice is the RFT ablation: WebArena nearly doubled from 8.5 to 18.2, while MiniWoB++ rose from 80.8 to 89.3. However, this specialization depends on sandbox reward signals and environment-specific successful traces.

The efficiency results show that model inference and waiting for webpages dominate latency. Improving HTML parsing or browser action execution alone would have comparatively limited impact.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- **AutoWebGLM:** an open web-navigation agent based on a single 6B ChatGLM3 model.
- **A unified interaction framework:** simplified HTML, OCR support, spatial page position, action history, and a ten-operation browser action space.
- **An HTML-pruning method:** it retains essential actionable elements and limited contextual relatives while removing irrelevant structure.
- **A hybrid human–AI construction pipeline:** approximately 10,000 real browsing traces, combining rule-based executable actions, LLM-generated tasks and intentions, and manually recorded complex trajectories.
- **A three-stage training strategy:** curriculum SFT, self-sampling DPO with an added SFT stabilizer, and environment-specific rejection sampling finetuning.
- **AutoWebBench:** a human-verified bilingual benchmark covering English and Chinese and both familiar and unseen websites.
- **Strong compact-model results:** 64.8–65.4 on AutoWebBench’s cross-task splits, 58.6–61.8 cross-domain, 59.5 average on Mind2Web, 89.3 on MiniWoB++, and 18.2 on WebArena.
- **Released resources:** the paper states that its code, model, and data are publicly released.

## 7. Limitations and Caveats

- **Incomplete visual understanding:** HTML works well for conventional pages, but the system struggles with maps, animation, video, images, icons, and special effects.
- **Graphical recognition errors:** These constitute 28% of analyzed errors.
- **Persistent hallucination:** Hallucination is the largest failure category at 44%, despite DPO training.
- **Context errors and interruptions:** Task-context misinterpretation accounts for 20% of errors and pop-ups for 8%.
- **Unfamiliar operating logic:** Success and efficiency can decline on websites whose structure or interaction rules differ from training experience.
- **Real-web instability:** Network problems and other environmental instability can cause a predicted operation to fail or produce an unexpected state.
- **RFT is environment-dependent:** It requires reliable reward signals and was performed in MiniWoB++ and WebArena sandboxes rather than unrestricted live websites.
- **Human effort remains substantial:** Twenty annotators worked for a month; complex trajectories could not be generated reliably by advanced LLMs alone.
- **Domain specialization versus generality:** The largest RFT improvements come from separate environment-specific finetuning.
- **Uneven task performance:** MiniWoB++ performance was excellent overall but ranged from 0.00 on `enter-time` to 1.00 on many tasks.
- **Latency:** Prediction consumes 47.89% and webpage loading 41.64% of execution time.
- **Evaluation reporting:** The paper gives success rates but no variability estimates or significance tests.
- **Benchmark size:** AutoWebBench uses 50 traces in each split, although all were manually verified.
- **Figure limitation:** The radar chart does not provide a complete readable numerical breakdown for every displayed curve; the tables are the authoritative source for exact benchmark values.

## 8. Future Work or Open Questions

The authors identify three main directions.

### Multimodal input

Future systems should jointly use HTML and screenshots. HTML is strong for text and numerals, while images are necessary for icons, pictures, maps, animation, video, and visual effects. Combining both could preserve precise textual understanding while adding graphical awareness.

### Better reasoning and self-checking

The authors propose reasoning methods beyond conventional chain-of-thought, particularly methods that use previous browsing experience to make better decisions on unfamiliar sites. They also recommend explicit self-checking, such as:

- confirming the current state,
- checking whether an action had its intended effect, and
- reacting to network or environmental failures.

These mechanisms could improve both success rate and robustness.

### Mobile applications

Mobile-device automation is another proposed setting. Smaller screens show fewer elements and may simplify the page XML, and mobile interaction logic can be more straightforward. However, mobile agents must support gestures and operate under stronger system-security restrictions.

Other unresolved questions evident from the study include how to reduce hallucinations further, obtain scalable reliable complex-task traces with less human labor, improve the two largest latency sources, and retain environment-specific gains without sacrificing general web performance.

## 9. High-Level Takeaway (Plain Language)

AutoWebGLM is a 6-billion-parameter AI agent trained to read simplified webpages and operate a browser step by step. Its training begins with basic page understanding, advances to complex tasks, teaches the model from its own mistakes, and finally lets it practice successful actions in simulated websites. Despite being much smaller than several competing systems, it substantially outperformed GPT-4 on the paper’s bilingual benchmark and achieved the best reported MiniWoB++ and WebArena scores. It is not fully reliable—especially with images, unusual sites, hallucinations, and unstable webpages—but the study shows that compact models can become capable web agents when they receive executable data, explicit browser context, error-based training, and environment-specific practice.