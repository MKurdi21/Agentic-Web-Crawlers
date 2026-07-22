# WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models

**Authors:** Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Yong Dai, Hongming Zhang, Zhenzhong Lan, and Dong Yu  
**Publication:** Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics, 2024, pp. 6864–6890

## 1. Background and Context

Large language models have stimulated interest in autonomous agents that can carry out complicated tasks. Web browsing is an important application because it requires an agent to understand instructions, plan a sequence of actions, interpret webpages, and interact with controls such as links, search boxes, calendars, and menus.

Earlier web agents had several limitations:

- Many relied only on textual representations such as HTML, simplified HTML, or accessibility trees. These representations can become long, complicated, and difficult for a model to interpret.
- Some operated in simplified simulators or static webpage snapshots rather than on live websites.
- Screenshot-based work existed, but the authors regarded its exploration of multimodal web navigation as preliminary.
- Stepwise benchmarks such as Mind2Web often compare an agent with one predefined “golden” action trajectory. A task may have several valid solutions, so penalizing deviations from one path can produce a biased measure of end-to-end ability.
- Direct online browsing introduces problems absent from static environments, including changing content, advertisements, pop-ups, loading delays, and real-time information.

Rendered webpages are designed to communicate through visual layout as well as text. The authors therefore argue that an effective general-purpose web agent should use both screenshots and textual signals. Large multimodal models such as GPT-4V provide a way to combine those signals.

Prior systems included text-based WebGPT, HTML- and code-based WebAgent, the multimodal WebGUM, and screenshot-only PIX2ACT. Concurrent work, SeeAct, also used a large multimodal model but depended on an additional fine-tuned cross-encoder to select web elements. WebVoyager is intended to operate on live sites without such an additional learned module.

## 2. Research Goal and Objectives

The main goal is to build and evaluate an agent that can autonomously complete real-world web tasks from beginning to end without intermediate human intervention.

The paper has four connected objectives:

1. Develop **WebVoyager**, a multimodal agent that observes live webpages, reasons about the task, and directly executes browser actions.
2. Test whether combining screenshots with textual information about interactive elements works better than text-only navigation and GPT-4 with integrated tools.
3. Create a diverse benchmark of open-ended tasks on 15 popular, live websites.
4. develop a scalable automatic evaluation protocol in which GPT-4V judges complete task outcomes from the instruction, the agent’s answer, and trajectory screenshots, then compare that protocol with human judgments.

## 3. Methods (Approach/Design)

### 3.1 WebVoyager architecture and interaction cycle

WebVoyager launches a Selenium-controlled browser and repeatedly follows an observation–reasoning–action loop.

At step \(t\), its context contains:

- the user instruction;
- current and recent observations;
- previous actions;
- the complete history of its generated thoughts and actions.

The multimodal model first generates a short natural-language thought and then one executable action. The browser performs that action and returns the next observation. This continues until the agent issues an answer or reaches the maximum number of steps.

In formal terms, the paper denotes the environment by \(E\), multimodal model by \(M\), observation space by \(O\), and action space by \(A\). The model maps its accumulated context to an action, and the environment maps the previous observation and action to the next observation. This equation expresses an iterative feedback loop rather than a one-shot response.

To prevent long trajectories from overwhelming the model, WebVoyager retains only the **three most recent webpage observations**, while preserving the complete thought and action history. This context clipping can reduce confusion from obsolete page states, although the error analysis shows that it can also contribute to repeated mistakes.

**Figure 1** depicts the overall workflow. A user sends a query; the agent observes a screenshot plus text describing web elements, generates a thought, selects an action, interacts with one of the available websites, and repeats until it returns an answer. Its illustrated example asks for the cost of two-year PS4 protection on Amazon, for which the agent navigates Amazon and returns **$30.99**.

### 3.2 Observation space and visual grounding

Screenshots are the primary input. To make controls addressable, the system uses the rule-based JavaScript tool GPT-4V-ACT to:

- extract interactive elements according to their web-element types;
- place a border around each element;
- add a numerical label in its upper-left corner.

Unlike object-detection approaches, this procedure requires no learned visual detector. The agent can issue an action such as “Click [10]” rather than describing coordinates.

**Figure 2** shows a Google Flights page covered with numbered black boxes around interactive controls. The authors chose black borders and black label backgrounds empirically because one black color produced higher success than multicolored marks.

The screenshot is augmented with text containing:

- the interactive element’s content;
- its element type;
- relevant `aria-label` comments where available.

All interactions occur in one browser tab. If execution raises an exception, the error message is added to the next prompt and the model is asked to regenerate its action. Each correction consumes one of the available steps.

### 3.3 Action space and system prompt

The agent supports seven action types:

1. **Click:** select a numbered link, button, or other element.
2. **Input:** select a numbered text field, delete its existing contents, enter new text, and automatically press Enter.
3. **Scroll:** move the whole page—or a selected scrollable region—up or down.
4. **Wait:** allow a page or action to finish loading.
5. **Back:** return to the preceding page.
6. **Jump to Search Engine:** abandon the current path and restart through Google Search.
7. **Answer:** terminate navigation and return the requested information.

If clicking downloads a PDF, its content is parsed and incorporated into the observation. Forward navigation is omitted because the agent can repeat previous actions.

**Figure 7** presents the WebVoyager system prompt. It tells the model to behave like a human browser, inspect the numbered screenshot and auxiliary text, execute exactly one action per iteration, avoid irrelevant elements such as login or donation controls, and return a strict two-part format containing a brief thought and one correctly formatted action. The authors emphasize that prompt guidance should remain general rather than site-specific so that the agent retains broad applicability.

### 3.4 Live browsing environment and constraints

The system interacts with the open web rather than locally hosted replicas. This exposes it to floating advertisements, pop-ups, page updates, and other real-world variability. It does not attempt to bypass CAPTCHAs; the stated policy is to respect website rules and seek information from alternative sources.

The browser viewport is fixed at **1024 × 768 pixels**. Generation temperature is **1**, and each trajectory is limited to **15 steps**.

The main agent initially uses **GPT-4 Turbo with Vision (`gpt-4-vision-preview`)**. Additional experiments use **Claude 3 Opus** and **GPT-4o** as alternative backbones.

### 3.5 Benchmark construction

The benchmark covers 15 sites:

- Allrecipes
- Amazon
- Apple
- ArXiv
- BBC News
- Booking
- Cambridge Dictionary
- Coursera
- ESPN
- GitHub
- Google Flights
- Google Map
- Google Search
- Hugging Face
- Wolfram Alpha

Sites requiring login or CAPTCHA access were omitted. Google Search was included because it can provide an entry point to other sites.

**Figure 3** illustrates the three-stage self-instruct pipeline:

1. Humans manually sampled and rewrote tasks from Mind2Web for Google Flights, Google Map, Google Search, Booking, and Wolfram Alpha, creating initial seeds.
2. Seed tasks were used as in-context examples for GPT-4 Turbo, which generated roughly **100 new tasks across 20 iterations**. Humans checked, filtered, and rewrote them as necessary, verifying that answers could be found on the designated site.
3. More varied in-context examples were sampled from the expanded task pool. Generated tasks were again checked for repetition and online answerability.

The resulting dataset contains **643 tasks**, with more than 40 tasks per website; Table 1 describes individual site totals as **40–45 tasks**.

To assess duplication, the authors computed similarity for all **206,403 task pairs** using `all-mpnet-base-v2`:

- Only **49 pairs** had similarity above 0.8.
- **140 pairs** were between 0.7 and 0.8.
- All such pairs were manually inspected and considered acceptable.
- **99.68%** of pairs had similarity below 0.6.

### 3.6 Answer annotation

Because online information may change and some tasks permit several correct outputs, answers were classified as:

- **Golden:** a comprehensive list of valid answers considered stable in the short term.
- **Possible:** used for open-ended tasks, tasks with too many acceptable answers to enumerate, or changing real-time information such as airfare.

Only **22.3%** of tasks have golden answers; the remainder have possible answers that were correct during the experiments.

### 3.7 External evaluation sets and baselines

The authors additionally evaluated:

- **90 GAIA Level 1 and Level 2 web tasks**, beginning from Google Search because GAIA does not specify websites;
- **50 online tasks from SeeAct**.

The principal metric is **Task Success Rate**: whether the task is completed, regardless of whether the trajectory is optimal.

The main comparisons are:

- **GPT-4 (All Tools):** an integrated agent with vision, browser access, code analysis, and plugins;
- **WebVoyager Text-only:** the same broad agent framework using a webpage accessibility tree instead of screenshots;
- multimodal WebVoyager with GPT-4V, Claude 3 Opus, or GPT-4o.

### 3.8 Human and automatic evaluation

Humans received the full trajectory—all screenshots and actions—and assigned a binary success/failure judgment. For **300 tasks**, three annotators independently evaluated each trajectory. Their pre-discussion Fleiss’s kappa was **0.7**, indicating substantial agreement.

The proposed automatic evaluator receives:

- the task instruction;
- WebVoyager’s final response;
- the last \(k\) screenshots, or the full trajectory.

It determines whether all task requirements were satisfied. Its temperature is **0** to reduce randomness.

**Figure 8** shows the evaluator prompt. It instructs the evaluator not to browse or assume unshown facts, to check every part of multi-part instructions, and to distinguish between screenshots and the generated answer. If they conflict, screenshot evidence takes priority; if the response contains information not visible in the screenshot, the evaluator is instructed to accept the response. It must explain its reasoning and output either “SUCCESS” or “NOT SUCCESS.”

Each automatic evaluation in Table 1 was repeated three times to obtain a mean and standard deviation.

## 4. Results and Findings

### 4.1 Main benchmark performance

Using human judgments, the principal multimodal WebVoyager achieved an overall success rate of **59.1%**, versus:

- **40.1%** for WebVoyager Text-only;
- **30.8%** for GPT-4 (All Tools).

Thus, multimodal WebVoyager exceeded text-only by **19.0 percentage points** and GPT-4 (All Tools) by **28.3 points**.

**Table 1** reports human-evaluated success by website:

| Website | GPT-4 (All Tools) | Text-only | WebVoyager |
|---|---:|---:|---:|
| Allrecipes | 11.1% | 55.6% | 53.3% |
| Amazon | 17.1% | 31.7% | 58.5% |
| Apple | 44.2% | 34.9% | 65.1% |
| ArXiv | 14.0% | 32.6% | 51.2% |
| GitHub | 48.8% | 61.0% | 63.4% |
| Booking | 22.7% | 2.3% | 43.2% |
| ESPN | 31.8% | 36.4% | 38.6% |
| Coursera | 31.0% | 23.8% | 73.8% |
| Cambridge Dictionary | 25.6% | 62.8% | 65.1% |
| BBC News | 9.5% | 45.2% | 61.9% |
| Google Flights | 2.4% | 7.1% | 59.5% |
| Google Map | 53.7% | 61.0% | 70.7% |
| Google Search | 60.5% | 67.4% | 76.7% |
| Hugging Face | 37.2% | 20.9% | 44.2% |
| Wolfram Alpha | 52.2% | 58.7% | 63.0% |
| **Overall** | **30.8%** | **40.1%** | **59.1%** |

The largest multimodal advantages are associated with visually complicated sites. On Google Flights, WebVoyager scored **59.5%**, compared with **7.1%** text-only and **2.4%** GPT-4 (All Tools). On Booking, it scored **43.2%**, versus **2.3%** text-only. Conversely, text-only slightly exceeded WebVoyager on Allrecipes (**55.6% vs. 53.3%**), and the two approaches were relatively close on text-heavy sites such as GitHub, ESPN, Cambridge Dictionary, and Wolfram Alpha.

### 4.2 Automatically evaluated variants

With full-trajectory GPT-4V evaluation, three evaluation runs produced:

- **WebVoyager Text-only:** **44.3% ± 0.6%**
- **GPT-4V WebVoyager:** **57.1% ± 0.2%**
- **Claude-backed WebVoyager:** **52.8% ± 1.4%**
- **GPT-4o-backed WebVoyager:** **55.5% ± 0.8%**

Notable site-level automatic results include:

- GPT-4V WebVoyager reached **77.5% ± 2.7%** on Google Search, **71.3% ± 1.3%** on Cambridge Dictionary, and **60.3% ± 2.8%** on BBC News.
- GPT-4o WebVoyager reached **82.2% ± 1.3%** on Cambridge Dictionary but only **28.6% ± 0.0%** on Google Flights.
- Claude WebVoyager reached **71.3% ± 3.6%** on Cambridge Dictionary and **68.2% ± 1.3%** on Coursera, but only **15.1% ± 5.5%** on Google Flights.
- Text-only remained especially weak on Booking (**2.3% ± 0.0%**) and Google Flights (**7.1% ± 0.0%**).

Review of Google Flights trajectories found different model-specific problems. GPT-4o repeatedly failed to select the one-way option, apparently assuming that a one-way trip only required entering the departure date. Claude 3 Opus had difficulty correctly interacting with controls while entering basic flight information. The authors suggest that backbone-specific prompt changes might improve these behaviors.

### 4.3 GAIA and SeeAct results

**Figure 5** is a grouped bar chart comparing success on GAIA:

| Agent | GAIA Level 1 | GAIA Level 2 |
|---|---:|---:|
| GPT-4V (All Tools) | 23.1% | 12.5% |
| WebVoyager Text-only | 19.2% | 12.5% |
| WebVoyager | 38.5% | 15.6% |

WebVoyager was therefore strongest at both difficulty levels, with a particularly large Level 1 advantage.

On the **50-task SeeAct online test set**, WebVoyager achieved **30%**, compared with **26%** for the best SeeAct autonomous agent.

### 4.4 Reliability of automatic evaluation

**Table 2** shows that supplying more screenshots improves agreement between GPT-4V and humans:

| Screenshots supplied | GPT-4V success estimate | Human agreement | Cohen’s κ |
|---|---:|---:|---:|
| Last 1 | 47.7% | 75.3% | 0.51 |
| Last 2 | 55.3% | 79.7% | 0.59 |
| Last 3 | 54.3% | 81.3% | 0.62 |
| Full trajectory | 58.3% | 85.3% | 0.70 |

Full-trajectory GPT-4V evaluation reached the same **0.70 kappa** as the three human annotators achieved before discussion. This supports the claim that full visual trajectories allow an LMM to provide a reasonably reliable, scalable end-to-end evaluation.

With full trajectories, Claude 3 Opus achieved **0.60 kappa** with humans, while GPT-4o achieved **0.72**, slightly above GPT-4V.

**Table 3** exposes evaluator-dependent bias. Rows are agent backbones and columns are evaluators:

| WebVoyager backbone | GPT-4V evaluator | Claude evaluator | GPT-4o evaluator |
|---|---:|---:|---:|
| GPT-4V | 57.1% | 55.1% | 63.0% |
| Claude 3 Opus | 52.8% | 61.6% | 55.4% |
| GPT-4o | 55.5% | 54.9% | 64.1% |

GPT-4o was relatively lenient, while GPT-4V was stricter. GPT-4V and GPT-4o each judged their own backbone favorably. Claude showed the clearest self-preference, assigning itself **61.6%** while scoring GPT-4V and GPT-4o at **55.1%** and **54.9%**. Nevertheless, GPT-4V and GPT-4o both ranked Claude as the weakest backbone.

### 4.5 Task and webpage complexity

**Figure 6** plots each website according to:

- horizontal axis: average trajectory length;
- vertical axis: average number of interactive elements per step;
- color: task success rate, with darker colors indicating higher success.

Sites vary roughly from trajectory lengths of 3–10 actions and about 20–70 interactive elements per step. Simpler sites with shorter paths and fewer controls tend to have higher success. Highly interactive sites such as Booking and ESPN occupy more difficult regions with many elements and/or long trajectories. The overall trend supports the authors’ view that both task length and webpage clutter contribute to difficulty, though it is not a perfect relationship for every site.

### 4.6 Successful trajectories shown in the figures

The appendix demonstrates that WebVoyager can handle searching, filtering, navigation, calendars, maps, quizzes, mathematical expressions, and multilingual pages:

- **Figure 4—Apple:** In six steps, the agent searched for “Smart Folio for iPad,” entered ZIP code 90038, and identified the nearest pickup location as **Apple Tower Theatre**.
- **Figure 9—Allrecipes:** It found **Baked Dijon Salmon**, with a **4.6-star rating** and **15-minute preparation time**, satisfying requirements of under 30 minutes and at least four stars.
- **Figure 10—Amazon:** It found the green **Xbox Core Wireless Gaming Controller – Velocity Green**, rated **4.7/5**.
- **Figure 11—ArXiv:** It navigated submission documentation and answered that multiple abstracts for a non-English submission are separated by a line represented as **“-----”**.
- **Figure 12—BBC News:** It identified **Taylor Swift** as the musician appearing in Music News headlines.
- **Figure 13—Booking:** After setting Jakarta and navigating hotel results, it reported **OYO 3755 Sweet Home for US$14** for a three-night, two-adult stay beginning January 1.
- **Figure 14—Cambridge Dictionary:** It completed an easy Animals image quiz in 12 actions and scored **6/6**.
- **Figure 15—Coursera:** It identified **Xi Yang** as the instructor of *Introduction to Finance: The Basics* and reported two other courses: *Introduction to Finance: The Role of Financial Markets* and *Introduction to Financial Analysis – The “Why?”*
- **Figure 16—ESPN:** It reported **30 NBA teams**, with the **New York Knicks** and **New Orleans Pelicans** containing “New” in their names.
- **Figure 17—GitHub:** For “climate change data visualization,” it reported **resource-watch/resource-watch with 63 stars**.
- **Figure 18—Google Map:** It planned a route from Boston Logan International Airport to North Station via **MA-1A S**, taking approximately **8 minutes** in then-current traffic.
- **Figure 19—Google Flights:** It configured a one-way Dublin-to-Athens flight for one adult departing December 30 and opened the two-month price graph. Its answer states that it analyzed the graph and observed price trends, but the caption supplies no numerical trend details.
- **Figure 20—Google Search:** It returned five comedy films sorted by user rating: *Life Is Beautiful*, *Back to the Future*, *The Intouchables*, *City Lights*, and *Modern Times*.
- **Figure 21—Hugging Face:** It filtered for a `cc-by-sa-4.0` model and reported **replit/replit-code-v1-3b with 703 likes**.
- **Figure 22—Wolfram Alpha:** It simplified  
  \(x^5-20x^4+163x^3-676x^2+1424x-1209\)  
  to **\((x-4)^5+3(x-4)^3+7\)**.
- **Figure 23—Chinese Google Flights task:** For a Hangzhou–Shenzhen trip, it reported departure at **17:35**, **Shenzhen Airlines**, and **HK$2,680**.
- **Figure 24—Spanish Cambridge Dictionary task:** It reported the pronunciation of *sostenibilidad* as **/sosteniβiliˈðað/**, identified it as a feminine noun, and summarized its meaning as the ability to continue over time while causing minimal environmental damage.

These examples demonstrate breadth rather than a separate statistical test.

### 4.7 Error analysis

The authors sampled **300 benchmark tasks** and manually classified each failed case.

**Table 4** gives the distribution:

| Failure category | Share of failures |
|---|---:|
| Navigation stuck | 44.4% |
| Visual grounding issue | 24.8% |
| Hallucination | 21.8% |
| Prompt misalignment | 9.0% |

#### Navigation stuck—44.4%

This was the most common problem. Causes included:

- imprecise searches producing too many irrelevant results;
- browsing or waiting rather than correcting an earlier mistake;
- failure to locate a small scrollable region;
- uncertainty over whether to scroll up or down;
- repeated actions or repeated earlier mistakes, sometimes associated with observation clipping;
- reaching the 15-step limit before completion.

**Figure 26** illustrates this on Allrecipes. The task required a Beef Wellington recipe with at least 200 reviews and a rating of at least 4.5, plus its main ingredients. The agent repeatedly scrolled down and up but never found the ingredients.

#### Visual grounding issue—24.8%

Problems included:

- misreading uncommon visual patterns, pronunciation characters, or mathematical notation;
- failing to notice subtle changes between screenshots;
- selecting a nearby but incorrect element;
- confusing calendar dates with the system’s numerical element labels.

Additional web-element text can mitigate these errors, but the authors believe stronger visual encoders or more textual input may be necessary.

**Figure 25** shows a Google Flights task for the lowest one-way fare from JFK to Heathrow on January 22. The agent intended to choose January 22 but selected **December 22** and failed to correct the date.

#### Hallucination—21.8%

The agent sometimes gave plausible but incomplete or incorrect answers. Two recurring forms were:

- ignoring a constraint, such as returning a merely cheap visible product without first sorting to establish that it was the cheapest;
- performing a valid but wrong action, such as entering text into the wrong field, which produces no exception but sends later reasoning down an incorrect path.

**Figure 27** shows a Coursera task asking for course duration and the number of quizzes across an Artificial Intelligence for Healthcare course. The agent reported only that Module 1 had **three quizzes**, omitting the other modules and the complete requested result.

#### Prompt misalignment—9.0%

This category includes:

- generating an unparseable response, such as a thought without an action;
- ending with `ANSWER` despite explicitly recognizing that the task remains incomplete;
- losing effective instruction-following as long contexts accumulate.

**Figure 28** shows the latter case. The agent correctly found that the Scottish Premiership has **12 teams** but ended by saying that further interaction would be needed to find the start time of Hibernian’s most recent match, even though it could have continued navigating.

## 5. Analysis and Interpretation

### Why visual and textual signals complement each other

The results support the central claim that neither modality is sufficient by itself.

Screenshots are especially useful for:

- calendars;
- spatially organized controls;
- maps;
- menus and visual filtering interfaces;
- understanding the webpage’s overall structure.

This explains the major multimodal gains on Booking and Google Flights, where an accessibility tree becomes lengthy and unintuitive.

Text remains important on dense, text-heavy sites. Screenshot-based recognition can struggle with small fonts or closely packed text, which helps explain the text-only agent’s competitive performance on Allrecipes and its relatively close results on GitHub, ESPN, Cambridge Dictionary, and Wolfram Alpha. The authors therefore advocate a stronger combination of screenshots with extracted HTML text rather than abandoning either modality.

### Why direct website interaction matters

GPT-4 (All Tools) often relied on pages retrieved through Bing instead of directly operating the target site. It could not reliably access and use search, click, and sorting controls on sites such as Apple, Amazon, and BBC News. This limits tasks requiring site-specific interaction rather than simple information retrieval. WebVoyager’s direct Selenium-based interaction is presented as a central reason for its stronger performance.

### Difficulty rises with interaction complexity

The Figure 6 pattern indicates that performance generally falls as trajectories become longer and pages contain more interactable elements. More controls create more opportunities to choose an adjacent or irrelevant element, while longer paths create more opportunities for accumulated mistakes, context growth, repeated actions, and premature termination.

### Interpretation of automatic evaluation

GPT-4V becomes substantially more consistent with humans when given the full trajectory rather than only the last screenshot. A final screenshot may omit earlier evidence or fail to reveal whether every task component was addressed. Full-trajectory agreement of **85.3%** and kappa of **0.70** suggest that an LMM can provide a scalable approximation to human evaluation.

However, Table 3 shows that evaluators are not neutral: different models apply different levels of strictness, and each may prefer outputs generated by itself. Thus, the protocol is promising but should not be interpreted as perfectly objective.

### Why open-source models were not tested

The authors state that existing open-source multimodal models were unsuitable for this setup because:

- models such as LLaVA reduce images to **224×224 or 336×336**, making small webpage text unreadable;
- LLaVA’s maximum context length is **4,096 tokens**;
- WebVoyager trajectories may contain 15 steps and require approximately **7,000+ tokens**.

These constraints prevent the required fine-grained visual reading and long-horizon reasoning.

## 6. Contributions and Novelty

The paper’s main contributions are:

- **An end-to-end live-web agent:** WebVoyager completes tasks directly on real websites rather than only in static snapshots or simplified simulators.
- **A multimodal interaction design:** It combines screenshots with text describing interactive elements.
- **Rule-based set-of-mark grounding:** Web controls are given black borders and numerical labels without a learned object-detection module.
- **A complete browser action loop:** The agent can click, type, scroll, wait, go back, restart through Google, parse downloaded PDFs, and terminate with an answer.
- **A new benchmark:** The authors created **643 diverse tasks across 15 websites**, with human validation and low measured duplication.
- **End-to-end evaluation:** Success is judged from completed trajectories rather than adherence to one prescribed action path.
- **An LMM-based automatic evaluator:** Full-trajectory GPT-4V evaluation reached **85.3% agreement** and **0.70 kappa** with humans.
- **Empirical evidence for multimodality:** Human-evaluated WebVoyager achieved **59.1%**, substantially above text-only (**40.1%**) and GPT-4 (All Tools) (**30.8%**).
- **Multilingual demonstrations:** Successful Chinese and Spanish trajectories indicate that the interaction framework can operate beyond English in the examples shown.
- **A detailed error taxonomy:** Navigation, visual grounding, hallucination, and prompt-following failures are quantified and illustrated.

## 7. Limitations and Caveats

### Technical and experimental limitations

- The action set does not cover everything a person can do. In particular, **dragging** is unsupported because drag distance is continuous rather than a small finite choice.
- The system analyzes basic formats such as text and PDFs but does not support all file types, especially **video**.
- Websites requiring authentication or CAPTCHA access were excluded.
- The benchmark is limited to 15 selected websites and non-login tasks.
- Live web content can change, so most tasks do not have fixed exhaustive answers. Only **22.3%** have golden responses.
- Each run is capped at 15 steps. Navigation failure often means exhausting this budget rather than proving that the task is impossible.
- Context clipping can remove observations that would have helped the model avoid repeating a mistake.
- Screenshots can make dense or small text hard to recognize.
- The current visual grounding method can confuse nearby controls, calendar numbers, pronunciation symbols, and mathematical notation.
- The paper’s successful trajectories are selected examples and should not be interpreted as showing universal reliability.
- Some illustrated answers are minimally informative. For example, the Google Flights price-graph trajectory says that trends were analyzed but does not report specific numerical trends in the supplied caption.

### Evaluation caveats

- Human evaluation is accurate but expensive and difficult to scale.
- Human judges themselves had only **0.70 Fleiss’s kappa** before discussion.
- GPT-4V automatic evaluation disagreed with humans on **14.7%** of full-trajectory cases.
- Automatic scores vary by evaluator. GPT-4o was more lenient, GPT-4V stricter, and all three evaluators displayed some self-preference.
- The evaluator prompt explicitly accepts response-only information if it is not contradicted by screenshots. This can preserve valid facts that were visible earlier, but it may also make unsupported generated claims difficult to detect.
- Open-source multimodal alternatives were not experimentally assessed due to the resolution and context limitations identified by the authors.

### Safety and ethical risks

Before real-world deployment, the authors say extensive safety checks are necessary. A web agent could:

- download malicious content from unauthorized sites;
- enter private or confidential information into public forms;
- send fake requests to servers;
- generate artificial user activity harmful to site owners.

For the study, agents were restricted to non-login tasks, monitored during evaluation, and manually checked task prompts were used to avoid harmful or unethical requests. The authors state that this approach was intended to respect website terms and prevent harmful consequences.

## 8. Future Work or Open Questions

The paper identifies several directions:

- Combine screenshots with richer text extracted from HTML, especially for dense, text-heavy sites.
- Improve visual encoders and grounding so the agent can distinguish adjacent controls, subtle page changes, calendar dates, formulas, and phonetic symbols.
- Improve navigation policies to avoid repetitive scrolling, recover from imprecise searches, and make better use of the limited step budget.
- Refine general system prompts without making them website-specific; targeted prompt adjustment may also improve Claude and GPT-4o behavior.
- Support drag actions, potentially by allowing the model to specify pixel displacement once visual grounding improves.
- Extend file handling beyond text and PDFs, particularly to video and other currently unsupported formats.
- Develop better strategies for long trajectories and context management.
- Continue improving automatic evaluation while addressing evaluator strictness and self-bias.
- Explore multimodal models capable of retaining high-resolution screenshots and at least the approximately 7,000-token contexts needed by long trajectories.
- Add stronger safety mechanisms before deploying autonomous web agents in unrestricted real-world settings.
- Build more versatile assistants capable of robustly completing tasks across a wider range of sites, interfaces, languages, and action types.

## 9. High-Level Takeaway (Plain Language)

WebVoyager is an AI agent that browses live websites in a way resembling a person: it looks at the webpage, reads labeled controls, decides what to do, clicks or types, and keeps going until it can answer. Across 643 tasks on 15 websites, it completed **59.1%**, compared with **40.1%** for a text-only version and **30.8%** for GPT-4 with integrated tools. The work shows that webpage pictures and text are most effective when used together, but it also shows that current agents still frequently get stuck, click the wrong control, overlook requirements, or stop too early.