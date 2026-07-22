# *Mind2Web: Towards a Generalist Agent for the Web*

**Authors:** Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Samuel Stevens, Boshi Wang, Huan Sun, and Yu Su  
**Affiliation:** The Ohio State University  
**Venue:** NeurIPS 2023, Datasets and Benchmarks Track

## 1. Background and Context

The paper asks how to build a general-purpose web agent that can receive a natural-language instruction, navigate any website, and perform the requested task.

Such an agent could make complex websites easier to use, particularly for people unfamiliar with information technology or people with disabilities. It could also make the web a more powerful tool for large language models (LLMs), allowing them to retrieve information and perform actions directly through web interfaces instead of depending only on search systems or a separate predefined API for every service.

The authors argue that a genuinely general web agent must satisfy three requirements:

1. **Work on any website.** It must generalize to websites—and even entire subject domains—not represented in its training data.
2. **Handle real-world websites.** Websites are dynamic, noisy, complex, and only partially observable: their content changes in response to actions, and their full state is not known in advance.
3. **Support varied, sophisticated interactions.** Real tasks can require clicking, typing, selecting options, navigating several pages, and planning long action sequences. One example in the paper requires 14 actions.

Earlier web-agent datasets and systems do not satisfy all three requirements. They commonly use simplified simulations, cover a small predetermined set of sites or task types, make strong assumptions about page structure, or provide low-level step-by-step directions rather than high-level goals. Work on mobile interfaces generally covers simpler applications with fewer functions, while traditional web-automation tools often require programming skills.

The paper connects this problem to several research areas:

- **Large language models**, which can learn from few examples and interpret natural-language goals.
- **Grounded language understanding**, where language must be translated into executable actions in an environment.
- **Embodied AI**, although web environments are broader and more heterogeneous than the specific physical settings commonly studied.
- **Tool learning**, where an LLM invokes tools. Unlike short, isolated tool calls, web tasks can require long sequences of decisions.
- **Natural-language web automation**, which could lower the technical barrier associated with conventional automation systems.

The missing foundation, according to the authors, was a realistic, diverse dataset suitable for developing and testing generalist web agents.

## 2. Research Goal and Objectives

The paper has two main objectives:

1. **Introduce Mind2Web**, a dataset for training and evaluating agents that execute high-level natural-language tasks on diverse, real-world websites.
2. **Provide an initial model and empirical study**, called **MindAct**, to determine whether language models can select the correct web elements and operations, including on websites and domains not seen during training.

The evaluation explicitly studies three levels of generalization:

- New tasks on websites represented during training.
- Entirely new websites within familiar domains.
- Entirely held-out top-level domains.

The work also investigates whether filtering a very large webpage with a smaller language model makes subsequent LLM-based action prediction more effective and efficient.

## 3. Methods (Approach/Design)

### 3.1 The Mind2Web dataset

Mind2Web contains **2,350 retained tasks** from **137 real-world websites**, organized into **31 secondary domains** under five top-level categories:

- Travel
- Shopping
- Service
- Entertainment
- Information

Each task instance contains three components:

1. **Task description:** A high-level user goal rather than step-by-step instructions.
2. **Action sequence:** The ordered actions needed to complete the task. Each action pairs a target webpage element with an operation.
3. **Webpage snapshots:** Records of the environment at each step.

The core dataset operations are:

- **Click**, which also subsumes Hover and Press Enter in the final data.
- **Type**, with a text value.
- **Select Option**, with the selected value.

Tasks frequently extend across multiple pages. At each prediction step, the agent receives the initial task, the current webpage, and the history of preceding actions, and must predict the next target element and operation.

The webpage records include:

- Self-contained MHTML with raw HTML.
- A DOM snapshot including the DOM tree, layout, and rendered style information.
- HAR files containing network traffic.
- Trace files containing the complete annotation interaction.

These records were intended to support offline replay and multiple modeling approaches.

### 3.2 Dataset coverage shown in Figure 1

**Figure 1** illustrates the variety of tasks and the complete domain distribution. Its example tasks include:

- Finding a one-way flight from New York to Toronto.
- Booking a Mumbai–London round trip for two adults, leaving July 1 and returning July 5.
- Finding a Chicago–London flight leaving April 20 and returning April 23.
- Finding Elon Musk’s profile, following it, enabling notifications, and liking the latest tweet.
- Browsing comedy films on Netflix released between 1992 and 2007.
- Opening the page for scheduling a car knowledge-test appointment.

The examples demonstrate evaluation across:

- Different tasks on the same website.
- Similar tasks on different websites.
- Completely different tasks, sites, and domains.

The top-level task distribution is:

- **Travel: 27.4%**
- **Information: 20.4%**
- **Service: 18.3%**
- **Shopping: 17.5%**
- **Entertainment: 16.1%**

The 31 secondary-domain shares shown are:

- Travel: Other 6.2%, Airlines 5.8%, Restaurant 4.3%, Ground 3.7%, General 3.1%, Car Rental 2.4%, and Hotel 1.8%.
- Information: Housing 3.7%, Job 3.5%, Social Media 3.5%, Education 2.8%, Finance 2.7%, Cooking 2.9%, and Weather 1.9%.
- Service: Health 6.5%, Government 3.4%, Home Service 2.5%, Pet 2.1%, Shipping 1.8%, and Moving 1.7%.
- Shopping: Specialty 5.0%, Auto 3.4%, General 3.3%, Digital 2.3%, Department 1.6%, and Fashion 1.6%.
- Entertainment: Event 3.8%, Music 3.5%, Sports 3.5%, Movie 3.2%, and Game 2.0%.

### 3.3 Example task instance

**Figure 2** shows a full data instance whose goal is to display reviews for the auto-repair business closest to ZIP code 10002. Its ten recorded actions are:

1. Type “auto repair” into the Find search box.
2. Click Auto Repair.
3. Type “10002” into the Near field.
4. Click the 10002 suggestion.
5. Click Search.
6. Click the “Show BBB Accredited only” switch.
7. Click an SVG element.
8. Click Sort By.
9. Click “Fast Lane 24 Hour Auto Repair.”
10. Click “Read Reviews.”

The figure pairs actions with webpage snapshots and HTML representations of their target elements. Actions that transition to a new page are highlighted in red, illustrating how one task can span multiple webpage states.

### 3.4 Data collection

Collection proceeded in four stages.

#### Website selection

The authors began with the five top-level categories and divided them into 31 secondary domains. Websites were selected based on U.S. popularity rankings from Similarweb. The authors manually chose approximately **3–5 representative websites per domain**, producing **137 websites**.

#### Task proposal

Annotators received:

- A target website.
- A short website description.
- Example tasks.

They proposed realistic, open-ended tasks that:

- Varied in type.
- Required multiple interactions.
- Described the goal rather than the steps.

ChatGPT generated **50 seed tasks per website** to stimulate ideas. Ten were randomly displayed during each proposal assignment. Annotators were told not to copy them, and highly similar submissions were rejected.

**Table 3** gives an American Airlines seed-task prompt. It asks for single-sentence, concrete, realistic goals that cover different cases without naming interface elements or giving step-by-step directions. Sample outputs involve retrieving a reservation confirmation number, finding a constrained round-trip fare, searching for a low-layover flight, renting a suitably equipped car, and cancelling a reservation without a fee.

For each task-proposal HIT, an annotator selected a website, saw ten generated examples, and could suggest at most five tasks. Each proposal HIT paid **$0.05 regardless of acceptance**. An accepted task earned the full **$0.80** after successful demonstration. Once approximately 20 tasks had been collected for a website, that website stopped being offered, supporting balance and diversity.

#### Task demonstration

A Playwright-based annotation system recorded how workers performed accepted tasks.

**Figure 7** shows its two-window design:

- A dialogue/control window on the left for managing the interaction and choosing operations.
- A live browser on the right for navigating and selecting elements.

**Figure 8** summarizes the workflow:

1. Select a website and task.
2. Explore and prepare the website.
3. Begin task demonstration.
4. Select an element.
5. Select the operation.
6. Confirm the task and complete the demonstration.

Workers first practiced the task in an unrecorded exploration stage. They closed pop-ups, cleared CAPTCHAs, learned the site, and then reset it to a fresh state. Anonymous accounts were supplied where necessary so workers would not enter private information.

During recording, direct browser actions were blocked. For every step, the worker selected an element, the tool highlighted it without executing the click, and the worker then selected an operation in the dialogue window.

The annotation interface offered six choices:

- Click
- Type
- Hover
- Press Enter
- Click (Fake)
- Ignore

Type required a value, as illustrated by **Figure 9**, where text such as “New York” is entered for a selected destination field. If a selected HTML element was a dropdown and the worker chose Click, the interface converted this into Select Option and prompted for a value, as shown in **Figure 10**, whose example options include Toyota, Fiat, Lotus, and Bentley.

Hover and Press Enter were mapped to Click in the final dataset. **Click (Fake)** was recorded like a click but was not executed. It protected real systems from state-changing actions such as posting comments or scheduling appointments and could support a future confirmation step before execution. Ignore allowed a worker to recover from selecting the wrong element.

Pop-ups, CAPTCHA handling, ad closing, and other extraneous steps were deliberately excluded from the final demonstrations unless necessary. The authors acknowledge that these are real parts of dynamic websites, but removing them made evaluation cleaner and less ambiguous.

#### Verification

All demonstrations were manually checked by the authors.

**Figure 11** shows the verification interface, which displays the task, action sequence, individual elements, and corresponding webpage. Verifiers decided whether to:

- Discard a low-quality task.
- Remove unnecessary or incorrect actions.
- Revise the task description so it accurately represented the actions.

An “unsure” decision triggered re-evaluation by the first author.

Of **2,411 collected tasks**, **61 were discarded**, leaving **2,350**. Among the retained tasks:

- **390 task descriptions** were refined.
- Extraneous actions were removed from **187 instances**.

Initial and final states were normalized. For example, irrelevant pop-up-closing actions were removed, and a “find” task could end at the search results rather than clicking a particular item.

### 3.5 Annotators and ethics

Annotators came from Amazon Mechanical Turk and needed:

- At least **1,000 approved HITs**.
- An approval rate above **98%**.

Compensation was designed around an estimated rate of **$10.10 per hour**, corresponding to Ohio minimum-wage guidance. Qualified workers received a bonus, and approved final tasks paid $0.80.

Workers received training documentation, a video tutorial, a questionnaire, and test demonstrations. They provided consent. The study collected no identifying private information, instructed workers not to enter sensitive data, and operated through a secure remote sandbox. It met the Ohio State University office’s criteria for IRB exemption.

Quality control had two stages: the first author screened proposals, and all authors participated in final verification. Each demonstration was checked by one author, with uncertain cases escalated to the first author.

### 3.6 Comparison with other datasets

**Table 1** compares Mind2Web with six earlier datasets:

| Dataset | Domains | Environments | Environment type | Avg. elements | Tasks/data units | Task information | Avg. actions |
|---|---:|---:|---|---:|---:|---|---:|
| MiniWoB++ | Not given | 100 | Simplified mobile websites | 28 | 100 | Low-level | 3.6 |
| WebShop | 1 | 1 | Simplified shopping website | 38 | 12,000 products | High-level | 11.3 |
| RUSS | Not given | 22 | Real-world websites | 801 | 80 | High- and low-level | 5.4 |
| PixelHelp | 4 | 4 | Mobile apps | Not given | 187 | High- and low-level | Not given |
| META-GUI | 6 | 11 | Mobile apps | 79 | 1,125 dialogues | High-level | 4.3 |
| MoTIF | 15 | 125 | Mobile apps | 188 | 756 | High- and low-level | 4.4 |
| Mind2Web | 5 top-level/31 secondary | 137 | Real-world websites | 1,135 | 2,350 | High-level | 7.3 |

Mind2Web therefore combines unusually broad website and domain coverage with real pages, high-level goals, and relatively long action sequences. Its pages average **1,135 elements**, making them substantially longer and more structurally complex than the compared datasets.

### 3.7 MindAct architecture

Raw webpages can contain thousands of DOM elements and are too large or costly to send directly to an LLM. MindAct therefore uses two stages.

#### Stage 1: candidate generation

A smaller, fine-tuned language model ranks page elements. Its query combines:

- The task description.
- All previous actions.

Each candidate element is represented using:

- Its HTML tag.
- Text content.
- Salient attributes.
- Representations of its parent and child elements.

The model uses a **cross-encoder**, jointly processing the task query and candidate representation to produce a match score. During training:

- The true target is a positive example.
- Random page elements are negatives.
- A sigmoid converts the score to a probability-like value.
- Binary cross-entropy trains the classifier.

At inference, every element is scored and the top \(k\) elements are passed to stage two.

**Figure 3** depicts the complete flow: HTML, task description, and previous actions enter the ranking model; the top-ranked elements form a shortened HTML snippet; a prediction LLM then outputs the target and operation.

**Figure 4** illustrates the candidate-generation representation with a restaurant-reservation task. The candidate includes its ancestor path and a target button containing “Boston, NY, USA,” while the query includes the high-level goal and prior actions such as selecting Pickup and typing Boston.

#### Stage 2: action prediction

The second model sees only the shortlisted elements and their neighboring HTML. Element selection is reformulated as a **multiple-choice question**, based on the idea that discriminating among alternatives may generalize better and require fewer examples than generating an entire target element.

Each question includes:

- Up to five candidate elements.
- A “None of the above” option.

If there are more candidates, they are split into groups of five. During inference, winners from multiple groups are regrouped and compared until:

- One element remains, or
- Every group selects None.

The model generates the operation and any required value, such as text to type or a dropdown option. A direct-generation baseline instead generates the entire target element.

**Figure 5** contrasts the two approaches. In its shopping example, the goal is to find queen-size pillow protectors, add two, and check out. The multiple-choice model selects the Size dropdown and predicts `SELECT` with value “Queen,” whereas the direct approach must generate the target representation itself.

### 3.8 Data splits

The experiments evaluate three generalization settings:

- **Cross-Domain:** The complete Information and Service top-level domains are held out. This test set contains **912 tasks from 73 websites**.
- **Cross-Website:** Ten websites from each remaining top-level domain are held out, totaling **177 tasks**. Their domains and possibly similar tasks are represented in training, but the websites are new.
- **Cross-Task:** A random 20% of the remaining data is held out, totaling **252 tasks from 69 websites**. The test websites—and probably similar tasks—appear in training.

The training set contains **1,009 tasks from 73 websites**.

### 3.9 Preprocessing and evaluation

Simple HTML heuristics retain visible, semantically meaningful elements based on attributes, text, and neighbors. This reduces the average page from **1,135 to 580 elements** while retaining the true target in **94.7%** of training cases.

Because multiple nested elements may produce the same effect—such as a text span inside a clickable button—the evaluation recognizes equivalent targets. It finds the nearest clickable ancestor of the labeled target and accepts all visible descendants within that element’s rendered bounding box. Manual inspection of **100 cases** where this heuristic selected a higher-level element confirmed its validity. All acceptable equivalents count as positives in training and evaluation.

The metrics are:

- **Element Accuracy:** Whether the predicted element matches any acceptable element.
- **Operation F1:** Token-level F1 for the operation and value. It is equivalent to accuracy for Click but also evaluates the input value for Type and Select Option.
- **Step Success Rate:** A step succeeds only if both element and operation are correct.
- **Task Success Rate:** A task succeeds only if every step is correct.

Each step is evaluated independently with the correct prior action history supplied. Step-wise metrics use a macro-average across tasks.

### 3.10 Models, training, and hyperparameters

Candidate generation uses **DeBERTa-v3-base**, an 86-million-parameter model. Its top **50** ranked elements form the candidate pool for subsequent experiments.

Action prediction uses Flan-T5 base, large, and XL. GPT-3.5-turbo and GPT-4 are evaluated through in-context learning with three examples.

**Table 4** reports:

- DeBERTa-v3-base: batch size 32, 5 epochs, learning rate \(3\times10^{-5}\).
- Flan-T5-base direct-generation baseline: batch size 32, 5 epochs, learning rate \(5\times10^{-5}\).
- MindAct with Flan-T5 base/large/XL: batch size 32, 5 epochs, learning rate \(5\times10^{-5}\).
- GPT-3.5-turbo and GPT-4: temperature 0 and three demonstrations.

Flan-T5-large and XL were trained on **four A100 80-GB GPUs**. Other trained models used a single **A6000 48-GB GPU**.

**Table 8** shows the GPT prompting format. A system prompt describes the model as skilled in website navigation. Three demonstrations supply HTML, the task, previous actions, multiple-choice candidates, and an answer consisting of the chosen option, operation, and optional value. Examples include selecting Pickup in a reservation interface, choosing None when the required date element is absent, and clicking a rental-car pickup-date button.

## 4. Results and Findings

### 4.1 Candidate generation

DeBERTa-v3-base achieved Recall@50 of:

- **88.9%** on Cross-Task.
- **85.3%** on Cross-Website.
- **85.7%** on Cross-Domain.

Thus, the correct target was generally present among the 50 candidates, although recall dropped modestly in unseen environments.

### 4.2 Main results

**Table 2** reports the principal comparison. Dashes mean that the classification model could not produce the relevant operation or task-level metrics.

| Model | Cross-Task: Element / Op. F1 / Step SR / Task SR | Cross-Website | Cross-Domain |
|---|---|---|---|
| Classification | 26.8 / – / – / – | 21.6 / – / – / – | 24.5 / – / – / – |
| Direct generation | 20.2 / 52.0 / 17.5 / 0.0 | 13.9 / 44.7 / 11.0 / 0.0 | 14.2 / 44.7 / 11.9 / 0.4 |
| MindAct + Flan-T5 Base | 43.6 / 76.8 / 41.0 / 4.0 | 32.1 / 67.6 / 29.5 / 1.7 | 33.9 / 67.3 / 31.6 / 1.6 |
| MindAct + Flan-T5 Large | 53.4 / 75.7 / 50.3 / 7.1 | 39.2 / 67.1 / 35.3 / 1.1 | 39.7 / 67.2 / 37.3 / 2.7 |
| MindAct + Flan-T5 XL | 55.1 / 75.7 / 52.0 / 5.2 | 42.0 / 65.2 / 38.9 / 5.1 | 42.1 / 66.5 / 39.6 / 2.9 |
| MindAct + GPT-3.5 | 20.3 / 56.6 / 17.4 / 0.8 | 19.3 / 48.8 / 16.2 / 0.6 | 21.6 / 52.8 / 18.6 / 1.0 |
| MindAct + GPT-4 | 41.6 / 60.6 / 36.2 / 2.0 | 35.8 / 51.1 / 30.1 / 2.0 | 37.1 / 46.5 / 26.4 / 2.0 |

GPT-4 was evaluated on only **50 tasks per split** and used the top **10 candidates** because of budget limits, so its numbers are not directly comparable to full-test-set results.

Key findings include:

- Directly generating an element worked poorly. Flan-T5 Base’s element accuracy was even lower than the smaller classification model despite Flan-T5 Base having **220 million parameters**.
- The multiple-choice MindAct formulation produced large gains over both baselines.
- The strongest step result was **52.0%** for Flan-T5 XL on Cross-Task.
- The best unseen-environment step results were **38.9%** on Cross-Website and **39.6%** on Cross-Domain, also from Flan-T5 XL.
- Whole-task success remained low because a single erroneous step makes the entire task unsuccessful.
- Flan-T5 Large attained the highest Cross-Task task success, **7.1%**, even though XL had higher step success.
- Flan-T5 XL achieved the highest Cross-Website task success, **5.1%**, and Flan-T5 XL’s Cross-Domain task success was **2.9%**.

### 4.3 Generalization patterns

All models performed best on Cross-Task. The authors report an average absolute step-success gap of more than **10 percentage points** between Cross-Task and the unseen-website/domain conditions.

Cross-Website and Cross-Domain results were remarkably similar. This suggests that the principal difficulty is not unfamiliar subject matter but unfamiliar page layouts, DOM structures, and interaction logic. Tasks in different domains often share operations, and pretrained models may be able to reason about the high-level plan. The harder problem is grounding that plan into the correct action on a particular page.

**Figure 6** plots per-website step success, from left to right, for Cross-Task, Cross-Website, and Cross-Domain, showing only sites with more than three test tasks. Bars are colored by top-level domain. Cross-Task websites are generally higher, while the Cross-Website and Cross-Domain distributions substantially overlap. Exact bar values and every website label are too small to read reliably from the supplied image, but the visual supports the paper’s conclusion that unseen websites and unseen domains have similarly difficult performance profiles.

### 4.4 GPT in-context learning

GPT-3.5 and GPT-4 used only three demonstrations rather than full fine-tuning. Both were broadly competitive with the two basic baselines, though this is not a fair comparison with fully fine-tuned Flan-T5 models.

GPT-3.5 obtained only around **20% element accuracy**. The analysis found that it frequently selected “None of the above,” effectively claiming the correct action was unavailable on the current page. This reflects a genuine difficulty: most tasks require several pages and intermediate actions, so the final desired outcome often is not yet visible. Nevertheless, excessive use of None hurt performance.

GPT-4 was more promising. Its element accuracy on Cross-Website and Cross-Domain approached that of tuned Flan-T5 systems, suggesting useful generalization from in-context examples. Its high operating cost remained a concern.

### 4.5 Random grouping stability

Candidates are shuffled and randomly divided into multiple-choice groups, so the paper tests whether grouping materially changes results.

**Table 5** reports mean step success and standard deviation over five seeds:

| Model | Cross-Task | Cross-Website | Cross-Domain |
|---|---:|---:|---:|
| Flan-T5 Base | 41.5 ± 0.7 | 30.0 ± 0.8 | 31.3 ± 0.5 |
| Flan-T5 Large | 49.9 ± 0.2 | 35.7 ± 0.5 | 36.7 ± 0.3 |
| Flan-T5 XL | 51.9 ± 0.8 | 39.5 ± 0.2 | 39.6 ± 0.2 |

Every standard deviation was below 1 percentage point, indicating that random candidate grouping introduced only small fluctuations.

### 4.6 Zero-shot Flan-T5 XL

**Table 6** compares zero-shot and fine-tuned Flan-T5 XL element-selection results:

| Setting | Cross-Task | Cross-Website | Cross-Domain |
|---|---:|---:|---:|
| Zero-shot | 10.8 | 7.8 | 11.7 |
| Fine-tuned | 52.0 | 38.9 | 39.6 |

Although Flan-T5 was already trained on multiple-choice formats and occasionally selected the correct element, zero-shot performance was far below fine-tuning and three-shot GPT performance. The authors attribute this to Flan-T5 not being tuned for HTML and coding-related tasks.

The numerical row labeled “fine-tuned” matches the paper’s reported step-success figures, although Table 6’s caption calls them element-selection results; this apparent labeling inconsistency is present in the supplied paper.

### 4.7 GPT-4 subset analysis

Because GPT-4 was run on only 50 tasks per split, **Table 7** evaluates the other systems on those same subsets. Parentheses contain full-test-set values:

| Model | Cross-Task | Cross-Website | Cross-Domain |
|---|---:|---:|---:|
| Flan-T5 Base | 43.3 (41.0) | 25.3 (29.5) | 28.1 (31.6) |
| Flan-T5 Large | 48.1 (50.3) | 30.8 (35.3) | 27.6 (37.3) |
| Flan-T5 XL | 47.9 (52.0) | 33.3 (38.9) | 34.6 (39.6) |
| GPT-3.5 | 15.2 (17.4) | 15.1 (16.2) | 16.7 (18.6) |
| GPT-4 | 36.2 | 30.1 | 26.4 |

The subset values differ from full-set scores, sometimes noticeably, but the authors conclude that the broad relative ordering across models and splits is consistent. On these subsets, GPT-4 is below the tuned Flan-T5 systems on Cross-Task, roughly competitive with them on Cross-Website, and between Flan-T5 Base/Large and XL on Cross-Domain.

## 5. Analysis and Interpretation

Mind2Web demonstrates that realistic web-agent evaluation is substantially harder than evaluation on simplified websites or narrowly defined apps. Pages contain hundreds or thousands of elements, tasks require planning across multiple page states, and users provide only goals rather than explicit action scripts.

The experiments support the paper’s central modeling claim: **using a small model to filter the page before invoking a larger model is substantially more effective than directly feeding a large, unfiltered generation problem to an LLM**. The smaller ranker reduces a page to plausible elements, while multiple-choice discrimination gives the larger model a more manageable decision.

Model scaling generally improves element selection and step success. Flan-T5 XL produces the strongest step-level results, although larger size does not consistently improve operation F1 or whole-task success. Because a task is judged successful only when every action is correct, moderate per-step performance compounds into very low end-to-end completion rates.

The similarity between Cross-Website and Cross-Domain performance is a noteworthy secondary result. The authors interpret it as evidence that domain-level semantic reasoning is not the main bottleneck. Pretrained models may already know how to decompose a task such as booking or searching into broad subgoals. They struggle more with locating the correct concrete controls and applying those plans in unfamiliar interfaces.

The data therefore exposes a distinction between:

- **High-level task planning**, which pretrained language models may partly possess.
- **Environment-specific grounding**, where the agent must map its plan to a particular page’s elements and changing state.

GPT-4’s few-shot performance reinforces the possibility of generalist LLM-based agents, particularly on unseen sites and domains, but its cost prevents it from being an uncomplicated practical solution. GPT-3.5’s overuse of “None” illustrates the importance of reasoning about intermediate states rather than expecting the final task outcome to be immediately available.

No statistical significance tests or p-values are reported. Stability is instead assessed through five random-grouping runs, whose standard deviations remain below one point.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- **Mind2Web**, presented as the first dataset specifically for developing and evaluating generalist web agents across diverse real-world websites.
- Coverage of **2,350 high-level tasks, 137 websites, 31 secondary domains, and five top-level categories**.
- Use of authentic rather than manually simplified websites, including raw HTML, DOM/layout snapshots, network traces, and complete annotation traces.
- A broad interaction space involving clicking, typing, dropdown selection, multipage navigation, and relatively long action sequences.
- Explicit out-of-distribution tests for new tasks, unseen websites, and entirely held-out domains.
- A carefully controlled crowdsourcing and author-verification process, including a tool for selecting exact elements and operations.
- **MindAct**, a two-stage model that combines efficient small-model element ranking with LLM-based multiple-choice action prediction.
- Evidence that the filtering-plus-discrimination strategy substantially outperforms direct generation and simple classification.
- Evaluation of both fine-tuned open models and few-shot GPT systems.
- Public release of the dataset, code, and trained models. The supplement lists an MIT license for the code and CC BY 4.0 for training and test data, with the authors and OSU NLP group committing to upkeep and updates.

## 7. Limitations and Caveats

### Dataset representation

- Most selected websites are English-language services primarily used in the United States.
- All annotators came from MTurk and may be more proficient with the web than the broader population.
- The tasks and sites therefore represent only a subset of possible web activity.
- The dataset does not yet represent different languages and countries or many demographic and professional groups.

### Text-only modeling

MindAct uses textual webpage context even though visual layout, colors, spatial relationships, and rendered appearance may provide important evidence. The dataset includes full snapshots that could support multimodal models, but the present method does not use them.

### Limited modeling of interaction dynamics

Every page is independently encoded at every step, with only previous actions supplied as history. The model does not directly represent webpage transformations, such as a dropdown appearing after a click, even though such changes can reveal what happened and what should follow.

### Fixed one-shot task specification

The user supplies one goal at the beginning. Users cannot modify requirements during execution, and the agent cannot ask clarifying questions or seek confirmation as part of the benchmark’s normal interaction.

### Offline evaluation

Evaluation uses cached website states. If a predicted action was not cached during collection, the task can fail even if it represents a valid alternative path, creating possible false negatives. Equivalent same-page elements are normalized, and network traces may eventually enable richer replay, but current evaluation does not fully support free exploration.

### Sanitized demonstrations

Pop-ups, CAPTCHAs, advertisements, and other interruptions are generally removed. This improves consistency but omits important difficulties encountered on live websites.

### Low end-to-end reliability

Even the strongest models have low whole-task success. The best reported task-success rates range only from a few percent to 7.1%, depending on split and model. Therefore, the models are not yet reliable autonomous agents.

### Candidate bottleneck

The second stage cannot select an element omitted by preprocessing or candidate ranking. HTML cleaning retains 94.7% of training targets, and Recall@50 is approximately 85–89% on test splits, leaving an unavoidable upper-bound loss.

### GPT-4 evaluation constraints

GPT-4 was tested on only 50 tasks per setting and with only the top ten candidates because of budget. Its values are therefore less comprehensive and not fully comparable with full-test results. Its operational cost is itself a deployment limitation.

### Real-world safety

A deployed general web agent might undertake sensitive actions such as financial transactions. Safety concerns include:

- Maintaining user control.
- Seeking confirmation before consequential actions.
- Transparency and interpretability.
- Potential circumvention of CAPTCHA or other security mechanisms.
- Malicious use, including dissemination of false information.

The paper argues that cybersecurity research should anticipate these capabilities and develop safeguards.

## 8. Future Work or Open Questions

The authors identify several directions:

- **Multimodal agents:** Combine HTML text with screenshots and visual-layout information.
- **Dynamic-state modeling:** Represent how pages change following actions rather than treating every page independently.
- **Reinforcement learning:** Learn from feedback obtained on real websites.
- **Specialized web language models:** Build smaller, lower-cost models optimized for understanding webpages and taking actions.
- **Conversational interaction:** Allow users to revise requirements during a task and allow agents to request clarification or confirmation.
- **Broader data coverage:** Add websites from more countries and languages and collect tasks from different age groups, people facing accessibility barriers, and professionals in fields such as software development, research, and law.
- **More realistic handling of disruptions:** Address pop-ups, CAPTCHAs, advertisements, and other unexpected events during execution.
- **Richer cached replay:** Use the recorded network traffic to support more exploration and multiple valid solution paths in offline environments.
- **Live evaluation:** Conduct end-to-end tests on current websites with human assistance.
- **Safety mechanisms:** Develop controls for sensitive or state-changing actions and defenses against malicious agent use.
- **Long-horizon web tools:** Use web agents as natural-language tools that another LLM can invoke for more complex problem solving.

## 9. High-Level Takeaway (Plain Language)

Mind2Web is a large collection of realistic web tasks designed to test whether an AI can follow an ordinary instruction and operate unfamiliar websites. Its accompanying model, MindAct, first uses a smaller model to find likely webpage controls and then asks a larger model to choose the right control and action. This works much better than directly generating an action from a large page, including on unseen websites and domains. However, complete-task success remains very low, showing that today’s language models can often identify individual steps but are still far from being dependable, general-purpose web assistants.