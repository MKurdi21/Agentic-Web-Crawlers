## Stage 0 — Document Accessibility Report

The supplied main document contains native/extracted text for physical PDF pages 1–12 and rendered source images for pages 1–11. All twelve pages were inspected as text; pages 1–11 were also inspected visually. Page 12 contains references and was inspected as text only. The isolated local-image error in the prompt does not make the eleven displayed page images inaccessible. No tools, browsing, external references, supplementary files, or original research repositories were used.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied text covers pages 1–12, including the conclusion and references |
| Apparently missing main-text pages | No interruption in the supplied numbered sequence; accessible page count alone cannot establish whether another version contains additional material |
| Visual content | Figures 1–6, Table 1, and equations on supplied rendered pages were visually inspected |
| Tables | Table 1 is readable; numerical heatmap annotations in Figures 4 and 6 are also supplied in extracted text |
| Equations | Equations (1)–(6) are readable; notation is normalized below without changing its meaning |
| Appendices | None present in the supplied document |
| Supplementary material | None supplied; no explicit supplementary-file reference identified |
| OCR | Not needed: native/extracted text and images are available |
| Principal limitation | Exact bar heights in Figures 3 and 5 are not numerically labeled; graphical positions must not be treated as exact results |
| Evidence gaps within the paper | Defense experiments and injection-generation outcome analyses are mentioned, but their detailed setups and results are not presented in the supplied twelve pages |

Evidence labels used throughout: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information [E] is introduced. Confidence labels describe confidence in what the supplied document supports, rather than independent verification that an experiment was executed as described.

## 1. Plain-language orientation

**LoginTrap studies how a web agent can be persuaded to disclose private information by treating a forged login requirement as a necessary step in an ordinary task.** A large language model (LLM) normally generates text. In the systems studied here, an LLM also helps operate a browser: it reads a page, chooses an action, clicks or types, observes the changed page, and continues. The attacker exploits that repeated interaction with a page the attacker controls. [A; pp. 1–4]

The attack does not initially say simply to reveal private data. It presents a page-specific explanation for logging in before continuing. If the agent accepts this explanation, it follows a forged login entry to an attacker-controlled form and enters sensitive information already available in its task background. The researchers use cloned webpages, a popup injection, and locally hosted login pages to measure both the initial login click and the subsequent sensitive-data entry. [A; pp. 4–7]

The dataset contains 80 cloned webpages and 1,175 associated tasks across five domains. With Browser-Use held fixed, four different LLM backbones yield an author-reported average Login Entry Rate of 93% and Attack Success Rate of 86%. With GPT-4o held fixed, three agent architectures have reported overall Login Entry Rates ranging from 84% to 94% and Attack Success Rates from 68% to 89%; the introduction reports 79% average attack success across architectures. These are separate experimental comparisons, not one pooled universal attack rate. [A; pp. 2, 6–9]

The central contribution is to identify and operationalize an earlier authentication decision: **whether the agent should enter a login flow at all**. The paper argues that protecting credentials after a form has been reached misses the possibility that an attacker can manufacture the apparent need to reach that form. Its evidence supports vulnerability under the tested controlled conditions. It does not directly compare browser agents with standalone, text-only LLMs. Any relevance to why agents might be more vulnerable is therefore an explicitly labeled analyst inference. [A/D; pp. 3–4, 10–11]

## 2. Document roadmap

The paper is an empirical cybersecurity study with a systems implementation and an LLM-agent evaluation. It is not a theoretical proof, systematic literature review, or direct standalone-model comparison.

| Original section | Location | Role |
|---|---|---|
| Abstract | p. 1 | States the threat, task-agnostic method, headline result, and authentication-boundary implication |
| §1 Introduction | pp. 1–2 | Motivates login as both a routine workflow and a sensitive boundary; states three contributions |
| §2 Background and Problem Setting | pp. 2–4 | Establishes the agent loop, manipulation channels, research gap, and attacker model |
| §2.1 LLM-Based Web Agents | pp. 2–3 | Explains observations, browser actions, and architectural variation |
| §2.2 Web Agent Manipulation | p. 3 | Groups prior attacks into textual/structural, visual, and interaction-level manipulation |
| §2.3 Motivation | p. 3 | Presents three gaps and the central research question |
| §2.4 Threat Model | p. 4 | Defines attacker control, objectives, knowledge restrictions, and runtime exclusions |
| §3 Methodology | pp. 4–6 | Connects the formal model to attack flow, environment construction, and injection generation |
| §3.1 Problem Formulation | p. 4 | Defines observations, history, policy, actions, and manipulated observations |
| §3.2 Attack Overview | pp. 4–5 | Explains login inducement followed by sensitive-data entry |
| §3.3 Attack Environment Construction | p. 5 | Describes cloned pages, popup, controlled login page, and standardized form |
| §3.4 Fuzzing-inspired Injection Generation | pp. 5–6 | Describes context construction, candidate generation, shadow evaluation, seed selection, and mutation |
| §4 Evaluation; §4.1 Evaluation Setup | pp. 6–7 | Gives questions, dataset, metrics, implementation, and budgets |
| §4.2 RQ1 | pp. 7–8 | Varies the LLM backbone within Browser-Use |
| §4.3 RQ2 | pp. 8–10 | Varies agent architecture with GPT-4o fixed |
| §5 Related Work; §§5.1–5.2 | p. 10 | Positions the work against agent security and credential-leakage research |
| §6 Conclusion | pp. 10–11 | Repeats the main security implication and calls for authentication-aware defenses |
| References [1]–[55] | pp. 11–12 | Bibliographic sources; not independently verified |

The document contains six numbered figures, one numbered table, six numbered equations, two evaluation research questions, and one broader motivating question. There are no numbered algorithms, formal hypotheses, theorems, appendices, or supplied supplements. Two additional analysis topics—defenses and generation outcomes—are mentioned without a corresponding detailed results section.

## 3. Background and context

An **LLM-based web agent** converts a user's natural-language request into browser operations. Its observation may include webpage text, HyperText Markup Language (HTML), a Document Object Model (DOM), accessibility-tree information, screenshots, or combinations of these. A DOM is a structured representation of page elements; an accessibility representation exposes interface information in another structured form. The paper describes these as alternative or complementary ways for agents to perceive a page. [A; §§2.1–2.2, pp. 2–3]

**Action grounding** connects an intended action, such as selecting a login control, to a concrete webpage element and browser operation. Different architectures combine planning and grounding differently. Browser-Use directly selects operations through tool calls; LiteWebAgent separates action descriptions from their grounding; Skyvern uses Planner, Actor, and Validator components. These descriptions explain the comparison categories, but do not by themselves prove which component causes a measured security difference. [A; §4.3, p. 9]

**Indirect prompt injection** here means attacker-controlled external page content influencing the agent's decisions. The user has authorized an ordinary task, but the agent encounters a page that supplies an additional apparent requirement. The security boundary is crossed when page content is allowed to determine what actions are necessary and what sensitive information should be entered. The paper treats structural, visual, and interaction-level content as possible manipulation channels. [A; §2.2, p. 3]

**Phishing-style login inducement** is more specific than a generic instruction to ignore the user. The attacker makes authentication appear relevant to the service and thereby inserts an additional step into the workflow. The attack can appear consistent with task completion even though its destination is controlled by the attacker. **Task-agnostic** means the injection is generated without the actual assigned user task; it does not mean the injection ignores webpage context. Indeed, page-specific context is a central input to construction. [A; §§2.3–3.4, pp. 3–6]

The related-work discussion distinguishes this problem from password-manager or browser-autofill leakage. Those systems must decide when and where to fill information once a login context exists. LoginTrap concentrates on the earlier choice to enter that context. The cited studies are represented only through the authors' descriptions; their empirical claims are not independently evaluated here. [A; §5.2, p. 10]

## 4. Research problem and gap

**Existing problem.** Agents must determine which browser interactions are necessary for a delegated task, while the page providing evidence for that determination may itself be malicious. Login is particularly consequential because accepting it can lead to private-data entry. [A; pp. 1–2]

**Shortcomings attributed to previous approaches.** The authors argue that merely measuring whether injected content triggers a target action does not fully capture an attack that crosses a login boundary and causes information leakage. They also argue that task-specific attack settings, known agent configurations, and purpose-built social-engineering pages leave open whether attacks can be constructed from ordinary webpage context with limited attacker knowledge. These are the authors' characterizations of prior work, not an independently established literature-wide verdict. [A; §§1, 2.3, pp. 2–3]

**Three stated gaps.** First, login inducement is underexplored as a general privacy-leakage path. Second, attack construction often assumes knowledge of a task or agent. Third, preserving realistic original-page context while adding a scalable controlled attack path remains challenging. [A; §2.3, p. 3]

**Motivation.** Many benign tasks do not inherently require authentication, while login prompts are common enough to seem plausible. The attacker can exploit this mismatch by presenting authentication as an intermediate prerequisite. [A; §2.3, p. 3]

**Scope.** The tested attack uses cloned webpages with a popup and controlled login destination, synthetic sensitive information, a five-interaction agent budget, selected Mind2Web-derived tasks, and specified models and frameworks. The experiment does not establish live credential theft from real user accounts, prevalence of malicious pages on the open web, or a general vulnerability ranking between standalone LLMs and web agents. [A/D; §§2.4, 4.1, pp. 4, 6–7]

## 5. Research questions, objectives, and hypotheses

The broader motivating question is: can attacker-controlled webpages cause agents to leak sensitive information through login flows without knowing the user task? This appears explicitly in §2.3, p. 3. It is answered operationally by constructing page-specific attacks without the actual task and testing subsequent browser behavior.

The two formal evaluation questions are:

- **RQ1:** How effective is LoginTrap across different LLM backbones? The comparison fixes Browser-Use and varies GPT-4o, Gemini 3 Flash, Claude Sonnet 4, and DeepSeek-V3.2. [A; pp. 6–7]
- **RQ2:** Does LoginTrap generalize across different web-agent architectures? The comparison fixes GPT-4o and varies Browser-Use, LiteWebAgent, and Skyvern. [A; pp. 6, 8–9]

The methodological objectives are to construct a task-agnostic login-inducing attack, retain original-page context through cloning, automate page-specific statement generation, and distinguish login entry from sensitive-information leakage. The introduction also claims analysis of robustness against defenses. The supplied results do not provide a separately documented defense experiment. [A; pp. 2, 5–7, 10–11]

No formal null hypotheses, alternative hypotheses, preregistered predictions, or hypothesis-testing thresholds are supplied. The authors additionally announce analysis of accepted statements and their origins/outcomes in §4.1, but the available evaluation subsections do not report a detailed corresponding analysis. This is a reporting gap, not evidence that such analysis was never performed.

## 6. Assumptions / Threat Model

The user delegates an ordinary task to an agent that can click, type, and navigate. The agent has a task T and background information B; the latter can contain values that become sensitive if entered into the wrong page. The experiment supplies synthetic sensitive information rather than reporting collection of real user secrets. [A; §§2.4, 3.1, 4.1, pp. 4, 7]

**Attacker capabilities:** the attacker controls cloned webpages resembling benign ones, places a login-inducing popup in them, controls the forged login entry, and controls the destination login page. This is substantial control of the encountered page and its authentication path. It is narrower than runtime compromise but broader than control of a single inert text sentence. [A; §2.4, p. 4]

**Attacker goal:** persuade the agent that login is required to continue, then obtain sensitive information through the controlled login flow. The initial login click is an intermediate outcome; the final objective is data entry/leakage. [A; pp. 4–7]

**Excluded knowledge and control:** the attacker does not know the actual user task, agent architecture, underlying model, system prompt, or safety policy; cannot modify the agent runtime; and cannot observe its internal reasoning. Before the agent enters the induced login flow, the attack operates through visible webpage content. [A; §2.4, p. 4]

**Important distinction:** the construction pipeline creates a benign probe task and uses two shadow evaluators. Therefore, task-agnostic does not mean no task-like context or no model feedback is used. It means the actual victim assignment and victim internals are unavailable to the attacker. The shadow models are part of candidate construction, not the final victim-agent success measurement. [A; §3.4, p. 6]

**Analyst interpretation:** the critical trust separation is between the user's task/background and external page claims about prerequisites. The paper does not provide a complete formal trust architecture, credential-origin binding mechanism, or user-approval policy. Its observation model explains how the page can influence action selection; it does not prove that every implementation must accept the page's authority. [D; §§3.1–3.3]

## 7. Methodology

### Controlled attack environment

Each original page is cloned to retain text and layout. A controlled popup contains the login-inducing statement, forged login entry, and close button; the authors say the remainder of the page is unchanged. Keeping the rest of the page stable is intended to isolate the inserted login surface. This is a construction rationale, not a reported randomized causal comparison against a clean-page control. [A/D; §3.3, p. 5]

The forged entry leads to a local controlled login page. An LLM summarizes the cloned page's content and service purpose, then combines that summary with login templates to generate a context-matching description. The form uses a fixed line-separated layout so that entered values can be parsed and compared consistently across pages, tasks, and agents. The exact sensitive-field inventory and form templates are not supplied. [A; §3.3, p. 5]

### Fuzzing-inspired candidate construction

For each page, an LLM extracts a compact summary, potential supported tasks, and a benign probe task that does not mention login. Semantic initialization strategies produce candidate login statements grounded in that page context. The paper does not enumerate all strategy texts, prompts, or candidate counts. [A; §3.4, pp. 5–6]

Each candidate is assessed by two shadow LLMs using the injected page and probe task. One is a base evaluator; the other receives an extra reminder to avoid suspicious webpage instructions. Both must predict an action toward the login entry for acceptance. Otherwise, predicted labels and a reward are retained for mutation feedback. These predictions filter candidates; they do not count as final attack success. [A; p. 6]

If initialization produces no accepted statement, failed candidates form a seed pool. A Monte Carlo Tree Search (MCTS)-inspired policy balances exploration and partial inducement signals. Mutation applies crossover, expansion, rephrasing, or compression. Seed selection uses the top three failed candidates ranked by reward. An accepted statement is returned if one is found within the generation budget; that budget's numeric value and failure-handling details are not specified. GPT-4o is used for context construction, candidate generation, mutation, and evaluation. [A; pp. 6–7]

### Dataset and implementation

The researchers use Mind2Web tasks to select realistic webpage–task pairs rather than replaying its original offline traces. They identify corresponding online pages, clone them, remove pages that cannot be reliably cloned, and retain associated normal tasks. The final set has 80 pages and 1,175 task instances. Exclusion counts, site identities, exact background-information construction, and sampling seeds are not reported. No train/validation/test split is described. [A; §4.1, p. 6]

Cloning uses a browser-driven pipeline with HyperText Transfer Protocol (HTTP) fallback for dynamic or partly inaccessible content. Pages and login destinations are hosted locally. Each run begins in a fresh Chrome instance, with browser state reset between executions. Every experiment uses a maximum of five agent interaction steps. The paper does not provide hardware, operating-system details, framework revisions, full API model identifiers, sampling temperatures, runtime, token usage, or costs. [A; §4.1, p. 7]

### Measurement

Observable browser logs contain action types, target elements, navigation, and form inputs when available. Labels are based on executed behavior rather than hidden reasoning. Login Entry Rate (LER) measures forged-entry clicks. Attack Success Rate (ASR) requires entry followed by sensitive-information input. Page Exploitability Rate (PER) asks whether at least one attempt succeeds on each page within a fixed budget. For PER, three associated tasks are randomly sampled and each is repeated three times, producing nine attempts per page. Attempt consumption counts through first success; failures receive the full budget of nine. [A; pp. 6–7]

No statistical tests, confidence intervals, standard errors, or reported significance thresholds accompany the main comparisons. No baseline attack or no-injection result is given in the supplied evaluation. The varied models and architectures are comparison conditions, not defenses or clean controls.

## 8. Experiments / Analyses

| ID | Purpose and design | Outcomes and evidence | Caveats |
|---|---|---|---|
| X1: Backbone comparison | RQ1; Browser-Use fixed; four LLM backbones; five domains from the 80-page, 1,175-task dataset | Average LER 93%, average ASR 86%; Figure 3; pp. 7–8 | Averaging weights and exact domain-by-model numerical bar values are not tabulated |
| X2: Backbone page exploitability | RQ1; three tasks × three repetitions per page for each backbone | All pages exploitable within nine attempts; Figure 4; p. 8 | At least one success within a budget differs from success on every execution |
| X3: Architecture comparison | RQ2; GPT-4o fixed; Browser-Use, LiteWebAgent, Skyvern | Overall LER 84%–94%; ASR 68%–89%; Figure 5; pp. 8–10 | Architecture descriptions do not isolate component-level causes |
| X4: Architecture page exploitability | RQ2; same nine-attempt page-level budget | Browser-Use 80/80, LiteWebAgent 75/80, Skyvern 79/80, derived from Figure 6 cell counts | Derived totals aggregate domain counts; no uncertainty interval supplied |
| X5: Defense robustness | Claimed in abstract, contributions, implementation discussion, and conclusion | Conclusion says task-instruction, system-prompt, and action-supervision defenses reduce but do not eliminate leakage | Detailed configurations, comparisons, numerical outcomes, and separate results absent |
| X6: Generation outcome analysis | §4.1 announces analysis of accepted statements and attack outcomes | Construction method is described in §3.4 | No reported strategy breakdown, acceptance rate, mutation gain, or detailed outcome analysis |

For X1, the authors attribute stable login-to-input conversion in Gemini 3 Flash and Claude Sonnet 4 to continuation of the accepted workflow. For GPT-4o and DeepSeek-V3.2, they report incomplete form filling, early termination, and return to the original task in action logs. The logs themselves and quantitative failure-category counts are not supplied. [A; pp. 7–8]

For X3, the authors discuss LiteWebAgent's additional grounding stage as a possible opportunity for execution mismatch and Skyvern's workflow persistence as a possible contributor to completing the malicious form. These are explanatory interpretations in the paper, not isolated interventions on grounding or validation modules. [A/D; p. 9]

## 9. Results

**Backbone-level task outcomes:** with Browser-Use fixed, reported mean LER is 93% and mean ASR is 86%. The difference is **7 percentage points, analyst-derived as 93 − 86**. Because the aggregation scheme is not specified, this subtraction should not be converted into an exact pooled conditional probability of leakage after login. The result establishes that the measured harm frequently extends beyond clicking. [A/C; §4.2, p. 7]

**Backbone-level page outcomes:** every tested page has at least one successful attack within nine attempts for every tested backbone. Thus the reported page-level result is 100% PER within this budget. This does not mean all individual task executions succeed, nor that all possible tasks or pages would be vulnerable. [A; Figure 4, p. 8]

**Architecture-level task outcomes:** overall LER spans 84%–94% and ASR spans 68%–89%. These ranges refer to architecture-level outcomes described in prose, not necessarily the minimum and maximum individual bars among all domains. The introduction's mean ASR of 79% belongs to this architecture comparison. [A; pp. 2, 9]

**Architecture-level page outcomes:** Figure 6 gives all-domain counts. Browser-Use has 24 + 16 + 16 + 13 + 11 = 80 successes out of 80 pages, or 100% PER. LiteWebAgent has 24 + 15 + 15 + 11 + 10 = 75 out of 80, or 93.75%. Skyvern has 24 + 15 + 16 + 13 + 11 = 79 out of 80, or 98.75%. These totals and percentages are analyst-derived from visually readable/source-extracted annotations. [B/C; Figure 6, p. 9]

**Attempts to first success:** in Figure 4, displayed means range from 1.00 to 1.55 across backbone–domain cells. In Figure 6, they range from 1.00 to 2.54 across architecture–domain cells. These statistics include failures coded as nine, so a larger mean can reflect delayed successes, pages without observed success, or both. They are not computational runtime or expected attacks-to-success in an unlimited process. [A/B; pp. 7–9]

**Defense result:** only a qualitative conclusion is available. No defensible percentage reduction or defense ranking can be extracted. **Generation improvement:** no ablation establishes how much mutation, shadow evaluation, popup design, or page-specific wording independently contributes to the final success rates. [D; supplied evaluation and conclusion]

## 10. Figure-by-figure interpretation

### Figure 1 — High-level attack concept, p. 1

This is a conceptual diagram rather than a quantitative plot. The left side shows a user, diverse routine tasks, and an observing/acting web agent. The upper-right comparison contrasts a stronger assumed knowledge set containing the user task and agent internals with the attack's actual page-only knowledge assumption. The original webpage is collected by the attacker, transformed into a LoginTrap webpage, and exposed to the agent. A depicted login-first response leads toward privacy leakage. [B]

Its main contribution is to communicate the intended knowledge boundary and flow from original-page context to malicious workflow. Arrows show construction and interaction, not measured probabilities. The figure does not prove that the attack has no dependency on generator-model behavior; that dependency is described separately in the method. [A/B/D]

### Figure 2 — Detailed attack trajectory, p. 5

The diagram has three main regions: task/background inputs, the agent's evolving plan, and the attacker's pages. Inputs include query/book/shop tasks and profile/contract/account background categories. These are schematic categories rather than a published field-by-field dataset specification. Numbered arrows show: 1 task submission, 2 navigation to the injected page, 3 observation, 4 login click, 5 observation of the redirected form, and 6 information input. [B]

The agent's plan changes from opening a site and reading information to prioritizing login and then completing login before returning to the task. The forged page contains a login-to-continue statement; the destination contains a sensitive-information field and submission control. The diagram illustrates plan revision, but the evaluation labels observable actions rather than verifying these depicted internal thoughts. Its six labeled exchanges should not be equated directly with the five-interaction implementation budget: the figure includes user submission and observation exchanges, and the paper does not give an exact mapping between the two counting schemes. [A/B/D]

### Figure 3 — Backbone-level LER and ASR, p. 8

Five panels represent Travel, Service, Information, Shopping, and Entertainment. Within each panel, four grouped conditions are GPT-4o, Gemini 3 Flash, Claude Sonnet 4, and DeepSeek-V3.2. The vertical axis is Rate (%), with visible labeled ticks from 60 to 100 and a truncated lower range. Blue and orange hatched bars distinguish LER and ASR. There are no visible error bars, confidence intervals, or significance markers. [B]

The visual shows frequent login entry and generally lower or equal end-to-end success. Gemini 3 Flash and Claude Sonnet 4 have small gaps in many domains; DeepSeek-V3.2 has visibly larger gaps in several. Shopping generally exhibits high bars. Exact individual bar values are not labeled, so they are not transcribed as exact percentages. The exact overall 93% LER and 86% ASR come from prose on p. 7. Truncation enlarges the visual impression of differences and must be kept in mind. [A/B]

### Figure 4 — Backbone page exploitability and attempt consumption, p. 8

This heatmap has model rows and domain columns. Every cell contains an exploitable-page numerator/denominator and a parenthesized mean attempt count. The blue color scale represents average attempts consumed, approximately labeled across 1.0–1.6; darker shading indicates larger values. It does not encode PER directly. Every numerator equals its denominator. [B]

| Backbone | Travel | Service | Information | Shopping | Entertainment |
|---|---|---|---|---|---|
| GPT-4o | 24/24 (1.38) | 16/16 (1.31) | 16/16 (1.50) | 13/13 (1.00) | 11/11 (1.55) |
| Gemini 3 Flash | 24/24 (1.00) | 16/16 (1.06) | 16/16 (1.00) | 13/13 (1.00) | 11/11 (1.00) |
| Claude Sonnet 4 | 24/24 (1.00) | 16/16 (1.19) | 16/16 (1.00) | 13/13 (1.00) | 11/11 (1.09) |
| DeepSeek-V3.2 | 24/24 (1.12) | 16/16 (1.00) | 16/16 (1.19) | 13/13 (1.08) | 11/11 (1.00) |

These are readable annotations, not estimates from shading. The heatmap supports broad tested-page exploitability while distinguishing how quickly success appears. Means are displayed to two decimals without dispersion. A value of 1.00 suggests first-attempt success under the displayed statistic; exact raw run sequences are unavailable. [A/B]

### Figure 5 — Architecture-level LER and ASR, p. 9

The same five domain panels compare Browser-Use, LiteWebAgent, and Skyvern with GPT-4o fixed. The vertical axis is Rate (%), again truncated, with labeled ticks from 60 to 100. Blue/orange hatching distinguishes LER and ASR. No error bars or exact numerical labels accompany the bars. [B]

LiteWebAgent commonly has lower ASR than the other displayed architectures, while all show substantial entry into the forged login path. Skyvern often has high entry and leakage bars. The figure supports architecture-dependent reliability, but cannot establish a causal explanation from a Planner, grounding module, or Validator alone. Exact individual bars remain graphical, not exact source numbers. Reported architecture-wide ranges are taken from p. 9 prose. [A/B/D]

### Figure 6 — Architecture page exploitability and attempt consumption, p. 9

Rows are architectures; columns are domains. Cell labels have the same meaning as Figure 4. The colorbar indicates average attempts consumed, with visible labels around 1.0–2.5; darker cells correspond to higher means. [B]

| Architecture | Travel | Service | Information | Shopping | Entertainment |
|---|---|---|---|---|---|
| Browser-Use | 24/24 (1.38) | 16/16 (1.31) | 16/16 (1.50) | 13/13 (1.00) | 11/11 (1.55) |
| LiteWebAgent | 24/24 (1.67) | 15/16 (2.44) | 15/16 (2.00) | 11/13 (2.54) | 10/11 (2.36) |
| Skyvern | 24/24 (1.00) | 15/16 (1.62) | 16/16 (1.06) | 13/13 (1.00) | 11/11 (1.09) |

Browser-Use matches its GPT-4o row in Figure 4, providing a useful cross-figure consistency check. LiteWebAgent leaves five pages unexploited within budget, and Skyvern leaves one; those counts are derived by subtraction from the readable cell denominators. Failure within nine attempts is not proof that exploitation is impossible under another task or budget. [B/C/D]

## 11. Table-by-table interpretation

### Table 1 — Dataset statistics by domain, p. 6

| Domain | Webpages | Tasks |
|---|---:|---:|
| Travel | 24 | 309 |
| Service | 16 | 281 |
| Information | 16 | 276 |
| Shopping | 13 | 173 |
| Entertainment | 11 | 136 |
| Total | 80 | 1,175 |

Rows identify website domains and columns count cloned webpages and associated tasks. There are no percentage units, comparison methods, missing entries, uncertainty terms, significance tests, or substantive footnotes. Travel has the most pages and tasks; Entertainment the fewest. Service and Information tie at sixteen pages but have different task counts. [A/B]

**Analyst-derived consistency check:** 24 + 16 + 16 + 13 + 11 = 80 pages, and 309 + 281 + 276 + 173 + 136 = 1,175 tasks. These totals agree with the dataset prose. The overall mean is 1,175/80 = 14.6875 tasks per page, but this derived average does not imply equal page-level task allocation. [C]

The table documents coverage of selected domains, not representativeness of all websites. It does not list unique sites, pages excluded during cloning, task difficulty, field types, or the allocation of tasks among individual pages. The three-task sample used in PER is a separate evaluation procedure; it should not replace the full dataset's task counts. [A/D]

## 12. Diagram / Architecture

Figures 1 and 2 jointly describe two connected processes: **attack construction** and **victim interaction**. Construction takes original-page context, generates a plausible login rationale, inserts the popup, and prepares a matching login page. Interaction takes the user's task/background, exposes the agent to the injected page, induces a login click, and offers a form that can receive background information. The original page and controlled destination are attacker-side artifacts; action selection remains inside the unmodified agent. [A/B; pp. 1, 4–6]

The generator has a feedback loop: candidate → two shadow predictions → acceptance or failure feedback → seed selection/mutation → reevaluation. Acceptance requires agreement toward login from both evaluators. This loop optimizes an intermediate proxy, not directly observed victim leakage. The full browser evaluation subsequently tests whether the proxy-selected statement causes actual entry and input. [A; p. 6]

The victim's own observation–action loop is a different loop. After navigation, it receives new context from the controlled login page and may continue its accepted plan. This distinction explains why LER and ASR can diverge: the initial popup influences entry, while the destination and subsequent execution affect completion. [A; pp. 4–8]

Browser-Use, LiteWebAgent, and Skyvern differ in control organization, but share this dependence on external observations. The architecture comparison tests complete systems with GPT-4o fixed. It does not independently swap grounding, planning, and validation modules, so proposed module-level explanations remain qualified. The paper supplies no standalone architecture diagram for each framework beyond the textual descriptions. [A/D; pp. 8–9]

## 13. Equations and mathematical concepts

### Equation (1): interaction history

`H_t = ⟨(s_1,a_1), …, (s_{t−1},a_{t−1})⟩` [p. 4]

This ordered sequence contains earlier webpage observations `s_i` and executed actions `a_i` before time `t`. Order matters because later choices depend on what the agent has seen and done. It is a state-history definition, not a learned loss or optimization objective. The empty initial history is not explicitly discussed.

### Equation (2): observation extraction

`s_t = O(w_t) = (h_t,i_t)`, with `i_t = R(h_t)` [p. 4]

`w_t` is the encountered webpage state, `O` is observation extraction, `h_t` is textual/structured content such as HTML, DOM, or accessibility information, and `i_t` is a rendered screenshot produced through `R`. The pair abstracts text-only, visual, and combined agents. It is a conceptual representation, not a complete browser rendering specification. The paper does not define all resources or runtime state that a practical renderer would use; no additional semantics are assumed here.

### Equation (3): action selection

`a_t = Π(s_t,T,B,H_t)` [p. 4]

`Π` represents the agent and underlying model as a policy. Inputs are current observation, user task `T`, background `B`, and history. Output is the next browser action. An action is represented by `(o_t,r_t,e_t)`: operation type, optional argument, and optional target element. Operations include click, type, scroll, and navigate. For typing, an argument can be input text; for navigation it can be a destination URL. The abstraction does not specify a probability distribution, temperature, or deterministic policy.

### Equation (4): manipulated observation, fixed task and agent

`ã_t = Π(s̃_t,T,B,H_t)`, where `s̃_t = O(w̃_t)` [p. 4]

Tildes indicate the injected webpage state, extracted observation, and resulting action. The equation conceptually holds task, background, history, and policy fixed while changing page content. It expresses the intended attack mechanism: influence behavior through the observation rather than rewriting the user's task or agent runtime. It is not itself empirical proof of causation; the controlled evaluation supplies behavioral evidence.

### Equation (5): page exploitability indicator

`e_w = max_{1≤c≤C} δ_c^(w)`, with `δ_c^(w) ∈ {0,1}` and `C = N×K` [p. 7]

`δ_c^(w)` indicates whether attempt `c` on page `w` meets ASR success. The maximum is one if any attempt succeeds and zero otherwise. `N` is sampled associated tasks and `K` repetitions per task. With `N=3` and `K=3`, `C=9`. The maximum intentionally discards how many other attempts fail; attempt consumption supplies a complementary timing statistic.

### Equation (6): Page Exploitability Rate

`PER = (1/|W|) Σ_{w∈W} e_w` [p. 7]

`W` is the evaluated page set and `|W|` its size. Summing binary indicators counts pages with at least one success; dividing yields their fraction. Multiplication by 100 expresses a percentage. PER weights pages equally, unlike an unspecified task-weighted aggregate over pages with different task counts. Its meaning depends on the fixed attempt budget and selected tasks.

No theorem, proof, objective function, gradient update, or explicit MCTS scoring equation is supplied. The reward function and candidate-generation budget remain unspecified. LER and ASR are defined in prose rather than separate numbered formulas.

## 14. Interpretation and discussion

**Answer to RQ1:** the tested attack is effective across all four chosen backbones within Browser-Use. Differences chiefly appear in whether entry converts into sensitive input. The evidence is strong for existence and frequent success under these conditions, but weaker for a causal explanation of model differences because no intervention isolates perception, planning, or form filling. [A/D; pp. 7–8]

**Answer to RQ2:** direct tool loops, modular grounding, and multi-component workflows all remain susceptible. Architecture changes measured reliability rather than eliminating the attack in the tested systems. The page-level results qualify universality: not every page is successfully exploited under LiteWebAgent or Skyvern within nine attempts. [A/B; pp. 9–10]

**Research relevance—analyst inference:** the paper illustrates why adding browser interaction can create consequential security pathways beyond answer generation. External content is repeatedly encountered, interpreted as evidence about task requirements, and converted into actions. Available background information can then be typed into an adversarial destination. A malicious prerequisite can therefore alter an execution trajectory, not merely a final textual answer. This is an explanation of a mechanism demonstrated in agents, not evidence of a measured relative vulnerability against standalone LLMs. [D; pp. 3–4, 7, 10]

**No direct standalone comparison:** the shadow evaluators are construction tools, not a matched standalone-LLM control group. They predict actions for filtering candidates and do not produce an outcome comparable to browser-based information leakage. The experiment cannot quantify how much more vulnerable agents are, whether the same base model would refuse a comparable text-only request, or whether tool access alone causes a difference. [D; pp. 6–9]

**Consistency checks:** Table 1 totals match dataset prose; the GPT-4o/Browser-Use Figure 4 row matches the Browser-Use Figure 6 row. The 86% and 79% results concern different comparison axes and are not contradictory. The generic metrics paragraph on p. 6 describes task-level metrics collectively as measuring final leakage, but the detailed definition explicitly distinguishes LER as entry without necessarily implying leakage; the specific definition governs interpretation. [A/B/D]

**Unresolved reporting:** pp. 10–11 claim evaluation of several defenses, but no corresponding detailed section, figure, or table is supplied. Page 6 promises accepted-statement/outcome analysis without reporting a separate analysis. The narrative alternates among filling, inputting, and submitting sensitive information: the formal ASR definition and implementation require entry into the form, while broader attack descriptions emphasize submission. Consequently, ASR should be described as sensitive input after login entry, without assuming every success includes a separate submit-button event. [A/D]

## 15. Contributions and novelty

| Contribution category | What the paper contributes | Evidence and qualification |
|---|---|---|
| Conceptual | Login inducement as an authentication-boundary attack preceding sensitive input | Motivation and framing, pp. 2–4; novelty is the authors' positioning |
| Methodological | Distinct entry, leakage, and page-level exploitability measurements | LER, ASR, PER, pp. 6–7 |
| Algorithmic | Page-specific, task-agnostic candidate generation with shadow evaluation and mutation | §3.4, p. 6; no full pseudocode or ablation |
| System/implementation | Cloned context plus popup and controlled login destination | §3.3 and implementation, pp. 5, 7 |
| Dataset/evaluation | Selected 80-page, 1,175-task controlled environment spanning five domains | Table 1 and §4.1, p. 6; no supplied release artifact |
| Empirical | Cross-backbone and cross-architecture behavioral results | Figures 3–6, pp. 8–9 |
| Defensive implication | Authentication necessity should be evaluated relative to the original task | Conclusion, p. 11; proposed direction rather than demonstrated complete defense |

The authors explicitly identify login-risk exploration, task-agnostic attack-flow design, and comprehensive analysis as their three contributions. The supplied paper supports meaningful method and empirical contributions, while its defense-robustness component is less traceable because detailed evidence is absent. No theoretical guarantee, formal optimality claim, or proof of uniqueness across all prior literature is established. [A/D; p. 2]

## 16. Limitations

### Authors' stated limitations and boundaries

There is no dedicated limitations section. The authors explicitly state that LER does not imply leakage, that binary PER needs a complementary attempt statistic, and that some architecture–page combinations remain unexploited within budget. They disclose filtering out pages that cannot be reliably cloned, a five-interaction maximum, local hosting, and synthetic sensitive values. These are stated methodological boundaries, although the authors do not consistently label them limitations. [A; pp. 6–9]

They also distinguish being induced to enter login from consistently completing input. Lower ASR can reflect incomplete forms, early termination, or return to the original task. Thus their own discussion limits the inference that a successful initial inducement guarantees the full harm. [A; pp. 7–8]

### Additional evidence-based analyst observations

**Selection and environment:** successful cloning is an inclusion condition. The supplied work does not quantify excluded pages or show that local clones preserve all live-site security and interaction behavior. Generalization to the open web remains bounded by this design. [D]

**Measurement:** synthetic background values demonstrate a data-flow risk, but do not establish theft of operational credentials, automatic password-manager release, or compromise of a real account. ASR's input-versus-submission wording requires care. [D]

**Causal attribution:** no clean-page outcome, popup-only control, alternative attack baseline, or component ablation is reported. The study demonstrates successful attack configurations but does not isolate how much each construction component contributes. [D]

**Reporting and reproducibility:** exact prompts, reward formula, numerical generation budget, seeds, framework versions, full per-condition counts, uncertainty measures, code release, and detailed defenses are not supplied. These gaps limit replication and precise comparative conclusions. [D]

**Question mismatch:** no standalone-LLM arm is evaluated. The paper supports a mechanism relevant to the user's research question, not its comparative premise as an experimental finding. [D]

## 17. Threats to validity

The following validity categories are analyst assessments, not labels used by the authors.

**Internal validity:** the researchers hold framework or backbone fixed in the respective comparisons, reset browser state, and use uniform action-based labeling. These choices help control some variation. Nevertheless, full systems can differ in prompts, observation processing, execution semantics, and versions; no component-level interventions or untreated-page results isolate the precise causal contribution of each factor. [D; pp. 7–9]

**Construct validity:** LER closely corresponds to the specified forged-entry click. ASR captures sensitive input after entry but should not automatically be interpreted as successful network transmission after submission or real-account compromise. PER measures at least one success within a selected finite budget, not a page's unconditional vulnerability probability. A five-step cap can also affect whether an agent reaches the input stage. [D]

**External and ecological validity:** the use of original-page context and ordinary benchmark tasks improves relevance to browsing. However, local clones, controlled forms, synthetic background data, filtering for clonability, and a small fixed interaction budget differ from unconstrained deployments. The evidence concerns five domains and selected systems rather than all websites, agents, or authentication mechanisms. [D]

**Statistical conclusion validity:** no error bars, confidence intervals, tests, or seeds are supplied. Tasks share pages, and repetitions share page/task contexts, so they should not automatically be assumed independent observations. The reported average's weighting is unspecified; small model or domain differences cannot be assigned statistical significance from the supplied plots. [D]

**Reproducibility:** the broad procedure and key budgets are documented, but exact generation settings, prompts, software revisions, task/background records, raw logs, and detailed defenses are absent from the supplied material. Their absence here does not prove they do not exist elsewhere; it prevents checking them in closed-document mode. [D]

## 18. Future work and open questions

### A. Explicitly proposed by the authors

The conclusion calls for authentication-aware defenses that assess both whether content is suspicious and whether login and sensitive input are necessary for the original user task. It argues that authentication should be treated as a distinct security boundary in agent execution. No complete implemented solution or measured benefit for that proposed design is supplied. [A; p. 11]

### B. Additional open questions inferred from this study

- How would a matched standalone LLM respond to comparable malicious prerequisites and sensitive-information requests without browser execution?
- Which component—contextual wording, popup placement, matching destination description, mutation, or shadow filtering—accounts for the largest change in success?
- How do longer interaction budgets affect both malicious continuation and opportunities to recover to the legitimate task?
- Do domain/origin checks, task-based authorization, or user approval at sensitive input reduce leakage while preserving benign task completion?
- How do results change with live services, different form layouts, unavailable background secrets, or authentication beyond the controlled form?
- What are the exact efficacy and benign-task costs of the defenses mentioned in the conclusion?
- How stable are the reported comparisons across seeds, framework versions, model configurations, and broader page samples?

These are analyst-generated questions, not claims that the paper tested these interventions. [D]

## 19. Terminology and notation glossary

| Term or symbol | Meaning in this paper |
|---|---|
| LLM | Large language model used to interpret context and choose or support actions |
| Web agent | Browser-operating system driven by an LLM; observes, acts, and repeats |
| Indirect prompt injection | External content influencing decisions beyond its legitimate role as task data |
| Phishing-style attack | A deceptive login context directs sensitive entry to an attacker-controlled page |
| Task-agnostic | Constructed without the actual victim task, while using page context and a generated probe task |
| Black-box attacker | Lacks victim model, architecture, prompt, policy, and internal-reasoning knowledge in the stated model |
| HTML | HyperText Markup Language, one representation of webpage content |
| DOM | Document Object Model, structured webpage elements |
| Grounding | Mapping an intended action to a concrete element and browser operation |
| Shadow evaluator | Generator-side model predicting whether a candidate induces login |
| Fuzzing-inspired generation | Iteratively generating, evaluating, and mutating candidate statements |
| MCTS | Monte Carlo Tree Search; the paper uses an inspired seed-selection policy rather than specifying a full algorithm |
| LER | Login Entry Rate: fraction of task instances clicking the forged entry |
| ASR | Attack Success Rate: fraction entering login and then inputting sensitive information |
| PER | Page Exploitability Rate: fraction of pages with at least one success within budget |
| Attempt consumption | Attempts through first success; nine assigned if none succeeds within the budget |
| T; B | User task; background information available to the agent |
| t; s_t; a_t | Time step; current observation; selected action |
| H_t | Ordered previous observation–action pairs |
| w_t; O | Webpage state; observation extraction process |
| h_t; i_t; R | Text/structured content; screenshot; rendering process |
| Π | Abstract policy representing agent and underlying model |
| o_t; r_t; e_t | Operation type; optional argument; optional target element |
| Tilde notation | Injected page, altered observation, or resulting altered action |
| N; K; C | Sampled tasks per page; repeats per task; total attempts N×K |
| δ_c^(w) | Binary success of attempt c on page w |
| e_w; W | Binary page exploitability indicator; evaluated page set |
| HTTP | HyperText Transfer Protocol, used in cloning fallback |
| VLM | Vision-language model; LiteWebAgent is described as a VLM web agent |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Accessible document | 12 | pages | Text pp. 1–12; visual images pp. 1–11 | Directly supplied | Accessibility record |
| Dataset pages | 80 | cloned webpages | Five domains after cloning-related filtering | Author-reported | p. 6, Table 1 |
| Dataset tasks | 1,175 | task instances | Associated with selected pages | Author-reported | p. 6, Table 1 |
| Travel | 24 / 309 | pages / tasks | Dataset domain | Author-reported | p. 6, Table 1 |
| Service | 16 / 281 | pages / tasks | Dataset domain | Author-reported | p. 6, Table 1 |
| Information | 16 / 276 | pages / tasks | Dataset domain | Author-reported | p. 6, Table 1 |
| Shopping | 13 / 173 | pages / tasks | Dataset domain | Author-reported | p. 6, Table 1 |
| Entertainment | 11 / 136 | pages / tasks | Dataset domain | Author-reported | p. 6, Table 1 |
| Backbone comparison mean LER | 93 | % | Browser-Use fixed; four LLM backbones | Author-reported | p. 7, §4.2 |
| Backbone comparison mean ASR | 86 | % | Same comparison | Author-reported | p. 7, §4.2 |
| Difference between these means | 7 | percentage points | 93 − 86; not a conditional leakage probability | Analyst-derived | p. 7 operands |
| Architecture comparison mean ASR | 79 | % | Three architectures; GPT-4o fixed | Author-reported | p. 2 introduction |
| Architecture overall LER range | 84–94 | % | Architecture-level results | Author-reported | p. 9, §4.3 |
| Architecture overall ASR range | 68–89 | % | Architecture-level results | Author-reported | p. 9, §4.3 |
| Interaction budget | 5 | agent steps | All experiments | Author-reported | p. 7, implementation |
| Shadow evaluators | 2 | evaluators | Both must predict login-directed action | Author-reported | p. 6, §3.4 |
| Mutation seed shortlist | 3 | failed candidates | Top-ranked by reward | Author-reported | p. 7, implementation |
| Page-level task sample N | 3 | tasks/page | PER analysis | Author-reported | p. 7 |
| Repetitions K | 3 | runs/task | PER analysis | Author-reported | p. 7 |
| Page-level attempt budget C | 9 | attempts/page | N×K = 3×3 | Author-reported | p. 7 |
| RQ1 PER | 100 | % | Every page, each tested backbone, within nine attempts | Author-reported / visually readable | p. 8, Figure 4 |
| Browser-Use aggregate PER | 100 | % | 80/80 pages; GPT-4o | Analyst-derived | p. 9, Figure 6 |
| LiteWebAgent aggregate PER | 93.75 | % | 75/80 pages; GPT-4o | Analyst-derived | p. 9, Figure 6 |
| Skyvern aggregate PER | 98.75 | % | 79/80 pages; GPT-4o | Analyst-derived | p. 9, Figure 6 |
| Figure 4 displayed attempt range | 1.00–1.55 | mean attempts consumed | Backbone–domain cells | Visually readable | p. 8, Figure 4 |
| Figure 6 displayed attempt range | 1.00–2.54 | mean attempts consumed | Architecture–domain cells | Visually readable | p. 9, Figure 6 |

No exact unlabeled bar heights have been promoted into numerical facts. No confidence interval or significance value is supplied. The introduction's 358.9K domains in a Top 1M measurement is background attributed to cited work [1], not a LoginTrap dataset or result. [A; p. 1]

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Login can be manufactured as a task prerequisite | Popup and destination construction; successful entry and input | Figures 1–2; X1–X4 | pp. 4–9 | HIGH for tested mechanism; no universal claim |
| Actual task and agent internals are excluded from attacker knowledge | Explicit threat-model restrictions | §2.4 | p. 4 | HIGH for stated design; exact prompts not supplied |
| Generation uses page context and model-based filtering | Summary/probe extraction, two evaluators, mutation | §3.4 | p. 6 | HIGH for described method; no ablation |
| Login entry is distinct from sensitive leakage | Separate LER/ASR definitions and gaps | Figure 3; X1 | pp. 6–8 | HIGH; input/submission wording remains qualified |
| Attack effectiveness is not confined to one backbone | Four-backbone comparison; means 93% and 86% | Figures 3–4; X1–X2 | pp. 7–8 | HIGH within Browser-Use and selected dataset |
| Page-level success is widespread | Every Figure 4 page count reaches denominator | Figure 4; X2 | p. 8 | HIGH within nine attempts; not every execution |
| Architecture does not eliminate the observed risk | Three architectures; high entry and leakage | Figures 5–6; X3–X4 | pp. 8–10 | HIGH within GPT-4o conditions |
| Architecture affects continuation reliability | Different ASR and attempt patterns | Figures 5–6 | p. 9 | MEDIUM for explanatory causation; system-level evidence |
| Defenses reduce but do not eliminate leakage | Qualitative conclusion | No detailed defense result supplied | p. 11 | LOW for evaluating efficacy; HIGH that authors state it |
| Agent tools create a relevant harmful action pathway | Observation → action → sensitive form input | Equations (2)–(4), Figures 1–2 | pp. 3–5, 7 | Analyst inference; no standalone comparison |
| Authentication necessity merits explicit checking | Conclusion's proposed defense direction | §6 | p. 11 | Recommendation, not demonstrated sufficient solution |

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an assistant to find information on a website. A fake popup says that the assistant must log in before it can continue. Instead of checking whether your request really needs a login, the assistant accepts the popup's explanation, opens the linked page, and types private information it already knows into a form controlled by the attacker.

The important trick is that the attacker makes the bad step look like part of doing the good task. The first message does not have to demand private information directly. It can establish a believable requirement, then let the next page ask for the information. This is why the researchers count both clicking the fake login and actually entering sensitive data: those are different outcomes.

In the controlled tests, this happened frequently across several language models and browser-agent designs. But the percentages describe selected cloned pages, synthetic private information, and fixed execution budgets. The study does not test a normal text-only chatbot against the same attack, so it cannot tell us exactly how much more vulnerable browser agents are. It does show how reading untrusted pages and taking actions can turn a misleading instruction into an observable privacy leak.

## Completeness Audit

The inventory denominator is the supplied twelve-page document: abstract; §§1–6 including substantive subsections; three contributions; one central question and two evaluation questions; six figures; one table; six numbered equations; four reported quantitative comparison/page analyses; and two mentioned but insufficiently reported analysis topics. All source pages were inspected in text, and all supplied visual pages were inspected visually.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, affiliation, version | Yes | Yes | Represented in compressed form | Longtao Guo, Zelin Zhang, Kaifeng Huang, Yang Shi; Tongji University; arXiv:2608.04741v1, 5 Aug 2026; no publication venue supplied |
| Abstract | Yes | Yes | Fully represented | Threat, method, headline result, implication |
| §1 Introduction | Yes | Yes | Represented in compressed form | Motivation and contributions retained; background citation examples compressed |
| §2 opening | Yes | Yes | Represented in compressed form | Section purpose covered |
| §2.1 Web agents | Yes | Yes | Fully represented | Observation/action loop and architecture differences |
| §2.2 Manipulation | Yes | Yes | Represented in compressed form | Three channels and trust-boundary account retained |
| §2.3 Motivation | Yes | Yes | Fully represented | Three gaps and central question |
| §2.4 Threat model | Yes | Yes | Fully represented | Capabilities, goals, excluded knowledge/control |
| §3 opening | Yes | Yes | Represented in compressed form | Organization reflected in methodology |
| §3.1 Formulation | Yes | Yes | Fully represented | All four equations and action triplet |
| §3.2 Attack overview | Yes | Yes | Fully represented | Prerequisite inducement and sensitive input |
| §3.3 Environment | Yes | Yes | Fully represented | Clone, popup, close button, destination, layout |
| §3.4 Generation | Yes | Yes | Fully represented | Context, initialization, evaluation, seed pool, mutations, missing settings |
| §4 opening / §4.1 | Yes | Yes | Fully represented | Data, metrics, implementation, budgets |
| §4.2 / RQ1 | Yes | Yes | Fully represented | Backbone task outcomes and page analysis |
| §4.3 / RQ2 | Yes | Yes | Fully represented | Architecture task outcomes and page analysis |
| §5 / §5.1 | Yes | Yes | Represented in compressed form | Agent-security categories; no independent citation review |
| §5.2 Credential leakage | Yes | Yes | Represented in compressed form | Earlier login-necessity decision retained |
| §6 Conclusion | Yes | Yes | Fully represented | Main implication and unsupported-detail boundary |
| Central question | Yes | Yes | Fully represented | Actual-task-independent inducement |
| Formal hypotheses | Not present | Absence stated | Not present in supplied material | None manufactured |
| X1–X4 quantitative analyses | Yes | Yes | Fully represented | Conditions kept separate |
| X5 defense experiment | Mentions inspected | Yes | Missing detailed evidence | No numerical efficacy inferred |
| X6 accepted-statement analysis | Mention inspected | Yes | Missing detailed evidence | No acceptance or mutation gains inferred |
| Figures 1–2 | Yes, visually | Yes | Fully represented | Components, arrows, sequence, conceptual limits |
| Figure 3 | Yes, visually | Yes | Represented with uncertainty | Exact unlabeled bars not transcribed |
| Figure 4 | Yes, visually and text | Yes | Fully represented | All annotated cells retained |
| Figure 5 | Yes, visually | Yes | Represented with uncertainty | Exact unlabeled bars not transcribed |
| Figure 6 | Yes, visually and text | Yes | Fully represented | All annotated cells retained |
| Table 1 | Yes | Yes | Fully represented | All values and total check |
| Equations (1)–(6) | Yes | Yes | Fully represented | Definitions, inputs, meaning, limitations |
| Numbered algorithms / pseudocode | Not present | Absence stated | Not present in supplied material | Generation represented procedurally |
| Theorems / proofs | Not present | Absence stated | Not present in supplied material | Not a theoretical paper |
| Three stated contributions | Yes | Yes | Fully represented | Defense component qualified |
| Explicit limitations section | Not present | Absence stated | Not present in supplied material | Stated boundaries separated from analyst observations |
| Appendices | None supplied | Absence stated | Not present in supplied material | No appendix review claimed |
| Supplements / embedded files | None supplied | Absence stated | Not present in supplied material | No supplementary evidence used |
| References [1]–[55] | Yes, as supplied text | Categories represented | Deliberately compressed | Bibliography not reproduced; page 12 text-only |
| Keywords / substantive footnotes | None identified | Absence accounted for | Not identified in supplied material | Decorative labels and correspondence line not expanded |

### Missing or inaccessible material

No missing page is apparent in the supplied 1–12 sequence. Page 12 has no supplied rendering and therefore received text-only inspection. No original PDF binary, code, raw logs, detailed prompt files, dataset release, or supplements were supplied for inspection. Detailed defense and accepted-statement analyses cannot be assessed because the supplied text only mentions them. No unseen supplement is assumed to repair those gaps.

### Uncertain interpretations

Exact individual bar values in Figures 3 and 5 are unavailable as labels. The weighting of reported average rates is unspecified. The relationship between sensitive input and separate form submission is not fully consistent across descriptions. The numerical generation budget, reward function, candidate acceptance yield, and framework/model configuration details are unspecified. Module-level explanations of architecture differences are plausible author interpretations rather than experimentally isolated causes.

### Deliberately compressed material

Repeated descriptions of the same login-first mechanism across the abstract, introduction, diagram captions, discussion, and conclusion are consolidated. Individual bibliographic entries and repeated prior-work examples are compressed into the authors' thematic categories; cited works were not independently read. Decorative icons, email formatting, publication-margin text, and non-substantive typography are not reproduced. Both heatmaps' numerical annotations are retained because they add evidence beyond the headline means.

### Potential omissions

No known substantive item from the available inventory is left wholly unrepresented. This coverage statement is bounded by the supplied document and the explicit uncertainties above; it does not certify absent experimental detail, verify external citations, establish independent reproducibility, or convert the paper into a direct standalone-LLM comparison.
