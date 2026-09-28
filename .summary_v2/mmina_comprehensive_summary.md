# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible range | Pages 1–16; all pages have page-labeled native/extracted text |
| Apparently missing pages | None |
| Visually rendered pages | 1, 2, 3, 4, 5, 7, 8, 10, 12, 13, 14 |
| Pages not visually rendered | 6, 9, 11, 15, 16; their text is available, but their typography and any unflagged visual details were not independently inspected |
| Figures | Figures 1–5 are visually available and readable, although exact values in Figures 3 and 5 are not labeled |
| Tables | Tables 1–3 and A1–A3 are available as text; all are also visually rendered except none omitted among the identified table pages |
| Equations | The partially observable Markov decision process formulation is readable in §3.1. The prediction equation and Equation (1) are available in extracted text; Equation (1) is on an unrendered page and is OCR-sensitive |
| Algorithms/pseudocode | None presented as a formal algorithm |
| Appendices | Appendices A–C are included on pp. 12–16 |
| Supplementary material | Appendix A is called “Experiment Details” and contains “Supplementary Results,” but no separate supplementary file was supplied |
| Embedded artifacts | No embedded files; the code/data repository mentioned by the authors was not supplied |
| OCR requirement | No page required OCR, but mathematical notation and the icon-based “Inputs” column of Table 2 require caution |
| Other limitation | Several conclusions refer to action trajectories, but the underlying trajectory records are not included in the supplied paper |

The paper is an empirical machine-learning/artificial-intelligence benchmark and dataset paper, with a web-agent environment, evaluation protocol, baseline experiments, diagnostic analyses, and a memory-augmentation ablation.

# 1. Plain-Language Orientation

MMInA—“Benchmarking Multihop Multimodal Internet Agents”—tests whether an artificial-intelligence agent can complete realistic web tasks that involve both multiple websites and multiple kinds of information, especially text and images.

A conventional web benchmark may ask an agent to perform one operation on one fixed website. MMInA instead poses compositional tasks such as:

1. identify a destination from clues on Wikipedia;
2. search for a flight;
3. arrange a hotel;
4. find relevant YouTube videos.

Each website-specific subtask is a **hop**. The benchmark contains 1,050 human-written tasks, covers 14 website categories, allows tasks as long as 10 hops, and reports an average of 2.85 hops and 12.9 browser actions per task (pp. 1–4, Fig. 1, Table 1).

The central finding is that tested agents were far worse than humans, particularly as tasks became longer. In Table 2, the best reported overall agent task-success rate is GPT-4V’s 21.77%, versus 96.25% for humans. The authors’ hop-level analysis shows that failure can occur at the first or second hop even when later hops are never reached. This motivates their **holistic evaluation**, which reports both overall task completion and partial, hop-by-hop progress.

The paper also proposes a lightweight memory method: insert action trajectories from similar previous tasks into the agent’s prompt. Figure 5 and Appendix A.3 indicate that a small history—typically two previous tasks—works best, while longer histories can add distracting context.

The principal contribution is therefore not a new foundation model. It is a benchmark and evaluation framework designed to expose the combined difficulty of multimodal interpretation, long-horizon planning, cross-website navigation, and memory.

# 2. Document Roadmap

| Pages | Original section | Role |
|---|---|---|
| 1–3 | Abstract and §1 Introduction | Defines the problem, gaps, contributions, and headline results |
| 3 | §2 Related Works | Positions MMInA against tool-use, general-agent, and web-agent benchmarks |
| 3–5 | §3 MMInA Benchmark | Defines the environment, dataset construction, multimodal content, multihop browsing, and evaluation |
| 6–8 | §4 Experiments | Introduces baselines, main results, failure analysis, and memory augmentation |
| 8–9 | §5 Conclusion, Challenges, and Outlook | Restates contributions and proposes action-focused evaluation |
| 9 | §6 Limitations; §7 Ethical Considerations | Gives a website-access limitation and a warning about model bias |
| 9–11 | References | Bibliographic material; compressed here |
| 12–13 | Appendix A: Experiment Details | Reports implementation settings, resources, extended hop analysis, and memory ablation |
| 12–14 | Appendix B: MMInA Benchmark Details | Adds annotation details, task composition, websites, and comparison with VisualWebArena |
| 13–16 | Appendix C: More Related Works | Expands the literature discussion on datasets, model backbones, and web/mobile agents |

# 3. Background and Context

A **web agent** is a program that receives a user goal, observes browser content, and chooses actions such as clicking, typing, scrolling, or returning an answer.

A **large language model (LLM)** primarily processes text. A **large multimodal model (LMM)** processes more than one modality, here principally text and images.

A task is **single-hop** when it can be completed on one website. A **multihop** task contains multiple website-specific subtasks that must be completed in sequence. MMInA treats each such subtask as a hop (§3.1, p. 3).

**Multimodal** means that success requires both visual and textual information. The authors’ example asks which of two chairs looks furrier; product names and descriptions are textual, while the relevant appearance is visual (§3.3, p. 5).

An **accessibility tree** is a structured textual representation of webpage elements. In MMInA, each node has an element identifier, element type, and text. When a node is an image, the environment downloads the image and overlays the element identifier so that the agent can connect the image to the corresponding webpage element (§3.1, pp. 3–4).

A **partially observable Markov decision process (POMDP)** is used as the formal environment model. The agent cannot receive the entire Internet state, so it sees only a partial observation comprising the task, current accessibility tree, linked images, and action/state history (§3.1, p. 3).

**Procedural memory** means retained knowledge of how to perform a sequence of actions. The proposed augmentation replays trajectories from completed, similar tasks so the current agent can reuse successful procedures (§4.4 and Fig. 4, p. 8).

# 4. Research Problem and Gap

## Existing problem

Useful Internet agents must interpret user goals, locate information, navigate websites, execute actions, and preserve intermediate state across a long task. Real tasks frequently cross website boundaries and rely on both page text and visual cues (§1, pp. 1–2).

## Shortcomings attributed to previous approaches

According to the authors:

- Many benchmarks focus on textual input and therefore do not adequately test image-dependent behavior (§1, pp. 1–2).
- Existing web benchmarks commonly use one website or short tasks rather than long, compositional workflows (§2, p. 3; Table 1, p. 4).
- Static or simplified websites do not reproduce the changing content and interaction conditions of real sites (Table 1).
- Whole-task success alone becomes nearly uninformative when almost every long task fails; it does not reveal how far an agent progressed (§1, pp. 2–3; §3.5, p. 5).
- Agents have difficulty retaining past actions, recognizing hop termination, and managing a large search space (§4.3, pp. 7–8).

## Research gap

The authors identify the absence of a benchmark that jointly evaluates:

- multimodal interpretation;
- ordered, cross-website task composition;
- open-ended browser interaction;
- evolving real-world websites;
- both hop-level and task-level progress.

## Motivation

These properties are presented as necessary for evaluating whether an Internet agent is useful for natural, high-level user requests rather than isolated interface operations (§1).

## Scope

MMInA evaluates browser tasks across 14 listed website categories. Its primary domains are travel, shopping, search, booking, food, recipes, events, social media, and video (§3.2; Fig. 2; Table A2). The paper assesses inference-time behavior; it does not train a new general-purpose web-agent model.

# 5. Research Questions / Objectives / Hypotheses

## Explicit research questions

The abstract asks one explicit broad question:

- **RQ1:** Can autonomous agents move among multimodal websites to complete complex user tasks? (p. 1)

## Stated objectives

- Construct a realistic benchmark for multihop, multimodal Internet tasks.
- Evaluate contemporary LLM-, LMM-, and heuristic-based agents.
- measure partial progress through hop success as well as complete task success.
- Analyze why longer tasks fail.
- Test whether replaying previous action trajectories improves performance.

## Hypotheses

No formal hypothesis list or statistical null/alternative hypotheses is supplied.

The closest stated expectation appears in §4.3: after semantically aligning first hops, the authors reason that the success of a particular hop “should be independent” of the task’s total hop count when the domain remains fixed. Table 3 contradicts this expectation: first-hop performance generally deteriorates in longer tasks. This is an analytical assumption, not a preregistered hypothesis.

# 6. Assumptions / Threat Model

A cybersecurity threat model is not applicable.

The relevant system and environmental assumptions are:

- Web browsing is represented as a POMDP \(\langle S,A,P,R\rangle\) (§3.1).
- The agent sees only partial observations, not the complete Internet state.
- A hop corresponds to a subtask on a particular website.
- Hops must be completed in order; the agent may advance only after completing the current hop (§3.5).
- Complete task success requires every hop to succeed sequentially.
- The environment exposes 12 summarized browser-action types through Playwright (§3.1). The complete enumerated list is not supplied.
- Correct completion is judged using essential keywords, semantic answer comparison, or arrival at desired URLs/states (§3.5).
- Annotators construct shortest successful paths while agents may explore additional sites (§3.2; Appendix B.1.2).
- Real websites can change; the evaluation is designed partly around states and URLs that remain recognizable despite changing content.
- The benchmark assumes that downloaded in-view images plus the accessibility tree adequately expose the relevant multimodal webpage information.
- The memory experiment assumes trajectories from the last \(K\) tasks can provide useful procedural analogies to the current task (Appendix A.3).

# 7. Methodology

## Study design

This is a benchmark-construction and comparative baseline study. The authors:

1. create 1,050 tasks;
2. implement a browser environment over 14 websites;
3. define hop- and task-level evaluation;
4. run multiple text, caption-augmented, and multimodal agents;
5. compare them with human test takers;
6. analyze performance by task length and hop position;
7. test history-based procedural memory.

## Environment

At time \(t\), the agent receives a partial observation \(o_t\in\Omega\), including the task description, accessibility-tree content, linked images, and action/state histories. It selects action \(a_t\in A\), which can be a browser operation or a textual answer (§3.1, p. 3).

The browser is simulated through Playwright on an X graphics server. The viewport is \(1280\times2048\) (§3.1; Appendix A.1, p. 12).

## Action and observation processing

The authors condense possible browser operations into 12 action categories, including clicks, keyboard input, and scrolling. They do not enumerate all 12 in the supplied paper.

The primary textual webpage representation is the accessibility tree. Images in the current view are downloaded and annotated with their corresponding element IDs (§3.1).

## Dataset construction

The question style was adapted from WebQA. GPT-4V generated related multimodal questions, and annotators manually added tasks to diversify wording, scope, and domain (§3.2).

Each agent prompt contains:

1. instructions;
2. rules, such as stopping after `[stop]`;
3. small question-answer examples;
4. the universe of available reference websites;
5. the current task.

Three trained, web-proficient human annotators created the dataset. They varied in age and gender, labeled separate portions, cross-validated diversity and answer accuracy, and recorded the shortest path containing all crucial nodes (§3.2; Appendix B.1.1–B.1.2).

Each template generated 2–10 tasks. The dataset contains 1,050 tasks, including 108 question-answer pairs filtered from WebQA (Appendix B.1.3).

## Website coverage

Table A2 lists:

- Kiwix-hosted Wikipedia;
- Trip.com car rental;
- Momondo flights;
- Trip.com hotels;
- Eventbrite;
- Twitter;
- Amazon;
- YouTube;
- Time Out;
- XE;
- Nomadic Matt;
- Allrecipes;
- Trip.com trains;
- offline OneStopMarket shopping.

The authors describe all except Shopping as evolving real-world sites. Wikipedia is accessed through a Kiwix library snapshot/path and is footnoted as potentially changing with library updates (Table A2).

## Evaluation

### Single-hop

- **must_include:** PASS only when all required keywords appear.
- **fuzzy_match:** GPT-3.5-Turbo receives the prediction and reference answer and returns “Yes” or “No” to decide PASS/FAIL (§3.5).

### Multihop

An \(N\)-hop task maintains \(N\) completion conditions plus an `END` marker, giving a queue length of \(N+1\). A hop passes when its required information or target state is reached. The next hop is locked until the current one passes (§3.5).

### Metrics

- **Hop success rate:** percentage of successful visits/completed website subtasks.
- **Task success rate:** percentage of full tasks completed.
- Both are reported for 1-hop, 2–4-hop, 5+-hop, and overall task groupings (Table 2).

The paper reports no confidence intervals, significance tests, variance estimates, or repeated-run analysis.

## Baselines

The tested systems include:

- text-model backbones: Fuyu-8B, CodeLLaMA-7B, DeepSeek-R1-Distill-Qwen-32B, Gemini-Pro, and GPT-4;
- heuristic/web-trained agents: WebShop and CogAgent-9B;
- multimodal models: Fuyu-8B, Gemini-Pro-Vision, GPT-4V, GPT-4o;
- human baseline: an average of three test takers.

Text models were evaluated with text alone and, for a second condition, with BLIP-2-generated image captions. Multimodal models received text and images. Some rows also include execution history. The exact icon mapping is partly corrupted in extracted text, although the Table 2 caption defines the intended input categories.

## Versions and computing resources

Appendix A.1 reports:

- GPT-4: `gpt-4-0125-preview`;
- GPT-4o: `gpt-4o-2024-11-20`;
- GPT-4V: `gpt-4-vision-preview`;
- Gemini-Pro: `gemini-1.0-pro-001`;
- Gemini-Pro-Vision: `gemini-1.0-pro-vision-001`.

Local pretrained baselines used one NVIDIA RTX6000 Ada GPU with 48 GB memory. Most had 7B, 8B, or 9B parameters. One full inference epoch required 4–8 hours, depending on model performance (Appendix A.2).

The authors say they used default model/API parameters. Random seeds, temperatures, exact decoding settings, software versions, number of repeated runs, and monetary/API cost are not specified.

## Memory augmentation

The agent prompt is augmented with task descriptions, webpage observations, action sequences, and outcomes from the last \(K\) tasks. The purpose is to narrow the search space through analogous experience. The added history multiplies prompt length by approximately \(K\), creating a context-cost tradeoff (Appendix A.3).

# 8. Experiments / Analyses

## X1 — Main benchmark comparison

**Purpose:** Compare language, multimodal, web-trained, and human agents.

**Data:** The MMInA task set of 1,050 tasks.

**Conditions:** Text-only, caption-augmented, native multimodal, and selected history-augmented inputs.

**Metrics:** Hop and task success rates across 1, 2–4, and 5+ hops.

**Result:** Every tested agent is substantially below the human baseline. The highest overall agent task-success value in Table 2 is GPT-4V at 21.77%; humans achieve 96.25%.

**Caveat:** The paper does not report uncertainty or repeated trials, so differences between nearby model values cannot be treated as statistically established.

## X2 — Modality/input comparison

**Purpose:** Test whether access to visual information helps.

Examples from Table 2:

- Fuyu-8B: 0% overall task success as text-only versus 13.39% as a multimodal system.
- GPT-4: 9.34% text-only versus 19.85% with caption augmentation.
- Gemini-Pro: 9.54% text-only versus 15.22% with captions.

However, caption augmentation does not improve every subgroup. For 2–4-hop hop success:

- Gemini-Pro falls from 34.12% without captions to 11.09% with captions.
- GPT-4 falls from 30.56% to 20.70%.

The authors attribute such counterintuitive cases to under-informed agents wandering through hops, looping, and losing the original task intent (§4.2).

## X3 — Performance by task length

Across most models, success declines sharply for 5+-hop tasks. Examples:

- GPT-4V task success: 42.91% at 1 hop, 3.03% at 2–4 hops, and 0% at 5+ hops.
- Gemini-Pro-Vision with history: 39.17%, 10.61%, and 1.13%.
- Humans: 99.02%, 95.34%, and 88.12%.

Thus longer tasks hurt humans modestly but agents severely (Table 2).

## X4 — Hop-position analysis

Table 3 compares GPT-4V and Gemini-Pro-Vision on tasks of total length 2–6.

For GPT-4V:

- first-hop success is 56.50% on 2-hop tasks;
- 22.73% on 3-hop;
- 12.50% on 4-hop;
- 12.28% on 5-hop;
- 16.67% on 6-hop.

For Gemini-Pro-Vision:

- 69.28%, 32.56%, 40.00%, 41.67%, and 31.03%, respectively.

Second-hop success is already low; almost every later-hop entry is zero. The authors infer that longer prompts enlarge the search space and expose weak zero-shot long-context reasoning (§4.3).

## X5 — Extended GPT-4V hop analysis

Table A1 extends GPT-4V analysis to total lengths 2–10 and supplies task counts:

- 2 hops: 200 tasks;
- 3: 44;
- 4: 16;
- 5: 57;
- 6: 60;
- 7: 59;
- 8: 35;
- 9: 30;
- 10: 19.

The first-hop trend is not monotonic: it rises again to 40.00% for 8-hop, 56.67% for 9-hop, and 52.63% for 10-hop tasks. The authors explicitly warn that the smaller number of tasks beyond seven hops causes random fluctuation (Appendix A.3).

## X6 — Procedural-memory ablation

**Purpose:** Determine how many past trajectories should be included.

**Manipulated variable:** History length \(K=0,1,2,3,4,5\).

**Model:** Gemini-Pro-Vision, according to Appendix A.3.

**Result:** Figure 5 visually shows that \(K=2\) produces the highest Hop 1 and overall performance. History also improves the other task-length groupings relative to \(K=0\), but performance declines with larger histories.

**Author interpretation:** Small histories narrow the search space; large histories lengthen prompts and introduce bias or distraction. For simpler shopping or Wikipedia tasks, \(K=1\) or \(2\) is preferable.

**Caveat:** Figure 5 lacks exact bar labels, and no uncertainty estimates are supplied.

# 9. Results

## R1 — The benchmark is far harder for agents than for humans

The best overall agent task-success result is 21.77% for GPT-4V, versus 96.25% for humans (Table 2).

**Analyst-derived:** The absolute difference is:

\[
96.25-21.77=74.48\text{ percentage points}.
\]

This is a percentage-point gap, not a 74.48% relative reduction.

## R2 — Full-task success collapses with task length

GPT-4V drops from 42.91% task success on 1-hop tasks to 3.03% on 2–4-hop tasks and 0% on 5+-hop tasks. Its hop success also falls from 42.91% to 21.23% to 3.99% (Table 2).

Gemini-Pro-Vision with history is the strongest reported 2–4-hop task performer at 10.61% and ties the other Gemini-Pro-Vision condition at 1.13% on 5+ tasks.

## R3 — Hop success and task success reveal different behavior

GPT-4 text-only has a 30.56% hop-success rate on 2–4-hop tasks but only 9.09% task success. Gemini-Pro text-only has 34.12% hop success but only 0.76% task success in the same grouping (Table 2).

This supports the authors’ claim that an agent can finish some subtasks while rarely completing the whole sequence.

## R4 — Native multimodal access helps, but does not solve long-horizon control

GPT-4V achieves 21.77% overall task success, higher than the textual GPT-4 result of 9.34% and caption-augmented GPT-4 result of 19.85%. Still, GPT-4V records 0% full-task success on 5+-hop tasks (Table 2).

Because these are different model/input configurations rather than a fully controlled modality-only ablation, causal attribution to modality alone should be cautious.

## R5 — Reasoning strength on one hop does not transfer cleanly to long tasks

Caption-augmented DeepSeek-R1-Distill-Qwen-32B obtains the best agent 1-hop task success in Table 2, 47.68%, but 0% on both 2–4-hop and 5+-hop full tasks. Its corresponding hop success is 3.84% and 4.68%, showing some partial progress but no complete multihop success.

## R6 — Agents fail earlier when the containing task is longer

Table 3 shows lower first-hop success in longer tasks even though the compared event is still “the first hop.” This is strongest from 2-hop to 3-hop tasks:

- GPT-4V: 56.50% to 22.73%;
- Gemini-Pro-Vision: 69.28% to 32.56%.

The trend is not strictly monotonic, especially in Table A1’s sparsely populated 8–10-hop groups.

## R7 — Small procedural histories help more than large histories

Figure 5 visually indicates the strongest performance at history length \(K=2\), followed by degradation as more trajectories are appended. Appendix A.3 supplies the authors’ explanation: longer histories produce diminishing returns and can disturb decision-making.

## R8 — Humans also decline with length, but remain highly successful

Human task success is 99.02% for one hop, 95.34% for 2–4 hops, and 88.12% for 5+ hops (Table 2). This demonstrates that the tasks are executable rather than universally impossible, while also showing that longer tasks impose some difficulty even on people.

# 10. Figure-by-Figure Interpretation

### Figure 1 — Example four-hop MMInA task

- **Purpose:** Demonstrates a full compositional workflow.
- **Content:** A user asks which of Seoul or Tianjin has a Ferris wheel near the city center, then requests a round-trip flight, hotel accommodation, and YouTube tours.
- **Panels/sequence:** Four horizontal hop blocks connected by arrows:
  1. Wikipedia information seeking;
  2. Momondo flight booking;
  3. Trip.com hotel arrangement;
  4. YouTube video search.
- **Visual encoding:** Browser screenshots represent pre/post states; green check marks mark successful hop completion; orange denotes information seeking and purple denotes action.
- **Axes/units:** None.
- **Conclusion supported:** A natural request combines question answering and browser actions across several sites, and evaluation can occur after each component.
- **Caveat:** Screenshots illustrate one task; they do not establish aggregate performance.

### Figure 2a — Source websites of the benchmark hops

- **Plot:** Pie chart.
- **Unit:** Percentage of source-site hops.
- **Caption denominator:** 2,991 hops.
- **Visually readable shares:** Wikipedia 28.4%, shopping 13.0%, flights 10.5%, hotels 10.3%, car rental 9.2%, Twitter 7.1%, YouTube 6.0%, food 5.7%, tour guide 5.6%, transfer 2.9%, events 0.9%, trains 0.2%, Amazon 0.2%, recipes 0.1%.
- **Main observation:** Wikipedia is the largest source, followed by shopping; travel-related categories collectively occupy much of the distribution.
- **Caveat:** §3.2 reports 2,989 hops, creating a text–figure discrepancy of two hops.

### Figure 2b — Hop intent types

- **Plot:** Pie chart.
- **Values:** Action 64.7%; information seeking 35.3%.
- **Meaning:** Nearly two-thirds of hops require performing an action rather than only retrieving information.
- **Encoding:** Purple for action, peach for information seeking.

### Figure 2c — Counts of multihop tasks

- **Plot:** Bar chart.
- **X-axis:** Task hop count, 2–10.
- **Y-axis:** Number of activities/tasks; ticks run approximately 0–200.
- **Observation:** Two-hop tasks are by far the most common. Counts for longer tasks are smaller and uneven.
- **Cross-reference:** Exact 2–10-hop counts for the GPT-4V multihop analysis appear in Table A1, but Figure 2c’s plotted universe and label should not automatically be assumed identical without an explicit statement.

### Figure 3 — Average actions by hop count

- **Plot:** Bar chart.
- **X-axis:** Hops, 1–10.
- **Y-axis:** Average actions, approximately 0–30+.
- **Trend:** Average action count generally rises with hop count.
- **Exception:** The five-hop bar is lower than the four-hop bar. Appendix B.1.3 explains that four-hop tasks often include comparison operations, while the dataset’s page-crossing definition prevents these comparisons from being counted as an additional hop.
- **Exactness:** Bar heights are approximate visual estimates because values are not printed.
- **Potential ambiguity:** Figure 2c’s extracted axis says “# Avg. Actions,” although its caption says task counts; Figure 3 is explicitly the average-action plot.

### Figure 4 — Memory-augmented agent architecture

- **Type:** Conceptual architecture diagram.
- **Components:** Multimodal agent at the center; semantic, episodic, and procedural memory around it.
- **Inputs:** General world/Internet-navigation knowledge, current and past action trajectories, and completed-task histories.
- **Flow:**
  - semantic memory exchanges knowledge with the agent;
  - episodic memory contains active action trajectories;
  - completed trajectories are “memorized” into procedural memory;
  - procedural histories are “retrieved” back into the agent.
- **Outcome symbols:** The procedural-memory block shows stored histories with successful and failed outcomes.
- **Conclusion:** The proposed intervention concerns reusable action procedures, not merely static factual knowledge.

### Figure 5 — Memory performance by history length

- **Plot:** Grouped bars.
- **X-axis:** Hop 1, Hop 2–4, Hop 5+, Overall.
- **Y-axis:** Performance, approximately 0–40.
- **Legend:** History lengths 0–5, shown in a blue-to-magenta sequence.
- **Main observation:** History length 2 is visually highest for Hop 1 and Overall. Performance declines for longer histories; the relationship is non-linear.
- **Approximate visual estimates:** Hop 1 appears roughly mid-20s at \(K=0\), near 40 at \(K=2\), and around 20 at \(K=5\). Overall appears roughly 11–12 at \(K=0\), around 18–19 at \(K=2\), and around 11–12 at \(K=5\).
- **Uncertainty:** These estimates are graphical readings, not reported exact values. No error bars are shown.

# 11. Table-by-Table Interpretation

### Table 1 — MMInA versus related benchmarks

The table compares multimodality, maximum/average hops, website type, interaction style, and number of websites.

Key MMInA values:

- multimodal: yes;
- maximum/average hops: 10/2.85;
- evolving real-world websites;
- open-ended dynamic interaction;
- 14 websites.

WebVoyager is the nearest listed comparator on average hop length, at 4/2.40, with 15 dynamic real-world websites. Other listed benchmarks have average hop counts from 1.00 to 1.10, except WebVoyager.

MMInA does not lead every column: MiniWoB++ lists 100 sites and Mind2Web 131. Its claimed distinction is the joint combination of multimodality, long multihop tasks, evolving sites, and open-ended interaction.

### Table 2 — Main benchmark results

Rows are agent/configuration combinations. Columns report hop and task success percentages for 1 hop, 2–4 hops, 5+ hops, and overall.

Important maxima among agents:

- 1-hop task success: 47.68%, caption-augmented DeepSeek-R1-Distill-Qwen-32B;
- 2–4-hop task success: 10.61%, history-enabled Gemini-Pro-Vision;
- 5+-hop task success: 1.13%, both Gemini-Pro-Vision conditions;
- overall task success: 21.77%, GPT-4V;
- overall hop success: 14.36%, history-enabled GPT-4o, narrowly above history-enabled Gemini-Pro-Vision at 14.27%.

Human results exceed every agent result in every grouping.

No confidence intervals or statistical significance indicators appear. Zero denotes a measured zero; it is not a missing value. Input icons are explained in the caption, but extraction corruption prevents perfectly reliable row-by-row reconstruction of every icon combination.

### Table 3 — Success by hop position and total task length

Two panels cover GPT-4V and Gemini-Pro-Vision. Rows give total hop count (H.C.) from 2 to 6; columns give success at each hop position.

GPT-4V’s first-hop value declines from 56.50% on 2-hop tasks to about 12–17% on 4–6-hop tasks. Gemini-Pro-Vision begins higher, 69.28%, and remains between 31.03% and 41.67% for 3–6-hop tasks. Most third and later hops are 0%.

Dashes mean that the hop position does not exist for a task of that length, not missing experimental data.

### Table A1 — Extended GPT-4V hop analysis

This table extends the total-length range to 10 and reports group sizes. It confirms severe later-hop failure but complicates any simple monotonic narrative: first-hop success rises in the 8-, 9-, and 10-hop groups. The authors attribute this fluctuation to the smaller number of long tasks.

Only the 9-hop group records nonzero success through the third hop: 56.67%, 20.00%, and 3.33%. All reported fourth-and-later values are zero.

### Table A2 — Benchmark websites

The table maps 14 functional categories to specific URLs. Thirteen use external web properties or a Kiwix Wikipedia library; Shopping uses an offline OneStopMarket installation.

The caption says all sites except Shopping are evolving real-world sites. This should be read alongside the Kiwix footnote and §6’s statement that one site is offline and another open-source because direct image fetching is difficult. The paper does not unambiguously name which site it calls “open-source” in §6.

### Table A3 — VWA and MMInA example comparison

The VisualWebArena (VWA) example asks a question using Wikipedia in a specified tab. The MMInA example asks the agent to compare two chairs for armrests, requiring product-page images and text.

The table illustrates the authors’ positioning: MMInA requires multimodal reasoning at multiple steps. It is an example comparison rather than a controlled performance experiment.

# 12. Diagram / Architecture Interpretation

The substantive architecture is Figure 4.

The multimodal agent is the active decision-making component. Its behavior is supported by three memories:

1. **Semantic memory:** general world knowledge, generally encoded in model weights or external knowledge stores.
2. **Episodic memory:** recent step-by-step actions for the current task, represented through context or in-context examples.
3. **Procedural memory:** reusable completed-task sequences and outcomes.

A completed trajectory passes from episodic storage into procedural memory through a “memorize” operation. When the agent encounters a similar task, stored histories return through “retrieve.” Semantic memory supplies broad concepts, while procedural memory supplies an actionable pattern.

The implemented experiment operationalizes procedural memory by appending the last \(K\) task trajectories to the prompt. The paper does not describe a learned retrieval model, similarity metric, vector database, or memory-update algorithm. “Similar tasks” is part of the conceptual description, but the operational appendix describes the last \(K\) tasks.

# 13. Equations and Mathematical Concepts

## Environment formulation, §3.1

\[
\langle S,A,P,R\rangle
\]

This is the benchmark’s POMDP-like representation:

- \(S\): complete Internet, browser, and agent state;
- \(A\): action space;
- \(P\): state-transition mechanism;
- \(R\): reward/evaluation response;
- \(\Omega\): partial-observation space;
- \(o_t\in\Omega\): observation at time \(t\);
- \(a_t\in A\): chosen action at time \(t\).

The paper writes:

\[
P:S\times A\rightarrow S'
\]

meaning that a current state and action lead to a subsequent state. The Internet environment implicitly implements this transition rather than exposing an explicit matrix.

The reward is represented linguistically as PASS or FAIL for each hop. This is a binary evaluation signal, not a differentiable training loss.

## Multihop completion structure, §3.5

For an \(N\)-hop problem, the evaluator stores \(N\) hop-completion conditions plus `END`, so:

\[
\text{queue length}=N+1.
\]

Task success requires sequential satisfaction of all \(N\) conditions.

## Multimodal prediction equation, Appendix C, p. 14

\[
A=f(I,M;\theta)
\]

where:

- \(I\): instruction;
- \(M\): multimodal input;
- \(A\): predicted answer;
- \(\theta\): model parameters;
- \(f\): the model.

Plainly, the model uses an instruction and multimodal evidence to generate an answer.

## Equation (1), Appendix C, p. 15

The extracted equation is:

\[
\mathcal{L}(\theta)
=
-\sum_{i=1}^{N}
\log p(R_i\mid I,R_{<i};\theta).
\tag{1}
\]

This is an autoregressive negative log-likelihood objective:

- \(R_i\): the \(i\)-th response token;
- \(R_{<i}\): preceding response tokens;
- \(N\): response length;
- \(p(\cdot)\): model probability;
- \(\mathcal L\): training loss.

Minimizing the loss encourages high probability for the correct response tokens.

**Notation uncertainty:** The preceding prose defines multimodal input \(M\), but \(M\) is absent from the extracted conditioning expression in Equation (1). This may be an author-side omission or an extraction issue. Page 15 was not visually rendered, so it cannot be resolved from the supplied visual evidence.

# 14. Interpretation and Discussion

The benchmark’s main lesson is that cross-website task composition creates a qualitatively different problem from repeating independent single-site tasks. Every hop changes what the agent must remember, which site it should use, and what completion condition it should recognize. A mistake early in the sequence prevents access to all later steps.

The evidence answers RQ1 conditionally: the tested agents can complete some MMInA tasks, especially single-hop ones, but do not reliably complete complex multihop tasks. Humans achieve 96.25% overall task success, while the best agent achieves 21.77% (Table 2).

Hop-level evaluation answers a diagnostic question that task success alone cannot: did the agent make no progress, or did it complete several subtasks and then fail? The large gaps between hop and task success show why this distinction matters.

The authors explain longer-task failure through:

- enlarged search spaces caused by prompts listing multiple websites;
- switching to irrelevant alternatives after failure;
- repeated actions and loops;
- failure to recognize hop termination;
- insufficient memory for previous actions;
- weak long-context reasoning.

The evidence is consistent with this account, but the paper does not quantify the frequency of each failure category or present a formal trajectory-coding analysis. Therefore, the mechanisms are author interpretations based on inspected trajectories rather than separately measured causal variables.

The claim that multimodal models generally perform better is broadly supported, but configuration differences prevent a clean modality-only causal conclusion. The caption-augmentation results also show that adding textualized visual information may sometimes impair intermediate performance.

The procedural-memory result suggests a context-quality tradeoff: no history deprives the agent of useful examples, while too much history adds irrelevant material. The reported optimum \(K=2\) is empirical for the shown Gemini-Pro-Vision setting and is not established as universal.

## Consistency findings

- **Text–figure discrepancy:** Figure 2a refers to 2,991 hops; §3.2 says 2,989.
- **Prose–table rounding:** The introduction describes GPT-4V as 21.8% and humans as 96.3%; Table 2 gives 21.77% and 96.25%. These are consistent after rounding.
- **Trend qualification:** The prose says first-hop success declines with total length, but Table A1 rises again at 8–10 hops. Appendix A.3 acknowledges fluctuations from smaller long-task samples.
- **Memory cross-reference:** §4.4 says “see Table 2,” while the clearest history-length ablation is Figure 5 and Appendix A.3.
- **Equation notation:** Equation (1), as extracted, does not condition on \(M\), despite the preceding multimodal formulation.

# 15. Contributions and Novelty

## Dataset and benchmark contribution

- 1,050 human-written multimodal tasks.
- Tasks spanning up to 10 ordered hops.
- Fourteen website categories.
- Mixture of information-seeking and action-oriented subtasks.
- Real/evolving websites, with an offline shopping exception.

## Methodological contribution

- A hop-based decomposition of complex Internet tasks.
- Sequential completion conditions with per-hop PASS/FAIL.
- Joint reporting of hop success and complete task success.

## System/environment contribution

- Browser interaction through Playwright.
- Accessibility-tree representations linked to downloaded in-view images.
- Open-ended browser operations summarized into 12 action types.

## Experimental contribution

- Comparison of text, caption-augmented, multimodal, web-trained, and human agents.
- Breakdown by task length and hop position.
- Evidence that early-hop behavior depends on total task length.

## Algorithmic/practical contribution

- Lightweight prompt-based procedural memory using replayed trajectories.
- Empirical analysis of history length \(K\).

There is no new theorem, formal optimization algorithm for web navigation, or newly trained foundation model.

# 16. Limitations

## Authors’ stated limitations

Section 6 states that website protection mechanisms make direct image retrieval from HTML difficult. Consequently, one selected website is an offline standalone site and another is open-source (p. 9). This limits the otherwise broad claim that the benchmark operates entirely on live, evolving websites.

Section 7 also warns that biases in base multimodal models can produce inaccurate or unfair outputs and says users should consider training-data representativeness.

Appendix A.3 acknowledges that:

- long-range task groups contain fewer examples, making success rates fluctuate;
- memory multiplies input length by \(K\);
- larger histories can introduce bias and disturbance;
- the memory experiments were conducted with Gemini-Pro-Vision, although the method is intended to be model-agnostic.

## Additional evidence-based analyst observations

These are not presented as author admissions:

- No confidence intervals, repeated-run variance, significance tests, or random seeds are reported.
- Only three annotators and an average of three human test takers are used; detailed demographic distributions are absent.
- The exact task-count distribution over 1-hop versus multihop groups is not fully tabulated.
- Dataset totals disagree between 2,989 and 2,991 hops.
- Dynamic websites create reproducibility and benchmark-drift risks.
- LLM-based `fuzzy_match` evaluation may inherit evaluator-model inconsistency, but no validation statistics are provided.
- Keyword matching may reject semantically correct paraphrases or accept answers containing required words in the wrong relation.
- The 12-action space is not fully enumerated.
- Default model parameters are insufficient for exact reproduction.
- The memory evaluation appears to use one model and lacks exact numerical labels and error bars.
- The claim that all tasks require multimodal processing is illustrated but not accompanied by a modality-removal audit of every task.
- Underlying agent trajectories, annotation agreements, prompts, and code are referenced as externally available but are not contained in the supplied work.

# 17. Threats to Validity

## Internal validity

The benchmark compares different model families and input configurations, so performance differences cannot always be isolated to a single cause such as vision, context length, or reasoning architecture. Dynamic page changes may also alter difficulty between runs.

## Construct validity

Hop success based on URL/state or answer matching measures progress, but it may not capture whether an agent followed an efficient, safe, or semantically appropriate procedure. Conversely, sequential gating may classify a task as failed even if an agent obtains a valid final result through a different ordering.

## Statistical conclusion validity

No uncertainty measures or statistical tests are supplied. Nearby scores—for example 14.36% versus 14.27% overall hop success—should not be interpreted as reliable rankings.

## External and ecological validity

Live websites improve realism, but only 14 categories are included, and travel-related compositions are prominent. Results may not transfer to other languages, authenticated workflows, professional software, inaccessible pages, or websites with different defenses.

## Reproducibility

Reproduction is threatened by evolving content, API-model updates, incomplete decoding parameters, unspecified seeds, and unavailable underlying trajectories in the supplied document. Model version identifiers and hardware are helpful but insufficient by themselves.

## Annotation validity

Annotators were trained and cross-validation was performed, but inter-annotator agreement, rejection counts, and detailed quality-control outcomes are not reported.

# 18. Future Work and Open Questions

## A. Future work proposed by the authors

- Develop action-focused evaluation that directly guides agent operations (§5, pp. 8–9).
- Apply the model-agnostic memory approach to other LLMs and LMMs (§1; Appendix A.3).
- Expand website support through the flexible evaluation framework (Table 1 and Table A2 captions).

## B. Additional open questions

- How stable are scores when the same tasks are rerun after websites change?
- Which failure modes—visual misunderstanding, navigation, planning, memory, or termination—contribute most?
- Does memory still help when trajectories are retrieved by semantic similarity rather than simple recency?
- Does the optimum \(K=2\) generalize across models, domains, and context windows?
- How accurate are `must_include` and GPT-3.5-based `fuzzy_match` relative to human judgments?
- Can an evaluator recognize alternative valid workflows without weakening correctness?
- How much of multimodal performance comes from image understanding versus differences among model families?
- What are the safety and privacy implications of agents carrying out consequential live-web actions?
- Can the 2,989/2,991-hop discrepancy be reconciled from the released dataset?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| MMInA | The paper’s Multihop Multimodal Internet Agent benchmark |
| Agent | A system that observes a situation and chooses actions toward a goal |
| Web agent | An agent that reads and manipulates webpages |
| LLM | Large language model; principally text-oriented |
| LMM | Large multimodal model; processes text plus images or other modalities |
| Multimodal | Requiring multiple data forms, here images and text |
| Hop | One website-specific subtask |
| Multihop task | An ordered workflow containing multiple website subtasks |
| Compositional task | A high-level task formed by combining smaller dependent tasks |
| Accessibility tree | Structured text describing webpage elements and their roles |
| Open-ended action | A generated browser operation rather than a multiple-choice selection |
| POMDP | Partially observable Markov decision process |
| \(S\) | Complete environment state space |
| \(A\) | Action space; also used in Appendix C for predicted answer |
| \(P\) | State-transition mechanism |
| \(R\) | Reward in §3.1; response sequence in Appendix C |
| \(\Omega\) | Partial-observation space |
| \(o_t\) | Observation at time \(t\) |
| \(a_t\) | Action at time \(t\) |
| PASS/FAIL | Binary hop-evaluation outcomes |
| must_include | Evaluation requiring all predefined keywords |
| fuzzy_match | LLM-judged semantic answer comparison |
| Hop success rate | Percentage of targeted hop states successfully reached |
| Task success rate | Percentage of complete tasks successfully finished |
| Semantic memory | General factual/conceptual knowledge |
| Episodic memory | Record of steps in a current or recent task |
| Procedural memory | Reusable knowledge of action sequences |
| \(K\) | Number of past task histories added to the prompt |
| BLIP-2 | The caption generator used to convert images into text for caption-augmented conditions |
| VWA | VisualWebArena, a benchmark compared with MMInA |
| QA | Question-answer pair |
| GUI | Graphical user interface |
| API | Application programming interface |
| \(I,M,R\) | Instruction, multimodal input, and ground-truth response |
| \(\theta\) | Model parameters |
| \(\mathcal L\) | Training loss |
| EOS | End-of-sequence token |
| H.C. | Total hop count in Table 3 |
| SR | Success rate |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Tasks | 1,050 | tasks | Full benchmark | Author-reported | Abstract; §1; Appendix B.1.3 |
| Websites | 14 | websites/categories | MMInA | Author-reported | Table 1; Table A2 |
| Maximum task length | 10 | hops | MMInA | Author-reported | Fig. 1; Table 1 |
| Average task length | 2.85 | hops/task | MMInA | Author-reported | Fig. 1; Table 1 |
| Average actions | 12.9 | actions/task | MMInA | Author-reported | Fig. 1; §3.1 |
| Hop total | 2,991 | hops | Figure denominator | Visually readable | Fig. 2a |
| Hop total | 2,989 | hops | Dataset prose | Author-reported | §3.2 |
| Action-oriented hops | 64.7 | % | All hops | Visually readable | Fig. 2b |
| Information-seeking hops | 35.3 | % | All hops | Visually readable | Fig. 2b |
| Wikipedia share | 28.4 | % of hops | Largest website category | Visually readable | Fig. 2a |
| Annotators | 3 | people | Dataset construction | Author-reported | Appendix B.1.1 |
| Human test takers | Average of 3 | people | Baseline evaluation | Author-reported | §4.1 |
| WebQA-derived pairs | 108 | QA pairs | Included within dataset | Author-reported | Appendix B.1.3 |
| Best overall agent task success | 21.77 | % | GPT-4V | Author-reported | Table 2 |
| Human overall task success | 96.25 | % | Human baseline | Author-reported | Table 2 |
| Human–best-agent gap | 74.48 | percentage points | \(96.25-21.77\) | Analyst-derived | Table 2 |
| Best 1-hop agent task success | 47.68 | % | Caption-augmented DeepSeek-R1-Distill-Qwen-32B | Author-reported | Table 2 |
| Best 2–4-hop agent task success | 10.61 | % | History-enabled Gemini-Pro-Vision | Author-reported | Table 2 |
| Best 5+-hop agent task success | 1.13 | % | Gemini-Pro-Vision conditions | Author-reported | Table 2 |
| GPT-4V 5+-hop task success | 0 | % | Native multimodal | Author-reported | Table 2 |
| Human 5+-hop task success | 88.12 | % | Human baseline | Author-reported | Table 2 |
| GPT-4V first hop, 2-hop tasks | 56.50 | % | Hop-position analysis | Author-reported | Table 3/Table A1 |
| GPT-4V first hop, 5-hop tasks | 12.28 | % | Hop-position analysis | Author-reported | Table 3/Table A1 |
| Gemini-Pro-Vision first hop, 2-hop tasks | 69.28 | % | Hop-position analysis | Author-reported | Table 3 |
| Memory optimum | Typically \(K=2\) | prior tasks | Gemini-Pro-Vision experiment | Author-reported | Fig. 5; Appendix A.3 |
| Viewport | \(1280\times2048\) | pixels | Browser environment | Author-reported | Appendix A.1 |
| GPU | 1 RTX6000 Ada, 48 GB | GPU/memory | Local baselines | Author-reported | Appendix A.2 |
| Runtime | 4–8 | hours/epoch | Full MMInA inference | Author-reported | Appendix A.2 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| MMInA combines multimodal, multihop, real-web interaction | 1,050 tasks, 14 sites, maximum 10 hops, image/text processing | Fig. 1; Table 1; Table A2 | pp. 1–5, 14 | Strong descriptive support, though one site is offline |
| Current agents remain far below humans | 21.77% best-agent versus 96.25% human overall task success | X1; Table 2 | pp. 6–7 | Strong within reported benchmark; no uncertainty measures |
| Longer tasks cause severe performance degradation | Agent success drops from one hop to 2–4 and 5+ groups | X3; Table 2 | p. 7 | Strong descriptive pattern across most agents |
| Agents fail early in longer tasks | First-hop success depends on total task length; later hops mostly zero | X4/X5; Table 3/A1 | pp. 7–8, 12–13 | Supported, but the longest groups fluctuate |
| Task success alone hides partial progress | Hop success often exceeds full-task success substantially | Table 2 | pp. 6–7 | Strong direct evidence |
| Multimodal access generally improves performance | Multimodal/caption configurations often exceed text-only counterparts | X2; Table 2 | pp. 6–7 | Broadly supported; not a fully controlled causal comparison |
| Search-space growth and weak memory cause early failure | Authors’ trajectory inspection reports site-switching, looping, and missed termination | §4.3 | pp. 7–8 | Qualitative author analysis; frequencies are not quantified |
| Procedural memory improves performance | Figure 5 peaks around \(K=2\) | X6; Fig. 5; Appendix A.3 | pp. 8, 12 | Visually supported for Gemini-Pro-Vision; exact values/error bars absent |
| More memory is not always better | Performance declines after small \(K\); authors report bias/disturbance | Fig. 5; Appendix A.3 | pp. 8, 12 | Supported in one reported ablation |
| MMInA is more compositionally demanding than VWA | MMInA example requires multimodal comparison across multiple steps | Table A3 | p. 14 | Illustrative, not a comprehensive controlled comparison |

# 22. Very Simple Explanation

Imagine giving a computer this job: “Figure out which city matches my clue, find me a flight there, book a hotel, and show me travel videos.” The computer must read text, inspect pictures, use several websites, remember what it already learned, and know when each part is finished. MMInA is a test built around jobs like that.

The tested AI agents could often make some progress, but they usually broke down when the job had several connected parts. The best agent finished about 22 out of every 100 tasks, while people finished about 96. Longer tasks were especially difficult because an early mistake blocked everything that followed.

The paper’s useful idea is to score both the finished job and each smaller step. That tells researchers whether an agent failed immediately or almost reached the end. The authors also gave an agent examples of action sequences from earlier tasks. A small number of examples helped, but too many became distracting.

# Completeness Audit

## Inventory-based coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/venue | Yes | Yes | Fully represented | ACL Findings 2025; bibliographic details noted in Stage 0/roadmap |
| Abstract | Yes | Yes | Fully represented | Claims integrated throughout |
| §1 Introduction | Yes, text and rendered page | Yes | Fully represented | Problem, gaps, contributions, headline results |
| §2 Related Works | Yes, text and rendered page | Yes | Represented in compressed form | Major benchmark categories retained |
| §3.1 Environment | Yes, text and rendered page | Yes | Fully represented | POMDP, actions, observations |
| §3.2 Dataset Construction | Yes, text and rendered page | Yes | Fully represented | Prompts, annotation, counts, metrics |
| §3.3 Multimodal Web Content | Yes, text and rendered page | Yes | Fully represented | Image/text dependence and extraction |
| §3.4 Multihop Cross-website Browsing | Yes, text and rendered page | Yes | Fully represented | Definition and task flow |
| §3.5 Evaluation | Yes, text and rendered page | Yes | Fully represented | Both single- and multihop methods |
| §4.1 Baselines | Yes, text only | Yes | Fully represented | Page 6 not visually rendered |
| §4.2 Main Results | Yes, text plus rendered Table 2 | Yes | Fully represented | Numerical conditions preserved |
| §4.3 Challenge Analysis | Yes, text plus rendered Tables/Figures | Yes | Fully represented | Search, memory, input length |
| §4.4 Memory-augmented Agents | Yes, text and rendered diagrams | Yes | Fully represented | Three memory systems and ablation |
| §5 Conclusion/Outlook | Yes, text and partial rendered page | Yes | Fully represented | Future action evaluation included |
| §6 Limitations | Yes, text only | Yes | Fully represented | Page 9 not rendered |
| §7 Ethical Considerations | Yes, text only | Yes | Fully represented | Bias warning represented |
| References | Yes | No individually | Inspected but deliberately omitted as repetitive/non-substantive | Prior-work categories summarized; full bibliography not reproduced |
| Appendix A.1 | Yes, text and rendered page | Yes | Fully represented | Versions and viewport |
| Appendix A.2 | Yes, text and rendered page | Yes | Fully represented | GPU and runtime |
| Appendix A.3 | Yes, text and rendered pages | Yes | Fully represented | Extended hops and memory ablation |
| Appendix B.1.1–B.1.3 | Yes | Yes | Fully represented | Annotators, protocol, statistics |
| Appendix B.2.1–B.2.2 | Yes | Yes | Fully represented | Website list and VWA comparison |
| Appendix C | Yes, text; pages 13–14 rendered | Yes | Represented in compressed form | Extended survey material condensed |
| Appendix C.1 | Yes, text only on p. 16 | Yes | Represented in compressed form | Benchmark descriptions grouped |
| Figure 1 | Yes, visually | Yes | Fully represented | Four-hop task workflow |
| Figure 2a–c | Yes, visually | Yes | Fully represented | Distribution, intents, task counts |
| Figure 3 | Yes, visually | Yes | Fully represented | Exact bars unavailable |
| Figure 4 | Yes, visually | Yes | Fully represented | Memory architecture |
| Figure 5 | Yes, visually | Yes | Fully represented with uncertainty | Values only approximately readable |
| Table 1 | Yes, visually/textually | Yes | Fully represented | Benchmark comparison |
| Table 2 | Yes, visually/textually | Yes | Fully represented | Input icons partly extraction-sensitive |
| Table 3a–b | Yes, visually/textually | Yes | Fully represented | Hop-position analysis |
| Table A1 | Yes, visually/textually | Yes | Fully represented | Counts and success rates |
| Table A2 | Yes, visually/textually | Yes | Fully represented | Fourteen websites |
| Table A3 | Yes, visually/textually | Yes | Fully represented | Example comparison |
| POMDP formulation | Yes | Yes | Fully represented | §3.1 |
| Prediction equation | Yes | Yes | Fully represented | Appendix C, p. 14 |
| Equation (1) | Text only | Yes | Represented with uncertainty | Page 15 was not visually rendered |
| Formal algorithms | Not present | Yes | Not applicable | No pseudocode/algorithm block |
| Theorems/lemmas | Not present | Yes | Not applicable | Empirical benchmark paper |
| Explicit RQ1 | Yes | Yes | Fully represented | Abstract |
| Formal hypotheses | None found | Yes | Fully represented | Absence explicitly stated |
| Main benchmark experiment | Yes | Yes | Fully represented | X1–X3 |
| Hop analyses | Yes | Yes | Fully represented | X4–X5 |
| Memory ablation | Yes | Yes | Fully represented | X6 |
| Major contributions | Yes | Yes | Fully represented | Separated by type |
| Author-stated limitations | Yes | Yes | Fully represented | §6 and appendix qualifications |
| Separate supplementary files | No | Yes | Missing from supplied material | None supplied |
| Code, data, and trajectories | No | Yes | Missing from supplied material | Repository merely referenced |

## Missing or inaccessible material

- No separate supplementary file was supplied.
- The referenced code/data repository and underlying dataset files were not supplied.
- Agent trajectories supporting the qualitative failure analysis were not supplied.
- Pages 6, 9, 11, 15, and 16 were available only as extracted text, not as rendered images.
- The full list of 12 summarized actions is not provided in the paper.
- Exact Figure 5 bar values are not labeled.
- Exact per-hop-count values in Figure 3 are not labeled.
- Exact decoding parameters, seeds, repeat counts, and evaluation costs are not specified.

## Uncertain interpretations

- Figure 2 reports 2,991 hops, while §3.2 reports 2,989.
- Table 2’s icon-based input column is partially corrupted in text extraction, so not every icon combination can be reconstructed with complete confidence.
- Equation (1) appears not to condition on multimodal input \(M\), despite the preceding definition; the unrendered page prevents visual verification.
- Section 6 does not clearly identify which non-offline website it characterizes as open-source.
- Figure 5 values beyond their qualitative ordering are approximate visual estimates.
- The first-hop decline is not monotonic in Table A1’s sparse 8–10-hop groups.

## Deliberately compressed material

- The complete bibliography was not reproduced.
- Appendix C’s descriptions of multimodal datasets, instruction tuning, web agents, and mobile agents were summarized by category.
- Repeated claims about realism, compositionality, and agent difficulty were consolidated.
- Minor screenshot text inside Figure 1 and example webpage images in Table A3 was described functionally rather than transcribed.

## Potential omissions

No known substantive section, subsection, experiment, figure, table, major equation, contribution, or author-stated limitation from the supplied 16-page inventory is absent from the analysis. The unrendered pages and unavailable external artifacts listed above prevent claiming full visual or artifact-level inspection beyond the supplied text.