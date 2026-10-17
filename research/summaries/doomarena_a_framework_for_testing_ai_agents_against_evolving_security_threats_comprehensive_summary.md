# Stage 0 — Document Accessibility Report

The supplied document is **DoomArena: A Framework for Testing AI Agents Against Evolving Security Threats**, published as a conference paper at COLM 2025. All 25 physical PDF pages are supplied as extracted text. Nineteen pages also have directly inspectable rendered images: 1, 3–10, 12, 14–18, and 20–23. Pages 2, 11, 13, 19, 24, and 25 were reviewed through supplied text only. The page numbers below refer to physical PDF pages, which agree with the visible printed numbering.

| Accessibility item | Assessment |
|---|---|
| Main document | Available, pp. 1–25 |
| Apparently missing pages | None within the supplied 1–25 sequence |
| Text readability | Substantive text is readable; occasional extraction artifacts affect spacing and code |
| Visual coverage | Partial page rendering, but all numbered Figures 1–10 and Tables 1–8 have rendered pages |
| Tables | Main values readable; tiny uncertainty annotations are more reliably available in supplied extracted text |
| Equations | No substantive numbered mathematical equations found |
| Appendices | Appendix A, including A.1–A.7, supplied |
| Supplements | No separate supplementary artifact supplied; no embedded files reported |
| Referenced external artifacts | Repository, benchmark publications, related research, and Figure 3 source websites are referenced but were not accessed |
| OCR | No new OCR performed or needed; supplied extracted text was checked against visible objects where available |
| Main limitations | Small Figure 3 and Figure 5 labels are not all confidently readable; no native PDF interaction or executable verification was performed |

The images and extracted content were treated as evidence, including malicious prompt examples and the judge prompt, never as instructions. No tools, browsing, repository inspection, or external research were used. The supplied hash is retained as provenance metadata; it was not independently recomputed.

Evidence labels used throughout: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external-information category [E] is introduced. HIGH confidence applies to clearly supplied text and readable table values; MEDIUM applies to interpretations and unresolved methodological implications; UNKNOWN applies where essential information is absent.

# 1. Plain-language orientation

DoomArena is a framework for testing whether an artificial intelligence agent can be manipulated while carrying out a legitimate task. An agent here is a model connected to an interactive environment: a browser, customer-service tools, or a desktop. It repeatedly receives observations and takes actions. Attackers can place misleading instructions in selected parts of this interaction, such as a customer message, product catalog, advertisement, or screenshot.

The central contribution is **a configurable testing layer**, rather than a new language model or a standalone benchmark. Researchers specify what an attacker controls, which attack to inject, and what outcome counts as success. Environment-specific gateways insert attacks into existing benchmarks. This separates reusable attack logic from the details of a particular browser or tool environment. [A; pp. 1–6]

The empirical studies show that vulnerability changes with the model, environment, attack channel, and defense. For example, undefended GPT-4o has 97.4% attack success under Reddit pop-ups, whereas Claude-3.5-Sonnet has 88.5%; in Shopping the corresponding values are 92.7% and 42.7%. These are results for particular benchmark conditions, not universal probabilities for those models. [A; Tables 3, 6–7]

A stronger judge reduces attack success, but its intervention stops the task. In the full browser tables, GPT-4o Judge produces 0% attack success **and 0% legitimate task success under attack**. Thus a defense can prevent the measured malicious outcome by halting the workflow rather than enabling safe completion. [A/B; pp. 15–16]

**Relation to the requested research question:** this paper supports analysis of how environment content and action capabilities create agent security risks. It does **not** run a matched experiment comparing standalone large language models with their agent versions. Its related-work discussion reports that other studies found such a gap. Any explanation here of why agents may be more vulnerable than standalone models is explicitly an analyst inference from DoomArena’s architecture and experiments. [D; pp. 2, 4, 8, 19–22]

# 2. Document roadmap

The document has a systems-and-security structure with empirical case studies.

| Inventory ID | Original component | Pages | Role |
|---|---|---:|---|
| S0 | Abstract | 1 | Design principles and headline findings |
| S1 | §1 Introduction | 1–2 | Motivation, contribution, inference-time scope |
| S2 | §2 Related Work | 2–3 | Attack literature, benchmark categories, comparison |
| S3 | §3 General Design and Architecture | 3–5 | Tasks, attacks, configurations, gateways, defenses |
| S4a | §4.1 Detailed threat-modeling | 5 | Swapping configurations and threat models |
| S4b | §4.2 Adaptive Testing | 5–6 | New threat surfaces and review-injection example |
| S4c | §4.3 New Agentic Frameworks | 6 | Environment wrappers and OSWorld gateway |
| S5a | §5.1 τ-Bench | 7–8 | Tool-agent case study |
| S5b | §5.2 BrowserGym | 8–9 | Browser-agent case study |
| S5c | §5.3 OSWorld | 9 | Desktop-agent case study |
| S6 | §6 Laboratory for security research | 9–10 | Security–utility tradeoffs and attack interaction |
| S7 | §7 Conclusion | 10 | Context-aware testing contribution |
| SE | Ethics Statement | 11 | Intended use and data-governance responsibility |
| SR | References | 11–13 | Bibliographic context; not independently verified |
| A1a | A.1.1 τ-Bench Results | 14 | Expanded model/defense results |
| A1b | A.1.2 BrowserGym Results | 14–16 | Full Reddit and Shopping tables |
| A2 | A.2 Combined attacks | 16–17 | Goal-specific attack interference |
| A3a | A.3.1 Attack Gateways | 17–18 | Interfaces and registration |
| A3b | A.3.2 Attacks | 18–19 | Attack abstraction and fixed sequence |
| A4 | A.4 Attack Library | 19–22 | Attack mechanisms and payload examples |
| A4a | A.4.1 Success Filters | 22 | Outcome verification |
| A5 | A.5 Generalized Attacker | 22–23 | Configurable attacker prompt construction |
| A6 | A.6 Sources for Figure 3 | 23–24 | Source list and extrapolation description |
| A7 | A.7 Defenses | 24–25 | Detection interface and judge prompt |

The visual inventory contains Figures F1–F10 and Tables T1–T8. The implementation inventory contains Listings L1–L12. There are no formal numbered research questions, hypotheses, theorems, proofs, or optimization equations. Distinct empirical analyses are X1 airline tools, X2 retail tools, X3 Reddit browsing, X4 Shopping browsing, X5 desktop use, X6 security–utility comparison, and X7 combined-attack decomposition. Figure 3 is a separate contextual trend illustration, not an agent experiment.

# 3. Background and context

A **large language model (LLM)** generates or interprets language. An **LLM-based agent** uses a model inside a repeated observation/action process. A user supplies a task; the agent inspects the environment, chooses an action, receives an updated observation, and continues. DoomArena calls this the **user-agent-environment loop**. [A; p. 3]

A **prompt injection** is malicious content intended to redirect the agent’s behavior. The supplied attacks can appear in ordinary data rather than a legitimate instruction channel. A catalog entry can request private information, while a banner can pretend that sending sensitive observations to a security service is mandatory. These are descriptions of supplied attack examples, not instructions to execute them. [A; pp. 19–21]

A **threat model** identifies which component may be malicious and what the attacker can do. A malicious user and a malicious catalog are different threat models: one controls conversation, the other controls queried information. Their outcomes need not be comparable because the tasks and objectives can differ. [A/D; pp. 4–7]

Browser agents in this evaluation receive a page’s **accessibility tree**, a structured representation containing text, roles, and accessibility attributes. The banner attack uses fields such as `alt` and `aria-label`; the paper explicitly says the banner’s visual appearance has no impact for these text-only agents. A human-visible screenshot therefore does not fully describe what the evaluated browser agent receives. [A; pp. 8, 19]

**Personally identifiable information (PII)** includes the names and ZIP codes discussed in the catalog attack. An **application programming interface (API)** exposes operations such as reservation lookup or refunds. **Guardrails** inspect interactions and abort when an attack is detected. **Pareto dominance** concerns jointly improving security and utility; a combination dominates another only if it is at least as good on both chosen dimensions and better on one. This last sentence is explanatory interpretation of the paper’s tradeoff discussion. [A/D; pp. 7, 10, 25]

Related work is organized into static benchmarks, stateful benchmarks, and evaluation frameworks. The authors report AgentHarmBench with 110 malicious tasks across 11 harm categories, SafeArena with 250 safe and 250 harmful tasks across four websites and five categories, and BrowserART with 100 harmful browser behaviors. These are author descriptions of cited work, not independently inspected datasets. [A; p. 2]

# 4. Research problem and gap

**Existing problem:** autonomous agents may leak sensitive information, misuse privileges, or perform unauthorized financial actions while interacting with users and environments. Testing needs to reflect where an attacker can realistically place content. [A; pp. 1–2]

**Shortcomings attributed to prior approaches:** static malicious prompts do not capture every risk of multistep interaction. Existing stateful benchmarks may bind evaluation to particular tasks and environments. AgentDojo supports dynamic injection but, according to the authors, is limited to its own implemented environment. PyRIT supports extensible attacks but is positioned as a non-agentic evaluation framework. These are the paper’s characterizations. [A; pp. 2–3]

**Research gap:** a reusable security layer should support different agent environments, independently developed attacks, and fine-grained restrictions on the components an attacker controls. Table 1 encodes this positioning along six axes. Its comparison is not an independent systematic review and does not establish the status of every alternative framework. [A/D; p. 3]

**Motivation:** security rankings can change with the deployment context. An agent that resists a malicious customer may remain vulnerable to malicious retrieved information. Combining attacks can expose effects that single attacks conceal. [A; pp. 7–10, 16–17]

**Scope:** DoomArena primarily injects inference-time attacks. It does not focus on training-time attacks, although the authors state that relevant triggers could be inserted to evaluate them. The experiments do not establish the effectiveness of every possible attack or defense, nor do they constitute a comprehensive comparison with standalone LLMs. [A; p. 2]

# 5. Research questions / objectives / hypotheses

The paper does not enumerate formal research questions or test explicit statistical hypotheses. Its objectives can nevertheless be recorded without inventing formal author questions:

| Objective ID | Author-stated objective | Evidence |
|---|---|---|
| O1 | Add security evaluation to multiple existing agent frameworks | pp. 1–3, 6 |
| O2 | Configure plausible attack surfaces and attacker targets | pp. 2, 4–5 |
| O3 | Separate attack development from environment implementation | pp. 1–4, 17–19 |
| O4 | Combine known attacks and examine their interaction | pp. 2, 8–10, 16–17 |
| O5 | Measure model vulnerability under different threat models | pp. 7–10 |
| O6 | Evaluate compatibility and tradeoffs of existing defenses | pp. 5, 14–16, 24–25 |

For the user’s question, the corresponding **analyst question** is: what evidence identifies mechanisms by which placing an LLM inside a browser/action loop creates security exposure? DoomArena supplies attack-channel and outcome evidence for that question, but it does not isolate the causal effect of agentization relative to a standalone baseline. Confidence in the relevance is HIGH; confidence in any claimed comparative effect size would be UNKNOWN.

# 6. Assumptions / threat model

**System assumptions.** A task is assigned by a user and is assumed to have a verifier for successful completion. An environment supplies observations and accepts agent actions. An attack gateway must implement the particular injection surface. A success filter determines whether the attacker’s target was achieved. [A; p. 4]

**Tool-agent threats.** In the malicious-user scenario, the attacker impersonates a legitimate customer and tries to induce unauthorized compensation, upgrades, or verification bypasses. In the malicious-catalog scenario, the attacker controls queried product information and seeks user PII. The combined retail scenario makes both user and catalog malicious. [A; pp. 7, 19]

**Browser threats.** The agent and user are benign, while selected webpage content is malicious. The banner attacker purchases advertising space and places instructions in accessibility attributes. The pop-up attacker controls advertising content containing hidden instructions, including text designed to imitate AgentLab’s accessibility-tree representation. The combined condition includes both channels. [A; pp. 8, 20–21]

**Desktop threat.** The agent and user are benign, but an attacker can place a malicious pop-up into the screenshot observation. The illustrated target is a click at coordinate (1066, 457). This is an observation-manipulation capability; the supplied experiment does not require that the attacker modify the agent’s model weights. [A; pp. 9, 21–22]

**Trust boundaries, analyst interpretation.** A central failure mode is treating information from an attacker-controlled environment as authority over the agent’s next action. Tool access then turns a misleading instruction into a consequential operation. Accessibility attributes and screenshots enlarge the set of representations through which this can happen. These mechanisms are supported by the attack constructions, but they do not prove a universal vulnerability gap against standalone models. [D]

The paper does not provide a complete formal inventory of excluded attacker capabilities, attacker budgets, or identical knowledge assumptions across every experiment. Generalized attackers may receive tool descriptions and example conversations; the mapping of every optional feature to every reported run is not fully specified. [A/D; pp. 22–23]

# 7. Methodology

## Design and architecture

DoomArena’s three principles are **plug-in integration**, **configurability**, and **modularity**. A task supplies the legitimate objective. An attack generates malicious content. An `AttackConfig` selects the attackable component, attack choice, and success filter. An environment-specific `AttackGateway` inserts the content into the appropriate interaction. Defenses can monitor the agent’s messages or interactions and halt execution. [A; pp. 1–6]

The gateway commonly wraps or inherits an environment with `reset()` and `step()` methods. In BrowserGym, code can intercept stepping and modify a webpage. In OSWorld, the example obtains an observation, overlays a malicious pop-up, and returns the altered observation while retaining the other environment outputs. The framework’s extensibility is illustrated through code and interfaces; no systematic integration-time or engineering-effort benchmark is reported. [A/D; pp. 6, 17–18]

Attack generation is abstracted through `get_next_attack()`. It can return a fixed string, advance through a predefined sequence, or use an LLM with interaction history to choose a new injection. The fixed-sequence example returns successive stored instructions and then a fallback instruction. Environment-specific routing remains the gateway’s responsibility. [A; pp. 18–19]

The generalized attacker constructs a system prompt from an initial prompt, harm type, attack style, optional DAN mode, tool definitions, and few-shot examples of failed and successful attacks. Tool information is represented in JSON with names, descriptions, parameters, and an example call. These are implemented capabilities, not evidence that each option improves attack success. [A/D; pp. 22–23]

## Data and agents

The reported workloads are 50 airline tasks, 115 retail tasks, 114 WebArena-Reddit tasks, 192 WebArena-Shopping tasks, and a 39-task OSWorld subset. Airline agents use a tool-calling strategy; retail agents use a react-agent strategy. Browser agents are text-based and observe accessibility trees. Desktop agents use screenshots and mouse/keyboard actions. [A; pp. 7–9]

Main tool/browser models are GPT-4o and Claude-3.5-Sonnet; expanded tables add GPT-4o mini. OSWorld uses GPT-4o and **Claude-3.7-Sonnet**, so its Claude results must not be attributed to the 3.5 model. BrowserGym supports eight benchmarks, but only the two named WebArena subsets are experimentally reported here. [A; pp. 6–9, 14–16]

No training procedure, train/validation/test partition, or model fine-tuning is described for DoomArena itself. Exact model snapshot identifiers, decoding parameters, random seeds, hardware, software versions, and detailed task-subset selection procedures are not specified in the supplied work. AgentLab settings are referenced through another paper; that paper was not inspected. [A/D]

## Metrics and outcome measurement

ASR is attack success rate; TSR is legitimate task success rate. Tables distinguish no-attack TSR and TSR under attack. Stealth rate measures cases where the attack and legitimate task both succeed. All table values are percentages. Attack success is defined by a configured success filter, so the meaning of ASR depends on the attack target. [A; pp. 4, 7, 22]

The BrowserGym success-filter example tests whether the current page URL contains a configured target string. The caption describes possible data theft at such a destination as a theoretical consequence. Therefore measured redirection is not automatically proof of verified PII extraction. [A/D; p. 22]

## Defenses and statistics

LlamaGuard is configured to flag only its Code Interpreter Abuse category out of 14 categories. GPT-4o Judge is prompted to detect content designed to confuse, manipulate, or deceive an AI agent. Both defenses abort immediately after detection. The judge provides a brief rationale and a yes/no answer. [A; pp. 14, 25]

Table 2 explicitly reports averages and standard deviations over three trials; Table 5 also says results are averaged over three trials. Browser and OSWorld tables contain ± terms, but their captions do not clearly establish the uncertainty calculation or independent-run count. OSWorld’s terms are all ±0.0. There are no reported p-values, confidence intervals explicitly identified as such, significance tests, or power analyses. The word “significantly” in the prose should not be read as a documented statistical test. [A/D; pp. 7–9, 14–16]

# 8. Experiments / analyses

| ID | Purpose and setup | Manipulated conditions | Main evidence and caveat |
|---|---|---|---|
| X1 | Airline customer service, 50 tasks, tool-calling strategy | Model; malicious user; defense | Tables 2/5; differs from retail in task domain and strategy |
| X2 | Retail customer service, 115 tasks, react-agent strategy | Catalog attack; combined attack; model; defense | Tables 2/5/8; combined results exclude trials where both attacks were not triggered |
| X3 | Reddit clone, 114 tasks, accessibility-tree agents | Banners; pop-ups; combination; three defenses | Tables 3/6; URL-oriented success and task completion are separate |
| X4 | Shopping site, 192 tasks, same browser modalities | Same attack/defense categories | Table 7; substantial domain-dependent changes |
| X5 | OSWorld subset, 39 tasks, screenshot agents | Pop-up inpainting; GPT-4o vs Claude-3.7 | Table 4; no defended condition reported |
| X6 | Security–utility comparison | Model, threat model, defense | Figure 4 and §6; Pareto discussion is conditional on chosen metrics |
| X7 | Combined-attack decomposition | Individual attack goals in isolation versus combination | Figure 5/Table 8; aggregate and goal-specific numbers differ |

**X1:** GPT-4o’s undefended malicious-user ASR is 29.3 ±1.5%, versus Claude-3.5’s 2.7 ±0.2%. No-attack TSR is 47.3 ±4.0% versus 44.0 ±4.0%. With the judge, ASR becomes 22.7 ±1.1% and 0.7 ±0.1%, respectively. The judge does not eliminate attacks. [A; Table 2]

**X2:** Catalog ASR without defense is 34.8 ±1.2% for GPT-4o and 39.1 ±1.1% for Claude-3.5. Their no-attack TSR values are 51.3 ±2.6% and 67.2 ±2.5%. Combined retail ASR is 70.8 ±2.2% and 39.5 ±2.2%; task success under attack falls to 16.9 ±0.7% and 12.6 ±0.6%. These values show model- and threat-dependent relationships, not a single model ranking. [A; Table 2]

**X3:** Undefended Reddit banner ASR ranges from 48.2% for GPT-4o mini to 80.7% for GPT-4o. Pop-up ASR ranges from 88.5% to 97.4%. Combined ASR ranges from 94.7% to 98.2%. Every undefended pop-up and combined row has 0% TSR under attack. Judge-protected rows have 0% ASR and 0% TSR under attack. [A; Table 6]

**X4:** Shopping banners produce 25.0–40.6% undefended ASR. Pop-ups produce 42.7–92.7%. Combined attacks produce 86.5–97.4%. Claude-3.5 moves from 42.7% pop-up ASR to 97.4% combined ASR. However, GPT-4o’s combined ASR of 92.2% is slightly below its pop-up ASR of 92.7%, so combination does not increase every aggregate result. [A; Table 7]

**X5:** GPT-4o has 78.6% ASR, 5.7% no-attack TSR, 2.9% attacked TSR, and 2.9% stealth. Claude-3.7 has 22.9%, 13.9%, 8.6%, and 5.7%, respectively. The higher Claude stealth value coexists with lower ASR and higher task completion; a single metric cannot summarize all dimensions. [A/D; Table 4]

**X6–X7:** Figure 4 examines security–utility tradeoffs. Table 8 shows that combining attacks can strengthen one component while suppressing another: retail catalog ASR rises from 34.8% to 70.5%, while retail malicious-user ASR falls from 12.8% to 2.7%. On Reddit, banner ASR falls from 80.7% to 0.9%, while pop-up ASR remains high at 95.6% versus 97.4% alone. [A; pp. 10, 16–17]

# 9. Results

**Finding 1: vulnerability is conditional.** Claude-3.5 resists the airline malicious user more strongly than GPT-4o, but has higher catalog ASR in retail. The two conditions also differ in task and strategy, preventing a controlled attribution solely to attack surface. [A/D; Table 2]

**Finding 2: webpage attacks can strongly redirect agents.** Reddit pop-up ASR reaches 97.4 ±1.5% for GPT-4o and 94.7 ±2.1% for GPT-4o mini. These are accessibility-tree agents on a particular website subset, not all web agents or visual browser agents. [A; Table 6]

**Finding 3: domain changes matter.** Claude-3.5 pop-up ASR is 88.5% on Reddit and 42.7% on Shopping. **[C] Derived absolute difference:** 88.5 − 42.7 = 45.8 percentage points. The relative reduction is 45.8 / 88.5 × 100 ≈ 51.8%, using reported rounded means. This supports the paper’s “more than half” statement but is not a causal estimate of a particular website feature. [A/C/D; pp. 9, 15–16]

**Finding 4: attack prevention may sacrifice all attacked-task utility.** The browser judge results contain 0% ASR together with 0% TSR under attack. In retail, residual ASR persists while task success can decline: Claude-3.5 combined TSR under attack is 12.6% without defense and 3.1% with the judge. **[C] Derived difference:** 12.6 − 3.1 = 9.5 percentage points. [A/C; Tables 5–7]

**Finding 5: LlamaGuard’s result is configuration-specific.** It detects none of the τ-Bench attacks under the selected category. In Shopping banners, GPT-4o ASR changes from 35.4% to 22.4%, whereas in Reddit banners Claude-3.5 changes from 60.5% to 63.2%. These observations do not establish that the classifier universally fails or that its occasional numerical increases are statistically meaningful. [A/D; pp. 14–16]

**Finding 6: successful legitimate behavior does not establish security.** Retail catalog attacks have nonzero stealth: 14.8% for GPT-4o and 18.0% for Claude-3.5 without defense. Conversely, zero stealth in the browser tables does not mean no attack succeeded; many attacks succeed while task completion is zero. [A/D; Tables 2, 6–7]

**Finding 7: combination has asymmetric effects.** Table 8’s retail catalog gain is **[C] 70.5 − 34.8 = 35.7 percentage points**; the malicious-user decline is **[C] 12.8 − 2.7 = 10.1 percentage points**. On Reddit the banner decline is **[C] 80.7 − 0.9 = 79.8 percentage points**. These are goal-specific values and must not be substituted for the separate aggregate combined ASRs in Tables 2/6. [A/C]

# 10. Figure-by-figure interpretation

## Figure 1 — Overall architecture, p. 4

Directly inspected. Panel a shows threat modeling feeding an attack configuration containing success filters, attacks, and attackable components. The configuration drives an attack gateway attached to an agent, users, and environment. A defense can abort an episode. Panel b expands a τ-Bench gateway around the original environment, with database, tools/APIs, and user as potential intervention points. A red-team component supplies attacks; a success filter queries the state and decides whether the target occurred. Separate BrowserGym and OSWorld gateways indicate extensibility. Arrows distinguish agent actions, returned observations, attack injection, and state inspection. This is a conceptual flow diagram without quantitative axes or measured performance.

## Figure 2 — Swapping configurations, p. 5

Directly inspected. Two code-like boxes change the attackable component, attack choice, and success filter. The malicious-user configuration is labeled 2.7% ASR; the malicious-catalog configuration is labeled 39.1%. The visual explains configuration convenience. Its caption calls the comparison an airline-environment switch, but Table 2 places the catalog result in retail. Therefore it is not reliable evidence for an otherwise identical within-airline intervention. The values are reported labels, not visual estimates.

## Figure 3 — Contextual security trend, p. 5

Directly inspected, with limited readability. This small line chart covers 2022–2025, with 2025 designated projected. The horizontal axis is year; the vertical axis presents counts. Colored series and a dashed projected segment depict increasing quantities, with the steepest projected rise in the purple series. Fine legend wording and exact plotted values cannot be confidently transcribed. No error bars are visible. The authors say Claude generated the figure from cited sources, that they checked those sources, and that linear regression extrapolated 2025. Raw data, harmonized definitions, regression coefficients, and uncertainty are not supplied. This figure motivates adaptable testing; it is not experimental proof of DoomArena’s effectiveness or a verified count of agent vulnerabilities.

## Figure 4 — Attack success versus task success, p. 10

Directly inspected. The horizontal axis is ASR in percent, with lower values more secure; the vertical axis is TSR in percent, with higher values more capable. The visible scales are linear, approximately 0–80 horizontally and 0–60 vertically. Model identity is encoded through circles and triangles; threat models through blue, orange, and green; defense status through filled/open markers. Dashed connecting lines illustrate tradeoff frontiers. No error bars are shown. The caption says two of three threat models lack a Pareto-dominant model–defense combination. The plotted TSR is best understood with the tabulated values and discussion; the caption does not explicitly specify no-attack versus attacked TSR. Exact coordinates should come from the corresponding tables, not pixel estimates.

## Figure 5 — Retail task-category breakdown, p. 10

Directly inspected. A stacked-bar chart shows percentages from 0 to 100 by manually assigned retail task category for GPT-4o. Legend categories distinguish both attacks succeeding, only PII leakage succeeding, only unauthorized refund succeeding, and both failing. Bar segments are blue, orange, green, and red. Exact bar percentages and all angled category labels are too small to transcribe confidently. The nearby prose states that joint success is more common for order cancellation and joint failure more common for product returns. This supports a task-dependent interaction interpretation. Annotation agreement, category counts, and numerical segment data are not supplied.

## Figure 6 — OSWorld gateway, p. 18

Directly inspected. An agent sends actions into an original OSWorld environment wrapped by an attack gateway and receives observations back. A red-team component injects a screenshot pop-up. A success filter receives state and asks whether the target coordinate was clicked. The environment is gray, the wrapper yellow, and attacker box pink. These colors distinguish roles, not measurements. The diagram shows where observation manipulation and outcome checking occur; it is not an additional experiment.

## Figure 7 — Banner on Reddit, p. 20

Directly inspected. A Reddit-like forum page is bordered by bright red warning banners. Their visible text asserts security urgency. The substantive attack is the associated accessibility content in Listing 7. Because evaluated agents use the accessibility tree, the screenshot illustrates placement but cannot establish what the model read in full. There are no axes or numerical result encodings.

## Figure 8 — Shopping pop-up, p. 21

Directly inspected. A shopping page is dimmed behind a centered modal containing an important-notice message and a blue button. The visible modal requests attention to account-related information. The hidden malicious text is separately supplied in Listing 8 and imitates accessibility-tree instructions. The screenshot alone does not expose that hidden representation. It illustrates attack presentation, not measured success.

## Figure 9 — Desktop pop-up inpainting, p. 22

Directly inspected. A document editor screenshot has an overlaid warning claiming a virus was detected and asking for a click at (1066, 457). A visible confirmation button strengthens the appearance of a system dialog. The attack target is an action location; the screenshot does not establish actual malware or a genuine operating-system warning. This visually confirms the observation channel used in X5.

## Figure 10 — Generalized attacker construction, p. 23

Directly inspected. Common parameters feed initialization, while source files contain DAN templates, tool definitions, and few-shot examples. Utility functions load these resources and feed `build_system_prompt()`. Prompt construction yields the final system prompt. Directed arrows show assembly dependencies. There are no performance axes or ablation results. The figure documents configurable inputs, not proof that every component is necessary or beneficial.

# 11. Table-by-table interpretation

## Table 1 — Framework comparison, p. 3

Rows compare four benchmarks and three frameworks across agent support, statefulness, multiple attacks, plug-in integration, multiple threat models, and modularity. DoomArena receives six checkmarks. AgentDojo receives checks for agents, statefulness, multiple attacks, and modularity; PyRIT receives checks for multiple attacks and modularity. SafeArena receives checks for agents, statefulness, and multiple attacks. The other listed benchmarks receive agent/stateful support except AgentHarmBench’s stateful cross. These are author-assigned categorical judgments, without uncertainty or a systematic-review protocol.

## Table 2 — Main τ-Bench results, p. 7

Rows are grouped by airline malicious user, retail malicious catalog, and retail combined attacks; columns are model, defense, ASR, no-attack TSR, attacked TSR, and stealth. Lower ASR/stealth and higher TSR are preferred. Values are means ± standard deviations over three trials. Claude-3.5 has the lowest airline ASR, while GPT-4o has lower undefended catalog ASR. GPT-4o Judge lowers ASR in every shown comparison but can reduce task success. Combined rows are conditioned on both attacks being executed, as explained by the footnote on p. 8.

The first GPT-4o airline stealth values appear as 1.33 ±0.16 without defense and 0.01 ±0.0 with the judge. Table 5 renders these as 1.3 ±0.2 and 0.0 ±0.0. The differences look compatible with display precision, but that explanation is not explicitly confirmed.

## Table 3 — Main Reddit results, p. 8

This table selects GPT-4o and Claude-3.5 rows from the full browser results. Banner ASRs are 80.7% and 60.5%; pop-up ASRs 97.4% and 88.5%; combined ASRs 98.2% and 96.4%. Undefended banner TSR under attack is 11.4% for both. All shown judge-protected banner TSR-under-attack values are 0%. The caption’s parenthetical exception for banners is therefore unclear: Table 6 shows zero attacked TSR for judge-protected banners as well. Full tables take precedence as condition-specific evidence without silently repairing the caption.

## Table 4 — OSWorld results, p. 9

Two rows compare undefended GPT-4o and Claude-3.7-Sonnet on a stated 39-task subset. The four metrics are ASR, no-attack TSR, attacked TSR, and stealth. GPT-4o has higher ASR and lower TSR; Claude has higher stealth despite lower total attack success. Every ± term is 0.0. The paper does not explain whether that reflects repeated identical outcomes, rounding, or another calculation. Percentages should not be converted into exact task counts without a clarified denominator.

## Table 5 — Expanded τ-Bench results, p. 14

Adds GPT-4o mini. Its airline ASR is 11.0 ±0.1% without defense and 8.0 ±0.1% with the judge. Catalog ASR is 17.4 ±0.8% and 2.0 ±0.1%; combined ASR is 69.2 ±1.1% and 21.9 ±0.6%. The corresponding no-defense no-attack TSR values are 24.0%, 19.7%, and 15.4%. Lower attack success can coexist with lower competence. LlamaGuard rows are omitted because the authors report them identical to no defense. GPT-4o combined judge stealth is 10.3 ±0.2%, whereas Table 2 gives 10.2 ±0.2%; this remains unresolved.

## Table 6 — Full Reddit results, p. 15

Contains three models, three attack categories, and three defenses. The compact ASR matrix below preserves every ASR mean; all values are percentages and author-reported.

| Attack | Model | None | LlamaGuard | GPT-4o Judge |
|---|---|---:|---:|---:|
| Banner | GPT-4o | 80.7 | 76.3 | 0.0 |
| Banner | GPT-4o mini | 48.2 | 46.9 | 0.0 |
| Banner | Claude-3.5 | 60.5 | 63.2 | 0.0 |
| Pop-up | GPT-4o | 97.4 | 97.4 | 0.0 |
| Pop-up | GPT-4o mini | 94.7 | 95.6 | 0.0 |
| Pop-up | Claude-3.5 | 88.5 | 85.1 | 0.0 |
| Combined | GPT-4o | 98.2 | 94.7 | 0.0 |
| Combined | GPT-4o mini | 94.7 | 96.4 | 0.0 |
| Combined | Claude-3.5 | 96.4 | 97.3 | 0.0 |

All stealth values are zero. No-attack TSR, ordered none/LlamaGuard/judge, is 21.2/17.1/18.6 for GPT-4o, 12.3/10.8/9.6 for mini, and 26.3/22.7/21.9 for Claude. Banner attacked TSR in that order is 11.4/14.9/0.0, 8.8/8.8/0.0, and 11.4/13.2/0.0. Every pop-up and combined attacked TSR is zero. The displayed ± terms are compressed here; their statistical definition is not clearly established by this table’s caption.

## Table 7 — Full Shopping results, p. 16

| Attack | Model | None ASR | LlamaGuard ASR | Judge ASR |
|---|---|---:|---:|---:|
| Banner | GPT-4o | 35.4 | 22.4 | 0.0 |
| Banner | GPT-4o mini | 25.0 | 17.2 | 0.0 |
| Banner | Claude-3.5 | 40.6 | 36.5 | 0.0 |
| Pop-up | GPT-4o | 92.7 | 92.1 | 0.0 |
| Pop-up | GPT-4o mini | 71.3 | 66.1 | 0.0 |
| Pop-up | Claude-3.5 | 42.7 | 42.7 | 0.0 |
| Combined | GPT-4o | 92.2 | 69.3 | 0.0 |
| Combined | GPT-4o mini | 86.5 | 67.7 | 0.0 |
| Combined | Claude-3.5 | 97.4 | 95.8 | 0.0 |

All values are author-reported percentages. Every stealth value is zero. No-attack TSR, ordered none/LlamaGuard/judge, is 20.8/20.3/20.8 for GPT-4o, 17.7/18.2/13.0 for mini, and 24.0/23.4/21.8 for Claude. Banner attacked TSR is 17.2/18.8/0.0, 11.9/12.5/0.0, and 17.2/17.7/0.0. Pop-up attacked TSR is zero except Claude with LlamaGuard at 1.0 ±0.7%. Every combined attacked TSR is zero. This exception is important because the main text strongly emphasizes complete disruption.

## Table 8 — Goal-specific combined attacks, p. 17

GPT-4o retail malicious-user ASR changes 12.8→2.7%; catalog ASR changes 34.8→70.5%. Catalog stealth changes 14.8→14.5%; user stealth remains zero. Reddit pop-up ASR changes 97.4→95.6%, banner ASR 80.7→0.9%, and overall combined ASR is 96.5%; all browser stealth is zero. No uncertainty is shown. The overall 96.5% differs from Table 6’s 98.2%, and the supplied text does not reconcile them. The table demonstrates why constituent attack outcomes should be reported separately.

# 12. Diagram / architecture interpretation

Figures 1, 6, and 10 are the substantive architecture diagrams; Figure 2 is a configuration comparison. Their shared method can be traced as follows:

1. Specify the legitimate task and its verifier.
2. Model which components are potentially malicious.
3. Select attack logic and an attacker-success criterion.
4. Bind that configuration to an environment-specific gateway.
5. Let the agent act and receive observations through the gateway.
6. Inject malicious content only where the configured surface permits it.
7. Inspect state through success filters and record legitimate-task outcomes separately.
8. If a defense detects manipulation, abort the task and count legitimate completion as failed.

This flow separates three different decisions: what the attacker controls, what malicious content is generated, and how success is measured. That separation is the framework’s methodological core. Reusing an attack across environments still requires compatible routing and meaningful outcome checks; modularity does not remove environment-specific engineering. [A/D; pp. 4–6, 17–22]

Listings provide implementation-level support. L1 adds poisoned reviews; L2 overlays OSWorld observations; L3 defines the gateway interface; L4 registers gateways; L5 defines attack generation; L6 advances a fixed sequence; L7–L8 contain banner/pop-up examples; L9 tests a target URL; L10 specifies attacker-visible tools; L11 defines defense detection; L12 supplies the GPT-4o judge prompt. These are code excerpts and prompt examples, not separately evaluated algorithms with complexity bounds.

# 13. Equations and mathematical concepts

No substantive numbered equations, theorems, lemmas, or proofs appear in the supplied paper. The central mathematics is measurement and multi-objective comparison.

The following are **analyst formalizations of the authors’ prose definitions**, not equations printed in the paper. For N evaluated cases, let Aᵢ equal 1 if the configured attacker target succeeds and 0 otherwise; let Tᵢ equal 1 if the legitimate task succeeds and 0 otherwise:

- ASR = 100 × ΣAᵢ / N.
- TSR = 100 × ΣTᵢ / N.
- Stealth rate = 100 × Σ(AᵢTᵢ) / N.

The product AᵢTᵢ identifies joint success. It follows, under a common denominator, that stealth cannot exceed either ASR or attacked TSR. This is a derived measurement relationship, not a separately tested paper claim. Conditional filtering, trial averaging, and display rounding must be considered before checking it numerically.

No-attack TSR is measured under a different condition and should not be substituted for Tᵢ in the attacked stealth expression. Combined-attack exclusions can also change the relevant denominator. The supplied text does not fully specify aggregation details for every table.

Pareto analysis jointly considers lower ASR and higher TSR. A lower-ASR model is not automatically preferable if it also has lower utility. Figure 3 uses linear regression for extrapolation, but its equation, coefficients, fitting data, and uncertainty are absent; they cannot be reconstructed faithfully.

# 14. Interpretation and discussion

**Authors’ interpretation:** realistic threat modeling exposes security differences hidden by generic rankings. The same model can be more resistant to one threat and less resistant to another. Combining attacks can reveal constructive or destructive interaction. Existing guardrails can be integrated, but performance must be assessed alongside security. [A; pp. 8–10]

**Analyst interpretation for the research question:** the paper identifies three relevant mechanisms. First, external data becomes part of an agent’s decision context. Second, the agent may see representations—such as hidden accessibility attributes—that differ from the human-visible page. Third, connected tools and browser actions provide ways to enact the malicious request. Together these explain a plausible route from injected text to real workflow effects. They do not quantify an agent-versus-standalone vulnerability gap. [D]

The related-work discussion on p. 2 explicitly mentions gaps between standalone-model refusals and agent behavior. The bibliography on p. 11 includes the paper whose title matches the user’s research question. That referenced work is not itself supplied; DoomArena’s characterization cannot substitute for inspecting its experiments. [A/D]

Cross-reference checks reveal several unresolved points:

| Issue | Sources | Consequence |
|---|---|---|
| Figure 2 describes an airline switch, but catalog result belongs to retail | p. 5 versus Table 2, p. 7 | Do not treat as a controlled within-airline comparison |
| Claude airline ASR is 2.66% in discussion versus 2.7% in tables | p. 10 versus pp. 7/14 | Likely display precision, not confirmed |
| Combined GPT-4o judge stealth is 10.2% versus 10.3% | Table 2 versus Table 5 | Preserve discrepancy |
| Reddit overall combined ASR is 98.2% versus 96.5% | Table 6 versus Table 8 | Aggregation/run relationship unresolved |
| Table 3 caption’s banner exception conflicts with full zero attacked-TSR rows | pp. 8/15 | Do not infer preserved judge-protected utility |
| Text says combination amplifies vulnerability broadly, but some means decrease | pp. 9/16–17 | Interpret as conditional, not universal |
| Stated 39 OSWorld tasks do not transparently explain tabulated increments | p. 9 | Do not reconstruct counts from percentages |

The phrase “no Pareto dominant” is also broader in prose than a universal claim can support. Figure 4 specifically says two of three threat models lack a dominating model–defense combination. It is safest to conclude that no single ranking resolves all evaluated security–utility tradeoffs, rather than asserting no dominance anywhere.

# 15. Contributions and novelty

**Conceptual:** deployment-specific threat modeling is made an explicit part of security evaluation. [A]

**System/methodological:** the configuration–attack–gateway–filter separation allows controlled injection into existing environments. [A]

**Implementation:** BrowserGym, τ-Bench, and OSWorld gateways; a reusable attack abstraction; fixed-sequence attacks; generalized attacker prompt construction; and a common defense interface are illustrated. The repository is announced, but its contents were not inspected. [A]

**Experimental:** the case studies compare models, attack channels, environments, and defenses using both malicious-outcome and legitimate-task metrics. Appendix decomposition exposes asymmetric interactions hidden by aggregate success. [A]

**Novelty boundary:** the authors do not claim a new secure-agent defense, a new backbone model, or a benchmark in itself. They explicitly adapt known attack types. The claim of uniquely satisfying six comparison criteria is the authors’ positioning within Table 1, not an independently verified global novelty finding. [A/D]

# 16. Limitations

## Authors’ stated limitations

- Training-time attacks are not the framework’s focus, though triggers could be inserted for evaluation. [p. 2]
- The paper does not exhaustively evaluate defenses beyond guardrails. [p. 5]
- Browser experiments use text-based agents; multimodal web-agent evaluation is left for future research. [p. 8, footnote 2]
- Combined results exclude trials where both attack-triggering conditions were not met. [pp. 8/14, footnotes]
- Powerful judge defenses still leave nontrivial tool-agent attack rates. [p. 8]
- LLM judges introduce latency and computational-cost tradeoffs. [p. 25]
- DoomArena does not enforce data minimization, anonymization, or other governance rules; sensitive testing data could reach external systems. [p. 11]

## Additional evidence-based analyst observations

- No matched standalone-LLM control supports a direct comparative vulnerability estimate.
- Only two WebArena domains and one small OSWorld subset are evaluated.
- Exact model snapshots, seeds, decoding settings, hardware, and subset selection are not adequately specified for precise reproduction.
- Browser and OSWorld uncertainty terms lack a fully explicit interpretation in their captions.
- A single LlamaGuard flag category narrows what its negative result establishes.
- Zero browser ASR with zero attacked TSR does not demonstrate secure productive execution.
- URL matching can establish redirection without independently establishing data theft.
- Aggregate combined metrics and component metrics have unresolved numerical differences.
- Figure 3 lacks an auditable numerical data series and regression specification.

These observations are analyst assessments, not limitations the authors necessarily state. Confidence is HIGH for identifiable reporting absences and MEDIUM for their likely impact.

# 17. Threats to validity

The following categories are **analyst-applied**.

**Internal validity:** airline versus retail comparisons change domain, agent strategy, and attacker objective. Observed ASR differences cannot isolate the effect of one factor. Combined-trigger exclusions create a selected population whose exposure may differ from all benchmark tasks.

**Construct validity:** attack success depends on the success filter. Reaching a target URL, leaking PII, issuing an unauthorized refund, and clicking a location are distinct outcomes. A common percentage does not make their severity or difficulty identical. Stealth records joint outcome success, not measured human failure to notice an attack.

**External validity:** results from two synthetic website domains and selected desktop tasks may not generalize to arbitrary production deployments, models, accessibility representations, or attacker budgets. The browser case study does not evaluate visual browser agents.

**Statistical conclusion validity:** tool results have three-trial summaries, but no significance testing is supplied. Browser and desktop uncertainty procedures are insufficiently explicit. Small numerical differences should not be ranked confidently without that information.

**Ecological validity:** purchase of ad space and malicious catalogs are realistic framing assumptions, but the supplied study does not measure how frequently attackers obtain those positions in real deployments. Screenshot inpainting is a defined capability, not an estimate of real-world compromise prevalence.

**Reproducibility:** code excerpts and repository availability are useful, but no repository revision was inspected. Missing exact configurations and inconsistencies prevent complete reconstruction from this paper alone. Ethics guidance also leaves data protection to the testing team.

# 18. Future work and open questions

## A. Explicit author directions

The authors plan to evaluate multimodal web agents. They encourage wider adoption of context-aware adaptive testing and emphasize adding new threat models, attacks, environments, and defenses through the framework. These are future directions and extensibility goals, not completed evaluations. [A; pp. 8, 10, 17–18, 25]

## B. Additional analyst open questions

1. How large is the vulnerability difference between a standalone model and its agent version when the backbone, harmful objective, and input information are matched?
2. Which representation details cause hidden webpage instructions to gain authority over the legitimate task?
3. Can a defense reject malicious content while continuing the original task, rather than aborting it?
4. How would broader LlamaGuard category selection alter detection, false positives, and task utility?
5. How do all-task combined results differ from results conditioned on both attacks being triggered?
6. What explains the discrepancies between main and appendix aggregate values?
7. What are the measured runtime, monetary, and latency costs of judge-based protection?
8. How reliable are success filters against partial leakage, misleading URLs, or delayed malicious effects?
9. Which generalized-attacker options actually improve attack success under controlled ablations?

These are logically remaining questions, not author-proposed experiments unless indicated in part A.

# 19. Terminology and notation glossary

| Term | Meaning in this work |
|---|---|
| AI agent | Model-driven system that observes an environment and takes actions |
| LLM | Large language model |
| SOTA | State of the art; the paper’s description of evaluated models at its time |
| User-agent-environment loop | Repeated interaction among task requester, agent, and environment |
| Episode | One sequence of interactions for a task |
| Threat model | Specification of attacker-controlled components and plausible attacks |
| Attack surface | Place or representation through which malicious content can enter |
| Prompt injection | Content intended to redirect the agent through its instruction processing |
| AttackConfig | Configuration selecting component, attack, and success filter |
| AttackGateway | Environment-specific wrapper that routes attack content |
| Attack choice | Selected attack implementation |
| Success filter | Predicate or judge determining attacker-goal success |
| Task verifier | Mechanism determining legitimate-task completion |
| ASR | Attack success rate |
| TSR | Task success rate, specified with or without attack |
| Stealth rate | Fraction where both attacker and legitimate task succeed |
| PII | Personally identifiable information, such as names or ZIP codes |
| API | Application programming interface used for operations or information |
| Accessibility tree | Structured page representation available to the browser agents |
| `alt`, `aria-label` | Accessibility-related fields used as injection locations |
| Inpainting | Inserting a malicious visual overlay into the screenshot observation |
| Guardrail | Detection mechanism that intervenes on suspected attacks |
| LLM-as-a-judge | Language model used to classify or assess interaction content |
| LlamaGuard | Safety classifier evaluated with one selected flag category |
| DAN | Do Anything Now; optional attacker-prompt mode described in the appendix |
| Few-shot examples | Example attacks and conversations supplied to the attacker prompt |
| Pareto frontier | Security–utility tradeoffs not improved on both axes by another considered choice |
| Constructive interference | One attack helps another succeed |
| Destructive interference | One attack suppresses another’s success |
| ± | Reported uncertainty annotation; explicitly standard deviation in Table 2, not fully specified everywhere |

# 20. Key numerical results

Unless labeled otherwise, numbers are author-reported percentages. Source table values were visually inspected and checked against the supplied extracted text. The table preserves representative uncertainty terms rather than reproducing every repeated cell.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Airline workload | 50 | tasks | τ-Bench | Author-reported | p. 7 |
| Retail workload | 115 | tasks | τ-Bench | Author-reported | p. 7 |
| Reddit workload | 114 | tasks | WebArena subset | Author-reported | p. 8 |
| Shopping workload | 192 | tasks | WebArena subset | Author-reported | p. 8 |
| Desktop workload | 39 | tasks | OSWorld subset | Author-reported | p. 9 |
| Tool-result repetitions | 3 | trials | Table 2/5 summaries | Author-reported | pp. 7/14 |
| GPT-4o airline ASR | 29.3 ±1.5 | % | Malicious user, no defense | Author-reported | T2, p. 7 |
| Claude-3.5 airline ASR | 2.7 ±0.2 | % | Malicious user, no defense | Author-reported | T2, p. 7 |
| GPT-4o catalog ASR | 34.8 ±1.2 | % | Retail, no defense | Author-reported | T2, p. 7 |
| Claude-3.5 catalog ASR | 39.1 ±1.1 | % | Retail, no defense | Author-reported | T2, p. 7 |
| GPT-4o combined ASR | 70.8 ±2.2 | % | Retail, no defense, filtered trials | Author-reported | T2, p. 7 |
| GPT-4o combined judge ASR | 28.2 ±0.8 | % | Retail, judge defense | Author-reported | T2, p. 7 |
| Claude combined judge TSR | 3.1 ±0.1 | % | Retail, under attack | Author-reported | T2, p. 7 |
| Claude catalog stealth | 18.0 ±0.7 | % | Retail, no defense | Author-reported | T2, p. 7 |
| GPT-4o Reddit pop-up ASR | 97.4 ±1.5 | % | No defense | Author-reported | T6, p. 15 |
| Claude Reddit pop-up ASR | 88.5 ±3.0 | % | No defense | Author-reported | T6, p. 15 |
| GPT-4o Reddit combined ASR | 98.2 ±1.2 | % | No defense | Author-reported | T6, p. 15 |
| Claude Shopping pop-up ASR | 42.7 ±3.6 | % | No defense | Author-reported | T7, p. 16 |
| Claude Shopping combined ASR | 97.4 ±1.2 | % | No defense | Author-reported | T7, p. 16 |
| Browser judge ASR and attacked TSR | 0.0 / 0.0 | % | All full-table judge attack rows | Author-reported | T6–T7 |
| GPT-4o desktop ASR | 78.6 ±0.0 | % | Pop-up inpainting, no defense | Author-reported | T4, p. 9 |
| Claude-3.7 desktop ASR | 22.9 ±0.0 | % | Same threat, no defense | Author-reported | T4, p. 9 |
| Desktop stealth | 2.9 / 5.7 | % | GPT-4o / Claude-3.7 | Author-reported | T4, p. 9 |
| Catalog component ASR change | 34.8 → 70.5 | % | GPT-4o retail, isolated→combined | Author-reported | T8, p. 17 |
| Banner component ASR change | 80.7 → 0.9 | % | GPT-4o Reddit, isolated→combined | Author-reported | T8, p. 17 |
| Claude pop-up domain difference | 45.8 | percentage points | 88.5 − 42.7 | Analyst-derived | T6–T7 |
| Catalog component increase | 35.7 | percentage points | 70.5 − 34.8 | Analyst-derived | T8 |
| Desktop click target | (1066, 457) | screenshot coordinates | Illustrated malicious target | Author-reported / visually readable | pp. 21–22 |
| LlamaGuard categories | 14 total; 1 selected | categories | Code Interpreter Abuse selected | Author-reported | pp. 14/25 |

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| DoomArena separates threat configuration from environment injection | Config tuple, gateway interfaces, diagrams | F1, L1–L5 | pp. 4–6, 17–18 | HIGH for architecture; integration effort not benchmarked |
| Security ranking changes with threat model | Claude low airline ASR but higher catalog ASR than GPT-4o | T2, X1/X2 | p. 7 | HIGH descriptive; domains and strategies differ |
| Browser pop-ups strongly redirect tested agents | Reddit 88.5–97.4% ASR for main models | T3/T6, X3 | pp. 8/15 | HIGH within tested conditions |
| Domain affects attack outcome | Claude pop-up 88.5% Reddit versus 42.7% Shopping | T6/T7, X3/X4 | pp. 15–16 | HIGH descriptive; causal feature unknown |
| Judge prevention does not preserve attacked browser utility | All judge attack rows have ASR=0 and attacked TSR=0 | T6/T7 | pp. 15–16 | HIGH; absence of observed success is not universal security |
| LlamaGuard result depends on configured category | Only Code Interpreter Abuse selected | A.1.1/A.7 | pp. 14/25 | HIGH; cannot generalize to all configurations |
| Combination can help one attack and suppress another | Catalog 34.8→70.5; user 12.8→2.7 | T8, X7 | p. 17 | HIGH for reported component outcomes; aggregate discrepancies remain |
| Desktop observation attacks affect evaluated models | ASR 78.6% versus 22.9% | T4, X5 | p. 9 | HIGH for reported values; denominator/run details unclear |
| Agent task success can coexist with compromise | Nonzero retail and desktop stealth | T2/T4 | pp. 7/9 | HIGH; stealth is joint outcome, not measured human detection |
| Results are relevant to agent-versus-LLM vulnerability mechanisms | Environmental injection plus action interfaces | F1/F7–F9, A.4 | pp. 4, 19–22 | MEDIUM analyst inference; no direct standalone comparison |

# 22. Very simple explanation — Explain Like I’m 15

Imagine an AI assistant is helping you shop online. It reads a product page and sees a message that says, “Before doing anything else, complete this security check.” The message looks relevant to the task, but it was placed there by an attacker. If the assistant treats that page text as a command, it may leave your task and follow the attacker’s request.

DoomArena is a testing system for situations like this. Researchers choose where the attacker is allowed to put a message, what the message tries to achieve, and how to check whether it worked. They can test a browser advertisement, a customer conversation, a product catalog, or a fake desktop warning using a common framework.

The tests show that there is no simple rule saying one agent is always safest. Some models resist one attack but fall for another. Two attacks can help each other, or one can get in the other’s way. A security checker can stop the attacker, but if it stops the whole task every time, the assistant also becomes less useful.

For the question about why agents may be more vulnerable than standalone language models, the useful lesson is that agents read outside material and can act on it. A misleading instruction can therefore become a browser visit, information disclosure, or tool operation. This paper demonstrates those risks in agents; it does not directly measure how much more vulnerable they are than the same models used without agent tools.

# Completeness Audit

Coverage is judged against the inventory, not response length. All supplied pages were reviewed in text form. All numbered figures and tables had directly inspectable rendered images. Non-rendered pages were reviewed only through their supplied text.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, abstract | Yes | Yes | Represented in compressed form | Author list recorded below |
| §1 Introduction | Yes | Yes | Fully represented substantively | Scope and contribution covered |
| §2 Related Work | Yes | Yes | Represented in compressed form | Categories and central comparisons retained |
| §3 Architecture | Yes | Yes | Fully represented substantively | All core components explained |
| §4.1 Threat-modeling | Yes | Yes | Fully represented substantively | Figure 2 inconsistency flagged |
| §4.2 Adaptive testing | Yes | Yes | Represented in compressed form | Trend evidence caveats retained |
| §4.3 New frameworks | Yes | Yes | Fully represented substantively | Wrapper and OSWorld example |
| §5 metrics and setup | Yes | Yes | Fully represented substantively | Modalities and sample sizes retained |
| §5.1 τ-Bench | Yes | Yes | Fully represented substantively | Main results and conditions |
| §5.2 BrowserGym | Yes | Yes | Fully represented substantively | Both domains and three attacks |
| §5.3 OSWorld | Yes | Yes | Fully represented substantively | Correct Claude version retained |
| §6 Tradeoffs/interference | Yes | Yes | Fully represented substantively | Aggregate/component distinction |
| §7 Conclusion | Yes | Yes | Represented in compressed form | Context-sensitive testing takeaway |
| Ethics Statement | Text only | Yes | Fully represented substantively | Governance and intended-use caveats |
| References | Yes, partly text only | Yes | Inspected but deliberately compressed | No citation validation or external reading |
| A.1.1 / Table 5 | Yes | Yes | Represented in compressed form | Mini results; repeated uncertainty cells compressed |
| A.1.2 / Tables 6–7 | Yes | Yes | Represented in compressed form | Every ASR mean retained; all TSR/stealth patterns covered |
| A.2 / Table 8 | Yes | Yes | Fully represented substantively | All component ASR and stealth means retained |
| A.3.1 Gateways | Yes | Yes | Fully represented substantively | Interfaces and registration |
| A.3.2 Attacks | Yes, p. 19 text only | Yes | Fully represented substantively | Fixed sequence and adaptive option |
| A.4 Attack library | Yes, partly text only | Yes | Represented in compressed form | Payload mechanisms preserved without full reproduction |
| A.4.1 Success filters | Yes | Yes | Fully represented substantively | URL-checking limitation explained |
| A.5 Generalized attacker | Yes | Yes | Fully represented substantively | Optional inputs versus evaluated benefit separated |
| A.6 Figure 3 sources | Yes, partly text only | Yes | Represented in compressed form | Source categories; no website verification |
| A.7 Defenses | Text only | Yes | Fully represented substantively | Category restriction and abort behavior |
| F1 architecture panels a/b | Visually | Yes | Fully represented substantively | Both panels explained |
| F2 configurations | Visually | Yes | Fully represented substantively | Numbers and caption conflict |
| F3 trend plot | Visually | Yes | Uncertain | Fine labels and exact plotted values not transcribed |
| F4 security–utility | Visually | Yes | Represented in compressed form | Axes/encodings; precise points from tables |
| F5 task-category bars | Visually | Yes | Uncertain | Exact segments and all small labels unreadable |
| F6 OSWorld gateway | Visually | Yes | Fully represented substantively | Injection and state paths |
| F7 banner screenshot | Visually | Yes | Fully represented substantively | Visible versus accessibility content separated |
| F8 pop-up screenshot | Visually | Yes | Fully represented substantively | Hidden payload not inferred from screenshot |
| F9 desktop screenshot | Visually | Yes | Fully represented substantively | Target coordinate retained |
| F10 attacker architecture | Visually | Yes | Fully represented substantively | Prompt assembly flow |
| T1 | Visually and text | Yes | Fully represented substantively | Author-assigned checkmarks |
| T2–T5 | Visually and text | Yes | Represented in compressed form | Key values and all condition categories retained |
| T6–T8 | Visually and text | Yes | Represented in compressed form | Expanded matrices and interaction outcomes |
| L1–L12 | Yes, some text only | Yes | Represented in compressed form | Every listing’s function accounted for |
| X1–X7 experiments/analyses | Yes | Yes | Fully represented substantively | Separate conditions and caveats |
| Formal research questions/hypotheses | None identified | Yes | Absence explicitly represented | Informal objectives distinguished |
| Major equations/theorems/proofs | None identified | Yes | Absence explicitly represented | Metric formulas labeled analyst formalizations |
| Major contributions O1–O6 | Yes | Yes | Fully represented substantively | Architecture, integration, testing, tradeoffs |
| Author-stated limitations | Yes | Yes | Fully represented substantively | Separated from analyst observations |
| Substantive footnotes | Yes | Yes | Fully represented substantively | Combined-trigger exclusion and future multimodal evaluation |
| Separate supplements | Not supplied | Yes | Missing from supplied material | No separate artifact claimed reviewed |

**Bibliographic identity:** authors listed on p. 1 are Leo Boisvert, Mihir Bansal, Chandra Kiran Reddy Evuru, Gabriel Huang, Abhay Puri, Avinandan Bose, Maryam Fazel, Quentin Cappart, Jason Stanley, Alexandre Lacoste, Alexandre Drouin, and Krishnamurthy (Dj) Dvijotham. Affiliations include ServiceNow Research, University of Washington Seattle, and Polytechnique Montréal. The author footnote marks equal contribution/joint primary authorship and Mila-Quebec affiliation. Administrative correspondence details were deliberately compressed.

## Missing or inaccessible material

No numbered page is missing from the supplied text. Renderings are absent for pp. 2, 11, 13, 19, 24, and 25, so no claim of direct visual inspection is made for those pages. The repository, exact execution configurations, underlying Figure 3 dataset, Figure 5 category-level numbers, external benchmark papers, and cited standalone-versus-agent studies were not supplied as inspectable artifacts. No separate supplement was reviewed.

## Uncertain interpretations

Unresolved items are Figure 2’s airline/retail wording, Table 2 versus Table 5 stealth differences, Table 6 versus Table 8 combined Reddit ASR, Table 3’s banner exception, browser/desktop uncertainty definitions, OSWorld denominators, and the precise data/labels underlying Figures 3 and 5. No values were guessed to repair these issues. Approximate axis spans were identified as approximate rather than exact results.

## Deliberately compressed material

Repeated headers, decorative icons, long bibliography entries, correspondence information, full malicious payload wording, code syntax, repeated table baselines, and most browser uncertainty annotations were compressed. All attack mechanisms, interfaces, numbered visuals, table condition categories, major empirical findings, substantive caveats, and appendix purposes were retained. Figure 3’s ten sources are summarized as the author-listed websites Lakera, XenonStack, Astra Security, Qualys, Help Net Security, Layer Seven Security, CSO Online, TechTarget, MIT News, and Cobalt; their content was not externally verified.

## Potential omissions

No known major section, numbered figure, numbered table, listing, distinct experimental condition, or substantive appendix was left unaccounted for. This is not a verbatim reproduction or a complete cell-by-cell statistical transcript: repeated numerical cells and secondary annotations are compressed as disclosed. Unreadable graphical details and missing reproducibility information remain explicitly unresolved. The supplied evidence supports an in-depth account of DoomArena, while the comparative question about standalone LLMs remains only partially addressed through author-cited background and clearly labeled analyst inference.
