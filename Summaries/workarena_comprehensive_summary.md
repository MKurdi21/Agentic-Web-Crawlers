# WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?

**Authors:** Alexandre Drouin, Maxime Gasse, Massimo Caccia, Issam H. Laradji, Manuel Del Verme, Tom Marty, Léo Boisvert, Megh Thakkar, Quentin Cappart, David Vazquez, Nicolas Chapados, and Alexandre Lacoste  
**Published in:** Proceedings of the 41st International Conference on Machine Learning (ICML), 2024

## 1. Background and Context

Graphical user interfaces are the main way people interact with software. Although familiar components such as forms, menus, lists, and buttons make software more approachable, complex or repetitive interface-based work can still be burdensome. Such interfaces may also create accessibility barriers, especially for visually impaired users.

Programmatic interfaces, or APIs, can automate software operations, but they are not always available. API-based automation may also be difficult for users to inspect. In contrast, a UI assistant visibly operates the same interface as the user. This makes its actions easier to observe and lets the user take control back at any time. UI assistants could therefore provide anything from partial help—finding a menu or filling a form—to complete task execution, such as placing an order.

Recent language and vision models have enabled web agents that operate browser interfaces. Earlier benchmarks span:

- MiniWoB: 125 synthetic tasks ranging from clicking buttons to using a text editor.
- WebShop: shopping tasks on a simulated e-commerce site.
- WebArena: 190 task specifications on realistic sites covering e-commerce, forums, software development, and content management. Its reported success rates were 14% for a GPT-4 agent and 78% for humans.
- Mind2Web: 2,000 human-curated web interactions from 137 sites.
- WebLINX: 2,337 expert demonstrations from 155 real-world sites, with an average of 43 dialogue interactions per task.
- WebVoyager: 300 information-retrieval tasks from 15 consumer websites.
- Mobile-interface datasets such as PixelHelp, Android in the Wild, and Macro Mining.

However, enterprise software had received relatively little attention. Such software supports repetitive workplace processes but often prioritizes functionality over usability, producing long learning curves and complicated interfaces.

The paper addresses this gap through ServiceNow, a cloud-based platform supporting IT service management, human resources, customer service, security operations, and other enterprise workflows. In 2023, ServiceNow served more than 7,000 companies, including 85% of Fortune 500 firms. The paper estimates that these firms alone potentially expose more than 12 million people to the platform, apart from public-facing services such as Disney+’s customer help center, reported to have 500,000 daily users.

The authors argue that enterprise web agents could improve accessibility, user experience, and productivity, but realistic evaluation requires tasks involving large pages, unfamiliar HTML, dynamic controls, and complete workplace workflows.

---

## 2. Research Goal and Objectives

The paper has two central goals:

1. **Create a realistic enterprise benchmark:** WorkArena measures whether web agents can complete common knowledge-work tasks in ServiceNow.
2. **Create a unified experimentation environment:** BrowserGym supports the development and evaluation of agents using textual, visual, coordinate-based, and code-based browser interactions.

The empirical objectives are to:

- Measure how well GPT-4o, GPT-3.5, and Llama3-70B perform as general-purpose, zero-shot web agents.
- Compare WorkArena’s difficulty with MiniWoB and WebArena.
- Measure the value of BrowserGym features through ablation experiments.
- Compare closed-source and open-source language models.
- Test whether adding screenshots and visual grounding improves browser-agent performance.
- Determine which agent-design choices—reasoning, history, coordinates, visibility metadata, action descriptions, and multi-action execution—help or hurt.

---

## 3. Methods (Approach/Design)

### 3.1 WorkArena benchmark

WorkArena contains **33 task types and 19,912 unique instances** covering six categories of ServiceNow interaction:

| Category | Task types | Instances |
|---|---:|---:|
| Lists | 12 | 6,900 |
| Forms | 5 | 5,000 |
| Knowledge bases | 1 | 1,000 |
| Service catalogs | 9 | 3,550 |
| Dashboards | 4 | 1,862 |
| Menus | 2 | 1,600 |
| **Total** | **33** | **19,912** |

Every instance begins with an explicit natural-language instruction generated from a human-written template populated with predefined values such as field names, menu names, product options, or target values.

Tasks contain two important mechanisms:

- **Validation functions** provide real-time feedback and detect errors, from missing mandatory fields to invalid database entries.
- **Oracle functions** are hand-written Playwright solutions that automatically complete tasks. They confirm feasibility, provide ground truth for learning agents, and help maintain the benchmark when ServiceNow changes.

Oracle action counts estimate task complexity, but the authors caution that hand-coded solutions are not necessarily optimal. Counts were averaged over 10 randomly sampled instances.

#### Lists

There are six filtering and six sorting tasks, each applied to a different table such as users, incidents, hardware, or service-catalog items.

- Filters contain 1–5 conditions.
- Sorting uses as many as three columns.
- Agents must expose hidden controls, create the correct number of conditions, fill them, and apply the result.
- Validation checks the resulting list on the client side.

Because list and form parameters produce very large combinatorial spaces, applicable tasks were capped at 1,000 randomly selected instances.

List tasks and oracle actions:

- FilterAssetList: 1,000 instances; 17.3 ± 6.5 actions.
- FilterChangeRequestList: 1,000; 18.7 ± 4.7.
- FilterHardwareList: 1,000; 18.4 ± 5.6.
- FilterIncidentList: 1,000; 16.2 ± 4.2.
- FilterServiceCatalogItemList: 1,000; 19.9 ± 5.9.
- FilterUserList: 1,000; 12.7 ± 3.2.
- SortAssetList: 150; 7.4 ± 2.3.
- SortChangeRequestList: 150; 7.7 ± 1.6.
- SortHardwareList: 150; 8.0 ± 2.3.
- SortIncidentList: 150; 8.0 ± 2.7.
- SortServiceCatalogItemList: 150; 8.3 ± 2.5.
- SortUserList: 150; 7.7 ± 2.1.

#### Forms

Each form task creates a database entry. Forms require between 1 and 26 fields and may involve hidden tabs, dynamic requirements, autocomplete fields, and date pickers. Validation retrieves the created entry from the database and checks its values.

- CreateChangeRequest: 1,000 instances; 21.5 ± 6.2 oracle actions.
- CreateIncident: 1,000; 23.0 ± 7.9.
- CreateHardwareAsset: 1,000; 47.1 ± 10.9.
- CreateProblem: 1,000; 10.0 ± 3.4.
- CreateUser: 1,000; 17.9 ± 5.2.

#### Knowledge-base retrieval

The agent searches the knowledge base, opens relevant articles, extracts a fact, and responds through chat. Validation accepts a predefined set of semantically equivalent formats—for example, “8.5/10,” “85%,” or “8.5 out of 10.”

The knowledge base contains **100 GPT-4-generated articles**, each built around one item–value fact. Examples include:

- Conference-room A-561 password: `roo918k`.
- Office #456 address: `42, Pizza street, New York, USA`.
- CEO’s name: Alex Johnson.

Each generated HTML article was required to contain the exact fact. For every fact, GPT-4 generated ten alternative questions and formatting instructions. GPT-3.5 then attempted each question against the article; failures were sent back to GPT-4 for revision. GPT-3.5 was used for this check to avoid having GPT-4 generate questions tailored to itself.

GPT-4 also generated ten acceptable answer formats for each value. The authors supplied examples and manually inspected the outputs for coherence. For the office address, acceptable variants include “42 Pizza Street, New York, USA,” “42, Pizza St., NY, United States,” and equivalent formulations.

KnowledgeBaseSearch has 1,000 instances and requires 4.0 ± 0.0 oracle actions.

#### Service catalogs

These tasks require locating a product, configuring it, setting a quantity, and submitting an order. Validation checks the created order in the database.

- OrderDeveloperLaptopMac: 1,000 instances; 8.7 ± 0.9 actions.
- OrderIpadMini: 80; 6.0 ± 0.0.
- OrderIpadPro: 60; 6.0 ± 0.0.
- OrderSalesLaptop: 1,000; 9.0 ± 0.8.
- OrderStandardLaptop: 1,000; 8.0 ± 0.6.
- OrderAppleWatch: 10; 4.0 ± 0.0.
- OrderAppleMacBookPro15: 10; 4.0 ± 0.0.
- OrderDevelopmentLaptopPC: 40; 6.0 ± 0.0.
- OrderLoanerLaptop: 350; 8.0 ± 0.0.

#### Dashboards

Four tasks extract values from charts, sometimes with simple reasoning such as finding a minimum or maximum. Complexity varies according to whether the page contains one or several charts. Validation checks the response for the necessary labels and numbers.

- SingleChartValueRetrieval: 1,000 instances; 1.0 ± 0.0 action.
- SingleChartMinMaxRetrieval: 346; 1.0 ± 0.0.
- MultiChartValueRetrieval: 444; 2.0 ± 0.0.
- MultiChartMinMaxRetrieval: 72; 2.0 ± 0.0.

#### Menus

- AllMenu requires navigating to a specified application or module: 1,000 instances; 3.0 ± 0.0 actions.
- Impersonation requires logging in as a specified user: 600 instances; 7.0 ± 0.0 actions.

### 3.2 Why WorkArena is technically difficult

The benchmark deliberately exposes agents to characteristics of real enterprise software:

- **Dynamic interfaces:** Changing one field may reveal or require another. For example, resolving an incident requires resolution notes. Right-clicking may open context-specific menus.
- **Non-standard HTML:** Pages contain nested iFrames, shadow DOMs, proprietary JavaScript APIs, and custom HTML tags.
- **Very large pages:** Cleaned flat HTML ranges from approximately **40,000 to 500,000 tokens**, creating long-context problems even when the conceptual task is simple.
- **Limited accessibility:** Some enterprise controls do not follow standard or accessibility-oriented interface practices.

WorkArena is open source. Tasks run on free, cloud-based ServiceNow Personal Developer Instances, while the benchmark itself contains no proprietary ServiceNow code.

### 3.3 BrowserGym

BrowserGym is an OpenAI Gym environment following a **partially observable Markov decision process**: at each step, the agent observes only the current browser state, so any longer-term memory must be implemented by the agent.

It uses Chromium, Chrome DevTools Protocol, and Playwright.

#### Observations

At each step, BrowserGym can provide:

- The chat history.
- Open pages and URLs.
- The most recent action error and stack trace.
- An HTML DOM snapshot.
- The accessibility tree, or AXTree.
- A viewport screenshot.
- A unique browser identifier (`bid`) for each element.
- Each element’s bounding box.
- Flags indicating whether the element is visible or clickable.

The DOM and AXTree can be converted to text for an LLM or combined with the screenshot for a vision-language model.

#### Actions

BrowserGym supports:

- Identifier-based actions: fill, click, double-click, hover, press keys, focus, clear, select options, and drag-and-drop.
- Coordinate actions: mouse movement, button down/up, clicks, double-clicks, drag-and-drop, keyboard presses, typing, and text insertion.
- Tab operations: open, close, or focus a tab.
- Navigation: back, forward, or go to a URL.
- Scrolling.
- Sending a message to the user.
- No operation.
- Arbitrary Python and Playwright code, marked unsafe because it gives broad execution access.

It handles multiple tabs, popups, nested iFrames, and shadow DOMs.

#### Benchmark creation

A new task requires up to four functions:

- `setup()` initializes data, authentication, and the starting page.
- `teardown()` removes created resources.
- `validate()` determines success and returns a reward, optional chat message, and completion flag.
- `cheat()` is an optional oracle solution.

BrowserGym supports WorkArena, WebArena, and a MiniWoB port. MiniWoB required only moving its on-page goal into BrowserGym’s chat and removing the hard episode time limit.

### 3.4 Agent design

The authors implemented one configurable chain-of-thought web-agent codebase. A generic example—not task-specific examples—showed the model how to format reasoning and actions, preserving a zero-shot setting.

The agent could use:

- Current goal.
- HTML and/or AXTree.
- Focused element.
- Last action error.
- Visibility and clickability tags.
- Center or box coordinates.
- Action history.
- Error history.
- Previous reasoning history.
- Single or multiple actions per step.
- Identifier-only or identifier-plus-coordinate actions.
- Short or long primitive descriptions.
- Individual action-call examples.

On WorkArena and WebArena, only AXTree was used because HTML was prohibitively large. MiniWoB used both AXTree and HTML because that combination performed best.

A parser could re-prompt the model up to four times after malformed output. Parsed actions were then executed by BrowserGym.

### 3.5 Models

The evaluated models were:

- GPT-4o, version `gpt-4o-2024-05-13`, with a nominal 128K context.
- GPT-3.5, version `gpt-3.5-turbo-1106`, with 16K context.
- Open-source Llama3-70B-Instruct with 8K context, deployed using Hugging Face Text Generation Inference on four A100 GPUs.
- GPT-4o-V, which added the current screenshot and Set-of-Mark visual annotations to GPT-4o.

Actual prompt limits were 40K tokens for GPT-4o, 15K for GPT-3.5, and 8K for Llama3. Oversized HTML or AXTree text was progressively truncated from the end.

### 3.6 Final model configurations

All three final agents used:

- Chain-of-thought reasoning.
- Action history.
- Identifier-based actions.
- Individual action examples.
- Single-action steps.
- Visibility tags.
- No coordinate metadata.
- No “only visible elements” filter.

Differences included:

- GPT-4o used the last error, clickable tags, and long action descriptions.
- GPT-3.5 used the last error, but not clickable tags or long descriptions.
- Llama3 used prior reasoning history and the focused element, but not the last error, clickable tags, or long descriptions.
- No final agent used full error history.

### 3.7 Experimental protocol

- BrowserGym version: 0.3.5.
- WorkArena version: 0.3.0.
- Maximum steps: **15 per episode**.
- Seeds: 10 per task for MiniWoB and WorkArena; one per WebArena task.
- Success rates and standard errors were computed using a stratified bootstrap with 1,000 samples of the mean.
- Each model’s flags were selected through random search on MiniWoB and WorkArena.
- Final configurations were evaluated with a different seed.
- WebArena was not used for tuning because it is deterministic.
- Some WorkArena tasks may require more than 15 steps unless multi-action mode is used.

---

## 4. Results and Findings

### 4.1 Main benchmark results

| Benchmark/category | GPT-4o | GPT-4o-V | GPT-3.5 | Llama3 |
|---|---:|---:|---:|---:|
| **WorkArena, 33 tasks** | **42.7 ± 1.5%** | **41.8 ± 1.7%** | **6.1 ± 1.3%** | **17.9 ± 1.5%** |
| Dashboards | 62.5 ± 6.8 | 72.5 ± 6.0 | 20.0 ± 4.8 | 37.5 ± 6.0 |
| Forms | 40.0 ± 5.9 | 34.0 ± 4.8 | 2.0 ± 2.5 | 32.0 ± 4.6 |
| Knowledge base | 80.0 ± 12.2 | 70.0 ± 13.9 | 0.0 ± 4.3 | 30.0 ± 12.3 |
| List filtering | 0.0 ± 1.6 | 0.0 ± 1.7 | 0.0 ± 1.6 | 0.0 ± 1.8 |
| List sorting | 10.0 ± 3.8 | 13.3 ± 4.0 | 8.3 ± 3.7 | 1.7 ± 2.5 |
| Menus | 60.0 ± 8.0 | 90.0 ± 6.0 | 5.0 ± 4.7 | 0.0 ± 2.9 |
| Service catalogs | 77.8 ± 3.2 | 65.6 ± 3.6 | 5.6 ± 2.3 | 26.7 ± 3.4 |
| **MiniWoB, 125 tasks** | **66.1 ± 1.0** | **67.7 ± 1.0** | **38.9 ± 1.1** | **62.6 ± 0.6** |
| WebGum subset, 56 tasks | 82.9 ± 1.5 | 83.2 ± 1.5 | 53.6 ± 1.4 | 80.5 ± 1.0 |
| **WebArena, 812 instances** | **23.5 ± 0.7** | **24.0 ± 0.6** | **6.7 ± 0.6** | **11.0 ± 0.6** |
| Content/configuration | 25.8 ± 1.0 | 26.8 ± 0.9 | 8.8 ± 0.8 | 12.7 ± 0.9 |
| Information seeking | 22.5 ± 1.0 | 22.5 ± 0.9 | 4.3 ± 0.9 | 9.8 ± 1.1 |
| Navigation | 15.8 ± 2.2 | 15.8 ± 1.8 | 5.3 ± 1.9 | 6.6 ± 1.9 |

The principal findings were:

- GPT-4o was substantially stronger than GPT-3.5 and Llama3 on every benchmark.
- The difference was particularly large on WorkArena: **42.7% versus 6.1% and 17.9%**.
- No agent solved every instance of any single WorkArena task.
- List filtering produced an unambiguous **0% success rate for every model**, despite being straightforward for humans.
- GPT-4o was strongest at knowledge retrieval and service-catalog orders but remained weak on lists and only moderately successful on forms.
- Llama3 substantially outperformed GPT-3.5 overall on WorkArena despite its shorter 8K context.
- Preliminary Llama2 experiments achieved 0% on both WorkArena and WebArena.
- GPT-4o’s WebArena score of 23.5% was presented as the best reported zero-shot result at the time and exceeded the original GPT-4 result of 14.4%.
- GPT-4o’s 82.9% on the MiniWoB WebGum subset also exceeded earlier zero-shot web-agent results cited by the paper.

### 4.2 Vision-augmented GPT-4o

Adding screenshots and Set-of-Mark annotations did not consistently improve performance:

- WorkArena fell slightly from 42.7% to 41.8%.
- MiniWoB rose from 66.1% to 67.7%.
- WebArena rose from 23.5% to 24.0%.

Category effects varied. Vision improved dashboards from 62.5% to 72.5% and menus from 60% to 90%, but reduced forms from 40% to 34%, knowledge retrieval from 80% to 70%, and service catalogs from 77.8% to 65.6%.

The authors therefore characterize multimodal performance as disappointing rather than a clear advance.

### 4.3 Ablation results

The ablations used a different random seed, so their initial scores differ from the main table.

#### GPT-4o

Initial performance was 68.2 ± 1.0% on MiniWoB and 45.5 ± 2.2% on WorkArena.

- Multiple actions: 68.5 ± 1.0; 40.6 ± 2.0.
- Box coordinates plus coordinate actions: 72.6 ± 1.0; 41.2 ± 1.8.
- Prior reasoning history: 66.7 ± 0.9; 42.4 ± 2.3.
- Full error history: 67.2 ± 0.9; 43.6 ± 2.1.
- Removing visibility tags: 68.8 ± 1.0; 43.0 ± 2.2.

Coordinates clearly helped MiniWoB but hurt WorkArena. Memory, error history, multi-action execution, and removing visibility metadata also failed to improve WorkArena.

#### GPT-3.5

Initial performance was 41.3 ± 1.1% on MiniWoB and 8.5 ± 1.3% on WorkArena.

- Removing reasoning: 30.2 ± 1.0; 6.1 ± 1.2.
- Removing action history: 34.1 ± 1.1; 5.2 ± 1.3.
- Adding reasoning history: 36.2 ± 1.2; 3.0 ± 1.0.
- Adding error history: 37.9 ± 1.0; 7.0 ± 1.4.
- Multiple actions: 41.4 ± 1.1; 9.4 ± 1.5.
- Only visible elements: 38.1 ± 1.0; 5.8 ± 1.3.
- Long action descriptions: 39.5 ± 1.0; 6.4 ± 1.2.
- Removing individual examples: 34.4 ± 1.0; 8.2 ± 1.3.
- Center coordinates and coordinate actions: 40.8 ± 1.1; 4.5 ± 1.1.
- Box coordinates and coordinate actions: 40.5 ± 1.2; 6.1 ± 1.4.
- Focused-element information: 40.3 ± 1.1; 9.4 ± 1.5.
- Removing visibility tags: 37.8 ± 1.0; 6.7 ± 1.3.
- Adding clickability tags: 37.9 ± 1.1; 7.6 ± 1.2.

#### Llama3

Initial performance was 59.8 ± 1.0% on MiniWoB and 20.0 ± 2.3% on WorkArena.

- Removing reasoning: 48.6 ± 1.1; 8.5 ± 1.7.
- Removing action history: 49.9 ± 1.1; 8.5 ± 1.7.
- Removing reasoning history: 52.2 ± 1.1; 18.8 ± 2.1.
- Multiple actions: 63.0 ± 1.0; 17.6 ± 2.1.
- Long descriptions: 55.5 ± 1.0; 17.6 ± 2.0.
- Adding the last error: 60.2 ± 1.1; 19.4 ± 1.8.
- Removing visibility tags: 61.3 ± 0.9; 15.8 ± 2.0.

### 4.4 Main design findings

- **Chain-of-thought was crucial.** Removing it hurt every model. For Llama3, WorkArena dropped from 20.0% to 8.5%, while MiniWoB dropped from 59.8% to 48.6%.
- **Action history was also important.** Removing it reduced Llama3 to 8.5% on WorkArena.
- **More prompt content was not necessarily better.** Long descriptions, extra examples, coordinates, or additional metadata could distract weaker models and force more truncation.
- **Reasoning memory could hurt.** Agents sometimes reused useful information from earlier pages, but they also became attached to early mistakes and corrected themselves less readily. Most benchmark tasks did not require cross-page memory because relevant information remained on the current page.
- **Two-dimensional actions were task dependent.** Coordinate features improved GPT-4o on MiniWoB from 68.2% to 72.6%, reflecting tasks that require drawing or spatial clicks. They reduced WorkArena performance from 45.5% to 41.2%, suggesting identifier-based actions were sufficient for most enterprise interactions.
- **Multi-action execution did not reliably help.** It reduced GPT-4o’s WorkArena performance, slightly improved GPT-3.5, and improved Llama3 only on MiniWoB.

### 4.5 Figures and visual evidence

- **Figure 1:** Contrasts the two contributions. WorkArena covers workspace pages, lists, forms, dashboards, knowledge bases, and service catalogs. BrowserGym places a browser and web agent in an observation–action loop and can supply HTML, AXTree, and screenshots while accepting identifier-based, coordinate-based, or Python/Playwright actions.
- **Figure 2:** Gives explicit sample goals for all six categories: filter a high-priority list, create a named user, retrieve a conference-room password, configure an iPad Pro, read a manufacturer percentage, and navigate through a menu.
- **Figure 3:** Shows a hardware-asset form. The agent must create a computer asset with a specified model, vendor, installation date, and serial number. Red annotations identify autocomplete fields, fields hidden behind tabs, and a date picker.
- **Figure 4:** Uses violin plots on a logarithmic token-count axis to compare pruned HTML and AXTree sizes across MiniWoB, WorkArena, and WebArena. MiniWoB observations are substantially smaller. WorkArena and WebArena are much larger, and AXTree generally reduces the size relative to HTML while remaining far larger than MiniWoB. Exact plotted values are not printed clearly enough to extract beyond the paper’s stated 40K–500K HTML range.
- **Figure 5:** Shows the difficult incident-filter widget. The agent must open the filter menu, add separate Priority = Critical and Category = Hardware conditions, then press Run.
- **Figure 6:** Shows knowledge-base retrieval: search, inspect result articles, read the relevant text, and reply in chat. The example asks for the CEO’s complete phone number and returns `+1 (555) 101-2020`.
- **Figure 7:** Shows a service-catalog task requiring five Developer Laptop (Mac) units with specified Adobe Acrobat, Eclipse IDE, Adobe Photoshop, and additional-software settings. The agent navigates to the item, configures options and quantity, then selects Order Now.
- **Figure 8:** Shows dashboard retrieval. The agent locates the “Configuration Item by Manufacturer” chart, reads Hewlett-Packard’s share, and replies **4.72%**.
- **Figure 9:** Shows menu navigation to the Open module of the Problem application. The agent opens All, searches, and selects the correct item while avoiding similarly named Open modules.
- **Figure 10:** Shows a generated knowledge article in which the fact that conference-room A-561’s password is `roo918k` is embedded and highlighted.
- **Figure 11:** Shows a MiniWoB angle-bisector drawing task rendered in BrowserGym, with the instruction moved into the chat interface.

---

## 5. Analysis and Interpretation

WorkArena exposes a substantial gap between the apparent simplicity of a workplace instruction and the difficulty of executing it through a real interface. Tasks such as filling a form, choosing a menu, or filtering a list require ordinary knowledge at a conceptual level. The main difficulty comes from long observations, non-standard controls, dynamic fields, hidden menus, nested document structures, and extended action sequences.

The much larger model gap on WorkArena and WebArena than on MiniWoB supports the authors’ view that advanced web behavior emerges mainly in very capable models. GPT-4o’s strong lead suggests that interface automation requires a combination of instruction following, coding knowledge, long-context processing, and error recovery.

The universal failure on list filtering is especially important. It shows that overall benchmark scores can conceal total inability on particular interaction patterns. The obstacle is not the logical meaning of filtering, but the implementation of the filter through an unfamiliar HTML widget.

The Llama3 results provide qualified encouragement for open-source models. Llama3 was well behind GPT-4o, but it greatly exceeded GPT-3.5 on WorkArena and performed close to GPT-4o on MiniWoB despite having the shortest context. This contrasts with the authors’ preliminary Llama2 result of zero on both realistic benchmarks.

The ablations show that agent design must be selective:

- Explicit reasoning and action history are foundational.
- Extra context can become noise.
- Long prompts are particularly harmful when they trigger truncation.
- Memory is useful only when tasks truly require information to persist across pages.
- Spatial coordinates are valuable for inherently spatial tasks, but unnecessary for most ordinary web controls.
- Screenshots do not automatically yield better performance; contemporary vision-language models may not make effective use of screen imagery.

The authors attribute BrowserGym’s strong WebArena and MiniWoB performance to its combination of structured observations, identifiers, flexible actions, parsing retries, and a carefully tuned agent configuration.

---

## 6. Contributions and Novelty

The paper’s principal contributions are:

- **WorkArena:** A realistic, open-source benchmark with 33 enterprise task types and 19,912 instances based on knowledge workers’ ServiceNow workflows.
- **Real-world enterprise coverage:** Tasks include filtering and sorting, record creation, knowledge retrieval, product ordering, chart reading, navigation, and user impersonation.
- **Automatic validation and oracles:** Each task can supply live validation, while hand-crafted Playwright solutions verify feasibility and aid future maintenance.
- **BrowserGym:** A general-purpose environment unifying HTML, AXTree, screenshots, Set-of-Mark, chat, element identifiers, screen coordinates, high-level actions, and arbitrary Playwright code.
- **Chat-based interaction:** The authors identify BrowserGym as the first environment of its type to support agent–user chat directly.
- **Cross-benchmark evaluation:** MiniWoB, WebArena, and WorkArena can be run through the same interface.
- **Empirical comparison:** The study quantifies the large performance gap among GPT-4o, GPT-3.5, and Llama3.
- **Agent-design evidence:** Ablations clarify the roles of reasoning, history, coordinates, visibility metadata, screenshots, action examples, descriptions, and multi-action steps.
- **Improved benchmark results:** The GPT-4o agent reached 23.5% on WebArena versus the original paper’s 14.4% GPT-4 result, and 82.9% on the MiniWoB WebGum subset.
- **A platform for capability measurement:** WorkArena’s difficulty and model separation make it useful for tracking emerging abilities that are less visible on simpler benchmarks.

---

## 7. Limitations and Caveats

### Experimental limitations

- Only three principal language models were studied, plus a vision-augmented GPT-4o variant.
- The scope was limited to LLM-based reasoning agents.
- WorkArena uses one enterprise platform, ServiceNow, so the findings do not directly establish performance on every enterprise application.
- Agents were limited to 15 steps. The oracle table shows that some tasks—especially forms and filters—often require more, unless multiple actions are allowed per step.
- Only 10 seeds per task were used for MiniWoB and WorkArena and one per WebArena task because of budget limits.
- Ablation results used a different seed from the main results and therefore are not numerically identical.
- WorkArena’s combinatorial form and list spaces were capped at 1,000 randomly selected instances per applicable task.
- Oracle action counts measure one hand-written solution and may not represent the shortest possible path.
- Oversized observations were truncated from the end, potentially hiding relevant elements.
- GPT-3.5 and Llama3 were especially constrained by 15K and 8K prompt limits.
- Most benchmark tasks did not require substantial long-term memory, limiting conclusions about memory mechanisms for cross-page workflows.
- The multimodal experiment used one particular screenshot-plus-Set-of-Mark design; it did not show that all possible visual agent designs would perform similarly.
- Despite the reported gains, the best WorkArena agent succeeded on fewer than half of cases, and no model fully solved even one WorkArena task type.

### Benchmark caveats

- Knowledge articles and question variants were generated using language models, although the authors used cross-model checking, revisions, alternative-answer generation, and manual inspection.
- WorkArena goals are highly explicit and generated from templates. Ambiguous or evolving real user requests may be harder.
- Current tasks are mostly atomic rather than long, compositional workplace workflows.
- WorkArena depends on live ServiceNow Personal Developer Instances. Oracle functions help detect changes, but platform updates may still require maintenance.
- BrowserGym itself does not provide agent memory; developers must implement it.
- Arbitrary Python and Playwright actions are powerful but unsafe if not constrained.

### Societal risks and cautions

The paper identifies both benefits and risks:

- **Productivity:** Automating repetitive work could free people for more creative and complex activities.
- **Accessibility:** UI agents could expand workplace access for people with disabilities, including visual impairments.
- **Labor displacement:** Automation may disrupt jobs, although the authors expect role evolution rather than universal replacement. Benchmarks could help forecast affected work and support preemptive reskilling.
- **Cybersecurity:** Human-like agents could enable sophisticated attacks that mimic normal user interactions, motivating constrained models and stronger security.
- **Privacy:** Workplace agents may transmit sensitive organizational data, requiring further protection.
- **Environmental impact:** Large-scale LLM inference consumes substantial energy and poses challenges for widespread deployment.

---

## 8. Future Work or Open Questions

The authors propose:

- Adding more standard benchmarks to BrowserGym, specifically WebShop and WebVoyager.
- Expanding WorkArena with compositional tasks that combine the existing atomic tasks into realistic, longer workflows.
- Designing tasks that jointly require retrieval, memorization, visual perception, and advanced reasoning.
- Improving multimodal web agents, since adding screenshots currently yields only small or inconsistent gains.
- Closing the large performance gap between open- and closed-source models.
- Improving long-context reasoning for very large HTML and accessibility-tree observations.
- Developing memory mechanisms that preserve useful information without reinforcing early errors.
- Exploring when coordinate-based interaction is necessary and when element identifiers provide a simpler and more reliable design.
- Using WorkArena to track which workplace tasks are becoming automatable and to study potential real-world impact.
- Continuing research on cybersecurity, privacy, accessibility, energy use, and worker reskilling before large-scale workplace deployment.

An important open technical problem is the complete failure on non-standard list-filtering widgets. More broadly, the best model’s 42.7% WorkArena score leaves substantial room for progress in planning, robust interaction, context management, and self-correction.

---

## 9. High-Level Takeaway (Plain Language)

This paper tests whether AI agents can operate the complicated websites employees use at work. The authors built WorkArena, a collection of nearly 20,000 ServiceNow tasks, and BrowserGym, a toolkit that lets agents see and control browsers in several ways. GPT-4o was the strongest model but completed only about 43% of WorkArena cases, while every tested model completely failed at list filtering. The central lesson is that understanding a simple workplace request is not enough: reliably carrying it out through large, dynamic, non-standard interfaces remains an unsolved problem.