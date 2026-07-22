# LASER: LLM Agent with State-Space Exploration for Web Navigation

**Authors:** Kaixin Ma, Hongming Zhang, Hongwei Wang, Xiaoman Pan, Wenhao Yu, and Dong Yu  
**Affiliation:** Tencent AI Lab, Bellevue, Washington

## 1. Background and Context

Large language models have increasingly been used for interactive tasks such as virtual-home navigation, text-based games, and web navigation. Earlier prompting-based agents commonly operate in a largely forward-only manner: they receive a few successful, “oracle” trajectories as in-context demonstrations and imitate their step-by-step reasoning.

The paper identifies two problems with this design:

- Oracle demonstrations show correct actions but generally do not teach the agent how to recover from unexpected mistakes. Covering every possible error with additional examples would be expensive or unrealistic.
- Earlier systems often expose a global action space, allowing the model to attempt any action at any time. This increases the decision difficulty and can produce actions that are invalid in the current webpage context.

The authors instead frame web navigation as exploration through a small, predefined state space. A state describes the structural type of the agent’s current environment, such as a search page, results page, or item-details page. Each state has its own instructions and permissible actions. Actions move the agent between states or keep it in the same state, making backtracking explicit.

The resulting system is called **LASER: LLM Agent with State-Space ExploRation**.

The broader research landscape includes:

- Prompted reasoning-and-action agents such as ReAct and InnerMonologue.
- Hierarchical or decomposed approaches such as ASH and WebAgent.
- Synapse, which also uses state-conditional prompts but decomposes few-shot trajectories into atomic examples; LASER instead relies on state-specific instructions without in-context examples.
- Planning and correction systems such as RCI, Adaplanner, and Reflexion. The authors regard these as complementary to LASER.
- Multimodal agents—including Pix2Act, AppAgent, SEEACT, WebVoyager, and Dual-VCR—that act from screenshots or combinations of screenshots and textual webpage elements. The paper suggests that LASER’s state-transition idea could potentially be incorporated into such systems.

## 2. Research Goal and Objectives

The main goal is to determine whether an LLM web agent can navigate more reliably by treating interaction as movement among explicitly defined states, rather than following only forward-running example trajectories.

The paper aims to demonstrate that this formulation can:

1. Handle unfamiliar situations that are not illustrated by demonstrations.
2. Recover from mistakes through explicit backtracking.
3. Restrict the model to valid actions for its current state.
4. Complete complex shopping instructions without in-context examples.
5. Outperform prior systems on the simulated WebShop benchmark.
6. Transfer without modification from WebShop to the real Amazon website.
7. Remain useful on longer trajectories and when powered by a different, less capable LLM.

## 3. Methods (Approach/Design)

### Formal task definition

Given a web environment \(E\), a user instruction \(I\), and an initial observation \(O_0\), the agent executes a sequence of actions:

\[
\{a_0,a_1,\ldots,a_n\}.
\]

Each action \(a_i\) produces a new observation \(O_i\). The special stopping state \(S\) is reached when the agent produces its final output and stops exploring. That output is compared with the target item to calculate evaluation metrics.

### LASER’s state-space agent

The authors manually identify the high-level states that can occur during the task. Two observations are treated as different states only when their structural layouts differ. This criterion allows a complex environment to be represented using only a small number of states.

LASER receives, at every step:

- The user’s overall instruction.
- The current observation.
- A system instruction specific to the current state.
- The actions permitted in that state.
- The history of its previous thoughts and actions.

Inspired by ReAct, the model first generates a rationale or thought and then selects an action based on it. The action may move it to another state or leave it in the same state. This continues until the finish state or the maximum step budget is reached.

For each state, the authors manually write a generic prompt containing:

- A sample observation layout.
- Placeholders replacing item-specific content.
- The state’s high-level objective.
- Detailed guidance about possible situations and appropriate responses.

This supplies general behavioral knowledge directly, rather than requiring the model to infer that knowledge from example trajectories.

### Figure 1: State-transition design

Figure 1 presents LASER’s WebShop navigation process as four colored state nodes:

- **Search**
- **Results**
- **Item**
- **Finish**

The principal transitions are:

- From **Search** to **Results** by issuing a search query.
- From **Results** to **Item** by selecting an item.
- Within **Results**, moving to the next page.
- From **Results** back to **Search** when the current query is inadequate.
- From **Item** back to **Results** when an item should be rejected.
- Remaining in **Item** while checking additional details.
- From **Item** to **Finish** by choosing to buy.
- From **Results** to **Finish** when the maximum iteration count is reached and the agent selects an item from its stored history.

This diagram illustrates the central distinction from forward-only prompting: unsuccessful choices do not terminate the reasoning path because the agent can explicitly return to an earlier state.

### State-specific prompts

LASER uses four states in the WebShop task. Detailed prompts are supplied for Search, Results, and Item; Finish is the stopping state.

#### Search state

The search prompt presents the user instruction and a Search button. The agent must formulate a query from the instruction and generate a rationale for its next action, taking previous rationales and actions into account when available.

#### Results state

The results prompt shows:

- The instruction.
- A Back to Search button.
- Current and total page information.
- A Next button.
- Item identifiers, names, and prices.
- Whether an item has already been clicked.

The agent is told to select an item that may match the instruction. It should not reject an apparently relevant item merely because its title contains a mismatching detail, since later customization options may permit a match. Previously clicked items should not be selected again.

#### Item state

The item prompt includes:

- The user instruction.
- Navigation back to search or the previous results page.
- Available customization options.
- The item’s name and details.
- Buttons for Description, Features, Reviews, and Buy Now.
- Any description, features, or reviews that have already been opened.
- Extracted target keywords and the maximum permitted price.

The agent must determine whether the item and its available customizations satisfy the instruction. It may inspect more information if uncertain, return to the results if the item does not match, or buy if it matches. Already displayed description, feature, or review content should not be reopened.

#### Thought-to-action prompt

A separate prompt receives the current observation and the generated rationale, then asks the model to perform the corresponding function call.

### State-specific action space

Table 8 defines the allowed actions:

| State | Permitted actions |
|---|---|
| Search | `Search` |
| Results | `select_item`, `Next`, `Back_to_Search` |
| Item | `Description`, `Features`, `Reviews`, `Buy_Now`, `Prev` |

The action descriptions explain when each function should be used. Additional function-call parameters are omitted in the paper. The authors note that state-specific actions could also be identified heuristically, for example by detecting clickable buttons.

LASER uses GPT-4-0613’s function-calling interface: each permissible action is passed to the model as a described function from which it selects. This architecture is intended to guarantee that the agent chooses a valid action for its current state.

### Memory and backup strategy

LASER maintains a memory buffer of items that it inspected and considered imperfect or non-matching. This imitates a shopper retaining backup options while continuing to search.

The agent is allowed at most 15 state transitions. In practice, if it has not reached Finish after 13 transitions, it is forced to select an item from its history so it will not exceed the budget. This is called the **backup strategy**.

### WebShop experiment

WebShop is a simulated online-shopping environment containing **1,181,436 items** collected from Amazon shopping sites. It includes human-written purchase instructions and corresponding target items.

The main evaluation used:

- **500 test instructions**
- **GPT-4-0613**
- A maximum of **15 state transitions**
- **Success rate**
- A reward on a **0–100 scale**

An episode is successful only when the purchased item perfectly matches the target. Partial matches receive partial rewards calculated from price, product category, hidden attributes, and customization options.

### Baselines

LASER was compared with:

- **ASH:** Builds on ReAct by summarizing the observation before acting.
- **ReAct:** Interleaves thoughts and actions while retaining its full interaction trajectory in the prompt. The original result used PaLM.
- **ReAct rerun:** The authors’ implementation powered by GPT-4-0613 for a more direct comparison.
- **WebGUM:** A supervised FlanT5-XL system fine-tuned on **1,000 human demonstrations**.
- **Human expert performance** reported with WebShop.

The ReAct and ASH systems used manually written instructions and manually annotated trajectories as demonstrations. WebGUM used 1,000 human-annotated gold trajectories. LASER used manually written, high-level state instructions but no demonstration trajectories.

### Sim-to-real Amazon transfer

LASER was transferred directly to Amazon without changing the agent. The researchers:

- Used the first **100 WebShop test instructions**.
- Converted Amazon webpages into WebShop’s textual format.
- Ran LASER as-is.
- Stopped the agent when it selected Buy, rather than allowing a real purchase.
- Manually judged category, attributes, customization options, and price.
- Applied the same reward and success functions as WebShop.

Both LASER and humans achieved **100% price matching**, so price results were omitted from Table 2.

### Ablation experiments

Because of limited computing resources, the ablations used **200 instructions**, rather than all 500.

They tested:

1. Standard zero-shot LASER.
2. LASER with one input-output example added to every prompt.
3. LASER without function calling, using textual JSON action generation.
4. LASER powered by `text-davinci-003`, which also generated actions as JSON because it lacks function calling.

### Failure analysis

The researchers manually categorized **30 development-set errors** into:

- “Item good enough”
- Retrieval failure
- Missing details

## 4. Results and Findings

### WebShop benchmark

Table 1 reports:

| Method | Success rate | Reward |
|---|---:|---:|
| ASH | 30.2 | 56.7 |
| ReAct, simplified setting | 40.0 | 66.6 |
| ReAct, authors’ GPT-4 rerun | 34.0 | 59.7 |
| WebGUM | 45.0 | 67.5 |
| LASER without backup | 48.4 | 71.2 |
| LASER | **50.0** | **75.6** |
| Human expert | 59.6 | 82.1 |

LASER achieved the best non-human performance on both metrics.

Relative to WebGUM, the strongest listed baseline by success rate, full LASER improved:

- Success rate from **45.0 to 50.0**, a 5-point gain.
- Reward from **67.5 to 75.6**, an 8.1-point gain.

Removing the backup strategy reduced success from 50.0 to **48.4** and reward from 75.6 to **71.2**, but this version still surpassed every automated baseline. Under this stricter condition, an agent that exhausted its budget received zero instead of selecting from its history.

LASER remained below human experts by:

- **9.6 points** in success rate.
- **6.5 points** in reward.

The authors’ ReAct rerun performed worse than the original simplified-setting result. In their experiments, ReAct sometimes:

- Tried to click a nonexistent Next button while on an item page.
- Became stuck repeatedly moving to later pages until reaching the step limit.
- Produced no final output.
- Continued to make invalid actions despite additional system instructions.

### Amazon transfer

Table 2 reports:

| Evaluator | Success rate | Overall reward | Attribute match | Option match | Type/category match |
|---|---:|---:|---:|---:|---:|
| LASER | 62.0 | 85.4 | 85.5 | 75.0 | 97.0 |
| Human | 65.0 | 88.2 | 86.2 | 76.3 | 99.0 |

Price matching was omitted because both achieved **100%**.

LASER came close to human performance:

- 3 points lower in success rate.
- 2.8 points lower in overall reward.
- 0.7 points lower in attribute matching.
- 1.3 points lower in option matching.
- 2 points lower in category/type matching.

LASER’s **62.0** success rate and **85.4** reward on Amazon were higher than its WebShop results of **50.0** and **75.6**. The authors suggest that Amazon’s stronger search engine probably contributed to the improvement.

### Ablation results

Table 3 reports results over 200 instructions:

| Configuration | Success rate | Reward |
|---|---:|---:|
| Standard zero-shot LASER | **52.0** | **77.6** |
| LASER plus one-shot example | 50.0 | 74.9 |
| LASER without function calling | 50.0 | 76.2 |
| LASER with `text-davinci-003` | 38.5 | 70.2 |

#### Zero-shot versus one-shot prompting

Adding one input-output example to each state prompt reduced:

- Success from **52.0 to 50.0**.
- Reward from **77.6 to 74.9**.

LASER already chose valid actions **100% of the time**. The authors therefore hypothesize that its state instructions were sufficient for understanding the task and that the added example sometimes distracted the model.

#### Function calling

Replacing GPT function calls with text-generated JSON reduced:

- Success from **52.0 to 50.0**.
- Reward from **77.6 to 76.2**.

The difference was small but favored function calling, suggesting that structured action selection can improve interactive agents.

#### Transfer to another LLM

Using the less powerful, non-chat `text-davinci-003` model produced a substantial decline:

- Success fell to **38.5**.
- Reward fell to **70.2**.

Despite that loss, the resulting reward remained above all listed baselines in Table 1, and its success rate remained above ASH and the authors’ ReAct rerun, though below the original ReAct result and WebGUM. The experiment shows that the LASER framework can be adapted to a model without native function calling.

### Trajectory length analysis

Figure 2 groups episodes by trajectory length: **3**, **4–6**, **7–9**, **10–13**, and **15** transitions.

The right-hand pie chart gives the exact distribution:

- 3 transitions: **75%**
- 4–6 transitions: **9%**
- 7–9 transitions: **5%**
- 10–13 transitions: **2%**
- 15 transitions: **9%**

Thus, three-quarters of tasks followed the direct three-transition sequence described as search–select–buy.

The left-hand bar chart shows reward and success rate by length group. Exact values are not printed above the bars, so only approximate readings are possible:

- Rewards stay around the high 70s for lengths 3 and 4–6.
- Reward is approximately in the low-to-mid 70s for lengths 7–9 and 10–13.
- Reward falls to roughly 50 for length 15.
- Success is approximately in the mid-50s for length 3, around 50 for 4–6, in the mid-40s for 7–9, around 40 for 10–13, and below 20 for length 15.

Performance generally declines as trajectories lengthen. The authors state that this decline is less severe than previously observed for ReAct and ASH. The length-15 group represents forced stopping and selection from history. Its performance is substantially lower, but its nonzero success rate shows that LASER sometimes encountered a matching item without recognizing it on the first pass.

### Failure cases

Of the **30 manually analyzed development-set errors**:

- **9 cases: “Item good enough.”** The chosen item appeared to satisfy the instruction from the researchers’ perspective but did not receive full benchmark credit.
- **12 cases: Retrieval failure.** The agent issued an appropriate query, but none of the returned items met the requirement.
- **9 cases: Missing details.** The selected item matched many requirements but failed on at least one important detail.

#### Figure 3: “Item good enough”

The instruction requests a **green table lamp for the living room priced below $60**. LASER selects a green Safavieh table lamp shown at **$58.07**, yet receives only **0.666 reward**. The authors consider the selected item to meet the stated request, illustrating that some apparent failures may reflect benchmark-target or scoring limitations rather than an unreasonable agent choice.

#### Figure 4: Missing details

The instruction requests women’s **high-heel** shoes with a closed toe, in pink, size 9, and below $40. LASER selects pink women’s sandals and receives **0.8 reward**. The displayed color and size options match the instruction, but the product is not a high-heel shoe. The example demonstrates how many matching attributes can lead the agent to overlook one decisive mismatch.

No image example is provided for retrieval failure.

## 5. Analysis and Interpretation

The results support the paper’s central claim that explicit state modeling makes web agents easier to guide and more reliable.

The authors attribute LASER’s gains to several connected properties:

- **Recovery is built into the navigation structure.** If an item is unsuitable, the agent can return to results; if a query is poor, it can return to search.
- **Each state reduces the decision space.** The model chooses only among actions that are meaningful in the current context.
- **State instructions convey reusable knowledge.** Rather than studying many case-specific trajectories and abstracting their common lessons, the model receives those high-level lessons directly.
- **In-context examples are unnecessary in this setup.** The one-shot ablation performed worse than zero-shot LASER.
- **Function calling provides a modest additional benefit.**
- **Memory salvages some long episodes.** The backup strategy helps when the model previously found a suitable item but failed to identify it as the target.

The authors contrast two forms of human knowledge:

- Earlier approaches provide low-level, case-by-case demonstrations.
- LASER provides concise, high-level instructions about how to behave in each state.

They argue that the latter is more efficient when it requires comparable or less human effort.

The Amazon experiment shows that the manually constructed states and prompts can transfer from simulation to a real website when the webpages are converted into the same representation. However, this was a guarded transfer: the agent was not allowed to execute an actual purchase.

The failure analysis also separates agent errors from retrieval and evaluation problems:

- **12 of 30 errors** occurred because the search engine returned no suitable item.
- **9 of 30** may have been acceptable selections that the benchmark did not fully reward.
- The remaining **9 of 30** were genuine matching errors involving missed requirements.

Thus, better retrieval could address the largest error category, while verification or self-feedback could help with overlooked product details.

No statistical significance tests, confidence intervals, or variance estimates are reported.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- It formulates LLM-based web navigation as explicit **state-space exploration**.
- It associates each webpage state with its own detailed instructions and restricted action set.
- It enables systematic backtracking and recovery rather than assuming every action proceeds correctly.
- It demonstrates zero-shot task execution without in-context demonstration trajectories.
- It adds a memory-based backup strategy for selecting among previously examined items.
- It obtains stronger WebShop results than ASH, ReAct, and WebGUM.
- It demonstrates direct simulation-to-real transfer to Amazon, with performance close to manually evaluated human results.
- It provides ablations on demonstrations, function calling, trajectory length, and the underlying language model.
- It presents a failure taxonomy distinguishing evaluation mismatches, retrieval failures, and missed product details.

## 7. Limitations and Caveats

The authors identify several important limitations:

- LASER was tested only on finding and selecting target products in the shopping domain.
- It was not evaluated on other common e-commerce tasks such as tracking orders or checking order history.
- The state set and state descriptions require manual annotation.
- This manual design may be practical only in structured domains with a small number of recurring states, such as e-commerce or travel booking.
- The method is not presented as a general open-world web agent.
- Although the Amazon experiment uses a real site, pages were transformed into WebShop’s representation, so the experiment does not evaluate unrestricted interaction with the original visual interface.
- Amazon results were manually scored because gold target annotations were unavailable.
- Only 100 Amazon instructions were evaluated.
- Ablation experiments used only 200 instructions because of limited computing resources.
- Failure analysis covered only 30 development-set errors.
- LASER’s performance depends partly on retrieval quality; 12 of 30 analyzed failures occurred when no returned result met the request.
- It can overlook decisive details when an item matches many other requirements.
- Its overall success rate remains imperfect: 50.0 on the full WebShop evaluation and 62.0 on Amazon.
- The length-15 group performs much worse than shorter trajectories, even though backup selection sometimes succeeds.
- Changing from GPT-4-0613 to `text-davinci-003` causes a large performance drop.
- Real-world actions may be difficult or impossible to reverse. The simulated WebShop allowed every permitted action, but a real Buy action could have consequences. The Amazon agent was therefore stopped when it decided to buy.
- High-stakes actions may require human verification because the system’s success rate is still far from perfect.
- No statistical significance analysis is reported.

The paper’s appendix states that WebShop and ReAct are released under the MIT License for research purposes and that the experiments conform to their intended use.

## 8. Future Work or Open Questions

The authors propose or imply several next steps:

- Extend LASER beyond product finding to order tracking, order-history checks, and other e-commerce activities.
- Give the agent more tools, such as a knowledge retriever or calculator, so it can process more complex instructions.
- Develop a hierarchical multi-agent architecture in which LASER-like agents manage individual structured domains and a general open-world agent coordinates among them.
- Improve the search or retrieval component to reduce cases where a suitable product never appears in the results.
- Add self-feedback or verification to catch overlooked constraints before an item is selected.
- Combine LASER’s state-space design with planning and adaptive correction approaches.
- Incorporate state-transition modeling into multimodal agents that operate from screenshots and webpage text.
- Test whether more capable future language models can close the remaining gap or surpass human performance.
- Conduct additional safety testing and retain human approval for consequential real-world actions.

## 9. High-Level Takeaway (Plain Language)

LASER gives a language-model shopping agent a small map of the situations it can encounter—searching, reviewing results, checking an item, and finishing—and tells it exactly what actions make sense in each situation. That lets the agent go backward after mistakes and prevents many invalid actions. It outperformed earlier automated methods on WebShop and came close to human results when transferred to Amazon, although it still depends on manually designed states, can miss important product details, and is not reliable enough to make consequential purchases without human verification.