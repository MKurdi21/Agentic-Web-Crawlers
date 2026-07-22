# GO-BROWSE: Training Web Agents with Structured Exploration

**Authors:** Apurva Gandhi and Graham Neubig, Carnegie Mellon University  
**Publication:** ICLR 2026 conference paper

## 1. Background and Context

Large language models remain much weaker at operating graphical websites than at many text-based tasks. On the 812-task WebArena benchmark, humans achieve a 78% success rate, while the paper reports 38% for GPT-4o, 19% for GPT-4o-mini, and 8% for the pretrained Qwen-2.5-7B-Instruct model. Models trained specifically for computer interaction perform better: Claude-3.7-Sonnet scores 45.4%, and OpenAI’s Computer-Using Agent scores 58%. The authors argue that this gap shows the importance of training on agent-specific interaction data.

Collecting such data is difficult:

- Human demonstrations are expensive and slow to produce at the scale needed for training.
- Some approaches extend human-generated data or keep people in the collection loop.
- Fully automatic approaches either turn indirect knowledge, such as tutorial articles, into demonstrations or directly explore websites.
- Direct environment exploration has performed substantially better than using generic indirect knowledge: the paper cites success rates of 16% versus 6%.

The underlying problem is that pretrained models do not adequately understand unfamiliar digital environments. Instructions learned for one site may not transfer to other websites with different layouts, controls, and navigation structures. The authors therefore argue that agents should learn directly from the environments in which they will operate.

### Web-agent formulation

The paper implements agents with the ReAct pattern. At time step \(t\), the model receives a state \(s_t\), produces an action \(a_t\), and the browser returns a new state \(s_{t+1}\).

Each state contains:

- The user’s goal.
- A flattened accessibility-tree representation of the page.
- A description of the available actions.
- Previous actions.
- Any error produced by the last action.

Actions are Python-style commands. The full action space includes waiting, clicking, hovering, filling fields, pressing keys, scrolling, selecting options, opening a URL, browser back/forward operations, opening or closing tabs, focusing a tab, replying to the user, and reporting that a task is infeasible.

A trajectory is the sequence of states and actions used to attempt a task. It ends when the step limit is reached or the agent performs a terminal action such as replying to the user. A binary reward model assigns 1 to a successful trajectory and 0 to a failure. BrowserGym supplies the browser-agent implementation and WebArena evaluation infrastructure.

### Earlier exploration policies

The paper distinguishes two main ways to gather web-agent data:

1. **Interaction-first exploration:** An agent explores under a broad instruction rather than a concrete task. A separate model labels the resulting behavior afterward. This can reach unexpectedly deep pages, but independent episodes repeatedly revisit easy-to-find areas, producing redundant demonstrations. Unguided exploration can also generate trajectories with no useful task.

2. **Instruction-first exploration:** A task proposer first generates plausible tasks from a page, an agent attempts each one, and a reward model retains successful task–trajectory pairs. This uses an LLM’s knowledge to produce relevant tasks efficiently, but static initial observations restrict tasks to visible content and can cause hallucinated or infeasible tasks. Some prior systems require human demonstrations or screenshots to supply broader context.

Go-Browse combines the useful aspects of these approaches while addressing their coverage, redundancy, and grounding problems.

## 2. Research Goal and Objectives

The paper’s main goal is to develop a fully automatic, scalable method for collecting diverse, realistic, website-specific training data through structured exploration.

The specific objectives are to:

- Treat website exploration as graph search so information can be reused across episodes.
- Cover an entire site more systematically than independent exploratory rollouts.
- Generate tasks grounded in pages the agent has actually explored.
- Separate difficult website navigation from local task execution, allowing weaker models to contribute useful trajectories.
- Build a large WebArena-derived dataset and test whether supervised fine-tuning on its successful trajectories improves a 7-billion-parameter web agent.
- Analyze task diversity, navigation depth, data-collection efficiency, website coverage, and out-of-domain generalization.

## 3. Methods (Approach/Design)

### 3.1 Go-Browse as structured graph exploration

Go-Browse represents a website as a graph \(G=(V,E)\):

- Each node \(v\) is a unique URL.
- Each edge is a trajectory connecting URLs.
- A frontier stores discovered pages that have not yet been fully explored.

The method uses an outer loop for broad website coverage and an inner loop for detailed exploration of each page.

**Figure 1** visualizes this process. The outer loop begins from a root page such as a dashboard, discovers pages such as Products and Best Sellers, and adds them to the frontier. Later iterations reset to previously discovered pages rather than navigating to them from scratch. If a shorter route is found, the corresponding graph edge is updated. For every frontier page, the inner loop proposes tasks, checks whether they are feasible, and samples trajectories for the feasible ones. Successful task solving can reveal additional pages, which return to the frontier.

This “reset, then explore” design is inspired by Go-Explore in reinforcement learning. It reduces repeated navigation, permits exploration to continue from promising pages, and separates:

- **Navigation:** reaching the correct webpage.
- **Local task solving:** acting once that page has been reached.

### 3.2 Go-Browse modules

#### NavExplorer

NavExplorer is an agent that interacts with the current page to discover neighboring URLs and propose concrete navigation tasks leading to them. It has an additional `add_tasks_to_dataset` action.

It is instructed to:

- Find pages linked from the current page.
- Add the corresponding navigation task immediately after reaching a new page.
- Return to the original page before continuing.
- Prioritize pages likely to support common, useful user tasks over niche pages.

Because NavExplorer interacts with the site, its proposals are grounded in observations acquired dynamically rather than inferred from one static page.

#### PageExplorer

PageExplorer proposes tasks local to the current page. It may interact with menus or other controls to understand available functionality, but should focus on tasks that can be performed without leaving the page.

Its task categories are:

- Information seeking.
- Site navigation.
- Content or state modification.

It is instructed to make tasks concrete and self-contained—for example, to name the particular product rather than say only “add item to cart”—because the eventual solving agent may begin elsewhere and lack the proposal page’s context.

#### FeasibilityChecker

The FeasibilityChecker filters proposed tasks by:

1. Asking a strong pretrained agent to solve each task.
2. Having a vision-language model judge the final trajectory using the goal, action history, accessibility tree, final screenshot, and agent response.

Up to three attempts are made, stopping after the first success. A task is feasible if at least one trajectory succeeds. The task and successful trajectory are retained; tasks with no success are discarded.

The judge applies task-specific criteria. Information-seeking answers must contain the requested information or clearly establish its unavailability. Navigation and content-modification tasks are judged from the action history and final browser state.

#### Solvers and prefixed versus unprefixed sampling

Cheaper solver models generate additional trajectories for feasible tasks:

- **Prefixed sampling:** The solver starts on the page where the task was proposed.
- **Unprefixed sampling:** The solver starts at the website’s root page.

Prefixed sampling removes the need to rediscover the page, making local task solving easier and enabling weaker models to produce good training data. Unprefixed sampling remains useful because it teaches long-horizon navigation and task completion from a realistic start.

**Algorithm 3** formalizes the complete process: initialize the dataset, graph, and frontier; add each site’s root; repeatedly select a frontier page; generate navigation and local tasks; check feasibility; update the graph with newly discovered URLs and edges; and sample both prefixed and unprefixed trajectories for every feasible task.

**Figure 2 and Algorithms 1–2** contrast this with conventional policies. Interaction-first exploration repeatedly starts an agent with generic exploration instructions and labels its trajectories afterward. Instruction-first exploration proposes tasks only from the initial state, attempts them, and retains successes. Go-Browse instead repeatedly performs instruction-first-style exploration from newly discovered frontier pages.

### 3.3 Data collection

The authors ran Go-Browse on five self-hosted WebArena domains:

- Shopping Admin, representing a content-management system.
- Shopping.
- Reddit.
- GitLab.
- Map.

They explored 20 URLs in each domain, for 100 URLs total.

Collection settings were:

- NavExplorer: Claude-3.7-Sonnet, up to 15 interaction steps.
- PageExplorer: GPT-4o for up to 20 steps and Claude-3.7-Sonnet for up to 10 steps.
- FeasibilityChecker agent: Claude-3.7-Sonnet.
- Feasibility attempts: at most 3 per task.
- Reward judge: GPT-4o-based vision-language model.
- Feasible-task cap: 30 tasks per URL.
- Solvers: GPT-4o-mini and Qwen-2.5-7B-Instruct.
- Solver horizon: 10 steps.
- Additional trajectories: 2 prefixed and 2 unprefixed per feasible task.
- Sampling temperature during collection: 0.7.
- Total collection cost: approximately $975.57.
- Collection time: approximately three weeks.

The released data include accessibility trees, HTML, and screenshots, although fine-tuning uses only accessibility trees. Both successful and failed interactions are released.

### 3.4 Fine-tuning and evaluation

The authors supervised-fine-tuned Qwen-2.5-7B-Instruct using only successful Go-Browse-WA trajectories. For comparison, they trained the same base model with the same settings on NNetNav-WA, which contains 45,000 interaction steps over the same five domains.

Fine-tuning used:

- 2 epochs.
- Maximum sequence length of 24,000 tokens.
- Learning rate \(2\times10^{-5}\).
- Batch size 8, one sample per GPU.
- 4 gradient-accumulation steps.
- One node with eight NVIDIA H100 GPUs, each with 80 GB memory.
- Approximately 40 hours per fine-tuning run.

Data generation used five parallel cluster nodes—one per WebArena domain—with 256 GB RAM and 8 CPUs each. Eight NVIDIA L40S GPUs hosted Qwen inference.

Models were evaluated at temperature 0 on all 812 WebArena tasks using WebArena’s task-specific rewards. Generalization was tested on Online-Mind2Web, which contains 300 tasks over 136 live websites.

## 4. Results and Findings

### 4.1 Go-Browse-WA dataset composition

**Table 1** reports:

| Measure | Success | Failure | Total |
|---|---:|---:|---:|
| Trajectories | 9,504 | 17,245 | 26,749 |
| Interaction steps | 39,339 | 157,123 | 196,462 |

The dataset contains **3,422 unique tasks**.

Thus, the abstract’s “10K successful trajectories and 40K interaction steps” refers to rounded counts of the 9,504 successful trajectories and their 39,339 successful steps.

**Figure 3** shows that successful trajectories came in relatively balanced proportions from the three collection models:

- Qwen-2.5-7B-Instruct: 29.5%.
- GPT-4o-mini: 36.6%.
- Claude-3.7-Sonnet: 33.9%.

There is an internal inconsistency in the conclusion, which describes “9.5K successful and 39K unsuccessful task solving trajectories.” The detailed dataset table instead reports 17,245 failed trajectories and 39,339 successful interaction steps. The table is the paper’s precise dataset breakdown.

### 4.2 Main WebArena results

**Table 3** gives the following success rates:

| Model | Overall | Admin | Shopping | Reddit | GitLab | Map |
|---|---:|---:|---:|---:|---:|---:|
| GPT-4o-mini | 19.3% | 19.2% | 19.3% | 21.1% | 20.9% | 15.6% |
| GPT-4o | 37.6% | 35.7% | 32.3% | 50.9% | 36.7% | 37.5% |
| Claude-3.7-Sonnet | 45.4% | 37.4% | 37.0% | 58.8% | 52.0% | 47.7% |
| Qwen-2.5-7B-Instruct | 8.3% | 7.1% | 9.4% | 7.9% | 8.7% | 7.8% |
| NNetNav-7B | 18.8% | 14.3% | 20.3% | 23.7% | 19.9% | 17.2% |
| Go-Browse-7B | **21.7%** | **25.3%** | **22.4%** | **30.7%** | 15.3% | **17.9%** |

Among the open-weight 7B models, Go-Browse-7B is best overall and in every domain except GitLab. Its improvements are:

- 13.4 percentage points over pretrained Qwen-2.5-7B-Instruct.
- 2.9 points over NNetNav-7B, the cited prior state of the art among sub-10B models.
- 2.4 points over GPT-4o-mini.
- 11.0 points over NNetNav-7B on Shopping Admin.
- 7.0 points over NNetNav-7B on Reddit.

Go-Browse-7B does not outperform the larger closed models GPT-4o or Claude-3.7-Sonnet. It also trails NNetNav-7B on GitLab, 15.3% versus 19.9%.

### 4.3 Statistical testing

The authors used paired bootstrap testing with 10,000 resamples.

**Table 10** reports baseline/tie/Go-Browse win ratios and \(p\)-values:

- Versus Qwen-2.5-7B-Instruct: 0.000/0.000/1.000; \(p<0.001\). This improvement is statistically significant.
- Versus NNetNav-7B: 0.076/0.018/0.906; \(p=0.094\).
- Versus GPT-4o-mini: 0.085/0.024/0.892; \(p=0.108\).
- Versus GPT-4o: GPT-4o wins all resamples; \(p=0.000\).
- Versus Claude-3.7-Sonnet: Claude wins all resamples; \(p=0.000\).

Although the point estimates favor Go-Browse over NNetNav and GPT-4o-mini, their reported \(p\)-values do not meet the conventional 0.05 threshold. The authors describe these outcomes as moderate confidence supported by high Go-Browse win ratios.

### 4.4 Task diversity

**Figure 4** compares hierarchical task-category distributions in NNetNav-WA and Go-Browse-WA across GitLab, Shopping Admin, Shopping, Map, and Reddit.

NNetNav-WA has several large category wedges, indicating repeated collection of similar tasks. This is especially apparent in difficult-to-navigate domains such as Shopping Admin: independent episodes repeatedly find accessible pages, while a difficult page discovered once may not be revisited.

Go-Browse-WA has:

- More numerous, smaller intent wedges, indicating greater task diversity.
- A more balanced distribution across domains.
- Less overrepresentation of GitLab.
- More Reddit coverage than NNetNav-WA.

This distribution parallels model performance: NNetNav-7B wins only on GitLab, where its dataset is disproportionately concentrated, while Go-Browse performs much better on Shopping Admin and Reddit.

### 4.5 Navigation depth

**Figure 5** plots trajectory density against maximum URL depth, defined as the number of path segments in the deepest URL reached.

- Across all trajectories, Go-Browse and NNetNav have similar depth distributions.
- Among tasks where only Go-Browse succeeds, the distribution is more right-skewed: Go-Browse’s trajectories tend to reach deeper URLs.
- Among tasks where only NNetNav succeeds, the two models show no similarly meaningful depth difference.

The authors conclude that deeper navigation is a distinctive feature of Go-Browse’s unique successes, not simply a general behavioral difference on every task.

**Table 4** lists URLs with the largest visit-count differences. Go-Browse more frequently reaches:

- Shopping Admin product-attribute editing: 10 versus 1 visits, difference 9, depth 5.
- Reddit search: 7 versus 0, difference 7, depth 2.
- A Shopping Admin configurable-product editing path: 5 versus 0, difference 5, depth 12.
- Shopping Admin order details: 6 versus 2, difference 4, depth 6.
- Reddit biography editing: 5 versus 0, difference 5, depth 3.

NNetNav more frequently reaches:

- GitLab new-project page: 2 versus 6, difference 4, depth 2.
- GitLab blank-project page: 2 versus 5, difference 3, depth 2.
- GitLab commit history: 2 versus 5, difference 3, depth 5.
- GitLab new-fork page: 1 versus 4, difference 3, depth 5.
- Reddit’s `by_submissions` forum path: 0 versus 3, difference 3, depth 3.

Go-Browse’s largest advantages include pages NNetNav never successfully visited. On Reddit, Go-Browse tends to use direct search, whereas NNetNav tries to locate forums through the `by_submissions` page.

### 4.6 Prefixed sampling

**Figure 6** compares success rates across source-node depth ranges of 1–4, 5–8, 9–12, 13–16, and 17–20. Node depth is the shortest trajectory length from the root, computed with Dijkstra’s algorithm.

The chart shows:

- Prefixed sampling generally succeeds more often than unprefixed sampling.
- The gap grows on deeper nodes because agents starting from the root must first rediscover those pages.
- The effect is especially large for Qwen-2.5-7B-Instruct.
- In the deepest 17–20 range, the plotted Qwen unprefixed success rate drops sharply, while prefixed sampling remains substantially higher.

The result supports the claimed bootstrapping effect: resetting weaker agents directly to relevant pages lets them generate higher-quality local task demonstrations than they could from the root.

### 4.7 Feasibility filtering

The FeasibilityChecker removed 403 proposed tasks. Avoiding further sampling for them saved:

- Approximately 3,200 trajectory rollouts.
- Approximately 29,400 interaction steps.
- 13% of collection steps while preserving the same amount of positive data.

### 4.8 Outer-loop website coverage

**Table 5** varies how 30 task proposals per domain are distributed across reset pages:

| Resets / tasks per reset | Unique URLs visited |
|---|---:|
| 1 / 30 | 183 |
| 5 / 6 | 214 |
| 15 / 2 | 260 |

The 1/30 condition effectively removes the outer loop by proposing all tasks from one page per domain. Increasing the number of reset nodes steadily increases unique URL coverage, demonstrating that distributing exploration across the frontier is important for representative site coverage.

### 4.9 Task-proposal design

**Table 7** compares PageExplorer behavior:

| Model | Navigation tasks | Information tasks | Modification tasks | Navigation clusters | Information clusters | Modification clusters | Max steps |
|---|---:|---:|---:|---:|---:|---:|---:|
| GPT-4o | 274 | 227 | 243 | 24 | 18 | 34 | 20 |
| Claude-3.7-Sonnet | 415 | 508 | 516 | 23 | 19 | 19 | 10 |

Claude proposes nearly twice as many tasks despite receiving half the step budget. GPT-4o produces greater diversity relative to its task count, especially for modification tasks, with 34 clusters versus Claude’s 19. The authors therefore use Claude for efficiency and GPT-4o to complement it with more varied modification tasks.

**Table 8** shows that the dedicated NavExplorer contributes 925 navigation tasks in 32 clusters, versus 689 tasks in 31 clusters from PageExplorer. Adding NavExplorer therefore more than doubles the available navigation-task count while slightly increasing category coverage.

### 4.10 Collection cost

**Table 9** gives detailed costs.

Agent rollouts:

| Model | Trajectories | Steps | Average cost/step | Total |
|---|---:|---:|---:|---:|
| GPT-4o-mini | 11,695 | 95,314 | $0.0008 | $76.25 |
| Qwen-2.5-7B-Instruct | 10,203 | 79,209 | $0.0025 | $198.02 |
| Claude-3.7-Sonnet | 5,102 | 24,532 | $0.0190 | $466.11 |
| GPT-4o | 103 | 789 | $0.0181 | $14.28 |
| **Total** | **27,103** | **199,844** | **$0.0037 average** | **$754.66** |

GPT-4o judged 11,105 trajectories at an average cost of $0.0199 each, totaling $220.91. The grand total was **$975.57**.

Approximately 53% of input tokens were cache reads, lowering the cost of Claude-3.7-Sonnet, GPT-4o, and GPT-4o-mini. Official provider prices were used for those models, while Together AI pricing estimated Qwen costs.

The rollout totals differ slightly from the finalized dataset statistics because this table concerns rollout and evaluation costs rather than only the retained dataset entries.

### 4.11 Online-Mind2Web generalization

**Table 2** reports overall success on Online-Mind2Web:

- NNetNav-7B: 4.00%.
- Go-Browse-7B: 5.33%.
- GPT-4o-mini: 9.33%.

Go-Browse therefore retains a 1.33-point lead over NNetNav on 300 tasks from 136 live sites, although all models perform worse than on in-domain WebArena.

The authors used GPT-4o-mini to classify Online-Mind2Web sites as:

- **In-Domain-Adjacent (IDA):** tasks resemble WebArena domains.
- **Out-of-Distribution (OOD):** genuinely dissimilar tasks.

**Figure 7** reports:

| Model | IDA | OOD |
|---|---:|---:|
| Go-Browse-7B | 5.3% | 4.9% |
| NNetNav-7B | 2.3% | 7.3% |
| GPT-4o-mini | 6.0% | 15.4% |

Go-Browse is within 0.7 percentage points of GPT-4o-mini on IDA tasks and exceeds NNetNav by 3.0 points. This suggests that its learned abilities transfer to new websites resembling those explored during collection. NNetNav performs better than Go-Browse on truly OOD tasks.

The paper also observes that Online-Mind2Web’s IDA tasks appear harder than its OOD tasks, most visibly because GPT-4o-mini scores 6.0% on IDA but 15.4% on OOD.

**Figure 8** breaks successes down by difficulty:

- IDA:
  - GPT-4o-mini: 4 easy, 2 medium, 2 hard.
  - Go-Browse-7B: 5 easy, 1 medium, 1 hard.
  - NNetNav-7B: 2 easy, 1 medium, 0 hard.
- OOD:
  - GPT-4o-mini: 16 easy, 2 medium, 1 hard.
  - Go-Browse-7B: 4 easy, 2 medium, 0 hard.
  - NNetNav-7B: 7 easy, 1 medium, 1 hard.

Most of NNetNav’s OOD advantage over Go-Browse comes from easy tasks.

**Table 11** supplies qualitative examples across models, domains, and difficulties. Go-Browse successes include finding Brooklyn neighborhood maps, an IGN game walkthrough, sub-$15 highly reviewed CVS multivitamins, historical EUR/USD data, and a Viagra–alcohol interaction report. Its failures include filtering Nest doorbell reviews by one-star rating, navigating SoundCloud repost relationships, finding constrained student housing, checking Qatar Airways baggage limits, filtering Walmart jobs, and finding dermatologists meeting distance and insurance constraints.

NNetNav successes include recipe reviews, the same IGN walkthrough, Tesla’s historical closing price, Walmart support-service jobs, and a difficult retirement-calculator task. Its failures include locating popular TV listings, nearby veterinarians, constrained solar-company quotes, a drug dosage, filtered cats, and an ovulation-calculator workflow.

GPT-4o-mini succeeds on examples involving Eventbrite tips, Apple specifications, a League of Legends skin, a natural-products database, faculty jobs, and the retirement calculator. It fails on examples requiring constrained apartment, postal-service, Airbnb, cleaning-service, SEC-chart, and UK-visa searches.

## 5. Analysis and Interpretation

The results support the authors’ main argument that structured exploration creates better training data than independent, unstructured episodes.

### Why Go-Browse improves data quality

The graph lets the system remember difficult-to-find pages. Once such a page has been discovered, later collection episodes can reset there and explore it thoroughly. This reduces repeated exploration of obvious pages and increases coverage of uncommon but useful functionality.

The inner and outer loops serve complementary roles:

- The outer loop distributes effort across URLs, increasing global site coverage.
- The inner loop generates and validates multiple tasks on each page, providing detailed local coverage.

The task-distribution analysis indicates that this produces less redundant and more domain-balanced data. The corresponding model is strongest in domains where Go-Browse-WA improves coverage, particularly Shopping Admin and Reddit. NNetNav’s superior GitLab result is consistent with that dataset’s heavy concentration of GitLab tasks.

### Why prefixed sampling matters

A weaker model may be capable of editing a field or reading information on a page but unable to navigate from the homepage to that page. Prefixed sampling isolates the easier local skill, allowing weaker models to contribute successful examples. Unprefixed examples then supplement these with full navigation behavior.

This is the paper’s bootstrapping mechanism: strong models discover and validate tasks, while cheaper or weaker models can generate additional demonstrations from helpful starting states.

### What the trained model learns

Go-Browse-7B does not merely visit deeper URLs more often across every trajectory. Instead, its unique successes disproportionately involve deeper pages. This suggests that structured exploration teaches capabilities useful for longer-horizon, deeply nested tasks.

The gain is meaningful for a 7B model: fine-tuning raises Qwen’s WebArena score from 8.3% to 21.7%. Nevertheless, large closed models remain substantially stronger, and the point-estimate advantages over GPT-4o-mini and NNetNav do not reach \(p<0.05\) in the paired bootstrap analysis.

### Generalization

Go-Browse’s strongest transfer occurs on unfamiliar websites whose tasks resemble the WebArena domains. It is less effective than NNetNav on genuinely dissimilar OOD sites, particularly on easy OOD tasks. Thus, the data appear to teach strong environment-related skills without solving broad web generalization completely.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- **A structured web-exploration algorithm:** Go-Browse treats websites as graphs of URLs connected by trajectories.
- **Cross-episode reuse:** The method remembers discovered pages and resets to them, reducing redundant navigation.
- **An unsupervised, interaction-grounded instruction-first method:** Task-proposal agents gather their own context rather than relying on human demonstrations or static initial observations.
- **Explicit separation of navigation and local task execution:** Prefixed sampling allows weaker models to generate useful demonstrations from deeper pages.
- **A large released dataset:** Go-Browse-WA contains 26,749 retained trajectories, including 9,504 successes, 17,245 failures, 196,462 steps, and 3,422 unique tasks over 100 URLs.
- **A strong small-model result:** Go-Browse-7B reaches 21.7% on WebArena, improving over pretrained Qwen by 13.4 points, NNetNav-7B by 2.9 points, and GPT-4o-mini by 2.4 points.
- **Extensive analysis:** The paper links structured exploration to task diversity, site coverage, deeper successful navigation, efficient filtering, and transfer to related live websites.
- **Reproducibility resources:** The authors release code, data, and models, along with collection and training settings.

Unlike work that adds APIs, learned workflows, or interaction memories to the agent scaffold, this work aims to improve the base model’s agentic ability while keeping its runtime structure relatively simple.

## 7. Limitations and Caveats

- Data collection covers only five WebArena domains and 100 URLs. Results may not generalize to substantially different sites.
- The model’s strongest Online-Mind2Web transfer is to in-domain-adjacent websites. NNetNav performs better on truly OOD tasks.
- Go-Browse-7B remains far below GPT-4o and Claude-3.7-Sonnet on WebArena.
- Its 2.4-point advantage over GPT-4o-mini has \(p=0.108\), and its 2.9-point advantage over NNetNav has \(p=0.094\). Only the improvement over pretrained Qwen is statistically significant at the 0.05 level.
- Go-Browse underperforms NNetNav on GitLab, showing that the method does not improve every domain.
- Fine-tuning uses only successful trajectories. The much larger body of failed interaction data is not exploited.
- Collection is resource-intensive: approximately $975.57, three weeks, multiple cluster nodes, several proprietary models, and eight L40S inference GPUs.
- Fine-tuning each model requires approximately 40 hours on eight 80-GB H100 GPUs.
- The system depends on strong proprietary models for task proposal, feasibility checking, and trajectory judging.
- A vision-language-model judge can itself make evaluation errors; the paper does not provide a separate human validation rate for those judgments.
- LLM-generated tasks and trajectories may inherit biases from the models and prompts. The authors state that these biases require auditing and mitigation before deployment.
- The paper contains a numerical inconsistency in its conclusion: it mentions 39K unsuccessful trajectories, whereas Table 1 reports 17,245 failures and 39,339 successful steps.
- The source reports statistical significance details but does not provide confidence intervals or effect-size estimates beyond win ratios and \(p\)-values.
- The paper uses accessibility trees for fine-tuning even though screenshots and HTML are available, so the experiments do not test whether multimodal or alternative page representations improve performance.

## 8. Future Work or Open Questions

The authors identify several directions:

- Expand collection beyond the five WebArena domains to produce broader and larger datasets.
- Use signals from unsuccessful trajectories instead of training only on successes.
- Investigate alternative objectives, including reinforcement-learning-based training.
- Scale to larger models, which may yield further performance gains.
- Audit and mitigate biases introduced by the task-proposal models, solver models, judges, and prompts before deployment.

The reported results also leave open how to improve transfer to genuinely dissimilar websites, reduce reliance on expensive proprietary models, validate automatic reward judgments more thoroughly, and use the released HTML and screenshot observations during training.

## 9. High-Level Takeaway (Plain Language)

Go-Browse teaches a web agent by systematically mapping a website instead of repeatedly wandering from the homepage. It remembers useful pages, returns directly to them, invents realistic tasks grounded in what it sees, checks that those tasks are solvable, and collects successful examples. This produces more varied data and helps a 7-billion-parameter model solve 21.7% of WebArena tasks—much better than the same model before training and modestly better than NNetNav-7B and GPT-4o-mini. Its central lesson is that organized, reusable exploration can teach smaller web agents to navigate more deeply and effectively, although broad out-of-domain generalization, statistical certainty over the closest baselines, cost, and model-induced bias remain important challenges.