# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Available page range | Pages 1–22 |
| Apparently missing pages | None |
| Native/extracted text | Available for all 22 pages; no page was flagged as scanned or unusually low-text |
| Visually rendered pages | 1–9, 12, and 16–22 |
| Pages not visually rendered | 10, 11, and 13–15 |
| Figures visually inspected | Figures 1–11; their rendered source pages were supplied |
| Tables visually inspected | Tables 1–6; their rendered source pages were supplied |
| Equations | The principal formalism on p. 3 is readable, but subscripts/superscripts are OCR-sensitive |
| Appendices | Appendix A, §§A.1–A.10, pp. 15–22 |
| References | pp. 10–14; supplied as text, but pages 10, 11, 13, and 14 were not visually rendered |
| Supplementary material | No separate supplementary files were supplied |
| Referenced external artifacts | Code, data, Docker images, reproduction resources, trajectories, videos, website manuals, and the project website/repository are mentioned but were not supplied |
| OCR required | No; native text was available. Extraction artifacts remain possible in mathematical notation and typography |
| Principal limitations | Visual inspection was partial at the page level, although every substantive figure and table was rendered. Bibliographic typography on four reference pages and the opening of Appendix A on p. 15 were assessed from text only. External artifacts and executable environment were not inspected. |

All substantive claims below are closed-document findings. Unless marked otherwise:

- **Author-reported** means stated in the supplied paper.
- **Directly observable** means visible in a supplied page image.
- **Analyst-derived** means calculated from reported values.
- **Analyst interpretation** means an inference rather than an explicit author claim.
- No external information is introduced.

# 1. Plain-Language Orientation

WebArena is both a software environment and a benchmark for testing artificial-intelligence agents that operate websites from natural-language instructions.

The problem is that many earlier agent benchmarks, according to the authors, simplify websites, freeze them into static snapshots, restrict the diversity of tasks, or judge whether an agent copied a reference sequence of clicks rather than whether it actually achieved the requested outcome. Such tests may not reveal whether an agent can handle realistic, multi-step web work (pp. 1–2, §§1–2).

The researchers therefore built a self-hosted collection of functional websites representing:

- online shopping;
- social discussion;
- collaborative software development;
- e-commerce content management;
- supporting services including a map, calculator, scratchpad, Wikipedia, and manuals.

They populated these services with sampled real-world data, packaged them in Docker containers, supplied mechanisms for deterministic reset, and constructed 812 benchmark tasks from 241 templates (pp. 2–5; Appendix A.1–A.2).

Tasks are expressed as high-level intents rather than click-by-click instructions. Examples include finding information from purchase history, navigating to assigned merge requests, posting content, changing configurations, and coordinating information across Wikipedia, a map, and GitLab (Figures 2 and 5).

Success is judged primarily by outcomes. Text answers are checked with exact matching, required-content matching, or a GPT-4 semantic-equivalence judge. Navigation and state-changing tasks are checked through URLs, page content, APIs, JavaScript selectors, or underlying website state (pp. 6–7, Table 1).

The main result is that the evaluated language-model agents performed poorly relative to humans:

- the best reported model condition, GPT-4 with chain-of-thought prompting and without the explicit “unachievable task” hint, succeeded on **14.41%** of tasks;
- sampled human participants succeeded on **78.24%**;
- GPT-4 with both chain-of-thought and the unachievable hint achieved **11.70%** (pp. 7–8, Table 2).

The central contribution is thus not a new high-performing agent. It is a reproducible, comparatively realistic testbed that exposes how unreliable contemporary web agents remain on long-horizon, functionally evaluated tasks.

# 2. Document Roadmap

The paper is organized as follows:

1. **Abstract and Introduction** (pp. 1–2) motivate realistic and reproducible evaluation and summarize WebArena’s environment, benchmark, and baseline results.
2. **Section 2: WebArena** (pp. 2–5) defines the environment, website selection, observations, actions, and simulated user roles.
3. **Section 3: Benchmark Suite** (pp. 5–7) explains intent creation, task categories, evaluators, unachievable tasks, annotation, and human performance.
4. **Section 4: Baseline Web Agents** (pp. 7–8) describes tested models, direct versus chain-of-thought prompting, accessibility-tree observations, and the unachievable-task hint.
5. **Section 5: Results and Analysis** (pp. 8–9) reports success rates and examines early stopping and consistency across related tasks.
6. **Section 6: Related Work** (p. 9) positions WebArena relative to other natural-language control benchmarks and interactive agents.
7. **Section 7: Conclusion** (p. 9) restates the environment, benchmark, outcome-based evaluation, and performance gap.
8. **Acknowledgements and References** (pp. 10–14) document support and cited literature.
9. **Appendix A** (pp. 15–22) gives implementation scale, reset behavior, user roles, intent distribution, human-performance qualifications, experimental settings, the fuzzy-match prompt and validation, full baseline prompts, and additional error analysis.

# 3. Background and Context

An **autonomous web agent** receives a human request, observes a browser, selects actions such as clicking or typing, and repeats this process until it believes the task is finished.

A **long-horizon task** requires many dependent actions. Figure 2 illustrates this with an itinerary request: find Pittsburgh art museums on Wikipedia, locate them on a map, optimize their order, and write the route into a particular GitLab repository.

A **large language model (LLM)** generates the agent’s next action. The tested models were GPT-3.5-Turbo-16K-0613, GPT-4-0613, and Text-Bison-001 (Appendix A.6).

**In-context learning** means that the prompt includes worked examples rather than updating model weights. Every tested prompting setup used two examples (§4, p. 7).

**Chain-of-thought (CoT) prompting** asks the model to write intermediate reasoning before emitting an action. The direct condition emits only an action (§4; Figures 7–10).

The **Document Object Model (DOM)** is the structured representation underlying an HTML page. An **accessibility tree** retains page elements useful to users and assistive technology—such as roles, labels, text, and focusability—while omitting much of the DOM’s less relevant structure (§2.3, Figure 3).

**Functional correctness** asks whether the requested outcome was achieved. It differs from requiring the same click sequence as a reference solution. Multiple action paths may be valid if they produce the correct final state (§1, p. 2).

A **content management system (CMS)** is an administrative interface for creating and modifying digital content. WebArena’s CMS is based on Adobe Magento’s administration portal (Appendix A.1).

# 4. Research Problem and Gap

## Existing problem

Developers need to determine whether language-guided agents can perform realistic web tasks reliably, not merely operate within small synthetic interfaces (§1).

## Shortcomings attributed to previous approaches

The authors identify four recurring weaknesses (pp. 1–2; Table 4):

- reduced functionality relative to real websites;
- simplified tasks and limited task diversity;
- static cached states that restrict exploration;
- evaluation against reference action sequences instead of completed outcomes.

They argue that live websites are also unsuitable for controlled comparison because CAPTCHAs, content changes, and configuration changes can alter task difficulty over time (§2, pp. 2–3).

## Research gap

The claimed gap is the absence of a benchmark combining all four properties listed in Table 4:

1. dynamic interaction;
2. a realistic environment;
3. diverse human-like tasks;
4. functional-correctness evaluation.

## Motivation

A realistic but resettable environment should allow fair, repeatable measurement of agents on tasks resembling those people perform online (§1).

## Scope

WebArena covers selected web domains and tools rather than the full public web. Its map is restricted to the northeastern United States, Wikipedia has a May 2023 cutoff, and the benchmark operates through locally hosted replicas and sampled data (Appendix A.1).

# 5. Research Questions / Objectives / Hypotheses

The paper does not state formally numbered research questions or hypotheses.

## Explicit objectives

- Build a **realistic and reproducible**, standalone web environment (§§1–2).
- Support high-level natural-language control of functional websites (§2.1).
- Construct a diverse benchmark of long-horizon tasks (§3).
- Evaluate task outcomes through functional correctness rather than action-sequence imitation (§3.2).
- Establish baseline agent and human performance (§§4–5).
- Analyze why current agents fail (§5.1; Appendix A.10).

## Informal questions addressed by analyses

The authors explicitly phrase two analysis questions:

- **Can models recognize when to stop or when a task is unachievable?** (§5.1, p. 8)
- **Can a model maintain consistent performance across similar tasks?** (§5.1, pp. 8–9)

## Author hypotheses

The authors hypothesize that limited LLM performance reflects missing capabilities such as active exploration and failure recovery (p. 2). In Appendix A.10, they further hypothesize that observation-related failures may be connected to dialogue-oriented pretraining and supervised fine-tuning, which emphasize responding to immediate observations and may encourage insufficient exploration. These are proposed explanations, not experimentally isolated causal findings.

# 6. Assumptions / Threat Model

This is not a security paper and specifies no adversarial threat model.

## System and environmental assumptions

- The environment state transition is deterministic (§2.1).
- Websites run as standalone local services rather than changing live services (§2).
- Website content, code, databases, and dependencies are packaged into Docker images (Appendix A.2).
- Agents interact through the supplied observation and action interfaces.
- Baseline agents receive accessibility-tree observations with element identifiers (§4).
- Users begin authenticated via cached cookies (Appendix A.3).
- Functional evaluators are assumed to capture the intent’s required outcome.
- For information-seeking tasks, annotated reference answers are treated as ground truth (§3.2).
- A maximum of 30 state transitions bounds each baseline execution (Appendix A.6).

## Trusted components

Implicitly trusted components include the local website implementations, initial data, reset images, task annotations, locator programs, and scoring functions.

## Excluded or unsupported situations

Some user requests are intentionally impossible because evidence, permissions, or website functionality is absent. Correctly returning “N/A” is part of the benchmark (§3.2, p. 7).

# 7. Methodology

## Study design

This is a mixed **systems, benchmark, dataset, and empirical evaluation** paper. The authors:

1. selected web domains;
2. implemented local website replicas;
3. populated them with realistic data;
4. defined browser observations and actions;
5. curated high-level task intents;
6. wrote outcome-oriented evaluators;
7. measured humans and three LLM-based agents;
8. performed prompt ablations and trajectory-based error analyses.

## Environment selection and implementation

Approximately 200 examples from the authors’ browser histories were inspected and grouped into abstract categories. The four most salient categories became e-commerce, social forums, collaborative development, and content management (§2.2, p. 3).

Implemented services include OneStopShop, GitLab, Reddit/Postmill, Magento CMS, OpenStreetMap, English Wikipedia, a calculator, and a scratchpad (§2.2; Appendix A.1).

Appendix A.1 reports:

- about **90,000 products** across more than **300 categories**;
- **95 subreddits**, **127,390 posts**, and **661,781 users**;
- **300 repositories** and more than **1,000 accounts** with at least one commit;
- at least ten repositories sampled for every programming language;
- 80% of repositories drawn from the top 90th-percentile star group and the remainder from the bottom 10th-percentile group, both weighted by stars;
- offline English Wikipedia with a **May 2023** cutoff;
- OpenStreetMap data limited to the northeastern United States.

## Environment model

On p. 3, §2.1, the environment is represented as:

\[
\mathcal{E}=\langle S,A,O,T\rangle
\]

where \(S\) is the state space, \(A\) the action space, \(O\) the observation space, and \(T:S\times A\rightarrow S\) the deterministic transition function.

At time \(t\), an agent chooses \(a_t\) from the intent \(i\), current observation \(o_t\), prior action history, and prior observation history. The action produces a new state and observation. A reward function evaluates the action trajectory and intermediate states against the intent.

## Observation space

Each observation can include (§2.3):

- the current URL;
- open browser tabs;
- the focused tab’s page content.

Content may be rendered as:

- raw HTML/DOM;
- an RGB screenshot;
- an accessibility tree.

Viewport restriction can reduce content to fit text-context or image-resolution constraints.

## Action space

Figure 4 lists:

- `noop`;
- `click(elem)`;
- `hover(elem)`;
- `type(elem, text)`;
- `press(key_comb)`;
- `scroll(dir)`;
- `tab_focus(index)`;
- `new_tab`;
- `tab_close`;
- `go_back`;
- `go_forward`;
- `goto(URL)`.

The prompts additionally define a `stop [answer]` completion action (Figures 7 and 9). Elements may be identified by screen coordinates or generated IDs (§2.4).

## User-role simulation

Separate profiles capture different permissions and histories. The shopping profile has more than 35 orders over two years; the GitLab profile manages public and private projects; the Reddit profile has many posts and comments; and the CMS profile is a shop owner with complete read/write access (Appendix A.3).

## Benchmark construction

Authors created 241 templates and 812 instantiated intents, averaging 3.3 instances per template (§3.1). Annotators were instructed to make tasks:

- high-level and multi-action;
- creative, often with constraints;
- template-based, with replaceable variables.

ChatGPT was available for inspiration, accompanied by descriptions of the sites and curated examples. The authors do not report how often generated suggestions were used.

Tasks fall into:

1. information seeking;
2. site navigation;
3. content/configuration operations.

## Annotation

Information-seeking reference answers were annotated twice by authors and an external annotator; disagreements went to a third annotator. Three JavaScript-proficient authors implemented the remaining evaluation programs. Difficult cases were discussed collectively, and annotators executed tasks while inspecting intermediate states (§3.2, p. 7).

## Outcome evaluation

For textual answers:

\[
r_{\text{info}}(\hat a,a^*)
\]

compares prediction \(\hat a\) with reference answer \(a^*\) using `exact_match`, `must_include`, or `fuzzy_match`.

For navigation and state-changing tasks:

\[
r_{\text{prog}}(s)
\]

checks intermediate or final website state through database queries, APIs, JavaScript selectors, URLs, and page content (§3.2, Table 1).

## Human evaluation

Five computer-science graduate students performed a sample containing one task from each of 170 templates. The paper does not specify allocation per participant, repetition across participants, or confidence intervals (§3.2).

## Model configurations

Appendix A.6 reports:

- GPT-3.5-Turbo-16K-0613;
- GPT-4-0613;
- Text-Bison-001;
- temperature \(1.0\);
- top-\(p=0.9\);
- at most 30 state transitions;
- termination after the same action is repeated more than three times on the same observation;
- termination after three consecutive invalid actions;
- ten extra retries for Text-Bison-001 to generate a valid action.

A GPT-3.5 condition at temperature 0.0 was separately reported for reproducibility (Table 5).

No hardware details, random seeds, confidence intervals, formal significance tests, or repeated-run aggregates are supplied.

# 8. Experiments / Analyses

## X1 — Human baseline

**Purpose:** Estimate human performance on representative task templates.

**Sample:** 170 tasks, one per template, performed by five computer-science graduate students.

**Metrics:** Mean task time and success rate overall and by task category.

**Results:** Mean time 110 seconds; information-seeking success 74.68%; other-task success 81.32%; overall success 78.24% (p. 7).

**Caveat:** Participants possess specialized computing knowledge, while Appendix A.5 notes that some tasks require domain knowledge not held by an average user.

## X2 — Main model comparison with CoT and UA hint

**Purpose:** Establish baseline performance under the prompt that explicitly teaches models to return “N/A” for impossible tasks.

**Conditions:** Two-shot prompting, accessibility-tree input, temperature 1.0, top-\(p=0.9\), up to 30 transitions.

**Results:** Text-Bison-001 5.05%, GPT-3.5 direct 6.41%, GPT-3.5 CoT 8.75%, and GPT-4 CoT 11.70% overall success (Table 2).

## X3 — Chain-of-thought comparison

For GPT-3.5 with the UA hint, direct prompting scored 6.41% and CoT scored 8.75%.

- **Analyst-derived absolute change:** \(8.75-6.41=2.34\) percentage points.
- **Analyst-derived relative change:** \(2.34/6.41\approx36.5\%\).

The prose calls this a “2.34% improvement,” but the table supports a 2.34-percentage-point absolute increase. No repeated-run uncertainty is provided.

Without the UA hint, GPT-3.5 direct scored 5.10% and CoT 6.16%, an analyst-derived increase of 1.06 percentage points.

## X4 — Unachievable-hint ablation

**Purpose:** Determine whether explicitly instructing the agent to stop on impossible tasks helps or harms performance.

For GPT-4 with CoT:

- with UA hint: overall 11.70%, achievable-task success 8.63%, unachievable-task success 77.78%;
- without UA hint: overall 14.41%, achievable-task success 13.02%, unachievable-task success 44.44%.

Analyst-derived changes after removing the hint:

- overall: +2.71 percentage points;
- achievable tasks: +4.39 points;
- unachievable tasks: −33.34 points.

The trajectory analysis reports that GPT-4 with the hint incorrectly labels 54.9% of feasible tasks as impossible (§5.1).

For GPT-3.5, removing the hint substantially lowers unachievable-task performance: both no-hint rows report 8.33% on unachievable tasks, versus 38.89% for direct and 58.33% for CoT with the hint.

## X5 — Consistency within templates

**Purpose:** Test whether success generalizes across different instances of the same task template.

The analysis considers 61 templates having at least one successful GPT execution under no-UA-hint conditions. GPT-4 achieves 100% success on only four templates; GPT-3.5 achieves 100% on none (§5.1, Table 3).

The authors infer that semantically related instances can differ sharply in operational difficulty—for example, forking one repository versus all repositories associated with an organization.

## X6 — Fuzzy-match validation

Appendix A.8 reports:

- manual checking of 40 examples, with 39 matching human judgment;
- 82 benchmark examples use GPT-4-based fuzzy evaluation;
- 49 of those 82, reported as 60%, involve dates or durations;
- two GPT-4 versions each scored 100% on 900 generated date examples and 900 generated duration examples (Table 6).

Analyst-derived manual agreement is \(39/40=97.5\%\).

## X7 — Temperature check

GPT-3.5 with CoT, no UA hint, and temperature 0.0 scored 6.28% (Table 5), compared with 6.16% in the corresponding main table at temperature 1.0.

**Analyst-derived difference:** +0.12 percentage points. The paper presents this as replication support, not a statistical comparison.

## X8 — Qualitative error analysis

Trajectory inspection identifies:

- premature stopping caused by the UA hint;
- observation bias toward the first superficially relevant information;
- failure to change page sections or result types;
- repeated typing despite visible evidence that a field is already filled;
- neglect of prior-action information;
- hallucinated answers, invalid-action loops, and step-limit exhaustion.

Figure 11 visually illustrates failure to select GitLab’s “Users” results and repeated entry of “DMV area.”

# 9. Results

| Major finding | Evidence and condition | Interpretation and qualification |
|---|---|---|
| Best model success was low | GPT-4 CoT, no UA hint: 14.41% (Table 2) | Supports the authors’ claim that the benchmark remains difficult for the tested agents |
| Humans substantially outperformed the best model | 78.24% versus 14.41% | Analyst-derived gap: 63.83 percentage points; the human sample consisted of CS graduate students |
| CoT helped GPT-3.5 modestly | 6.41% to 8.75% with UA hint | +2.34 percentage points; no variance or significance test supplied |
| UA hint traded feasible-task performance for impossible-task detection | GPT-4 achievable: 8.63% with hint vs 13.02% without; unachievable: 77.78% vs 44.44% | Prompt wording materially changes behavior, but the design does not isolate all causal mechanisms |
| GPT-4 often stopped too early | 54.9% of feasible tasks classified as impossible with the hint | Trajectory-based author observation |
| Performance was inconsistent across template variants | 4 of 61 templates at 100% for GPT-4; 0 for GPT-3.5 | Success on one instantiation does not imply robust execution of related instances |
| Fuzzy evaluator aligned closely with checked judgments | 39/40 manual cases; 100% on two generated 900-example format sets for both GPT-4 versions | Strong evidence for tested date/duration formatting, narrower than general semantic equivalence |
| Human errors were often partial or interpretive | 50% of recorded human failures fell into misinterpretation, incomplete answer, or incomplete execution categories | Remaining failures were described as more severely off-target |

The abstract says the 14.41% result is “significantly lower” than 78.24%, but the supplied paper does not report a significance test, uncertainty interval, or p-value. The numerical difference is plainly large; formal statistical significance is not demonstrated in the supplied text.

# 10. Figure-by-Figure Interpretation

## Figure 1 — WebArena overview

- **Type:** Architecture/concept diagram; no axes.
- **Content:** Web applications, tools, and knowledge resources feed observations to an AI agent; the agent sends actions back; validators inspect results and return functional success or failure.
- **Examples:** Spending on food in March 2023 and creating a Nolan-themed repository.
- **Conclusion supported:** WebArena integrates environment, agent interaction, and outcome-based validators.
- **Visual status:** Directly observable on p. 2.

## Figure 2 — Cross-site, long-horizon itinerary task

- **Type:** Three-stage workflow.
- **Stages:** Wikipedia museum search → map search and route optimization → GitLab README update.
- **Input:** A high-level request to visit Pittsburgh art museums from Schenley Park with minimal driving distance.
- **Output:** An ordered route stored in a named repository.
- **Conclusion supported:** Realistic tasks may require information retrieval, spatial reasoning, planning, and state-changing actions across sites.
- **Caveat:** The figure demonstrates task structure, not measured agent success.
- **Visual status:** Directly observable on p. 3.

## Figure 3 — Observation representations

- **Panels:** Screenshot, trimmed HTML/DOM tree, and trimmed accessibility tree.
- **Shared page content:** An e-commerce listing including product information, rating, reviews, price, and controls.
- **Visual encoding:** The screenshot is pixel-based; DOM exposes nested markup; accessibility tree exposes semantic roles, text, and properties.
- **Conclusion supported:** The same page can be presented to agents through different modalities.
- **Caveat:** The DOM and accessibility examples are intentionally truncated.
- **Visual status:** Directly observable on p. 4.

## Figure 4 — Action space

- **Type:** Two-column action table labeled as a figure.
- **Content:** Element operations, scrolling, tab management, and URL/history navigation.
- **Conclusion supported:** WebArena models a compound browser-control interface.
- **Notable omission:** `stop` appears in the baseline prompts but not in this displayed action-space list.
- **Visual status:** Directly readable on p. 5.

## Figure 5 — Example task categories

- **Type:** Category/example table labeled as a figure.
- **Categories:** Information seeking, site navigation, and content/configuration.
- **Examples:** Finding the latest shampoo purchase, comparing route times, locating merge requests, selecting the best-rated chair, posting about needing a car, and deleting reviews.
- **Conclusion supported:** The benchmark includes both read-only and state-changing tasks.
- **Visual status:** Directly readable on p. 5.

## Figure 6 — Intent distribution

- **Type:** Pie chart; no conventional x/y axes.
- **Visually readable shares:** E-commerce 23.0%, CMS 22.4%, GitLab 22.2%, Map 13.4%, Reddit 13.1%, Cross Site 5.9%.
- **Analyst-derived check:** Shares total 100.0%.
- **Conclusion supported:** Tasks are distributed across several sites, with the three largest categories roughly balanced.
- **Caveat:** “Cross Site” marks tasks requiring multiple websites, while the caption states all intents require multiple pages.
- **Visual status:** Directly observable on p. 16.

## Figure 7 — Reasoning-agent system prompt

- **Type:** Prompt text box.
- **Content:** Observation fields, allowed actions, completion syntax, homepage/password resources, validity rules, one-action-at-a-time constraint, step-by-step reasoning requirement, and UA hint.
- **Conclusion supported:** The reasoning agent is explicitly instructed to reason before acting and to return “N/A” for impossible tasks.
- **Visual status:** Directly readable on p. 18.

## Figure 8 — Reasoning-agent demonstrations

- **Type:** Two few-shot examples.
- **Examples:** Answering a product-price question and entering a restaurant-near-location search.
- **Distinguishing feature:** The assistant narrates reasoning before the formatted action.
- **Visual status:** Directly readable on p. 19.

## Figure 9 — Direct-agent system prompt

- **Type:** Prompt text box.
- **Difference from Figure 7:** It omits the instruction to reason step by step before the action.
- **Minor visible issue:** “To be successful…” is duplicated.
- **Visual status:** Directly readable on p. 20.

## Figure 10 — Direct-agent demonstrations

- **Type:** Two few-shot examples parallel to Figure 8.
- **Distinguishing feature:** Only the action is returned, with no reasoning prose.
- **Visual status:** Directly readable on p. 21.

## Figure 11 — GPT-4 failure examples

- **Left panel:** GitLab search results show zero projects but one user for “Facebook”; the agent fails to switch to the Users section for the task of forking Facebook repositories.
- **Right panel:** The accessibility text shows that “DMV area” is already present, yet the agent repeatedly types the same query.
- **Conclusion supported:** Agents may overlook granular observation content and fail to change strategy.
- **Visual status:** Directly observable on p. 22.

# 11. Table-by-Table Interpretation

## Table 1 — Evaluation implementations

The table contrasts:

- \(r_{\text{info}}\): textual-answer evaluation;
- \(r_{\text{prog}}\): programmatic state evaluation.

Examples demonstrate exact matching, multiple required substrings, fuzzy semantic matching, URL checking, and post-body checking. It shows that evaluators are task-specific and can combine several conditions. No statistical quantities appear.

## Table 2 — Main success-rate results

Columns are CoT, UA hint, model, overall success rate (SR), achievable-task success (\(SR_{AC}\)), and unachievable-task success (\(SR_{UA}\)); units are percentages.

Best model values:

- overall: GPT-4 CoT without UA hint, 14.41%;
- achievable tasks: the same condition, 13.02%;
- unachievable tasks: GPT-4 CoT with UA hint, 77.78%.

Humans score 78.24%, 77.30%, and 100.00%, respectively.

No error bars, confidence intervals, run counts, or statistical tests are shown.

## Table 3 — Distribution of within-template success

Despite being called “Table 3,” this is a histogram. The x-axis is within-template success rate and the y-axis is the number of templates. Colors distinguish GPT-3.5 direct, GPT-3.5 CoT, and GPT-4 CoT without UA hints.

Exact individual bar heights are difficult to read reliably at the supplied resolution. The accompanying text supplies the important exact facts: 61 included templates, four fully solved by GPT-4, none fully solved by GPT-3.5.

## Table 4 — Benchmark feature comparison

Rows compare Mind2Web, Form/QAWoB, MiniWoB++, WebShop, ALFRED, VirtualHome, AndroidEnv, and WebArena. Columns indicate dynamic interaction, realistic environment, diverse human tasks, and functional correctness.

WebArena is the only row marked positively on all four dimensions. These classifications are author-provided qualitative judgments; the supplied document does not independently validate each prior benchmark entry.

## Table 5 — Low-temperature GPT-3.5 result

GPT-3.5-Turbo-16K-0613 with CoT, no UA hint, and temperature 0.0 achieves 6.28% success. It provides a limited reproducibility comparison with the 6.16% temperature-1.0 row in Table 2.

## Table 6 — Fuzzy-match formatting accuracy

GPT-4-0613 and GPT-4-1106-preview each score:

- 100% on 900 date-format examples;
- 100% on 900 duration-format examples.

The table supports accuracy on generated equivalence judgments for these two answer types, not all possible semantic answers.

# 12. Diagram / Architecture Interpretation

The central system architecture appears in Figure 1.

1. **Task input:** A user provides a high-level natural-language intent.
2. **Observation:** The environment exposes URLs, tabs, and page content in a selected representation.
3. **Agent processing:** The agent interprets the current observation and history and chooses one browser action.
4. **Environment transition:** The action changes or navigates the deterministic local website state.
5. **Feedback:** A new observation is returned, creating an action–feedback loop.
6. **Termination:** The agent issues `stop`, optionally with a textual answer.
7. **Validation:** Task-specific evaluators inspect the answer, URL, page, API result, database, or intermediate state.
8. **Output:** The attempt is marked functionally successful or unsuccessful.

Figure 2 instantiates this architecture across multiple services, while Figure 3 shows the selectable observation encodings and Figure 4 lists the browser controls.

# 13. Equations and Mathematical Concepts

## Environment tuple

**Location:** p. 3, §2.1.

\[
\mathcal{E}=\langle S,A,O,T\rangle
\]

- \(S\): all possible environment states.
- \(A\): available agent actions.
- \(O\): observations presented to the agent.
- \(T\): deterministic transition function.
- Output: a formal description of the interactive environment.

## Transition function

\[
T:S\times A\rightarrow S
\]

Given a state and an action, the underlying websites determine the next state. “Deterministic” means that the same relevant state and action are intended to produce the same next state.

## Agent decision process

The extracted text states that \(a_t\) depends on the intent \(i\), current observation \(o_t\), and previous action and observation histories. The histories appear OCR-flattened as forms resembling \(a^{t-1}_1\) and \(o^{t-1}_1\). They denote sequences from the first step through \(t-1\), but the exact typesetting should be treated cautiously.

## Reward over a trajectory

\[
r(a^T_1,s^T_1)
\]

This evaluates whether the complete action sequence and encountered states satisfy the intent. It is not presented as a learned optimization loss; it is an evaluation function.

## Information-answer scoring

\[
r_{\text{info}}(\hat a,a^*)
\]

- \(\hat a\): agent’s predicted textual answer.
- \(a^*\): annotated reference answer.
- Output: binary success under exact, required-content, or fuzzy matching.

Table 1’s caption reverses argument order typographically in one place, displaying \(r_{\text{info}}(a^*,\hat a)\), whereas §3.2 gives \(r_{\text{info}}(\hat a,a^*)\). Because the described matching operations are conceptually directional for `must_include`, this is a notation-order inconsistency, although the implementation examples make the intended prediction-versus-reference roles clear.

## Programmatic scoring

\[
r_{\text{prog}}(s)
\]

This checks whether relevant website states possess properties required by the intent. The exact internal mathematical definition is not supplied; Table 1 provides implementation examples.

# 14. Interpretation and Discussion

The results answer the paper’s objectives chiefly by showing that WebArena discriminates strongly between current baseline agents and skilled humans. The benchmark is difficult enough that even the best tested agent completes fewer than one in six tasks.

The stopping analysis reveals a genuine policy tradeoff. Telling GPT-4 explicitly to recognize impossible tasks improves impossible-task detection but also makes the model abandon many achievable tasks. Removing the instruction increases overall success because gains on feasible tasks outweigh losses on impossible ones.

The within-template analysis indicates brittleness rather than stable acquisition of a reusable procedure. Similar high-level semantics can conceal different numbers of repositories, pages, or repeated operations. The tested agents often solve only one instantiation rather than the entire family.

The qualitative errors align with the authors’ proposed capability gaps:

- insufficient exploration;
- weak verification;
- poor tracking of prior actions and fine-grained page state;
- limited recovery from unsuccessful behavior;
- action repetition.

However, the causal explanation involving dialogue-oriented pretraining remains a hypothesis. The paper analyzes outputs and trajectories but does not experimentally manipulate pretraining data or fine-tuning objectives.

Two wording issues merit caution:

- “significantly lower” is used without a reported significance test.
- “2.34% improvement” is numerically a 2.34-percentage-point increase from 6.41% to 8.75%.

# 15. Contributions and Novelty

## Conceptual contribution

The paper frames realistic web-agent evaluation around functional outcomes rather than matching a prescribed action trace.

## System contribution

It provides a standalone collection of functional, locally hosted websites spanning multiple common web domains and supporting tools.

## Benchmark contribution

It supplies 812 long-horizon tasks based on 241 templates, including information seeking, navigation, content modification, configuration, and intentionally unachievable requests.

## Evaluation contribution

It implements task-specific validators that inspect textual answers and website state through exact matching, required-content checks, model-based semantic matching, URLs, APIs, JavaScript, and databases.

## Data contribution

The environment includes substantial sampled content: approximately 90,000 products, 127,390 forum posts, 661,781 forum users, and 300 repositories, among other resources.

## Reproducibility contribution

Dockerized services and restart-based resets are designed to restore deterministic initial conditions.

## Empirical contribution

The authors establish model and human baselines, conduct a UA-hint ablation, analyze consistency across template variants, validate part of the fuzzy evaluator, and document characteristic failure modes.

# 16. Limitations

## Authors’ stated limitations

- Map data is limited to the northeastern United States because of storage constraints (Appendix A.1).
- Docker restart may add a small but non-negligible evaluation-time cost (Appendix A.2).
- Human performance may vary with participant demographics and domain-specific knowledge; the sampled participants may not represent average users (Appendix A.5).
- The authors characterize baseline agents as lacking exploration and failure recovery, while presenting these as capability limitations rather than limitations of the benchmark itself (§5.1).
- Some tasks are impossible because of missing evidence, permissions, or unsupported functionality (§3.2); this is intentional benchmark design but constrains the attainable behaviors.
- The paper notes that websites use sampled rather than complete live-world data (§3.1; Appendix A.1).

## Additional evidence-based analyst observations

- Only five human participants were used, and participant/task allocation is insufficiently described for estimating inter-person variability.
- Model results lack confidence intervals, repeated-run summaries, and formal significance tests despite stochastic temperature 1.0.
- Task authors, reference annotators, and evaluator implementers substantially overlap, which may align the benchmark with its creators’ expectations.
- ChatGPT was used for task inspiration, but the extent and influence of this assistance are not quantified.
- The fuzzy-match validation is strongest for generated date and duration formatting; broader semantic equivalence is supported by only 40 manually checked cases.
- Functional evaluators can validate only encoded properties. A task may appear successful according to the validator while violating an unencoded aspect of user intent.
- The environment’s realism is bounded by selected domains, sampled content, simulated users, a regional map, and a static Wikipedia cutoff.
- The tested model set and prompts establish baselines, not an exhaustive comparison of agent architectures.
- The public artifacts were not supplied here, so claims about installation, reset fidelity, and executable reproducibility cannot be independently checked in this analysis.

# 17. Threats to Validity

## Internal validity

Prompt format, UA wording, temperature, early-termination rules, and action-parser behavior can affect success independently of underlying reasoning capability. Only selected ablations are reported.

## Construct validity

Task success is represented by binary validators. These capture functional correctness better than exact action matching, but may not measure efficiency, safety, user satisfaction, unintended side effects, or partially correct execution.

## Statistical conclusion validity

No uncertainty estimates, statistical tests, or repeated-run distributions are supplied. Consequently, small differences between model conditions should not be treated as stable rankings. Large raw gaps are descriptively clear but not formally tested.

## External validity

The environment covers four main application categories and selected tools. Results do not directly establish performance on the entire live web, different languages, inaccessible sites, CAPTCHAs, rapidly changing interfaces, or other user roles.

## Ecological validity

The use of realistic software and data improves resemblance to ordinary websites. Conversely, self-hosting removes live-web variability and operational barriers, and participants know they are completing benchmark tasks.

## Reproducibility

Docker images, reset scripts, trajectories, prompts, and public resources are positive reproducibility provisions. Reproducibility is nevertheless dependent on artifacts not included in the supplied document and on externally hosted model versions/services.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed or motivated by the authors

- Develop more robust and effective autonomous agents for WebArena (§§1, 5, 7).
- Improve active exploration and failure recovery (p. 2; Appendix A.10).
- Investigate memory components that reuse successful strategies across tasks (§5.1).
- Apply hierarchical planning, program-like execution, search, backtracking, self-correction, and observation summarization in this more demanding environment (§6).

## B. Additional open questions

- How stable are reported model results across repeated runs and model-version changes?
- How well do the evaluators capture all semantic constraints in complex intents?
- Do agents optimized for WebArena generalize to unseen website software, layouts, and data?
- How does performance vary across user roles, accessibility modes, screenshots, DOM input, and multi-modal input?
- What fraction of failure comes from planning, perception, action formatting, tool use, memory, or evaluator mismatch?
- How would ordinary nontechnical users perform compared with the sampled computer-science graduate students?
- Can partial-credit metrics provide more diagnostic information without weakening functional evaluation?
- What are the safety implications of agents capable of purchases, deletions, account changes, and content publication?

# 19. Terminology and Notation Glossary

| Term | Meaning in this paper |
|---|---|
| WebArena | The authors’ self-hosted web environment and associated benchmark |
| Agent | A system that observes the browser and chooses actions to satisfy an intent |
| Intent | A high-level natural-language task request |
| LLM | Large language model |
| CoT | Chain-of-thought: generating reasoning before the next action |
| UA hint | Unachievable-task hint instructing the model to stop and answer “N/A” when completion seems impossible |
| Functional correctness | Whether the requested outcome was achieved, regardless of the exact action path |
| Long horizon | Requiring many dependent interaction steps |
| DOM | Document Object Model, the structured HTML representation of a page |
| Accessibility tree | A compact semantic representation of page elements, roles, text, and properties |
| CMS | Content management system |
| POI | Point of interest on a map |
| In-context learning | Conditioning a model through examples in its prompt |
| Template | A general task pattern containing replaceable variables |
| Instantiated intent | A concrete task produced by filling a template’s variables |
| Locator | Code that retrieves the page, URL, database state, or content relevant to evaluation |
| `exact_match` | Returns success only for an identical expected answer |
| `must_include` | Requires specified content to appear in the prediction or located state |
| `fuzzy_match` | Uses GPT-4 to judge semantic equivalence |
| SR | End-to-end task success rate |
| \(SR_{AC}\) | Success rate on achievable tasks |
| \(SR_{UA}\) | Success rate on unachievable tasks |
| \(S\) | Environment state space |
| \(A\) | Agent action space |
| \(O\) | Observation space |
| \(T\) | Deterministic state-transition function |
| \(a_t\) | Action selected at time step \(t\) |
| \(o_t\) | Observation at time step \(t\) |
| \(a^*\) | Annotated reference answer |
| \(\hat a\) | Agent-predicted answer |
| \(r_{\text{info}}\) | Textual-answer evaluation function |
| \(r_{\text{prog}}\) | Programmatic website-state evaluator |
| top-\(p\) | A generation-sampling parameter; the paper reports 0.9 but does not define it |
| Temperature | A generation parameter; 1.0 is used to encourage exploration, with one 0.0 check |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Benchmark size | 812 | intents/tasks | Full benchmark | Author-reported | p. 5, §3.1 |
| Task templates | 241 | templates | Full curation | Author-reported | p. 5, §3.1 |
| Average instances per template | 3.3 | instances/template | Full benchmark | Author-reported | p. 5, §3.1 |
| Browser-history examples analyzed | approximately 200 | examples | Website selection | Author-reported | p. 3, §2.2 |
| Human evaluation tasks | 170 | tasks | One per sampled template | Author-reported | p. 7 |
| Human participants | 5 | people | CS graduate students | Author-reported | p. 7 |
| Human mean time | 110 | seconds/task | Human evaluation | Author-reported | p. 7 |
| Human overall success | 78.24 | % | Sampled human baseline | Author-reported | p. 7; Table 2 |
| Human information-seeking success | 74.68 | % | Human baseline | Author-reported | p. 7 |
| Human other-task success | 81.32 | % | Human baseline | Author-reported | p. 7 |
| Text-Bison-001 success | 5.05 | % | CoT + UA hint | Author-reported | p. 8, Table 2 |
| GPT-3.5 direct success | 6.41 | % | UA hint | Author-reported | p. 8, Table 2 |
| GPT-3.5 CoT success | 8.75 | % | UA hint | Author-reported | p. 8, Table 2 |
| GPT-4 CoT success | 11.70 | % | UA hint | Author-reported | p. 8, Table 2 |
| Best GPT-4 success | 14.41 | % | CoT, no UA hint | Author-reported | p. 8, Table 2 |
| Best-model/human gap | 63.83 | percentage points | 78.24 − 14.41 | Analyst-derived | Table 2 |
| GPT-3.5 CoT gain with hint | 2.34 | percentage points | 8.75 − 6.41 | Analyst-derived | Table 2 |
| Relative GPT-3.5 CoT gain | approximately 36.5 | % | 2.34 / 6.41 | Analyst-derived | Table 2 |
| Feasible tasks wrongly called impossible | 54.9 | % | GPT-4 with UA hint | Author-reported | p. 8, §5.1 |
| GPT-4 no-hint achievable success | 13.02 | % | CoT | Author-reported | Table 2 |
| GPT-4 no-hint unachievable success | 44.44 | % | CoT | Author-reported | Table 2 |
| Templates in consistency analysis | 61 | templates | At least one GPT success | Author-reported | p. 8, §5.1 |
| Templates fully solved by GPT-4 | 4 | templates | No-UA-hint analysis | Author-reported | p. 8, §5.1 |
| Templates fully solved by GPT-3.5 | 0 | templates | Same analysis | Author-reported | p. 8, §5.1 |
| Products | approximately 90,000 | products | Shopping site | Author-reported | p. 15, Appendix A.1 |
| Product categories | over 300 | categories | Shopping site | Author-reported | p. 15, Appendix A.1 |
| Subreddits | 95 | forums | Reddit replica | Author-reported | p. 15, Appendix A.1 |
| Forum posts | 127,390 | posts | Reddit replica | Author-reported | p. 15, Appendix A.1 |
| Forum users | 661,781 | users | Reddit replica | Author-reported | p. 15, Appendix A.1 |
| GitLab repositories | 300 | repositories | Development site | Author-reported | p. 15, Appendix A.1 |
| GitLab accounts | over 1,000 | accounts | At least one commit | Author-reported | p. 15, Appendix A.1 |
| E-commerce share | 23.0 | % of intents | Intent distribution | Visually readable | p. 16, Figure 6 |
| CMS share | 22.4 | % | Intent distribution | Visually readable | p. 16, Figure 6 |
| GitLab share | 22.2 | % | Intent distribution | Visually readable | p. 16, Figure 6 |
| Map share | 13.4 | % | Intent distribution | Visually readable | p. 16, Figure 6 |
| Reddit share | 13.1 | % | Intent distribution | Visually readable | p. 16, Figure 6 |
| Cross-site share | 5.9 | % | Intent distribution | Visually readable | p. 16, Figure 6 |
| Maximum transitions | 30 | state transitions | Baseline runs | Author-reported | p. 17, Appendix A.6 |
| Main temperature | 1.0 | parameter value | Baseline runs | Author-reported | p. 17, Appendix A.6 |
| top-\(p\) | 0.9 | parameter value | Baseline runs | Author-reported | p. 17, Appendix A.6 |
| Temperature-0 GPT-3.5 success | 6.28 | % | CoT, no UA hint | Author-reported | p. 17, Table 5 |
| Manually checked fuzzy cases | 40 | examples | Evaluator validation | Author-reported | p. 17, Appendix A.8 |
| Agreement in checked cases | 39/40 (97.5%) | cases / derived % | Human comparison | Author-reported / Analyst-derived | p. 17, Appendix A.8 |
| Fuzzy-evaluated benchmark items | 82 | examples | Benchmark | Author-reported | p. 17, Appendix A.8 |
| Date/duration fuzzy items | 49 (60%) | examples (%) | Among 82 | Author-reported | p. 17, Appendix A.8 |
| Date-format judge accuracy | 100 | % | 900 examples, both GPT-4 versions | Author-reported | p. 17, Table 6 |
| Duration-format judge accuracy | 100 | % | 900 examples, both GPT-4 versions | Author-reported | p. 17, Table 6 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| WebArena combines realistic interaction, reproducibility, diverse tasks, and functional evaluation | Local functional sites, Docker delivery, benchmark, programmatic validators | Figures 1–5; Table 4 | §§2–3; Appendix A.1–A.2 | Strong within the described design; executable artifacts not supplied here |
| Current baseline agents struggle with the benchmark | Best model SR 14.41% | X2/X4; Table 2 | p. 8, §5 | Strong descriptive evidence for tested models and prompts |
| Humans outperform tested agents | 78.24% human versus 14.41% best model | X1/X2; Table 2 | pp. 7–8 | Large descriptive gap; small specialized human sample and no statistical test |
| CoT improves GPT-3.5 performance | 6.41% direct versus 8.75% CoT with UA hint | X3; Table 2 | p. 8 | Descriptive 2.34-point difference; no uncertainty |
| UA hint causes premature stopping on feasible tasks | 54.9% false impossibility classification; achievable SR rises when hint removed | X4; Table 2 | p. 8, §5.1 | Good ablation evidence for this prompt configuration |
| Models are inconsistent across related instances | GPT-4 fully solves only 4 of 61 templates; GPT-3.5 none | X5; Table 3 | pp. 8–9 | Strong descriptive evidence among templates with at least one success |
| Outcome evaluation supports multiple valid action paths | Validators inspect answers and resulting state rather than reference traces | Table 1 | pp. 2, 6–7 | Strong methodological evidence; validator completeness remains task-dependent |
| Fuzzy matching is accurate for tested formats | 39/40 manual agreement; 100% on date/duration format sets | X6; Table 6 | p. 17 | Strong for tested formatting cases, limited for unrestricted semantics |
| Observation handling is a major failure source | Agents select wrong result sections, repeat filled queries, and latch onto superficial information | Figure 11; X8 | p. 22, Appendix A.10 | Qualitative trajectory evidence; prevalence not quantified |
| More exploration and recovery capability is needed | Low success and observed failure modes | X2, X4, X8 | pp. 2, 8–9, 22 | Reasonable author interpretation; causal mechanisms not isolated |

# 22. Very Simple Explanation

Imagine giving a computer a request like, “Find all the art museums in Pittsburgh, work out a short driving route, and save it in my project.” A simple test might only ask whether the computer clicked the expected buttons. WebArena instead gives the computer working websites and checks whether the requested result actually exists at the end.

The researchers built local versions of shopping, discussion, programming, map, and management websites. They then wrote 812 tasks that often require many steps. Some tasks only ask for information; others ask the agent to change something, such as creating a post or editing a repository.

The tested AI agents were not reliable. The strongest GPT-4 setup succeeded on 14.41% of tasks, while the sampled humans succeeded on 78.24%. Agents often stopped too early, focused on the first related-looking information, repeated actions, or failed to notice small but important details on the page.

The paper’s main message is therefore: realistic web work is much harder than producing a plausible answer or clicking through a toy interface. WebArena gives researchers a repeatable way to measure whether future agents truly finish such work.

# Completeness Audit

## Inventory-based coverage

| Item | Inspected? | Represented? | Status | Notes |
|---|---:|---:|---|---|
| Title, authors, venue | Yes | Yes | Fully represented | WebArena; ICLR 2024; full author list visible on p. 1 |
| Abstract | Yes | Yes | Fully represented | Incorporated into orientation, results, and contributions |
| §1 Introduction | Yes | Yes | Fully represented | Problem, gap, contributions, and headline results covered |
| §2 WebArena environment | Yes | Yes | Fully represented | System goals and standalone design covered |
| §2.1 Formal control model | Yes | Yes | Fully represented | Environment tuple, histories, transitions, and reward covered |
| §2.2 Website selection | Yes | Yes | Fully represented | Browser-history analysis, domains, tools, and resources covered |
| §2.3 Observation space | Yes | Yes | Fully represented | URL, tabs, DOM, screenshot, accessibility tree, viewport covered |
| §2.4 Action space | Yes | Yes | Fully represented | All listed actions and element addressing covered |
| User-role simulation in main text | Yes | Yes | Fully represented | Expanded using Appendix A.3 |
| §3 Benchmark suite | Yes | Yes | Fully represented | Size, categories, construction, and evaluation covered |
| §3.1 Intent collection | Yes | Yes | Fully represented | Guidelines, templating, ChatGPT inspiration, counts covered |
| §3.2 Evaluation annotation | Yes | Yes | Fully represented | All evaluator types, unachievable tasks, annotation, humans covered |
| §4 Baseline web agents | Yes | Yes | Fully represented | Models, direct/CoT prompts, UA hint, observations covered |
| §5 Results | Yes | Yes | Fully represented | All Table 2 conditions and principal claims covered |
| §5.1 Analysis | Yes | Yes | Fully represented | Stopping and template consistency analyses covered |
| §6 Related work | Yes | Yes | Represented in compressed form | Categories and author positioning retained; individual citations compressed |
| §7 Conclusion | Yes | Yes | Fully represented | Main conclusions integrated |
| Acknowledgements | Yes | Partly | Represented in compressed form | Funding and named thanks are non-methodological; existence accounted for |
| References, pp. 10–14 | Yes, text | Partly | Inspected but deliberately omitted as repetitive/non-substantive | Used only to understand paper positioning; bibliography not reproduced |
| Appendix A.1 | Yes | Yes | Fully represented | Website implementations and dataset scale covered |
| Appendix A.2 | Yes | Yes | Fully represented | Docker delivery and reset covered |
| Appendix A.3 | Yes | Yes | Fully represented | Roles, permissions, histories, authentication covered |
| Appendix A.4 | Yes | Yes | Fully represented | Figure 6 distribution covered |
| Appendix A.5 | Yes | Yes | Fully represented | Human-domain-knowledge qualification covered |
| Appendix A.6 | Yes | Yes | Fully represented | Models, sampling, limits, retries, and temperature check covered |
| Appendix A.7 | Yes | Yes | Represented in compressed form | Fuzzy prompt’s role, variables, N/A rule, and binary scoring covered |
| Appendix A.8 | Yes | Yes | Fully represented | Manual and generated-format validations covered |
| Appendix A.9 | Yes | Yes | Fully represented | Reasoning/direct prompts and demonstrations covered |
| Appendix A.10 | Yes | Yes | Fully represented | Observation bias and interpretation failures covered |
| Figure 1 | Yes, visual | Yes | Fully represented | Architecture and validation loop |
| Figure 2 | Yes, visual | Yes | Fully represented | Multi-site itinerary workflow |
| Figure 3 | Yes, visual | Yes | Fully represented | Three observation modes |
| Figure 4 | Yes, visual | Yes | Fully represented | Action list |
| Figure 5 | Yes, visual | Yes | Fully represented | Intent categories |
| Figure 6 | Yes, visual | Yes | Fully represented | All labeled percentages transcribed |
| Figure 7 | Yes, visual | Yes | Fully represented | Reasoning prompt |
| Figure 8 | Yes, visual | Yes | Fully represented | Reasoning examples |
| Figure 9 | Yes, visual | Yes | Fully represented | Direct prompt |
| Figure 10 | Yes, visual | Yes | Fully represented | Direct examples |
| Figure 11 | Yes, visual | Yes | Fully represented | Two failure cases |
| Table 1 | Yes, visual | Yes | Fully represented | Evaluator examples |
| Table 2 | Yes, visual | Yes | Fully represented | All success-rate rows represented |
| Table 3/histogram | Yes, visual | Yes | Represented with uncertainty | Exact bar heights not confidently readable; exact prose facts retained |
| Table 4 | Yes, visual | Yes | Fully represented | All benchmark dimensions and central comparison covered |
| Table 5 | Yes, visual | Yes | Fully represented | Temperature-0 result covered |
| Table 6 | Yes, visual | Yes | Fully represented | Both datasets and model versions covered |
| Major equations/formalism | Yes | Yes | Fully represented with OCR caution | No numbered equation environment or theorem is present |
| Algorithms/pseudocode | Yes | Yes | Not present | No formal algorithms found |
| Theorems/lemmas/propositions | Yes | Yes | Not present | None found |
| Explicit research questions | Yes | Yes | Not formally present | Two analysis questions identified without manufacturing formal RQs |
| Formal hypotheses | Yes | Yes | Not formally present | Informal author hypotheses separated |
| Major experiments/analyses X1–X8 | Yes | Yes | Fully represented | Human, model, CoT, UA, consistency, fuzzy, temperature, errors |
| Major contributions | Yes | Yes | Fully represented | Conceptual, system, benchmark, evaluation, data, reproducibility, empirical |
| Author-stated limitations | Yes | Yes | Fully represented | Kept separate from analyst observations |
| Supplied supplementary material | N/A | N/A | Missing from supplied material | None supplied |
| External code/data/environment/videos | No | Yes as absent | Missing from supplied material | Referenced but not inspected |

## Missing or inaccessible material

- Pages 10, 11, and 13–15 were not visually rendered. Their extracted text was readable, but page typography and any non-textual details could not be visually verified. Pages 10–14 are principally references; p. 15 begins Appendix A.
- The public code, datasets, Docker images, reset scripts, execution trajectories, video demonstrations, website manuals, and hosted project resources were not supplied.
- No separate supplementary files were supplied.
- Exact histogram bar heights in Table 3 cannot be confidently recovered from the supplied resolution; the paper’s explicit prose values were used.
- Hardware and infrastructure details for model execution are not specified beyond acknowledgement of computational support.

## Uncertain interpretations

- Time-indexed history notation on p. 3 is vulnerable to superscript/subscript extraction errors.
- The argument order of \(r_{\text{info}}\) differs between §3.2 and Table 1’s caption.
- The term “significantly lower” lacks a reported statistical test.
- The phrase “2.34% improvement” is best read numerically as 2.34 percentage points.
- Table 3 is visually a histogram despite being labeled a table.
- Figure 4 omits the completion action later included in the prompts; the paper does not explain whether completion is considered outside the browser action space.
- The precise division of 170 human tasks among five participants is not supplied.

## Deliberately compressed material

- The full bibliography was not reproduced; its major thematic categories are represented in the related-work discussion.
- Acknowledgement names, grant language, and government disclaimers were compressed because they do not alter the method or findings.
- Full prompt wording in Figures 7–10 was summarized structurally rather than repeated verbatim.
- Repetitive examples of URL, JavaScript, and required-string validators were consolidated after their logic was explained.
- Website framework provenance was summarized while preserving all substantive dataset sizes and implementation choices.

## Potential omissions

No known substantive section, subsection, figure, table, equation, experiment, contribution, or author-stated limitation in the supplied 22-page document is absent from the analysis. The only materially unresolved items are those explicitly listed above as visually unrendered, externally referenced but unsupplied, underspecified by the authors, or unreadable at exact graphical resolution.