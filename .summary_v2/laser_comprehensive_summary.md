# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible page range | Pages 1–12 |
| Apparently missing pages | None |
| Native/extracted text | Available for all 12 pages |
| Visually rendered pages | 1, 2, 3, 4, 6, 8, 10, 11, and 12 |
| Pages not visually rendered | 5, 7, and 9; assessed from supplied page-labeled text only |
| Figures visually inspectable | Yes—all four numbered figures appear on rendered pages 1, 4, and 8 |
| Tables visually inspectable | Yes—all eight numbered tables appear on rendered pages 3 and 10–12 |
| Equations | No displayed or numbered equations; only inline formal notation in §2.1 |
| Algorithms/pseudocode | No formal algorithm block; the iterative procedure and state-action mapping are described in prose and Table 8 |
| Appendices | Appendices A–E are present in the supplied 12 pages |
| Supplementary files | None supplied or explicitly referenced as separate supplementary material |
| Embedded images | Figure 1, Figure 2, and the two case-study screenshots in Figures 3–4 |
| OCR needed | No; native/extracted text was supplied |
| OCR-sensitive concerns | Minor typography and URL/footnote alignment only; no mathematical OCR issue affecting the method |
| Important limitation | The analysis can visually verify all numbered figures and tables, but cannot visually verify the formatting of pages 5, 7, and 9. References are compressed rather than individually analyzed because they are bibliographic rather than substantive evidence. |

The supplied text appears to contain the complete paper, including references and Appendices A–E. Page 9 contains only the headings for Appendix D and Appendix E plus the license statement; Appendix D’s substantive prompt tables follow on pages 10–12.

# 1. Plain-Language Orientation

This paper introduces **LASER**, short for **LLM Agent with State-Space ExploRation**. It is an agent based on a large language model (LLM) that searches an online shop for a product matching a user’s requirements.

The problem is that earlier web agents were commonly shown examples of successful, forward-moving action sequences. Such examples teach what to do when everything goes correctly, but not necessarily how to recover after inspecting the wrong product, reaching an unhelpful results page, or attempting an action unavailable on the current page. The authors also argue that giving an agent every possible action everywhere creates avoidable opportunities for invalid actions (§1, pp. 1–2).

LASER instead divides shopping navigation into a small set of states—principally **Search**, **Results**, **Item**, and **Finish**—and gives the model:

- an instruction tailored to its current state;
- only the actions permitted in that state;
- the current page observation;
- its past thoughts and actions; and
- a memory of rejected products that can serve as backups.

This creates explicit forward and backward paths. For example, an agent can move from Results to an Item, return to Results if the product is wrong, or return to Search if the retrieved result set is poor (Figure 1; §2.2–2.4).

The authors evaluate LASER on 500 WebShop test instructions and transfer it without method modification to 100 instructions on Amazon.com. On WebShop, LASER reports a **50.0% success rate and 75.6 reward**, compared with the strongest listed non-human baseline, WebGUM, at **45.0% and 67.5** (Table 1, p. 3). On Amazon.com, it reports **62.0% success and 85.4 reward**, close to the human reference of **65.0% and 88.2** (Table 2, p. 3).

The central contribution is therefore not a newly trained language model. It is a **control structure for an LLM agent**: represent web navigation as movement through explicitly defined states, attach an appropriate local action space and instructions to each state, and permit backtracking.

# 2. Document Roadmap

| Section | Pages | Role |
|---|---:|---|
| Abstract | 1 | States the problem, state-space solution, evaluation environments, and headline claim |
| §1 Introduction | 1–2 | Motivates recovery from mistakes and state-specific actions |
| §2 Methods | 2–3 | Formalizes the task and describes states, actions, thought/action iteration, history, and backup memory |
| §3 Experiments | 3 | Defines WebShop and Amazon.com evaluations, metrics, model, and baselines |
| §4 Results | 3–4 | Presents overall results, ablations, trajectory-length analysis, and model-transfer analysis |
| §5 Conclusions | 4 | Restates the contribution and findings |
| Limitations | 5 | Discusses domain scope, manual state design, deployment risk, and future work |
| References | 5–7 | Bibliographic sources |
| Appendix A | 7 | Related-work positioning |
| Appendix B | 7–8 | Dataset, metrics, transition budget, Amazon transfer, and human-evaluation details |
| Appendix C | 8 | Manual categorization of 30 development-set errors |
| Appendix D | 9–12 | Exact state prompts, thought-to-action prompt, and action mapping in Tables 4–8 |
| Appendix E | 9 | License information |

The main paper gives the conceptual and empirical argument. The appendices materially extend it: Appendix B supplies evaluation details, Appendix C exposes failure modes, and Appendix D makes the state-specific control design concrete.

# 3. Background and Context

A **large language model (LLM)** generates or processes language. In an interactive agent, it can repeatedly inspect an environment, reason about what to do, and select an action.

A **web-navigation agent** acts on a website to satisfy an instruction. In this paper the instruction might request a product of a particular type, color, size, and maximum price.

An **observation** is the page representation available after an action. An **action trajectory** is the sequence of observations, reasoning steps, and actions taken through the environment.

An **in-context example** is a worked example placed in the model’s prompt rather than used to change the model’s weights. An **oracle trajectory** is a demonstration containing the correct action at each step. According to the authors, such successful examples insufficiently demonstrate recovery from unexpected mistakes (§1, p. 1).

A **state space** is a structured set of situations an agent may occupy. LASER defines states according to differences in the structure of the current observation (§2.3, p. 2). A product-search page and product-detail page are therefore different states, even though many concrete pages can instantiate each one.

An **action space** is the set of actions available to an agent. LASER uses a local, state-specific action space rather than a single global one (§2.4).

**Backtracking** means moving to an earlier state after an unproductive choice. It is central to LASER’s recovery mechanism.

**Function calling** gives the model a predefined list of callable actions with descriptions and arguments. LASER uses GPT-4-0613 function calling for action selection (§3 and Appendix B).

**Zero-shot** means the prompt contains no worked input-output demonstration; **one-shot** means it contains one. LASER’s standard condition uses state-specific instructions with no worked trajectory (§4.1).

**Sim-to-real transfer** here means designing/evaluating in the simulated WebShop environment and then applying the same agent method to Amazon.com (§3, p. 3). The webpages are converted into the WebShop-style representation (Appendix B, p. 7).

# 4. Research Problem and Gap

## Existing problem

LLM agents must execute multi-step web tasks under uncertainty. They can inspect unsuitable items, retrieve poor results, repeat actions, or attempt controls that do not exist on the current page (§1; §4).

## Shortcomings attributed to previous approaches

The authors identify two main shortcomings:

1. **Forward-only demonstrations.** Prior prompting approaches often provide a few correct trajectories. These show the correct action at every demonstrated step but do not cover unexpected test-time errors or recovery paths (§1, p. 1).

2. **Global action spaces.** Prior approaches may define all actions at the beginning or expect the LLM to infer them. The model can consequently attempt invalid actions for its current situation (§1; §2.4).

The authors also argue that covering every contingency with examples would be costly or unrealistic.

## Research gap

The paper targets a web-agent formulation that:

- handles unfamiliar situations without exhaustive trajectory demonstrations;
- supports backward as well as forward transitions;
- restricts action choice to valid actions for the current page structure; and
- supplies concise, reusable procedural knowledge through state-specific instructions.

## Motivation

Reliable recovery matters because a multi-step agent’s first decision will not always be correct. Invalid or repeated actions can waste the limited interaction budget and prevent an output (§4, p. 3).

## Scope

The implemented and evaluated scope is **finding a target shopping item**. It does not cover broader commerce tasks such as tracking orders or inspecting order history (Limitations, p. 5).

# 5. Research Questions / Objectives / Hypotheses

The paper does not state formally numbered research questions or preregistered hypotheses.

## Explicit objectives

- Formulate interactive web navigation as state-space exploration (§1–2).
- associate each state with specific instructions and permissible actions (§2.3–2.4);
- allow recovery and backtracking without exhaustive in-context trajectories;
- evaluate LASER on WebShop and Amazon.com (§3);
- analyze the effects of demonstrations, function calling, trajectory length, and the underlying LLM (§4.1);
- study common failure modes (Appendix C).

## Informal questions implicit in the experiments

These are analyst-organized objectives, not author-numbered research questions:

- **RQ1:** Does LASER outperform prior WebShop agents?
- **RQ2:** Does it transfer to Amazon.com and approach the human reference?
- **RQ3:** Does a one-shot example improve or harm standard zero-shot LASER?
- **RQ4:** Does structured function calling improve action selection?
- **RQ5:** How does performance change with trajectory length?
- **RQ6:** Does the framework remain useful with a weaker, non-chat LLM?
- **RQ7:** What kinds of errors remain?

## Hypotheses

No formal hypotheses are declared. The authors do express expectations that state-specific control should reduce invalid actions, permit recovery, and improve performance. In §4.1 they additionally hypothesize, after observing the one-shot result, that the example can distract an agent that already understands the task.

# 6. Assumptions / Threat Model

This is not a cybersecurity paper and contains no attacker threat model. Its applicable system and environmental assumptions are:

- The environment can be manually partitioned into a small set of structurally distinct states (§2.3).
- A state-specific observation template and instruction can adequately describe each state.
- The agent can be restricted to a known set of permissible actions (§2.4).
- WebShop observations expose button-like actions and product information in text form.
- Amazon pages can be converted into the same representation used by WebShop (Appendix B).
- A product can be evaluated against a target instruction using item category, attributes, options, and price.
- The interaction has a finite transition budget: at most 15 transitions, with forced backup selection after 13 if Finish has not been reached (Appendix B, p. 7).
- The LLM’s history of thoughts/actions can be retained as input (§2.2).
- For the real website, the agent must not execute an irreversible purchase: it stops when it chooses Buy (Limitations, p. 5).

Trusted components implicitly include the environment interface, page-to-observation conversion, search engine, action executor, evaluation functions, and human Amazon annotations. Their reliability is not independently tested in the supplied paper.

# 7. Methodology

## 7.1 Task formulation

Given a web environment \(E\), instruction \(I\), and initial observation \(O_0\), the agent performs actions \(\{a_0,a_1,\ldots,a_n\}\). Executing \(a_i\) produces a new observation \(O_i\). \(S\) denotes the stopping state, after which the output is compared with the target (§2.1, p. 2).

## 7.2 State design

A state is defined by the **structure** of the observation, not its particular product content (§2.3). The authors manually categorize the possible structures and write for each:

- a generic observation layout with placeholders;
- a high-level goal;
- detailed instructions about how to behave;
- the actions available in that state.

The text says WebShop has four states. Figure 1 visibly identifies **Search**, **Results**, **Item**, and **Finish**. Appendix D supplies prompts for the first three; Finish is a stopping state and has no comparable decision prompt.

## 7.3 Agent loop

At every step (§2.2–2.4):

1. The agent receives the user goal.
2. It is placed in the current state.
3. It receives the state-specific prompt, current observation, permissible actions, and past thoughts/actions.
4. It produces a rationale or “thought.”
5. It selects an action based on that rationale.
6. The action either changes the state or leaves it unchanged.
7. The cycle continues until Finish or the interaction limit.

Table 7 separates rationale generation from function selection: the model sees the observation and next-action rationale, then performs a function call.

## 7.4 State-action mapping

From Table 8:

- **Search:** `Search`
- **Result:** `select_item`, `Next`, `Back_to_Search`
- **Item:** `Description`, `Features`, `Reviews`, `Buy_Now`, `Prev`

Figure 1 further visualizes the possible transitions:

- Search → Results by search query;
- Results → Results by Next page;
- Results → Search by Back to search;
- Results → Item by item selection;
- Item → Item by detail checking;
- Item → Results by rejecting the item/going back;
- Item → Finish by Buy.

## 7.5 Memory and backup strategy

LASER stores examined but rejected items in a memory buffer (§2, p. 3). If the agent exhausts its budget, it selects an intermediate item as its final output. The authors call this the **backup strategy**.

Appendix B specifies a maximum of 15 state transitions; after 13 without Finish, the system forces selection from history so the total does not exceed the limit.

## 7.6 Models and implementation

- Standard LASER backbone: **GPT-4-0613**
- Action implementation: GPT function calling
- Alternative action implementation: textual action descriptions formatted as Python dictionaries, with the LLM asked to return JSON
- Alternative LLM: `text-davinci-003`, necessarily using JSON rather than function calling (§4.1)

No hardware, library versions, decoding parameters, temperature, random seed, token budget, cost, latency, or number of repeated runs are reported.

## 7.7 Dataset and samples

### WebShop

Appendix B reports:

- 1,181,436 items collected from Amazon shopping sites;
- human-annotated purchase instructions and target products;
- 500 test instructions for the primary evaluation;
- 200 instructions for ablation studies because of limited computing budget;
- 30 development-set errors manually categorized in the case study.

### Amazon.com transfer

- First 100 WebShop test instructions;
- web pages converted to WebShop’s format;
- LASER applied “as is”/without modification;
- selected products manually annotated for category, attribute, option, and price match;
- both LASER and humans attained 100% price matching, so price was omitted from Table 2 (Appendix B, p. 8).

The paper does not report annotator count, instructions, blinding, agreement, adjudication, or confidence intervals.

## 7.8 Baselines

- **ReAct:** interleaves reasoning and actions while retaining the full trajectory. The paper lists the published ReAct result and the authors’ GPT-4-0613 rerun.
- **ASH:** adds observation summarization to ReAct.
- **WebGUM:** supervised FlanT5-XL fine-tuned on 1,000 human demonstrations.
- **Human Expert:** reference numbers from Yao et al. (2022).

The table marks the published ReAct result as using a “simplified setting,” which weakens direct comparability (Table 1 footnote).

## 7.9 Metrics

- **Success rate:** percentage of cases where the purchased item perfectly matches the target.
- **Reward:** 0–100 partial-match score based on price, product category, hidden attributes, and customization options (Appendix B).

Table 2 decomposes Amazon evaluation into success rate (`SR`), overall reward, attribute match (`Att.`), option match (`Opt.`), and type/category match (`Type.`). All are presented on a 0–100 scale; the table does not print a percent sign.

## 7.10 Statistical methodology

No inferential statistical tests, uncertainty intervals, variance estimates, or repeated-run analyses are reported. The abstract uses “significantly,” but the supplied paper does not provide a statistical-significance analysis.

# 8. Experiments / Analyses

## X1 — Main WebShop comparison

- **Purpose:** Compare LASER with prior systems and a human reference.
- **Data:** 500 WebShop test instructions.
- **System:** GPT-4-0613 LASER with function calling.
- **Conditions:** ASH, published ReAct, authors’ ReAct rerun, WebGUM, LASER without backup, full LASER, and Human Expert.
- **Metrics:** Success rate and reward.
- **Evidence:** Table 1, p. 3.
- **Result:** Full LASER is the strongest non-human row on both metrics.
- **Caveat:** Published baseline settings/models differ; the published ReAct row is explicitly marked “simplified setting.”

## X2 — Backup-strategy ablation

- **Purpose:** Test whether LASER’s advantage depends on choosing a remembered product when the budget expires.
- **Condition:** `LASER - backup` assigns zero when the budget is exhausted.
- **Data:** Presented with the 500-instruction main comparison.
- **Result:** 48.4 success and 71.2 reward without backup versus 50.0 and 75.6 with it (Table 1).
- **Interpretation:** Backup helps, but the no-backup variant still exceeds every listed non-human baseline.
- **Analyst-derived differences:** Backup adds 1.6 percentage points of success and 4.4 reward points.

## X3 — Amazon.com sim-to-real transfer

- **Purpose:** Determine whether the WebShop-designed system works on a real shopping site.
- **Data:** First 100 WebShop test instructions.
- **Procedure:** Convert Amazon pages to WebShop format; stop before actual purchase; manually annotate selected products.
- **Comparison:** LASER versus Human reference.
- **Metrics:** SR, reward, attribute, option, and category/type matching.
- **Evidence:** Table 2 and Appendix B.
- **Result:** LASER trails the human row slightly across every reported metric.
- **Caveats:** Small sample; manual annotations lack reliability reporting; Amazon conversion details are delegated to a footnoted external repository and are not reproduced in the supplied document.

## X4 — Zero-shot versus one-shot

- **Purpose:** Test whether one worked example improves state-specific instruction prompting.
- **Data:** 200 instructions.
- **Conditions:** Standard LASER versus LASER + One-shot.
- **Evidence:** Table 3 and §4.1.
- **Result:** Standard LASER: 52.0/77.6; one-shot: 50.0/74.9.
- **Author interpretation:** One-shot examples can distract the model because the instructions already suffice.
- **Caveat:** The explanation is a hypothesis, and no variability or significance test is provided.

## X5 — Function-calling ablation

- **Purpose:** Test structured function calling against plain text/JSON action generation.
- **Data:** Same 200-instruction ablation set.
- **Conditions:** LASER versus LASER without function calling.
- **Result:** 52.0/77.6 versus 50.0/76.2 (Table 3).
- **Author interpretation:** Function calling slightly improves an interactive agent.
- **Caveat:** The exact rate of malformed or invalid JSON is not reported.

## X6 — Trajectory-length analysis

- **Purpose:** Examine task frequency and performance by number of state transitions.
- **Data:** Test episodes grouped as 3, 4–6, 7–9, 10–13, and 15 steps.
- **Evidence:** Figure 2 and §4.1.
- **Result:** Most tasks finish in three transitions; reward and success generally decline as trajectories lengthen. The forced-stop group at 15 is lowest but still has nonzero success.
- **Caveat:** The exact group counts and exact bar values are not numerically tabulated.

## X7 — Generalization to another LLM

- **Purpose:** Test whether the framework works with a weaker non-chat model.
- **Data:** 200-instruction ablation subset.
- **Model:** `text-davinci-003` with text/JSON action generation.
- **Result:** 38.5 success, 70.2 reward (Table 3).
- **Author interpretation:** Performance drops substantially but remains above the listed baseline values.
- **Caveat:** This changes both the language model and action interface, so their separate effects cannot be identified.

## X8 — Failure-case study

- **Purpose:** Categorize LASER’s remaining failures.
- **Data:** 30 development-set error cases, manually annotated.
- **Categories:** Item good enough (9), retrieval failure (12), missing details (9).
- **Evidence:** Appendix C and Figures 3–4.
- **Result:** Retrieval failure is the largest of the three categories.
- **Caveat:** Selection procedure and annotation reliability are not reported.

# 9. Results

## Main WebShop result

LASER achieves **50.0 success and 75.6 reward** (Table 1). The strongest listed non-human baseline, WebGUM, achieves **45.0 and 67.5**.

**Analyst-derived comparisons:**

- Success: \(50.0-45.0=5.0\) percentage points.
- Relative success increase: \(5.0/45.0 \approx 11.1\%\).
- Reward: \(75.6-67.5=8.1\) points.
- Relative reward increase: \(8.1/67.5=12.0\%\).

LASER remains below Human Expert by 9.6 success points and 6.5 reward points.

## Comparison with the authors’ ReAct rerun

The directly rerun GPT-4-0613 ReAct result is 34.0 success and 59.7 reward, versus LASER at 50.0 and 75.6:

- **Analyst-derived:** +16.0 success percentage points;
- **Analyst-derived:** +15.9 reward points.

The prose reports that ReAct sometimes tries actions unavailable in the current state or repeatedly advances pages until the budget expires (§4, p. 3).

## Backup effect

Full LASER improves over `LASER - backup`:

- Success: 50.0 versus 48.4;
- Reward: 75.6 versus 71.2.

The no-backup version still exceeds WebGUM by 3.4 success points and 3.7 reward points (analyst-derived).

## Amazon.com transfer

LASER versus Human:

| Metric | LASER | Human | Analyst-derived gap |
|---|---:|---:|---:|
| Success rate | 62.0 | 65.0 | −3.0 points |
| Reward | 85.4 | 88.2 | −2.8 points |
| Attribute match | 85.5 | 86.2 | −0.7 points |
| Option match | 75.0 | 76.3 | −1.3 points |
| Type/category match | 97.0 | 99.0 | −2.0 points |

Both reportedly achieved 100% price matching, omitted from Table 2 (Appendix B).

## Ablations

On 200 instructions, standard LASER leads every ablation row:

- One-shot reduces success by 2.0 percentage points and reward by 2.7 points.
- Removing function calling reduces success by 2.0 points and reward by 1.4.
- Using `text-davinci-003` reduces success by 13.5 points and reward by 7.4.

These are descriptive comparisons, not statistically tested effects.

## Trajectory length

Figure 2 shows that 75% of episodes use exactly three transitions; the remaining displayed distribution is 9% at 4–6, 5% at 7–9, 2% at 10–13, and 9% at 15. Performance declines with length, with the forced-stop 15-step group performing worst. Exact bar heights are not labeled and should only be treated as approximate visual estimates.

## Failure categories

Of 30 development errors:

- 9/30 = 30% “Item good enough”;
- 12/30 = 40% retrieval failure;
- 9/30 = 30% missing details.

The percentages are analyst-derived from author-reported counts.

# 10. Figure-by-Figure Interpretation

## Figure 1 — LASER state-transition diagram

- **Location:** p. 1; discussed in §2.2.
- **Type:** Directed state-transition diagram.
- **Components:** Search, Results, Item, and Finish, each represented by a colored circle labeled “LLM Agent.”
- **Flow:** Search query moves Search → Results; item selection moves Results → Item; Buy moves Item → Finish.
- **Self-loops:** Next page remains within Results; detail checking remains within Item.
- **Backtracking:** Results can return to Search; Item can return to Results.
- **Stopping/budget path:** The visual indicates that reaching the maximum iteration can lead to item selection/termination via the backup behavior.
- **Meaning:** Navigation is not a single forward chain. The same high-level state can recur, and unsuccessful decisions can be reversed.
- **Support:** Establishes the architecture claimed to address forward-only prompting.
- **Caveat:** The diagram is conceptual; it does not display probabilities, timing, or learned transition functions.

## Figure 2 — Performance and frequency by trajectory length

- **Location:** p. 4; §4.1.
- **Left panel:** Grouped bar chart. X-axis categories are 3, 4–6, 7–9, 10–13, and 15 steps. The y-axis runs approximately 0–80. Blue bars encode reward and green bars success rate.
- **Right panel:** Pie chart showing the share of trajectories in those length groups.
- **Visually readable pie values:** 75% (3), 9% (4–6), 5% (7–9), 2% (10–13), and 9% (15).
- **Approximate bar values:** Reward declines from roughly the high 70s at length 3 to about 30 at length 15; success declines from roughly the mid-50s to the mid-teens. Intermediate values are not labeled and cannot be read as exact.
- **Main observation:** Short, direct `search → select → buy` paths dominate. Longer paths correlate with lower performance.
- **Special interpretation:** Nonzero success at 15 suggests that the backup history sometimes contains a correct item even when the agent initially failed to recognize it.
- **Caveat:** The figure does not show uncertainty or group sample counts. The 9% at 15 may include forced stops rather than naturally completed trajectories.

## Figure 3 — “Item good enough” case

- **Location:** p. 8; Appendix C.
- **Content:** Screenshot of a WebShop-style product page with the instruction above and the selected green table lamp below.
- **Captioned reward:** 0.666.
- **Author interpretation:** The selected product appears to satisfy the substantive request—a green living-room table lamp within the price limit—but does not receive full credit.
- **Purpose:** Illustrates possible mismatch between benchmark target matching and a plausibly acceptable substitute.
- **Caveat:** The small screenshot does not make every product detail confidently readable; the interpretation relies jointly on the visible example and Appendix C.

## Figure 4 — “Missing details” case

- **Location:** p. 8; Appendix C.
- **Content:** Screenshot of selected women’s shoes and an instruction requiring high heels with specified color, size, and price.
- **Captioned reward:** 0.8.
- **Author interpretation:** Color and size match, but the selected shoes are not high heels.
- **Purpose:** Shows that many matching attributes can cause the agent to overlook one decisive mismatch.
- **Caveat:** This is one illustrative error, not an estimate of how frequently each individual attribute is missed.

# 11. Table-by-Table Interpretation

## Table 1 — WebShop results

| Method | Success | Reward |
|---|---:|---:|
| ASH | 30.2 | 56.7 |
| ReAct, published* | 40.0 | 66.6 |
| ReAct, authors’ rerun | 34.0 | 59.7 |
| WebGUM | 45.0 | 67.5 |
| LASER − backup | 48.4 | 71.2 |
| LASER | **50.0** | **75.6** |
| Human Expert | 59.6 | 82.1 |

- **Location:** p. 3.
- **Purpose:** Main WebShop comparison.
- **Best overall:** Human Expert.
- **Best non-human:** LASER.
- **Worst:** ASH.
- **Footnote:** Published ReAct uses a simplified setting.
- **Statistical information:** None.
- **Demonstrates:** LASER’s advantage is not solely due to backup, although backup adds performance.
- **Caveat:** Not all methods share the same backbone, training regime, or prompting resources.

## Table 2 — Amazon.com transfer

| System | SR | Reward | Att. | Opt. | Type |
|---|---:|---:|---:|---:|---:|
| LASER | 62.0 | 85.4 | 85.5 | 75.0 | 97.0 |
| Human | 65.0 | 88.2 | 86.2 | 76.3 | 99.0 |

- **Location:** p. 3; details in Appendix B.
- **Purpose:** Sim-to-real comparison on 100 instructions.
- **Meaning:** `Att.` = item attribute match; `Opt.` = option/customization match; `Type.` = category match.
- **Price:** Omitted because both scored 100%.
- **Result:** Human is higher in every printed column, but the gaps are small.
- **Caveat:** The paper does not report annotation reliability or uncertainty.

## Table 3 — WebShop ablations

| Condition | Success | Reward |
|---|---:|---:|
| Standard LASER | **52.0** | **77.6** |
| + One-shot | 50.0 | 74.9 |
| − Function call | 50.0 | 76.2 |
| `text-davinci-003` | 38.5 | 70.2 |

- **Location:** p. 3; analyzed on p. 4.
- **Sample:** 200 instructions.
- **Purpose:** Test demonstrations, function calling, and alternate LLM.
- **Best:** Standard zero-shot GPT-4 LASER.
- **Worst success/reward:** `text-davinci-003`.
- **Caveat:** Its standard LASER result differs from Table 1 because the ablation uses 200 rather than 500 instructions.

## Table 4 — Search-state prompt

- **Location:** p. 10, Appendix D.
- **Observation:** WebShop label, user instruction, and Search button.
- **Instruction:** Generate a query and rationale while considering history.
- **Purpose:** Defines behavior at the initial Search state.
- **Available decision:** Search only.
- **Caveat:** No example of actual model output is supplied here.

## Table 5 — Result-state prompt

- **Location:** p. 10, Appendix D.
- **Observation:** Instruction, Back to Search, page number, result count, Next, and item IDs/names/prices.
- **Behavior:** Select a plausibly matching item, consider later customization, avoid already-clicked items, advance if needed, or return to Search after sufficiently exploring poor results.
- **Required rationale form:** Restate requested keywords and explain the candidate match.
- **Methodological importance:** Encodes search-result judgment without a worked trajectory.
- **Caveat:** “Partially matches” leaves substantial judgment to the LLM.

## Table 6 — Item-state prompt

- **Location:** p. 11, Appendix D.
- **Observation:** Navigation controls, customization choices, product details, Description/Features/Reviews, Buy, target keywords, and maximum price.
- **Behavior:** Decide whether the product matches, inspect additional details if uncertain, buy if it matches, or return to Results otherwise.
- **Repeated-action protection:** Do not reopen Description, Features, or Reviews if their content is already displayed.
- **Methodological importance:** Concentrates verification behavior in the state where detailed product evidence is available.
- **Caveat:** The prompt asks the model to determine “perfectly matches” but does not define a formal matching function.

## Table 7 — Thought-to-action prompt

- **Location:** p. 12, Appendix D.
- **Inputs:** Current observation and previously generated next-action rationale.
- **Output:** One function call.
- **Purpose:** Separates reasoning generation from executable action selection.
- **Caveat:** The table does not show function schemas or argument-validation behavior.

## Table 8 — State-specific action space

- **Location:** p. 12, Appendix D.
- **Rows:** Search, Result, Item.
- **Actions:** One, three, and five actions respectively.
- **Purpose:** Restrict the model to actions valid in the current state.
- **Note:** Additional function parameters are omitted for brevity.
- **Caveat:** Finish is not listed because it is a stopping state; implementation details needed for reproduction are incomplete.

# 12. Diagram / Architecture Interpretation

LASER’s architecture can be understood as a controlled loop:

`User instruction → current state/observation → state-specific reasoning prompt → rationale → state-specific function selection → environment action → new observation/state`

Two forms of memory feed the next decision:

- the full history of prior rationales and actions;
- a buffer of inspected but rejected products that can become backups.

The control layer determines which actions the model may choose. It is manually designed rather than learned. The environment then determines the resulting observation. A transition can:

- move forward toward purchase;
- remain in the same state while gathering information or paging;
- move backward to reconsider candidates or reformulate the search; or
- enter Finish.

Figure 1 and Table 8 are complementary: Figure 1 shows possible transitions; Table 8 lists the callable controls available at each decision state. Tables 4–6 define the information and reasoning instructions associated with those states, and Table 7 converts reasoning into action.

# 13. Equations and Mathematical Concepts

There are no numbered equations, loss functions, learned objectives, theorems, or proofs.

The main formalization appears in §2.1:

- \(E\): web environment;
- \(I\): user instruction;
- \(O_0\): initial observation;
- \(\{a_0,a_1,\ldots,a_n\}\): action sequence;
- \(O_i\): observation produced after action \(a_i\);
- \(S\): stopping state.

In plain language, the agent starts with a goal and a view of the website, repeatedly acts and receives a new view, and stops when it reaches Finish or exhausts its budget.

The implied transition can be written illustratively as \(O_i \xrightarrow{a_i} O_{i+1}\), but this expression is **analyst-provided for explanation**, not an equation printed by the authors.

The reward lies on a 0–100 scale and combines price, category, hidden attributes, and customization options (Appendix B), but the paper does not give the explicit reward formula.

# 14. Interpretation and Discussion

The evidence supports the narrower claim that explicit state organization is associated with better reported WebShop performance than the listed baselines. The design addresses a concrete failure mode: if only Result-state actions are exposed while the agent is viewing results, it cannot call an Item-only control that does not exist there.

The experiments address the informal questions as follows:

- **RQ1:** Yes descriptively. LASER is the best non-human row in Table 1.
- **RQ2:** Yes, within the authors’ transfer setup. Its Amazon scores are close to the human reference, though always lower.
- **RQ3:** No benefit is observed from one-shot prompting; it decreases both reported metrics.
- **RQ4:** Function calling provides a small descriptive improvement.
- **RQ5:** Performance declines with longer trajectories, although the authors state the decline is less severe than previously observed for ReAct and ASH.
- **RQ6:** The framework still operates with `text-davinci-003`, but performance drops sharply.
- **RQ7:** Failures involve benchmark-equivalent alternatives, retrieval limitations, and missed product details.

The state system provides **procedural structure**, not guaranteed semantic correctness. It can stop invalid action types, yet it cannot guarantee that a product truly satisfies every requirement. Figure 4 demonstrates this distinction.

A notable unresolved point is the paper’s use of “significantly outperforms.” The numerical gaps are visible, but no statistical test or uncertainty analysis establishes statistical significance. The word should therefore be read as an author claim of a substantial empirical difference, not a reported hypothesis-test result.

Another qualification concerns the phrase “without modification” for Amazon transfer. The LASER decision logic is reportedly unchanged, but Amazon pages are converted into WebShop’s representation. Thus the agent is not interacting with arbitrary raw Amazon pages without an adaptation layer.

# 15. Contributions and Novelty

## Conceptual contribution

Models web navigation as explicit state-space exploration rather than an implicitly forward-only trajectory.

## Methodological contribution

Associates each state with:

- a structured observation template;
- instructions tailored to that state; and
- a restricted action space.

## Agent/system contribution

Adds bidirectional transitions, state tracking, thought-action iteration, history, and backup-item memory.

## Implementation contribution

Uses function calling to constrain action selection and supplies the prompts and state-action definitions in Appendix D.

## Experimental contribution

Evaluates the approach on WebShop, transfers it to Amazon.com, and conducts ablations on examples, function calling, trajectory length, and model choice.

## Empirical contribution

Reports stronger WebShop results than the listed non-human baselines and performance near the supplied human reference on Amazon.com.

## What is not contributed

The paper does not introduce a new pretrained LLM, training algorithm, dataset, reward definition, formal theorem, or learned state-discovery technique.

# 16. Limitations

## Authors’ stated limitations

From the Limitations section (p. 5):

- Evaluation covers target-item search only, not order tracking, order history, or other common e-commerce operations.
- LASER requires manual annotation of possible states and their descriptions.
- This manual requirement may restrict it to bounded domains with few states rather than open-world web navigation.
- The success rate remains imperfect.
- Real-world actions can have difficult-to-reverse consequences.
- High-stakes actions may require human verification.
- On Amazon.com, Buy was not actually executed; the system stopped at that decision.

Additional author-discussed weaknesses elsewhere include:

- ablations were limited to 200 instructions because of computing constraints (§4.1);
- performance deteriorates on longer trajectories;
- changing to a weaker LLM causes a large drop;
- retrieval can fail even with a suitable query;
- the agent can miss a decisive product detail.

## Additional evidence-based analyst observations

These are not presented as author admissions:

- No confidence intervals, significance tests, or repeated-run variation are reported.
- Primary evaluation uses one named model snapshot, GPT-4-0613.
- Baselines vary in backbone, supervision, demonstrations, and reported settings.
- The published ReAct result is marked as simplified, limiting direct comparability.
- The Amazon sample contains only 100 instructions and uses manual judgment without inter-annotator agreement.
- The alternate-LLM experiment changes both model and action interface, confounding their effects.
- The paper does not report inference cost, latency, prompt length, or token consumption.
- Function schemas and arguments are omitted, limiting exact reproduction.
- Manual state construction may shift labor from trajectory annotation to prompt/state engineering; no effort comparison is quantified.
- The reward combines several matching dimensions but its full formula is not supplied.
- Error analysis covers only 30 development errors and lacks a reported sampling protocol.
- Conversion of Amazon pages into WebShop format is a substantive interface dependency.

# 17. Threats to Validity

These categories are analyst-organized; the authors do not frame them formally in this vocabulary.

## Internal validity

The improvement cannot be attributed solely to state-space structure because LASER combines several components: state prompts, restricted actions, GPT-4-0613, function calling, history, and backup memory. Only backup and function calling receive partial ablations.

## Construct validity

“Success” requires a perfect match to a benchmark target, which may reject plausible alternatives; the “Item good enough” cases illustrate this. Conversely, partial reward may hide a crucial semantic mismatch, as in Figure 4’s non-high-heel shoes.

## Statistical conclusion validity

No uncertainty estimates, statistical tests, or multiple-run results are supplied. Small ablation differences may not be stable.

## External validity

Evidence comes from one domain and one principal task: product finding. Amazon transfer improves realism but retains WebShop-style observations and the same shopping instructions.

## Ecological validity

The system does not complete real purchases. This is appropriate for safety but means it does not demonstrate the complete real transaction workflow.

## Reproducibility

Prompts and action names are supplied, which helps. Reproduction remains limited by omitted function parameters, model-access details, decoding settings, Amazon conversion specifics, annotator protocol, and absent code in the supplied material.

## Generalizability

The framework conceptually supports other domains, but the paper does not empirically test travel, finance, general browsing, or open-world navigation.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- Support order tracking, order history, and other e-commerce tasks (p. 5).
- Equip LASER with tools such as a knowledge retriever or calculator (p. 5).
- Develop a hierarchical multi-agent system with domain-specific LASER-like agents coordinated by a general open-world agent (p. 5).
- Use stronger search/retrieval to address retrieval failures (Appendix C).
- Add self-feedback or verification to catch missed product details (Appendix C).
- Combine LASER with planning/refinement approaches described as orthogonal in Appendix A.
- Incorporate state-transition modeling into multimodal web agents (Appendix A).
- Investigate more powerful future LLMs (§4.1).

## B. Additional open questions

- Can states and transition rules be learned automatically?
- How much human labor is required for state prompts versus demonstrations?
- Which component accounts for most of the improvement?
- How robust are results across random/model variability?
- Can the method safely handle authentication, forms, checkout, and irreversible actions?
- How does performance scale as the number of states and actions grows?
- What happens when a page does not fit any known observation structure?
- How much do raw screenshots or visual layout add beyond text-converted pages?
- Can formal verification or confirmation gates guarantee safety-critical action policies?
- Would an independent annotation protocol reproduce the Amazon scores?

# 19. Terminology and Notation Glossary

| Term | Meaning in this paper |
|---|---|
| LLM | Large language model |
| LASER | LLM Agent with State-Space ExploRation |
| WebShop | Simulated online-shopping environment used for evaluation |
| State | A category of environment observation with a distinct structural layout |
| State space | Set of possible high-level states |
| Transition | Movement between states caused by an action |
| Action space | Actions the agent may choose |
| Global action space | Same broad set of actions exposed regardless of current state |
| State-specific action space | Only actions valid for the current state |
| Observation | Environment/page representation visible to the agent |
| Trajectory | Sequence of observations, thoughts, and actions |
| Oracle trajectory | Demonstration containing correct actions |
| In-context example | Worked example placed in the prompt |
| Zero-shot | No worked example in the prompt |
| One-shot | One worked input-output example |
| Backtracking | Returning to an earlier state after an unsuitable choice |
| Function calling | Structured selection from predefined callable actions |
| Rationale/thought | Model-generated reasoning preceding action selection |
| Backup strategy | Selecting a previously inspected item when the step budget expires |
| Sim-to-real transfer | Applying the simulated-environment agent to Amazon.com |
| Success rate | Share of instructions for which the chosen item perfectly matches the target |
| Reward | 0–100 partial-match score |
| Attribute match | Match on target item properties |
| Option match | Match on customization options |
| Type match | Match on item category |
| \(E\) | Web environment |
| \(I\) | User instruction |
| \(O_i\) | Observation at interaction step \(i\) |
| \(a_i\) | Action at step \(i\) |
| \(S\) | Stopping state |
| SR | Success rate |
| Att. | Attribute match |
| Opt. | Option match |
| Type. | Item type/category match |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| WebShop inventory | 1,181,436 | items | Dataset size | Author-reported | Appendix B, p. 7 |
| Main WebShop evaluation | 500 | instructions | Test set | Author-reported | §3, p. 3 |
| Ablation evaluation | 200 | instructions | Limited compute | Author-reported | §4.1, p. 4 |
| Amazon transfer | 100 | instructions | First WebShop test instructions | Author-reported | §3; Appendix B |
| Transition maximum | 15 | transitions | LASER budget | Author-reported | Appendix B, p. 7 |
| Forced history selection begins | after 13 | transitions | To remain within budget | Author-reported | Appendix B |
| LASER WebShop success | 50.0 | percentage-scale points | 500-test main result | Author-reported | Table 1 |
| LASER WebShop reward | 75.6 | reward points | 500-test main result | Author-reported | Table 1 |
| WebGUM success/reward | 45.0 / 67.5 | points | Strongest listed non-human baseline | Author-reported | Table 1 |
| LASER advantage over WebGUM | +5.0 / +8.1 | success pp / reward points | Main WebShop | Analyst-derived | Table 1 operands |
| LASER − backup | 48.4 / 71.2 | success/reward | Main WebShop | Author-reported | Table 1 |
| Human Expert WebShop | 59.6 / 82.1 | success/reward | Reference | Author-reported | Table 1 |
| LASER Amazon | 62.0 / 85.4 | success/reward | 100 instructions | Author-reported | Table 2 |
| Human Amazon | 65.0 / 88.2 | success/reward | 100 instructions | Author-reported | Table 2 |
| LASER Amazon attribute | 85.5 | points | Human: 86.2 | Author-reported | Table 2 |
| LASER Amazon option | 75.0 | points | Human: 76.3 | Author-reported | Table 2 |
| LASER Amazon type | 97.0 | points | Human: 99.0 | Author-reported | Table 2 |
| Amazon price match | 100 | percent | LASER and Human; omitted from table | Author-reported | Appendix B, p. 8 |
| Standard LASER ablation | 52.0 / 77.6 | success/reward | 200 instructions | Author-reported | Table 3 |
| One-shot LASER | 50.0 / 74.9 | success/reward | 200 instructions | Author-reported | Table 3 |
| Without function call | 50.0 / 76.2 | success/reward | 200 instructions | Author-reported | Table 3 |
| `text-davinci-003` | 38.5 / 70.2 | success/reward | 200 instructions | Author-reported | Table 3 |
| Three-step trajectories | 75 | percent of episodes | Figure 2 distribution | Visually readable | Figure 2 |
| Four-to-six-step trajectories | 9 | percent | Figure 2 distribution | Visually readable | Figure 2 |
| Seven-to-nine-step trajectories | 5 | percent | Figure 2 distribution | Visually readable | Figure 2 |
| Ten-to-thirteen-step trajectories | 2 | percent | Figure 2 distribution | Visually readable | Figure 2 |
| Fifteen-step trajectories | 9 | percent | Figure 2 distribution | Visually readable | Figure 2 |
| Case-study errors | 30 | cases | Development set | Author-reported | Appendix C |
| Item-good-enough errors | 9 | cases | 30% derived | Author-reported count | Appendix C |
| Retrieval failures | 12 | cases | 40% derived | Author-reported count | Appendix C |
| Missing-detail errors | 9 | cases | 30% derived | Author-reported count | Appendix C |
| Figure 3 example reward | 0.666 | reward fraction | Item-good-enough example | Author-reported | Figure 3 caption |
| Figure 4 example reward | 0.8 | reward fraction | Missing-details example | Author-reported | Figure 4 caption |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| LASER outperforms listed non-human WebShop baselines | 50.0/75.6 exceeds all non-human rows | X1, Table 1 | p. 3 | Strong descriptive evidence; no statistical test |
| Improvement is not entirely caused by backup | No-backup result 48.4/71.2 also exceeds baselines | X2, Table 1 | p. 3 | Strong within-table evidence; still a bundled-system comparison |
| LASER approaches human performance on Amazon | 62.0/85.4 vs 65.0/88.2 | X3, Table 2 | p. 3 | Descriptively close; small manual evaluation |
| State/action design prevents invalid action types | Each state exposes only permissible actions | Figure 1, Table 8 | pp. 1, 12 | Strong architectural support; does not guarantee correct semantic actions |
| LASER performs valid actions “100%” | Explicit prose statement | X4 discussion | §4.1, p. 4 | Author-reported; no separate count/table |
| One-shot examples do not help this setup | 50.0/74.9 vs 52.0/77.6 | X4, Table 3 | pp. 3–4 | Descriptive 200-case result; distraction explanation is hypothesized |
| Function calling helps slightly | 50.0/76.2 without vs 52.0/77.6 standard | X5, Table 3 | pp. 3–4 | Small untested difference |
| Performance declines with trajectory length | Descending grouped bars | X6, Figure 2 | p. 4 | Clear trend; exact values and uncertainty absent |
| Backup memory can rescue some failures | Fifteen-step group has nonzero success | X6, Figure 2 | p. 4 | Plausible author interpretation, not direct causal proof |
| Framework transfers to a weaker LLM | `text-davinci-003` reaches 38.5/70.2 | X7, Table 3 | pp. 3–4 | Demonstrates operation, but model and interface both change |
| Retrieval is a major remaining failure source | 12 of 30 errors | X8 | Appendix C, p. 8 | Useful small case study; sampling/reliability unknown |
| Benchmark scoring may reject plausible substitutes | 9 item-good-enough cases; Figure 3 | X8, Figure 3 | p. 8 | Evidence of construct mismatch in selected errors |
| Agent can overlook a decisive detail | 9 missing-detail cases; Figure 4 | X8, Figure 4 | p. 8 | Supported by manual categorization and example |
| Method “significantly” outperforms prior work | Numerical gaps in Table 1 | X1 | Abstract; §4 | Statistical significance is not demonstrated |

# 22. Very Simple Explanation

Imagine a shopping robot that has only been shown perfect examples: search once, click the right product, and buy it. If it clicks the wrong product, those examples may not teach it how to return and try again. It may also try to press a button that is not available on the page it is viewing.

LASER gives the robot a small map. It knows whether it is on the search page, a results page, or a product page. At each place it sees only the sensible moves for that place. It can inspect a product, go back if it is wrong, try another results page, or restart with a better search. It also remembers products that were almost right.

In the simulated WebShop benchmark, LASER chose a perfectly matching product in 50% of 500 tasks, compared with 45% for the best listed non-human baseline. On 100 Amazon.com tasks, it scored 62% success compared with a 65% human reference. It was not allowed to complete real purchases.

The system is promising but not foolproof. It can still miss an important detail, fail because search returned no suitable product, or disagree with a benchmark that accepts only one target product. Its states and instructions must also be designed manually, and the evidence is limited to product-finding tasks.

# Completeness Audit

## Inventory and coverage

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, affiliation | Yes | Yes | Represented in compressed form | Title and method identified; author list not repeated in narrative |
| Abstract | Yes | Yes | Fully represented | Problem, method, environments, and claim covered |
| §1 Introduction | Yes | Yes | Fully represented | Forward-only and global-action critiques covered |
| §2.1 Problem Formulation | Yes | Yes | Fully represented | All defined symbols explained |
| §2.2 LLM Agent | Yes | Yes | Fully represented | Inputs, loop, history, and transitions covered |
| §2.3 State Description | Yes | Yes | Fully represented | Structural definition and manual prompts covered |
| §2.4 Action Space | Yes | Yes | Fully represented | Local permissible actions and heuristic possibility covered |
| Backup/memory passage | Yes | Yes | Fully represented | Memory and forced selection covered |
| §3 Experiments | Yes | Yes | Fully represented | Samples, metrics, model, and baselines covered |
| §4 Results | Yes | Yes | Fully represented | Main and transfer findings covered |
| §4.1 Zero/few-shot | Yes | Yes | Fully represented | Setup, values, and hypothesis covered |
| §4.1 Function calling | Yes | Yes | Fully represented | JSON alternative and results covered |
| §4.1 Trajectory length | Yes | Yes | Fully represented | Plot distribution and trend covered |
| §4.1 Alternate LLM | Yes | Yes | Fully represented | Model/interface confounding noted |
| §5 Conclusion | Yes | Yes | Fully represented | Claims integrated throughout |
| Limitations section | Text only | Yes | Fully represented | Page 5 was not visually rendered |
| References | Yes | Partly | Deliberately compressed | Relevant work categories summarized; individual citations not inventoried |
| Appendix A Related Works | Text only | Yes | Represented in compressed form | Method categories and positioning included |
| Appendix B Experimental Details | Text only on p. 7; visual/text p. 8 | Yes | Fully represented | Dataset, budget, transfer, metrics, supervision covered |
| Appendix C Case Studies | Yes | Yes | Fully represented | Counts, categories, and examples covered |
| Appendix D Prompts | Yes | Yes | Fully represented | Tables 4–8 individually interpreted |
| Appendix E Licenses | Text only | Yes | Represented in compressed form | MIT licensing for WebShop and ReAct recorded here |
| Figure 1 | Yes, visually | Yes | Fully represented | States, loops, and backtracking audited |
| Figure 2 left | Yes, visually | Yes | Fully represented with uncertainty | Unlabeled bar values treated as approximate only |
| Figure 2 right | Yes, visually | Yes | Fully represented | All displayed percentages recorded |
| Figure 3 | Yes, visually | Yes | Fully represented | Small details supplemented by caption/prose |
| Figure 4 | Yes, visually | Yes | Fully represented | Small details supplemented by caption/prose |
| Table 1 | Yes, visually/textually | Yes | Fully represented | Every row and footnote covered |
| Table 2 | Yes, visually/textually | Yes | Fully represented | Every column and omitted-price note covered |
| Table 3 | Yes, visually/textually | Yes | Fully represented | Every row covered |
| Tables 4–7 | Yes, visually/textually | Yes | Fully represented | Prompt roles and contents covered |
| Table 8 | Yes, visually/textually | Yes | Fully represented | Every state and action covered |
| Explicit equations | N/A | N/A | None present | Only inline notation exists |
| Theorems/lemmas/proofs | N/A | N/A | None present | Not a theoretical paper |
| Formal algorithms | N/A | Yes | Represented from prose | No numbered pseudocode block |
| Main WebShop experiment | Yes | Yes | Fully represented | X1 |
| Backup ablation | Yes | Yes | Fully represented | X2 |
| Amazon transfer | Yes | Yes | Fully represented | X3 |
| One-shot ablation | Yes | Yes | Fully represented | X4 |
| Function-calling ablation | Yes | Yes | Fully represented | X5 |
| Trajectory analysis | Yes | Yes | Fully represented | X6 |
| Alternate-LLM analysis | Yes | Yes | Fully represented | X7 |
| Error analysis | Yes | Yes | Fully represented | X8 |
| Author-stated contributions | Yes | Yes | Fully represented | Separated by contribution type |
| Author-stated limitations | Text only | Yes | Fully represented | Separated from analyst observations |
| Supplementary material | N/A | N/A | Missing/not referenced | No separate supplement supplied |
| Footnote 1 | Yes | Yes | Represented in compressed form | Points to WebShop transfer code |
| Footnote 2 | Partially | Yes | Uncertain | Table 8 refers to OpenAI function-calling guidelines; exact reference formatting is not visible in supplied extraction |

## Missing or inaccessible material

- No pages are missing.
- Pages 5, 7, and 9 were not visually rendered, so their layout was not inspected; their complete supplied text was analyzed.
- No separate source code, model logs, raw outputs, annotation sheets, or Amazon conversion implementation was supplied.
- The full function schemas and additional arguments are explicitly omitted from Table 8.
- The explicit WebShop reward formula is not included.
- No statistical-analysis artifacts, run-level scores, confidence intervals, or seeds are supplied.
- No supplementary file was supplied or clearly referenced as supplementary material.

## Uncertain interpretations

- Exact Figure 2 bar heights are unlabeled and therefore cannot be reported confidently; only the direction of the trend and the pie-chart percentages are reliable.
- Figure 3 and Figure 4 contain small screenshot text; the case interpretations rely partly on their captions and Appendix C.
- “Significantly” is not supported by a reported statistical test.
- “Without modification” applies to the LASER agent logic, but an Amazon-to-WebShop page-conversion layer is used.
- Table 8’s superscripted reference to function-calling guidelines is imperfectly represented in the extraction.
- The paper says the four states are Search, Results, Item, and Finish through the combined evidence of Figure 1 and §2.3; only the first three require prompts/actions.

## Deliberately compressed material

- Individual reference entries were not separately summarized because they are bibliographic rather than direct empirical evidence.
- Appendix A’s many cited systems were grouped by approach: fine-tuning, prompted reasoning/action, decomposition, planning/reflection, state-conditioned prompting, and multimodal agents.
- Repetitive prompt boilerplate in Tables 4–7 was compressed while preserving each state’s observation format, decisions, restrictions, and output role.
- Typographical errors and formatting artifacts in the extracted paper were not catalogued because they do not alter substantive meaning.
- Appendix E’s license statement was compressed to: WebShop and ReAct are reported as MIT-licensed for research use, and the authors state their experiments conform to that use.

## Potential omissions

No substantive numbered section, subsection, experiment, figure, table, formal notation block, contribution, author-stated limitation, or supplied appendix identified in the inventory is known to be absent from this analysis. Bibliographic entries and repeated prompt wording were deliberately compressed as documented above.