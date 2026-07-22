# AWE: Adaptive Agents for Dynamic Web Penetration Testing

**Authors:** Akshat Singh Jaswal and Ashish Baghel, Stux Labs  
**Venue:** Workshop on LLM Assisted Security and Trust Exploration (LAST-X), February 27, 2026

## 1. Background and Context

Modern web applications are increasingly built with AI-assisted programming tools, no-code platforms, automated code generation, and rapid deployment pipelines. These tools accelerate development and allow people with limited security expertise to create applications, but they also broaden the attack surface. Security assessment tools have not adapted at the same pace.

The paper identifies weaknesses in two existing approaches:

- **Traditional Dynamic Application Security Testing scanners**, including Burp Suite, OWASP ZAP, Nuclei, and sqlmap, generally replay known payloads and match responses against signatures or heuristics. They work well for familiar injection patterns but cannot reliably create new payloads or adjust their strategies when they encounter unusual sanitization, application-specific input processing, or adaptive web application firewalls. Their rigidity can produce false positives when benign behavior resembles a vulnerability and false negatives when exploitation requires contextual or multi-step reasoning.
- **LLM-based penetration-testing systems** can reason more flexibly, but many use general-purpose agents that explore with few constraints. This can cause high token and monetary costs, unstable behavior, poor reproducibility, generic payload generation, and premature abandonment when the first payloads fail.

PentestGPT showed that LLMs can help human testers organize workflows, recommend reconnaissance, and formulate exploit logic, but humans still maintain state, execute tools, and validate findings. More autonomous systems—including AutoPT, AutoAttacker, CAI, and MAPTA—combine LLM controllers with reconnaissance and command-execution tools. However, the paper argues that they generally lack persistent, vulnerability-specific state for tracking authentication, filters, response changes, and attempted payloads.

MAPTA is the paper’s principal baseline. It uses three roles:

- A coordinator for high-level planning.
- Sandbox agents that execute commands and scripts in isolated Docker environments.
- A validation agent that turns candidate exploits into execution-backed proofs of concept.

MAPTA demonstrates broad, autonomous end-to-end exploitation, but it follows a general-purpose, reasoning-centric design.

The authors identify three broader architectural gaps:

1. General agents do not reliably interpret subtle exploitation details such as filter order, encoding quirks, type coercion, template-engine semantics, or multi-parameter interactions.
2. They often lack persistent structured memory of attempted payloads, changing filters, and evidence of partial progress.
3. They lack specialized procedures such as type-confusion probes, template-context shifts, timing inference, and controlled syntax fragmentation.

The resulting problem is not merely generating attack strings. An autonomous tester must turn a sequence of noisy HTTP responses into precise hypotheses, adapt payloads to the discovered context, and prove that an apparent weakness is actually exploitable.

### Threat and system model

The study considers a black-box automated adversary interacting with web applications through ordinary HTTP interfaces:

- It sends arbitrary GET and POST requests and places inputs in parameters, headers, cookies, and request bodies.
- It has no access to source code, server configuration, runtime logs, or internal state.
- Observations are limited to HTTP responses, response differences, errors, and timing.
- Targets may use PHP, Python, Node.js, Java, input validation, output encoding, and application-layer firewalls.
- The application stack, hosting infrastructure, and network are assumed not to be compromised.
- When benign registration or low-privilege accounts are available, the tester may conduct authenticated probing.
- Commercial LLM APIs may generate context-aware payloads, subject to cost limits.
- Each target endpoint receives no more than ten minutes of testing.

The attacker’s goal is to find injection-related weaknesses through controlled changes to application inputs and then exploit observable abnormalities such as timing differences, error structures, or output changes.

### Scope

The intended scope includes vulnerabilities observable through black-box input manipulation:

- Cross-site scripting (XSS).
- SQL injection, including blind SQL injection.
- Server-side template injection (SSTI).
- Command injection.
- Local file inclusion and path traversal.
- XML external entity expansion (XXE).
- Server-side request forgery (SSRF).
- Insecure direct object references (IDOR), when valid credentials are available.

The system intentionally does not target network- or protocol-level attacks, cryptographic weaknesses, or business-logic flaws requiring substantial semantic knowledge or reasoning beyond observable request–response behavior.

---

## 2. Research Goal and Objectives

The paper introduces **AWE, the Adaptive Web Exploitation Framework**, a memory-augmented, multi-agent system for autonomous web penetration testing.

Its central objective is to bridge the gap between static scanners and unconstrained general-purpose LLM agents by combining:

- Explicit, vulnerability-specific exploitation procedures.
- LLM-guided, context-aware payload generation and mutation.
- Persistent memory across probes.
- Global resource-aware orchestration.
- Browser-backed exploit verification.

The evaluation asks whether this specialization-oriented architecture can:

1. Reliably exploit targeted injection vulnerabilities.
2. Outperform a stronger general-purpose system on the categories for which it is specialized.
3. Reduce solve time, token consumption, and API cost.
4. Produce deterministic, reproducible, execution-backed findings rather than speculative vulnerability reports.
5. Reveal the trade-off between narrow specialization and broad exploratory capability.

The paper’s main thesis is that architecture and domain-specific structure matter at least as much as the raw reasoning ability of the underlying LLM.

---

## 3. Methods (Approach/Design)

### Overall system architecture

AWE is an autonomous black-box penetration-testing system consisting of three layers.

#### Figure 1: AWE system architecture

Figure 1 depicts the layers and their relationships:

1. **Orchestration Layer**

   - A conversational agent handles memory, input context, and tool chaining.
   - An intelligent orchestrator performs LLM-based agent selection, prioritization, and early-exit decisions.
   - A token tracker monitors cost, execution mechanisms, and budget limits.

2. **Specialized Agents Layer**

   The diagram shows dedicated agents for:

   - XSS.
   - SQL injection.
   - Server-side template injection.
   - IDOR.
   - Local file inclusion.
   - XXE.
   - SSRF.
   - Command injection.

3. **Foundational Layer**

   - A reconnaissance tool performs endpoint discovery, form parsing, and parameter extraction.
   - A memory manager stores SQLite-backed persistence, session and long-term state, and filter tracking.
   - A verifier provides browser verification, console-log observation, and screenshots.

The orchestration layer invokes relevant specialized agents, while the foundational services support all agents.

### Orchestration layer

The orchestration layer manages a scan from reconnaissance through multi-step exploitation. It maintains a global state containing:

- Discovered inputs.
- Observed server-side transformations.
- Authentication status.
- Previously attempted payloads.
- Successful exploit steps.

This state lets the system change strategy—for example, moving to authenticated testing when credentials are acquired or suppressing payloads that have already failed.

The **Intelligent Orchestrator**:

1. Receives reconnaissance results.
2. Evaluates which vulnerability classes appear plausible.
3. Uses an LLM to translate contextual evidence into a prioritized execution plan.
4. Invokes only the agents whose prerequisites are satisfied.

The LLM serves primarily as an advisory and interpretive component rather than directly controlling unrestricted exploration. It examines cues such as reflected parameters, sanitization behavior, and language-specific template constructs.

The orchestration layer also monitors runtime, token use, and tool costs. It can stop early after a high-impact result or reduce resources allocated to low-yield agents.

### Specialized-agent layer

Each vulnerability agent is a self-contained module that converts application behavior into class-specific hypotheses and tests them through a structured procedure. Expert methods are encoded in the pipeline, limiting dependence on free-form LLM reasoning.

#### XSS agent

The XSS agent illustrates the approach:

1. It sends parallel canary inputs to discover whether and where user input is reflected.
2. It identifies the precise output context, such as:

   - Quoted attributes.
   - Unquoted attributes.
   - JavaScript string literals.
   - Raw HTML.

3. It probes server-side filters to identify:

   - Character transformations.
   - Blocked tag families.
   - Event-handler restrictions.

4. It packages the discovered context and constraints into a structured description.
5. The LLM generates payload candidates tailored to those constraints.
6. A real browser must provide definitive evidence of JavaScript execution.

This grounding is intended to prevent an LLM from declaring speculative or hallucinated XSS vulnerabilities.

#### Figure 2: Five-phase XSS pipeline

Figure 2 expands the workflow:

- A target URL enters reconnaissance, including endpoint discovery, parameter extraction, and technology detection.
- Discovered parameters enter a parameter queue.
- **Phase 1: Multi-canary injection** checks several XSS possibilities in parallel, including reflection behavior, stored behavior, and DOM-related signals.
- **Phase 2: Context analysis** determines the reflection context, such as attribute, tag, script, quote, and encoding conditions.
- **Phase 3: Filter and security detection** probes for defenses and identifies allowed tags, events, and encoding bypass opportunities.
- **Phase 4: Payload mutation** sends the inferred context and blocked patterns to an LLM, which produces mutated payloads. Failed verification can loop back to this phase for another mutation.
- **Phase 5: Browser verification with Playwright** tests the payload in a controlled browser, observes execution signals such as alerts or DOM changes, and produces either an XSS-found or XSS-failed outcome.

The diagram therefore shows an iterative feedback loop: browser failure does not immediately end testing but can trigger another context-informed payload mutation.

#### Other specialized agents

- **SQL injection:** Combines deterministic payload sets with database-error analysis, backend fingerprinting, and inferred query structure. It uses controlled mutations to explore alternate execution paths and firewall bypasses.
- **SSTI:** Sends engine-specific probes, identifies the likely template framework, and generates exploit strings consistent with that engine’s internal semantics.
- **IDOR:** Uses authenticated differential testing, comparing access to different resource identifiers to detect authorization inconsistencies.
- **Command injection, XXE, SSRF, and LFI:** Follow the same general philosophy of structured domain knowledge, controlled probing, constrained LLM assistance, and behavioral validation.

### Foundation layer

#### Persistent memory

AWE combines short- and long-term memory:

- **Short-term memory** records attempted payloads and outcomes, inferred filters, and each agent’s progress during an engagement. This prevents redundant work.
- **Long-term memory** stores domain-level characteristics such as sanitization signatures, effective bypasses, and historical payload success rates.

The design is intended to let the system reuse experience across similar applications. However, in the reported XBOW evaluation, memory was reset between challenges, so the experiment measured single-engagement performance rather than cross-target learning.

#### Browser verification

A controlled browser verifies vulnerabilities that cannot be proven from raw HTTP responses. It can observe:

- Script execution.
- DOM changes.
- Dialog or alert triggers.
- Console-related signals and screenshots shown in the architecture diagram.

This separates merely theoretical payloads from vulnerabilities that can be exploited in practice and reduces false positives.

#### Reconnaissance

Endpoint discovery, form parsing, parameter extraction, and technology fingerprinting map the initial attack surface. These signals also allow the orchestrator to avoid invoking agents that are unlikely to be relevant.

### Design principles

AWE follows three principles:

1. **Specialization over general-purpose reasoning:** Detailed exploitation is encoded as dedicated state machines and inference pipelines.
2. **Stateful, memory-driven operation:** Multi-request context is retained rather than reconstructed by an unconstrained agent.
3. **Verification rather than speculation:** Every finding requires evidence such as execution, differential behavior, or extracted data.

### Evaluation design

The study uses two benchmarks.

#### XBOW

XBOW contains **104 vulnerable containerized web applications across 26 vulnerability categories**. Every challenge contains a hidden flag retrievable only by completing an end-to-end exploit.

The benchmark includes:

- Straightforward reflected XSS.
- Context-specific sanitization bypasses.
- Authentication and authorization chains.
- Single-step injections.
- Multi-stage exploitation requiring several findings or authenticated request sequences.

Injection-related vulnerabilities constitute most of the benchmark.

AWE is compared against MAPTA using MAPTA’s published per-challenge results. MAPTA reportedly solved 76.9% of XBOW under generous compute and time budgets.

#### DVWA

DVWA provides deterministic, repeatable vulnerability configurations and adjustable difficulty. The tested categories were:

- Reflected XSS.
- Stored XSS.
- DOM-based XSS.
- Error-based SQL injection.
- Time-based blind SQL injection.

Claude Sonnet 4, GPT-4o, and Gemini 2.0 Flash were tested using identical AWE agent logic and verification procedures. Each model received **10 independent trials per vulnerability type**.

### Experimental configuration

For XBOW:

- AWE used its aggressive configuration, conducting deep reconnaissance and running every agent considered relevant.
- Every challenge had a ten-minute limit, matching MAPTA’s reported configuration.
- Experiments used identical hardware.
- Every challenge ran in isolation.
- Memory was reset between challenges.
- Verification used a consistent headless Chromium configuration.
- Claude Sonnet 4 was used for all large-scale AWE experiments.

### Metrics and success criterion

The evaluation measured:

- Overall and category-specific solve rates.
- Challenges solved uniquely by each system.
- Average and median time to solve.
- Total tokens and tokens per successful exploit.
- Total API cost and cost per solved challenge.

A challenge counted as solved only when the correct hidden flag was retrieved through a verified exploit. Detection or partial progress without flag recovery did not count.

No statistical significance tests, confidence intervals, or p-values are reported.

---

## 4. Results and Findings

### DVWA model comparison

All three models achieved **100% success on reflected XSS**, suggesting that this was the easiest baseline task.

Differences appeared on tasks requiring context-sensitive or iterative reasoning:

- **Stored XSS with content-security-policy enforcement**

  - Claude Sonnet 4: **67%**.
  - GPT-4o: **67%**.
  - Gemini 2.0 Flash: **50%**.

- **Blind SQL injection**

  - Claude Sonnet 4: **70%**.
  - GPT-4o: **60%**.
  - Gemini 2.0 Flash: **55%**.

Claude was particularly strong where the pipeline required temporal inference, semantic constraint handling, and repeated payload refinement.

#### Figure 3: Model success rates

Figure 3 is a grouped bar chart comparing Claude Sonnet 4, GPT-4o, and Gemini 2.0 Flash across reflected XSS, stored XSS, DOM XSS, basic SQL injection, and blind SQL injection. The vertical axis is success rate from 0% to 100%.

Claude’s bars indicate approximately:

- Reflected XSS: **100%**.
- Stored XSS: **67%**.
- DOM XSS: **80%**.
- Basic SQL injection: **80%**.
- Blind SQL injection: **70%**.

The chart confirms the exact text-reported values for reflected XSS, stored XSS, and blind SQL injection. GPT-4o and Gemini are similar to Claude on the simpler categories but fall behind on blind SQL injection; Gemini also falls behind on stored XSS. Some individual labels for the non-Claude bars are too small to read confidently, so exact values beyond those explicitly supplied in the text should not be inferred from the image.

### Payload-iteration efficiency

Claude Sonnet 4 generally converged within **10–40 payload attempts**. GPT-4o needed about **20% more attempts**, and Gemini about **40% more**.

#### Figure 4: Payload efficiency across difficulty levels

Figure 4 presents four histograms of the number of payload attempts required for successful exploitation:

- DVWA low difficulty: average **10 attempts**.
- DVWA medium difficulty: average **20 attempts**.
- DVWA hard difficulty: average **40 attempts**.
- A fourth XSS-related difficulty panel: average **12 attempts**.

The caption interprets these distributions as showing that Claude converges in the fewest attempts, GPT-4o uses around 20% more, and Gemini around 40% more. The distributions are concentrated around the marked average lines, with harder DVWA settings shifted toward substantially more attempts. This supports the authors’ claim that Claude offers greater iterative stability and lower operational overhead.

Based on its accuracy and convergence behavior, Claude Sonnet 4 was selected for the XBOW evaluation.

### Overall XBOW performance

#### Table I: Overall solve rate and time

| System | Solve rate | Solved challenges | Average solve time | Model |
|---|---:|---:|---:|---|
| AWE | 51.9% | 54/104 | 53.1 seconds | Claude Sonnet 4 |
| MAPTA | 76.9% | 80/104 | 190.8 seconds | GPT-5 |

MAPTA solved **26 more challenges overall**, demonstrating substantially broader coverage. AWE was nevertheless much faster on successful challenges.

The paper summarizes the timing difference as approximately a **4.4× speedup**. Across solve-time percentiles, the reported speedup is consistently about **4–5×**.

Median solve times were:

- AWE: **35.7 seconds**.
- MAPTA: **156.2 seconds**.

### Cost and token efficiency

#### Table II: Cost and token comparison

| System | Total API cost | Reported cost per solve | Total tokens | Tokens per solve |
|---|---:|---:|---:|---:|
| AWE | $7.73 | $0.113 | 1.12 million | 20.7K |
| MAPTA | $21.38 | $0.267 | 54.87 million | 685.9K |

AWE used approximately **98% fewer tokens** and incurred approximately **63% lower total API cost**.

The authors attribute this to:

- Specialized agents avoiding the enormous search spaces encountered by general-purpose reasoning agents.
- Memory-guided heuristics preventing redundant attempts.
- The orchestrator invoking only relevant agents.
- Faster convergence during iterative payload mutation.

There is a minor internal numerical issue in the presented data: Table I reports 54 AWE solves, while Table II’s stated total cost and cost per solve do not arithmetically correspond to 54 solves. The summary preserves the table’s reported values rather than attempting to correct them.

### Category-level XBOW performance

#### Table III: Injection-category results

| Vulnerability | Total challenges | MAPTA | MAPTA rate | AWE | AWE rate |
|---|---:|---:|---:|---:|---:|
| XSS | 23 | 13 | 57% | 20 | 87% |
| Blind SQL injection | 3 | 1 | 33% | 2 | 67% |
| SQL injection | 6 | 6 | 100% | 6 | 100% |
| XXE | 3 | 3 | 100% | 3 | 100% |
| SSRF | 3 | 3 | 100% | 3 | 100% |
| SSTI | 13 | 11 | 85% | 7 | 54% |
| Command injection | 11 | 9 | 82% | 5 | 45% |

#### XSS

AWE’s strongest category was XSS:

- AWE: **20/23, or 87%**.
- MAPTA: **13/23, or 57%**.
- Absolute percentage-point advantage: **30 points**.
- The abstract describes this as a **30.5% gain over MAPTA**.

AWE-only XSS successes commonly required:

- Matching payload structure to the precise reflection context.
- Distinguishing attribute and string contexts.
- Inferring filters from response changes.
- Adapting to several layers of encoding.

The paper argues that MAPTA’s general-purpose pipeline frequently failed to infer these exact contextual constraints.

#### Blind SQL injection

- AWE: **2/3, or 67%**.
- MAPTA: **1/3, or 33%**.
- The abstract reports AWE’s result as **66.7%** and a **33.3% gain** over MAPTA.

The authors attribute AWE’s advantage to structured inference and backend-specific timing probes.

#### Categories with equal performance

Both systems solved every tested challenge in:

- Ordinary SQL injection: **6/6**.
- XXE: **3/3**.
- SSRF: **3/3**.

This suggests that both could reliably handle relatively straightforward exploit patterns in these categories.

#### Categories favoring MAPTA

MAPTA performed better on:

- SSTI: **11/13 (85%)** versus AWE’s **7/13 (54%)**.
- Command injection: **9/11 (82%)** versus AWE’s **5/11 (45%)**.

It also performed better in broader categories involving:

- Privilege escalation.
- Insecure deserialization.
- Business logic.
- Long-horizon procedural reasoning.
- Authentication workflows and cross-endpoint state.
- Semantic exploration.

These categories are not all represented in Table III because the table focuses on major injection-related classes.

### Failure analysis

- AWE failed **50** of 104 challenges.
- MAPTA failed **24**.
- Both failed the same **15** challenges.

The authors divide AWE’s failures into several groups:

- About **one-third** belonged to intentionally unsupported categories, including business logic, deserialization, and cryptographic misuse.
- About **one-quarter** required multi-step reasoning and stateful exploit chains that AWE’s current agents could not represent.
- The remainder involved:

  - Authentication irregularities.
  - Heavy filtering that defeated the mutation engine.
  - Extremely narrow exploitation windows, including race conditions.

Challenges solved only by AWE were concentrated in XSS and blind SQL injection. Challenges solved only by MAPTA overwhelmingly required open-ended exploration, multi-agent state management, and semantic reasoning.

---

## 5. Analysis and Interpretation

The results support an architectural trade-off rather than showing that one system is universally superior.

MAPTA achieved higher overall coverage because it combines GPT-5 in extended-reasoning mode with unrestricted sandbox execution. This lets it explore arbitrary procedures and construct longer exploitation chains. AWE deliberately narrows the search space, uses Claude Sonnet 4, and encodes vulnerability-specific assumptions and procedures.

For XSS and blind SQL injection, AWE’s structure produced better outcomes despite the less capable underlying model. The authors attribute this to explicit modeling of:

- Reflection positions.
- Sanitization and encoding behavior.
- SQL operator boundaries.
- Backend-specific timing.
- Previously attempted payloads and observed outcomes.

These abstractions constrain payload generation to options that fit the observed application context. The LLM therefore searches a smaller and more meaningful space than a general-purpose agent.

The large efficiency gains support the same interpretation. AWE does not repeatedly rediscover the same facts or explore unrelated vulnerability classes. It uses memory and orchestration to avoid redundant requests, while browser verification prevents weak evidence from becoming a false-positive report.

However, specialization does not replace broad reasoning. AWE’s agents operate mostly as independent pipelines and cannot adequately combine discoveries across long sequences. MAPTA remains stronger when exploitation requires authentication transitions, privilege escalation, business understanding, or several coordinated endpoints.

The comparison therefore suggests that model strength alone is not a sufficient predictor of exploitation performance:

- Strong architectural priors can let a smaller model outperform a larger one within a narrow domain.
- A flexible, frontier-grade model remains advantageous for broad and semantically complex exploration.
- Specialized and general-purpose systems are complementary.

The authors see AWE’s **98% token reduction, 63% lower cost, and 4.4× faster solves** as particularly relevant to continuous or high-frequency security testing, where repeatedly running an expensive general-purpose agent may be impractical.

Persistent storage of filters, successful bypasses, and payload histories may also allow the system to adapt across changing applications. That cross-target benefit is a design goal, although it was not measured in the benchmark because memory was reset between challenges.

---

## 6. Contributions and Novelty

The paper’s main contributions are:

- **A memory-augmented multi-agent penetration-testing architecture** that combines global orchestration, vulnerability-specific agents, and shared foundational services.
- **Structured exploitation pipelines** for XSS, SQL injection, SSTI, command injection, XXE, SSRF, IDOR, and LFI.
- **Context-aware LLM use:** the model receives explicit information about reflection context, sanitization, filters, backend behavior, and earlier attempts rather than exploring freely.
- **Persistent state management** for payload outcomes, filter behavior, authentication status, and agent progress, plus a design for longer-term reuse of bypass knowledge.
- **Browser-backed verification** that requires concrete exploit evidence and helps eliminate speculative findings and false positives.
- **Resource-aware orchestration** that monitors tokens, runtime, and tool costs and invokes only relevant agents.
- **A strict end-to-end evaluation** in which only retrieval of the hidden challenge flag counts as success.
- **Evidence that specialization can outperform a stronger general-purpose system on targeted classes:** AWE substantially exceeds MAPTA on XSS and blind SQL injection despite using Claude Sonnet 4 rather than GPT-5.
- **Evidence of major operational efficiency:** AWE uses approximately 98% fewer tokens, costs 63% less in total, and solves successful challenges about 4.4 times faster.
- **An empirical account of complementary architectures:** specialization improves precision and efficiency, while general-purpose exploration improves overall coverage.

The paper reports that AWE’s source code is publicly available through the repository link supplied in the article.

---

## 7. Limitations and Caveats

### Explicit limitations

- **Restricted vulnerability scope:** AWE primarily targets injection-centric weaknesses. It does not address business-logic flaws, complex authentication workflows, cryptographic weaknesses, or protocol-level problems such as request smuggling and desynchronization.
- **Weak multi-step planning:** Agents work mainly in independent pipelines and do not coordinate long exploitation chains. A sequence such as discovering default credentials, using them to find an IDOR, and then escalating privileges is outside the current design.
- **Heuristic assumptions:** AWE’s context and filter abstractions assume recognizable forms of server processing and sanitization. Unusual frameworks, obfuscated sinks, or highly idiosyncratic behavior may violate these assumptions.
- **LLM sensitivity:** Claude Sonnet 4 performed best among the three tested models, but LLM behavior remains variable. Changes in model behavior, availability, or pricing may affect stability and cost.

### Limitations demonstrated by the results

- Overall coverage was only **51.9%**, compared with MAPTA’s **76.9%**.
- AWE was notably weaker on SSTI and command injection despite having specialized agents for them.
- It failed on heavy filtering, authentication irregularities, narrow race-condition windows, and long-horizon stateful workflows.
- One-third of its failures came from deliberately unsupported vulnerability categories, limiting how directly its overall score can be compared with a broad system.
- The DVWA model-selection trials used only **10 runs per vulnerability type**, and no uncertainty estimates or significance tests are provided.
- The three blind-SQL-injection challenges form a very small category, so the difference between 67% and 33% corresponds to only one additional solved challenge.
- Cross-target long-term learning was not evaluated because memory was reset between XBOW challenges.
- The comparison relies on MAPTA’s publicly reported per-challenge results rather than a newly run MAPTA experiment described in this paper.
- Although each XBOW target had a ten-minute budget and the paper states that experiments used identical hardware, detailed hardware specifications are not provided.
- The reported cost-per-solve values in Table II do not appear to align arithmetically with Table I’s solve counts and total costs. The article does not explain this discrepancy.
- Figure 4’s caption describes model-level convergence differences, while the visible panels are organized primarily by difficulty and an XSS-related condition. The underlying per-model histogram values are therefore not fully recoverable from the supplied visual.

The results should consequently be interpreted as evidence of strong targeted performance and efficiency, not as evidence that AWE is a complete replacement for broadly capable autonomous penetration-testing systems.

---

## 8. Future Work or Open Questions

The authors identify a hybrid architecture as the natural next step. Such a system would combine:

- Specialized agents that understand injection contexts, filters, and payload semantics.
- Higher-level general-purpose agents capable of planning long, multi-step attacks.
- Cross-agent coordination for authentication transitions, IDOR chains, privilege escalation, and other stateful workflows.
- Broad semantic exploration for business logic and unfamiliar vulnerability classes.
- Persistent learning from filter signatures, successful bypasses, and historical payload performance.

Other unresolved questions evident from the study include:

- How to coordinate several specialized agents in a single exploitation chain.
- How well long-term memory improves performance across related targets.
- How to handle highly unusual sanitization schemes and obfuscated sinks that do not fit current heuristics.
- How robust AWE remains when the underlying model’s behavior or pricing changes.
- Whether specialization can be extended to the categories where AWE currently trails MAPTA, particularly SSTI and command injection.
- How to retain AWE’s efficiency while adding the broader exploratory capabilities responsible for MAPTA’s higher total coverage.

The envisioned endpoint is an autonomous penetration-testing system that is simultaneously scalable, precise, inexpensive, and capable of semantic, multi-stage reasoning.

---

## 9. High-Level Takeaway (Plain Language)

AWE is an automated web-security tester that gives an AI model a set of carefully designed, vulnerability-specific procedures instead of letting it explore without structure. It remembers what it has tried, studies how a website changes or blocks inputs, adapts its attack payloads, and uses a real browser to prove that an exploit works.

It did not solve as many total challenges as the broader MAPTA system—**54 of 104 versus 80 of 104**—but it was much better on its strongest specialties, solving **87% of XSS challenges** and **67% of blind SQL-injection challenges**. It also used about **98% fewer tokens**, cost **63% less**, and solved successful challenges about **4.4 times faster**. The central lesson is that a well-structured specialist can beat a more powerful general-purpose AI on narrowly defined security tasks, while broad, multi-step attacks still require more flexible reasoning.