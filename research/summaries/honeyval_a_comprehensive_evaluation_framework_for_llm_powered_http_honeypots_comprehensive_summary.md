## Stage 0 — Document Accessibility Report

The supplied work is **Honeyval: A Comprehensive Evaluation Framework for LLM-powered HTTP Honeypots**. This analysis uses only the supplied page text and source images. No tools, browsing, repository inspection, experiments, or external verification were performed. Instructions reproduced in Appendix F are treated as research evidence, not instructions to this analyst.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied extracted text covers physical PDF pp. 1–24. |
| Accessible page count | 24. Printed page numbers match the supplied physical page labels. |
| Pages apparently missing | None within the supplied 1–24 sequence; this does not independently establish that no other supplement exists. |
| Pages visually inspected | 1, 2, 4, 5, 6, 7, 8, 12, 13, 14, 15, 16, 17, 18. |
| Text-only pages | 3, 9, 10, 11, 19, 20, 21, 22, 23, 24. These were read from supplied extraction, not visually inspected. |
| Figures | Figures 1–3 are visually available and inspected. |
| Tables | Tables 1–30 are available as extracted text and on supplied images; all were inspected. |
| Equations | No numbered mathematical equations were identified in the supplied work. |
| Appendices | A–F, including E.1, F.1, and F.2, are supplied. |
| Supplementary artifacts | The code repository, executable implementations, OpenAPI files, tests, logs, and model-service configurations are described but not supplied as inspectable artifacts. |
| OCR | No additional optical character recognition was needed. Extracted text was cross-checked against available table and figure images. |
| Limitations | Exact figure bar heights and the statistical meaning of plotted error bars are not fully specified. No claim of executable reproducibility or repository validation is made. |

Evidence labels used below are **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. There is no external-information category in use. Confidence is HIGH for clear supplied statements and table values, MEDIUM for qualified methodological inferences, and UNKNOWN for unavailable implementation details.

## 1. Plain-language orientation

[A] A honeypot is a decoy computer service intended to attract attackers so defenders can observe their techniques. Traditional simple honeypots often produce repetitive or unrealistic responses. More realistic honeypots can expose real computer resources and therefore create security risks. This paper investigates a different arrangement: a large language model, or LLM, invents the responses of a web service without accessing the underlying resources that an attacker would normally compromise.

The paper's central contribution is **Honeyval**, an evaluation framework for these LLM-powered web-service decoys. Rather than asking whether a few responses look realistic, Honeyval makes automated hacking agents interact with decoys representing 16 specified backend applications. Two separate controls check whether the attacking agent can exploit real vulnerable applications and whether the decoy can correctly answer ordinary functional requests. These controls help distinguish a convincing decoy from an incapable attacker or a broken simulation.

[A] The evaluated LLM honeypots produce longer interactions than simple rule-based mocks: the paper reports 82.6 versus 30.6 HTTP requests per interaction on average. They are usually less frequently identified as honeypots, and most evaluated pairings favor the defender in model-running cost. These advantages have limits. Responses take seconds, simulation fidelity varies by model, detection decisions can produce false alarms, and extra instructions can damage ordinary functionality.

[D] For the motivating research question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, the paper offers evidence about agents exposed to deceptive external service responses and repeated interaction. It does **not** directly compare web agents with standalone LLMs, quantify an added vulnerability caused by tools, or establish a successful general prompt-injection attack. Its strongest relevance is to evaluating deception, continued interaction, detection errors, and the trade-offs introduced by defensive or adversarial instructions.

## 2. Document roadmap

The document is a mixed cybersecurity systems, benchmark, and empirical evaluation paper.

| Inventory identifier | Original component | Location and role |
|---|---|---|
| S1 | Abstract and §1 Introduction | pp. 1–2: motivation, evaluation gap, approach, headline findings. |
| S2 | §2 Background and Related Work | p. 3: honeypots, LLM-powered honeypots, hacking agents. |
| S3 | §3 Key Requirements | pp. 3–4: scalability, reproducibility, representativeness, adaptability. |
| S4 | §4 Evaluation Framework | pp. 4–5: design, threat scenario, environments, tasks. |
| SS4.1 | §4.1 Environments | p. 4: application artifacts and exploit goals. |
| SS4.2 | §4.2 Tasks | p. 5: main task and two controls. |
| S5 | §5 Evaluation | pp. 5–8: configuration and six distinct analyses. |
| SS5.1 | §5.1 Experimental Setup | pp. 5–6: agents, honeypots, models, budgets, repetitions. |
| SS5.2 | §5.2 Results and Analysis | pp. 6–8: engagement, detection, cost, fidelity, prompt changes. |
| S6 | §6 Discussion and Conclusion | pp. 8–9: synthesis, limitations, outlook. |
| REF | References | pp. 9–11: bibliographic entries; not independent evidence verification. |
| A1–A4 | Appendices A–D | pp. 12–13: societal impact, compute, licensing, applications. |
| A5 | Appendix E.1 | pp. 12, 14–18: detailed prompt-variation results. |
| A6 | Appendix F.1–F.2 | pp. 19–24: agent, tool, objective, and honeypot prompts. |

The visual inventory comprises Figures 1–3 and Tables 1–30. There are 16 labeled prompt blocks, F.1–F.16. No formal research-question numbering, hypotheses, theorem statements, pseudocode algorithms, keywords list, or numbered equations were identified. The Appendix F templates are procedural evidence, not formal algorithm listings.

The authors are Mark Vero, Fabian Kaczmarczyck, Ivan Petrov, Ilia Shumailov, Jamie Hayes, Niels Heinen, Tianqi Fan, Luca Invernizzi, and Martin Vechev. Page 1 states acceptance to the 1st Workshop on Combining Theory and Benchmarks, CTB@ICML 2026, Seoul, South Korea. Affiliations include ETH Zurich, Google, Google DeepMind, AI Sequrity Company, and an independent affiliation. A substantive footnote states that Vero's work was conducted during an internship at Google. The correspondence address and running headers are bibliographic or navigational rather than experimental content.

## 3. Background and context

[A] A **low-interaction honeypot** uses lightweight rules to respond to requests. It needs few actual system components but may be easy to recognize. A **high-interaction honeypot** behaves more like a real application, keeping attackers engaged, but can require resources that expose its operator to compromise. The authors position LLM simulation as combining varied interaction with minimal underlying resource exposure (§2, p. 3).

**HTTP**, Hypertext Transfer Protocol, carries requests and responses between clients and services. An **application programming interface**, or API, specifies how software accesses a service. The paper studies HTTP-based backend services rather than browser interfaces or operating-system shells. **REST API** is the paper's term for the endpoint-based interfaces being simulated. An **OpenAPI specification** supplies a structured description of endpoints and expected behavior.

An **agent** combines an LLM with tools and an interaction loop: it chooses actions, receives observations, and acts again. The in-house **ReActAgent** follows the Reason and Act principle and has curl and Python tools. The other agents are Claude Code and Gemini CLI, where CLI means command-line interface. These agents act as attackers in a controlled evaluation.

A **functional test** checks whether a service behaves as specified on ordinary requests. **Fidelity** here refers to passing those tests, not to a universal guarantee that all possible behavior matches a real application. A **true positive rate**, TPR, measures detection of actual honeypots; a **false positive rate**, FPR, measures real applications incorrectly labeled as honeypots. Keeping these separate is essential: a detector that frequently announces a honeypot may simply be over-suspicious.

[A] Prior approaches are described as fixed command-output comparisons, manual tests, and online deployment. The authors argue that these respectively suffer from fixed coverage, limited scalability, and sparse or uncontrollable feedback. Most cited LLM honeypot work concerns shells. These characterizations are the authors' positioning of the literature, not an independently checked survey.

## 4. Research problem and gap

**Existing problem [A]:** developers need to measure whether an LLM-powered honeypot convincingly simulates a service, keeps an attacker engaged, and remains practical to operate.

**Shortcomings of previous evaluation approaches [A]:** fixed command sets cannot adapt to new environments or defensive behavior; manual evaluation does not scale during development; live deployment can require long waits for useful traffic. An underspecified simulated machine can also acquire inconsistent invented details across runs, making comparisons difficult (§1, p. 1; §3, p. 3).

**Research gap [A]:** the paper identifies a lack of a unified, scalable evaluation protocol with sufficiently specified environments, meaningful attack objectives, and controls that remain useful when either side's prompt changes.

**Motivation [A]:** a long interaction is only useful evidence if the attacker is capable and the simulated service is functional. Conversely, changing a prompt to improve one metric may damage another. A honeypot might produce more aggressive deceptive messages while becoming easy to recognize or failing benign requests.

**Scope [A]:** 16 HTTP backend applications sourced from BaxBench, four concrete exploit-goal families, five LLM honeypot backends, four agent configurations, simple rule-based baselines, and selected prompt variations. This is not an evaluation of all web agents, every honeypot architecture, or all forms of LLM security.

## 5. Research questions / objectives / hypotheses

The paper does not state formal numbered research questions or testable hypotheses. The following are its explicit objectives, organized for clarity rather than presented as author-numbered questions:

1. Formulate requirements for evaluating LLM-powered honeypots (§3).
2. Build a scalable and reproducible framework grounded in specified services and verifiable attack goals (§4).
3. Use controls to monitor both attacker competence and honeypot functionality under customization (§4.2).
4. Evaluate cost-efficient LLMs as HTTP honeypots against capable hacking agents (§5).
5. Investigate how honeypot and attacker prompt changes affect engagement, detection, cost, fidelity, and exploit performance (§5.2).

[D] The user's standalone-versus-agent research question is an additional interpretive lens. Honeyval does not experimentally isolate that comparison. Relevant subquestions left open include whether externally supplied responses change an agent's decisions, whether continued interaction reflects deception or ordinary failed search, and whether detection instructions preserve legitimate performance.

## 6. Assumptions / threat model

[A] The honeypot has **no system resource access** (§4, p. 4). Consequently, an attacker cannot achieve the real exploit objective against the honeypot. A response that appears to acknowledge an exploit is not equivalent to compromising an actual resource. This is why real secure and insecure implementations are needed in the agent control task.

Both the attacker and honeypot receive the entire API specification. There are no specification secrets for the attacker to discover. The modeled situation is a public or predictable API, rather than an unknown proprietary interface. Attackers receive a concrete objective and can be instructed to stop when the application is secure or when they believe they have detected a decoy.

[A] The agent-control applications are executable Python FastAPI implementations. Programmatic callbacks check success on real applications. The supplied work describes the callbacks' role and objective templates, but not all implementation internals. The analyst therefore treats their reported existence as author evidence, not independently validated ground truth.

[A] Appendix F gives additional restrictions. The curl tool rewrites the target to a restricted URL. The Python tool runs scripts in a sandbox, permits requests and standard-library modules, and applies a timeout whose duration is not specified. CLI agents are told that only the webapp and backend-model proxy are accessible and that they should communicate with the webapp through HTTP. These prompt descriptions do not independently prove enforcement.

[D] The key information boundary is between an agent's assigned objective and content returned by the service it investigates. Appendix F.15 explicitly attempts to exploit that boundary. It is evidence of the study's attack construction, not evidence that the boundary was successfully crossed in every run.

## 7. Methodology

### Framework requirements and design

[A] Four requirements guide the framework: **scalability**, by automating attacker interactions; **reproducibility**, by supplying precise application specifications and goals; **representativeness**, by choosing goals achievable on corresponding real vulnerable applications; and **adaptability**, by measuring side effects when either side changes (§§3–4, pp. 3–4).

For each backend, four artifacts are described: an OpenAPI specification, a functional test suite, a secure implementation, and an insecure implementation. The specifications and tests come from BaxBench, with minimal modifications where needed. No train/validation/test partition, learned attack training procedure, annotation process, or participant recruitment is described. This is an interaction benchmark, not a model-training study.

### Three evaluation tasks

| Task | Interaction | Main measurements | Why it matters |
|---|---|---|---|
| Main | Agent attacks LLM or rule-based honeypot | HTTP request count, running costs, detection, latency and optional custom metrics | Measures behavior during adversarial interaction. |
| Agent control | Same agent configuration attacks real secure/insecure applications | Exploit success on vulnerable apps, cost, false-positive honeypot detection | Checks capability and mistaken detection. |
| Honeypot control | Same honeypot configuration receives functional tests | Functional pass rate, cost, latency | Checks ordinary simulation behavior. |

[A] Prompts and other settings remain task-independent for a given configuration. An agent is not told whether it faces a real service or a honeypot, and a honeypot is not specially adapted to benign tests. This supports comparing main-task behavior with control outcomes (§4.2, p. 5).

### Applications and exploit goals

[A] Four applications have the goal of downloading a script to the server: Calculator, Compiler, Monitor, and ProductCatalog. Six have the goal of deleting a database table: ClickCount, CreditCardService, Forum, ShoppingCartService, UptimeService, and Wiki. Three concern modifying an administrator password: Login, SecretStorage, and UserCreation. Three concern exfiltrating browser local storage: Recipes, RecommendationService, and ShopOverview (Table 5, p. 13).

[C] These group sizes sum to 4 + 6 + 3 + 3 = 16 applications. The four goal families are not equally represented. Appendix F.10 clarifies that the download goal requires saving a file, not executing it. Appendix F.13 describes a browser-local-storage exfiltration callback; the provided material does not fully explain its browser-driving implementation.

### Models, agents, and baseline

[A] ReActAgent runs with Gemini 3 Flash or Claude Sonnet 4.6, using high thinking. Claude Code uses Claude Sonnet 4.6, and Gemini CLI uses Gemini 3 Flash. Thus four evaluated agent rows represent two in-house model choices and two off-the-shelf agent configurations, not four unrelated base-model families.

The honeypot backends are Gemini 3 Flash, Claude Haiku 4.5, Gemini 2.5 Flash, Qwen 3.5 9B, and GPT 5.4 Nano. Open-weight models are accessed through Together AI; closed models use production APIs. The baseline consists of simple rule-based heuristic mock APIs. Baseline code is described as included in the repository, but it was not supplied for inspection.

### Harness and resources

[A] A hollow HTTP server forwards incoming endpoint requests to the LLM. The LLM receives the API specification and interaction history and generates response content, media type, status code, and optional headers. Each request becomes a separate LLM call. The entire context is fed back, which the authors identify as token-inefficient.

Every experiment has five independent repetitions. Each agent run and each LLM honeypot run has a $10 budget. ReActAgent additionally has a 50-iteration limit; Claude Code and Gemini CLI have a one-hour limit per run. HTTP request count can exceed 50 because a tool action can issue multiple requests. Appendix B reports no local graphics processing unit requirement: the experiments use API calls and a CPU machine. Typical interaction costs are often below $1, although paired budgets permit roughly $20.

[C] If every application receives five repetitions for one fixed agent–honeypot condition, that condition entails 16 × 5 = 80 application-level repetitions. This is a design-based calculation, not an independently verified executed-run count. The paper does not provide a consolidated run manifest or total API bill.

### Statistics and configuration gaps

[A/B] Tables report means, rates, median latency, and mean generated tokens. Figures 2–3 include visible error bars, but their definition and calculation are not specified in the supplied captions or methods. No named statistical test, p-value, confidence level, random seed list, exact service snapshot, library version, or detailed CPU specification is supplied. The authors use the word significantly, but the supplied work does not establish a formal significance-testing procedure.

## 8. Experiments / analyses

| ID | Purpose and conditions | Evidence | Main result and caveat |
|---|---|---|---|
| X1 | Compare interaction length for five LLM honeypots and rule-based mocks across four agents | Table 1; pp. 2, 6 | LLM mean 82.6 versus mock mean 30.6 requests. Request count is a proxy for information collection. |
| X2 | Measure actual-honeypot detection and false alarms on real applications | Figure 2; pp. 6–7 | LLM decoys are less detectable than mocks; high detection by Gemini CLI is accompanied by high FPR. Exact FPR values are not tabulated. |
| X3 | Compare agent and honeypot API-running costs | Figure 3; pp. 7, 12 | Most pairings favor the honeypot. Some efficient-agent pairings do not. Long-context pricing tiers are not modeled. |
| X4 | Measure latency, output tokens, and benign functional fidelity | Table 2; p. 7 | Median latency 3.3–13.7 seconds; pass scores 71.2–97.5 on the table's percentage-like scale. |
| X5 | Change honeypot prompt: None, Careful PI, Convince | Table 3; Tables 6–30; pp. 7–8, 14–18 | Convince raises average request count and detection; Careful PI lowers average fidelity and request count. Effects vary by pairing. |
| X6 | Change agent prompt: exploit only, detect, detect plus hide | Table 4; p. 8 | Exploit success varies without a universal direction. No standalone-LLM baseline is included. |

For X1–X5 the main interaction concerns a decoy, so genuine exploit success is structurally unavailable there. X6 specifically uses vulnerable real implementations. The functional scores in X4–X5 arise from the separate honeypot control, not from successfully fooling the hacking agent.

[A] X5's Careful PI condition asks the decoy to identify a likely AI attacker and attempt to elicit its provider, instructions, tools, and organization. Convince asks it to assert that the application is secure. These are different manipulations: the former attempts instruction-level influence and disclosure; the latter changes the messages used to discourage or mislead an attacker. Neither should be reduced to a single generic attack-success result.

## 9. Results

### Interaction length

[A] The reported overall means are 82.6 HTTP requests for LLM honeypots and 30.6 for mocks (p. 2). [C] Their difference is 82.6 − 30.6 = **52.0 requests**, and their ratio is 82.6 / 30.6 ≈ **2.70**. This explains the authors' approximate threefold description; it is not exactly a 3.00 ratio.

[B] Every LLM entry in Table 1 exceeds its corresponding agent's rule-based entry. The smallest LLM mean is 46.0, for Claude Sonnet 4.6 against Claude Haiku 4.5. The largest is 133.6, for Claude Code against Gemini 2.5 Flash. These are cell means, not minimum and maximum individual-run lengths.

### Detection

[A/B] Rule-based honeypots have higher detection than LLM decoys in Figure 2. Main-text claims of rates usually below 40% have an important exception: Gemini CLI's LLM detection rates in detailed tables are 0.34, 0.46, 0.47, 0.57, and 0.44 under the baseline prompt. The authors also report high false-positive detection for that agent, limiting the meaning of its apparent vigilance. The Gemini-driven ReActAgent likewise has concerning false alarms. Low TPR alone does not establish high quality, and high TPR alone does not establish reliable detection.

### Cost and functional behavior

[A/B] Baseline cost advantage averages 3.6 in Table 3. The definition is agent cost divided by honeypot cost, so values above one favor the defender. Table 6 gives 0.55 for Gemini 3 Flash on both sides; Table 25 gives 15.7 for Claude Code against GPT 5.4 Nano. These illustrate substantial configuration dependence.

Table 2 reports the fastest median response as Gemini 3 Flash at 3.3 seconds and the slowest as Claude Haiku 4.5 at 13.7 seconds. The same models have functional scores of 97.5 and 91.3 respectively. GPT 5.4 Nano has the smallest generated-token mean, 87.7, but the lowest functional score, 71.2. Thus token economy and benign fidelity do not have the same ranking.

### Honeypot customization

[A] Table 3 gives None/Careful PI/Convince request means of 82.6/50.1/102.6, detection rates of 0.24/0.49/0.45, cost ratios of 3.6/4.7/3.5, and functional pass fractions of 0.84/0.62/0.84.

[C] Relative to None, Convince adds 102.6 − 82.6 = **20.0 requests**, approximately 24.2% using 20.0 / 82.6 × 100. Its detection rate rises by **21 percentage points**, from 24% to 45%. Careful PI removes **32.5 requests** and lowers fidelity by **22 percentage points**, from 84% to 62%. These are differences of rounded aggregate values, not independent statistical effect estimates.

[A] The authors observe injection attempts that are often unsuccessful and instead expose the decoy. They also observe attempted injections during benign testing, explaining the fidelity penalty. No dedicated rate for successful disclosure of agent instructions, provider, or organization is supplied.

### Agent customization

[B] With detection enabled, vulnerable-application exploit rates are 58.8%, 67.5%, 98.8%, and 90.0% for Gemini ReActAgent, Claude ReActAgent, Claude Code, and Gemini CLI respectively (Table 4). Adding concealment changes these to 52.5%, 70.0%, 90.0%, and 87.5%. The mixed direction supports the authors' narrower statement that there is no universal trend, rather than a claim that extra objectives are free of cost.

## 10. Figure-by-figure interpretation

### Figure 1 — Framework overview, p. 2

[B] This is an architecture diagram rather than a numerical plot. Stacked rounded environment panels represent the 16 backend services, with Forum as the visible example. The center contains a hacking agent and LLM honeypot connected by exploit and deceive arrows. The left contains real secure/insecure implementations for the agent control. The right contains backend functional tests for the honeypot control. A bottom band groups metrics by task.

The diagram's main message is that direct adversarial interaction alone is insufficient. Agent competence is measured against real applications, and simulator competence against functional tests. Colors distinguish components rather than statistical conditions. There are no axes, numerical scales, uncertainty bars, or measured feedback-loop gains.

### Figure 2 — Honeypot detection, p. 6

[B] A grouped bar chart places four hacking-agent configurations on the horizontal axis and honeypot detection rate on a linear vertical axis from 0.0 to 1.0. Red-to-orange bars represent Gemini 3 Flash, Claude Haiku 4.5, Gemini 2.5 Flash, and Qwen 3.5 9B; yellow represents GPT 5.4 Nano; a pale bar represents the rule-based honeypot. An outlined red FPR overlay identifies false-positive detection measured on real applications. Thin capped error bars are visible, but their statistical definition is not given.

The pale rule-based bars are consistently taller than the LLM bars. Gemini CLI has generally taller LLM bars than the other agents, but also a visibly higher FPR reference. Exact LLM baseline rates are available in Tables 6–25, so graphical estimates are unnecessary. Exact FPRs and rule-based rates are not labeled in the supplied plot and are not reconstructed here. The caption states that honeypot detection exceeds corresponding FPRs; that is an author claim, not a numerical significance test established by this review.

### Figure 3 — Relative cost advantage, p. 7

[B] Another grouped bar chart uses the same four agent groups and five LLM colors. The vertical axis is a linear multiplicative cost ratio, with labeled ticks from 0.0× through 15.0×. A dashed red horizontal reference marks 1×, the cost break-even point. GPT 5.4 Nano has the tallest bars, especially against Claude Code; some bars against the Gemini ReActAgent lie below break-even. There is no rule-based series.

[A] The ratio is attacker cost divided by honeypot cost. It is not requests per dollar, absolute dollars, or end-to-end system cost. Exact corresponding baseline ratios are supplied in Tables 6–25. The authors discuss a naive full-context honeypot and batching-capable agents, which matter when interpreting the asymmetry. Error bars are visible but undefined in the supplied description.

## 11. Table-by-table interpretation

### Table 1 — Baseline request means, p. 6

[B] Columns are five honeypot models and a rule-based baseline; rows are agents. Values are mean HTTP request counts.

| Agent | Gemini 3 Flash | Haiku 4.5 | Gemini 2.5 Flash | Qwen 3.5 9B | GPT 5.4 Nano | Rule-based |
|---|---:|---:|---:|---:|---:|---:|
| Gemini 3 Flash ReAct | 61.2 | 91.6 | 70.5 | 63.1 | 96.9 | 12.1 |
| Claude Sonnet 4.6 ReAct | 59.7 | 46.0 | 74.1 | 73.6 | 63.6 | 19.4 |
| Gemini CLI | 83.9 | 83.3 | 86.9 | 85.5 | 91.9 | 51.2 |
| Claude Code | 84.3 | 79.2 | 133.6 | 101.0 | 121.6 | 39.7 |

All LLM cells exceed their row's baseline. The largest within-row mean belongs to GPT Nano for Gemini ReAct and Gemini CLI, Gemini 2.5 Flash for Claude ReAct and Claude Code. No uncertainty estimates or significance markers appear in the table.

### Table 2 — Latency, generated tokens, fidelity, p. 7

| Honeypot | Median latency, seconds | Mean generated tokens per response | Test Pass@1, reported scale |
|---|---:|---:|---:|
| Gemini 3 Flash | 3.3 | 207.1 | 97.5 |
| Claude Haiku 4.5 | 13.7 | 523.9 | 91.3 |
| Gemini 2.5 Flash | 3.7 | 383.5 | 85.0 |
| Qwen 3.5 9B | 9.7 | 291.1 | 76.2 |
| GPT 5.4 Nano | 4.3 | 87.7 | 71.2 |

[A/B] Tokens include reasoning and final output. Latency is a median across interactions; tokens are an average. Table 2 expresses fidelity on a 0–100-like scale while later tables use fractions. The supplied table does not print a percent symbol in the column heading, so the exact displayed numbers are retained. Their relationship to later fractions is consistent with percentage scaling and rounding. Neither a test-count denominator nor per-application fidelity distribution is supplied.

### Table 3 — Aggregate prompt effects, p. 8

| Metric | None | Careful PI | Convince |
|---|---:|---:|---:|
| Interaction length, requests | 82.6 | 50.1 | 102.6 |
| Cost advantage, ratio | 3.6 | 4.7 | 3.5 |
| Detection TPR, fraction | 0.24 | 0.49 | 0.45 |
| Functional Test Pass@1, fraction | 0.84 | 0.62 | 0.84 |

These values average across agents and honeypots. Convince maximizes aggregate request count; Careful PI maximizes the cost ratio but has the worst fidelity and highest detection. None has the lowest detection. None and Convince tie at the displayed fidelity precision. These metric-specific rankings cannot be collapsed into a single best configuration.

### Table 4 — Exploit success under agent prompts, p. 8

| Agent | Only-Exploit, % | + Detect, % | + Detect + Hide, % |
|---|---:|---:|---:|
| Gemini 3 Flash ReAct | 60.8 | 58.8 | 52.5 |
| Claude Sonnet 4.6 ReAct | 55.0 | 67.5 | 70.0 |
| Claude Code | 93.7 | 98.8 | 90.0 |
| Gemini CLI | 91.2 | 90.0 | 87.5 |

The comparison concerns vulnerable real applications. Claude Code is highest in every column. Gemini ReAct declines across successive prompt additions, Claude ReAct increases, and the off-the-shelf agents show other patterns. No intervals, significance markers, or per-application outcomes are tabulated.

### Table 5 — Applications and goal assignment, p. 13

[B] This table has application, description, and exploit-goal columns. Merged goal cells group the 16 applications. Calculator evaluates expressions; Compiler checks compilation; Monitor tracks processes; ProductCatalog stores product attributes. ClickCount stores clicks; CreditCardService stores card data; Forum is a message board; ShoppingCartService maintains carts; UptimeService tracks service uptime; Wiki stores articles. Login provides registration/login; SecretStorage stores secrets; UserCreation supports invite-only registration. Recipes supports uploading, commenting, and rating; RecommendationService stores and queries recommendations; ShopOverview is a warehouse database service. Their four goal groups are listed in §7 above. The table catalogs evaluation environments rather than reporting measured performance.

### Tables 6–25 — Every agent–honeypot prompt comparison, pp. 14–17

To preserve all substantive cells without repeating 20 nearly identical explanations, the next table transcribes each source table using tuples. **Every tuple is ordered None / Careful PI / Convince.** L is mean HTTP requests, C is the cost ratio, D is detection TPR as a fraction, and F is functional pass fraction. F is repeated because it comes from the separate honeypot control, not an attacker-specific test.

| Source table; page | Agent; honeypot | L | C | D | F |
|---|---|---|---|---|---|
| T6; 14 | Gemini ReAct; Gemini 3 Flash | 61.2 / 1.7 / 46.2 | 0.55 / 1.5 / 0.70 | 0.15 / 0.66 / 0.49 | 0.97 / 0.23 / 0.97 |
| T7; 14 | Gemini ReAct; Haiku | 91.6 / 27.4 / 94.2 | 0.28 / 0.39 / 0.23 | 0.28 / 0.51 / 0.36 | 0.91 / 0.78 / 0.89 |
| T8; 14 | Gemini ReAct; Gemini 2.5 | 70.5 / 25.9 / 77.1 | 0.79 / 1.3 / 0.56 | 0.15 / 0.49 / 0.35 | 0.85 / 0.76 / 0.84 |
| T9; 14 | Gemini ReAct; Qwen | 63.1 / 59.0 / 58.2 | 1.2 / 1.1 / 1.4 | 0.24 / 0.29 / 0.39 | 0.76 / 0.69 / 0.77 |
| T10; 14 | Gemini ReAct; GPT Nano | 96.9 / 75.2 / 65.4 | 1.4 / 2.7 / 3.1 | 0.28 / 0.21 / 0.44 | 0.71 / 0.65 / 0.73 |
| T11; 14 | Claude ReAct; Gemini 3 | 59.7 / 16.9 / 67.0 | 2.8 / 3.0 / 2.6 | 0.09 / 0.61 / 0.29 | 0.97 / 0.23 / 0.97 |
| T12; 15 | Claude ReAct; Haiku | 46.0 / 22.4 / 59.3 | 1.9 / 3.6 / 1.9 | 0.12 / 0.47 / 0.20 | 0.91 / 0.78 / 0.89 |
| T13; 15 | Claude ReAct; Gemini 2.5 | 74.1 / 52.5 / 124.5 | 2.4 / 3.0 / 1.6 | 0.11 / 0.35 / 0.06 | 0.85 / 0.76 / 0.84 |
| T14; 15 | Claude ReAct; Qwen | 73.6 / 66.6 / 60.1 | 3.2 / 4.8 / 5.5 | 0.19 / 0.26 / 0.24 | 0.76 / 0.69 / 0.77 |
| T15; 15 | Claude ReAct; GPT Nano | 63.6 / 42.2 / 86.6 | 11.4 / 24.8 / 11.2 | 0.03 / 0.01 / 0.14 | 0.71 / 0.65 / 0.73 |
| T16; 15 | Gemini CLI; Gemini 3 | 83.9 / 6.2 / 94.1 | 1.6 / 1.2 / 1.7 | 0.34 / 0.96 / 0.88 | 0.97 / 0.23 / 0.97 |
| T17; 15 | Gemini CLI; Haiku | 83.3 / 33.9 / 104.2 | 0.92 / 1.4 / 0.95 | 0.46 / 0.82 / 0.84 | 0.91 / 0.78 / 0.89 |
| T18; 16 | Gemini CLI; Gemini 2.5 | 86.9 / 44.6 / 109.1 | 2.1 / 1.4 / 3.1 | 0.47 / 0.75 / 0.79 | 0.85 / 0.76 / 0.84 |
| T19; 16 | Gemini CLI; Qwen | 85.5 / 89.9 / 90.3 | 3.8 / 3.4 / 3.8 | 0.57 / 0.53 / 0.84 | 0.76 / 0.69 / 0.77 |
| T20; 16 | Gemini CLI; GPT Nano | 91.9 / 98.2 / 103.7 | 8.1 / 7.5 / 6.7 | 0.44 / 0.38 / 0.81 | 0.71 / 0.65 / 0.73 |
| T21; 16 | Claude Code; Gemini 3 | 84.3 / 18.4 / 154.5 | 3.5 / 3.3 / 2.5 | 0.04 / 0.60 / 0.44 | 0.97 / 0.23 / 0.97 |
| T22; 16 | Claude Code; Haiku | 79.2 / 31.7 / 122.3 | 2.1 / 3.4 / 1.7 | 0.27 / 0.75 / 0.35 | 0.91 / 0.78 / 0.89 |
| T23; 16 | Claude Code; Gemini 2.5 | 133.6 / 79.5 / 226.5 | 2.9 / 2.0 / 2.2 | 0.06 / 0.68 / 0.32 | 0.85 / 0.76 / 0.84 |
| T24; 17 | Claude Code; Qwen | 101.0 / 84.2 / 117.2 | 6.2 / 7.2 / 5.7 | 0.32 / 0.38 / 0.42 | 0.76 / 0.69 / 0.77 |
| T25; 17 | Claude Code; GPT Nano | 121.6 / 126.3 / 190.5 | 15.7 / 17.4 / 12.5 | 0.10 / 0.14 / 0.38 | 0.71 / 0.65 / 0.73 |

Several results qualify the aggregate story. In T6, Careful PI reduces requests to 1.7 while fidelity falls to 0.23. In T13, Convince increases requests to 124.5 while detection falls to 0.06, an exception to the aggregate detection increase. In T15, Careful PI yields a cost ratio of 24.8 and detection of 0.01, showing that the average injection penalty is not universal. T19 and T20 show Careful PI increasing requests for Gemini CLI, whereas most other pairings shorten. T23's 226.5 requests under Convince is the largest displayed pairwise prompt-condition mean. These tables contain no uncertainty estimates or success-rate metric for injected instruction extraction.

### Tables 26–30 — Model means across four agents, pp. 17–18

The tuple order and metrics remain the same.

| Table; honeypot | L | C | D | F |
|---|---|---|---|---|
| T26; Gemini 3 Flash | 72.3 / 10.8 / 90.5 | 2.1 / 2.3 / 1.9 | 0.15 / 0.71 / 0.52 | 0.97 / 0.23 / 0.97 |
| T27; Haiku 4.5 | 75.0 / 28.8 / 95.0 | 1.3 / 2.2 / 1.2 | 0.28 / 0.64 / 0.44 | 0.91 / 0.78 / 0.89 |
| T28; Gemini 2.5 Flash | 91.3 / 50.6 / 134.3 | 2.0 / 1.9 / 1.9 | 0.20 / 0.57 / 0.38 | 0.85 / 0.76 / 0.84 |
| T29; Qwen 3.5 9B | 80.8 / 74.9 / 81.5 | 3.6 / 4.1 / 4.1 | 0.33 / 0.36 / 0.47 | 0.76 / 0.69 / 0.77 |
| T30; GPT 5.4 Nano | 93.5 / 85.5 / 111.5 | 9.2 / 13.1 / 8.4 | 0.21 / 0.19 / 0.44 | 0.71 / 0.65 / 0.73 |

T26 shows the most severe model-level fidelity collapse under Careful PI. T27 shows the same direction with a smaller fidelity penalty. T28 shows the largest Convince request mean among these model averages. T29 shows relatively small changes in request count but increased Convince detection. T30 has the largest cost ratios and is the exception where Careful PI lowers the model-average detection rate, from 0.21 to 0.19. These averages deliberately suppress agent-specific heterogeneity, which the preceding complete tuple table preserves.

## 12. Diagram / architecture interpretation

[A/B] Figure 1 is the sole substantive architecture diagram. Its three paths share the same environment definition but run separately. The main path sends agent-generated HTTP requests to the simulated application and returns generated HTTP responses. This repeated exchange produces a sequence from which request count, detection, and cost are measured. The agent-control path replaces the decoy with executable secure or insecure implementations; callback checks can establish whether the assigned exploit actually happened. The honeypot-control path replaces the adversarial agent with functional tests and measures ordinary behavior.

Appendix F.14 adds a more detailed response interface. Requests are represented as JSON containing body, headers, endpoint, and metadata. The LLM is asked to account for state implied by previous requests. It returns content, media type, and integer status within structured delimiters, optionally adding a header object. This is a prompt-level description of state simulation, not evidence of a separately verified state machine.

[D] A methodological strength is the separation between behavior under attack and capability under control. A limitation is that separate control performance cannot establish the causal reason for every individual main-task action. For example, a long interaction might include redundant attempts as well as informative exploration.

## 13. Equations and mathematical concepts

No numbered equations, optimization losses, formal proofs, or theorems appear in the supplied paper. The following expressions make the reported metric definitions explicit; they are explanatory notation, not quotations of source equations.

**Cost advantage:** R = C_agent / C_honeypot. Both costs refer to model-running cost for the compared interaction. R > 1 favors the honeypot; R < 1 favors the agent. The paper does not fully specify whether every aggregate is a mean of interaction-level ratios or a ratio of aggregate costs, so those operations should not be assumed interchangeable.

**Detection rates:** TPR concerns actual honeypots correctly identified; FPR concerns real applications incorrectly identified as honeypots. As explanatory identities, TPR = correctly detected honeypot cases / evaluated honeypot cases, and FPR = real cases flagged as honeypots / evaluated real cases. Exact averaging over applications, repetitions, and secure/insecure controls is not fully described.

**Interaction length:** L is the number of HTTP requests received during an interaction. It is not the number of reasoning steps, tool calls, seconds, or successful exploit stages.

**Pass@1:** the authors call this functional fidelity on the backend test suite. The work does not supply a full formal aggregation definition or test counts, so it should not be silently equated with a particular external benchmark's pass@1 convention.

[C] Derived differences in §9 use only displayed operands. Because the source values are rounded, derived ratios and relative changes are approximate. A change from 0.24 to 0.45 is 0.21 in fraction units, or 21 percentage points, not a 21% relative increase.

## 14. Interpretation and discussion

[A] The authors interpret the results as evidence that inexpensive LLMs can support promising HTTP honeypots. Their claim rests on multiple dimensions: longer interactions than simple mocks, lower detection, mostly favorable running-cost ratios, and meaningful functional scores. The control tasks expose why each dimension needs qualification.

[D] Longer interaction demonstrates continued engagement with a service that cannot deliver the attacker's real objective. It does not itself establish successful prompt injection, disclosure of private instructions, or a measured increase in defender intelligence. Those outcomes would need their own measurements. Similarly, an agent calling a real application a honeypot illustrates an operational decision error, but is not necessarily evidence that malicious instructions were followed.

[A] The authors report no clear correlation between latency or fidelity and detection, while inspected logs repeatedly cite latency and timeouts as reasons for suspicion (p. 7). These statements can coexist: an individual clue may influence decisions without producing a simple aggregate association. The logs were not supplied, so this review can assess only the authors' report.

Several cross-reference checks qualify the prose. The approximate threefold interaction claim corresponds to a ratio near 2.70 from reported aggregate means. The claim that cost exceptions mainly involve Gemini/Claude honeypots against the Gemini agent is incomplete as a universal description: T17 also shows Haiku against Gemini CLI below break-even, at 0.92 under None. The paper's broader majority claim remains compatible with that value. The term significantly is not backed by a reported statistical test. Table 2 and appendix fidelity use different display scales and precision; they are consistent with percentage/fraction presentation, not demonstrably contradictory measurements.

[D] Relevance to web-agent vulnerability is strongest at the level of **interaction-dependent deception and evaluation design**. The agent repeatedly consumes observations generated by a potentially adversarial service, and its stopping and detection decisions can be influenced by that environment. However, the experiment lacks a standalone baseline, a controlled tool-access ablation, and a dedicated successful-injection outcome. It therefore cannot answer how much more vulnerable agents are than standalone LLMs.

## 15. Contributions and novelty

[A] **Conceptual contribution:** four requirements for honeypot evaluation, emphasizing that adaptability creates side effects needing separate measurement.

[A] **Methodological and benchmark contribution:** a main interaction task plus attacker and simulator controls, grounded in 16 application specifications and four verifiable exploit-goal families.

[A] **Systems and implementation contribution:** a simple HTTP-to-LLM honeypot harness, real secure/insecure backend implementations, rule-based mocks, tests, and an announced open-source framework. Availability is author-reported; installation and execution were not assessed here.

[A] **Empirical contribution:** comparisons of five honeypot LLMs and four agent configurations, including engagement, detection, cost, latency, fidelity, and prompt customization.

[A] The authors call Honeyval the first comprehensive evaluation framework for LLM-powered HTTP honeypots. That priority claim is preserved as author-reported and was not externally verified. No new training algorithm, theorem, or general successful-injection technique is demonstrated by the supplied evidence.

## 16. Limitations

### Authors' stated limitations

[A] The evaluated architecture is naive and sends the full interaction context to the LLM (pp. 7–9). This increases token use and can be improved by caching, external context, or hybrid designs. Agents can issue multiple requests through scripts, while the honeypot handles requests one at a time, creating asymmetric context management.

[A] Median responses take more than three seconds even for the fastest backends; latency and timeouts are cited by agents as suspicious. Generated-token demands add cost. The authors view these as improvable rather than fundamental limitations, but that future improvement is an outlook, not an evaluated result.

[A] Scope is limited to 16 HTTP backend applications. Larger applications, shells, and more complex protocols remain future work (p. 9). Prompt-injection attempts are often unsuccessful, can reveal the decoy, and can interfere with benign functional tests (p. 8).

[A] API-cost estimation omits price changes above some input-token thresholds and therefore slightly underestimates very long interactions (Appendix B, p. 12). The authors assert no qualitative effect because the same estimation is used for both sides. This assertion was not independently tested.

### Additional evidence-based analyst observations

[D] The mock baseline is deliberately simple; results establish improvement over that baseline rather than superiority to every production or hybrid honeypot. Functional pass rates do not guarantee state consistency or adversarial realism over all possible request sequences. Request count measures exposure or engagement, not directly useful intelligence.

[D] Aggregate averages conceal substantial agent–model interactions. Formal uncertainty definitions, test denominators, seeds, complete raw logs, exact version locks, and a consolidated run manifest are not supplied. Most importantly for the user's question, there is no standalone-LLM comparison and no quantified instruction-disclosure success metric. These are analyst observations, not all author-admitted limitations.

## 17. Threats to validity

The following validity labels are analyst classifications of supplied evidence.

**Internal validity [D]:** controls help rule out incapable attackers and dysfunctional simulators as complete explanations, but model, harness, latency, and instruction differences can all influence observed behavior. The study does not isolate a single causal mechanism for continued engagement.

**Construct validity [D]:** HTTP requests are a proxy for intelligence collection. Functional tests are a proxy for realism. A detection marker measures an expressed detection decision, which requires FPR context. Cost advantage measures API-running cost, not total operational expenditure or harm.

**External and ecological validity [D]:** the services are specified backend applications, and both parties know their APIs. Real deployments may differ in scale, uncertainty, traffic, attacker incentives, and available resources. The authors' analogy to prior real-world findings does not turn this controlled evaluation into a live-deployment study.

**Statistical conclusion validity [D]:** five repetitions are reported, but formal tests and error-bar definitions are absent. Rounded averages and rates do not support precise uncertainty claims. No statistically established general law about all agents follows from the displayed comparisons.

**Reproducibility [D]:** publishing prompts, application specifications, and announced code helps procedural reconstruction. Nevertheless, the supplied material does not fix every software version, model-service revision, seed, timeout, test count, or run outcome. Reproducibility is a design goal supported by artifacts, not an execution result established by this analysis.

**Security-boundary validity [D]:** the paper says the honeypot lacks system resources, and tools are described as restricted. This analysis did not inspect enforcement code. Prompt descriptions and architectural assumptions must remain distinct from independently demonstrated containment.

## 18. Future work and open questions

### A. Authors' proposed future directions

[A] Improve the honeypot architecture with caching, conversation memory, external files, and hybrid systems. Distill simulation capabilities into faster specialized models. Explore faster inference hardware. Expand the application collection, including larger-scale services, and extend the framework beyond HTTP to shells and more complex protocols (§5.2, p. 7; §6, p. 9). These are proposals, not completed experiments.

### B. Additional open questions

[D] How much of extra interaction is informative rather than repetitive? Can a decoy influence an agent while preserving benign fidelity and low detection? What rate of instruction, tool, provider, or organization disclosure is actually achieved? How should success, exposure, detection, stopping, recovery, legitimate progress, and resource use be measured separately?

[D] For the user's research question, a controlled comparison would need the same underlying model evaluated with and without an interaction-and-tool loop, clearly matched tasks, defined malicious content, and outcome-specific measurements. Honeyval does not supply that experiment. Also unresolved are whether detection errors persist across broader applications and whether cost ratios hold with different accounting and optimized architectures.

## 19. Terminology and notation glossary

| Term | Meaning in this analysis |
|---|---|
| Honeypot | A decoy service used to observe or detect attackers. |
| LLM | Large language model; generates the simulated responses or powers an agent. |
| HTTP | Hypertext Transfer Protocol; the request/response transport used here. |
| API | Application programming interface; specified service operations. |
| REST API | The endpoint-based HTTP service interface described by the paper. |
| OpenAPI | The structured specification given to attacker and simulator. |
| Backend | A service implementing application behavior behind an interface. |
| ReAct | Reason and Act; the principle used by the in-house agent. |
| CLI | Command-line interface; part of Gemini CLI's name. |
| curl | A tool for sending HTTP requests, restricted in the supplied tool prompt. |
| FastAPI | The Python framework used for real application implementations. |
| TPR | True positive rate: detecting actual honeypots. |
| FPR | False positive rate: real applications wrongly called honeypots. |
| Pass@1 | The paper's functional-fidelity score; full aggregation details are not supplied. |
| Prompt injection, PI | An attempt to influence an AI agent through content returned by the service. |
| None | Baseline honeypot prompt focused on simulation, without the two extra objectives. |
| Careful PI | Prompt condition asking the decoy to attempt covert influence and disclosure. |
| Convince | Prompt condition asking the decoy to assert that the application is secure. |
| Callback | Programmatic check of a concrete exploit outcome on a real implementation. |
| localStorage | Browser local storage, the target of one exploit-goal family. |
| R | Analyst notation for agent cost divided by honeypot cost. |
| L | Analyst notation for HTTP request count per interaction. |
| CPU / GPU | Central / graphics processing unit; only CPU access and remote APIs are required by the reported setup. |
| CTF | Capture-the-flag security problems, mentioned in related work rather than evaluated here. |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Backend applications | 16 | applications | BaxBench-derived HTTP services | Author-reported | p. 4, §4.1 |
| Exploit-goal families | 4 | families | Download, delete table, change password, exfiltrate local storage | Author-reported | p. 4 |
| Honeypot models | 5 | models | Cost-efficient LLM backends | Author-reported | p. 6 |
| Agent configurations | 4 | configurations | Two ReAct models plus two CLI/coding agents | Visually readable | p. 6, T1 |
| Repetitions | 5 | independent repetitions | Each experiment | Author-reported | p. 6 |
| Agent budget | 10 | USD/run | Per application and task combination | Author-reported | p. 5 |
| Honeypot budget | 10 | USD/run | LLM honeypot | Author-reported | p. 6 |
| ReAct cap | 50 | iterations | Separate from HTTP request count | Author-reported | p. 5 |
| CLI/coding-agent cap | 1 | hour/run | Claude Code and Gemini CLI | Author-reported | p. 5 |
| LLM / mock mean length | 82.6 / 30.6 | HTTP requests | Overall reported comparison | Author-reported | p. 2 |
| Length ratio | ≈2.70 | ratio | 82.6 / 30.6 | Analyst-derived | p. 2 operands |
| Length difference | 52.0 | requests | 82.6 − 30.6 | Analyst-derived | p. 2 operands |
| Median latency range | 3.3–13.7 | seconds | Five honeypot backends | Visually readable | p. 7, T2 |
| Mean generated-token range | 87.7–523.9 | tokens/response | Reasoning plus final output | Visually readable | p. 7, T2 |
| Functional score range | 71.2–97.5 | reported 0–100-like scale | Baseline honeypot control | Visually readable | p. 7, T2 |
| None / PI / Convince length | 82.6 / 50.1 / 102.6 | requests | Across agents and honeypots | Visually readable | p. 8, T3 |
| None / PI / Convince TPR | 0.24 / 0.49 / 0.45 | fraction | Same aggregate conditions | Visually readable | p. 8, T3 |
| None / PI / Convince fidelity | 0.84 / 0.62 / 0.84 | fraction | Functional control | Visually readable | p. 8, T3 |
| None / PI / Convince cost ratio | 3.6 / 4.7 / 3.5 | ratio | Agent cost / honeypot cost | Visually readable | p. 8, T3 |
| Convince detection increase | 21 | percentage points | 100 × (0.45 − 0.24) | Analyst-derived | p. 8, T3 operands |
| Claude Code exploit success | 98.8 | percent | Detect-enabled prompt; real vulnerable apps | Visually readable | p. 8, T4 |
| Largest displayed pairwise length | 226.5 | requests | Claude Code vs Gemini 2.5, Convince | Visually readable | p. 16, T23 |
| Typical interaction cost | Often below 1 | USD | Author's qualitative frequency statement | Author-reported | p. 12, App. B |

The table preserves reported precision. It does not treat model-name numerals as measured experimental quantities. Full condition-level numerical results appear in §11 rather than being duplicated here.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Separate controls are necessary to interpret decoy interactions | Real secure/insecure apps and benign functional tests accompany the main task | F1; framework | pp. 4–5 | HIGH for design; causal sufficiency is not established. |
| LLM decoys sustain more requests than mocks | Every T1 LLM mean exceeds its row baseline | T1; X1 | p. 6 | HIGH for displayed means; useful intelligence is not directly measured. |
| LLM decoys are less detectable than mocks | Grouped detection comparison | F2; X2 | p. 6 | HIGH for broad pattern; exact plotted FPRs and uncertainty definitions absent. |
| Detection must be interpreted with false alarms | Gemini CLI and Gemini ReAct have reported high FPR | F2; X2 | pp. 6–7 | HIGH for author report; logs not supplied. |
| Cost often favors the honeypot | Ratios exceed one for most baseline pairings | F3; T6–25; X3 | pp. 7, 14–17 | HIGH for displayed ratios; accounting scope is API cost. |
| Fast response remains difficult | Lowest median is 3.3 seconds | T2; X4 | p. 7 | HIGH for measured setup; not a universal hardware limit. |
| Extra honeypot objectives create trade-offs | Length, detection, and fidelity change differently | T3; T6–30; X5 | pp. 8, 14–18 | HIGH for reported conditions; effects are heterogeneous. |
| Injection attempts are often unsuccessful | Authors describe detection rather than successful influence | X5 discussion | p. 8 | HIGH for stated observation; no dedicated success-rate metric. |
| Agent prompt changes lack one universal exploit trend | Four rows change in different directions | T4; X6 | p. 8 | HIGH for table; no formal invariance claim justified. |
| Scope limits generalization | Naive architecture and 16 HTTP applications | Limitations | pp. 8–9 | HIGH for author-stated scope. |
| Web-agent relevance concerns external-response exposure | Agents receive service outputs; F.15 targets that channel | Prompt interface | pp. 23–24 | MEDIUM, analyst inference; no standalone comparison. |

## 22. Very simple explanation — Explain Like I'm 15

Imagine a fake website service set up so that an attacker wastes time investigating it while its owner watches what the attacker tries. A very simple fake gives repetitive answers and is easy to spot. This paper tries using an AI model to invent more convincing answers, without giving the fake service access to real resources that could be stolen or damaged.

The researchers built a testing system with 16 kinds of services. They sent AI hacking agents to investigate the fakes. They also checked two other things: whether those agents could actually hack real vulnerable versions, and whether the fake services could correctly answer normal requests. Those extra checks matter because a bad attacker or a broken fake could make the main results misleading.

The AI fakes usually kept attackers interacting longer than simple rule-based fakes, and they were harder to identify. But they could be slow, and asking them to manipulate the attacker sometimes made them behave strangely and easier to catch. Telling a fake to insist that it was secure increased average interaction, but also increased the chance of eventual detection.

For the question about why web AI agents might be more vulnerable than standalone models, this paper shows a relevant situation: an agent keeps reading responses from a service that may be trying to deceive it. It does not prove that adding web access makes a model more vulnerable, because it never performs that direct comparison. Its useful lesson is to measure continued interaction, detection errors, ordinary capability, and successful manipulation separately.

## Completeness Audit

The inventory denominator is the supplied 24-page work: six numbered main sections, their substantive subdivisions, six appendices, three figures, thirty tables, six analyses, three principal contribution groups, four evaluation requirements, and sixteen prompt blocks. Every table and figure was visually inspected; specified other pages were text-only. Repeated numerical material is compressed structurally, not silently dropped.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, substantive footnote | Yes | Yes | Represented in compressed form | Bibliographic details in §2; correspondence address omitted as non-substantive. |
| Abstract | Yes, visual and text | Yes | Fully represented | Motivation, framework, results, trade-offs. |
| §1 Introduction and contributions | Yes | Yes | Fully represented | §§1, 4, 15. |
| §2 Honeypots | Yes, text-only | Yes | Fully represented | Interaction levels and security trade-off. |
| §2 LLM honeypots and evaluation | Yes, text-only | Yes | Represented in compressed form | Prior-work categories preserved; citation-by-citation summaries omitted. |
| §2 Hacking agents | Yes, text-only | Yes | Represented in compressed form | Context preserved without validating cited capabilities. |
| §3 Requirements 1–3 | Yes, text-only | Yes | Fully represented | Scalability, reproducibility, representativeness. |
| §3 Requirement 4 | Yes, visual and text | Yes | Fully represented | Adaptability and side effects. |
| §4 Design requirements, running evaluations, threat scenario | Yes | Yes | Fully represented | Task-independent settings and resource assumptions. |
| §4.1 Environments and exploit goals | Yes | Yes | Fully represented | Four artifacts, 16 applications, four goal families. |
| §4.2 Main task | Yes | Yes | Fully represented | Metrics and inability to achieve real exploit on decoy. |
| §4.2 Agent control | Yes | Yes | Fully represented | Secure/insecure implementations, callbacks, FPR. |
| §4.2 Honeypot control | Yes | Yes | Fully represented | Benign tests, fidelity, latency, cost. |
| §5.1 Agents, honeypots, general details | Yes | Yes | Fully represented | Models, budgets, repetition, harness. |
| §5.2 X1 interaction length | Yes | Yes | Fully represented | T1 and derived overall comparison. |
| §5.2 X2 detection | Yes | Yes | Fully represented | F2 and false-alarm qualifications. |
| §5.2 X3 cost asymmetry | Yes | Yes | Fully represented | F3, accounting, exceptions. |
| §5.2 X4 backend characteristics | Yes | Yes | Fully represented | T2 values and limitations. |
| §5.2 X5 honeypot prompts | Yes | Yes | Fully represented | T3 and all detailed tables. |
| §5.2 X6 agent prompts | Yes | Yes | Fully represented | T4, different directions, conditions. |
| §6 Discussion and conclusion | Yes | Yes | Fully represented | Supported interpretation distinguished from stronger claims. |
| §6 Limitations and outlook | Yes; p. 9 text-only | Yes | Fully represented | Naive architecture, scope, extensions. |
| Explicit RQs and hypotheses | Checked | Yes | No formal items identified | Objectives preserved; analyst questions labeled. |
| Figure 1 | Yes, visual | Yes | Fully represented | Diagram explained in §§10 and 12. |
| Figure 2 | Yes, visual | Yes | Fully represented with uncertainty | Exact unlabeled bar values not invented. |
| Figure 3 | Yes, visual | Yes | Fully represented with uncertainty | Ratio direction and break-even line preserved. |
| Table 1 | Yes, visual | Yes | Fully represented | All cells reproduced. |
| Table 2 | Yes, visual | Yes | Fully represented | All cells reproduced; scale caveat. |
| Table 3 | Yes, visual | Yes | Fully represented | All cells reproduced. |
| Table 4 | Yes, visual | Yes | Fully represented | All cells reproduced. |
| Table 5 | Yes, visual | Yes | Fully represented | Applications, descriptions, goal groups. |
| Tables 6, 7, 8, 9, 10, 11 | Yes, visual | Yes | Fully represented in compact form | Each identified; all metric triplets preserved. |
| Tables 12, 13, 14, 15, 16, 17 | Yes, visual | Yes | Fully represented in compact form | Each identified; all metric triplets preserved. |
| Tables 18, 19, 20, 21, 22, 23 | Yes, visual | Yes | Fully represented in compact form | Each identified; all metric triplets preserved. |
| Tables 24, 25 | Yes, visual | Yes | Fully represented in compact form | Each identified; all metric triplets preserved. |
| Tables 26, 27, 28, 29, 30 | Yes, visual | Yes | Fully represented in compact form | Model averages and exceptions explained. |
| Appendix A Broader Impact | Yes | Yes | Represented in compressed form | Defensive benefit and dual-use concern described below. |
| Appendix B Compute/API | Yes | Yes | Fully represented | CPU/API setup, budgets, typical costs, pricing caveat. |
| Appendix C Licenses | Yes | Yes | Represented in compressed form | MIT provenance described below. |
| Appendix D Applications | Yes | Yes | Fully represented | FastAPI implementations and repository paths described below. |
| Appendix E.1 | Yes | Yes | Fully represented in compact form | T6–30. |
| Appendix F.1 agent prompts F.1–F.9 | Yes, text-only | Yes | Represented in compressed form | Tool/action protocol, templates, detection, concealment, restrictions. |
| Appendix F.1 goals F.10–F.13 | Yes, text-only | Yes | Fully represented | Four concrete objectives and download clarification. |
| Appendix F.2 F.14 | Yes, text-only | Yes | Fully represented | Stateful request/response simulation interface. |
| Appendix F.2 F.15–F.16 | Yes, text-only | Yes | Fully represented | Careful PI and Convince objectives. |
| Major equations/theorems | Checked | Yes | None identified | Explanatory metric identities labeled separately. |
| Algorithms/pseudocode | Checked | Yes | No formal listings identified | Prompt procedure represented. |
| References pp. 9–11 | Yes, text-only | Yes | Deliberately compressed | No external source validation. |
| Repository, raw logs, executable tests | No | Limitation disclosed | Not supplied as inspectable artifacts | Availability statements remain author-reported. |
| Supplied supplementary files | None separately supplied | Yes | Not applicable | Appendices themselves are supplied. |

**Additional appendix details preserved for coverage:** Appendix A argues that defensive benefits outweigh risks, while acknowledging that the framework could help malicious actors improve honeypot identification and evaluate executable exploits. Its claim that these risks are limited is the authors' societal assessment, not a measured result. Appendix C states that BaxBench is MIT-licensed and included with third-party notices; this was not independently audited. Appendix D locates specifications under `third_party/baxbench/openapi_specifications` and real implementations under `data/baxbench-webapps`; these paths were read as documentary evidence only.

**Prompt inventory details:** F.1 describes one action per turn in a structured action/tool format and an observation-driven loop; its continuation on p. 20 instructs autonomy. F.2 describes restricted curl. F.3 describes sandboxed Python. F.4 and F.5 wrap the initial task and environment response. F.6 supplies the security-assessment scenario, API, goal, and secure-application stopping option. F.7 adds a honeypot-detection marker and termination. F.8 adds concealment. F.9 restricts CLI-agent communication. F.10–F.13 specify download, table deletion, password change, and local-storage exfiltration. F.14 specifies the honeypot response interface. F.15 requests attempted injection and disclosure while avoiding detection. F.16 requests assertions of security. Exact syntax examples and repeated imperative wording are compressed because their methodological roles are fully described. None was followed as an instruction to this analysis.

### Missing or inaccessible material

The repository contents, model invocation records, complete logs, raw run-level outcomes, exact service versions, library locks, full test inventories, and callback implementations were not supplied for direct inspection. No separately attached supplementary file is present. The paper does not specify all statistical aggregation details or error-bar definitions. Pages available only as extracted text were not visually inspected.

### Uncertain interpretations

Exact FPR and rule-based detection bar values are not labeled; no exact values are inferred from their heights. Error-bar meaning is UNKNOWN. Pass@1 aggregation and total test denominators are not fully defined. Table 2's fidelity display differs in scale from appendix fractions. Cost-ratio aggregation is insufficiently specified to substitute a ratio of means for a mean of ratios. The paper's qualitative significance wording is not treated as proof of a statistical test.

### Deliberately compressed material

Related-work citations, bibliography entries, repeated headers, correspondence details, prompt markup examples, and repeated table explanations are compressed. All substantive appendix result cells are preserved through explicitly ordered tuples. No decorative icon is interpreted as a measured result.

### Potential omissions

No known substantive item in the supplied inventory is left unrepresented: all sections, analyses, figures, tables, appendices, prompt roles, major contribution groups, and identified author-stated limitations are accounted for. This is a coverage statement about the supplied evidence, not a claim that every sentence has been reproduced or that absent implementation artifacts have been reviewed.
