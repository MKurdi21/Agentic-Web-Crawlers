# WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks

**Authors:** Léo Boisvert, Megh Thakkar, Maxime Gasse, Massimo Caccia, Thibault Le Sellier De Chezelles, Quentin Cappart, Nicolas Chapados, Alexandre Lacoste, and Alexandre Drouin  
**Affiliations:** ServiceNow Research, Mila, Polytechnique Montréal, and Chandar Research Lab  
**Venue:** NeurIPS 2024, Datasets and Benchmarks Track

## 1. Background and Context

Large language models (LLMs) increasingly power autonomous agents that can use software through APIs or interact directly with graphical interfaces on phones, desktops, and websites. Web agents are especially useful because they can operate software even when no API is available, potentially automating tedious workplace activities and improving accessibility.

The motivating problem is substantial: the paper reports that, in 2024, the average adult spent about **400 minutes per day** using software and the internet. Workplace users often spend part of this time finding information buried in knowledge bases, coordinating schedules, and completing forms in complicated interfaces. Autonomous agents could take over such routine work, freeing people for more valuable activities.

Methods such as chain-of-thought, ReAct, and tree-of-thought prompting suggest that modern LLMs can plan and reason. However, it remains unclear whether they can apply those abilities reliably while carrying out realistic, multi-step work in enterprise software.

Earlier web-agent benchmarks do not fully answer this question:

- **MiniWoB** contains 125 synthetic tasks involving actions such as clicking buttons and filling fields.
- **WebArena** contains 190 realistic tasks across diverse websites, including e-commerce and social forums.
- **WorkArena L1** contains 33 basic enterprise tasks in ServiceNow, such as filling a form or sorting a list.
- WorkArena’s tasks are certifiable but mostly atomic: the agent receives explicit field values or navigation instructions and performs a limited operation that is easy for humans.

WorkArena++ addresses the absence of a benchmark for complex, compositional knowledge work. It builds realistic workflows by chaining atomic tasks and requires planning, retrieval, memorization, contextual understanding, and logical or mathematical reasoning.

### Technical foundation

WorkArena++ is built on two existing systems:

- **BrowserGym** provides chat-based user–agent interaction, multimodal browser observations—including HTML, accessibility trees, screenshots, element coordinates, and set-of-marks—and a standardized action interface.
- **WorkArena** supplies atomic ServiceNow tasks. Each task includes:
  - an **oracle**, a human-coded Playwright procedure that solves it; and
  - a **validator**, which checks the browser and database state and returns success or failure.

Agents interact with a remotely hosted ServiceNow Personal Developer Instance through BrowserGym. Validation examines both the database through backend REST APIs and the open page through frontend JavaScript APIs. The code interacting with ServiceNow is open source and does not depend on proprietary ServiceNow code.

**Figures 2–3** illustrate this architecture: a natural-language request is sent through chat, the agent observes the browser through representations such as HTML, an accessibility tree, or a screenshot, and it performs standardized actions. BrowserGym mediates perception and action, while WorkArena controls task setup, teardown, and validation.

---

## 2. Research Goal and Objectives

The central goal is to determine whether current LLM- and vision-language-model-based web agents can perform realistic, multi-step knowledge-worker workflows in enterprise software.

The paper pursues five related objectives:

1. Create a substantially larger and more demanding enterprise web-agent benchmark.
2. Test agents’ ability to plan, solve constrained problems, retrieve information, perform logical and arithmetic reasoning, remember information across pages, and recognize impossible tasks.
3. make evaluation reproducible, certifiable, isolated between tasks, and affordable.
4. Compare contemporary open- and closed-source agents with human workers to establish whether the tasks are genuinely solvable.
5. Provide a compositional framework and oracle-generated browser traces that support expansion of the benchmark and future model fine-tuning.

The experiments implicitly address two central questions:

- Are WorkArena++ tasks feasible for people?
- Why do otherwise capable web agents fail on them?

---

## 3. Methods (Approach/Design)

### 3.1 Benchmark construction

WorkArena++ contains **682 tasks**, expanding WorkArena from 33 atomic tasks. The benchmark defines **341 workflows**, each presented at two difficulty levels:

- **L2—explicit instructions:** The chat message gives the exact steps and required values, though the agent must still determine how to operate the interface and sometimes reason about constraints.
- **L3—ticket plus knowledge base:** The agent receives an assigned ticket containing key task-specific details but not the procedure. It must recognize the ticket as work to be done, locate the appropriate knowledge-base article, remember its rules, combine information from multiple sources, execute the workflow, and close the ticket.

Thus, L2 and L3 contain the same underlying workflows, but L3 presents them in a less explicit and more realistic manner.

For example, an L2 expense task directly tells the agent to open Expense Lines, filter entries by a supplied hashtag, and remove duplicate descriptions. Its L3 version merely asks the agent to complete the assigned task; the ticket directs it to a knowledge-base article containing the rules.

**Figure 1** gives a representative workflow: an IT worker receives a restocking ticket, reads a dashboard to identify low-stock products, orders enough units from the service catalog to reach a minimum quantity, and finally closes the ticket.

### 3.2 Skills and task families

The 682 tasks are divided into five skill categories.

#### Planning and problem solving: 66 workflows × 2 levels

These require a global plan and constrained decision-making:

- **Workload balancing:** 3 tasks per level, redistributing problems from the busiest to the least busy worker.
- **Work assignment:** 6 per level, assigning incidents or problems to appropriate category experts, sometimes according to priority and expertise.
- **Scheduling requests:** 48 per level, placing requests into time windows while handling duration, risk, impact, ordering, and non-overlap constraints.
- **Problem deduplication:** 9 per level, identifying duplicate problem descriptions and sometimes using priority to choose which record to mark as the duplicate.

#### Information retrieval: 39 workflows × 2 levels

- **Dashboard retrieval:** 29 per level. Agents read values or labels from bar or pie charts and use them to filter records, create incidents, or order low-stock products.
- **List/form retrieval:** 10 per level. Agents filter lists or inspect forms, then order something or return the requested information in chat.

#### Data-driven decision-making and reasoning: 156 workflows × 2 levels

- **Expense management:** 12 per level. Agents find duplicate expenses and apply hierarchical rules based on dates, amounts, links to other tasks, or other attributes.
- **Investment maximization:** 57 per level. Agents choose investments that maximize return under a budget—effectively a small knapsack problem—and may need to delete rejected items, report selected IDs, or calculate total return.
- **Chart-based calculations:** 87 per level. Agents compute quantities such as a mean, median, or mode from plots, then act on the result—for example, creating probation calls for below-median workers.

#### Sophisticated memorization

The main text reports **28 workflows × 2**, while Appendix C reports **29 × 2**. The appendix further lists:

- **Navigation-and-do:** 26 per level, requiring agents to remember page and operation details while navigating and then sorting, filtering, filling forms, or ordering products.
- **User management:** 2 per level, covering onboarding and offboarding.

These appendix subtotals equal 28, so the appendix heading’s value of 29 appears internally inconsistent. The complete benchmark total remains reported as 682.

Onboarding can require creating a user, ordering a laptop, creating a hardware asset, and assigning it to that user. Offboarding can require unassigning hardware and deleting or deactivating the user.

#### Contextual understanding through infeasible tasks: 52 workflows × 2 levels

These contain impossible instructions, such as requesting a nonexistent field or an invalid product configuration. Depending on the variant, the agent must either declare the task infeasible or explain precisely why—for example, identifying the missing field.

**Figure 4a** shows the distribution across these five categories. Data-driven decision-making is the largest group, followed by planning/problem solving, contextual understanding, information retrieval, and memorization.

### 3.3 Knowledge-base protocols

**Figures 23–32** show the procedural articles available to agents during L3 tasks:

- Workload balancing: find the busiest and least busy workers, locate a low-priority problem assigned to the busiest worker, and reassign it.
- Work assignment: locate the incident, identify its category and priority, and assign it to the corresponding expert, supporter, or planner.
- Scheduling: enforce the allowed time frame, higher-impact-first ordering, limits between consecutive requests, and risk-based durations of **3 days for high risk, 2 for moderate risk, and 1 for low risk**.
- Deduplication: find identical problem statements, preserve the higher-priority record, and apply special handling to critical records.
- Dashboard retrieval: locate a dashboard by hashtag, read chart values or labels, apply specified rounding or comparison rules, and use the result in a downstream task.
- Warranty retrieval: find the laptop assigned to a user and read its warranty expiration.
- Expense management: find duplicate descriptions; keep linked expenses over unlinked ones, otherwise the oldest linked record, otherwise the most expensive, or any one if costs match.
- Investment maximization: inspect return and amount fields, choose the best subset within budget, and return or retain the requested outputs.
- Onboarding: create a user, order an Apple MacBook Pro 15-inch laptop, create a matching hardware asset, and assign it.
- Offboarding: unassign hardware and delete the user account.

**Figures 11–22** contrast explicit L2 chat instructions with terse L3 ticket descriptions for the task families. Their central point is that L3 preserves the workflow but moves the procedure into an external company document that the agent must discover and remember.

### 3.4 Visual diversity, isolation, and extensibility

To reduce overfitting to one visual style, each task randomly uses one of **10 fictitious company themes**. **Figures 34–43** show landing pages and list views for Astranova, Charlie’s Cookies, Great Pasta, Mighty Capital, Skyward, SpeedyTires, TurboBots, UltraShoes, VitaSphere, and WorkArena. The themes change colors and branding while retaining the underlying functionality.

For consistency and isolation:

- An installer standardizes system settings, themes, knowledge bases, list layouts, and form layouts.
- Every task runs under a newly created user account.
- The user account is deleted after the task.
- Interface changes made during one task therefore do not alter later tasks or interfere with parallel evaluation.

The benchmark builds complex tasks by composing atomic setup, teardown, oracle, and validation functions. Validation may be sequential—checking each constituent operation—or global, by examining the final database state.

**Figures 45–46** demonstrate compositional construction. A basic onboarding workflow creates a user, orders a laptop, and assigns it. It can be extended simply by adding another validated step, such as creating the new employee’s first assigned task.

### 3.5 Ground-truth trace generation

Every task has a Playwright oracle that solves it step by step. BrowserGym records:

- screenshots;
- accessibility trees;
- the DOM;
- optional set-of-marks; and
- the oracle’s executed actions.

**Figure 44** illustrates a trace for purchasing an iPad Pro: the oracle starts at the landing page, opens the catalog, reaches the product, configures it, and submits the order. Every action is stored alongside the corresponding browser observation. This mechanism can generate thousands of high-quality observation–action trajectories for fine-tuning web agents.

### 3.6 Standardized evaluation curriculum

Each task supports thousands of possible configurations controlled by a task-level random seed. For example, an investment task may receive a different budget.

To make evaluation reproducible and manageable, the authors define a hierarchical curriculum:

1. Group tasks by the primary skill.
2. Divide each skill into buckets of tasks requiring similar abilities.
3. Assign sampling weights that maximize coverage while reducing redundancy.
4. Use a single meta-seed to generate task seeds.
5. Sample tasks without replacement within each bucket.

Seeds **0–9** are reserved for evaluation; other seeds may be used for tuning. Averaging results across evaluation seeds is recommended to reduce standard error. The curriculum produces **235 L2 and 235 L3 instances**, or 470 WorkArena++ agent-evaluation instances.

**Figure 33** displays the curriculum configuration dictionary and its buckets, weights, and number of seeds. **Figure 4b** plots oracle action counts for the 470 L2/L3 instances and WorkArena L1 tasks. Most tasks require fewer than 50 actions, but WorkArena++ has a longer tail reaching approximately 140 actions. This motivates, while also qualifying, the experimental 50-step limit.

### 3.7 Agent design

At each time step, an LLM receives the goal and browser state and uses chain-of-thought prompting to select one action.

The observation includes:

- the goal;
- HTML and/or the accessibility tree;
- the focused element;
- the preceding action’s error, if any;
- BrowserGym’s `clickable` and `visible` properties;
- the full history of earlier thoughts and actions; and
- for GPT-4o vision, a screenshot annotated with set-of-mark element identifiers.

The history acts as a crude memory mechanism for otherwise memoryless models.

The available high-level actions are restricted to:

- chat actions, including returning requested information;
- `report_infeasible(reason)`;
- element-ID-based browser operations such as clicking, typing, filling, or selecting.

Agents can issue only one action per step. A parsing loop can reprompt a model up to **four times** when its response has invalid syntax. The prompt contains one generic formatting example but no task-specific examples, making the setup zero-shot.

**Figures 9–10** show the prompt and matching screenshot. Each browser element is assigned a `bid` identifier that appears in both the textual accessibility tree and visual set-of-marks, so the model can refer to the same element through either modality.

### 3.8 Models and compute

The evaluated models were:

- GPT-3.5 (`gpt-3.5-turbo-1106`);
- GPT-4o (`gpt-4o-2024-05-13`);
- GPT-4o with screenshots and set-of-marks, called GPT-4o-v;
- Llama3-70B-Instruct; and
- Mixtral-8×22B.

Llama3 and Mixtral were hosted through Hugging Face Text Generation Inference on **four A100 GPUs**.

Although the models’ native limits differ, experimental prompts were capped at:

- **40K tokens** for GPT-4o;
- **15K** for GPT-3.5;
- **8K** for Llama3;
- **32K** for Mixtral.

If necessary, the end of the HTML/accessibility tree was progressively removed. Each agent run was capped at **50 time steps** for cost, credit, and rate-limit reasons.

### 3.9 Human study

The feasibility study recruited **15 unpaid volunteers**, including ServiceNow research personnel and students from the University of Montreal and École de technologie supérieure. All gave informed consent.

The in-person protocol at ServiceNow’s Montreal office consisted of:

1. a **15-minute recorded training presentation**;
2. **15 minutes of self-guided exploration** in a free ServiceNow Personal Developer Instance; and
3. up to **seven individually completed tasks** per participant.

Participants could not discuss tasks, and both completion time and success were recorded.

The human curriculum contained **98 instances**: 49 sampled uniformly across skills, each presented in its L2 and L3 form. Humans used the same BrowserGym chat and browser interface as agents, plus a movable evaluation console with:

- a Validate button;
- a Give Up button;
- continuous automatic validation; and
- only incomplete/solved status, without intermediate corrective feedback.

**Figures 5, 7, and 8** show the consent form, training slides, and evaluation interface.

---

## 4. Results and Findings

### 4.1 Main agent results

The central result is an extreme failure of contemporary agents on WorkArena++ despite substantially better performance on simpler benchmarks.

#### WorkArena++ L3: 235 instances

Every tested agent achieved **0.0% ± 0.0** overall:

- GPT-3.5: 0.0%
- GPT-4o: 0.0%
- GPT-4o-v: 0.0%
- Llama3: 0.0%
- Mixtral: 0.0%

Every model also scored zero in all five individual L3 skill categories.

Humans achieved **93.9% ± 3.4** overall on the human curriculum’s L3 subset:

- Contextual understanding: **87.5% ± 11.7**
- Data-driven decision-making: **100.0% ± 0.0**
- Planning/problem solving: **87.5% ± 11.7**
- Information retrieval: **100.0% ± 0.0**
- Sophisticated memorization: **91.7% ± 8.0**

GPT-4o achieved **0.0%** on that same human L3 subset.

#### WorkArena++ L2: 235 instances

Overall agent performance was:

- GPT-3.5: **0.0% ± 0.0**
- GPT-4o: **3.0% ± 1.1**
- GPT-4o-v: **3.8% ± 1.3**
- Llama3: **0.0% ± 0.0**
- Mixtral: **0.0% ± 0.0**

By skill:

- Contextual understanding: all agents 0.0%.
- Data-driven decision-making: all agents 0.0%.
- Planning/problem solving: all agents 0.0%.
- Information retrieval: GPT-4o-v reached **3.6% ± 2.5**; all others scored zero.
- Sophisticated memorization: GPT-4o and GPT-4o-v each reached **14.6% ± 5.1**; all others scored zero.

Humans again achieved **93.9% ± 3.4** overall:

- Contextual understanding: **100.0% ± 0.0**
- Data-driven decision-making: **84.6% ± 10.0**
- Planning/problem solving: **100.0% ± 0.0**
- Information retrieval: **100.0% ± 0.0**
- Sophisticated memorization: **91.7% ± 8.0**

GPT-4o achieved only **2.1% ± 2.0** on the same human L2 subset, with its sole nonzero category being sophisticated memorization at **8.3% ± 8.0**.

Thus, over the human curriculum, humans scored **93.9%**, whereas GPT-4o scored **2.1%**.

### 4.2 Comparison with earlier benchmarks

**Table 2** shows that these agents are not universally incapable of browser use; their failure is specific to the benchmark’s increased complexity.

| Benchmark | GPT-3.5 | GPT-4o | GPT-4o-v | Llama3 | Mixtral | Human |
|---|---:|---:|---:|---:|---:|---:|
| WorkArena L1, 33×10 seeds | 6.1±1.3 | 42.7±2.7 | 41.8±2.7 | 17.9±2.1 | 12.4±1.8 | — |
| MiniWoB, 125×5 seeds | 43.4±1.6 | 71.3±1.5 | 72.5±1.5 | 68.2±1.2 | 62.4±1.6 | 93.5 |
| WebArena, 812 instances | 6.7±0.9 | 23.5±1.5 | 24.0±1.5 | 11.0±1.1 | 12.6±0.5 | 78.2 |

The results establish three patterns:

1. Performance collapses as tasks move from atomic WorkArena L1 operations to WorkArena++ workflows.
2. GPT-4o substantially outperforms GPT-3.5, but remains very weak.
3. Vision provides a small advantage: GPT-4o-v alone solves some chart-retrieval tasks, suggesting that screenshots help when values must be read visually. It does not solve the broader planning and reasoning problem.

No statistical hypothesis tests or p-values are reported; uncertainty is expressed through standard errors.

### 4.3 Human-participant characteristics

**Figure 6** reports the cohort demographics. The paper emphasizes the following exact values:

- **11 of 15** participants had been employed by ServiceNow.
- Four of those 11 were student researchers whose work did not expose them to the product.
- **46.7%** described themselves as first-time ServiceNow users.
- **86.7%** used ServiceNow at most a few times per month.
- All participants had undergraduate degrees, and approximately half had advanced degrees.
- Approximately three-quarters had worked at ServiceNow.

The visual also indicates that the group covered multiple countries, occupations, ages, education levels, and prior human-evaluation experience, but the small chart labels do not support a more reliable transcription beyond the percentages explicitly discussed in the text.

A learning effect was observed: participants became faster or more efficient as they progressed. Only **3 of 15** received a repeated underlying task, and those repetitions used the other difficulty level and a different seed.

During evaluation, several participants changed an L3 ticket to “Closed—Complete” but failed to save it with Update. A general announcement explained this requirement, after which the error did not recur. The authors argue that this hint cannot explain the human–agent gap because agents generally failed much earlier in L3 trajectories.

Humans had no explicit action limit. AI agents had 50 steps because of practical resource constraints, but oracle analysis indicated that this was enough for most curriculum tasks.

### 4.4 Error analysis

The authors manually examined traces from the strongest closed- and open-source agents, GPT-4o and Llama3. Failures fell into several recurring classes.

#### Information retrieval and element grounding

Agents often reached the correct dashboard or page but extracted the wrong value, misread the current state, or selected the wrong element.

Browser elements inside an iframe combine the iframe letter with a number. For example, element 252 inside iframe `a` is `a252`. One agent observed `a252` but clicked `252`, either activating an unrelated element or causing an error.

In another example, the list header explicitly said it was already sorted in ascending order by Number. The model repeated a click on that header rather than moving to the second required sort field. This shows that detecting text does not guarantee understanding it.

#### Insufficient exploration

Agents frequently failed to reveal hidden interface content.

**Figure 47** shows the folded and expanded All menu. When the Asset submenu is folded, Hardware Assets is absent from the accessibility tree. A successful agent must either search for it or expand the submenu. Agents often failed to try either strategy.

Forms also divide fields among tabs. In **Figures 48–49**, the agent filled almost an entire change-request form but failed to open the Closure Information tab for “Close notes.” It instead overwrote another field and then submitted the incorrect form.

#### Hallucinated actions and controls

Agents invented:

- unsupported functions such as `check` and `uncheck`;
- element references based on names rather than valid `bid` identifiers;
- selector-like controls such as `button:has-text("All")`; and
- imaginary one-click buttons that would directly solve the task.

These actions do not exist in the supplied action interface and therefore fail.

#### Asking the user for help

When uncertain, an agent sometimes sent a chat message asking the user to confirm whether a task was complete instead of continuing to inspect and solve it.

#### Thought–action inconsistency

An agent recognized that it was on a “Belkin iPad Mini Case” page and stated that it needed an iPad Mini, but then clicked Order this Item and purchased the case. Since ordering ends that WorkArena task, the run immediately failed.

#### Misunderstanding L3 tickets

In **Figure 50**, the ticket described a hardware asset that still needed to be created. The model interpreted those details as evidence that the asset had already been created and immediately changed the ticket state to Closed Complete. It confused task instructions with completed work.

#### Hallucinated consequences

Agents frequently believed that an action had succeeded without verifying the page state.

In **Figures 51–52**, the model correctly filled the Serial Number field, then accidentally overwrote it with the cost-center value while searching for a hidden field. It later reasoned as if the original serial number were still present and moved on.

Similarly, after filling the wrong field in the change-request form, an agent assumed that only submission remained and finalized an invalid record.

#### Repeated useless actions

Agents could become trapped in loops. **Figure 53** shows a service-catalog page where the agent needed to enter Hardware and order a Loaner Laptop. It repeatedly clicked the same search box because the click neither changed the page nor returned an error, continuing until the episode ended.

### 4.5 Context-length ablation

A separate ablation on WorkArena L1 compared a Llama3-based agent across four context sizes:

- **130K:** 17.9% ± 2.1
- **64K:** 14.8% ± 2.0
- **32K:** 17.6% ± 2.1
- **13K:** 18.2% ± 2.1

Performance was similar across context lengths. The authors caution that this result comes from simpler L1 tasks and should not be assumed to hold for WorkArena++ workflows, which demand more memory and prompt detail.

---

## 5. Analysis and Interpretation

The findings answer the paper’s two primary empirical questions.

First, WorkArena++ is feasible: lightly trained humans solved about **94%** of the evaluated tasks, including L3 tasks. The benchmark is therefore not merely impossible or incorrectly specified.

Second, the low model scores cannot be explained solely by unfamiliarity with ServiceNow or difficulty operating its widgets. The trace analysis shows failures in planning, exploration, goal interpretation, state tracking, grounding, and reasoning about action consequences.

The L2–L3 contrast is especially informative. GPT-4o-based agents solved a small number of explicitly instructed L2 tasks but no L3 tasks. L3 adds the need to recognize a ticket as an assignment, seek external instructions, integrate the ticket with the knowledge-base protocol, remember both, and close the task properly. Current agents could not reliably coordinate these capabilities.

The authors also argue that human familiarity does not explain the result:

- Nearly half of participants were first-time users.
- Most used ServiceNow rarely.
- Some ServiceNow-employed participants did not work with the product.
- LLMs themselves showed detailed knowledge of ServiceNow APIs, data structures, and procedures, probably acquired from public material.
- Most agent errors concerned planning and reasoning, not elementary widget use.

Although the cohort was highly educated and not representative of all users, the tasks mostly require following instructions, using ordinary UI components, and performing basic reasoning rather than advanced academic expertise.

The vision result suggests that screenshots improve perceptual retrieval from charts, but visual access alone does not resolve multi-step reasoning failures. Likewise, reinjecting full thought/action history provides a form of memory, yet does not produce robust long-horizon execution.

The authors expect several lessons to generalize beyond ServiceNow because lists, forms, tabs, menus, and dashboards appear across enterprise software, while the observed errors—hallucination, weak exploration, misunderstanding goals, and poor consequence tracking—are not specific to ServiceNow.

---

## 6. Contributions and Novelty

The paper makes the following main contributions:

- It introduces **WorkArena++**, a benchmark of **682 certified enterprise tasks**, compared with WorkArena’s 33 atomic tasks.
- It is presented as the first web-agent benchmark requiring this combination of compositional planning, constrained problem-solving, logical and arithmetic reasoning, information retrieval, long-context understanding, memorization, and recognition of infeasibility.
- It defines two presentation levels—explicit L2 and realistic ticket/knowledge-base L3—over the same 341 workflows.
- It introduces a reproducible curriculum that samples task instances uniformly across skill areas while reducing redundancy.
- It provides strong automated validation through browser and database state.
- It improves task isolation by creating and deleting a dedicated user account for each episode.
- It adds 10 visual themes to test robustness to changes in branding and color.
- It supplies a modular framework for constructing new workflows from reusable atomic tasks and validators.
- It can automatically generate ground-truth multimodal observation–action traces through the human-coded oracles.
- It provides empirical evidence of a very large gap between current agents and humans: approximately **2.1% versus 93.9%** for GPT-4o and humans on the human curriculum.
- It supplies a detailed taxonomy of failure modes that can guide improvements in web-agent planning, grounding, exploration, and state tracking.

---

## 7. Limitations and Caveats

### Benchmark coverage

WorkArena++ does not cover every knowledge-work role, persona, or workflow. The authors estimate that comprehensive coverage would require thousands more tasks.

All tasks are confined to ServiceNow. Multi-application workflows would be more diverse and representative, although BrowserGym already includes other benchmarks and WorkArena++’s common UI components may support some generalization.

The study does not evaluate safety or robustness against malicious behavior. This remains a major obstacle to real-world deployment.

The experiments also omit other potentially relevant open- and closed-source models, especially models with very long contexts, such as the cited one-million-token system.

### Agent evaluation

The 50-action limit is a practical constraint, although oracle action counts suggest that most curriculum tasks fit within it. Some tasks have longer oracle trajectories, so the limit may prevent completion in a minority of cases.

History reinjection is only a crude memory mechanism. Prompt truncation can also remove parts of the HTML or accessibility tree when observations become too long.

The context-length ablation was conducted on L1, so it does not establish that context size is unimportant for WorkArena++.

### Human evaluation

The human sample was small—15 participants—and the curriculum contained only 98 instances rather than the full benchmark.

The cohort was not demographically representative:

- about 75% had worked at ServiceNow;
- all held undergraduate degrees;
- about half held advanced degrees.

Participants received 30 minutes of combined training and exploration, and performance improved with experience. The protocol did not directly correct for this learning effect.

The general announcement about saving closed tickets changed the evaluation environment after a recurring human mistake. The authors argue that it did not explain the broad gap because agents did not reach that stage.

Humans had no action limit, unlike AI agents, though the authors state that the AI limit was designed to be sufficient for completion.

### Internal reporting inconsistency

The paper reports sophisticated memorization as **28 × 2** tasks in the main text, **29 × 2** in the appendix heading, and then lists 26 navigation-and-do plus 2 user-management workflows, totaling 28. This discrepancy is present in the supplied document.

### Societal caveats

More capable workplace agents could improve productivity and accessibility and may open opportunities for users with impairments. Potential harms include:

- displacement of human workers;
- privacy and security risks;
- gradual loss of human skills and independent decision-making;
- substantial computation and energy use, with environmental effects.

---

## 8. Future Work or Open Questions

The authors propose several directions:

- Add further ServiceNow workflows.
- Create tasks explicitly evaluating agent safety and cybersecurity.
- Develop a hidden test set suitable for competitions.
- Use oracle-generated traces to fine-tune more robust LLM- and VLM-based agents.
- Expand coverage toward the thousands of tasks required to represent more knowledge-worker roles.
- Build longer and more complex workflows, potentially drawing inspiration from occupational task databases.
- Add collaborative tasks in which agents delegate subtasks to human or artificial colleagues, exchange chat messages, or leave ticket comments. Excessive delegation could be penalized.
- Create workflows spanning multiple external applications.
- Potentially introduce an L4 level using multiple environments—for example, replacing ServiceNow’s internal knowledge base with an external source.
- Encourage open-source community contributions to tasks and environments.
- Study whether better memory, exploration, grounding, consequence assessment, and planning can close the human–agent gap.

The benchmark’s modular design supports these expansions: a new atomic task requires setup, teardown, oracle, and validation functions, while larger workflows can be built by composing existing pieces.

---

## 9. High-Level Takeaway (Plain Language)

WorkArena++ tests whether AI agents can do realistic office work in a browser—not just click one button or fill one form, but gather information, remember instructions, reason about constraints, complete several connected steps, and recognize impossible requests. Humans solved about **94%** of the tested tasks, while GPT-4o solved about **2%**, and every tested model scored zero on the more realistic L3 benchmark. The main obstacle was not merely using the interface: agents misunderstood goals, overlooked hidden information, invented controls, forgot what actions actually did, and became trapped in loops. The benchmark therefore provides both a demanding target and a source of training traces for developing web agents that are substantially more reliable in real workplaces.