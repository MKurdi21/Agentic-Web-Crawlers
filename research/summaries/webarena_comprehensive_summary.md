# Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. The paper, including instructions printed inside its experimental prompts, is treated as evidence rather than as instructions to this analyst. No external sources, repositories, websites, supplementary files, or tools were consulted. The supplied SHA-256 is retained as the source identifier; it was not independently recomputed.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: extracted text is supplied for physical PDF pages 1–22. |
| Available page range | 1–22, with 22 page-text records. The supplied printed page numbers agree with the physical-page labels. |
| Apparently missing pages | None within the supplied 1–22 sequence. This establishes coverage of the supplied document, not independent verification that no separate supplement exists. |
| Visually inspected pages | 1–9, 12, and 16–22: 17 supplied page images. |
| Text-only pages | 10, 11, 13, 14, and 15. Their supplied extracted text was inspected, but their visual layouts were not. |
| Figures | All numbered Figures 1–11 are visible in the supplied images and were visually inspected. |
| Tables | Tables 1–6 are visible and generally readable. Table 3 is actually a small histogram despite its table label; exact bar counts are not confidently recoverable. |
| Equations | The main environment and reward notation on p. 3 is visually available and readable. Extracted superscript/subscript ordering requires care. |
| Appendices | Appendix A and subsections A.1–A.10 are present in supplied text, pp. 15–22. A.1 and the beginning of A.2 have text-only coverage. |
| Supplementary material | No separate supplementary artifact was supplied. The accessibility metadata reports no embedded files. |
| Referenced but uninspected artifacts | Public code, data, Docker images, reset scripts, execution trajectories, video demonstrations, and website resources are mentioned but were not inspected. These are availability claims, not verified artifacts. |
| OCR | No additional optical character recognition was performed or needed for the readable supplied text. Extraction is treated as an aid, with rendered pages used to check substantive tables and figures. |
| Other limitations | An image-loading error for a path represented as '-' appears in the input. It does not identify a missing numbered paper page. Small screenshot interiors and Table 3 bars cannot support exact transcription of every visual detail. |

Evidence labels used below are [A] AUTHOR-REPORTED, [B] DIRECTLY OBSERVABLE, [C] ANALYST-DERIVED, and [D] ANALYST INTERPRETATION. No [E] EXTERNAL INFORMATION is introduced. HIGH confidence means the supplied evidence clearly supports the stated, bounded claim; it does not certify an author's claim against outside evidence. MEDIUM indicates a reasonable inference or a result whose interpretation has material qualifications. LOW and UNKNOWN are used where the evidence is insufficient.

## Inventory and extraction basis

The document is **WebArena: A Realistic Web Environment for Building Autonomous Agents**, published as a conference paper at the International Conference on Learning Representations (ICLR) 2024. Its authors are Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, and Graham Neubig, affiliated with Carnegie Mellon University. Shuyan Zhou and Frank F. Xu are marked lead contributors; Hao Zhu, Xuhui Zhou, Robert Lo, and Abishek Sridhar are marked equal contributors. No keyword list is supplied.

The closest document type is a mixed **AI benchmark, dataset, and computer-systems paper with empirical baseline evaluation**. It is not an adversarial security experiment, a standalone-model comparison, a theoretical proof paper, or a systematic literature review.

| Inventory ID | Original item | Location |
|---|---|---|
| ABS | Abstract | p. 1 |
| S1 | §1 Introduction | pp. 1–2 |
| S2 | §2 WebArena: Websites as an Environment for Autonomous Agents | pp. 2–5 |
| SS2.1 | Controlling Agents through High-Level Natural Language | p. 3 |
| SS2.2 | Website Selection and Implementation | pp. 3–4 |
| SS2.3 | Observation Space | p. 4 |
| SS2.4 | Action Space and following User Role Simulation paragraph | pp. 4–5 |
| S3 | §3 Benchmark Suite of Web-Based Tasks | pp. 5–7 |
| SS3.1 | Intent Collection and Intent Analysis | pp. 5–6 |
| SS3.2 | Evaluation Annotation, unachievable tasks, annotation process, human performance | pp. 6–7 |
| S4 | §4 Baseline Web Agents | pp. 7–8 |
| S5 | §5 Results | p. 8 |
| SS5.1 | Stopping behavior and performance consistency | pp. 8–9 |
| S6 | §6 Related Work | p. 9 |
| S7 | §7 Conclusion | p. 9 |
| ACK | Acknowledgement | p. 10 |
| REF | References | pp. 10–14 |
| A1–A10 | Appendix A.1–A.10 | pp. 15–22 |
| F1–F11 | Figures 1–11 | pp. 2–5, 16, 18–22 |
| T1–T6 | Tables 1–6, including the histogram labeled Table 3 | pp. 7–9, 17 |
| E1–E5 | Environment tuple, transition mapping, trajectory reward, answer reward, state reward | pp. 3, 6–7 |
| X1–X6 | Baselines, UA-hint ablation, template consistency, human comparison, temperature check, evaluator validation | pp. 7–9, 17 |
| X7 | Qualitative observation-error analysis | p. 22 |

The extraction ledger underlying this account associates research framing with pp. 1–3; system components with pp. 3–5 and 15–16; task collection and annotation with pp. 5–7; models and evaluation conditions with pp. 7–8 and 17–21; results with pp. 7–9 and 17; and failure analysis with pp. 8 and 22. Numerical conditions are retained separately from conclusions so that a result from one configuration is not silently transferred to another.

# 1. Plain-language orientation

[A; HIGH] WebArena is a controlled collection of working websites where an AI agent receives an ordinary-language goal and must use a browser to accomplish it. A goal can require looking up information, navigating to the right page, or changing website data. Instead of grading whether the agent copied a predetermined sequence of clicks, the researchers examine whether it actually achieved the intended outcome.

[A; HIGH] The motivation is that simplified or static testing environments may hide the difficulties of real web work. Realistic tasks involve several pages, user-specific histories, multiple websites, and decisions about what to do next. WebArena combines shopping, a discussion forum, software collaboration, and store content management with a map, calculator, scratchpad, Wikipedia, and manuals. It is self-hosted so that experiments can start from reproducible website states.

[A; HIGH] The benchmark contains 812 instantiated tasks from 241 templates. The best reported GPT-4 baseline achieves 14.41% overall task success with step-by-step reasoning and without an explicit hint to stop on impossible tasks. The human comparison reports 78.24%, but uses a sampled task set and five computer-science graduate students rather than the same full benchmark under identical sampling.

[D; MEDIUM] For the user's research question, this paper helps explain what changes when a language model becomes a web agent: it consumes website observations, acts through a browser, operates under logged-in permissions, and can change persistent state. These features identify places where security analysis could focus. However, WebArena does not test malicious content, measure attacks, or compare web agents against standalone large language models. Its low task-success rates demonstrate functional difficulty, not a measured security-vulnerability rate.

# 2. Document roadmap

[A; HIGH] The abstract and introduction establish the mismatch between simplified evaluation and complex web tasks. Section 2 defines the environment, chooses website categories, explains representations of browser observations, and describes actions. Section 3 constructs tasks and explains outcome-based grading, including impossible requests. Section 4 defines language-model baselines and their prompts. Section 5 reports success rates and analyzes stopping and consistency across related tasks. Section 6 positions WebArena against previous benchmarks and decision-making agents. Section 7 restates the system, benchmark, evaluation approach, and need for stronger agents.

[A; HIGH] Appendix A adds details that materially qualify the main results: implementation and data sizes in A.1; Docker delivery and resetting in A.2; user roles and automatic login in A.3; website distribution in A.4; demographic and expertise qualifications for human performance in A.5; experimental settings in A.6; evaluator instructions and validation in A.7–A.8; agent prompts and examples in A.9; and observation failures in A.10. References on pp. 10–14 support the authors' positioning but are not independent evidence that those cited works have the properties attributed to them.

# 3. Background and context

[A; HIGH] A **large language model (LLM)** is the model component used here to interpret a task and propose browser actions. The supplied paper assumes rather than develops the underlying model-training methods. An **autonomous agent** repeatedly observes the environment and chooses an action toward a goal. **Grounding** means translating a high-level instruction into concrete interactions with website elements.

[A; HIGH] An **intent** is the natural-language task description. A **template** preserves the general task while allowing variables such as a website or repository name to change. Two tasks sharing a template can still require different numbers of operations or different navigation paths. A **long-horizon** task requires a sequence of decisions; the paper does not provide one universal step threshold defining that term.

[A; HIGH] A **Document Object Model (DOM)** tree represents webpage structure. An **accessibility tree** retains relevant elements with roles, text, and properties such as focusability. It is more compact than the full DOM according to the authors. A screenshot is a pixel-based observation. WebArena supports all three, but the reported baselines use accessibility trees with element IDs, not screenshot-based decision making.

[A; HIGH] **Functional correctness** asks whether the result satisfies the goal. For example, creating the intended post in the intended forum can be successful even if the agent used a different valid route from an annotator. **Chain-of-thought (CoT) prompting** in this experiment asks the model to write step-by-step reasoning before selecting an action. **Few-shot in-context learning** supplies two worked examples in the prompt; the paper does not describe fine-tuning the baseline models on WebArena.

[A; HIGH] A **content management system (CMS)** manages digital content; WebArena uses a store administration portal. Docker images package website code, databases, and dependencies. A gym-style application programming interface (API) exposes the environment for agents. These are implementation descriptions, not evidence of a security boundary or isolation guarantee.

# 4. Research problem and gap

[A; HIGH] The existing problem is evaluating agents on tasks people actually care about while preserving a fair, repeatable environment. The authors identify three shortcomings: reduced website functionality limits task diversity; simplified environments reduce task complexity; and static cached states limit exploration. They also criticize grading by surface similarity of action sequences because it can reject alternative valid solutions or overlook unsuccessful execution (pp. 1–2).

[A; HIGH] The research gap is a benchmark combining realistic working websites, dynamic interaction, diverse human tasks, reproducibility, and outcome-based grading. Live websites introduce changing content and configurations and technical obstacles such as CAPTCHAs. Self-hosted websites address repeatability while imported data and existing open-source implementations support realism (pp. 2–3).

[A; HIGH] The scope is a selected set of website categories, sampled organic content, specific user profiles, and curated high-level tasks. It does not encompass every website, user population, open-web condition, or security scenario. The map is limited to the northeastern United States, and offline Wikipedia has a May 2023 knowledge cutoff (p. 15).

[D; MEDIUM] In a security-oriented literature review, this closes part of the experimental-platform gap: it offers concrete stateful interactions that could be adapted to study harmful outcomes. It does not itself close the comparative-security evidence gap posed by 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?'

# 5. Research questions / objectives / hypotheses

[A; HIGH] The paper does not present a numbered list of formal research questions or a preregistered hypothesis-testing plan. Its explicit objectives are to create a realistic and reproducible web environment, curate high-level tasks, evaluate functional correctness, and measure language-model agent performance.

[A; HIGH] Section 5.1 explicitly frames two analysis questions: whether models know when to stop, and whether a model maintains consistent performance across similar tasks. These are examined through the unachievable-hint ablation and template-level success distribution, respectively.

[A; MEDIUM] The authors hypothesize that limited performance reflects missing capabilities such as active exploration and failure recovery (p. 2). Appendix A.10 further hypothesizes that dialogue-oriented pretraining and supervised fine-tuning contribute to observation failures and insufficient exploration (p. 22). These explanations are hypotheses supported by qualitative observations, not controlled causal tests of training procedures.

[D; HIGH] The user's security question is separate from the paper's objectives. This report therefore uses WebArena to identify candidate mechanisms and experimental requirements, not to manufacture an author hypothesis that web agents are more vulnerable than standalone LLMs.

# 6. Assumptions / threat model

[A; HIGH] The environment is modeled as deterministic: its transition function maps the current state and action to the next state according to website implementation. Deterministic environment transitions do not imply deterministic language-model output; the main inference temperature is 1.0 (pp. 3, 17).

[A; HIGH] Agents are given a task, current browser information, and previous-action information. The formal description allows action and observation histories, whereas the baseline description and printed prompt explicitly emphasize the current observation and previous action. The supplied material does not establish that the baselines receive the full histories contemplated by the general formalism (pp. 3, 7–8, 18).

[A; HIGH] Users have platform-specific roles and histories. Cached cookies automatically log them in. The CMS profile is a shop owner with full read-and-write access to all system content; the shopping profile has over 35 orders over two years; the GitLab profile maintains public projects and some private projects (p. 16). These are benchmark account conditions, not attacker capabilities.

[D; HIGH] No explicit adversarial threat model is provided. The paper does not define attacker control of pages, injected instructions, malicious accounts, credential theft, exfiltration, defense policies, or attack success. Its system messages mention a homepage containing account names and passwords, but no experiment demonstrates that an attacker can reach or misuse those credentials. Security-relevant assets and interfaces can be inferred from the system; their exploitability remains UNKNOWN.

# 7. Methodology

## Environment selection and implementation

[A; HIGH] The authors examined approximately 200 examples from their browser histories, summarized session goals, grouped sites into categories, and selected four salient categories. This is author-centered convenience sampling, not a population-representative survey of internet activity (p. 3).

[A; HIGH] Appendix A.1 reports approximately 90,000 shopping products across over 300 categories, including prices, options, descriptions, images, and reviews. Adobe Magento supplies the shopping platform. The forum uses Postmill and contains 95 subreddits, 127390 posts, and 661781 users. Selection includes sampling from the top 50 subreddits and manually adding northeastern-city and machine-learning topics to encourage cross-site tasks (p. 15).

[A; HIGH] GitLab contains 300 repositories and more than 1000 accounts with at least one commit. The sampling description selects at least ten repositories per programming language; 80% come from a top-90-percentile set with star-proportional weighting, and the remainder from a bottom-ten-percentile set with similar weighting. The exact percentile convention is not fully clarified, so those phrases are retained rather than reinterpreted. The CMS uses Magento's admin portal and official sample data. OpenStreetMap supplies the regional map; the authors implement the calculator and scratchpad. Kiwix hosts offline English Wikipedia, and manuals are scraped from official sites (p. 15).

## Packaging and resetting

[A; HIGH] Each website has a separate self-contained Docker image including code, database, dependencies, and data, without required external volume mounts. Resetting entails restarting from the original image after stopping and deleting the current container. The reported reset interval is a few seconds to one minute, depending on the site. Read-only tasks may not require a reset. The authors characterize the resulting evaluation-time impact as non-negligible but small when combined with model inference time; no measured overhead distribution is supplied (pp. 15–16).

## Observation and action interfaces

[A; HIGH] Observations include the current URL, open tabs, and focused-tab page content. Content can be raw HTML, screenshot, or accessibility tree. Viewport limiting is optional. Elements can be selected through screen coordinates or IDs assigned while traversing the DOM or accessibility tree. The authors describe ID selection as an n-way classification problem, avoiding element disambiguation (p. 4).

[A; HIGH] Actions include clicking, hovering, typing, key combinations, scrolling, opening/closing/focusing tabs, navigating to a URL, and browser-history movement. Figure 4 also lists a no-operation action. Printed agent prompts add a completion action, stop with an answer. Action naming differs slightly between Figure 4 and prompts: tab_close versus close_tab. The analysis preserves the distinction rather than assuming which exact parser implementation was used (pp. 5, 18, 20).

## Task collection and annotation

[A; HIGH] Annotators explored the sites, then created abstract tasks requiring more than one or two actions, added creative constraints, and expressed tasks as templates with variable instantiations. ChatGPT was offered as an inspiration aid, alongside curated examples; the paper does not state that all tasks were automatically generated. The resulting collection has 241 templates and 812 instantiated intents, with a reported average of 3.3 examples per template (p. 5).

[A; HIGH] Tasks fall into information seeking, site navigation, and content/configuration operations. Information tasks often involve user-specific data and multiple pages. Content/configuration tasks include transactions, account management, settings, posts, and repository files. Unachievable tasks arise from absent evidence, permissions, or unsupported website functions, and expect an N/A-equivalent answer (pp. 6–7).

[A; HIGH] Authors contribute intents. Information answers are annotated twice by authors and an external annotator, with a third adjudicator resolving disagreement. Three JavaScript-proficient authors build the remaining evaluators. Difficult cases are discussed collectively, and annotators execute tasks and inspect intermediate states (p. 7). No inter-annotator agreement statistic or detailed disagreement count is reported.

## Evaluation and configuration

[A; HIGH] Answer grading uses exact_match, must_include, or GPT-4-based fuzzy_match. State grading retrieves relevant content through database queries, website APIs, or JavaScript and applies conditions to URLs or content. Fuzzy-match predictions receive one only if judged correct; incorrect and partially correct receive zero (pp. 6–7, 17).

[A; HIGH] Baselines are GPT-3.5-TURBO-16K-0613, GPT-4-0613, and TEXT-BISON-001, with temperature 1.0 and top-p 0.9. The maximum number of state transitions is 30. Execution halts after the same action is repeated more than three times on the same observation or after three consecutive invalid actions. TEXT-BISON-001 receives ten retries to produce a valid action. Random seeds, model-run repetitions, confidence intervals, detailed hardware specifications, and task-specific token costs are not reported (p. 17).

[A; HIGH] This is inference-time benchmark evaluation. No training/validation/test split beyond the described benchmark test examples is provided, and no WebArena fine-tuning procedure or leakage audit is supplied. Public artifact availability is stated but not independently checked.

# 8. Experiments / analyses

| ID | Purpose and conditions | Result and qualification |
|---|---|---|
| X1: model/prompt baseline comparison | Three LLMs; direct versus reasoning prompts where reported; two in-context examples; accessibility-tree observations; main temperature 1.0. | Table 2 shows low overall success. With UA hint and CoT, TEXT-BISON-001 scores 5.05%, GPT-3.5 8.75%, and GPT-4 11.70%. Direct GPT-3.5 with hint scores 6.41%. This is not a complete factorial experiment across all models. |
| X2: UA-hint ablation | Remove the explicit sentence instructing N/A for impossible tasks; separate achievable and unachievable outcomes. | GPT-4 CoT overall success rises to 14.41%; achievable success rises from 8.63% to 13.02%; unachievable success falls from 77.78% to 44.44%. GPT-3.5 does not exhibit the same overall improvement. |
| X3: template consistency | No-UA-hint GPT models; histogram conditioned on templates with at least one successful execution. | Of the described 61 templates, GPT-4 fully solves only four; GPT-3.5 fully solves none. Exact bar counts are not recoverable from the small visual. Selection excludes wholly unsuccessful templates. |
| X4: human benchmark | One task from each of 170 templates; five computer-science graduate students. | Overall 78.24%, information seeking 74.68%, other tasks 81.32%, average time 110 seconds. Sampling differs from the 812-task model benchmark, and allocation across participants is insufficiently detailed. |
| X5: lower-temperature check | GPT-3.5-TURBO-16K-0613, CoT, no UA hint, temperature 0.0. | Table 5 reports 6.28% overall success, versus 6.16% for the corresponding main-temperature row. No repeated-run uncertainty is supplied. |
| X6: fuzzy evaluator validation | Manual comparison on 40 examples; separate generated-format tests for dates and durations. | 39/40 agree with human judgment. Two GPT-4 versions score 100% on 900 date and 900 duration examples. This validates bounded evaluator tasks, not every possible semantic-answer judgment. |
| X7: qualitative failure analysis | Recorded GPT-4 trajectories and screenshots. | Observation bias, failure to switch to Users, repeated filled search queries, and neglect of previous actions are illustrated. Only the early-stopping analysis supplies a broad numerical error rate; other categories lack prevalence estimates. |

[A; HIGH] The main dependent variable is end-to-end success, with subgroup success for achievable and unachievable tasks. Manipulated conditions include model, prompting strategy, UA hint, and the one temperature check. No statistical tests or uncertainty intervals accompany these comparisons. The paper's language about significantly lower performance should not be read as a supplied statistical-significance test.

# 9. Results

[A/B; HIGH] Table 2 contains the following exact percentages. SR is overall success; SR_AC is success on achievable tasks; SR_UA is success on unachievable tasks.

| CoT | UA hint | Model | SR (%) | SR_AC (%) | SR_UA (%) |
|---|---|---|---:|---:|---:|
| Yes | Yes | TEXT-BISON-001 | 5.05 | 4.00 | 27.78 |
| No | Yes | GPT-3.5 | 6.41 | 4.90 | 38.89 |
| Yes | Yes | GPT-3.5 | 8.75 | 6.44 | 58.33 |
| Yes | Yes | GPT-4 | 11.70 | 8.63 | 77.78 |
| No | No | GPT-3.5 | 5.10 | 4.90 | 8.33 |
| Yes | No | GPT-3.5 | 6.16 | 6.06 | 8.33 |
| Yes | No | GPT-4 | 14.41 | 13.02 | 44.44 |
| Not applicable | Yes | Human | 78.24 | 77.30 | 100.00 |

[C; HIGH] With the UA hint, GPT-3.5 reasoning improves overall success by **2.34 percentage points**, calculated as 8.75 − 6.41. The prose calls this a '2.34% improvement'; the operands show an absolute percentage-point difference, not a 2.34% relative increase. The relative increase would be approximately 36.51%, calculated as 2.34 / 6.41 × 100, but that derived quantity is not the author's reported measure.

[C; HIGH] Removing the UA hint for GPT-4 CoT changes overall success by **+2.71 percentage points** (14.41 − 11.70), achievable success by **+4.39 points** (13.02 − 8.63), and unachievable success by **−33.34 points** (44.44 − 77.78). This is a tradeoff between completing feasible tasks and recognizing infeasible ones, not a uniform improvement on every metric.

[C; HIGH] For GPT-3.5 CoT, removing the hint reduces overall success by **2.59 percentage points** (6.16 − 8.75), achievable success by **0.38 points** (6.06 − 6.44), and unachievable success by **50.00 points** (8.33 − 58.33). Thus a general statement that removing the hint improves all agents would contradict Table 2.

[A; HIGH] The authors report that GPT-4 incorrectly treats 54.9% of feasible tasks as impossible in their stopping analysis. The text associates this with the UA-hint setting, but does not provide the underlying error count, denominator, or a dedicated table of classifications (p. 8).

[C; HIGH] The reported human–best-agent difference is **63.83 percentage points**: 78.24 − 14.41. This subtraction is descriptive only because the human and model evaluations use different task sampling. It does not estimate a matched experimental effect or a security-risk difference.

[A; HIGH] Human failure analysis attributes 50% of failures jointly to intent misinterpretation, incomplete answers, and incomplete execution; the remaining failures are described as more severe, off-target execution. The paper does not assign individual percentages to those three categories (p. 7).

# 10. Figure-by-figure interpretation

## Figure 1 — Environment, interaction loop, and outcome validation

[B; HIGH] On p. 2, a rounded environment box contains application icons above tool and knowledge-resource icons. An AI-agent icon sits to the right. An Action arrow points from agent toward environment; a Feedback arrow returns toward the agent. Two natural-language task bubbles illustrate spending analysis and creating a film repository. A validator illustration leads to green functional-success and red functional-failure outcomes.

[A/B; HIGH] This is an architecture overview rather than a plot: there are no numerical axes, units, error bars, or measured effect sizes. The meaningful encoding is components, arrows, and binary outcome symbols. It supports the claim that agents act within a website environment and are evaluated by functional outcomes. The icons are illustrative and do not establish measured use of every tool.

## Figure 2 — A cross-website itinerary task

[B; HIGH] On p. 3, three panels show Wikipedia museum information, a map, and a GitLab repository document. The task asks for a minimal-driving-distance route through Pittsburgh art museums starting at Schenley Park and saving the visit order to a named repository. Beneath the panels, labels show searching for museums, searching each museum on the map, and recording results.

[A; HIGH] The caption makes the stages explicit: discover museums, identify locations while optimizing the route, and update the appropriate README. This shows retrieval, planning, and a persistent write combined in one task. It is not evidence that a baseline solved the task optimally. No route length, optimality certificate, solver algorithm, or quantitative routing result is supplied.

## Figure 3 — Three representations of one webpage

[B; HIGH] On p. 4, the left panel is a shopping screenshot, the middle is HTML structure, and the right is an accessibility tree. The tree includes role labels, text such as Rating and 12 Reviews, a price of $49.99, and button properties. An 82% rating is visible in the text representations.

[A; HIGH] The caption says the middle and right panels are trimmed to save space. These values are illustrative webpage content, not experimental results. The figure supports configurable observation representations, but the baseline experiments use the accessibility tree. Tiny screenshot details are not used to reconstruct a full product record.

## Figure 4 — Action-space catalog

[B; HIGH] On p. 5, a two-column tabular figure groups no-operation/page actions, tab actions, and URL navigation actions. It lists noop, click, hover, type, press, scroll, tab_focus, new_tab, tab_close, go_back, go_forward, and goto. Horizontal rules separate groups. There are no plot axes or statistical markers.

[A/B; HIGH] It shows the browser operations the environment exposes. Completion through stop appears in the agent prompt rather than this figure. Naming variation with close_tab in Figures 7 and 9 is recorded as an interface-documentation ambiguity.

## Figure 5 — Intent categories and examples

[B; HIGH] On p. 5, a tabular figure lists information seeking, site navigation, and content/configuration. Examples include purchase-history lookup, comparing walking and driving time, assigned merge requests, finding a best-rated chair, posting about needing a car in New York City, and deleting a user's reviews.

[A; HIGH] It establishes task diversity and the distinction between answering, locating, and modifying. It gives examples rather than category frequencies. No inference about the percentage of destructive tasks follows from these examples.

## Figure 6 — Website distribution

[B; HIGH] On p. 16, a pie chart has six labeled slices: E-commerce 23.0%, CMS 22.4%, GitLab 22.2%, Map 13.4%, Reddit 13.1%, and Cross Site 5.9%. Colors distinguish slices; labels and percentages provide exact readable values. There are no axes, confidence intervals, or sampling-error bars.

[A; HIGH] The caption says cross-site intents require multiple websites and all intents require multiple webpages. Cross-site therefore differs from multi-page. [C; HIGH] The labels sum to 100.0%: 23.0 + 22.4 + 22.2 + 13.4 + 13.1 + 5.9. Rounded percentages cannot establish exact category counts out of 812.

## Figure 7 — Reasoning-agent system message

[B; HIGH] On p. 18, a boxed prompt supplies the user objective, accessibility tree, URL, open tabs, and previous action. It enumerates page, tab, navigation, and stop actions, describes default Enter behavior after typing, points to the benchmark homepage and credential listing, and instructs the experimental agent to issue one valid action at a time with reasoning and a formatted action.

[A; HIGH] The UA-hint sentence tells the experimental agent to answer N/A if it believes completion is impossible. The text below the box says this sentence is removed in ablations. These are author-provided prompt contents, not instructions followed by this report. The figure specifies a prompt condition, not a security policy or tested defense.

## Figure 8 — Reasoning-agent examples

[B; HIGH] On p. 19, two worked examples show answering an observed fax-machine price of $279.49 and entering a map search for restaurants near a placeholder location ABC. The first reasons that the task is complete before stop; the second reasons about the search field before typing with Enter enabled.

[A; HIGH] These are the two few-shot examples, not measured benchmark successes. Element IDs, prices, and URLs are prompt-example values. The simplicity of the examples contrasts with the benchmark's multi-step tasks, but the paper does not experimentally isolate example complexity.

## Figure 9 — Direct-agent system message

[B; HIGH] On p. 20, the boxed prompt largely duplicates the reasoning prompt's environment information and action descriptions. It requires formatted actions without the reasoning example rule. The success-rules introductory line appears twice, a visible textual repetition.

[A/B; HIGH] The figure supports the direct-versus-reasoning comparison. Its repeated line is compressed as non-substantive prompt repetition, not treated as an independently tested variable. Like Figure 7, it includes the UA-hint condition before ablation.

## Figure 10 — Direct-agent examples

[B; HIGH] On p. 21, the same price and restaurant-search observations appear, but assistant examples output only stop with $279.49 or the type action. This controls the example task content while changing the demonstrated reasoning behavior. It does not prove every other inference-level behavior is controlled.

## Figure 11 — Two GPT-4 failures

[B; HIGH] On p. 22, the left screenshot shows a GitLab search for Facebook with Projects 0 and Users 1; its accessibility excerpt highlights those options. The right screenshot shows a forum search whose field contains DMV area, accompanied by a searchbox ID and StaticText identifying the entered text. The gray excerpts tie visible page state to the agent's textual observation.

[A; HIGH] The caption explains that the left agent fails to proceed to Users for the repository-forking task, while the right repeats an already-entered query. These illustrate exploration and state-interpretation failures. They do not show malicious page instructions, attacker intervention, or attack success. Exact prevalence cannot be inferred from two examples.

# 11. Table-by-table interpretation

## Table 1 — Answer and state validators

[A/B; HIGH] On p. 7, rows 1–3 compare predicted answers against references. Exact match expects Samantha Jones for a cancellation-history query. Must-include checks require both Sean Miller and sean@gmail.com for a phone-number query. Fuzzy match checks walking 2h58min and driving 21min. These are reference-answer examples, not model accuracy numbers.

[A/B; HIGH] Rows 4–5 evaluate website state: an assigned-merge-request URL and a new post whose URL contains /f/nyc and body contains a car in NYC. The table shows how different task types can share outcome-focused evaluation. It does not document every evaluator's complete implementation. Notational argument order differs between its displayed r_info label and nearby prose; the roles of predicted and reference answers remain clear from the implementations.

## Table 2 — Baselines and UA-hint ablation

[A/B; HIGH] On p. 8, rows distinguish model, reasoning, and UA hint; columns distinguish overall, achievable, and unachievable success, all in percent. Exact values are reproduced in section 9. Best machine overall and achievable values are GPT-4 CoT without hint, 14.41% and 13.02%; best machine unachievable value is GPT-4 CoT with hint, 77.78%. Humans score highest in all three columns, with the sampling caveat already noted.

[A/B; HIGH] There are no uncertainty intervals, significance symbols, standard deviations, or repeated-run counts. A dash in the human CoT column indicates inapplicability rather than a missing numeric measurement. No direct GPT-4 or no-hint TEXT-BISON row is present, so missing configurations cannot be inferred.

## Table 3 — Histogram of template-level success

[B; MEDIUM] This object on p. 8 is labeled Table 3 but drawn as grouped bars. The x-axis is labeled Success rate (%) within a template, yet its ticks run from 0.1 to 1.0; these appear to encode proportions corresponding to 10%–100%. That apparent axis-unit mismatch is flagged, not silently repaired. The y-axis is number of templates, with ticks from 0 to 25. The legend distinguishes GPT-3.5 direct, GPT-3.5 CoT, and GPT-4 CoT in green, orange, and blue-toned bars.

[A; HIGH] The caption restricts the distribution to templates with at least one successful execution for GPT models without the UA hint. The prose says GPT-4 achieves complete success on four of 61 templates and GPT-3.5 on none. Most visible mass is at low success values, especially for GPT-4 around the 0.2 tick, but exact bar heights are UNCERTAIN. No error bars are shown, and the conditional selection must be preserved.

## Table 4 — Benchmark feature comparison

[A/B; HIGH] On p. 9, columns are dynamic interaction, realistic environment, diverse human tasks, and functional correctness. The authors mark Mind2Web and Form/QAWoB as no/yes/yes/no; MiniWoB++, Webshop, and ALFRED as yes/no/no/yes; VirtualHome as no/no/yes/no; AndroidEnv as yes/yes/no/no; and WebArena as yes/yes/yes/yes.

[A; HIGH] This is the authors' qualitative taxonomy, encoded with checkmarks and crosses. It is not a quantitative performance comparison or an independently validated survey. Reproducibility is discussed nearby but is not one of these four columns. No table entry evaluates security resilience.

## Table 5 — Temperature-zero result

[A/B; HIGH] On p. 17, a single row reports GPT-3.5-TURBO-16K-0613 with CoT, no UA hint, temperature 0.0, and 6.28% success. It is a reproducibility-oriented supplemental condition. [C; HIGH] Its difference from the 6.16% main-temperature row is +0.12 percentage points. Without repeated-run uncertainty, that small difference does not establish a robust temperature advantage.

## Table 6 — Date and duration equivalence grading

[A/B; HIGH] On p. 17, GPT-4-0613 and GPT-4-1106-preview each score 100% accuracy on a 900-example date dataset and a 900-example time-duration dataset. These are evaluator-validation results on generated format-equivalence tasks. They are not web-agent task-success rates and do not imply perfect grading for all 82 fuzzy-match benchmark cases. Class balance and detailed generation settings are not supplied.

# 12. Diagram / architecture interpretation

[A/B; HIGH] The system's control loop is: receive a high-level intent; observe URL, open tabs, and focused-page content; choose a browser action; execute it in a website; receive the resulting observation; and continue until completion or a termination rule. Figure 1 depicts action and feedback arrows; §2.1 defines the state transition. The validators assess task outcomes from answers or recorded states rather than instructing the agent along a reference route.

[A/B; HIGH] Figure 2 illustrates a data path across components: Wikipedia supplies candidate museums, the map supplies locations and routing information, and GitLab stores the resulting itinerary. Figure 3 shows alternative ways to encode the observed page before model decision making. The content of a webpage is therefore part of the agent's decision input, and some actions update website data.

[D; MEDIUM] For security research, this architecture suggests a candidate path from observed content to selected actions to persistent consequences. Whether an attacker can control the content, whether the model treats it as authoritative, and whether harmful actions occur are separate questions requiring experiments absent here. The action-feedback loop is directly supported; an adversarial exploitation chain is only a proposed analytical application.

# 13. Equations and mathematical concepts

## E1: Environment tuple

[A; HIGH] On p. 3, the environment is E = ⟨S, A, O, T⟩. S is the state space, A the action space, O the observation space, and T the transition function. This is a system specification, not an optimization objective. An observation is information exposed to the agent; a state includes environment conditions that may be assessed by evaluators. The paper does not provide an exhaustive mathematical enumeration of all states.

## E2: Deterministic transition

[A; HIGH] T: S × A → S maps a state-action pair to a new state. Given intent i, observation o_t, action history a_1 through a_(t−1), and observation history o_1 through o_(t−1), an agent chooses a_t ∈ A. Its action produces s_(t+1) ∈ S and corresponding o_(t+1) ∈ O. The Cartesian product S × A means a pair containing one state and one action.

[A; HIGH] The transition function is determined by website implementation. The mapping from state to observation is described operationally but not given a separate formal function. No Markov-property proof or stochastic-transition analysis is presented.

## E3: Trajectory reward

[A; HIGH] The paper writes r(a_1^T, s_1^T) for task success, where a_1^T denotes actions from the start to terminal time T and s_1^T denotes intermediate states. Here T is also used as the transition-function symbol, creating an overloading that is resolved by context. The reward asks whether the executed trajectory satisfies the intent, such as actually placing an order or giving the correct answer. There is no supplied discounted-return equation, learned reward model, or reinforcement-learning training loss.

## E4: Information reward

[A; HIGH] r_info(â, a*) compares predicted answer â with annotated reference a*. Exact matching rewards identity; must-include rewards presence of required content; fuzzy matching uses a language-model judgment of semantic equivalence. Correct fuzzy judgments receive 1; all other judgments receive 0. The paper does not specify one universal normalization or string-preprocessing routine for every exact match.

## E5: Programmatic state reward

[A; HIGH] r_prog(s) checks relevant states for intended properties. A locator retrieves a URL, database value, or webpage content, and conditions determine whether the task was accomplished. Table 1 illustrates multiple required checks, but the supplied text does not give a general mathematical aggregation rule for every multi-condition task.

[D; HIGH] These equations formalize functional task evaluation. They do not define a threat model, malicious-instruction probability, security loss, or comparative vulnerability metric. No numbered theorem, lemma, proposition, proof, or standalone algorithm/pseudocode block appears in the supplied document.

# 14. Interpretation and discussion

[A; HIGH] The main empirical message is that these baseline agents struggle with realistic multi-step web tasks despite using capable language models. Reasoning helps GPT-3.5 within the reported hint conditions, but does not eliminate failures. The stop-hint experiment answers the first §5.1 question by revealing a configuration-dependent tradeoff: explicit awareness of impossible tasks can improve recognition while encouraging premature abandonment of feasible tasks.

[A; HIGH] The template analysis answers the second question by showing that shared high-level semantics do not guarantee robust execution across variations. Forking one repository can be easier than forking all repositories from an organization because repetition and navigation demands change. This supports evaluating varied instantiations rather than assuming one successful example demonstrates a reusable skill.

[A; MEDIUM] The authors' exploration and recovery explanation is compatible with the examples, but is not causally isolated. Likewise, the training-based explanation in A.10 remains speculative because the study does not compare controlled training regimes.

## Consistency and cross-reference findings

[A; HIGH] The task collection reports 241 templates on p. 5, while human evaluation samples from 170 templates on p. 7. These may describe different eligible subsets, but the supplied material does not explain the transition. Both values are retained; the human comparison is not represented as covering all 241 templates.

[A/B; MEDIUM] Table 3's caption conditions on templates with successful executions, and the text refers to 61 templates. The exact relationship between that set and each model's eligible templates is not fully specified. Its proportion-like ticks conflict with the percentage wording on the axis.

[A; MEDIUM] Appendix A.6 says repetition of the same action more than three times on an unchanged observation terminates execution. Appendix A.10 describes repeating the same search query until the maximum step limit. Changing observations, parser details, or a simplified description might reconcile them, but the supplied evidence does not establish which explanation applies.

[A; HIGH] Table 1 reverses the displayed argument order of r_info relative to nearby prose; its example functions still identify predicted and reference answers. Figure 4 and agent prompts differ in the tab-closing action name. These are documentation ambiguities, not evidence that the evaluated implementation failed to parse actions.

[A; HIGH] Main conclusions correctly identify 14.41% as the best reported GPT-4 condition, while the initial main-results discussion emphasizes the 11.70% hint condition. They are different experimental configurations, not contradictory measurements.

# 15. Contributions and novelty

[A; HIGH] The **system contribution** is a self-hostable collection of operational websites, tools, and knowledge resources with reproducible initialization. The **benchmark/dataset contribution** is 812 high-level intents from 241 templates with annotated outcomes. The **evaluation contribution** is answer and state validation that accommodates alternative valid execution paths. The **empirical contribution** is baseline performance and analysis of stopping, template variation, and observation errors.

[A; HIGH] The authors additionally claim novelty for multi-tab web tasks and role-specific, automatically logged-in users. These priority claims are reported as author claims; this closed-document analysis does not verify them against all previous work.

[D; HIGH] There is no new model-training algorithm, theorem, adversarial attack, security defense, or standalone-LLM comparison demonstrated in this paper. For the user's project, the novel value is a platform and behavioral evidence that can inform a later security study.

# 16. Limitations

## Authors' stated limitations

[A; HIGH] Baseline success is low, and agents lack robustness on realistic tasks (pp. 1–2, 8–9). The authors identify incorrect stopping, observation bias, missed granular page information, repeated actions, and neglected previous actions (pp. 8, 22). These are limitations of evaluated agents, not necessarily limitations of every possible WebArena agent.

[A; HIGH] Human performance can change with demographics and expertise; many tasks require domain-specific knowledge, such as merge requests or complex store administration. The authors target easy-to-imagine outcomes rather than tasks every average user can readily execute (p. 16).

[A; HIGH] Map coverage is geographically limited by storage constraints (p. 15). Websites use sampled data and attempt to reproduce familiar functionality rather than claiming an exhaustive replica of the entire open web. Resetting adds non-negligible evaluation time (pp. 15–16).

## Additional evidence-based analyst observations

[D; MEDIUM] Author-generated intents and author browser-history selection may shape which tasks and website practices dominate. Five computer-science graduate students are a narrow human comparison group. The 170-versus-241-template distinction is unresolved.

[D; HIGH] A 30-transition budget and early termination rules limit what counts as successful execution. Different model retry allowances complicate strict resource-matched comparison. Missing repeated-run statistics and confidence intervals constrain judgments about small numerical differences.

[D; MEDIUM] Keyword and URL checks establish specified properties but may not capture every unintended side effect. The paper does not show that all validators assess broader safety or every semantic constraint. This is a limitation of what can be concluded from the presented examples, not a demonstrated universal evaluator defect.

[D; HIGH] No malicious-content experiment or standalone-model baseline is present. Functional failure is not an attack-success measure. Security-vulnerability conclusions remain unsupported by this study alone.

# 17. Threats to validity

The following validity labels are analyst framing, not terminology attributed to the authors.

[D; MEDIUM] **Internal validity:** prompt changes have interpretable within-model comparisons, but sampling randomness at temperature 1.0 lacks reported repeated-run uncertainty. Qualitative errors do not isolate whether reasoning, memory, observation representation, prompt content, or model training caused failures. Model-specific retries introduce an additional procedural difference.

[D; MEDIUM] **Construct validity:** functional success is well aligned with accomplishing requested tasks, but it is not equivalent to safe behavior, least-privilege operation, resistance to malicious instructions, or absence of side effects. The impossible-task metric combines accurate recognition of infeasibility with willingness to stop, which can conflict with success on feasible tasks.

[D; MEDIUM] **External and ecological validity:** operational sites and organic data improve resemblance to ordinary web activity, but sampled content, selected user roles, regional maps, frozen resources, and author-designed tasks limit transfer. Avoiding live-site changes improves controlled comparisons while excluding some real deployment conditions.

[D; MEDIUM] **Statistical conclusion validity:** point estimates support descriptive differences, especially the large reported performance gap, but no confidence intervals, repeated-run variability, or formal significance tests are supplied. The human comparison's task sampling prevents interpreting its difference as a matched causal effect.

[D; MEDIUM] **Reproducibility:** fixed website images, reset scripts, model identifiers, prompts, and configurations provide useful specifications. The referenced artifacts were not reviewed here; random seeds, complete infrastructure specifications, and API execution details are not visible. Reproducible environment state should be distinguished from reproducible model sampling.

[D; HIGH] **Security generalizability:** no evidence establishes how an adversary's control, account privileges, or injected content would change outcomes. A comparative security study must supply these conditions rather than treat this benchmark's reliability results as their substitute.

# 18. Future work and open questions

## A. Explicit author proposals

[A; HIGH] The authors call for more robust and effective agents, improved exploration and failure recovery, and further testing of planning, backtracking, self-correction, and observation summarization. Section 5.1 highlights methods with memory components that reuse successful strategies. The paper presents WebArena as a testbed for these improvements rather than reporting that they were implemented and validated here (pp. 2, 8–9).

## B. Additional analyst open questions

[D; MEDIUM] For security analysis, the immediate questions are which observed content an adversary can control, which actions the agent can perform under each account, what unauthorized outcome defines attack success, and whether validators can distinguish goal completion from harmful side effects. The printed credentials page and automatic login identify concrete experimental conditions worth examining; they do not establish a vulnerability on their own.

[D; HIGH] To answer the user's comparison, a future study would need matched web-agent and standalone-LLM conditions, a specified attacker, comparable malicious inputs, and outcome measures separating mistaken text from consequential actions. This paper supplies none of those comparative results. Other open questions include robustness over seeds, different examples, task budgets, broader users, and adversarial versus ordinary observation variation.

# 19. Terminology and notation glossary

| Term or symbol | Beginner-friendly meaning in this paper |
|---|---|
| WebArena | The self-hosted website environment and associated task benchmark. |
| ICLR | International Conference on Learning Representations; the stated 2024 venue. |
| LLM | Large language model used to interpret observations and select actions. |
| Agent | A system that repeatedly observes and acts toward a goal. |
| Intent i | A natural-language request specifying the desired result. |
| Grounding | Converting a request into concrete website interactions. |
| Template | A task pattern containing replaceable variables. |
| Instantiated intent | A concrete task formed by filling a template's variables. |
| Long horizon | A task requiring multiple sequential decisions; no universal numeric definition is supplied. |
| DOM | Document Object Model, the structured representation of a webpage. |
| HTML | HyperText Markup Language, used for webpage structure. |
| Accessibility tree | A compact tree of relevant page elements, roles, text, and properties. |
| Viewport | The currently visible region of the browser page. |
| Element ID | An identifier assigned to a page element for action selection. |
| CMS | Content management system; here, a store administration environment. |
| API | Application programming interface, used for environment interaction or evaluation access. |
| CoT | Chain-of-thought prompting: reasoning text before an action. |
| UA hint | Unachievable hint: explicit guidance to stop with N/A on impossible tasks. |
| SR | Overall end-to-end task success rate, expressed in percent. |
| SR_AC | Success rate on achievable tasks. |
| SR_UA | Success rate on unachievable tasks. |
| N/A | The benchmark's special response meaning not achievable. |
| exact_match | A validator requiring the predicted answer to equal the reference. |
| must_include | A validator requiring specified text to be present. |
| fuzzy_match | A language-model judgment of semantic equivalence to a reference. |
| Locator | Code that retrieves task-relevant state or content for a validator. |
| E | The environment tuple. |
| S, s_t | State space and a state at time t. |
| A, a_t | Action space and an action at time t. |
| O, o_t | Observation space and an observation at time t. |
| T | Transition function, or terminal time when used in a trajectory superscript. |
| a_1^T, s_1^T | Action and state sequences from the beginning to terminal time. |
| a*, â | Annotated reference answer and predicted answer. |
| r, r_info, r_prog | Overall trajectory reward, answer evaluator, and state evaluator. |
| Docker image | A packaged website, database, data, and software dependencies. |
| README | The repository document used in example writing tasks. |
| POI | Point of interest, such as a museum or other mapped location. |
| Top-p | An inference-sampling parameter reported as 0.9; its mechanism is not defined in the paper. |
| Temperature | An inference-sampling setting; the authors use 1.0 to encourage exploration. |

# 20. Key numerical results

Values below are exact author reports or clearly readable labels unless identified as derived. Approximate source quantities retain their qualifiers. Example prices, IDs, and reference-answer times are accounted for in the visual and table interpretations rather than confused with experimental metrics.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Website-selection examples | Approximately 200 | browser-history examples | Authors' history analysis | Author-reported | p. 3, §2.2 |
| Core website categories | 4 | categories | Shopping, forum, development, CMS | Author-reported | pp. 1–3 |
| Utility tools | 3 | tools | Map, calculator, scratchpad | Author-reported | p. 3 |
| Benchmark tasks | 812 | instantiated intents | Full curated benchmark | Author-reported | pp. 2, 5 |
| Task templates | 241 | templates | Intent collection | Author-reported | p. 5 |
| Mean instantiations | 3.3 | examples/template | Reported mean | Author-reported | p. 5 |
| Human sample template count | 170 | templates | One task from each | Author-reported | p. 7 |
| Human participants | 5 | people | Computer-science graduate students | Author-reported | p. 7 |
| Human average time | 110 | seconds | Reported human task performance | Visually readable | p. 7 |
| Human information success | 74.68 | % | Information-seeking tasks | Visually readable | p. 7 |
| Human other-task success | 81.32 | % | Other task categories | Visually readable | p. 7 |
| Human overall success | 78.24 | % | Sampled human evaluation | Author-reported | pp. 7–8 |
| Human achievable success | 77.30 | % | Table 2 subgroup | Visually readable | p. 8, T2 |
| Human unachievable success | 100.00 | % | Table 2 subgroup | Visually readable | p. 8, T2 |
| Human failures in grouped partial/misread categories | 50 | % of failures | Joint category, not each separately | Author-reported | p. 7 |
| GPT-4 best overall success | 14.41 | % | CoT, no UA hint, main settings | Author-reported | p. 8, T2 |
| GPT-4 hinted overall success | 11.70 | % | CoT, UA hint | Author-reported | p. 8, T2 |
| GPT-4 feasible tasks labeled impossible | 54.9 | % of feasible tasks | Stopping analysis associated with hint | Author-reported | p. 8, §5.1 |
| GPT-3.5 hinted CoT success | 8.75 | % | CoT, UA hint | Author-reported | p. 8, T2 |
| GPT-3.5 hinted direct success | 6.41 | % | Direct, UA hint | Visually readable | p. 8, T2 |
| TEXT-BISON overall success | 5.05 | % | CoT, UA hint | Author-reported | p. 8, T2 |
| GPT-3.5 temperature-zero success | 6.28 | % | CoT, no hint, temperature 0.0 | Author-reported | p. 17, T5 |
| Main temperature / top-p | 1.0 / 0.9 | inference settings | All main baseline models | Author-reported | p. 17, A.6 |
| Transition limit | 30 | state transitions | Per execution | Author-reported | p. 17, A.6 |
| Repetition termination | More than 3 | repeats | Same action, same observation | Author-reported | p. 17, A.6 |
| Invalid-action termination | 3 | consecutive invalid actions | Per execution | Author-reported | p. 17, A.6 |
| TEXT-BISON retries | 10 | retries | Producing a valid action | Author-reported | p. 17, A.6 |
| Few-shot examples | 2 | examples | Both prompting strategies | Author-reported | p. 7 |
| Template consistency subset | 61 | templates | Described successful-template analysis | Author-reported | p. 8 |
| Fully solved GPT-4 templates | 4 | templates | No-hint consistency analysis | Author-reported | p. 8 |
| Shopping products | Approximately 90k | products | Magento shopping site | Author-reported | p. 15, A.1 |
| Shopping categories | Over 300 | categories | Product coverage | Author-reported | p. 15, A.1 |
| Forum subreddits / posts / users | 95 / 127390 / 661781 | counts | Postmill forum data | Author-reported | p. 15, A.1 |
| Initial subreddit sampling pool | Top 50 | subreddits | Before manual additions | Author-reported | p. 15, A.1 |
| GitLab repositories | 300 | repositories | Sampled environment | Author-reported | p. 15, A.1 |
| GitLab contributing accounts | More than 1000 | accounts | At least one commit | Author-reported | p. 15, A.1 |
| Repository sampling minimum | At least 10 | repositories/language | Reported sampling rule | Author-reported | p. 15, A.1 |
| Repository sampling allocation | 80 / remaining 20 | % | Upper/lower described percentile sets | Author-reported; second share derived from remainder | p. 15, A.1 |
| Shopping user history | Over 35 / 2 | orders / years | Logged-in customer profile | Author-reported | p. 16, A.3 |
| Environment reset | A few seconds to 1 minute | time | Varies by website | Author-reported | p. 15, A.2 |
| Wikipedia cutoff | May 2023 | date | Offline knowledge resource | Author-reported | p. 15, A.1 |
| Website task distribution | 23.0 / 22.4 / 22.2 / 13.4 / 13.1 / 5.9 | % | E-commerce / CMS / GitLab / Map / Reddit / Cross Site | Visually readable | p. 16, F6 |
| Fuzzy evaluator manual agreement | 39 of 40 | judgments | Compared with human judgment | Author-reported | p. 17, A.8 |
| Fuzzy-evaluated task examples | 82 | examples | Require GPT-4 evaluation | Author-reported | p. 17, A.8 |
| Date/duration fuzzy cases | 49, reported as 60% | examples / % | Subset of 82 | Author-reported | p. 17, A.8 |
| Format-equivalence test size | 900 each | examples | Dates and durations | Visually readable | p. 17, T6 |
| Format-equivalence accuracy | 100 each | % | Both GPT-4 versions, both datasets | Visually readable | p. 17, T6 |
| Manual evaluator agreement rate | 97.5 | % | 39 / 40 × 100 | Analyst-derived | p. 17 operands |
| Reasoning gain, hinted GPT-3.5 | 2.34 | percentage points | 8.75 − 6.41 | Analyst-derived | p. 8, T2 |
| GPT-4 no-hint overall change | +2.71 | percentage points | 14.41 − 11.70 | Analyst-derived | p. 8, T2 |
| Human–best-agent descriptive gap | 63.83 | percentage points | 78.24 − 14.41; different samples | Analyst-derived | pp. 7–8 |

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| WebArena evaluates realistic, operational web interactions. | Four self-hosted application categories, tools, resources, imported data. | F1–F3; system construction | pp. 2–4, 15 | HIGH for described design; realism and novelty remain author characterizations. |
| The benchmark tests high-level multi-step intents. | 812 intents, 241 templates, annotation criteria. | F5–F6; task construction | pp. 5–6, 16 | HIGH; selected tasks do not represent all internet use. |
| Outcome validation accommodates different valid paths. | Answer matching and state locators instead of action-sequence equality. | T1 | pp. 2, 6–7 | HIGH for evaluation approach; validator completeness is not established globally. |
| Baseline agents have low success. | Best reported GPT-4 overall SR 14.41%. | T2, X1–X2 | p. 8 | HIGH under stated prompt and inference conditions; not a security statistic. |
| UA guidance changes completion/abstention behavior. | GPT-4 achievable success rises while unachievable success falls without hint. | T2, X2 | p. 8 | HIGH descriptive evidence; effects differ for GPT-3.5. |
| Similar task semantics do not ensure consistent success. | Four fully solved GPT-4 templates; none for GPT-3.5 in described subset. | T3, X3 | p. 8 | HIGH for prose result; conditional subset and small plot limit generalization. |
| Human comparison substantially exceeds agent point estimates. | 78.24% versus 14.41%. | T2, X4 | pp. 7–8 | HIGH for reported values; unequal sampling and narrow participant group. |
| Fuzzy evaluator is accurate on examined cases. | 39/40 manual agreement; 100% format-equivalence accuracy. | T6, X6 | p. 17 | HIGH for bounded tests; MEDIUM for broad semantic-grading reliability. |
| Agents can miss important observed state. | Filled-query repetition, failure to select Users, wrong historical-data source. | F11, X7 | p. 22 | HIGH for examples; prevalence and causal explanation are not established. |
| Logged-in permissions make state-changing actions relevant. | Cached-cookie login and full CMS read/write profile. | A.3 | p. 16 | HIGH for setup; harmful misuse is not tested. |
| WebArena informs candidate security mechanisms. | Observation-to-action loop, user-specific access, persistent operations. | F1–F3, F7; analyst synthesis | pp. 3–6, 16, 18 | MEDIUM analyst inference; attacker control and exploitability remain unknown. |
| It does not establish comparative vulnerability against standalone LLMs. | All reported performance conditions are web agents or humans; no adversarial comparator. | T2 and experiment inventory | pp. 7–9, 17 | HIGH negative finding within the supplied document. |

# 22. Very simple explanation — Explain Like I'm 15

Imagine giving an AI a browser and asking it to organize a museum trip, buy something, or update a project page. Knowing what the words mean is only the beginning. It also has to find the correct information, remember what it already did, choose the right buttons, and check that the final result matches your request.

The researchers built a repeatable set of working websites to test this. They wrote 812 tasks and graded the outcome rather than demanding one exact sequence of clicks. Their best reported GPT-4 agent completed 14.41% of the tasks. A group of five computer-science graduate students achieved 78.24% on a sampled task set, so the numbers show a large descriptive gap, though the tests were not identical in sampling.

One surprising result was that telling an AI to stop when a task seemed impossible could make it give up on tasks that were possible. Removing that sentence helped GPT-4 complete more tasks, but made it worse at recognizing truly impossible ones. Other examples showed an AI using the wrong information or repeatedly typing a search that was already present.

For a security project, the important idea is that a browser agent connects reading to doing. It can see website content while logged into an account and can change that website's data. This paper gives evidence about those capabilities and ordinary mistakes. It does not show an attacker exploiting them, and it does not prove browser agents are more vulnerable than standalone language models. That comparison needs a separate security experiment.

# Completeness Audit

This audit measures coverage against the supplied inventory, not against an assumed ideal or unseen supplement. All main sections and Appendix A.1–A.10 were read from supplied text. All numbered figures and tables were additionally inspected in rendered page images. Text-only coverage is explicitly distinguished below.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, contributor footnotes | Yes, text and image | Yes | Fully represented | Inventory and opening metadata. |
| Abstract | Yes, text and image | Yes | Represented in compressed form | Central design and best results retained. |
| §1 Introduction | Yes, text and images | Yes | Fully represented substantively | Problem, gap, motivation, evaluation criticism. |
| §2 environment overview | Yes, text and images | Yes | Fully represented substantively | Components and realism/reproducibility rationale. |
| §2.1 formal environment | Yes, text and image | Yes | Fully represented | Tuple, transitions, histories, rewards, overloaded notation. |
| §2.2 website selection and implementation | Yes, text and images | Yes | Fully represented substantively | Approximate 200-history basis and four categories. |
| §2.3 observation space | Yes, text and image | Yes | Fully represented | URL, tabs, three modalities, viewport option. |
| §2.4 action space | Yes, text and images | Yes | Fully represented | Operations, coordinates/IDs, naming ambiguity. |
| User Role Simulation paragraph | Yes, text and image | Yes | Fully represented | Connected to A.3. |
| §3 benchmark overview | Yes, text and image | Yes | Fully represented | Task count and functional evaluation. |
| §3.1 collection criteria | Yes, text and images | Yes | Fully represented substantively | Abstraction, creativity, variables, inspiration aid. |
| §3.1 intent analysis | Yes, text and images | Yes | Fully represented | Counts, categories, distribution. |
| §3.2 answer evaluation | Yes, text and image | Yes | Fully represented | Three matching methods and evaluator model. |
| §3.2 state evaluation | Yes, text and images | Yes | Fully represented | Locators and required properties. |
| Unachievable tasks | Yes, text and image | Yes | Fully represented | Causes, N/A expectation, no security substitution. |
| Annotation process | Yes, text and image | Yes | Fully represented | Double annotation, adjudication, evaluator authors. |
| Human performance | Yes, text and image | Yes | Fully represented | Sample, participants, time, category scores, failure grouping. |
| §4 baseline agents | Yes, text and images | Yes | Fully represented | Models, prompts, examples, representation. |
| §5 main results | Yes, text and image | Yes | Fully represented | Every T2 numeric row retained. |
| §5.1 stopping analysis | Yes, text and image | Yes | Fully represented | 54.9% and model-specific ablation effects. |
| §5.1 template consistency | Yes, text and images | Yes | Represented with uncertainty | Prose counts retained; exact histogram bars unreadable. |
| §6 benchmark-related work | Yes, text and image | Yes | Represented in compressed form | Author categories and all T4 judgments retained. |
| §6 interactive-agent related work | Yes, text and image | Yes | Represented in compressed form | Planning, programs, search, recovery, summarization. |
| §7 conclusion | Yes, text and image | Yes | Represented in compressed form | Repeated claims integrated with conditions. |
| Acknowledgement | Yes, text only | Yes | Represented in compressed form | Thanks, resource support, sponsorship disclosure accounted for below. |
| References pp. 10–14 | Yes, supplied text; p. 12 also visual | Yes | Inspected but deliberately compressed | Bibliographic details not individually reproduced or verified. |
| A.1 website implementation | Yes, text only | Yes | Fully represented substantively | Dataset sizes, frameworks, sampling, regional/cutoff limits. |
| A.2 delivery and reset | Yes, text; p. 16 continuation visual | Yes | Fully represented | Packaging, reset procedure, time range, author overhead judgment. |
| A.3 user roles | Yes, text and image | Yes | Fully represented | Histories, permissions, cookies. |
| A.4 distribution | Yes, text and image | Yes | Fully represented | F6 labels retained exactly. |
| A.5 human-performance qualification | Yes, text and image | Yes | Fully represented | Demographics and domain knowledge. |
| A.6 configuration | Yes, text and image | Yes | Fully represented | Models, sampling, budget, termination, retries. |
| A.7 fuzzy-match prompt | Yes, text and image | Yes | Represented in compressed form | Semantic grading and binary scoring retained. |
| A.8 evaluator accuracy | Yes, text and image | Yes | Fully represented | 40, 39, 82, 49, 60%, both generated datasets. |
| A.9 agent prompts | Yes, text and images | Yes | Represented in compressed form | Inputs, action syntax, examples, hint ablation, credential page. |
| A.10 error analysis | Yes, text and image | Yes | Fully represented substantively | Bias, granular-state failures, previous action, speculative cause. |
| Figures 1–3 | Yes, visually | Yes | Fully represented substantively | Architecture, cross-site example, representation panels. |
| Figures 4–6 | Yes, visually | Yes | Fully represented | Actions, intent examples, all pie labels. |
| Figures 7–10 | Yes, visually | Yes | Represented in compressed form | Repeated prompt text not transcribed wholesale. |
| Figure 11 | Yes, visually | Yes | Fully represented substantively | Both failure panels and excerpts. |
| Tables 1–2 | Yes, visually | Yes | Fully represented | Validator examples and all result cells. |
| Table 3 | Yes, visually | Yes | Uncertain at exact-bar level | Labeled histogram; axes, legend, condition, prose results retained. |
| Tables 4–6 | Yes, visually | Yes | Fully represented | All feature patterns and numeric results retained. |
| E1–E5 mathematical concepts | Yes | Yes | Fully represented substantively | No major numbered equations or proofs omitted. |
| X1–X7 experiments/analyses | Yes | Yes | Fully represented | Distinct purposes, conditions, results, caveats. |
| Explicit objectives and §5.1 questions | Yes | Yes | Fully represented | No manufactured formal RQs. |
| Exploration/recovery and training hypotheses | Yes | Yes | Fully represented | Clearly identified as untested causal hypotheses. |
| Major contributions | Yes | Yes | Fully represented | System, dataset, evaluation, empirical findings, priority caveats. |
| Author-stated limitations | Yes | Yes | Fully represented substantively | Agent failures, human expertise, geography, reset cost. |
| Algorithms, theorems, lemmas | Not present as standalone objects | Accounted for | No such inventory objects | Procedures and equations described instead. |
| Separate supplementary files | Not supplied | Limitation stated | Missing from supplied material | No claim of supplementary review. |
| Public repository, images, scripts, trajectories, videos | No | Availability claims only | Uninspected referenced artifacts | No execution or artifact validation. |

## Missing or inaccessible material

No numbered page in the supplied 1–22 text sequence is missing. Rendered page images for pp. 10, 11, 13, 14, and 15 are absent, so those pages received text-only inspection. Public software, data packages, Docker images, reset scripts, trajectories, videos, and linked site resources were not supplied for inspection. No separate supplement was provided. The failed '-' image reference is not identifiable as an additional paper object.

## Uncertain interpretations

Exact Table 3 bar counts and the axis percentage/proportion convention remain uncertain. The relationship between 241 collected templates and 170 human-evaluation templates is unexplained. The successful-template subset of 61 requires its stated selection caveat. The repetition-termination description and the search-loop narrative are not fully reconciled. Tab-closing names and r_info argument order differ across presentations. Repository percentile wording is retained without inventing a sorting convention. Full baseline-history availability, exact task allocations to human participants, seeds, repeated runs, infrastructure specifications, and all validator aggregation rules are not specified.

Security exploitation and comparative vulnerability against standalone LLMs are UNKNOWN because the relevant attacker conditions and comparisons were not conducted. No evidence-based inference in this report is promoted into an author-reported security result.

## Deliberately compressed material

Repeated abstract, introduction, and conclusion statements are integrated rather than repeated verbatim. Figures 7–10 and A.7 contain lengthy prompt text; their substantive inputs, output rules, examples, credential-page reference, and ablation sentence are represented, while repeated boilerplate is compressed. Decorative application icons, browser chrome, page headers, and small screenshot interiors are accounted for without exhaustive transcription. Illustrative prices, IDs, example answers, and URLs are retained where necessary to understand validators or prompts rather than all being treated as study outcomes.

The acknowledgement thanks annotation reviewers, data providers, and discussion contributors; identifies computational support from the Center for AI Safety, partial Air Force Research Laboratory sponsorship, and an AWS AI gift; and includes a government-policy disclaimer (p. 10). These disclosures are represented here in compressed form and do not establish a methodological effect. References were inspected as bibliographic content, but individual publication metadata and links are not reproduced or externally validated.

## Potential omissions

No known major section, substantive appendix, numbered figure, numbered table, major mathematical concept, distinct reported experiment, central contribution, or author-stated limitation in the supplied inventory is wholly unrepresented. Exact low-resolution histogram values and unsupplied artifact contents remain unavailable. The report is therefore a comprehensive representation of the supplied evidence with explicit compression and uncertainty, not a claim to preserve every word or to verify unseen material.
