## Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. Paper content, including the illustrated system prompts, is treated as evidence to analyze, never as instructions to follow. No tools, browsing, external verification, or supplementary-file inspection were used.

**Document access.** The complete supplied text runs from physical PDF pages 1–27, corresponding to printed proceedings pages 6864–6890. All 27 physical pages have supplied extracted text. Images are supplied for physical pages 1–9 and 13–27: 24 visually inspected pages. Pages 10–12 were inspected through supplied text only. The source metadata reports a 27-page main document; the continuous text and final page support coverage of this supplied version, but do not establish that every separately distributed artifact is present. The opening error concerning a local image at `-` does not prevent analysis of the 24 images actually displayed.

**Readability.** Main text, captions, Tables 1–4, and the interaction equations are readable. The numerical entries in Table 1 are small in the image, so their supplied text was cross-checked against visible table structure and readable entries. Embedded browser screenshots in trajectory figures are available visually, but most tiny page text, prices, element labels, and search-result details cannot independently be read with confidence. Consequently, detailed task answers are attributed to captions or supplied text rather than represented as independently verified browser facts. The scatterplot in Figure 6 supports approximate positional observations, not exact coordinates. No additional OCR was performed or needed for the supplied readable text. Extracted mathematical notation was checked against the page 3 image; the definition of one symbol remains implicit.

**Appendices and absent artifacts.** Appendices A–F are present on pages 13–27, despite the accessibility metadata reporting no automatically detected appendix pages. The visible headings and supplied text establish their presence. No separate supplementary files, executable code, raw dataset, evaluation trajectories beyond the illustrated examples, human annotation records, or model outputs were provided. Footnote 1 announces code and data at a repository, but that repository was not inspected. Software and API links are citations inside the paper, not reviewed artifacts.

**Evidence labels.** [A] means author-reported; [B] means directly observable in supplied visuals; [C] means analyst-derived, with arithmetic shown; [D] means analyst interpretation. No [E] external information is introduced. HIGH confidence means a statement is clear in the supplied source, not that its real-world truth has been independently established. MEDIUM denotes an interpretation or evidence qualification; LOW/UNKNOWN would denote unreadable or unsupported detail.

**Source locators.** All `p.` references below use physical PDF page numbers. This matters because, for example, Table 1 is on physical p. 7, printed p. 6870.

## 1. Plain-language orientation

WebVoyager is an artificial intelligence system that opens real websites and performs a sequence of browser actions to answer a user's request. Instead of receiving only a long textual description of a webpage, it sees a screenshot plus selected text describing interactive elements. The system places numbered markers on clickable or editable items, asks a large multimodal model to choose one action, executes that action, and then shows the updated page to the model. This continues until the model answers or exhausts its action budget. [A, pp. 1–4]

The problem is practical: answering a question from a static text passage differs from finding a product, entering dates, using a calendar, comparing results, and deciding when a task has been finished. The authors argue that earlier agents and benchmarks often used simplified environments, static snapshots, verbose HTML representations, or a single predefined sequence of correct actions. Their proposed contribution combines a real-browser agent, a 643-task benchmark covering 15 websites, and a multimodal model that judges whether an entire browsing task succeeded. [A, pp. 1–5]

On the new benchmark, human judgments give WebVoyager a 59.1% task success rate, compared with 40.1% for its text-only version and 30.8% for GPT-4 (All Tools). These are task-completion scores, not security scores. Full-trajectory GPT-4V evaluation agrees with consolidated human judgments on 85.3% of a 300-task subset. Performance varies substantially by website and by evaluator. The paper also documents navigation failures, incorrect selection of webpage elements, partial or wrong answers, and premature stopping. [A, pp. 6–9]

For the requested research question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis**, this paper supplies an architecture and explicit risk statements, but does not conduct that comparison. Its security relevance is analyst inference: the model receives content from live websites and can turn its decisions into clicks, typed text, downloads, and server requests. The authors themselves warn about malicious downloads, disclosure of private information, and harmful fake requests or activity. They do not measure attacks, prompt injection, security defenses, or relative vulnerability against a standalone large language model. [A, p. 10; D, architecture-based interpretation]

## 2. Document roadmap

**Bibliographic identity.** The original title is *WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models*. Authors are Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Yong Dai, Hongming Zhang, Zhenzhong Lan, and Dong Yu. Affiliations are Zhejiang University, Tencent AI Lab, and Westlake University. The proceedings identify the venue as the 62nd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp. 6864–6890, August 11–16, 2024. A footnote states that Hongliang He's work was performed during an internship at Tencent AI Lab. [A, p. 1]

**Document type.** This is a mixed AI systems, benchmark, and empirical evaluation paper. It is not a security experiment, formal theoretical paper, or systematic literature review. No separately listed keywords, formal research questions, hypotheses, numbered algorithm, theorem, or proof appear in the supplied document.

**Inventory.** The abstract and §1 Introduction frame the problem and contributions on pp. 1–2. §2 Related Work spans pp. 2–3. §3 WebVoyager covers browsing environment (§3.1), interaction formulation (§3.2), observation space (§3.3), and action space (§3.4), pp. 3–4. §4 Benchmark covers website selection (§4.1), data construction (§4.2), and annotation (§4.3), pp. 4–5. §5 Experiment includes Dataset and Metrics, Experimental Details, Evaluation Methods (§5.1), Result (§5.2), Discussions (§5.3), and Error Analysis (§5.4), pp. 5–9. §6 Conclusion is on p. 9. Limitations span pp. 9–10; Ethics Statement is on p. 10; References span pp. 10–12.

Appendix A describes the agent prompt; B the evaluation prompt; C action formats; D successful and multilingual trajectories; E additional related work; F error examples. Their text and figures occupy pp. 13–27. The visual inventory consists of Figures 1–28: workflow and data diagrams, an annotated webpage, successful browsing trajectories, two quantitative plots, two prompt displays, and four failure trajectories. Tables 1–4 respectively report benchmark performance, evaluator–human consistency, backbone–evaluator comparisons, and failure-category shares. The major mathematical content is the unnumbered interaction formulation in §3.2. Figure 22 additionally contains an example polynomial simplification.

The paper's organization moves from problem to implementation, benchmark construction, evaluation, interpretation, and limitations; the appendices expose operational details and selected examples rather than adding a separate adversarial study.

## 3. Background and context

A **large language model (LLM)** processes and generates language. A **large multimodal model (LMM)**, as used here, can process both images and text. GPT-4V denotes the vision-capable model; GPT-4o denotes GPT-4 Omni. These explanations follow the paper's use of the terms, without adding current product information. [A, pp. 1, 5, 14]

A webpage can be described through **HTML**, the textual representation underlying the page, or an **accessibility tree**, a structured textual account of page elements used by the text-only baseline. The **Document Object Model (DOM)** tree is mentioned as another representation whose verbosity can burden the model. WebVoyager instead uses the rendered screenshot as its primary input, retaining auxiliary text for interactive elements. Its **visual grounding** problem is to connect something seen on the screen to the correct executable browser target. Numbered bounding boxes help establish that connection. [A, pp. 3–4]

A **trajectory** is the sequence of observations and actions during one task. **End-to-end evaluation** judges the final completion of that task, allowing different routes through the website. The authors contrast this with evaluation against a predefined **golden trajectory**, which can penalize a different but successful route. A golden trajectory should not be confused with a **Golden answer**, the benchmark's label for a sufficiently comprehensive and relatively stable answer listing. [A, pp. 2, 5–6]

**ReAct prompting** is described here as generating a natural-language thought before generating the executable action. **Set-of-Mark prompting** inspires numbered marks on screenshots. **Self-instruct** describes the process of using existing task examples to generate further task instructions, followed here by human filtering and verification. These are operational descriptions from the supplied paper, not external accounts of those methods. [A, pp. 3–5]

The evaluator metrics distinguish **agreement**, the fraction of matching labels, from **kappa**, the named agreement statistic reported by the authors. The paper cites Cohen for model–human comparisons and Fleiss for the three human annotators. It provides values but no equations for these statistics; this analysis therefore does not introduce a missing mathematical definition as author content.

## 4. Research problem and gap

**Existing problem.** A web agent must understand instructions, plan a sequence of decisions, interpret complex webpage structures, and act in a changing environment. Live sites add floating advertisements, pop-ups, and constant updates. Correctly generating an answer requires both navigation and recognition that every requested condition has been satisfied. [A, pp. 2–3, 9]

**Shortcomings attributed to previous approaches.** The authors identify verbose HTML as a major burden, single-modality inputs as restrictive, and simplified simulators or static snapshots as insufficiently realistic. They also argue that offline evaluation against one golden action sequence can miss the variety of valid strategies. These are the authors' positioning claims; the supplied paper is not a systematic census establishing that all earlier work has these properties. [A, pp. 1–3]

**Research gap.** The target is an autonomous multimodal browser agent that performs complete tasks on real websites, together with evaluation that recognizes task completion rather than reproducing one particular path. WebVoyager does not require the extra candidate-selection module that the authors attribute to the best concurrent SeeAct agent. This does not mean WebVoyager has no supporting software: Selenium, webpage marking JavaScript, and file parsing remain part of its implementation. [A, pp. 3–4, 13]

**Scope.** The work emphasizes non-login open-web tasks on 15 selected websites and two additional task sets. It excludes websites requiring login or CAPTCHA access, constrains activity to one browser tab, supplies seven action types, and permits at most 15 exploration steps. Its gap is task capability and evaluation, not a demonstrated security gap between browser agents and isolated models. [A, pp. 4–5, 10]

## 5. Research questions, objectives, and hypotheses

**Explicit formal research questions:** none are stated as numbered or formally phrased questions. **Explicit hypotheses:** none are stated. They should not be retroactively invented.

The authors' objectives can be organized as follows. O1: build an agent that autonomously browses the open web to complete user instructions without intermediate human intervention. O2: establish a diverse benchmark of real-world tasks on commonly used websites. O3: investigate whether an LMM can automatically evaluate completed navigation trajectories with useful agreement with humans. O4: compare multimodal WebVoyager with GPT-4 (All Tools), a text-only configuration, and additional LMM backbones. O5: examine recurring failures and factors associated with task difficulty. [A, pp. 1–9]

The externally supplied research question concerning greater vulnerability is a separate analytical lens. It is addressed here only through clearly labeled implications of the architecture, observed non-adversarial failures, and the authors' potential-risk discussion. A finding that a multimodal agent completes more tasks does not answer whether it withstands attackers better or worse than a standalone LLM. [D]

## 6. Assumptions / Threat Model

**Operational assumptions.** The agent has access to a browser controlled through Selenium, webpages can be rendered into screenshots, and interactive elements can be identified through rule-based JavaScript and assigned numerical labels. User tasks are expected to be answerable through accessible website content. The model receives the current page plus recent observations and accumulated thought/action history. Correct execution depends on choosing the right label and producing a parsable action format. [A, pp. 3–5, 13–14]

**Environmental restrictions.** Multiple tabs are disabled. Websites requiring login or CAPTCHA are omitted from benchmark selection. The CAPTCHA footnote says the agent is prompted to retrieve information from alternative sources in accordance with website rules. The experimental ethics statement restricts tasks to non-login activity, describes monitoring of the agent, and states that all evaluation queries receive manual harmlessness inspection. These are author-reported procedures; the supplied materials do not independently demonstrate universal compliance. [A, pp. 3–4, 10]

**Threat model absent.** There is no defined attacker, attack objective, controlled malicious webpage, attacker budget, trust-boundary enforcement mechanism, attack success metric, or security baseline. Figure 7 gives action and browsing guidelines, but is not evidence of a formally enforced security policy. Likewise, binary task-completion evaluation does not assess confidentiality or integrity. [D, absence in supplied methods and experiments]

**Security-relevant interpretation.** A plausible boundary exists between the user's task and website-sourced observations, because both enter the model's context while only the former is intended to specify the task. The paper does not test whether the agent confuses these roles. The execution boundary is directly documented: model-selected actions are executed by the browser environment. Therefore this paper can ground an architectural discussion of possible exposure and consequences, but cannot quantify exploitation or establish comparative vulnerability. [A, pp. 3–4; D]

## 7. Methodology

### Agent architecture and interaction

WebVoyager instantiates a browser, captures the webpage, prepares observations, asks the LMM for a thought and an action, executes the action, and updates the context. Iteration ends at a terminating action or maximum step count. The principal backbone is GPT-4 Turbo with vision, identified as `gpt-4-vision-preview`; Claude 3 Opus and GPT-4o are additional backbones. No training or fine-tuning procedure for WebVoyager itself is reported. [A, pp. 3, 5]

The environment uses Selenium on real websites rather than locally hosted replicas. The rule-based GPT-4V-Act JavaScript tool finds interactive elements based on their types and overlays bounding boxes and numerical labels. This avoids a separate object-detection model. Borders and label backgrounds are black. The authors say black gives better success than multiple colors, but provide no numerical color ablation, sample size, or uncertainty for that assertion. [A, pp. 3–4]

Observations combine the screenshot, interactive-element text, element type, potentially `aria-label` comment text, and history. The last three observations are retained; outdated page observations are clipped, while the entire history of thoughts and actions is kept. The stated rationale is that excessive page observations can confuse the model. Execution exceptions are inserted into the prompt and the model is asked to regenerate; each correction consumes another step. Importantly, the paper also later attributes repeated mistakes partly to this clipping. [A, pp. 3–4, 9]

Seven actions are available: Click; Input/Type; Scroll; Wait; Back/GoBack; Jump to Search Engine/Google; and Answer. Type deletes existing text and inputs new content, followed automatically by ENTER. Scroll can target the whole window or an element within a scrollable region. Google starts anew at Google Search. Clicking a PDF link can download a file whose content is parsed using the OpenAI Assistant API and incorporated into the observation. These are explicit operational details, including an additional file-derived input pathway. [A, pp. 4, 13]

### Dataset construction and annotation

The benchmark covers Allrecipes, Amazon, Apple, ArXiv, BBC News, Booking, Cambridge Dictionary, Coursera, ESPN, GitHub, Google Flights, Google Map, Google Search, Huggingface, and Wolfram Alpha. The authors select sites covering everyday activities and omit login/CAPTCHA-dependent content. Table 1 states 40–45 tasks per website; the construction section states 40+ per site and 643 in total. These descriptions are compatible. [A, pp. 4–5, 7]

Construction has three stages. First, humans sample and rewrite seed tasks from Mind2Web for several websites. The prose names Google Flights, Google Map, Google Search, Booking, and Wolfram Alpha. Second, sampled tasks are provided as in-context examples to GPT-4 Turbo to generate approximately 100 new tasks over 20 iterations. Humans verify and rewrite generated tasks, checking quality and whether answers can be found on their websites, and add accepted tasks to the pool. Third, more diverse pool examples guide further generation; generated tasks are added iteratively and manually checked for low repetition and answer availability. [A, pp. 4–5]

The all-mpnet-base-v2 model measures pairwise task similarity. Of 206,403 pairs, 49 have similarity greater than 0.8, 140 lie between 0.7 and 0.8, and 99.68% have similarity below 0.6. The high-similarity pairs were manually accepted. The supplied paper does not provide a full similarity distribution, similarity-function implementation, or proof that semantic similarity guarantees task diversity. [A, p. 5; D, qualification]

Answers are labeled Golden or Possible. Golden entries contain comprehensive possible-answer listings considered stable in the short term. Possible entries cover open-ended requests, multiple acceptable answers impractical to enumerate, and real-time information that may change. Golden answers account for 22.3% of questions. This is an evaluation dataset; the paper does not report train/validation/test splits for learning a new WebVoyager model. Nor does it describe participant demographics, dataset licensing terms, or a dedicated leakage-control experiment. [A, p. 5]

### Configuration, baselines, and evaluation

The browser viewport is 1024 × 768 pixels. Agent generation temperature is 1, and the maximum exploration budget is 15 steps. Automatic evaluation temperature is 0. The paper supplies no hardware specification, browser/Selenium version, random seed, token cost, latency, throughput, or system memory measurements. [A, pp. 5, 13]

The main baselines are GPT-4 (All Tools), described as integrating vision, browsing, code analysis, and plugins, and a WebVoyager text-only configuration receiving an accessibility tree. They are agents with different capabilities and observation pathways, not a standalone-LLM security control. Additional evaluation uses 90 GAIA Level 1/2 web tasks, starting at Google Search because GAIA does not prescribe websites, and 50 tasks from SeeAct's online evaluation. [A, pp. 2, 5]

The main metric is Task Success Rate: successful completion without requiring optimal actions. Human evaluators receive complete screenshots and actions and give binary judgments. Three annotators evaluate a 300-task subset; their pre-discussion Fleiss's kappa is 0.7. Consolidated human labels are compared with GPT-4V judgments. The automatic evaluator receives the instruction, agent response, and last k screenshots or full trajectory. Table 1 repeats GPT-4V evaluation three times to report mean and standard deviation; these repetitions should not be mistaken for three independent browsing runs. [A, pp. 6–7]

## 8. Experiments / Analyses

**X1 — Main 643-task benchmark.** Purpose: compare task completion on live websites. Conditions: multimodal WebVoyager, text-only WebVoyager, and GPT-4 (All Tools), with human success judgments. Overall results are 59.1%, 40.1%, and 30.8%, respectively. Website-specific results appear in Table 1. The strongest primary WebVoyager score is Google Search, 76.7%; its weakest is ESPN, 38.6%. Multimodal WebVoyager trails text-only on Allrecipes, 53.3% versus 55.6%. This qualifies a universal superiority claim. [A, pp. 6–7]

**X2 — GAIA transfer evaluation.** Purpose: examine performance on another web-task source. Data: 90 Level 1/2 tasks with golden responses; start page is Google Search. Figure 5 reports Level 1 success of 23.1%, 19.2%, and 38.5% for the All Tools baseline, text-only, and WebVoyager. Level 2 results are 12.5%, 12.5%, and 15.6%. The paper does not give the per-level sample sizes in the supplied text, so they are not reconstructed from rounded percentages. [A, pp. 5, 8]

**X3 — SeeAct online task comparison.** Data: 50 tasks used in SeeAct's online evaluation. WebVoyager reaches 30%, versus 26% for the best autonomous SeeAct result cited by the authors. The supplied material gives no detailed table of these tasks, repeated-run uncertainty, or matched environmental timing. Thus this is a reported cross-method comparison, not a fully exposed controlled replication. [A, pp. 5–6; D, qualification]

**X4 — Evaluator screenshot-context analysis.** On the 300-task human-comparison subset, k is varied between 1, 2, 3, and full trajectory. Agreement rises from 75.3% to 85.3%, with kappa from 0.51 to 0.70. Evaluator success rates are 47.7%, 55.3%, 54.3%, and 58.3%, demonstrating that its estimated performance is not monotonically increasing at every intermediate setting. Agreement, not every measure, improves monotonically. [A, pp. 6–7]

**X5 — Backbone and evaluator comparison.** GPT-4V-evaluated overall task success is 57.1% ± 0.2% for the principal WebVoyager backbone, 52.8% ± 1.4% for Claude 3 Opus, and 55.5% ± 0.8% for GPT-4o. Table 3 evaluates all three backbones using each of three evaluators. GPT-4o evaluation gives higher scores in every backbone row than GPT-4V evaluation. Claude evaluation rates its own backbone highest. Full-trajectory human agreement kappas are 0.70 for GPT-4V, 0.60 for Claude, and 0.72 for GPT-4o. This exposes evaluator dependence, not a single authoritative ordering. [A, pp. 7–8]

**X6 — Website-complexity association.** Figure 6 plots website-level average trajectory length against average interactive elements per step, colored by task success. The authors use these as approximate complexity indicators and say the results broadly support simpler pages and shorter trajectories being easier. No regression, correlation coefficient, uncertainty interval, or causal intervention is supplied. Averages for trajectory length concern tasks completed within the maximum iterations; this conditioning matters when interpreting difficulty. [A, p. 8]

**X7 — Failure analysis.** The authors sample 300 benchmark tasks and manually label the main category for each failed case. Shares of failures are Navigation Stuck 44.4%, Visual Grounding Issue 24.8%, Hallucination 21.8%, and Prompt Misalignment 9.0%. The number of failed cases within this sample is not explicitly supplied. The categories overlap conceptually, but the authors use a main-reason classification. These are non-adversarial failure labels, not attack categories. [A, pp. 8–9]

**X8 — Task-diversity check and illustrative trajectories.** Pairwise similarity statistics support a low-repetition claim for generated instructions. Figures 4 and 9–24 show selected successful trajectories; Figures 25–28 show selected failures. Chinese and Spanish examples demonstrate individual multilingual cases, not measured multilingual benchmark accuracy. The examples illustrate how the system operates and fails; they do not provide random-sample performance evidence. [A, pp. 5, 13–27; D]

## 9. Results

The primary result is better human-judged benchmark completion for multimodal WebVoyager, under the paper's website selection, prompts, and 15-step limit. **Analyst-derived:** 59.1 − 30.8 = 28.3 percentage points above GPT-4 (All Tools), and 59.1 − 40.1 = 19.0 percentage points above text-only. These are absolute percentage-point gaps. Relative improvements would be 28.3/30.8 × 100 ≈ 91.9% and 19.0/40.1 × 100 ≈ 47.4%; they are separate derived quantities, not author-reported statistics. [C, Table 1, p. 7]

The website pattern is important. On Booking, scores are 22.7% All Tools, 2.3% text-only, and 43.2% WebVoyager. On Google Flights they are 2.4%, 7.1%, and 59.5%. These support the authors' interpretation that visual interfaces such as calendars challenge text-only representations. Conversely, Allrecipes favors text-only slightly, and GitHub, ESPN, Cambridge Dictionary, and Wolfram Alpha show smaller multimodal gaps. The authors suggest denser HTML-derived text could help screenshot-based decisions on text-heavy sites. [A, pp. 6–8]

Generalization is limited rather than solved: GAIA Level 2 success remains 15.6%, and SeeAct-task success is 30%. **Analyst-derived:** the SeeAct comparison is 30 − 26 = 4 percentage points; the GAIA Level 1 gain is 38.5 − 23.1 = 15.4 points over All Tools and 38.5 − 19.2 = 19.3 points over text-only. Level 2 gains are 15.6 − 12.5 = 3.1 points over either baseline. No significance tests are supplied for these differences. [C, pp. 6, 8]

Automatic evaluation is useful but imperfect. Its full-trajectory agreement is 85.3%, not 100%. **Analyst-derived:** 100 − 85.3 = 14.7% disagreement with consolidated human labels on the evaluated subset. This is not a false-positive rate or false-negative rate, because the paper does not provide the confusion matrix needed to distinguish them. Table 3 further shows that estimated task success changes with evaluator identity. [A/C, p. 7]

Failure analysis reveals execution-specific problems: wasted scrolling, wrong nearby elements, valid actions in wrong text boxes, missing requested information, unparsable responses, and ending while acknowledging incompleteness. These demonstrate imperfect task reliability. They do not demonstrate adversarial exploitability; such a claim would require a separate attack design and outcome measurement. [A, p. 9; D]

## 10. Figure-by-figure interpretation

All Figures 1–28 were visually inspected in the supplied page images. Caption details remain author-reported where tiny embedded webpage text cannot be independently verified. Only Figures 5–6 are quantitative plots; browser trajectories have no statistical axes or error bars.

**Figure 1 — Overall workflow, p. 2.** The user sends a query to the agent and receives an answer. Screenshot and element-text observations feed the reasoning process; a thought precedes an action, which operates on available websites and produces the next observation. Arrows depict the repeated feedback loop. The Amazon example returns a two-year PS4 protection price of $30.99, an illustrative author-reported historical task answer rather than a current price. Website logos denote available environments, not numerical evidence.

**Figure 2 — Marked webpage observation, p. 3.** A Google Flights screenshot has many black boxes with numerical tags placed at interactive elements. It visually demonstrates label-based grounding. It does not establish that all tags are read correctly or all targets are actionable; the later failure examples qualify that impression.

**Figure 3 — Benchmark-generation diagram, p. 5.** Human task seeds, in-context examples, GPT-4 generation, manual filtering, and a 15-website task pool are connected by arrows. Filtered tasks enter the pool, and pool examples guide further generation. A final manual filtering stage checks answers online. The top seed-stage labeling and the prose's approximate generation count are not detailed enough to reconstruct an exact per-iteration production schedule. The diagram supports the hybrid generation/verification process, not a purely human-authored dataset.

**Figure 4 — Apple successful trajectory, p. 6.** Six panels show accessory navigation, typing Smart Folio for iPad, clicking a product, entering pickup-location information, typing zip code 90038, and ANSWER. The caption reports Apple Tower Theatre as the nearest pickup answer. Labels identify the action targets; orange annotations highlight relevant elements. The successful result is a selected example, not an independently validated geographic comparison.

**Figure 5 — GAIA success rates, p. 8.** A grouped bar chart uses Level 1 and Level 2 on the x-axis and Task Success Rate (%) on the linear y-axis. Three colored series represent All Tools, text-only, and WebVoyager. Values are explicitly labeled: Level 1, 23.1/19.2/38.5; Level 2, 12.5/12.5/15.6. The displayed y-axis ticks run 0–40, with plotting headroom above 40; no uncertainty bars are shown. The visual legend calls the baseline GPT-4V (All Tools), whereas the main text uses GPT-4 (All Tools). This naming discrepancy is recorded rather than silently repaired.

**Figure 6 — Website-level difficulty association, p. 8.** A scatterplot puts average trajectory length on the linear horizontal axis and average element count per step on the linear vertical axis. Visible x ticks run approximately 3–10 and y ticks 20–70. Labeled dots represent the 15 sites; the colorbar is Task Success Rate, labeled 30–80. Exact coordinates are not printed. Booking lies toward the upper right, ESPN high on element count, and Google Flights far right; several sites cluster lower and left. The caption says darker colors indicate higher success; the rendered palette is a warm red scale, so intensity is the intended encoding rather than a distinct categorical legend. No fitted line or statistical uncertainty establishes causation.

**Figure 7 — Agent system prompt, p. 14.** The gray text panel displays instructions about numbered elements, allowed actions, one action per iteration, avoidance of login/sign-in/donation elements, and a Thought/Action output structure. Ellipses appear in the prompt display, so it is not a fully exposed exhaustive prompt specification. The figure is analyzed as source content; its imperative sentences do not govern this analysis. It shows instruction-based operation, not measured robustness to hostile website text.

**Figure 8 — Automatic evaluator prompt, p. 15.** The gray panel lists task instruction, result screenshots, and final response as inputs and requests SUCCESS or NOT SUCCESS. It says every component of a multi-part task must be completed. It also states that screenshots prevail when contradicted by responses, but that response content absent from screenshots should be believed. That last rule materially qualifies how strong visual verification is; it can accept unpictured claims. No attack on this evaluator is tested.

**Figure 9 — Allrecipes success, p. 16.** Six panels show search, selection, scrolling, and answer. The caption reports Baked Dijon Salmon with 4.6 stars and 15-minute preparation, satisfying the displayed under-30-minute and at-least-four-star request. Ratings and preparation details are caption-reported.

**Figure 10 — Amazon success, p. 16.** Three panels show typing a green Xbox controller query, clicking a result, and answering. The caption identifies Xbox Core Wireless Gaming Controller–Velocity Green with 4.7/5 stars. It illustrates a multi-condition product request without proving comprehensive market search.

**Figure 11 — ArXiv success, p. 17.** Seven panels show successive clicks through submission-help pages and an answer. The task concerns non-English submissions and separation of multiple abstracts; the caption returns a line written as `-----`. This is a caption-reported website answer, not independently checked current submission policy.

**Figure 12 — BBC News success, p. 17.** Three panels navigate to music-related news and answer Taylor Swift. It demonstrates page navigation for a time-sensitive headline request. The historical caption answer is not a current claim.

**Figure 13 — Booking success, p. 18.** Nine panels show Jakarta input, date selection, scrolling, options, and answer. The request is a three-night stay from January 1 for two adults; the caption reports OYO 3755 Sweet Home at US$14 for the stay. The visual supports calendar and listing interaction, but tiny prices and the cheapest-across-all-options condition are not independently verified.

**Figure 14 — Cambridge Dictionary quiz success, p. 19.** Twelve panels show navigation to image quizzes, animal-answer selections, and a final score. The caption reports 6 out of 6. This demonstrates that the agent can perform a sequence of interactive choices rather than only retrieve text.

**Figure 15 — Coursera success, p. 20.** Five panels search for Introduction to Finance: The Basics, inspect the course, search Xi Yang, and answer. The caption names Xi Yang and two additional courses: Introduction to Finance: The Role of Financial Markets, and Introduction to Financial Analysis–The Why? It illustrates a request with several information components.

**Figure 16 — ESPN success, p. 20.** Five panels navigate and scroll through NBA teams. The caption reports 30 teams and names New York Knicks and New Orleans Pelicans for the requested New-name filter. These are historical example outputs, not external sports verification.

**Figure 17 — GitHub success, p. 21.** Five panels search climate change data visualization and navigate results. The caption reports resource-watch/resource-watch with 63 stars as the selected most-starred project. The screenshot sequence does not independently establish exhaustive search coverage, and stars are time-sensitive.

**Figure 18 — Google Map success, p. 21.** Four panels open directions, type Boston Logan Airport and North Station, and answer. The caption gives MA-1A S and approximately eight minutes under current traffic at evaluation time. Approximate duration is an author-reported example, not an estimate made from the image by this analyst.

**Figure 19 — Google Flights graph task, p. 22.** Eleven panels show a one-way Dublin–Athens request, date selection, flight results, and two price-graph views. The graphs are embedded browser content; their tiny axes and exact prices are not confidently readable. The caption answer says the price graph was analyzed and shows trends, but supplies no actual trend description or numerical price findings. This weakens what the illustrated answer demonstrates about satisfying the requested analysis, even though Appendix D presents it among successful cases.

**Figure 20 — Google Search movie task, p. 23.** Five panels move from search to a film-ranking page and scroll. The caption lists Life Is Beautiful, Back to the Future, The Intouchables, City Lights, and Modern Times as the top five requested comedy movies. No rating values are supplied in the caption; the ranking is an author-reported example result.

**Figure 21 — Huggingface model search, p. 23.** Six panels show navigation and filtering. The caption identifies replit/replit-code-v1-3b with 703 likes under a cc-by-sa-4.0 license condition. License and popularity are example outputs, not independently inspected model metadata.

**Figure 22 — Wolfram Alpha simplification, p. 24.** Three panels show entering a polynomial, scrolling, and answering with `(x − 4)^5 + 3(x − 4)^3 + 7`. It illustrates mathematical information retrieval through a website. The caption provides the exact polynomial and result; the tiny webpage derivation is not reconstructed.

**Figure 23 — Chinese Google Flights case, p. 24.** Eight panels accompany Chinese task and answer text. The request specifies Hangzhou–Shenzhen, June 15, 2024 outbound, June 20 return, departure at night, with departure time, airline, and price. The reported answer is 17:35, Shenzhen Airlines, HK$2,680. The paper supplies no definition of night; whether 17:35 satisfies that condition is unresolved. One trajectory does not establish broad Chinese-task performance.

**Figure 24 — Spanish dictionary case, p. 25.** Three panels type sostenibilidad, open a result, and answer. The displayed answer gives pronunciation `/sosteniβiliˈðað/`, feminine noun status, and an environmental-continuity definition. This is a selected Spanish-input example, with an English explanatory answer, not a measured multilingual evaluation.

**Figure 25 — Google Flights grounding failure, p. 25.** Six panels show calendar interactions for a January 22 one-way request from JFK to Heathrow. Appendix F reports selection of December 22 rather than January 22, followed by failed correction. The caption says the agent selects the wrong numerical label despite intending the correct date. The distinction between intention, screen label, and execution is central to the failure.

**Figure 26 — Allrecipes navigation failure, p. 26.** Six panels show down/down/down/up/up/down scrolling. The request requires Beef Wellington with at least 200 reviews, a rating of at least 4.5, and its ingredients. The agent fails to find the ingredients. The two-column extracted order puts Step 6 before Step 5, but the visual bottom-row layout establishes Steps 4, 5, and 6 left to right; this is an extraction-order issue, not evidence of changed execution order.

**Figure 27 — Coursera incomplete answer, p. 26.** Six panels show course search and assessment navigation. The agent answers only that Module 1 includes three quizzes, whereas the task requests course duration and the assessment quiz count more broadly. The authors classify this as hallucination/partial fulfillment. It illustrates that a plausible local fact can fail a multi-part global request.

**Figure 28 — BBC premature termination, p. 27.** Three panels show football navigation and ANSWER. The answer gives 12 Scottish Premiership teams but explicitly says further interaction is needed to obtain Hibernian's latest match start time. The authors identify premature stopping despite known incompleteness. This is particularly clear evidence that an executable termination action can be chosen even when the answer admits failure.

## 11. Table-by-table interpretation

### Table 1 — Main benchmark and automatic-evaluation results, p. 7

Columns are the 15 websites plus Overall; entries are Task Success Rate percentages. The first three rows use human expert labels. Starred rows use full-trajectory GPT-4V evaluation, with three evaluation repetitions producing mean ± standard deviation. Stars are evaluation-condition markers, not significance markers. No p-values or confidence intervals are supplied.

| Website | GPT-4 All Tools | Text-only, human | WebVoyager, human | Text-only*, GPT-4V judge | WebVoyager*, GPT-4V judge | Claude backbone*, GPT-4V judge | GPT-4o backbone*, GPT-4V judge |
|---|---:|---:|---:|---:|---:|---:|---:|
| Allrecipes | 11.1 | 55.6 | 53.3 | 57.8 ± 0.0 | 51.1 ± 2.2 | 45.9 ± 3.4 | 56.3 ± 1.3 |
| Amazon | 17.1 | 31.7 | 58.5 | 43.1 ± 1.4 | 52.9 ± 1.4 | 58.6 ± 4.2 | 53.7 ± 2.5 |
| Apple | 44.2 | 34.9 | 65.1 | 36.4 ± 3.5 | 62.8 ± 2.3 | 58.1 ± 4.0 | 56.6 ± 1.3 |
| ArXiv | 14.0 | 32.6 | 51.2 | 50.4 ± 1.4 | 52.0 ± 1.3 | 55.0 ± 7.0 | 60.5 ± 0.0 |
| GitHub | 48.8 | 61.0 | 63.4 | 63.4 ± 2.5 | 59.3 ± 3.7 | 56.9 ± 1.4 | 57.7 ± 3.7 |
| Booking | 22.7 | 2.3 | 43.2 | 2.3 ± 0.0 | 32.6 ± 2.7 | 19.0 ± 1.3 | 43.9 ± 3.5 |
| ESPN | 31.8 | 36.4 | 38.6 | 38.6 ± 2.3 | 47.0 ± 1.3 | 46.2 ± 1.3 | 44.0 ± 2.7 |
| Coursera | 31.0 | 23.8 | 73.8 | 24.6 ± 1.4 | 57.9 ± 2.7 | 68.2 ± 1.3 | 65.1 ± 2.8 |
| Cambridge Dictionary | 25.6 | 62.8 | 65.1 | 66.7 ± 3.6 | 71.3 ± 1.3 | 71.3 ± 3.6 | 82.2 ± 1.3 |
| BBC News | 9.5 | 45.2 | 61.9 | 45.2 ± 2.4 | 60.3 ± 2.8 | 66.7 ± 4.8 | 54.8 ± 2.4 |
| Google Flights | 2.4 | 7.1 | 59.5 | 7.1 ± 0.0 | 51.6 ± 1.4 | 15.1 ± 5.5 | 28.6 ± 0.0 |
| Google Map | 53.7 | 61.0 | 70.7 | 62.6 ± 2.8 | 64.3 ± 2.8 | 55.3 ± 1.4 | 56.9 ± 2.8 |
| Google Search | 60.5 | 67.4 | 76.7 | 75.2 ± 1.3 | 77.5 ± 2.7 | 72.9 ± 1.3 | 63.6 ± 1.3 |
| Huggingface | 37.2 | 20.9 | 44.2 | 31.0 ± 1.4 | 55.8 ± 2.3 | 53.5 ± 4.7 | 42.6 ± 3.6 |
| Wolfram Alpha | 52.2 | 58.7 | 63.0 | 60.2 ± 1.3 | 60.9 ± 2.2 | 51.5 ± 5.4 | 65.2 ± 2.2 |
| Overall | 30.8 | 40.1 | 59.1 | 44.3 ± 0.6 | 57.1 ± 0.2 | 52.8 ± 1.4 | 55.5 ± 0.8 |

The primary human rows show WebVoyager highest overall, but Allrecipes is a counterexample at website level. Within the starred configurations, the strongest website–configuration entry is GPT-4o on Cambridge Dictionary, 82.2% ± 1.3%, and the weakest is text-only Booking, 2.3% ± 0.0%. Claude and principal WebVoyager tie at a reported mean of 71.3% on Cambridge Dictionary, with different standard deviations. Per-site task counts vary, so an unweighted mean of website scores should not be substituted for the reported Overall. The authors' term significantly better is not accompanied by a statistical significance test in the supplied paper.

### Table 2 — Automatic judge versus humans, p. 7

| Screenshots supplied | Judge success rate | Agreement | Kappa |
|---|---:|---:|---:|
| k = 1 | 47.7% | 75.3% | 0.51 |
| k = 2 | 55.3% | 79.7% | 0.59 |
| k = 3 | 54.3% | 81.3% | 0.62 |
| Full | 58.3% | 85.3% | 0.70 |

Rows vary visual evidence available to GPT-4V; columns distinguish estimated success from label consistency. Full provides the highest agreement and kappa. The 58.3% full-trajectory success estimate is associated with this comparison setting and should not replace Table 1's 59.1% human benchmark result or 57.1% automatic overall mean. No per-row error bars or confusion matrices are supplied.

### Table 3 — Backbone–evaluator matrix, p. 7

| Agent backbone | GPT-4V evaluator | Claude 3 Opus evaluator | GPT-4o evaluator |
|---|---:|---:|---:|
| GPT-4V | 57.1 | 55.1 | 63.0 |
| Claude 3 Opus | 52.8 | 61.6 | 55.4 |
| GPT-4o | 55.5 | 54.9 | 64.1 |

Values are overall Task Success Rate percentages. Each row keeps the agent backbone fixed while varying the judge. Under GPT-4V and GPT-4o judges, Claude is lowest; under Claude's judge, Claude is highest. The largest entry is 64.1 for GPT-4o judging GPT-4o; the smallest is 52.8 for GPT-4V judging Claude. This supports the authors' discussion of leniency and preference for one's own outputs, but the table alone cannot isolate why the judges differ. It contains no uncertainty terms or formal bias test.

### Table 4 — Main failure reasons, p. 9

Navigation Stuck is 44.4%, Visual Grounding Issue 24.8%, Hallucination 21.8%, and Prompt Misalignment 9.0%. These sum to 100.0% [C: 44.4 + 24.8 + 21.8 + 9.0]. The denominator is classified failed cases within a 300-task sample, not all 643 benchmark tasks and not all 300 sampled tasks regardless of success. The exact failure count is unspecified. Navigation is the largest category and prompt misalignment the smallest. No inter-annotator agreement for the failure labels is reported.

## 12. Diagram / Architecture Interpretation

Figures 1–3 provide three complementary views. Figure 1 is the runtime feedback loop: user instruction → multimodal observation and thought → executable action → website change → next observation, ending in a user-facing answer. Figure 2 explains the interface between visual understanding and execution: webpage elements are converted into numbered targets, so an action can specify a concise label rather than an unconstrained pixel coordinate. Figure 3 is a data-development loop: seeds and generated tasks enter a shared pool, human checks filter them, and accepted examples guide further generation.

The underlying runtime components are the browser environment, element-marking script, screenshot/text observation construction, LMM, action parser/executor, history management, and optional PDF parser. The control path is the generated action; the data path is website-derived screenshot/text and optional parsed-file content. Exception messages provide another feedback input. Context clipping changes which earlier observations remain available, while action and thought history persist. [A, pp. 3–4, 13]

**Analyst security interpretation:** this architecture expands both incoming material and outgoing effects. Website and downloaded-file content can enter the decision process; Click and Type can cause real environment changes. The paper's risk paragraph recognizes harmful downloads and information submission. However, neither the diagrams nor their captions demonstrate attacker control, an exploited trust boundary, or a defense. The existence of a pathway is evidence of an interface to analyze, not evidence of a successful attack.

## 13. Equations and mathematical concepts

The central equations are unnumbered in §3.2, p. 3. The authors denote the environment by E, the multimodal model by M, observation space by O, and action space by A. Subscripts index steps rather than separate model versions.

**Context:** `c_t = (o_1, a_1, …, o_{t−1}, a_{t−1}, o_t, I)`. This is an ordered interaction history containing previous observations o_i, previous actions a_i, the current observation o_t, and I. In context, I appears to represent the user instruction, but the displayed notation does not explicitly define I; its identification as instruction is an analyst interpretation. Inputs are the accumulated interaction and task information; output is the context supplied to the model. The later clipping rule means the implementation retains only the three latest observations, despite the formal expression displaying a full-history sequence. This is a disclosed implementation simplification rather than an invented equivalence.

**Action generation:** `a_t = M(c_t)`. The model maps current context to the next action. It expresses an inference/control step, not a training loss or optimization objective. The action is then executed in the browser. The source does not formulate a probability distribution or guarantee that the chosen action is correct.

**Environment update:** `o_{t+1} = E(o_t, a_t)`. The environment maps the current observation and selected action to the next observation. This is the paper's simplified interaction notation; no full browser-state representation or stochastic transition model is separately specified. The equation is used to explain repeated sensing and acting until termination or the budget limit.

**Thought/action composition:** `a_t = (s_t, â_t)`, described as composing a_t into a natural-language thought s_t and action code â_t. The thought supports planning; the code identifies an executable operation. The system prompt concretizes this as Thought and Action fields. A thought without a parsable action is one documented failure mode. [A, pp. 3, 9, 14]

There is no numbered mathematical optimization problem, learned loss, theorem, or proof. Task Success Rate is defined verbally as successful task completion; kappa is reported and cited but not mathematically derived. Figure 22's example is `x^5 − 20x^4 + 163x^3 − 676x^2 + 1424x − 1209` rewritten as `(x − 4)^5 + 3(x − 4)^3 + 7`. Here x is a polynomial variable, not a system parameter. The paper presents this as a retrieved website answer, not a methodological theorem.

**Analyst-derived consistency check:** the reported pair count matches the number of unordered pairs among 643 tasks: `643 × 642 / 2 = 206,403`. This supports numerical consistency of the diversity-check denominator but says nothing about whether the similarity model captures every kind of duplicate task.

## 14. Interpretation and discussion

The results support the authors' main capability argument: combining screenshots and element text with direct browser action improves task completion over the reported baselines in this benchmark. They do not isolate the entire gain to vision alone, because the All Tools baseline differs in browsing access and workflow. The authors attribute its weakness partly to dependence on Bing-fetched pages and limited direct use of search, clicking, and sorting on certain sites. The text-only WebVoyager comparison is closer to an observation-modality contrast, though the paper does not expose every implementation-equivalence detail. [A, pp. 6–8; D]

O1 is supported by a working runtime and selected complete trajectories, but success of 59.1% means autonomous task completion is not reliable across all sampled cases. O2 is supported by the documented construction and 643-task inventory. O3 receives agreement evidence, qualified by residual disagreement, evaluator dependence, and the evaluator prompt's acceptance of unpictured response content. O4 receives the main table, GAIA plot, SeeAct comparison, and evaluator matrix. O5 receives the scatterplot and labeled failure analysis, without a formal causal study. [A/D]

Several consistency issues remain. The Figure 5 baseline name includes GPT-4V while the main text names GPT-4. Figure 19's caption describes a graph-analysis task but provides only a generic assertion of analysis. Figure 23 requests nighttime departure but reports 17:35 without defining nighttime. These points should not be silently normalized into stronger success evidence. The differences among 59.1%, 58.3%, and 57.1% are not inherently contradictions: they arise in human benchmark evaluation, screenshot-context judge comparison, and repeated automatic benchmark evaluation, respectively. [A/B/D, pp. 7–8, 22, 24]

For security, the strongest source-grounded conclusion is narrower than the requested comparative question: browser integration gives the model pathways to affect external systems, and the authors acknowledge potentially harmful consequences. The observed wrong-textbox and premature-answer failures show that apparently valid actions can violate the task's intent. **Analyst inference:** similar intent–execution mismatches could matter in a security-sensitive workflow. The paper does not show that they are exploitable, more frequent under attack, or more severe than errors from a standalone LLM.

## 15. Contributions and novelty

**System contribution:** an autonomous LMM browser agent working on real websites through repeated observations and actions. **Method contribution:** screenshot-first observations augmented by interactive-element text, rule-based numbered element marking, a concise action vocabulary, and clipped observation history. **Benchmark contribution:** 643 manually checked, partly model-generated tasks across 15 websites with Golden/Possible answer annotations. **Evaluation contribution:** full-trajectory multimodal automatic judging compared with human judgments. **Empirical contribution:** comparisons across modalities, backbones, evaluators, additional task sets, website complexity, and failure types. [A, pp. 1–9]

The authors position the system as avoiding a separate candidate-selection model and exposing more realistic online task completion than simplified or stepwise settings. There is no new formal theorem, security defense, adversarial benchmark, or vulnerability measurement. Security relevance is a secondary analytical use of the architecture and limitation statements, not an author-demonstrated central novelty.

## 16. Limitations

### Authors' stated limitations

The action set does not support every human browser action, especially Drag. The authors describe difficulty because drag extent is not a finite set and propose selecting pixel values when visual grounding improves. File support is limited to basic formats such as text and PDF, excluding full support for videos and other formats. [A, pp. 9–10]

The authors acknowledge difficulty with dense text, subtle visual changes, neighboring elements, unfamiliar pronunciation characters and formulas, complex calendars, scrolling regions, and long instruction contexts. Input clipping can contribute to repeated errors. Additional backbones have specific Google Flights problems: GPT-4o fails to select one-way travel in some cases, while Claude struggles entering basic flight information. [A, pp. 6–9]

Benchmark selection excludes login/CAPTCHA-dependent websites. The discussion attributes the absence of open-source LMM experiments to image downsampling to 224 × 224 or 336 × 336 and a 4096-token context for models such as LLaVA, compared with approximately 7000+ tokens for up to 15 steps. These are the authors' 2024 rationale about referenced models, not current externally verified limits of all open-source systems. [A, pp. 4, 8]

Potential risks explicitly include unintentional malicious-content downloads, private/confidential information entered on public sites, fake server requests, and fake user activities harmful to website owners. The authors call for substantial safety checks before deployment. [A, p. 10]

### Additional evidence-based analyst observations

The supplied evidence cannot establish security robustness: no attacks or standalone-model comparison are included. Non-login harmless tasks restrict the tested risk profile. A correct answer can coexist with unsafe activity that binary task-success judging would not capture. The evaluator's acceptance of response content missing from screenshots weakens independent outcome verification. Model–judge preference complicates comparisons. Live website changes and time-sensitive Possible answers limit repeatability. Selected success figures are illustrative rather than representative sampling. These are analyst observations, not statements that the authors formally admitted all of these threats.

## 17. Threats to validity

The following labels organize analyst observations; they are not a named validity framework used by the authors.

**Internal validity.** Baseline browsing capabilities differ, so the comparison does not isolate one mechanism as the cause of all improvement. Website-specific assertions about dense text and calendars are plausible and supported by patterns, but lack controlled interventions. Figure 6 is associative, and selected completed trajectories can affect average-length interpretation.

**Construct validity.** Task Success Rate measures completion, not route optimality, security, privacy protection, or truthful claims independently of trajectory evidence. Golden/Possible annotations accommodate ambiguity but introduce judgment dependence. The evaluator prompt can accept unsupported response content if not contradicted by screenshots, and a generic graph-analysis assertion is presented as a successful example.

**Statistical conclusion validity.** Repeated evaluation means and standard deviations describe judge variation, not necessarily environment or agent-run variation. No formal significance testing, confidence intervals for human benchmark scores, per-level GAIA counts, or failure-category uncertainty are supplied. High agreement does not identify which kinds of mistakes the evaluator misses.

**External and ecological validity.** Live websites increase environmental realism, while exclusions of login, CAPTCHA, multiple tabs, drag, and many file formats restrict the range of tasks. The benchmark's harmless manually inspected queries do not establish behavior on malicious pages or authenticated private workflows. Multilingual coverage consists of two examples.

**Reproducibility.** Configuration includes viewport, temperatures, model names, and step budget, but does not report hardware, browser/library versions, seeds, exact website snapshots, complete raw trajectories, or the full prompt beyond ellipses in Figure 7. The repository announcement is not a reviewed replication artifact. None of these observations proves the results wrong; they define what the supplied evidence can support.

## 18. Future work and open questions

**A. Author-proposed directions.** Augment screenshot inputs with extracted HTML text for text-heavy sites; improve visual encoders or add textual cues; optimize general-purpose prompts while preserving universality; modify prompts for additional backbones; address navigation, grounding, hallucination, and prompt-alignment failures; support drag through pixel-based choices when grounding improves; support more file formats; and implement substantial deployment safety checks. [A, pp. 6–10, 13]

**B. Analyst open questions.** Does website-provided content influence the agent differently from the authorized user task? Which browser capabilities increase potential harm, and which controls restrict them? Can a system distinguish useful website information from unauthorized task redirection? Do execution errors become consequential in authenticated settings? Can an evaluator assess both completion and unsafe side effects without accepting unpictured claims? How much performance variation comes from model randomness, judge randomness, and website changes? These are research questions suggested by the architecture and gaps, not experiments already answered by this paper.

For the user's comparative security question, a future study would need explicit standalone-model and browser-agent conditions, an attack model, controlled hostile inputs, clearly defined outcomes, and comparable task settings. This statement identifies missing evidence requirements; it does not introduce external attack findings.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| LLM | Large language model; a model used for language understanding and generation |
| LMM | Large multimodal model; here, a model receiving images and text |
| GPT-4V | Vision-capable model used as agent backbone and automatic evaluator |
| GPT-4o | GPT-4 Omni; an additional backbone and evaluator |
| Selenium | Software used to automate the real browser environment |
| HTML / DOM | Webpage markup / its structured document representation, described as potentially verbose inputs |
| Accessibility tree | Structured textual webpage representation used by the text-only baseline |
| Visual grounding | Matching a visible screen item to the correct interaction target |
| Bounding box | Border marking an interactive webpage element |
| Numerical label | Number attached to an element so the action can identify it |
| aria-label | Element attribute whose text can supplement the observation |
| ReAct | Prompting approach producing a thought before an action |
| Set-of-Mark | Prompting inspiration for marking screen elements |
| Self-instruct | Generating new instructions from examples, followed here by manual checks |
| In-context example | Example supplied in the prompt to guide new task generation |
| Trajectory | Sequence of observations and actions during a task |
| Golden trajectory | Predefined action route used in some earlier evaluations |
| Golden answer | Comprehensive response listing regarded as short-term stable |
| Possible answer | Partial, open-ended, multiple-valid, or time-varying response annotation |
| Task Success Rate | Proportion of tasks judged completed; does not require optimal steps |
| Agreement | Label overlap between automatic and human judgments |
| Kappa, κ | Named agreement statistic reported for annotators or judges; equation not supplied |
| Context clipping | Removing older observations while preserving thought/action history |
| E, M, O, A | Environment, model, observation space, and action space |
| t, o_t, a_t, c_t | Step index, observation, action, and model context at that step |
| s_t, â_t | Natural-language thought and executable action code |
| I | Symbol in context equation; instruction meaning is implicit rather than explicitly defined |
| CAPTCHA | Completely Automated Public Turing test to tell Computers and Humans Apart, expanded in the footnote |
| Hallucination | Author's category including partially correct answers and actions leading to wrong answers |
| Prompt Misalignment | Author's category including unparsable action output and knowingly premature termination |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Benchmark size | 643 | tasks | 15 websites | Author-reported | p. 5, §4.2 |
| Tasks per website | 40–45 | tasks | Table 1 benchmark | Author-reported | p. 7, T1 caption |
| Golden-answer share | 22.3 | % | Full benchmark | Author-reported | p. 5, §4.3 |
| Similarity pairs | 206,403 | pairs | 643 questions | Author-reported | p. 5 |
| Similarity > 0.8 | 49 | pairs | Manually checked | Author-reported | p. 5 |
| Similarity 0.7–0.8 | 140 | pairs | Manually checked | Author-reported | p. 5 |
| Similarity < 0.6 | 99.68 | % of pairs | Diversity analysis | Author-reported | p. 5 |
| Viewport | 1024 × 768 | pixels | Agent observations | Author-reported | p. 5 |
| Agent/evaluator temperatures | 1 / 0 | parameter | Generation / automatic judging | Author-reported | pp. 5, 13 |
| Maximum exploration | 15 | steps | Includes correction attempts | Author-reported | pp. 4–5 |
| Observations retained | 3 | observations | Full thought/action history retained | Author-reported | p. 3 |
| Main success | 59.1 | % | WebVoyager, human judge | Author-reported | p. 7, T1 |
| Baseline successes | 30.8 / 40.1 | % | All Tools / text-only, human judge | Author-reported | p. 7, T1 |
| Main absolute gains | 28.3 / 19.0 | percentage points | 59.1−30.8 / 59.1−40.1 | Analyst-derived | p. 7 operands |
| Human-comparison subset | 300 | tasks | Three human annotators | Author-reported | p. 6 |
| Human pre-discussion agreement | 0.7 | Fleiss's kappa | Three annotators | Author-reported | p. 6, footnote 7 |
| Full GPT-4V agreement | 85.3 | % | Against consolidated humans | Author-reported | p. 7, T2 |
| Full GPT-4V kappa | 0.70 | kappa | Human-comparison setting | Author-reported | p. 7, T2 |
| Full-judge disagreement | 14.7 | % | 100−85.3; not a false-positive rate | Analyst-derived | p. 7 operand |
| Additional evaluator kappas | 0.60 / 0.72 | kappa | Claude / GPT-4o versus humans | Author-reported | p. 7 |
| Automatic overall successes | 57.1 ± 0.2 / 52.8 ± 1.4 / 55.5 ± 0.8 | % | GPT-4V / Claude / GPT-4o backbones, GPT-4V judge | Author-reported | p. 7, T1 |
| Evaluation repetitions | 3 | judge runs | Mean and standard deviation | Author-reported | p. 7, T1 caption |
| GAIA sample | 90 | tasks | Level 1/2 web tasks | Author-reported | p. 5 |
| GAIA Level 1 | 23.1 / 19.2 / 38.5 | % | All Tools / text-only / WebVoyager | Visually readable | p. 8, F5 |
| GAIA Level 2 | 12.5 / 12.5 / 15.6 | % | Same ordering | Visually readable | p. 8, F5 |
| SeeAct sample and successes | 50; 30 / 26 | tasks; % | WebVoyager / best autonomous SeeAct | Author-reported | pp. 5–6 |
| Failure shares | 44.4 / 24.8 / 21.8 / 9.0 | % of classified failures | Navigation / grounding / hallucination / misalignment | Author-reported | p. 9, T4 |
| Pair-count check | 206,403 | pairs | 643×642/2 | Analyst-derived | p. 5 operands |

Exact Figure 6 coordinates are not included because they are unlabeled visual positions. Numerical task-example answers are preserved in the figure register as historical caption-reported values, not benchmark statistics or current verified website facts.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Agent performs real-browser multimodal interaction | Selenium, screenshots, element text, generated and executed actions | F1–2; X1 architecture | pp. 3–4 | HIGH for documented design; implementation not executed here |
| Dataset combines model generation and human verification | Seed pool, GPT-4 Turbo generation, manual filtering, 643 tasks | F3; X8 | pp. 4–5 | HIGH source confidence; raw data absent |
| WebVoyager improves overall task completion | 59.1% versus 40.1% and 30.8% | T1; X1 | p. 7 | HIGH for reported conditions; no formal significance test |
| Vision helps some complex interfaces | Booking and Flights gaps | T1; X1 | pp. 6–8 | HIGH values; mechanism explanation is author interpretation, not isolated causal proof |
| Multimodal superiority is not universal | Allrecipes 53.3% versus text-only 55.6% | T1 | p. 7 | HIGH; website-level counterexample |
| Full trajectories improve automatic judge agreement | 75.3% to 85.3%, κ 0.51 to 0.70 | T2; X4 | p. 7 | HIGH; disagreement remains |
| Judge choice changes score and ranking | Three-by-three backbone–judge matrix | T3; X5 | pp. 7–8 | HIGH observed scores; bias mechanism not experimentally isolated |
| Navigation is the largest labeled failure group | 44.4% of classified failures | T4; X7 | pp. 8–9 | HIGH; failed-case count and category reliability unspecified |
| Browser action can be valid yet task-inappropriate | Wrong text-box example; early Answer | F28; failure discussion | pp. 9, 27 | HIGH for examples; no adversarial cause demonstrated |
| Safety checks are needed according to authors | Malicious downloads, private data submission, fake requests/activity | Limitations | p. 10 | HIGH for warning; no measured incident rate |
| Architecture is relevant to agent security | Website inputs feed a model whose outputs become actions | F1; §3; Appendix C | pp. 3–4, 13 | MEDIUM analyst inference; does not prove comparative vulnerability |
| Standalone-LLM vulnerability comparison remains unanswered | Reported experiments measure agent completion and evaluator consistency | X1–X7 | pp. 5–10 | HIGH confidence in scope boundary; no security comparison supplied |

Source-grounded checking distinguishes the human Table 1 condition from starred judge conditions, the 300-task comparison subset from 643 tasks, and failure shares from total-task rates. Captions and visual panels were revisited within the supplied evidence when describing key examples. No inference is promoted into a direct author claim.

## 22. Very simple explanation — Explain Like I'm 15

Imagine an AI that can see a webpage and use a mouse and keyboard. To make clicking easier, this system puts a number beside each useful button or box. The AI looks at the page, chooses one numbered item or a scrolling action, watches what changes, and repeats. Its job is to finish the whole request, such as finding an item and checking whether it is available nearby.

The researchers tested it on 643 tasks from 15 websites. People judged that it finished 59.1% of them, compared with 40.1% for a version receiving only a text description of the page and 30.8% for another tool-using agent. Seeing the page helped especially with complicated interfaces, but the system still got lost, clicked the wrong thing, answered only part of a question, or stopped too soon.

They also asked another AI to judge success from the browsing record. With the whole record, it agreed with people 85.3% of the time. That is useful, but it is not perfect, and different judging models gave different scores. A convincing answer alone is not always proof that the requested work was done.

For your security question, the key difference suggested by this paper is that a browser agent can act on real websites: it can type information, click links, and download files. The authors warn that these actions could have harmful consequences. But this paper did not attack the agent or compare its security with an AI that only chats. It explains why those extra connections deserve investigation; it does not prove how much more vulnerable they make the agent.

## Completeness Audit

The inventory, rather than length alone, is the basis of coverage. Every identified substantive section, subsection, table, figure, interaction equation, contribution, and available appendix is represented below or explicitly bounded. Full representation means its substantive content is covered, not that every sentence or every tiny screen element has been transcribed.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, abstract | Yes, text and image | Yes | Fully represented | Identity and central reported results |
| §1 Introduction | Yes, text and image | Yes | Fully represented | Motivation, gap, three contributions |
| §2 Related Work | Yes, text and image | Yes | Represented in compressed form | Categories and relevant contrasts; no independent literature validation |
| §3 WebVoyager | Yes, text and image | Yes | Fully represented | Runtime and iterative control |
| §3.1 Browsing Environment | Yes | Yes | Fully represented | Selenium, live sites, CAPTCHA footnote |
| §3.2 Interaction Formulation | Yes | Yes | Fully represented with uncertainty | All interaction equations; I implicit |
| §3.3 Observation Space | Yes | Yes | Fully represented | Marking, auxiliary text, single tab, exception feedback |
| §3.4 Action Space | Yes | Yes | Fully represented | Seven actions and termination |
| §4.1 Website Selection | Yes | Yes | Fully represented | All 15 sites and exclusions |
| §4.2 Data Construction | Yes | Yes | Fully represented | Generation, filtering, counts, similarity |
| §4.3 Annotation Process | Yes | Yes | Fully represented | Golden/Possible and 22.3% |
| §5 Dataset and Metrics | Yes | Yes | Fully represented | Benchmark, GAIA, SeeAct, success definition |
| §5 Experimental Details | Yes | Yes | Fully represented | Models, viewport, temperature, budget; unreported details identified |
| §5.1 Evaluation Methods | Yes | Yes | Fully represented | Human protocol and screenshot-context judge |
| §5.2 Result | Yes | Yes | Fully represented | Main, transfer, model, judge results |
| §5.3 Discussions | Yes | Yes | Fully represented | Direct interaction, modality tradeoffs, complexity, open-source rationale |
| §5.4 Error Analysis | Yes | Yes | Fully represented | Four categories and examples |
| §6 Conclusion | Yes | Yes | Fully represented | Capability and evaluation contribution |
| Limitations, pp. 9–10 | Yes; p. 10 text-only | Yes | Fully represented | Drag, formats, deployment risks |
| Ethics Statement | Yes, text-only | Yes | Fully represented | Non-login, monitoring, manual harmlessness inspection |
| References | Yes, text-only pp. 10–12 | Yes | Represented in compressed form | Related-work roles; individual bibliographic entries not reproduced |
| Explicit research questions/hypotheses | Checked | Yes | None identified | Informal objectives separated from user research question |
| X1 main benchmark | Yes | Yes | Fully represented | Human versus automatic conditions distinguished |
| X2 GAIA | Yes | Yes | Fully represented | Per-level sample counts unspecified |
| X3 SeeAct | Yes | Yes | Fully represented with limits | 50 tasks; 30% versus 26% |
| X4 screenshot-context judging | Yes | Yes | Fully represented | All Table 2 values |
| X5 backbone/evaluator study | Yes | Yes | Fully represented | Tables 1 and 3; kappas |
| X6 complexity association | Yes | Yes | Represented with uncertainty | No exact coordinates or causal result |
| X7 failure analysis | Yes | Yes | Fully represented | Failure denominator not numerically specified |
| X8 diversity and illustrative cases | Yes | Yes | Represented in compressed form | Similarity figures and selected examples |
| F1 workflow | Yes, visual and text | Yes | Fully represented | Inputs, actions, feedback, answer |
| F2 marked observation | Yes, visual and text | Yes | Fully represented | Tiny target labels not exhaustively transcribed |
| F3 data construction | Yes, visual and text | Yes | Fully represented | Pool and filtering arrows |
| F4 Apple | Yes, visual and text | Yes | Represented in compressed form | Six-panel trajectory and answer |
| F5 GAIA plot | Yes, visual and text | Yes | Fully represented | All labels; baseline naming discrepancy |
| F6 complexity plot | Yes, visual and text | Yes | Represented with uncertainty | Axes, color, broad positions; exact coordinates absent |
| F7 agent prompt | Yes, visual and text | Yes | Fully represented with limits | Ellipses mean exhaustive prompt absent |
| F8 evaluation prompt | Yes, visual and text | Yes | Fully represented | Evidence hierarchy and unpictured-response rule |
| F9 Allrecipes | Yes, visual and text | Yes | Represented in compressed form | Task, six panels, rating/time |
| F10 Amazon | Yes, visual and text | Yes | Represented in compressed form | Task, three panels, product/rating |
| F11 ArXiv | Yes, visual and text | Yes | Represented in compressed form | Seven panels, separator answer |
| F12 BBC | Yes, visual and text | Yes | Represented in compressed form | Three panels, headline answer |
| F13 Booking | Yes, visual and text | Yes | Represented in compressed form | Nine panels, dates/occupancy/price |
| F14 Cambridge quiz | Yes, visual and text | Yes | Represented in compressed form | Twelve panels, 6/6 |
| F15 Coursera | Yes, visual and text | Yes | Represented in compressed form | Five panels, instructor and courses |
| F16 ESPN | Yes, visual and text | Yes | Represented in compressed form | Five panels, teams and name filter |
| F17 GitHub | Yes, visual and text | Yes | Represented in compressed form | Five panels, project and 63 stars |
| F18 Google Map | Yes, visual and text | Yes | Represented in compressed form | Four panels, route and approximate duration |
| F19 Google Flights | Yes, visual and text | Yes | Represented with uncertainty | Eleven panels; graph values unreadable; generic answer caveat |
| F20 Google Search | Yes, visual and text | Yes | Represented in compressed form | Five panels and all five movies |
| F21 Huggingface | Yes, visual and text | Yes | Represented in compressed form | Six panels, license/model/likes |
| F22 Wolfram Alpha | Yes, visual and text | Yes | Fully represented | Three panels and polynomial identity |
| F23 Chinese Flights | Yes, visual and text | Yes | Represented with uncertainty | Eight panels; night/17:35 mismatch unresolved |
| F24 Spanish dictionary | Yes, visual and text | Yes | Represented in compressed form | Three panels, pronunciation/definition |
| F25 grounding failure | Yes, visual and text | Yes | Fully represented | Six panels, January/December error |
| F26 navigation failure | Yes, visual and text | Yes | Fully represented | Six panels; extraction-order issue accounted for |
| F27 partial course answer | Yes, visual and text | Yes | Fully represented | Six panels; missing task components |
| F28 premature termination | Yes, visual and text | Yes | Fully represented | Three panels; explicit admission of incompleteness |
| T1 benchmark scores | Yes, visual and text | Yes | Fully represented | Every website/configuration entry retained |
| T2 judge consistency | Yes, visual and text | Yes | Fully represented | All values and conditions |
| T3 judge/backbone matrix | Yes, visual and text | Yes | Fully represented | All nine entries |
| T4 failure distribution | Yes, visual and text | Yes | Fully represented | All categories and denominator qualification |
| Major equations | Yes, visual and text | Yes | Fully represented with uncertainty | Context, action, update, decomposition; I implicit |
| Numbered algorithms/theorems | Checked | Yes | None identified | Action protocol is described in prose and prompts |
| Major contributions | Yes | Yes | Fully represented | System, dataset, method, evaluation, empirical findings |
| Author-stated limitations | Yes | Yes | Fully represented | Includes p. 10 security-risk continuation |
| Appendix A | Yes | Yes | Fully represented with limits | Generic prompt rationale and F7 |
| Appendix B | Yes | Yes | Fully represented | Temperature 0 and F8 |
| Appendix C | Yes | Yes | Fully represented | Formats, ENTER, region scroll, PDF parsing |
| Appendix D | Yes | Yes | Represented in compressed form | All successful/multilingual example figures |
| Appendix E | Yes | Yes | Represented in compressed form | Vision agents and multimodal-model background |
| Appendix F | Yes | Yes | Fully represented | All four failure examples |
| Footnotes 1–8 | Yes, supplied text | Yes | Represented in compressed form | Availability, baseline, software, CAPTCHA, similarity model, human kappa, PDF API; links not visited |
| Separate supplementary material | Not supplied | No | Missing from supplied material | No separate supplement reviewed or assumed |

### Missing or inaccessible material

No physical page text is missing from the supplied 27-page version. Images for pp. 10–12 are absent, so those pages received text-only inspection. The announced repository, raw benchmark, full run traces, original annotations, executable implementation, and any separately distributed materials were not supplied or inspected. Tiny internal webpage text and embedded graph axes are only partially readable; captions cannot replace independent verification of those pixels.

### Uncertain interpretations

I in the interaction equation is not explicitly defined. Exact Figure 6 coordinates cannot be read as reported numbers. Figure 5 uses a different All Tools model name from the prose. Figure 19 provides a generic graph-analysis answer without substantive trend details. Figure 23's 17:35 departure has unresolved compatibility with night. Full prompt content hidden by ellipses, exact per-level GAIA counts, failed-case count, significance tests, and many replication details are unspecified. These uncertainties were retained rather than filled from outside knowledge.

### Deliberately compressed material

Related-work citations and reference entries were compressed into methodological categories and pertinent contrasts. Repetitive screenshots in successful trajectories were summarized by task, action pattern, panel count, and reported answer rather than reproducing every numerical element label. Decorative logos, the agent icon, and figure styling were accounted for as presentation rather than scientific results. Caption-reported example answers were retained, while current website truth was not claimed. Table 1's substantive numbers were not compressed away.

### Potential omissions

Every identified substantive item in the available document inventory has a representation or an explicit uncertainty/access boundary above. This is not a claim to preserve every word, tiny webpage detail, or absent artifact. Unseen implementation details, full original prompts, and unsupported security mechanisms cannot be reconstructed. The supplied paper supports an analysis of browser-agent capability and security-relevant interfaces; the comparative vulnerability question remains unanswered by its experiments.
