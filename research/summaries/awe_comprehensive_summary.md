## Stage 0 — Document Accessibility Report

The supplied main document is available as extracted text for physical PDF pages 1–9. Six page images are also supplied: pages 1, 2, 3, 4, 5, and 7. Thus, textual coverage extends across all nine supplied pages, while direct visual inspection covers six pages. Pages 6, 8, and 9 are text-only in this analysis. The visible section sequence reaches the conclusion and a reference list ending at reference [14]; this supports treating the supplied nine pages as the available paper, but does not independently establish that no other version or supplemental artifact exists.

Figures 1–4 are visually available. Tables II and III are visually available on page 7. Table I is available through extracted text on page 6, without a supplied page image. Main prose and table entries are readable. Some small diagram labels and plot markings are less legible than the surrounding prose, so exact values are taken from readable labels or supplied text rather than guessed from pixel positions. No major displayed equation, theorem, proof, or separately numbered pseudocode algorithm appears in the supplied material. No appendix is present. No supplementary file is supplied, and the accessibility metadata detects no embedded attachment or supplementary reference. The paper does advertise a source-code repository; that repository was not inspected.

OCR was not needed because native/extracted text and page images were supplied. No tools, browsing, external references, repository inspection, or memory lookup were used. The source hash is the identifier supplied by the user; it was not independently recomputed. All source content is treated as evidence rather than instructions.

Evidence labels used below: [A] AUTHOR-REPORTED identifies statements made by the paper; [B] DIRECTLY OBSERVABLE identifies readable visual content; [C] ANALYST-DERIVED identifies calculations from supplied numbers; [D] ANALYST INTERPRETATION identifies explicitly labeled reasoning beyond the authors' wording. No [E] external information is introduced. Confidence describes fidelity to the supplied evidence, not independent proof that the system behaves as claimed.

## 1. Plain-language orientation

[A; pp. 1, 3–5] This paper introduces AWE, an automated system for finding and exploiting vulnerabilities in web applications. Its title is **AWE: Adaptive Agents for Dynamic Web Penetration Testing**. The introduction expands AWE as Adaptive Web Exploitation Framework. The authors are Akshat Singh Jaswal and Ashish Baghel, both affiliated with Stux Labs, with an equal-contribution footnote. Page 1 identifies the Workshop on LLM Assisted Security and Trust Exploration, LAST-X 2026, held on 27 February 2026 in San Diego, California, and gives DOI 10.14722/last-x.2026.23037.

The central problem is how to make automated security testing adapt to application-specific behavior without spending excessive time and model tokens. According to the authors, conventional scanners repeat known attack patterns, while general-purpose large language model systems explore too freely and do not consistently turn subtle feedback into effective exploits. AWE combines specialized attack procedures, persistent state, selective language-model assistance, and concrete exploit verification.

[A; pp. 6–8] The main result is a trade-off. On 104 XBOW challenges, AWE solves 54, or 51.9%, while MAPTA solves 80, or 76.9%. AWE nevertheless solves more cross-site scripting challenges: 20 of 23 against MAPTA's 13 of 23. It also solves two of three blind SQL injection challenges against one of three. AWE uses fewer tokens and has lower reported total API cost and shorter solve times. These advantages do not mean it provides broader overall coverage.

[D] Relevance to the user's question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,' is indirect. This is a paper about AI agents discovering vulnerabilities in web applications. It does not compare the susceptibility of web agents and standalone language models to adversarial compromise. It can inform a discussion of how browser access, HTTP interaction, authentication, memory, and tool execution change what an agent can do, but it cannot establish that web agents are more vulnerable or identify a measured cause of such a difference.

## 2. Document roadmap and inventory

The paper is a mixed cybersecurity, computer-systems, and empirical AI evaluation paper. It proposes a system and evaluates exploit success and operational efficiency. It is not a survey, theoretical proof, or controlled study of attacks against AI agents.

| Inventory ID | Original component | Location | Role |
|---|---|---|---|
| S1 | Abstract and index terms | p. 1 | Contribution and headline findings |
| S2 | I. Introduction | p. 1 | Motivation and problem framing |
| S3a | II.A System Model | p. 1 | Black-box target interaction |
| S3b | II.B Attacker Capabilities and Goals | pp. 1–2 | Requests, accounts, LLM assistance, budgets |
| S3c | II.C Trust Relationship | p. 2 | Trusted infrastructure and malicious inputs |
| S3d | II.D Scope | p. 2 | Included and excluded vulnerability families |
| S4a–c | III.A–C Background and Related Work | pp. 2–3 | Scanners, LLM testers, architectural gaps |
| S5a | IV.A Orchestration Layer | pp. 3–4 | Global state, planning, resource governance |
| S5b | IV.B Specialized Agents Layer | p. 4 | Vulnerability-specific procedures |
| S5c | IV.C Foundation Layer | pp. 4–5 | Memory, reconnaissance, verification |
| S5d | Design Rationale | p. 5 | Specialization, state, evidence |
| S6a–f | V.A–F Methodology | pp. 5–6 | Benchmarks, baseline, models, configuration, metrics, success |
| S7a | VI.A Evaluation on DVWA | p. 6 | Model comparison within AWE |
| S7b | VI.B Evaluation on XBOW Benchmark | p. 6 | Overall system comparison |
| S7c–f | VI.C–F | pp. 7–8 | Categories, failures, efficiency, synthesis |
| S8 | VII. Discussion | p. 8 | Architectural interpretation |
| S9 | VIII. Limitations | p. 8 | Four explicit limitations |
| S10 | IX. Conclusion | p. 8 | Contribution and hybrid future direction |
| R1 | References [1]–[14] | pp. 8–9 | Cited artifacts and related literature |
| F1 | Figure 1 | p. 3 | Three-layer architecture |
| F2 | Figure 2 | p. 4 | Five-phase XSS workflow |
| F3 | Figure 3 | p. 5 | Three-model detection success comparison |
| F4 | Figure 4 | p. 7 | Four payload-attempt distributions |
| T1 | Table I | p. 6 | Overall XBOW performance |
| T2 | Table II | p. 7 | Cost and token efficiency |
| T3 | Table III | p. 7 | Seven vulnerability-category comparisons |

The distinct analyses are X1: DVWA model selection and success rates; X2: payload-iteration behavior; X3: overall XBOW comparison; X4: category-specific comparison; X5: failure and solve-overlap analysis; and X6: cost, token, and timing analysis. No formal research-question or hypothesis numbering is present. The substantive footnote records equal author contribution. Publication details and reference entries are accounted for but compressed rather than reproduced verbatim.

## 3. Background and context

[A; pp. 1–5] Penetration testing means trying to demonstrate exploitable weaknesses in an application. In this paper, merely noticing a suspicious response is insufficient for an XBOW success: the system must retrieve a hidden flag through a verified exploit. A flag is the benchmark's success artifact, not a general-purpose measure of every possible real-world security outcome.

A payload is an input designed to exercise a suspected weakness. Context matters because the same text can be interpreted differently depending on where the application inserts or processes it. For example, the paper distinguishes quoted attributes, unquoted attributes, JavaScript string literals, and raw HTML insertion when analyzing cross-site scripting. This is the paper's reason for using specialized context analysis before generating candidate payloads.

Large language models, abbreviated LLMs, generate or interpret text and structured information in AWE. They do not replace every component. The orchestration model selects relevant agents from reconnaissance evidence; specialist agents apply structured tests and sometimes ask a model for constrained payload candidates. Memory records prior attempts and observations. Verification checks whether a candidate produces the required behavior.

[A; pp. 2–3] The authors distinguish traditional Dynamic Application Security Testing, or DAST, tools from LLM-based penetration-testing systems. They describe tools such as Burp Suite, OWASP ZAP, Nuclei, and sqlmap as relying on signatures, templates, or heuristics. They characterize PentestGPT as primarily assistive and describe AutoPT, AutoAttacker, CAI, and related systems as moving toward autonomous orchestration. These are the authors' descriptions of prior work; the cited systems were not independently inspected here.

MAPTA is the principal comparison system. The paper describes a Coordinator for planning, Sandbox agents for execution in isolated Docker environments, and a Validation agent that converts candidates into verified proof-of-concept exploits. A proof of concept, or PoC, is a concrete demonstration of exploitability. MAPTA's general-purpose execution and exploration are important to interpreting its broader coverage.

## 4. Research problem and gap

**Existing problem [A; p. 1]:** AI-assisted development, no-code platforms, and rapid deployment can produce applications faster than existing security tooling can adapt. The authors argue that application vulnerabilities persist despite improved development practices.

**Shortcomings attributed to prior approaches [A; pp. 2–3]:** Static scanners cannot readily synthesize new inputs for unusual sanitization or adapt their strategy to complex response behavior. General-purpose LLM agents may generate a few generic payloads, misinterpret filtering, fail to preserve useful context, and abandon exploration prematurely. The paper specifically mentions filter ordering, encoding quirks, type coercion, template-engine semantics, and interactions among multiple parameters.

**Research gap [A; p. 3]:** Receiving server feedback is insufficient unless a system has the domain-specific, stateful, iterative mechanisms required to turn that feedback into targeted exploit construction. The authors position AWE as filling that architectural gap.

**Motivation [A; pp. 1, 5]:** A practical tester should combine adaptability with low operational overhead, explainable procedures, and evidence-backed findings. Its resource use should fit realistic time and API-cost constraints.

**Scope [A; p. 2]:** AWE focuses on vulnerabilities discoverable through black-box manipulation of application inputs. It is not a universal tester for every security weakness. Its scope includes several injection families and authenticated unauthorized-object-access testing, but excludes attacks requiring capabilities or semantic reasoning outside the stated model.

[D] The supplied experiments compare complete systems and models inside AWE. They do not isolate every proposed architectural mechanism. Therefore, the gap and proposed remedy are clearly articulated, but the causal contribution of each component remains only partially established.

## 5. Research questions, objectives, and hypotheses

**Explicit formal research questions:** None are stated as numbered or separately formulated research questions in the supplied paper.

**Explicit objectives [A; pp. 1, 5–6]:** Build an autonomous, intelligent, transparent vulnerability-discovery system; combine domain-specific exploitation logic with LLM assistance; assess effectiveness and efficiency under realistic attacker constraints; compare AWE with MAPTA; and use controlled DVWA experiments to select an underlying language model.

**Explicit hypotheses:** No formal null hypothesis, alternative hypothesis, preregistered prediction, or hypothesis test is reported.

**Analytical questions used to organize this report [D]:** Does AWE find more verified exploits in its intended categories? How much overall coverage does it sacrifice? Which model works best within its fixed agent procedures? What operational resources does it consume? Where does its specialized architecture fail? These are analyst organizing questions, not quotations or formal author research questions.

**User-question boundary [D]:** Whether web AI agents are more vulnerable than standalone LLMs remains unanswered. The paper does not include a standalone-model control, adversarial prompt-injection experiment, agent-compromise metric, or matched comparison of the same model with and without tools.

## 6. Assumptions / Threat Model

[A; II.A–D, pp. 1–2] The target is a web application exposing parameterized Hypertext Transfer Protocol, or HTTP, endpoints. The system sends GET and POST requests and varies input placement. The authors list PHP, Python, Node.js, and Java as representative server-side environments. Applications may use input validation, output encoding, and application-layer firewalls.

The attacker has no privileged access to source code, runtime logs, server configuration, or internal application state. It can craft arbitrary HTTP requests and observe responses and timing. It may obtain ordinary authentication through benign registration or low-privilege accounts. Commercial LLM application programming interfaces, or APIs, help generate and adapt candidate inputs under cost constraints. The threat-model time budget is at most ten minutes per target endpoint.

The target stack is assumed uncompromised and behaves according to its implementation, even if that implementation contains vulnerabilities. Hosting infrastructure and network fabric are trusted and provide no special attacker access. Parameters, headers, cookies, and request bodies are potentially malicious. Dynamic client-side content can also be used in exploit construction.

Included families are cross-site scripting, SQL injection, server-side template injection, command injection, file inclusion/path traversal, XML external entity expansion, server-side request forgery, and unauthorized object access when credentials are available. Excluded areas include network- or protocol-level attacks, cryptographic weaknesses, and business-logic flaws requiring semantic knowledge or reasoning beyond observable request–response behavior.

**Boundary requiring care [D]:** The system-model wording says observations arise solely from HTTP responses and timing, while later design sections add controlled-browser observations such as script execution, document mutation, and dialogs. Browser execution is plainly part of the implemented design, so the opening observation model is narrower than the later description. This is a wording tension rather than evidence that browser verification was absent.

**Budget distinction [A/D]:** Section II gives an endpoint budget; Section V.D gives a ten-minute budget per challenge. The paper does not explain how endpoint budgets aggregate when a challenge has multiple endpoints.

## 7. Methodology

### Architecture and state

[A; IV, pp. 3–5] AWE has three layers. The Orchestration Layer maintains global exploitation context, coordinates agents, and enforces budgets. The Specialized Agents Layer contains vulnerability-specific exploitation modules. The Foundation Layer supplies reconnaissance, persistent memory, hybrid payload generation, and browser verification.

Global context includes discovered inputs, observed server transformations, authentication status, prior payload attempts, and successful exploitation steps. The orchestrator uses this state to prioritize relevant agents, avoid repeating failures, and potentially upgrade to authenticated testing when credentials become available. Its LLM acts as an adviser over reconnaissance and context rather than as the direct generator of every attack input. Resource monitoring covers tokens, runtime, and tool costs and can trigger early exit or reduced attention to low-yield agents.

### Specialist procedures

[A; IV.B, p. 4] The XSS agent first injects parallel canaries to identify where inputs reappear. It distinguishes fine-grained browser/document contexts, probes filtering behavior, summarizes discovered constraints, and obtains tailored candidate payloads. Concrete JavaScript execution is required for verification. The SQL injection agent combines deterministic inputs with database errors, backend identification, query-pattern inference, and controlled mutation. The server-side template injection agent uses engine-specific probes and constructs inputs consistent with the detected engine. The insecure direct object reference agent compares authenticated access behavior across resource identifiers. Other named agents follow the same general principles but receive less procedural detail.

### Foundation services

[A; IV.C, pp. 4–5] Short-term memory records attempted payloads, outcomes, inferred filters, and progress within an engagement. Long-term memory is intended to retain effective bypass patterns, sanitization signatures, and historical success rates across targets. Figure 1 labels SQLite persistence, session/long-term memory, and filter tracking. Browser verification runs candidates in a controlled browser and observes script execution, document changes, and dialog triggers. Reconnaissance discovers endpoints, extracts parameters, and identifies technologies.

### Evaluation data and controls

[A; V–VI, pp. 5–6] XBOW contains 104 vulnerable, containerized web applications across 26 vulnerability categories. Each embeds a hidden flag retrievable through an end-to-end exploit. The paper describes both single-step injections and multi-stage authenticated or filtered challenges. DVWA, Damn Vulnerable Web Application, provides repeatable vulnerability configurations and security levels for model comparison. Five DVWA categories are tested, with n=10 independent trials per model per vulnerability type as stated in V.A.

AWE is evaluated in aggressive configuration: deep reconnaissance and execution of all agents considered relevant by the orchestrator. Each challenge has a ten-minute budget. Challenges are isolated; memory is reset between challenges; headless Chromium verification uses a consistent configuration. The paper states that experiments use identical hardware, but gives no hardware specifications. MAPTA comparisons use its publicly reported per-challenge results rather than an explicitly documented local rerun.

### Metrics and omitted configuration

Effectiveness comprises overall and category solve rates and unique solves. Efficiency comprises time-to-solve and token use per successful exploit. Cost comprises total API spending and amortized cost per solved challenge. An XBOW success requires the correct flag through a verified exploit; partial progress is excluded.

The supplied work does not specify model sampling settings, random seeds, exact prompts, software versions, operating system, hardware model, detailed price schedule, retry rules, browser version, or a complete runnable evaluation recipe. No training procedure, train/validation/test split, annotation process, or statistical significance test is described. These omissions should not be filled with assumptions about common practice.

## 8. Experiments / Analyses

### X1 — DVWA model comparison

[A; V.A, VI.A, pp. 5–6; F3] Purpose: select a model while holding AWE's agent logic and verification procedures fixed. Conditions are Claude Sonnet 4, GPT-4o, and Gemini 2.0 Flash, across reflected, stored, and document-object-model-based XSS, basic/error-based SQL injection, and blind/time-based SQL injection. The stated sample is n=10 trials per vulnerability type for each model. Reflected XSS is 100% for all three. Content Security Policy-enforced stored XSS is 67% for Claude and GPT-4o and 50% for Gemini. Blind SQL injection is 70%, 60%, and 55%, respectively. Figure 3 explicitly labels Claude's five values as 100%, 67%, 80%, 80%, and 70%.

The authors select Claude for later experiments because of its overall success and iterative-refinement behavior. Caveat: these are models embedded in AWE, not standalone models or agent-free controls. The stated n=10 does not explain percentages such as 67% and 55%; see Section 14.

### X2 — Payload-iteration efficiency

[A/B; VI.A, p. 6; F4, p. 7] Purpose: assess how many candidate attempts are required for successful exploitation. The text and caption state that Claude converges in 10–40 attempts, GPT-4o needs about 20% more, and Gemini about 40% more. The actual four panels are difficulty/task distributions labeled DVWA Low, Medium, Hard, and XSSy, with average annotations of 10, 20, 40, and 12 attempts. The figure does not visibly separate the three model distributions. Sample counts and the meaning of XSSy are not specified in the supplied prose.

### X3 — Overall XBOW performance

[A; VI.B, p. 6; T1] Purpose: compare complete autonomous testing systems. AWE uses Claude Sonnet 4; MAPTA uses GPT-5, described as extended-reasoning mode. AWE solves 54/104, or 51.9%; MAPTA solves 80/104, or 76.9%. Reported average solve times are 53.1 and 190.8 seconds. The common stated budget is ten minutes per challenge. Caveat: the baseline uses published results, different models, and different execution capabilities.

### X4 — Category comparison

[A/B; VI.C, T3, p. 7] Purpose: determine where specialization helps or hurts. AWE wins on XSS and blind SQL injection, ties on SQL injection, XML external entities, and server-side request forgery, and loses on server-side template injection and command injection. Exact counts appear in Section 11. Categories contain only three to 23 challenges, so a large percentage difference may correspond to a single solved case.

### X5 — Failures and overlap

[A; VI.D, p. 7] AWE fails 50 challenges, MAPTA 24, and both fail 15. The authors attribute approximately one-third of AWE failures to intentionally excluded categories, another quarter to multi-step chains its agents cannot express, and the remainder to authentication irregularities, resistant filtering, or narrow exploitation windows. No challenge-by-challenge failure taxonomy is supplied. Derived overlap counts are given in Section 9.

### X6 — Resource efficiency

[A/B; VI.E, T2, pp. 6–8] Purpose: compare operational burden. Total token use is 1.12 million for AWE and 54.87 million for MAPTA in Table II; prose rounds MAPTA to 54.9 million. Costs are $7.73 and $21.38. Median solve times are 35.7 and 156.2 seconds. The authors summarize approximately 98% fewer tokens, 63% lower cost, and 4.4 times faster solves. Caveats include an inconsistent AWE cost-per-solve entry and incomplete information about failed-run timing and baseline measurement conditions.

## 9. Results and numerical interpretation

[A; T1, p. 6] MAPTA has higher overall coverage: 76.9% versus 51.9%. [C] From exact counts, the solve-rate gap is (80−54)/104 × 100 = 25 percentage points. AWE solves 26 fewer challenges. This is a coverage disadvantage, even though AWE leads in selected categories.

[A/B; T3, p. 7] For XSS, AWE solves 20/23 and MAPTA 13/23. [C] The exact count-based difference is 7/23 × 100 ≈ 30.43 percentage points. The relative increase in solved XSS challenges is (20−13)/13 × 100 ≈ 53.85%. The abstract's '+30.5%' should therefore not be read as a relative percentage improvement; it approximately matches an absolute percentage-point difference from unrounded rates. Table III prints rounded values of 87% and 57%.

[A/B] For blind SQL injection, AWE solves 2/3 and MAPTA 1/3. [C] This is approximately 33.33 percentage points and one additional solved challenge. Relative to MAPTA's single solve, it is a 100% increase in count. The tiny denominator is essential context.

[A/B] SQL injection is 6/6 for both; XML external entities and server-side request forgery are each 3/3 for both. Server-side template injection favors MAPTA, 11/13 versus AWE's 7/13. Command injection also favors MAPTA, 9/11 versus 5/11. Thus, even within the listed injection-oriented comparison, AWE does not lead uniformly.

[C; derived from T1/T2 and VI.E] The average-time ratio is 190.8/53.1 ≈ 3.59, while the median-time ratio is 156.2/35.7 ≈ 4.38. The paper's 4.4-times headline aligns with medians, not the average values in Table I. Token reduction using Table II is (54.87−1.12)/54.87 × 100 ≈ 97.96%. Total-cost reduction is (21.38−7.73)/21.38 × 100 ≈ 63.84%. These calculations explain the headline direction while preserving the reported operands.

[C; derived from VI.D and T1] If both fail 15 of 104, at least one system solves 104−15=89 challenges. Both solve 54+80−89=45. AWE alone solves 54−45=9; MAPTA alone solves 80−45=35. These are analyst-derived aggregate overlaps, not a reconstructed list of individual challenges.

## 10. Figure-by-figure interpretation

### Figure 1 — AWE system architecture, p. 3

[B] This is a layered block diagram with a yellow/orange Orchestration Layer at the top, a green Specialized Agents Layer in the middle, and a cyan Foundation Layer at the bottom. It has no numerical axes, scale, units, confidence intervals, or statistical annotations. Vertical connections link the layers, and branches from orchestration reach specialist agents.

The top contains Conversational Agent, Intelligent Orchestrator, and Token Tracker boxes. Readable labels associate these with memory handling/input control/tool chaining; model or agent selection, priority ranking, and early exit; and costs, timeout, and budget limits. The middle has eight boxes: XSS, SQLi, SSTI, IDOR, LFI, XXE, SSRF, and CmdInj. The bottom contains Recon Tool, Memory Manager, and Verifier. Labels identify endpoint discovery, form parsing, common paths, SQLite persistence, session and long-term memory, filter tracking, browser verification, console logs, and screenshots.

[A/D] The diagram supports the proposed separation of planning, specialized procedures, and shared services. It does not show enough interface detail to establish concurrency, message schemas, synchronization, or the exact movement of every state update. The lower placement of foundation services should not be mistaken for a strictly one-pass execution sequence; the prose describes iterative use of shared memory and verification.

### Figure 2 — Five-phase XSS detection pipeline, p. 4

[B] This flowchart starts at a target URL, proceeds through reconnaissance and a parameter queue, and then passes through five colored stages. Phase 1 is multi-canary injection; its branches distinguish reflected, stored, and document-object-model pathways. Phase 2 analyzes context, including attributes, tags, encoding, and character behavior. Phase 3 detects filters/security behavior. Phase 4 gives context and blocked-pattern information to an LLM to obtain mutated payloads. Phase 5 performs browser verification with Playwright and contains an alert-trigger decision.

The positive decision path reaches XSS Found. A negative path can return for another mutation, while exhausted retries end at XSS Failed. Some internal wording is small, so the broader flow is more reliable than every miniature label. The diagram has no quantitative axis or statistical encoding.

[A/D] The nearby prose explains the same logic: identify reflection context, infer filtering, tailor candidates, and require concrete browser evidence. This is the most procedural visual in the paper. It exposes a feedback loop rather than a single model response being accepted as proof. The shown alert decision is a specific visual check; the prose describes broader verification signals as well.

### Figure 3 — Model success rates, p. 5

[A/B] A grouped bar chart compares Claude Sonnet 4, GPT-4o, and Gemini 2.0 Flash. The horizontal axis lists reflected XSS, stored XSS, DOM XSS, basic SQL injection, and blind SQL injection. The vertical axis is Success Rate (%) on a linear 0–100 scale, with labeled intervals of 20. Claude is cyan/teal, GPT-4o green, and Gemini purple. A dashed horizontal reference line appears near 80%; its intended methodological role is not explained in the supplied text.

Claude's readable labels are 100%, 67%, 80%, 80%, and 70%. The text confirms reflected XSS at 100% for all models, stored XSS at 67%, 67%, and 50%, and blind SQL injection at 70%, 60%, and 55%. Other bar heights are visually comparable, but exact unlabeled values are not promoted to numerical facts here. The plot shows no error bars, confidence intervals, or significance markings.

The evidence supports model-dependent performance inside AWE. The stored-XSS result is a tie between Claude and GPT-4o, despite surrounding general wording about Claude outperforming both alternatives. The 67% and 55% rates require an unexplained denominator or aggregation if n=10 is the only trial count.

### Figure 4 — Payload-attempt distributions, p. 7

[B] Four histograms are arranged in a two-by-two grid under a payload-efficiency title. Panels are DVWA Low Difficulty, DVWA Medium Difficulty, DVWA Hard Difficulty, and XSSy Difficulty. Horizontal axes count payload attempts; vertical axes show frequency, with linear scales. Approximate displayed horizontal ranges are 6–18, 10–35, 25–60, and 8–20, respectively. Blue bars encode frequency, and red dashed vertical lines mark annotated averages: 10, 20, 40, and 12 attempts.

The distributions indicate that the hard condition requires more attempts and has a broader visible attempt range than the low condition. Exact bin counts, total samples, and uncertainty of the means are not supplied in a readable table. XSSy is not defined in the supplied text.

[A/B] A caption–visual inconsistency matters: the caption describes comparisons among Claude, GPT-4o, and Gemini, but the visible panels distinguish difficulties/tasks and provide no model-separated legend. Consequently, the caption and prose report the model ranking, while the plotted panels do not independently display that ranking. The chart supports difficulty-dependent attempt behavior more directly than a three-model comparison.

## 11. Table-by-table interpretation

### Table I — Overall XBOW performance, p. 6

[A; extracted text only] Rows are systems; columns are solve rate, average time in seconds, and model. AWE: 51.9% (54/104), 53.1 seconds, Claude Sonnet 4. MAPTA: 76.9% (80/104), 190.8 seconds, GPT-5. MAPTA is better on coverage, while AWE is better on reported average time. No uncertainty interval, significance test, or timing-denominator footnote is visible in the supplied extraction. The table does not establish whether both means use matched solved challenges.

### Table II — Cost and token efficiency, p. 7

[A/B] Rows compare AWE and MAPTA; columns give total cost, cost per solve, tokens, and tokens per solve. Dollar symbols identify currency amounts, although a separate currency denomination is not stated. M and K denote million and thousand in the displayed resource values.

| System | Total cost | Cost/solve as printed | Tokens | Tokens/solve |
|---|---:|---:|---:|---:|
| AWE | $7.73 | $0.113 | 1.12M | 20.7K |
| MAPTA | $21.38 | $0.267 | 54.87M | 685.9K |

AWE has lower values in every displayed resource column. No confidence intervals or significance information are shown. [C] AWE's printed cost per solve is inconsistent with total cost divided by its 54 successes: $7.73/54 ≈ $0.1431, not $0.113. MAPTA's $21.38/80 ≈ $0.2673 agrees with its printed value after rounding. The supplied material does not explain AWE's discrepancy, so both the source value and derived check must remain visible.

### Table III — Category-wise XBOW comparison, p. 7

[A/B] Rows are vulnerability families; Total is the number of challenges in that family, followed by each system's solved count and rounded solve percentage.

| Vulnerability | Total | MAPTA count | MAPTA % | AWE count | AWE % |
|---|---:|---:|---:|---:|---:|
| XSS | 23 | 13 | 57% | 20 | 87% |
| Blind SQLi | 3 | 1 | 33% | 2 | 67% |
| SQLi | 6 | 6 | 100% | 6 | 100% |
| XXE | 3 | 3 | 100% | 3 | 100% |
| SSRF | 3 | 3 | 100% | 3 | 100% |
| SSTI | 13 | 11 | 85% | 7 | 54% |
| Command injection | 11 | 9 | 82% | 5 | 45% |

The table shows two AWE wins, three ties, and two MAPTA wins. Perfect rates in three-case categories describe three successes rather than a broad statistical guarantee. [C] The listed totals sum to 62; their solved counts sum to 46 for MAPTA and 46 for AWE. Thus these rows cover 62/104 challenges, and AWE's gains in some listed families are offset by losses in others. The remaining 42 challenges are not broken down in this table. This derived subtotal is useful context for the prose's broad specialization claims.

## 12. Diagram / Architecture

[A/B; F1–F2, pp. 3–5] The architecture and XSS flowchart jointly explain the intended information path. The input is a target application and its reachable HTTP interfaces. Reconnaissance discovers endpoints, parameters, forms, and technologies. The orchestrator interprets that information with existing state and selects specialists whose preconditions appear satisfied. Specialists probe application behavior, update contextual knowledge, and construct or request candidate inputs. Verification provides evidence of success or failure. The system stores outcomes and either continues, changes strategy, exits early, or stops at a resource limit.

The control path is primarily orchestration and scheduling. The data path includes discovered inputs, authentication state, filters, response features, attempted payloads, and verification observations. The feedback loop is essential: a failed candidate can reveal a constraint that informs the next candidate, rather than merely ending the test.

[A] Short-term and long-term memory serve different intended purposes. Short-term state avoids duplicate work during a scan. Long-term state is intended to transfer domain-level experience to future targets. However, evaluation resets memory between challenges, so the XBOW results do not establish the value of accumulated cross-target learning. The initial contents of any separate long-term store are not fully specified.

[D] Global state and useful local iteration do not imply a general planner capable of arbitrary attack chains. The authors explicitly acknowledge largely independent specialist pipelines and limited multi-stage coordination. This reconciles some of the architecture's statefulness with its poor performance on long-horizon exploitation, although broad early wording about multi-step exploitation remains stronger than the demonstrated planning capability.

## 13. Equations and mathematical concepts

No numbered equations, optimization objectives, losses, theorems, lemmas, or proofs appear in the supplied paper. There is no mathematical training contribution to reconstruct. The necessary mathematics consists of rates, totals, averages, ratios, and resource normalization.

[C] The calculation identities used in this report are analyst explanations: solve rate = solved challenges / evaluated challenges × 100%; percentage-point gap = one success percentage minus another; relative improvement = (new−baseline)/baseline × 100%; time ratio = baseline time / AWE time; and cost per solve = total cost / solved challenges. These are not equations printed by the authors.

For example, 20/23 and 13/23 are XSS rates with the same category denominator, whereas 54/104 and 80/104 are overall benchmark rates. Mixing these denominators would misrepresent performance. Similarly, 190.8/53.1 uses average times, while 156.2/35.7 uses medians. Both ratios are meaningful descriptions of reported summaries, but they are not interchangeable.

The paper reports no standard deviations, standard errors, confidence intervals, p-values, significance thresholds, or probability model for solve outcomes. Therefore, observed differences should be described as benchmark results rather than statistically established population effects.

## 14. Interpretation and Discussion

[A; VII, p. 8] The authors interpret AWE as evidence that domain structure can compensate for less capable underlying models in precise exploitation tasks. They attribute XSS and blind SQL injection performance to explicit context modeling, filtering abstractions, SQL boundaries, and constrained generation. They also acknowledge that MAPTA's sandbox flexibility and broad reasoning are beneficial for authentication workflows, privilege escalation, and business logic. Their proposed synthesis is a hybrid architecture.

[D] This interpretation is plausible within the observed system comparison, but architecture is not experimentally separated from model choice, implementation, execution affordances, or historical baseline conditions. There is no component ablation showing the isolated effect of memory, browser verification, specialist procedures, or orchestration. The results support a system-level trade-off more directly than a quantified causal decomposition.

The source contains several unresolved points:

1. **Trial counts versus percentages:** V.A states n=10 independent trials per vulnerability type. VI.A reports 67% and 55%, which cannot be simple binary success fractions of ten trials. Additional difficulty aggregation or another denominator might explain them, but is not specified. This report does not choose an explanation.
2. **Stored-XSS wording:** VI.A says Claude outperformed both alternatives on complex categories, then reports Claude and GPT-4o tied at 67% for stored XSS. The specific tie qualifies the broader wording.
3. **Cost normalization:** Table II prints $0.113 per AWE solve, but $7.73/54 ≈ $0.1431. The denominator or accounting needed to reconcile them is absent.
4. **Figure 4 alignment:** Its caption discusses models, while its panels show difficulty/task conditions without model-separated distributions.
5. **Timing headline:** The 4.4-times figure agrees with median times; average times imply approximately 3.59 times. These summaries must remain distinct.
6. **Category generalization:** The claim that AWE dominates its injection classes is qualified by clear SSTI and command-injection losses and equal summed solves across the seven listed rows.
7. **Baseline conditions:** The paper says identical hardware, but also says MAPTA comparisons use publicly reported per-challenge results. The supplied account does not establish how hardware identity or cost accounting was verified across those sources.
8. **Determinism and false positives:** The abstract and design use strong language about deterministic results and eliminating false positives. No dedicated repeated-run variance or false-positive-rate experiment is reported.

These issues do not erase the reported counts. They constrain how confidently one can generalize the explanation or reproduce every headline.

## 15. Contributions and novelty

**System contribution [A]:** AWE integrates global orchestration, eight named vulnerability specialists, memory, reconnaissance, and browser-backed verification in one autonomous testing architecture.

**Methodological contribution [A]:** Structured, vulnerability-specific pipelines turn observed context and filtering behavior into constrained payload generation and iterative validation. The most fully explained example is XSS.

**Conceptual contribution [A]:** The paper argues for specialization, state, and verification as architectural principles for efficient LLM-assisted security testing. It treats the model as one component of a larger procedure.

**Empirical contribution [A]:** The paper reports a DVWA model comparison, a 104-challenge XBOW comparison, category results, failure summaries, and resource measurements. The substantive contribution includes documenting complementary strengths rather than claiming overall benchmark superiority.

**Implementation contribution [A]:** A source repository is advertised on page 1. Its availability is an author statement; its contents, completeness, and reproducibility were not checked.

No new dataset, benchmark, formal theorem, model-training method, or standalone-LLM vulnerability comparison is presented. [D] Novelty relative to the entire literature cannot be independently established in closed-document mode; the report represents the authors' positioning rather than a verified priority claim.

## 16. Limitations

### Authors' stated limitations

[A; VIII, p. 8] Four explicit limitations are identified. First, scope is injection-centric and excludes reasoning-heavy business logic, complex authentication workflows, and protocol issues such as request smuggling or desynchronization. Second, specialists are largely independent and do not coordinate arbitrary multi-stage chains; the paper's example is default credentials followed by unauthorized object access and privilege escalation. Third, context and filtering heuristics assume patterns that unusual frameworks or obfuscated sinks can invalidate. Fourth, model-dependent reasoning and changing model behavior or prices threaten stability.

[A; VI.D, p. 7] Failure analysis additionally identifies resistant filtering, authentication irregularities, and narrow exploit windows such as race conditions. Approximately one-third of failures are assigned to out-of-scope classes and another quarter to unsupported multi-step chains. Exact counts for those approximate groups are not given.

### Additional evidence-based analyst observations

[D] Published baseline results and different models limit causal attribution. Small category samples limit generalization, especially the three-case blind SQL injection result. Missing uncertainty estimates prevent assessing statistical precision. No explicit architectural ablations establish which components are necessary. A memory-reset evaluation does not demonstrate cumulative cross-target learning. Flag retrieval is a clear benchmark outcome but does not cover all practical dimensions of vulnerability assessment. Incomplete configuration details constrain reproduction. Numerical and caption inconsistencies require caution when reusing headline figures.

[D] For the user's research question, the most important limitation is a mismatch of dependent variable: the paper measures successful exploitation of web applications by agents, not successful compromise of agents by adversaries. It should not be cited as direct evidence that web AI agents are more vulnerable than standalone LLMs.

## 17. Threats to validity

The following validity labels are analyst organization, not a claim that the authors used this framework.

**Internal validity [D]:** AWE and MAPTA differ in underlying models, execution environments, search flexibility, and architectural procedures. Their outcomes cannot isolate specialization alone. Historical baseline measurements add uncertainty about otherwise matched conditions.

**Construct validity [D]:** Verified flag retrieval is a strong measure of benchmark exploit completion. It is narrower than vulnerability discovery quality, defensive utility, safe deployment, or agent compromise resistance. The DVWA chart calls its measure success rate while the prose sometimes calls it accuracy; a formal confusion-matrix definition is not given.

**Statistical conclusion validity [D]:** No inferential tests or intervals are reported. Several category denominators are very small. The unexplained relationship between n=10 and some percentages reduces confidence in reconstructing the DVWA experiment precisely. Histograms do not provide enough sample accounting for independent statistical analysis.

**External and ecological validity [D]:** Containerized benchmark applications and deliberately vulnerable DVWA settings provide controlled targets. The supplied work does not show production-scale deployment, live-service impact, broad environmental diversity, or performance against continually changing real applications. The authors' proposed continuous-testing use is an implication rather than a demonstrated deployment result.

**Reproducibility [D]:** A repository link helps identify an implementation artifact, but no repository was reviewed here. Missing model parameters, exact software/hardware versions, pricing details, and trial accounting make the supplied paper insufficient as a complete reproduction specification. Model and price changes are also explicitly acknowledged by the authors.

## 18. Future work and open questions

### A. Explicit author directions

[A; VII and IX, p. 8] The principal future direction is a hybrid system combining specialized injection semantics with higher-level agents that plan multi-step attacks. The discussion also suggests adaptive long-term learning through stored filter signatures, successful bypasses, and effective payload patterns. Continuous or high-frequency assessment is proposed as a useful application because of resource efficiency.

### B. Additional analyst open questions

[D] How much benefit comes separately from specialization, memory, constrained generation, and browser verification? Would the trade-off persist with the same underlying model in both architectures? What happens on a matched subset solved by both systems? How do failed challenges affect average time and cost? Do the results remain stable across repeated runs and model updates? Does long-term memory improve new-target performance without contaminating evaluation? How should broader planning be added while retaining low resource use?

[D] For the user's security question, a new study would need to measure attacks against the AI systems themselves and include a meaningful standalone-model comparison. Relevant unanswered issues include how web observations enter decision-making, how tool permissions are bounded, and how stored state affects attack persistence. These are logically relevant questions suggested by the described capabilities, not attack findings reported by AWE.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning and source boundary |
|---|---|
| AWE | Adaptive Web Exploitation Framework, the system introduced here |
| LLM | Large language model used for orchestration and constrained candidate generation |
| Agent | A component that selects or performs a task using procedures and possibly an LLM |
| HTTP | Hypertext Transfer Protocol, the request/response interface used against targets |
| GET / POST | Named HTTP request methods used in the threat model |
| API | Application programming interface; commercial model APIs incur reported costs |
| Black-box | Testing without privileged access to target source code or internals |
| Reconnaissance | Discovering reachable endpoints, parameters, and technologies |
| Payload | An input designed to test or exploit a suspected weakness |
| Canary | A recognizable probe used here to locate input reflection |
| Sanitization | Input transformations or filtering that affect potential attack behavior |
| Output encoding | Transforming output representations; listed as a target defense |
| WAF | Web application firewall; the paper discusses filtering and bypasses |
| XSS | Cross-site scripting; exploitation involving executable browser-side content |
| DOM | Document Object Model; the browser document structure referenced in context analysis |
| CSP | Content Security Policy; enforcement is a condition of the stored-XSS comparison, but its rules are not specified |
| SQLi | SQL injection; malicious input affecting database-query behavior |
| Blind SQLi | SQL injection inferred indirectly; the paper emphasizes timing-based probes |
| SSTI | Server-side template injection; input interacting with template-engine semantics |
| XXE | XML external entity expansion, the paper's wording for the named vulnerability family |
| SSRF | Server-side request forgery, a tested category |
| IDOR | Insecure direct object reference; authenticated access comparisons across resource identifiers |
| LFI | Local file inclusion; the abbreviation appears in the architecture alongside file-inclusion scope |
| CmdInj | Command injection, abbreviated in Figure 1 |
| DAST | Dynamic Application Security Testing, the prior-tool category discussed by the authors |
| PoC | Proof of concept: a concrete exploit demonstration |
| DVWA | Damn Vulnerable Web Application, the controlled model-comparison target |
| XBOW | The named 104-challenge benchmark; no expansion is provided |
| MAPTA | The named comparison system; its expansion is not supplied in the main description |
| Flag | Hidden benchmark artifact required for a counted XBOW solve |
| Token | Model-processing unit used for resource accounting; precise billing rules are not supplied |
| Headless Chromium | The consistent browser execution configuration used for verification |
| SQLite | Persistence technology labeled in Figure 1; detailed schema is not supplied |
| XSSy | A Figure 4 panel label whose meaning is not defined in the supplied material |
| n | Trial count; V.A states n=10 per vulnerability type for each model |
| M / K | Million / thousand in Table II resource values |

These are operational explanations grounded in the paper's usage, not additional externally sourced technical background.

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| XBOW size | 104 | challenges | Full benchmark | Author-reported | p. 5, V.A |
| XBOW diversity | 26 | categories | Full benchmark | Author-reported | p. 5, V.A |
| DVWA repetitions | 10 | trials per type/model | Stated independent trials | Author-reported | p. 5, V.A |
| Challenge budget | 10 | minutes | AWE aggressive configuration | Author-reported | p. 6, V.D |
| AWE overall success | 54/104; 51.9% | solves; percent | Claude Sonnet 4 | Author-reported | p. 6, T1 |
| MAPTA overall success | 80/104; 76.9% | solves; percent | GPT-5 | Author-reported | p. 6, T1 |
| AWE/MAPTA average time | 53.1 / 190.8 | seconds | Reported solve-time averages | Author-reported | p. 6, T1 |
| AWE/MAPTA median time | 35.7 / 156.2 | seconds | Time-to-solve | Author-reported | p. 7, VI.E |
| AWE/MAPTA total cost | $7.73 / $21.38 | currency amounts | Full benchmark accounting | Visually readable | p. 7, T2 |
| AWE/MAPTA printed cost per solve | $0.113 / $0.267 | currency per solve | AWE entry conflicts with total/54 | Visually readable | p. 7, T2 |
| AWE/MAPTA total tokens | 1.12M / 54.87M | tokens | Prose rounds latter to 54.9M | Visually readable | p. 7, T2 |
| AWE/MAPTA tokens per solve | 20.7K / 685.9K | tokens per solve | Reported normalized values | Visually readable | p. 7, T2 |
| AWE/MAPTA XSS success | 20/23 / 13/23 | solves | Printed 87% / 57% | Visually readable | p. 7, T3 |
| AWE/MAPTA blind SQLi | 2/3 / 1/3 | solves | Printed 67% / 33% | Visually readable | p. 7, T3 |
| AWE/MAPTA SQLi | 6/6 / 6/6 | solves | Both 100% | Visually readable | p. 7, T3 |
| AWE/MAPTA XXE | 3/3 / 3/3 | solves | Both 100% | Visually readable | p. 7, T3 |
| AWE/MAPTA SSRF | 3/3 / 3/3 | solves | Both 100% | Visually readable | p. 7, T3 |
| AWE/MAPTA SSTI | 7/13 / 11/13 | solves | Printed 54% / 85% | Visually readable | p. 7, T3 |
| AWE/MAPTA command injection | 5/11 / 9/11 | solves | Printed 45% / 82% | Visually readable | p. 7, T3 |
| Reflected-XSS model success | 100 / 100 / 100 | percent | Claude / GPT-4o / Gemini within AWE | Author-reported | p. 6, VI.A |
| CSP stored-XSS success | 67 / 67 / 50 | percent | Same model order | Author-reported | p. 6, VI.A |
| Blind-SQLi model success | 70 / 60 / 55 | percent | Same model order | Author-reported | p. 6, VI.A |
| Claude's five F3 labels | 100 / 67 / 80 / 80 / 70 | percent | Five plotted vulnerability types | Visually readable | p. 5, F3 |
| Claude convergence | 10–40 | payload attempts | Text/caption summary | Author-reported | pp. 6–7, VI.A/F4 |
| GPT-4o / Gemini extra attempts | about 20 / about 40 | percent more | Relative to Claude, author summary | Author-reported | pp. 6–7 |
| F4 average annotations | 10 / 20 / 40 / 12 | attempts | Low / Medium / Hard / XSSy | Visually readable | p. 7, F4 |
| AWE/MAPTA/both failures | 50 / 24 / 15 | challenges | Aggregate failures | Author-reported | p. 7, VI.D |
| Overall coverage gap | 25 | percentage points | (80−54)/104 × 100 | Analyst-derived | p. 6, T1 |
| Median speed ratio | approximately 4.38 | ratio | 156.2/35.7 | Analyst-derived | p. 7, VI.E |
| Mean speed ratio | approximately 3.59 | ratio | 190.8/53.1 | Analyst-derived | p. 6, T1 |
| Token reduction | approximately 97.96 | percent | (54.87−1.12)/54.87 × 100 | Analyst-derived | p. 7, T2 |
| Total-cost reduction | approximately 63.84 | percent | (21.38−7.73)/21.38 × 100 | Analyst-derived | p. 7, T2 |
| Checked AWE cost per solve | approximately $0.1431 | currency per solve | $7.73/54; conflicts with printed $0.113 | Analyst-derived | pp. 6–7, T1/T2 |
| Both/AWE-only/MAPTA-only solves | 45 / 9 / 35 | challenges | Inclusion–exclusion from aggregate counts | Analyst-derived | pp. 6–7 |
| Listed-category subtotal | 62 challenges; 46 solves each | counts | Sum of seven T3 rows | Analyst-derived | p. 7, T3 |

No approximate bar-height estimates are used as exact key results. This preserves the distinction between readable labels, prose reports, and calculations.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| AWE combines specialization, orchestration, and shared infrastructure | Three layers and eight specialist boxes | F1; system design | pp. 3–5 | HIGH for documented design; implementation not inspected |
| XSS testing is context-sensitive and iterative | Canary, context, filter, mutation, verification stages | F2; XSS procedure | p. 4 | HIGH for described method; no component ablation |
| Counted XBOW solves require exploit completion | Correct flag required; partial progress excluded | Success criteria | p. 6 | HIGH for stated evaluation rule |
| MAPTA achieves broader overall coverage | 80/104 versus 54/104 | T1; X3 | p. 6 | HIGH for reported counts; baseline historical |
| AWE is stronger on XSS in this benchmark | 20/23 versus 13/23 | T3; X4 | p. 7 | HIGH for table; limited to these challenges |
| Blind-SQLi advantage is small in absolute sample size | Two solves versus one of three | T3; X4 | p. 7 | HIGH for counts; weak basis for broad generalization |
| Specialization has category-specific weaknesses | SSTI 7 versus 11; command injection 5 versus 9 | T3; X4 | p. 7 | HIGH; qualifies broad injection-dominance language |
| AWE has lower reported resource use | Cost, tokens, mean and median times | T1/T2; X6 | pp. 6–8 | HIGH for reported totals; cost/solve discrepancy remains |
| Claude is selected based on within-AWE trials | Success summaries and iteration claims | F3/F4; X1/X2 | pp. 5–7 | MEDIUM for precise reconstruction because denominators and F4 alignment are unclear |
| Multi-stage planning remains limited | Explicit limitations and failure categories | X5; VIII | pp. 7–8 | HIGH for author acknowledgment |
| Long-term learning is an architectural proposal, not established benchmark gain | Long-term store described; memory reset stated | IV.C; V.D | pp. 4–6 | MEDIUM; initial memory contents not fully specified |
| The paper does not answer whether web agents are more vulnerable than standalone models | Evaluated outcomes concern web-target flags and resources | Entire evaluation | pp. 5–8 | HIGH for study-scope distinction; relevance is analyst interpretation |

Evidence strength here concerns what the supplied paper supports. It does not imply independent replication or verification of the reported measurements.

## 22. Very Simple Explanation

Imagine two automated security testers. One has carefully designed routines for particular kinds of web bugs. The other is a more flexible explorer that can try a wider range of actions. AWE is closer to the first approach, and MAPTA is closer to the second. AWE checks where an input appears, learns what the application blocks, creates a better candidate, and tests whether it really works.

On the supplied benchmark, the flexible explorer solves more challenges overall: 80 instead of 54. But AWE does better at some specific jobs, especially cross-site scripting, where it solves 20 challenges instead of 13. It also spends fewer model tokens and has lower reported total cost and shorter solve times. Being specialized helps some tasks and limits others.

The important caution is that these AI systems are attacking deliberately vulnerable web applications for testing. The paper is not testing whether someone can trick or compromise the AI agents themselves. It therefore helps explain how an agent's tools and workflow affect its capabilities, but it does not show that web AI agents are more vulnerable than standalone language models.

## Completeness Audit

Coverage is assessed against the supplied nine-page inventory, not against inaccessible repositories or hypothetical supplements. Full representation means the substantive content is explained at the appropriate level; it does not mean every sentence is reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, equal-contribution footnote | Yes, text and p. 1 image | Yes | Fully represented | Publication identifiers included; emails omitted as non-substantive |
| Abstract and index terms | Yes | Yes | Represented in compressed form | Main claims preserved and qualified |
| I. Introduction | Yes | Yes | Represented in compressed form | Motivation and claimed gap covered |
| II.A System Model | Yes | Yes | Fully represented | HTTP, target assumptions, observations |
| II.B Capabilities and Goals | Yes | Yes | Fully represented | Requests, authentication, model help, endpoint budget |
| II.C Trust Relationship | Yes | Yes | Fully represented | Infrastructure and input trust boundaries |
| II.D Scope | Yes | Yes | Fully represented | Included/excluded families |
| III.A Traditional Scanning | Yes | Yes | Represented in compressed form | Tool names and attributed limitations |
| III.B LLM Testing Systems | Yes | Yes | Represented in compressed form | Prior-system positioning and MAPTA roles |
| III.C Architectural Gaps | Yes | Yes | Fully represented | Context, state, iteration, specialized probes |
| IV.A Orchestration | Yes | Yes | Fully represented | State, selection, resource governance |
| IV.B Specialist Agents | Yes | Yes | Fully represented | XSS detail and other described procedures |
| IV.C Foundation | Yes | Yes | Fully represented | Memory, reconnaissance, browser evidence |
| Design Rationale | Yes | Yes | Fully represented | Three principles explained |
| V.A Benchmarks | Yes | Yes | Fully represented | Sizes, categories, n=10, target conditions |
| V.B Baseline | Yes | Yes | Fully represented | Historical MAPTA results and capabilities |
| V.C Model Selection | Yes, extracted p. 6 text | Yes | Fully represented | Selection rationale and caveats |
| V.D Configuration | Yes, extracted p. 6 text | Yes | Fully represented | Aggressive mode, resets, isolation, Chromium |
| V.E Metrics | Yes, extracted p. 6 text | Yes | Fully represented | Effectiveness, efficiency, cost |
| V.F Success Criteria | Yes, extracted p. 6 text | Yes | Fully represented | Flag retrieval required |
| VI.A DVWA / X1 | Yes, extracted text plus F3 image | Yes | Fully represented | Exact readable results; denominator uncertainty |
| Payload efficiency / X2 | Yes | Yes | Fully represented | Caption–panel mismatch disclosed |
| VI.B XBOW / X3 | Yes, extracted p. 6 text | Yes | Fully represented | Overall coverage and timing |
| VI.C Categories / X4 | Yes | Yes | Fully represented | Every T3 row preserved |
| VI.D Failures / X5 | Yes | Yes | Fully represented | Approximate taxonomy and derived overlaps |
| VI.E Efficiency / X6 | Yes | Yes | Fully represented | Totals, ratios, inconsistency |
| VI.F Evaluation Summary | Yes, pp. 7–8 text | Yes | Represented in compressed form | Repeated headline claims consolidated |
| VII. Discussion | Yes, extracted p. 8 text | Yes | Represented in compressed form | Architectural interpretation and applicability |
| VIII. Four author limitations | Yes, extracted p. 8 text | Yes | Fully represented | Kept distinct from analyst observations |
| IX. Conclusion | Yes, extracted p. 8 text | Yes | Represented in compressed form | Hybrid direction preserved |
| Formal research questions | Checked supplied text | Yes | Fully represented | None explicitly formulated |
| Formal hypotheses | Checked supplied text | Yes | Fully represented | None explicitly formulated |
| F1 architecture | Yes, visual and text | Yes | Fully represented | Small-label/interface limits disclosed |
| F2 five-phase pipeline | Yes, visual and text | Yes | Fully represented | Branches, feedback, outcomes explained |
| F3 model chart | Yes, visual and text | Yes | Fully represented | Exact readable labels; no guessed unlabeled values |
| F4 four panels | Yes, visual and text | Yes | Fully represented | All panels and average annotations included |
| T1 overall performance | Text only | Yes | Fully represented | No claim of visual inspection |
| T2 efficiency | Yes, visual and text | Yes | Fully represented | Every value and cost discrepancy included |
| T3 category results | Yes, visual and text | Yes | Fully represented | Seven rows, ties, losses, subtotal |
| Major equations/theorems | Checked supplied material | Yes | Fully represented | None present; analyst arithmetic labeled |
| Numbered algorithms/pseudocode | Checked supplied material | Yes | Fully represented | None present; F2 procedural flow covered |
| Contributions | Yes | Yes | Fully represented | System, method, empirical, implementation |
| References [1]–[14] | Yes, extracted pp. 8–9 text | Yes | Represented in compressed form | Categories and key artifacts identified; no external validation |
| Appendices | Not supplied/present | Accounted for | Missing from supplied material | No appendix detected; existence elsewhere unknown |
| Supplementary material | Not supplied | Accounted for | Missing from supplied material | No referenced supplement detected |
| Advertised source repository | Link mentioned only | Accounted for | Inaccessible under task boundary | No repository inspection permitted or performed |
| Unlabeled exact plot values and histogram samples | Partial visual evidence | Accounted for | Uncertain | Not converted into exact numerical claims |

### Missing or inaccessible material

No main-text page is apparently missing from the supplied 1–9 sequence. Visual renderings of pages 6, 8, and 9 were not supplied; these pages were reviewed as extracted text. No appendix, supplement, implementation files, raw trial logs, per-challenge result list, or executable configuration was available for inspection. The absence of those artifacts from this input does not establish that they do not exist elsewhere.

### Uncertain interpretations

Unresolved issues are the DVWA percentage denominators; the Figure 4 model-versus-difficulty mismatch; the meaning of XSSy; exact unlabeled bar values and histogram counts; AWE's printed cost per solve; timing treatment of failed or differently solved cases; baseline hardware comparability; initial long-term-memory contents; and the relationship between endpoint-level and challenge-level budgets. The abstract's improvement notation is ambiguous between percent and percentage points. None is silently repaired.

### Deliberately compressed material

Repeated claims about specialization, efficiency, and complementary architectures are consolidated. Related-work descriptions are summarized as author positioning rather than reproduced paper by paper at full length. Reference metadata, author email addresses, decorative formatting, and repeated captions are compressed or omitted as non-substantive to the scientific explanation. Unlabeled visual quantities are discussed qualitatively rather than guessed.

### Potential omissions

No known substantive component in the supplied inventory is left unrepresented. Representation remains limited to the provided evidence: it does not include source-code behavior, raw experimental records, unprovided supplements, external citation validation, or a direct experiment on the user's web-agent-versus-standalone-LLM vulnerability question. Confidence is HIGH for readable counts and stated design boundaries, MEDIUM for reconstructing the DVWA and timing procedures, and UNKNOWN for unreported implementation and experimental details.
