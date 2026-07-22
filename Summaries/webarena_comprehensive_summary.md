# WebArena: A Realistic Web Environment for Building Autonomous Agents

**Authors:** Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, and Graham Neubig  
**Affiliation:** Carnegie Mellon University  
**Publication:** ICLR 2024 conference paper

## 1. Background and Context

Advances in generative AI make it possible to imagine autonomous agents that carry out everyday web tasks from natural-language instructions. Such agents could improve efficiency, accessibility, and human capabilities. However, the environments traditionally used to develop and evaluate them differ substantially from the real web.

The paper identifies four recurring problems with prior environments:

- Their websites or simulated worlds often provide only simplified versions of real functionality, limiting task variety.
- Simplification makes tasks easier and shorter than their real-world equivalents.
- Some benchmarks are static collections of previously recorded states, so agents cannot freely explore or cause genuine changes.
- Evaluation often compares the agent’s action sequence with a reference sequence rather than checking whether the desired outcome was actually achieved. This penalizes alternative valid solutions and may reward superficially similar but functionally unsuccessful behavior.

Real websites offer greater authenticity, but relying on live services causes other problems: CAPTCHAs, changing content, configuration changes, and other unpredictable conditions prevent fair, repeatable comparisons over time.

WebArena addresses this tension by creating a realistic but standalone web environment. Its websites are based on open-source systems, populated with sampled real-world data, and hosted locally in reproducible Docker containers. The benchmark evaluates whether the final result satisfies the user’s intent, irrespective of the exact path taken.

**Figure 1** summarizes this design. An AI agent receives natural-language commands, acts on WebArena, and observes feedback. The environment combines applications from popular web domains, utility tools, and knowledge resources. Programmatic validators—illustrated with checks such as repository, README, or answer verification—classify an execution as a functional success or failure. Example commands include calculating how much the user spent on food in March 2023 and creating a “NolanFans” repository whose README lists Christopher Nolan’s Oscar-winning films.

## 2. Research Goal and Objectives

The central goal is to create a web-agent environment that is simultaneously:

- **Realistic:** its applications, content, user histories, permissions, and tasks resemble ordinary web use.
- **Reproducible:** it is standalone and resettable rather than dependent on changing live websites.
- **Fully interactive:** agents can explore, navigate, and modify genuine application state.
- **Functionally evaluated:** success is determined from the resulting answer, page, or database state rather than agreement with one reference action sequence.

The paper has three main objectives:

1. Build WebArena from fully functional applications spanning major kinds of web activity, supplemented by common tools and knowledge resources.
2. Construct a benchmark of realistic, diverse, creative, long-horizon tasks expressed as high-level natural-language intents.
3. Measure the capabilities of contemporary LLM-based agents—including agents that reason before acting—and compare them with human performance.

## 3. Methods (Approach/Design)

### 3.1 WebArena as an interactive environment

WebArena is formalized as an environment  
\(\mathcal{E}=\langle\mathcal{S},\mathcal{A},\mathcal{O},\mathcal{T}\rangle\):

- \(\mathcal{S}\) is the state space.
- \(\mathcal{A}\) is the available action space.
- \(\mathcal{O}\) is the observation space.
- \(\mathcal{T}:\mathcal{S}\times\mathcal{A}\rightarrow\mathcal{S}\) is a deterministic transition function implemented by the websites.

Given a natural-language intent, an agent chooses each action from the current observation plus its action and observation histories. The action changes the environment state and produces a new observation. A reward function examines the full action and state trajectory to determine whether the transitions achieved the intended outcome—for example, whether an order was actually placed or a returned answer was correct.

### 3.2 Selection and implementation of websites

The researchers examined approximately **200 segments from the authors’ actual browsing histories**, summarized the goals of those sessions, and grouped the sites into abstract categories. They selected four prominent categories:

1. E-commerce and online shopping.
2. Social discussion forums.
3. Collaborative software development.
4. Content management systems for creating and revising digital content.

They also included:

- A map for navigation and points-of-interest searches.
- A calculator.
- A scratchpad.
- General and specialized knowledge resources, including an offline English Wikipedia and application manuals.

The implemented systems were:

- **E-commerce:** OneStopShop, built with Adobe Magento. It contains approximately **90,000 products** across more than **300 categories**, including prices, options, descriptions, images, and reviews. Data came from real online-site resources, including the WebShop data dump.
- **Social forum:** Postmill, an open-source Reddit counterpart. The data cover **95 subreddits, 127,390 posts, and 661,781 users**. Sources included popular subreddits plus manually selected northeastern U.S., machine-learning, and deep-learning communities to enable cross-site tasks.
- **Collaborative development:** GitLab. The environment contains **300 repositories** and more than **1,000 accounts** with at least one repository commit. For each programming language, at least ten repositories were sampled: **80%** from the top 90th percentile by stars, using sampling weighted by star count, and the remainder from the bottom 10th percentile. This creates both popular projects with many issues and merge requests and smaller personal projects.
- **E-commerce CMS:** Magento’s administrative portal with official sample data.
- **Map:** OpenStreetMap, restricted to the northeastern United States because of storage constraints.
- **Knowledge resources:** Kiwix hosts an offline English Wikipedia with a **May 2023 knowledge cutoff**. GitLab and Adobe Commerce manuals were scraped from their official documentation.
- **Calculator and scratchpad:** implemented by the authors.

**Figure 2** illustrates the intended complexity. To create a minimum-driving-distance itinerary for all Pittsburgh art museums starting at Schenley Park and save it in the `awesome-northeast-us-travel` repository, an agent must:

1. Find Pittsburgh art museums through Wikipedia.
2. locate each museum on the map and optimize their order.
3. Edit the appropriate GitLab README with the route.

This requires long-term planning, cross-site navigation, information integration, and content modification.

### 3.3 Reproducibility and reset

Each website is packaged in its own self-contained Docker image containing its code, database, data, and dependencies, with no external volume mounts required. Users can download and recreate the benchmark websites locally.

Because tasks may modify website state, users can reset a site by stopping and deleting its container and restarting it from the original image. Depending on the website, reset takes from **a few seconds to one minute**. Many information-gathering tasks are read-only and need no reset. The authors argue that reset overhead is small relative to LLM inference time, although not negligible.

### 3.4 User-role simulation

WebArena gives users distinct roles, permissions, and interaction histories:

- The shopping profile has more than **35 orders over two years**.
- The GitLab user maintains several popular open-source projects with numerous issues and merge requests, as well as several private personal projects.
- The Reddit user has many posts and comments and actively participates in discussions.
- The CMS profile represents a shop owner with full read-and-write access to all content.

Users are automatically signed in through cached cookies. The authors state that, to their knowledge, this was the first publicly available agent-evaluation environment to model this characteristic; earlier environments generally assumed identical user roles.

### 3.5 Observation space

An observation consists of:

- The current page URL.
- The set of open tabs.
- The focused tab’s content.

WebArena supports multi-tab interaction so agents can use tools, compare pages, and carry information between sites in a way that more closely resembles human browsing.

Page content can be represented as:

1. Raw HTML in a Document Object Model tree.
2. A screenshot represented as an RGB array.
3. An accessibility tree.

An accessibility tree is a compact subset of the DOM containing relevant elements represented by role, text, and properties such as focusability. Content can be restricted to the current viewport to fit the context limits of text models or the resolution limits of image models.

**Figure 3** shows the same e-commerce page as a rendered screenshot, HTML, and accessibility tree. The structured versions preserve information such as the “Outdoor Patio” link, an **82% rating**, **12 reviews**, a **$49.99** price, and focusable “Add to Cart,” “Wish List,” and “Compare” buttons. The HTML and accessibility examples are truncated in the figure.

### 3.6 Action space

The compound action space imitates keyboard, mouse, tab, and browser-navigation operations.

**Figure 4** lists:

- `noop`: do nothing.
- `click(elem)`: click an element.
- `hover(elem)`: hover over an element.
- `type(elem, text)`: type into an element.
- `press(key_comb)`: press a key combination.
- `scroll(dir)`: scroll up or down.
- `tab_focus(index)`: focus the indexed tab.
- `new_tab`: open a tab.
- `tab_close`: close the current tab.
- `go_back`: return to the previous URL.
- `go_forward`: reverse a previous back action.
- `goto(URL)`: visit a URL directly.

An element can be selected by screen coordinates or by an ID attached during traversal of the DOM or accessibility tree. IDs turn element choice into an \(n\)-way selection problem and avoid ambiguity. For example, `click [1582]` operates the element displayed as `[1582] Add to Cart`. This supports different observation modalities without making step-count comparisons unfair.

### 3.7 Benchmark construction

The benchmark contains **812 test examples**, generated from **241 intent templates**, or an average of **3.3 examples per template**.

Annotators first explored the websites, then wrote intents meeting three criteria:

- **Abstract and high-level:** tasks should require more than one or two actions. For example, “post a greeting message on the science subreddit” is preferred to merely clicking that subreddit.
- **Creative:** ordinary goals were enriched with constraints, such as creating an account identical to a profile on another site.
- **Templated:** replaceable elements were expressed as variables and instantiated several ways. Different instances of one template could require different execution traces despite sharing high-level semantics.

Annotators could use a supplied ChatGPT prompt for inspiration and were also given curated examples.

The tasks fall into three functional classes:

- **Information seeking:** produce a textual answer, often by visiting multiple pages or using private user history. An example is finding the user’s most recent shampoo purchase.
- **Site navigation:** reach a page or section using searches, links, and other controls.
- **Content and configuration:** create, revise, configure, purchase, or otherwise alter website content or settings.

**Figure 5** gives representative intents:

- Information seeking: determine when shampoo was last purchased; compare walking and driving time from AMC Waterfront to Randyland.
- Site navigation: open merge requests assigned to the user; display the highest-rated ergonomic chair.
- Content/configuration: post a question about needing a car in New York City; delete reviews from a scammer named Yoke.

**Figure 6** reports the site distribution:

- E-commerce: **23.0%**
- CMS: **22.4%**
- GitLab: **22.2%**
- Map: **13.4%**
- Reddit: **13.1%**
- Cross-site: **5.9%**

Cross-site tasks require multiple websites, while all tasks require interaction with multiple pages.

### 3.8 Outcome-based evaluation

Information-seeking tasks have a reference answer \(a^*\), compared with the predicted answer \(\hat a\) using one of three functions:

- **Exact match:** only an identical answer receives 1.
- **Must include:** the prediction receives 1 if it contains a required answer or concept; this can accommodate unordered lists or flexible phrasing.
- **Fuzzy match:** `gpt-4-0613` decides whether the prediction is semantically equivalent to the reference. Only a judgment of “correct” earns 1; “incorrect” and “partially correct” earn 0.

Fuzzy matching is used when equivalent answers can have different forms, such as matching “2h58min,” “2 hour 58 minutes,” and “2:58” while preserving the association between a duration and the correct mode of transport.

For navigation and state-changing tasks, programmatic reward functions inspect intermediate and final states. A **locator** retrieves relevant content through a database query, application API, or JavaScript selection; exact-match or must-include checks then test required properties. Thus, evaluation can verify URLs, page contents, or underlying database changes.

**Table 1** illustrates both approaches:

- The customer with the most cancellations must exactly match **Samantha Jones**.
- A lookup by phone number `8015551212` must include both **Sean Miller** and **sean@gmail.com**.
- The route comparison must fuzzily match **walking: 2h58min** and **driving: 21min**.
- “Checkout merge requests assigned to me” succeeds when the resulting URL exactly matches the merge-request page filtered to `assignee_username=byteblaze`.
- A post asking whether a car is needed in NYC must have a URL containing `/f/nyc` and a body containing “a car in NYC.”

### 3.9 Unachievable tasks and annotation quality

Some tasks are impossible because evidence is absent, permissions are insufficient, or the website lacks required functionality. These are labeled **N/A**, and agents are expected to return an equivalent response rather than hallucinate. For example, the OneStopShop contact number cannot be retrieved because the site does not provide it.

The authors supplied the intents. Information-seeking answers were annotated by authors and an external annotator:

- Every question was annotated twice.
- A third annotator resolved disagreements.
- Three authors proficient in JavaScript wrote the programmatic evaluators.
- Difficult cases were discussed collectively.
- Evaluator authors executed the full tasks and inspected intermediate states.

### 3.10 Human evaluation

Five computer-science graduate students attempted one task from each of **170 templates**.

They achieved:

- Average completion time: **110 seconds**
- Information-seeking success: **74.68%**
- Other-task success: **81.32%**
- Overall success: **78.24%**

Half of human failures involved intent misinterpretation, incomplete answers, or incomplete execution—for example, reporting travel distance instead of time, providing a name without the requested email, or only partly entering product information. The remaining failures were more severely off target.

The paper cautions that human performance may depend on annotator demographics and domain expertise. Tasks can require knowledge of concepts such as Git merge requests or complex CMS workflows. The benchmark prioritizes outcomes that are easy to imagine, such as creating a product page, rather than tasks necessarily easy for an average person to execute.

### 3.11 Baseline agents and prompts

The researchers tested:

- `GPT-3.5-TURBO-16K-0613`
- `GPT-4-0613`
- `TEXT-BISON-001`

Each agent received two in-context examples and used one of two prompting strategies:

1. **Direct:** predict the next action immediately.
2. **Chain of thought (CoT):** reason step by step before producing the action.

The system prompt described the environment, observations, permissible actions, formatting rules, homepage, password page, and completion action. A separate **unachievable-task hint (UA hint)** told the model to stop with `N/A` if it believed the task impossible.

The baseline observation was the accessibility tree with element IDs.

**Figures 7–10** document the prompting difference:

- **Figure 7:** The reasoning-agent prompt asks for one valid action at a time, explicit step-by-step reasoning, correct formatting, and a final `stop [answer]`.
- **Figure 8:** A reasoning example identifies the fax machine’s price as **$279.49** before emitting `stop [$279.49]`; another explains why the map search box should receive “restaurants near ABC.”
- **Figure 9:** The direct-agent prompt supplies the same environment and action information but does not require a reasoning narrative.
- **Figure 10:** The direct examples immediately emit `stop [$279.49]` or the map-search typing action.

The main experiments used:

- Temperature: **1.0**
- Top-\(p\): **0.9**
- Maximum state transitions: **30**

Execution stopped early when:

- The same action was repeated more than three times on the same observation, or
- The agent generated three consecutive invalid actions.

`TEXT-BISON-001` was allowed up to ten retries to produce a valid action. The high temperature was intended to encourage exploration.

## 4. Results and Findings

### 4.1 Main end-to-end success rates

**Table 2** reports overall success rate (SR), success on achievable tasks (SR AC), and success on unachievable tasks (SR UA):

| CoT | UA hint | Model | Overall SR | Achievable SR | Unachievable SR |
|---|---|---:|---:|---:|---:|
| Yes | Yes | TEXT-BISON-001 | 5.05% | 4.00% | 27.78% |
| No | Yes | GPT-3.5 | 6.41% | 4.90% | 38.89% |
| Yes | Yes | GPT-3.5 | 8.75% | 6.44% | 58.33% |
| Yes | Yes | GPT-4 | 11.70% | 8.63% | 77.78% |
| No | No | GPT-3.5 | 5.10% | 4.90% | 8.33% |
| Yes | No | GPT-3.5 | 6.16% | 6.06% | 8.33% |
| Yes | No | GPT-4 | **14.41%** | **13.02%** | **44.44%** |
| — | Yes | Human | **78.24%** | **77.30%** | **100.00%** |

The principal findings are:

- The best agent—GPT-4 with CoT but without the UA hint—succeeded on only **14.41%** of tasks.
- Human participants achieved **78.24%**, a gap of **63.83 percentage points**.
- With CoT and the UA hint, GPT-4 reached **11.70%**.
- GPT-3.5 with CoT and the UA hint reached **8.75%**.
- Under the UA-hint condition, CoT improved GPT-3.5 by **2.34 percentage points**, from **6.41% to 8.75%**.
- `TEXT-BISON-001` with CoT and the UA hint scored **5.05%**, below GPT-3.5.
- No statistical significance test is reported; “significantly lower” is used descriptively for the large GPT-4–human gap.

### 4.2 Effects of the unachievable-task hint

The UA hint helped agents recognize impossible requests but also caused premature stopping on feasible ones.

GPT-4 incorrectly classified **54.9% of feasible tasks** as impossible when prompted to consider unachievability. Removing the hint:

- Raised GPT-4’s achievable-task success from **8.63% to 13.02%**.
- Raised its overall success from **11.70% to 14.41%**.
- Reduced unachievable-task success from **77.78% to 44.44%**.

Even without the hint, GPT-4 sometimes recognized impossible tasks by independently explaining why they could not be completed. GPT-3.5 showed much less of this behavior: without the hint, its unachievable-task success was only **8.33%**, whether using direct or CoT prompting. Instead, it often hallucinated answers, repeated invalid actions, or ran into the step limit.

These findings show a real tradeoff: explicit caution against impossible tasks improves abstention but can substantially increase false declarations of impossibility.

### 4.3 Consistency across related task variants

The paper examines per-template performance for the **61 templates with at least one successful GPT execution** under the no-UA-hint setting.

**Table 3**, presented as a histogram, compares GPT-3.5 direct, GPT-3.5 CoT, and GPT-4 CoT across template success-rate bins. Exact bar counts are not fully recoverable from the supplied rendering, but the text provides the central results:

- GPT-4 achieved **100% success on only four templates**.
- GPT-3.5 achieved 100% on **none**.
- Models often completed only one variation of a template.

Similar high-level tasks can have very different practical difficulty. “Fork metaseq” may require one straightforward operation, whereas “Fork all repos from Facebook” involves repeated operations and is considerably harder.

### 4.4 Prompt-temperature replication result

**Table 5** reports GPT-3.5-Turbo-16K-0613 using CoT, no UA hint, and temperature **0.0**. Its success rate was **6.28%**. This is close to the **6.16%** result for the corresponding main configuration at temperature 1.0, although the paper does not provide a formal comparison.

### 4.5 Fuzzy-match evaluator validation

The authors manually examined **40 fuzzy-match examples**:

- GPT-4 agreed with human judgment on **39 of 40**, or **97.5%**.

Among **82 examples** requiring GPT-4 evaluation:

- **49 examples (60%)** involved dates or durations, where GPT-4 primarily had to recognize equivalent formats.

The researchers generated alternative date and duration formats and sampled negative examples to test this capability.

**Table 6** reports:

- `gpt-4-0613`: **100%** on 900 date examples and **100%** on 900 duration examples.
- `gpt-4-1106-preview`: **100%** on both sets of 900 examples.

Thus, both GPT-4 versions perfectly recognized the generated equivalent and non-equivalent date and duration formats in this test.

### 4.6 Qualitative errors

**Figure 11** visualizes two GPT-4 failures:

- On “Fork all Facebook repos,” a search for Facebook returns **0 projects** but **1 user**. The agent fails to move to the “Users” section, even though the accessibility tree exposes that option.
- In a map search, the accessibility tree already contains the entered term **“DMV area.”** The agent keeps issuing the same typing command until reaching the step limit.

The authors identify two broader failure modes:

- **Observation bias:** GPT-4 latches onto the first related information without checking whether it is the correct source. For “What is the top-1 best-selling product in 2022,” it uses recent best-selling information on the CMS homepage rather than generating the required historical report.
- **Failure to interpret fine-grained state:** Although GPT-4 can summarize observations, it may overlook small but operationally crucial details, including filled input fields and the previously executed action.

### 4.7 Comparison with earlier benchmarks

**Table 4** compares environments on dynamic interaction, realism, diversity of human tasks, and functional-correctness evaluation:

| Benchmark | Dynamic interaction | Realistic environment | Diverse human tasks | Functional correctness |
|---|---:|---:|---:|---:|
| Mind2Web | No | Yes | Yes | No |
| Form/QAWoB | No | Yes | Yes | No |
| MiniWoB++ | Yes | No | No | Yes |
| WebShop | Yes | No | No | Yes |
| ALFRED | Yes | No | No | Yes |
| VirtualHome | No | No | Yes | No |
| AndroidEnv | Yes | Yes | No | No |
| WebArena | **Yes** | **Yes** | **Yes** | **Yes** |

WebArena is the only listed benchmark marked positively on all four dimensions.

## 5. Analysis and Interpretation

The low success rates demonstrate that strong language models still struggle with realistic, long-horizon web interaction. The primary difficulty is not merely understanding individual page elements. Agents must explore, plan across many steps, track changing state, integrate information across pages or websites, recover from mistakes, repeat operations reliably, and recognize when a task is genuinely impossible.

Chain-of-thought reasoning helps somewhat, as seen in GPT-3.5’s 2.34-point gain with the UA hint, but it does not close the large gap with humans. Explicit reasoning therefore does not by itself provide robust execution.

The UA-hint ablation shows that small prompt changes can substantially alter interactive behavior. A safety-oriented instruction to abstain on impossible tasks makes agents more accurate on unachievable cases but can suppress exploration and cause feasible tasks to be abandoned prematurely.

The inconsistent performance among instances of the same template suggests that agents do not reliably learn or reuse a general procedure. Small changes in content or the number of repeated operations can turn a successful plan into a failure. The authors therefore point to memory systems that retain and reuse successful strategies as a promising direction.

The qualitative failures further suggest weak active exploration and error recovery. GPT-4 often accepts readily visible but insufficient evidence, misses small changes in an accessibility tree, forgets what it just did, or repeats actions that the page state shows have already been completed.

The authors hypothesize that these weaknesses may be connected to dialogue-oriented pretraining and supervised fine-tuning. Dialogue models are commonly trained to respond to immediate observations, while interactive web tasks demand sustained exploration and sensitivity to small state differences. In ordinary dialogue, minor wording changes may not matter much; in a browser, a small change can determine the correct next action.

The comparison with related work positions WebArena as a venue for testing methods involving:

- Hierarchical planning and decomposition.
- Program-like representations of task execution.
- Search and backtracking.
- Memory and reuse of successful skills.
- Failure recovery and self-correction.
- Observation summarization.
- Screenshot-based or other multimodal interaction.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- **A realistic, standalone web environment:** WebArena provides self-hosted, fully operational applications from e-commerce, social forums, software collaboration, and content management.
- **Reproducibility:** Dockerized sites contain their code, databases, dependencies, and data and can be reset to deterministic initial states.
- **Authentic data and functionality:** The environment imports sampled real-world content and reproduces both popular public projects and personal user histories.
- **Utility and knowledge integration:** Agents can use a map, calculator, scratchpad, offline Wikipedia, and application manuals as independent websites.
- **Multi-tab interaction:** Agents can work across tabs for comparison, information transfer, and tool use.
- **Flexible observations and actions:** WebArena supports screenshots, DOM trees, accessibility trees, viewport restrictions, coordinates, and element-ID actions.
- **User-specific roles and histories:** The environment models permissions, private content, purchase history, and platform-specific identities rather than assuming identical users.
- **A large, realistic benchmark:** It contains **812 instantiated tasks from 241 templates**, covering information seeking, navigation, and state-changing operations.
- **Functional outcome evaluation:** Answers, page content, URLs, and databases are checked directly, allowing multiple valid action paths.
- **Unachievable-task evaluation:** The benchmark tests whether an agent can abstain rather than invent an answer.
- **Empirical evidence of the remaining difficulty:** The best GPT-4 agent reaches only **14.41%**, compared with **78.24%** for humans.
- **A framework for measuring progress:** The authors release code, data, reproduction resources, execution trajectories, and video demonstrations.

## 7. Limitations and Caveats

The paper identifies or implies several constraints:

- WebArena reproduces only four major application categories plus selected tools; it does not cover the full diversity of the internet.
- Realism is based on sampled and locally hosted data rather than continuously changing live services.
- The map is restricted to the northeastern United States because of storage constraints.
- Offline English Wikipedia has a **May 2023 cutoff**, so later information is unavailable.
- Resetting a modified site takes from a few seconds to one minute. The authors regard this as a small but non-negligible evaluation overhead.
- Human performance was measured with only **five computer-science graduate students** on **170 tasks**, not all 812 benchmark examples. Their technical background may not represent the general public.
- Many tasks require specialized knowledge, such as GitLab or CMS concepts, so human success may vary by demographic and expertise.
- Human performance itself was only **78.24%**, showing that the benchmark includes ambiguity, execution complexity, or expertise demands that can challenge people.
- GPT-4 is part of the fuzzy-match evaluator, creating a model-based rather than entirely rule-based evaluation component. The authors validate it strongly—39/40 agreement with humans and 100% on generated date/duration tests—but the manual check covers only 40 cases.
- The main agent experiments use one observation format: accessibility trees with element IDs. Although WebArena supports screenshots and DOM input, the reported baseline results do not compare these modalities.
- The main study tests three particular model versions and two few-shot prompting strategies. It does not exhaustively evaluate other planning, memory, search, backtracking, or multimodal techniques.
- The 30-transition cap and early-termination rules can prevent completion of especially long or repetitive tasks, although they are intended to stop executions likely already to have failed.
- High temperature encourages exploration but introduces stochasticity. A temperature-zero replication is supplied only for GPT-3.5 in one configuration.
- The paper reports success rates but no confidence intervals or formal significance tests.
- Static reproduction avoids CAPTCHAs and uncontrolled site changes, but consequently does not test agents against those real-web difficulties.
- Distinct instances of one template vary considerably in difficulty, so template-level semantic similarity does not ensure comparable execution complexity.

## 8. Future Work or Open Questions

The paper calls for research that makes autonomous agents more robust and effective in WebArena. Specific directions discussed include:

- **Active exploration:** agents should seek additional evidence instead of accepting the first plausible information.
- **Failure recovery and self-correction:** agents need to detect when an action failed and revise their approach.
- **Memory:** successful strategies from previous tasks could be stored and reused across related template instances.
- **Hierarchical planning:** long goals could be decomposed into manageable subgoals.
- **Program-like task representations:** plans expressed as reusable procedures may improve subtask management and skill reuse.
- **Search and backtracking:** agents could reconsider earlier decisions rather than proceeding irreversibly.
- **Improved state tracking:** systems should attend to previously performed actions, populated fields, tab state, and subtle observation changes.
- **Observation summarization:** compact state representations may help agents maintain relevant information over long trajectories.
- **Multimodal interaction:** screenshot-based agents and other combinations of visual and structured observations can be evaluated using WebArena’s flexible representations.
- **Better handling of impossibility:** future systems must distinguish genuinely unachievable tasks from feasible tasks requiring more exploration, avoiding both hallucination and premature abstention.
- **More consistent skill transfer:** agents should apply a successful procedure reliably across task variants, including cases with many repeated operations.

The broader open question is how to create agents that can combine language understanding with durable planning, precise perception, exploration, and reliable action over extended real-world workflows.

## 9. High-Level Takeaway (Plain Language)

WebArena is a locally hosted imitation of several real kinds of websites, built so researchers can test browser-controlling AI agents fairly and repeatedly. Its 812 tasks ask agents to do realistic multi-step work—searching personal records, navigating sites, editing repositories, posting content, or combining information across websites—and success is judged by whether the desired result actually occurred. Current systems are far from dependable: the best GPT-4 setup completed only **14.41%** of tasks, versus **78.24%** for people. The central message is that producing plausible language and isolated actions is not enough; useful web agents must explore, remember state, plan across many steps, verify evidence, recover from mistakes, and know when a request truly cannot be completed.