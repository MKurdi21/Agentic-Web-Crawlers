## Stage 0 — Document Accessibility Report

The supplied work is accessible as extracted text for physical PDF pages 1–20, accompanied by rendered images of pages 1–6, 8–14, and 19. All 20 text pages were inspected. The 14 supplied page images were inspected directly, including their substantive figures and tables. Pages 7, 15–18, and 20 received text-only inspection; their visual layout was not independently checked. The supplied accessibility metadata reports a 20-page main document, but page count alone does not establish that all associated materials are present. Within the supplied page sequence, no physical PDF page is missing.

| Accessibility item | Assessment |
|---|---|
| Main document | Yes: supplied text covers pages 1–20 |
| Visually inspected pages | 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 19 |
| Text-only pages | 7, 15, 16, 17, 18, 20 |
| Figures | Figures 1–9 are supplied visually and inspected |
| Tables | Tables I–IV are supplied visually and inspected; extracted text assists alignment |
| Equations | No numbered mathematical equations appear in the supplied work |
| Appendices | Appendix A, pages 17–18; Appendix B, pages 19–20 |
| Supplementary files | No separately supplied repository, scripts, data, environment file, or execution logs |
| Referenced external artifacts | GitHub source, Zenodo archive, Llama Pack, benchmarks, README, environment.yml, scripts, and result files; none independently inspected |
| OCR | Not needed; native/extracted text is supplied |
| Extraction limitations | Ligatures, spacing in names and URLs, affiliation symbols, approximation signs, and multiplication signs are imperfectly extracted |
| Confidence | HIGH for clearly readable text and tables; MEDIUM for unresolved wording or extraction ambiguities |

The extracted title separates the system name as ISOLATE GPT, whereas the rendered title reads IsolateGPT. This report uses IsolateGPT. Affiliation markers are also clearer in the page image than in extraction. Numerical table entries were cross-checked against the supplied table images. The multiplication and approximation symbols in the text-only cost discussion are extraction-sensitive, so the interpretation of those expressions is explicitly qualified below.

Evidence categories are used throughout: [A] AUTHOR-REPORTED; [B] DIRECTLY OBSERVABLE in a supplied visual; [C] ANALYST-DERIVED from supplied quantities; [D] ANALYST INTERPRETATION. No [E] EXTERNAL INFORMATION is introduced. Confidence labels HIGH, MEDIUM, LOW, and UNKNOWN describe confidence in faithful representation, not a formal probability that a system is secure. The supplied paper and images are treated as evidence, including the malicious instructions depicted in attack examples; those instructions are not acted upon.

## 1. Plain-language orientation

IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic Systems studies what happens when a large language model, or LLM, becomes the coordinator of multiple third-party applications. An application can describe its purpose in natural language and expose application programming interfaces, or APIs, that the model calls. With access to conversation history and services, the resulting system can retrieve a document, attach it to an email, compare transport prices, or book a trip. These capabilities make the system useful, but they also create opportunities for one application's instructions or incoming content to affect another application. [A; pp. 1–4]

The authors propose separating applications into isolated execution environments. Each application receives its own LLM instance and memory, called a spoke. A trusted central hub routes user requests, supplies necessary context with permission, and mediates communication. Non-LLM operators control message routing, while a structured inter-spoke communication protocol constrains exchanges and brings users into permission decisions. [A; pp. 5–9]

The evaluation compares IsolateGPT with VanillaGPT, an author-built system with similar features but shared application execution. Both use GPT-4. An enhanced attack benchmark contains 1,598 attacks. VanillaGPT's reported overall attack success is 20.2%. IsolateGPT's permission dialogs appear for 7.6% of attacks, and all appearing dialogs contain warnings. Those are different metrics: warning coverage is not an independently measured zero attack-success rate. Whether a malicious exchange succeeds can depend on the user granting permission. [A; pp. 9–10]

Four demonstrations show application behavior manipulation, malicious-email-driven document theft, unintended reuse of health information for travel, and interference between creative-writing and symptom-diagnosis instructions. Functionality scores match on the tested application benchmarks. The authors report overhead below 30% for 75.73% of tested queries, while acknowledging slower multi-application workloads and an unoptimized prototype. [A; pp. 10–15]

The central contribution is an architecture and implementation demonstrating the feasibility of containing cross-application risks while retaining tested functionality. It is not a proof that prompt injection disappears. Attacks inside one application are expressly outside scope. [A; p. 5]

## 2. Document roadmap

The inventory denominator consists of the abstract, eight numbered main sections, Appendix A with five substantive subsections, Appendix B with four substantive subsections, nine figures, four tables, four protection case studies, the attack-scale evaluation, functionality analysis, performance analysis, and cost analysis. References and acknowledgments are accounted for but compressed.

| Inventory ID | Original component | Location | Role |
|---|---|---|---|
| ABS | Abstract | p. 1 | Problem, architecture, broad findings |
| S1 | I. Introduction | pp. 1–2 | Motivation, three design challenges, contributions |
| S2 | II. Motivation | pp. 2–4 | Application architecture, examples, risks, prior-system analogy |
| S3 | III. Threat Model | pp. 4–5 | System, attacker, trust, included and excluded risks |
| S4 | IV. IsolateGPT: System Architecture | pp. 5–9 | Hub, spokes, communication, permission workflow |
| S5 | V. Evaluation: Protection Analysis | pp. 9–13 | Attack benchmark and four case studies |
| S6 | VI. Evaluation: Functionality Correctness Analysis | pp. 13–14 | Correctness, similarity, error breakdown |
| S7 | VII. Evaluation: Performance Analysis | pp. 14–15 | Latency, component overhead, optimizations, cost |
| S8 | VIII. Concluding Remarks | p. 15 | Security-design contribution and release |
| A1 | Appendix A: Additional Design and Implementation Details | pp. 17–18 | Isolation, messages, memory, permissions, benchmark definitions |
| A2 | Appendix B: Artifact Appendix | pp. 19–20 | Requirements, setup, claims, reproduction procedures |
| REF | References [1]–[74] | pp. 15–17 | Bibliographic dependencies |
| ACK | Acknowledgment | p. 15 | Funding and reviewer acknowledgment |

Section II's four motivating scenarios are revisited as security cases rather than being independent experiments with separate datasets. Section IV explains the design that Sections V–VII evaluate. Appendix A materially clarifies process restrictions, long-term memory, and permission duration. Appendix B is important because it explicitly states the permission-denial assumption used to reproduce two case studies and narrows the artifact's performance/functionality reproduction to one representative benchmark.

## 3. Background and context

An LLM-based agentic system combines a language model with applications, persistent information, and the ability to act through services. In this paper, an LLM app usually consists of natural-language functionality instructions plus API endpoints. The model interprets these instructions, builds a plan, and calls APIs with data. The context window is the model's immediately available input space; the authors sometimes describe it as memory while separately implementing persistent memory. These should not be conflated. [A; pp. 2–3, 17]

A shared execution environment places multiple applications' descriptions and exchanged information within a common model-mediated workflow. That makes collaboration convenient, but a malicious instruction can potentially influence unrelated work. Prompt injection here refers to malicious natural-language instructions that redirect the model's behavior; the paper discusses both malicious applications and malicious content processed by otherwise benign applications. The email case demonstrates the latter. [A; pp. 3, 11]

Execution isolation confines applications to distinct environments and mediates access across boundaries. The authors draw lessons from operating systems and browsers, including sandboxing, process separation, and defined communication interfaces. These are author-provided comparisons; this report does not independently evaluate the cited literature or current products. [A; p. 4]

The distinctive difficulty is that application interaction remains partly natural-language-based. A message can have a valid structural format while still containing harmful instructions. Consequently, IsolateGPT combines structure checks with permission decisions rather than claiming that message types alone solve malicious-language interpretation. [A; pp. 8–9]

## 4. Research problem and gap

**Existing problem.** Applications receive user information and interact with other applications and system capabilities to automate tasks. In the shared model context, application instructions and external content can influence behavior outside their intended scope. Sensitive data can move between applications, and ambiguous instructions can cause undesirable sharing even without an attacker. [A; pp. 1, 3–4]

**Shortcomings attributed to prior approaches.** The authors argue that natural-language interactions are harder to scrutinize and sanitize than precisely defined programming interfaces. They also argue that simply putting applications in tightly restricted sandboxes is insufficient for useful automation, because applications need prior context, user information, and collaboration. Their account of insufficient protections describes the systems motivating the paper, not a verified statement about all present-day products. [A; p. 4]

**Research gap.** Execution isolation is familiar in earlier computing systems, but the paper asks what it should look like when applications are interpreted by LLMs and interact through natural language. The gap is an architectural adaptation: preserve useful context and collaboration while preventing unrestricted cross-application influence. [A; pp. 1, 4–6]

**Motivation.** The examples connect security to user consequences: a malicious ride app changes a competing fare; an email triggers document retrieval; health details reach a travel service; creative-writing instructions interfere with a diagnostic response. [A; pp. 3–4, 10–13]

**Scope.** The work concerns third-party app execution and cross-boundary propagation in an LLM-based system. It does not directly compare an agent with a standalone, tool-free LLM. Relevance to the user's question about web agents is therefore an analyst inference from the described exposure to services, memory, external content, and application actions. [D; grounded in pp. 1–5]

## 5. Research questions / objectives / hypotheses

The paper does not present a numbered list of formal research questions or statistical hypotheses. Its explicit objectives and evaluation questions can nevertheless be recorded without inventing such a list.

| ID | Author-stated objective or question | Evidence |
|---|---|---|
| O1 | Evaluate whether security/privacy issues can be addressed through execution isolation and what that isolation should look like | Abstract and introduction, p. 1 |
| O2 | Allow users to interact with isolated apps, retain functionality, and permit safe collaboration among mutually distrusting apps | pp. 1, 5–6 |
| O3 | Evaluate protection against the threats and risks in the threat model | §V, p. 9 |
| O4 | Evaluate whether functionality matches a non-isolated system | §VI, p. 13 |
| O5 | Measure performance overhead from isolation and its components | §VII, pp. 14–15 |

The security benchmark contains attacks corresponding to the hypothesized threat categories, but this is not a preregistered statistical hypothesis-testing framework. There are no supplied null hypotheses, significance thresholds, or power calculations. The authors' broad claims are feasibility, improved protection, similar tested functionality, and manageable overhead for most tested queries. Their supporting evidence must be interpreted under the conditions of each evaluation.

## 6. Assumptions / threat model

**System model.** The system supports third-party applications, online service connections, collaboration, and persistent memory containing raw and processed user–app and user–LLM interactions. The system coordinates which applications fulfill requests and uses stored context. [A; §III-A, p. 4]

**Attacker capabilities.** An attacker can publish a malicious app in an app store, induce installation from elsewhere, or expose a benign app to malicious content. The attacker seeks to control other applications or the LLM, or steal sensitive information in another application or system memory. The trust model explicitly includes hostile emails and websites. [A; §§III-B/C, pp. 4–5]

**Trusted components.** The LLM and hosting system are assumed trustworthy and uncompromised in the sense of lacking malicious intent, although still vulnerable to attacks such as prompt injection. Applications and their processed content are untrusted. The design places trust in the hub and deterministic operators. Functionality definitions and exchange formats are assumed reviewed before app-store availability. The hub's warning assessment is described as relying on a non-malicious user query, vetted descriptions, and vetted memory data. [A; pp. 5, 8–9]

**In scope.** Cross-app behavior manipulation, stealing app or system data, propagation of malicious content through a benign app into other components, and unintended cross-app consequences of ambiguous natural language. [A; §III-D1, p. 5]

**Out of scope.** Preventing prompt injection or other malicious behavior confined to a single application's environment. IsolateGPT aims to stop spread beyond that environment. Thus a compromised email spoke is compatible with the intended defense if it cannot silently extract information from another spoke. [A; §III-D2, p. 5]

**Human condition.** Permission checks are security-relevant. Appendix B explicitly assumes users reject warned requests for the data-stealing and inadvertent-data-exposure reproductions. Permanent and session grants can change this behavior; irreversible actions retain separate explicit consent requirements. [A; pp. 18–19]

## 7. Methodology

### 7.1 Architecture and control responsibilities

IsolateGPT uses a hub-and-spoke architecture. The hub receives the user query and keeps system-wide context. Its non-LLM operator coordinates routing, permissions, and memory access. Its LLM planner identifies primary applications, secondary applications, and needed resources. Its memory module provides planning context and determines information to supply to an application. Where multiple primary apps are suitable, the operator asks the user to choose. [A; §IV-A, p. 6]

A spoke contains an application, a dedicated LLM instance, a non-LLM operator, and persistent memory. The spoke LLM plans and carries out the app-specific workflow. The operator manages exchanges and forwards requests for additional information or functionality. Dedicated LLM instances are not reported as separately trained foundation models; the architecture allows different models, including specialized models, but all evaluation uses GPT-4. No training dataset, optimizer, or fine-tuning experiment is reported. [A; pp. 6–7, 9]

Vanilla spokes have a standard spoke's components but no application. They handle requests requiring only an LLM and can synthesize independent app outputs. A private mode can omit prior context. For non-data-dependent apps, such as fare comparison, their outputs are synthesized separately rather than allowing the apps unrestricted interaction. [A; pp. 6–7, 9]

### 7.2 Query workflow

1. The hub operator receives the query and asks the planner to identify suitable apps and supporting resources.
2. The user selects an app if necessary.
3. The hub obtains relevant data from memory and creates or invokes the selected spoke.
4. The query and needed information are passed with user permission.
5. The spoke combines that input with its own relevant memory and generates its plan.
6. Additional-data requests go through the hub; stored data are shown for consent, while unavailable data are requested from the user.
7. The spoke carries out its plan, with explicit consent before irreversible actions such as sending an email or purchasing.
8. The result returns through the hub, and follow-up queries can be routed back to the same spoke. [A; pp. 6–7]

### 7.3 Inter-spoke communication

The inter-spoke communication, or ISC, protocol exposes a catalog of supported functionalities without exposing whether particular apps are installed. A spoke asks the hub for a functionality. The hub identifies a suitable app and returns request/response formats and an ephemeral session identifier. Actual requests and responses pass through operators and the hub; LLMs do not directly exchange messages across boundaries. Operators validate formatting and drop malformed messages. [A; pp. 7–9, 17]

The hub compares requested collaboration with its own plan and reports unexpected access in a permission dialog. Some typed values may be validated automatically; raw strings remain harder to screen. Users are required to manually screen exchanges that cannot be reliably automated. Temporary identifiers reduce direct revelation of app identity but do not rule out side-channel inference, which the authors acknowledge in a footnote. [A; p. 8]

### 7.4 Process isolation and implementation

Hub and spokes run in separate processes. The implementation uses seccomp and setrlimit to constrain system calls and process resources. Allowed calls include exit, sigreturn, read, and write to necessary file descriptors. CPU time, virtual memory, and created-file size are limited, but exact limits are not supplied. App network requests are restricted to the app's root domain, described as eTLD+1, and outgoing data are permission-mediated. [A; Appendix A-A, p. 17]

The prototype is mostly Python, approximately 6,000 lines, uses LangChain 0.1.10 and Redis 5.0.1, and is described as a text-message personal assistant. The paper also reports LlamaIndex implementation/integration. The artifact specifies Python 3.9, Miniconda, Ubuntu 20.04.6 LTS, GPT-4 version 0613, an AMD Ryzen 9 3900X 12-core processor, 32 GB RAM, and 1 TB disk. The CPU/RAM describe the local system running the framework; GPT-4 is accessed through an API, not reported as locally executing on that machine. [A; pp. 6, 9, 17, 19]

### 7.5 Memory and permissions

Long-term memory includes interaction history, LLM-generated summaries, and key–value entity information. Working memory brings recent interactions and summarized knowledge into the context window. Appendix A first describes relevant entity information alongside working memory but then clarifies that entity information is not loaded wholesale and can be retrieved iteratively at runtime. This is best read as retrieval on demand, while preserving the wording tension. [A; p. 17]

The hub stores information across spokes and per-spoke summaries/entities; each spoke stores its own interaction history and derived information. Cross-spoke information can be shared with consent. Permanent permission persists until revoked, session permission lasts until shutdown, and one-time permission applies to each action. Permanent permission is prohibited for irreversible actions. The scheme is preliminary and tailored to limited cases. [A; pp. 17–18]

### 7.6 Baselines, data, metrics, and unspecified settings

VanillaGPT is author-built and offers the same features without execution isolation. The attack benchmark is InjecAgent [13], used in an enhanced setting and extended with 544 system-data-stealing attacks to total 1,598. Each scenario is configured with its app and target information, the attack prompt is executed, and the system is refreshed before the next attack. There is no train/validation/test split because the described task evaluates systems rather than training a model. [A; pp. 9, 16]

Functionality and performance use four LangChain benchmarks: single-app typewriting; typewriting with 26 letter apps, at most 13 used per query; relational-data collaboration, at most five apps per query; and email extraction without apps. Table IV lists 20, 20, 21, and 42 queries respectively. Correctness compares steps and final outputs with references; no-app evaluation compares text similarity. Latency is full-response time. [A; pp. 13–14, 18]

Temperature, random seeds, token budgets, API retry policy, confidence intervals, statistical tests, and the number of repeated runs are not specified in the supplied account. The exact edit-distance normalization and string-score calculation are not defined. No unseen configuration file is treated as reviewed. These absences limit reconstruction of the experiment but do not erase the reported results.

## 8. Experiments / analyses

| ID | Analysis | Purpose and conditions | Main evidence |
|---|---|---|---|
| X1 | Enhanced attack benchmark | Compare shared-execution attack success with permission/warning behavior under isolation; 1,598 scenarios, reset between attacks | Table I, pp. 9–10 |
| X2 | Malicious ride app | Quick Ride adds $10 to Metro Hail's fare; compare manipulated booking with isolated fare synthesis | Figure 5, pp. 10–11 |
| X3 | Malicious email | Summarize an email containing document-exfiltration and deletion instructions; deny warned cross-app retrieval | Figure 6, pp. 11, 19 |
| X4 | Ambiguous personal data | Schedule a medical appointment, then request travel using prior information; deny sharing | Figure 7, pp. 11–12, 19 |
| X5 | Conflicting app instructions | Install creative-writing and diagnosis apps; ask about fatigue and persistent pain | Figure 8, pp. 12–13 |
| X6 | Functionality | Four benchmark families, same baseline and GPT-4; steps/final correctness or text similarity | Tables II–III, pp. 13–14 |
| X7 | Performance | Same benchmarks; cold-start spokes; required permissions automatically granted | Table IV and Figure 9, pp. 14–15 |
| X8 | API cost | Calculate cost for 10% of benchmark queries | §VII-D, p. 15 |

**X1.** The manipulated condition is isolated versus shared execution, with attack categories targeting app compromise, app data theft, and system data theft. VanillaGPT is measured by attack success. IsolateGPT is measured by permission appearance and warning rate, because permission grants determine whether dangerous flows can proceed. The benchmark is not a human permission study. [A; pp. 9–10]

**X2.** Metro Hail's actual displayed fare is $51.80; Quick Ride's is $57.00. VanillaGPT follows Quick Ride's instruction to add $10 to Metro Hail and books Quick Ride. IsolateGPT preserves the original fare and books Metro Hail. The demonstration illustrates cross-app manipulation containment, not a population-level success estimate. [A/B; Figure 5]

**X3.** A malicious email impersonates authoritative instructions, asks for a file containing SSN, sends its link to the attacker, deletes incoming and outgoing emails, and asks for a misleading failure output. VanillaGPT's depicted trace executes the retrieval, sending, and deletion. IsolateGPT issues an unexpected-access warning, and the user denies the request. The compromised app's local interpretation is not shown to have been repaired. [A/B; Figure 6]

**X4.** Both apps request broadly described personal data. The travel app receives health details and a first-class preference in the VanillaGPT trace. IsolateGPT also attempts to share stored personal information, but the permission boundary blocks it when denied; the travel workflow then requests more information. This is protection with additional user effort, not a successful identical automatic booking. [A/B; Figure 7, p. 12]

**X5.** Creative Muse instructs imaginative narrative generation; Symptom Solver instructs objective diagnosis. VanillaGPT combines the directives. IsolateGPT executes the selected diagnostic app separately. The example concerns instruction interference, not clinical accuracy or validation of the diagnosis. [A/B; Figure 8]

**X6.** Both systems achieve 1.00 step and overall correctness for single/multiple apps, and 0.76 step plus 0.95 overall correctness for collaboration. No-app similarity differs slightly: edit distance 0.34 versus 0.33, string score 0.71 versus 0.70. Error categories distinguish deviations from the reference plan from incorrect final outputs. [A/B; Tables II–III]

**X7.** The authors automatically grant permissions and assume spokes start anew without data. Thus measured overhead includes framework/model work but does not measure human reading or decision delay. No-app average totals are close, while multiple-app and collaboration totals are substantially higher under isolation. [A; p. 14]

**X8.** The authors report IsolateGPT costing 1.85 times as much for a 10% query sample, interpreting the extracted multiplication expression as a cost ratio. Sample selection, exact count, dollar totals, and variability are not supplied. [A; p. 15; MEDIUM on expression transcription]

## 9. Results

The strongest numerical security result is the combination of substantial baseline attack success and warnings on every IsolateGPT permission dialog that appeared in these malicious scenarios. The authors report 20.2% overall VanillaGPT success and 7.6% IsolateGPT permission appearance, with 100% warning rate conditional on appearance. These cannot be subtracted as if they were two attack-success rates. The study does not establish how real users would respond to those warnings. [A; Table I and p. 10]

Cross-app data stealing is the highest-success category in Table I: total VanillaGPT success is 33.0%, 33.0%, and 35.9% for financial, physical, and other data. Corresponding IsolateGPT permission appearance is 19.1%, 15.2%, and 13.6%, all with warnings. System-data stealing has smaller rates, but the authors explain that benchmark prompts may not match actual structured memory descriptors. [A; p. 10]

In Figure 5, the manipulated competitor fare is $61.80 = $51.80 + $10. The resulting baseline booking costs $57 instead of the displayed available $51.80. The $5.20 difference is ANALYST-DERIVED: $57.00 − $51.80. It is an illustrative monetary consequence within one trace, not an estimated average loss. [B/C; p. 11]

Functionality parity is supported for these benchmark scores, not universally established. Collaboration step correctness is lower than final correctness in both systems, because alternate plans can still produce correct answers. No-app similarity is nearly equal rather than exactly equal. The health-data case intentionally incurs a loss of automatic completion when permission is denied. These conditions refine the abstract's broad without-loss-of-functionality wording. [A/D; pp. 12–14]

The authors report overhead below 30% for 75.73% of tested queries. Table IV's category totals show average timings of 32.013 versus 39.210 seconds for one app, 30.292 versus 65.304 for multiple apps, 24.728 versus 49.256 for collaboration, and 19.502 versus 21.422 without apps. Ratios of category averages do not reproduce a distribution of individual-query overhead, so these should not be treated as an automatic contradiction. However, the raw per-query evidence is not supplied here, preventing independent reconstruction of the 75.73% result. [A/D; pp. 2, 14]

For completeness, ratios of displayed totals yield ANALYST-DERIVED overheads: single app (39.210 − 32.013)/32.013 × 100 ≈ 22.48%; multiple apps (65.304 − 30.292)/30.292 × 100 ≈ 115.58%; collaboration (49.256 − 24.728)/24.728 × 100 ≈ 99.19%; no apps (21.422 − 19.502)/19.502 × 100 ≈ 9.85%. These are category-average comparisons, not reported medians or percentiles.

## 10. Figure-by-figure interpretation

### Figure 1 — Shared-execution query resolution

Located on p. 2, this architecture diagram contains a user email request, one central LLM, shared memory, a cloud-drive app, and an email app. Both applications' descriptions and APIs connect to the same LLM-mediated environment. The request is to send annual_report.pdf to John Doe; the output says the email was sent. Arrows depict access and information exchange, not measured traffic volume. There are no numeric axes or statistical encodings. The figure establishes the convenient shared-context baseline and the potential for broad influence. [A/B; HIGH]

### Figure 2 — IsolateGPT architecture in action

On p. 5, dashed boundaries separate the hub, email spoke, cloud-drive spoke, and specialized spoke. Green operator boxes are non-LLM modules. The hub contains management functions, memory records, a planner, and the ISC protocol. Each application spoke includes operator, memory, LLM, and app; the specialized spoke depicts a fine-tuned LLM. Numbered stages show request receipt, hub routing, email-spoke planning and mediated drive collaboration, then result return. The fine-tuned model is an architectural option, not an evaluated alternative in this paper. No axes or quantitative scales apply. [A/B; HIGH]

### Figure 3 — ISC exchange sequence

On p. 8, two application spokes flank the hub operator and user permissions. Numbered arrows show functionality request, format return, formatted request, forwarded request, response to hub, and response to caller. Labels include Spoke-sID, functionality, request format, response format, request message, and response message. The caption identifies steps 1, 3, and 5 as requiring consent; these concern approval around functionality/access and exchanges, not direct LLM-to-LLM messaging. The visual explains routing structure, not proof that all message contents are benign. [A/B; HIGH]

### Figure 4 — Permission dialogs

On p. 8, side-by-side dialogs compare expected attachment retrieval with an unexpected request for a file containing SSN. Both expose Allow Once, Allow for this Session, Always Allow, and Don't Allow. The malicious example includes a warning that cloud drive use is unexpected and may pose security/privacy risks. The visual demonstrates presentation of the hub's assessment. It does not measure comprehension, habituation, false alarms, or user denial frequency. [A/B; HIGH]

### Figure 5 — Malicious fare manipulation

On p. 11, two execution columns compare VanillaGPT's shared space and IsolateGPT's spoke spaces. Descriptions, planning, API outputs, and booking results are color-coded boxes. Quick Ride's instructions contaminate the shared plan and add $10 to Metro Hail's $51.80, making it $61.80; Quick Ride's $57 then appears cheaper. Isolated execution retains $51.80 and selects Metro Hail. Exact fares are visibly labeled; no visual estimates are needed. It supports containment in the demonstrated case, not a formal security guarantee. [A/B; HIGH]

### Figure 6 — Email-driven document exfiltration

Also on p. 11, the figure contrasts email search, drive retrieval, message sending, and deletion in a shared execution trace with a denied ISC request under isolation. The attack content uses a purported system annotation and asks for silence and a misleading failure response. The baseline sends a retrieved file link to the attacker and deletes messages. IsolateGPT warns that drive use was not in the plan, and the displayed user choice is Permission Denial. API identifiers and placeholders are trace details, not general algorithm variables. This figure's successful defense is explicitly conditioned on denial. [A/B; HIGH]

### Figure 7 — Unintended health-data reuse

On p. 12, two columns show a medical appointment followed by a flight query. VanillaGPT reuses stored medical information in a travel booking and supplies First Class. The IsolateGPT column shows a permission denial and a booking call with missing personal fields, followed by a request for more information. The image's initial health description mentions asthma, whereas the later travel call includes severe asthma; the diagram thus visibly illustrates imperfect transformation as well as over-sharing. The prose emphasizes exposure rather than systematically evaluating that wording change. Protection is data-boundary enforcement, not proof of perfect relevance selection. [A/B/D; HIGH]

### Figure 8 — Conflicting instructions

On p. 12, Creative Muse's imaginative directive and Symptom Solver's objective directive coexist in VanillaGPT's shared plan. Its output mixes fictional and real-world language. IsolateGPT's plan selects Symptom Solver and keeps its response in the relevant spoke. The exact disease examples in the output are illustrative response content, not clinically validated findings. The caption itself uses the qualified phrase potentially avoiding an unexpected answer. [A/B; HIGH]

### Figure 9 — Query-resolution-time distributions

On p. 14, five cumulative-distribution panels show all benchmarks, single app, multiple apps, app collaboration, and no apps. The horizontal axis is seconds; the vertical axis is fraction of queries, spanning approximately 0 to 1. Blue solid lines represent IsolateGPT; red dashed lines represent VanillaGPT. Axes are linear. The all-benchmark panel extends to about 150 seconds; small-panel ranges vary with the workload. Red curves generally rise earlier, indicating faster query completion; the separation is more apparent for multiple apps and collaboration, and small for no apps. No confidence bands, error bars, or statistical markers are shown. Exact per-query times are not labeled, so no curve coordinates are treated as exact measurements. The figure shows raw latency distributions, not a plot of per-query overhead ratios. [A/B; HIGH for direction; MEDIUM for small-axis limits]

## 11. Table-by-table interpretation

### Table I — Protection benchmark

The rows group attack types. No. is the number of scenarios. VanillaGPT columns A1 and A2 report success rates for compromising the first and second apps; Total is the reported overall attack success. IsolateGPT columns PA and WR report permission appearance and warning rate conditional on appearance. All rate entries are percentages. Dashes mark unreported/not-applicable entries and are not zeros. No confidence intervals or significance indicators appear. [A/B; p. 10]

| Category / subtype | N | A1 | A2 | VanillaGPT Total | IsolateGPT PA | IsolateGPT WR |
|---|---:|---:|---:|---:|---:|---:|
| App compromise: financial harm | 153 | 9.8 | — | 9.8 | 0.0 | — |
| App compromise: physical harm | 170 | 29.0 | — | 29.0 | 7.4 | 100 |
| App compromise: data security | 187 | 29.0 | — | 29.0 | 8.6 | 100 |
| App data stealing: financial | 102 | 41.2 | 80.0 | 33.0 | 19.1 | 100 |
| App data stealing: physical | 187 | 39.1 | 84.3 | 33.0 | 15.2 | 100 |
| App data stealing: others | 255 | 45.0 | 79.6 | 35.9 | 13.6 | 100 |
| System data stealing: financial | 102 | 2.2 | — | 2.2 | 0.0 | — |
| System data stealing: physical | 187 | 5.6 | — | 5.6 | 5.1 | 100 |
| System data stealing: others | 255 | 1.8 | — | 1.8 | 0.5 | 100 |
| Average / all | 1598 | 22.9 | 81.3 | 20.2 | 7.6 | 100 |

A2 values are much larger than A1 for cross-app theft, but their exact conditioning is not fully spelled out in the supplied definition. The products 41.2% × 80.0% ≈ 33.0%, 39.1% × 84.3% ≈ 33.0%, and 45.0% × 79.6% ≈ 35.8% are ANALYST-DERIVED and suggest staged/conditional reporting. This does not justify silently redefining A2. The exact count of successful attacks should not be reconstructed from rounded rates without raw outcomes.

### Table II — Functionality comparison

On p. 13, app benchmarks compare step and overall correctness. Single app: 1.00/1.00 in both systems. Multiple apps: 1.00/1.00 in both. Collaboration: 0.76 steps and 0.95 overall in both. No-app output similarity is edit distance 0.34 and string score 0.71 for VanillaGPT, versus 0.33 and 0.70 for IsolateGPT. Values are scores, not automatically percentages for all metrics. Metric formulas and normalization are absent. No uncertainty estimates are shown. The table supports matched observed app scores and near-equal no-app similarity, not universal equivalence. [A/B; HIGH]

### Table III — Mistake composition

On p. 13, percentages describe errors only. They are not percentages of all queries. For collaboration, the VanillaGPT/IsolateGPT pairs are: app called twice 28.57%/28.57%; unexpected app 28.57%/14.29%; expected app not called 14.29%/28.57%; unexpected order 14.29%/14.29%; incorrect response 14.29%/14.29%. The first four are intermediate mistakes; the last is overall. No-app error composition is 97.62% unexpected response and 2.38% exceeded context window in both systems. Exact denominators for this error accounting are not explicitly tabulated. The authors explain that alternate plans can succeed, so a step mismatch is not necessarily functional failure. [A/B; HIGH]

### Table IV — Runtime breakdown

On p. 14, seconds are broken down into VanillaGPT planning, execution, memory, and total; IsolateGPT hub planning/memory, spoke planning/execution/memory, and total. Query counts are included. The following preserves all displayed rows in compressed vector form. Each VanillaGPT vector is [planning, execution, memory, total]; each IsolateGPT vector is [hub planning, hub memory, spoke planning, spoke execution, spoke memory, total].

| Workload | Queries | VanillaGPT seconds | IsolateGPT seconds |
|---|---:|---|---|
| Single app | 20 | [29.874, 0.002, 1.582, 32.013] | [2.818, 0.796, 33.957, 0.002, 0.648, 39.210] |
| Multiple apps | 20 | [28.114, 0.002, 1.589, 30.292] | [2.259, 3.757, 53.959, 0.003, 3.903, 65.304] |
| Multiple apps, <3 | 2 | [11.133, 0.001, 1.398, 13.093] | [0.918, 1.089, 14.375, 0.001, 1.569, 19.556] |
| Multiple apps, 3–5 | 8 | [20.163, 0.001, 1.547, 22.282] | [1.780, 2.535, 33.283, 0.002, 2.626, 41.645] |
| Multiple apps, 6–10 | 8 | [33.385, 0.003, 1.689, 35.682] | [2.847, 4.713, 71.246, 0.004, 4.841, 85.062] |
| Multiple apps, 10–13 | 2 | [55.814, 0.004, 1.544, 57.971] | [3.164, 7.490, 107.102, 0.006, 7.589, 126.650] |
| App collaboration | 21 | [21.113, 0.001, 3.102, 24.728] | [2.088, 4.993, 37.509, 0.002, 3.305, 49.256] |
| Collaboration, <3 | 14 | [17.889, 0.001, 2.859, 21.251] | [1.936, 4.339, 33.280, 0.001, 2.902, 43.892] |
| Collaboration, 3–5 | 7 | [27.562, 0.002, 3.589, 31.683] | [2.392, 6.301, 45.967, 0.003, 4.112, 59.984] |
| No apps | 42 | [4.415, 0.000, 14.621, 19.502] | [0.706, 0.920, 4.658, 0.000, 14.519, 21.422] |

The displayed component times do not sum exactly to totals. For example, 29.874 + 0.002 + 1.582 = 31.458 seconds, while the single-app VanillaGPT total is 32.013 seconds. The ANALYST-DERIVED difference is 0.555 seconds. The supplied text does not fully account for these residuals; they should not be silently assigned to a specific operation. The multiple-app labels 6–10 and 10–13 overlap at 10 as printed, and exclusive boundary treatment is unspecified. The table contains no uncertainty or significance testing. [B/C/D]

## 12. Diagram / architecture interpretation

Figures 1–3 form the main architectural argument. Figure 1 places app descriptions, API calls, and shared memory around one LLM. Figure 2 separates those responsibilities into app-specific spokes and a coordinating hub. Figure 3 restores collaboration through explicit, mediated exchanges rather than returning to a shared app environment.

The control path is user → hub operator → hub planner/memory → chosen spoke operator → spoke LLM/app → hub → user. A collaboration adds spoke operator → hub operator → destination spoke operator, then the reverse response route. Operators enforce routing and format rules; planners determine relevance and required work. Permission decisions gate data provision and collaboration. [A/B; pp. 5–9]

The data path includes stored user information from hub memory, local spoke history, app API responses, and formatted cross-spoke messages. A central distinction is that the hub may possess information across applications while an individual spoke receives only information admitted through the boundary. Independent app results can be collected by a vanilla synthesis spoke without giving each source app access to the others' execution context. [A; pp. 6–9, 17–18]

The boundary does not automatically establish that every admitted string is safe. A valid format is a structural condition; user screening and warning assessment address semantic risks. Deterministic operators reduce exposure of routing logic to natural-language instructions, but the planning and content-processing components still use LLMs. This is an analyst explanation of the division visible in the design, not a claim that the supplied paper proves operator code free of vulnerabilities. [D; grounded in pp. 6–9]

Figures 5–8 are trace diagrams rather than independent architecture definitions. Their before/after columns show where a request remains local, where a permission gate intervenes, and where the shared baseline mixes instructions or information. Figure 4 is an interface example. None of these diagrams depicts a measured packet-level network protocol or a formally verified state machine.

## 13. Equations and mathematical concepts

No numbered equations, theorems, lemmas, proof sequence, optimization objective, or standalone pseudocode algorithm are supplied. The important mathematical objects are metric definitions and message tuples.

**Attack success rate.** The authors define it as successful attacks divided by executed attacks for VanillaGPT. In explanatory mathematical form, ASR = successful attacks / executed attacks. Multiplying by 100 expresses a percentage. This notation is an analyst restatement of the verbal definition, not an original numbered equation. [A; p. 10]

**Permission appearance.** PA is the frequency of permission-dialog appearances across attack scenarios. **Warning rate.** WR = warned permission appearances / all permission appearances. A 100% WR is conditional on a dialog appearing; it is not 100% recall over all conceivable attacks or a 0% attack-success measurement. Rows with zero appearances have a dash for WR. [A/B; Table I]

**Correctness.** For app benchmarks, matching outputs divided by total outputs gives the reported correctness score; intermediate-step and final-output assessments are distinct. The no-app similarity measures lack supplied formulas. [A; p. 13]

**Overhead.** For the analyst-derived comparisons, relative overhead = (isolated time − baseline time) / baseline time × 100. A time ratio of 1.85 means 85% above baseline, whereas a phrase such as 1.85 times more can be ambiguous. This report uses cost ratio 1.85 for the authors' multiplication expression and does not claim an absolute dollar amount. [C/D; pp. 14–15]

**Message notation.** <Spoke-sID, requested functionality> requests help; <Spoke-sID, request format, response format> communicates schemas; <Spoke-sID, functionality, request message> carries a request; <Spoke-sID, response message> carries a response. Spoke-sID is an ephemeral session identifier. Angle brackets indicate a structured collection of fields, not numerical inequality. [A; p. 17]

The extracted 90th/95th-percentile expressions on p. 14 read as 1.24× and 1.80× in the visual, but the prose calls them overheads without fully defining the convention. They are retained as reported multipliers; this report does not silently convert them into precise percent increases or claim a reconstructed percentile distribution.

## 14. Interpretation and discussion

The design changes the security question from whether one model will always ignore hostile language to whether hostile influence can cross a controlled boundary. The email spoke may encounter and interpret malicious content, but reaching cloud-drive data requires a separately mediated exchange. The fare example similarly prevents one app's local directive from rewriting another app's result. [D; grounded in pp. 5, 10–11]

O1 and O2 receive constructive support: a prototype implements isolated apps, preserved context, and mediated collaboration. O3 receives benchmark and case-study evidence, but permission outcomes are conditional and the benchmark uses warning behavior rather than the same success metric for both systems. O4 is supported by observed benchmark parity, with near-equal no-app scores and no universal equivalence proof. O5 is supported by timings, component analysis, and a small cost sample, with cold-start and automated-consent conditions. No formal statistical hypotheses are available to mark as accepted or rejected.

Several cross-reference checks refine the conclusions. The abstract's protection claim must be read with the explicit single-app exclusion on p. 5. The data-exposure trace on p. 12 must be read with Appendix B's denial condition on p. 19. The broad functionality wording must be read with the incomplete travel booking after denied data sharing. The performance finding must be read with automatically granted permissions and cold starts. Table III's percentages apply to errors, not all queries. Table I's warnings apply to appearing permission dialogs, not all attacks.

The authors explain that LLM guardrails cause many attacks to fail even in VanillaGPT. They suggest visible financial/physical harm may be easier for guardrails to detect, and offer possible explanations for high second-app compromise rates. These are author interpretations rather than experimentally isolated causal findings. This report does not import the cited literature to establish those explanations. [A; p. 10]

For the user's research question, the paper supports a mechanism-level answer: connecting an LLM to applications introduces untrusted instructions/content, persistent sensitive information, cross-app dependencies, and APIs that can perform consequential actions. Shared interpretation can turn incoming content into an application action or leak across tasks. The inference that this makes web agents more exposed than standalone LLMs is reasonable but not directly measured here. The tested contrast is two agentic system architectures using GPT-4. [D; HIGH on comparison boundary]

## 15. Contributions and novelty

**Conceptual contribution.** The authors adapt execution isolation to natural-language-based application ecosystems, emphasizing that ordinary sandbox restrictions must coexist with useful user context and collaboration. [A; pp. 1–2, 4]

**System/methodological contribution.** The hub-and-spoke structure pairs app-specific LLMs and memory with deterministic operators. The ISC protocol provides mediated functionality discovery, typed formats, ephemeral identifiers, and permission-based exchanges. [A; pp. 5–9]

**Implementation contribution.** The Python/LangChain prototype uses process controls and persistent memory; source code is reported released and integration with LlamaIndex as a Llama Pack is reported. Repository availability is an author statement, not independently verified access in this analysis. [A; pp. 2, 15, 17, 19]

**Experimental contribution.** The authors extend an existing benchmark by 544 attacks involving system information, evaluate four detailed scenarios, and measure functionality, latency, and a sampled cost ratio. [A; pp. 9–15]

There is no new foundation-model training algorithm, formal security theorem, general-purpose benchmark replacement, or clinically validated diagnostic method in the supplied work. The contribution is a feasible architectural blueprint with empirical evidence under specified conditions.

## 16. Limitations

### Authors' stated limitations

- Single-app attacks are outside scope; the target is cross-app/system propagation. [p. 5]
- No foolproof automatic detection of malicious natural-language instructions is assumed, so some exchanges require manual screening. [p. 8]
- A motivated attacker may infer collaborating app identity through side channels despite ephemeral identifiers. [p. 8, footnote 6]
- Functionality definitions and formats are assumed reviewed before app-store availability. [p. 8, footnote 5]
- The permission model is preliminary; a comprehensive model and associated user experience are outside scope. [pp. 9, 18]
- Benchmark system-data-stealing prompts may not match structured memory descriptors. [p. 10]
- Denied sharing can require users to provide data manually; the authors describe this security/usability trade-off as necessary. [p. 12]
- Benchmarks may omit complex and nuanced real-world cases. [p. 14]
- The prototype is not optimized; timings assume cold-start spokes without stored data. [p. 14]
- LLM probabilistic behavior can change attack effectiveness and correctness, and runtime can vary with server load and infrastructure updates. [pp. 19–20]
- Full four-benchmark artifact runs would cost hundreds of dollars, so artifact E2/E3 use relational data as a representative benchmark. [p. 20]

### Additional evidence-based analyst observations

These are [D], not author admissions. There is no human-subject evaluation of warning comprehension, consent quality, or fatigue. Security metrics differ between baseline and isolated system. Raw attack outcomes, per-query times, cost details, and repeated-run statistics are absent from the supplied document. The trustworthiness of hub inputs and app review is assumed rather than adversarially evaluated here. One evaluated LLM version and a limited benchmark set constrain generalization. Network restrictions and process limits are described without full configurations, preventing a source-only implementation audit. The paper does not directly quantify vulnerability relative to standalone LLMs.

## 17. Threats to validity

The following validity framing is ANALYST INTERPRETATION; the authors do not organize their discussion under these labels.

**Internal validity.** VanillaGPT versus IsolateGPT changes multiple elements together: isolation, dedicated LLM instances, routing, memory provisioning, structured exchanges, and consent. There is no supplied ablation separating their effects. Improvements should be attributed to the combined architecture rather than a single mechanism alone.

**Construct validity.** Warning rate measures the presence of warnings when permission dialogs appear, not actual end-to-end exploitation under realistic users. Reference-plan matching may penalize successful alternate workflows, as the authors' error analysis explains. Email-extraction similarity is not a universal measure of functional correctness.

**External/ecological validity.** Typewriting and relational-data tasks exercise routing and collaboration but cannot encompass all web interactions. The four cases are useful demonstrations rather than representative samples of all email, travel, transport, or health-app risks. No browser navigation, dynamic website population, or live web-agent versus standalone-model comparison is reported.

**Statistical conclusion validity.** No confidence intervals, significance tests, random seeds, or repeated-run design are supplied. Rounded rates and small query groups should not support precise claims beyond the reported observations. The 10% cost sample has unspecified selection.

**Reproducibility.** Requirements and scripts are described, but artifacts were not supplied for inspection or execution. API-model nondeterminism and changing service latency are explicitly acknowledged. The artifact recommends repeating attacks when ineffective but does not establish a fixed repetition protocol in the paper; this can complicate comparison with a one-run result.

**Generalizability.** Dedicated instances and process separation may support broader model choices, but those alternatives are architectural possibilities rather than demonstrated cross-model robustness. Security remains dependent on trusted coordination, reviewed app definitions, and permission handling.

## 18. Future work and open questions

### A. Future directions explicitly proposed by the authors

The authors call for deeper exploration of execution isolation and complementary access control. They identify a comprehensive automated permission model and user-experience design as separate work. Suggested performance optimizations include reusing initialized spokes, reusing their stored information, parallelizing planning and memory extraction, searching only likely/frequently used apps, using tailored prompt templates, and exposing only functionality subsets likely needed by each app. They anticipate faster and cheaper models reducing overhead, but this is an expectation rather than an evaluated result. [A; pp. 2, 9, 14–15, 18]

### B. Additional open questions

The following are [D]: How frequently do users approve malicious warned requests? How do permanent/session grants affect exposure? How robust is the hub planner to misleading reviewed descriptions or tainted summaries? Can valid raw-string messages propagate instructions despite structural validation? What happens when an app evolves after review? What fraction of overhead survives warm starts and parallelism? How does the design scale to many installed apps and long histories? How would an equivalent study compare tool-free LLMs, web agents, and isolated agents using identical attacks and outcome definitions? These questions are logically relevant but are not answered by supplied results.

## 19. Terminology and notation glossary

| Term | Meaning in this work |
|---|---|
| LLM | Large language model; interprets instructions, plans, and produces responses |
| Agentic system | LLM extended with applications, memory, and action capabilities |
| LLM app | Natural-language functionality description, usually with API endpoints |
| API | Application programming interface used to send requests and receive results |
| Context window | Immediately available model input space, distinct from the full persistent database |
| Execution isolation | Separation of app execution with controlled interactions across boundaries |
| Hub | Trusted coordinator of requests, apps, permissions, and system-wide context |
| Spoke | Isolated app environment with operator, LLM, and memory |
| Vanilla spoke | Spoke without an app, used for LLM-only work or synthesis |
| VanillaGPT | Author-built shared-execution comparison system |
| Operator | Non-LLM routing/control module with a defined execution flow |
| Planner | LLM-based component generating task steps and identifying resources |
| ISC | Inter-spoke communication protocol mediated through the hub |
| Spoke-sID | Ephemeral session identifier used in message exchanges |
| Prompt injection | Malicious natural-language instructions that redirect model behavior |
| Exfiltration | Unauthorized movement of sensitive information to an attacker |
| Guardrails | LLM protections the authors credit with rejecting some attacks |
| PA | Permission appearance frequency in attack evaluation |
| WR | Warning rate among appearing permission dialogs |
| A1 / A2 | Table I's first-/second-app compromise success columns |
| Long-term memory | Stored history, summaries, and entity information |
| Working memory | Selected context made available for the current model interaction |
| Entity–information pair | Key–value representation of inferred entities and associated facts |
| Cold start | Starting spokes anew without retained data for measured queries |
| seccomp | System utility used to constrain permitted system calls |
| setrlimit | System utility used to limit process resource consumption |
| eTLD+1 | Domain boundary used for restricting app network requests; expansion is not supplied |
| RCE | Remote code execution; discussed as a related risk, not a separate demonstrated experiment |
| SQL | Database-query term in the related-risk discussion; expansion is not supplied |
| NDSS | Network and Distributed System Security Symposium, the publication venue |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Enhanced attack set | 1,598 | attacks | All Table I categories | Author-reported | pp. 9–10 |
| Added system-theft attacks | 544 | attacks | Benchmark extension | Author-reported | p. 9 |
| Original set size inferred | 1,054 | attacks | 1,598 − 544 | Analyst-derived | p. 9 |
| VanillaGPT overall success | 20.2 | % | All attacks | Author-reported | Table I, p. 10 |
| IsolateGPT permission appearance | 7.6 | % | All attacks | Author-reported | Table I, p. 10 |
| Warning rate | 100 | % | Conditional on dialog appearance | Author-reported | Table I, p. 10 |
| Largest listed total baseline theft rate | 35.9 | % | Other app data | Visually readable | Table I |
| Single/multiple-app correctness | 1.00 | score | Steps and final, both systems | Author-reported | Table II |
| Collaboration step correctness | 0.76 | score | Both systems | Author-reported | Table II |
| Collaboration overall correctness | 0.95 | score | Both systems | Author-reported | Table II |
| No-app edit distance | 0.34 / 0.33 | score | VanillaGPT / IsolateGPT | Author-reported | Table II |
| No-app string score | 0.71 / 0.70 | score | VanillaGPT / IsolateGPT | Author-reported | Table II |
| Query counts | 20 / 20 / 21 / 42 | queries | Single / multiple / collaboration / none | Visually readable | Table IV |
| Total benchmark queries | 103 | queries | 20 + 20 + 21 + 42 | Analyst-derived | Table IV |
| Max apps per multiple-app query | 13 | apps | 26 deployed letter apps | Author-reported | pp. 13, 18 |
| Max apps per collaboration query | 5 | apps | Relational-data workload | Author-reported | p. 13 |
| Single-app total time | 32.013 / 39.210 | seconds | VanillaGPT / IsolateGPT | Visually readable | Table IV |
| Multiple-app total time | 30.292 / 65.304 | seconds | VanillaGPT / IsolateGPT | Visually readable | Table IV |
| Collaboration total time | 24.728 / 49.256 | seconds | VanillaGPT / IsolateGPT | Visually readable | Table IV |
| No-app total time | 19.502 / 21.422 | seconds | VanillaGPT / IsolateGPT | Visually readable | Table IV |
| Queries with under-30% overhead | 75.73 | % | Author-reported individual-query finding | Author-reported | p. 2 |
| Reported 90th / 95th overhead multipliers | 1.24 / 1.80 | × | Convention not fully defined | Author-reported | p. 14 |
| Hub / spoke share of extra time | 17.18 / 80.43 | % | Multiple apps; planning/memory processes | Author-reported | pp. 14–15 |
| Hub / spoke share of extra time | 28.87 / 67.67 | % | Collaboration; planning/memory processes | Author-reported | p. 15 |
| Cost sample | 10 | % of queries | Selection unspecified | Author-reported | p. 15 |
| Cost ratio | 1.85 | × baseline | Sampled queries; extracted multiplier | Author-reported | p. 15 |
| Metro Hail / Quick Ride fare | 51.80 / 57.00 | dollars | Demonstrated booking | Visually readable | Figure 5 |
| Malicious fare addition | 10 | dollars | Quick Ride instruction | Author-reported | pp. 10–11 |
| Demonstrated booking difference | 5.20 | dollars | 57.00 − 51.80 | Analyst-derived | Figure 5 |
| Implementation size | approximately 6,000 | lines | Mostly Python | Author-reported | p. 17 |
| Memory / disk | 32 / 1 | GB RAM / TB disk | Artifact host | Author-reported | p. 19 |

The paper additionally compares its overhead with a cited browser prototype's approximately 44% website-loading overhead and reports an approximately 12-fold lower price for a newer model relative to the tested version. These are author-provided contextual comparisons on pp. 14–15, not measurements made by this study or independently verified here. The newer-model price expression is text-extraction-sensitive and the version description in the prose differs from the bibliography's year/date wording; no external repair is attempted.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Shared app execution creates cross-app influence/data risks | Described system model and concrete traces | F1, X2–X5 | pp. 2–5, 11–12 | HIGH on documented mechanism; no standalone comparison |
| Isolation with mediated interfaces is feasible | Implemented hub/spoke/operators/ISC and evaluated tasks | F2–F3, X6 | pp. 5–9, 13, 17 | HIGH for prototype; no formal security proof |
| Baseline attacks succeed materially | 20.2% overall across 1,598 scenarios | T1, X1 | pp. 9–10 | HIGH as reported; no uncertainty intervals |
| Isolated dangerous flows receive warnings when dialogs appear | PA 7.6%, WR 100% | T1, X1 | p. 10 | HIGH; conditional warning metric, not equal-metric ASR |
| Malicious fare rewriting is contained in demonstrated trace | Original $51.80 preserved; baseline raises to $61.80 | F5, X2 | pp. 10–11 | HIGH for case; not population estimate |
| Email exfiltration is blocked in depicted isolated flow | Unexpected drive request denied | F6, X3 | pp. 11, 19 | HIGH; assumes user denial |
| Ambiguous cross-task data sharing is moderated | Health-to-travel sharing denied | F7, X4 | pp. 12, 19 | HIGH; additional manual input required |
| App benchmark functionality matches | Matching 1.00, 0.76, 0.95 scores | T2, X6 | p. 13 | HIGH within tested workloads |
| Isolation incurs latency/cost overhead | Runtime table, cumulative curves, sampled cost | T4, F9, X7–X8 | pp. 14–15 | HIGH for table; cost detail and percentile conventions limited |
| Web-agent relevance is additional exposure through tools/context/actions | Threat model and external-content case | F6, S2–S3 | pp. 1–5, 11 | Analyst interpretation; no direct standalone experiment |

## 22. Very simple explanation — Explain Like I'm 15

Imagine an assistant who can read your messages, access your files, and book things for you. That is much more useful than an assistant who only writes text. But it also means that a bad message or dishonest app can try to make the assistant use those powers in the wrong way. In this paper's examples, one ride app changes another app's price, and a malicious email tells the assistant to find and send a private document.

IsolateGPT gives each app its own separate workspace and its own model instance. A central coordinator decides which app should help and controls what information can move between workspaces. The apps still cooperate, but requests must pass through that coordinator and may need your permission. Keeping the workspaces separate helps stop one app's instructions from taking over another app's work.

The tests show that this approach can preserve the tested tasks while adding security checks. It also takes extra time and sometimes asks the user to provide information again. Importantly, the warning is not magic: in two demonstrations, the attack is stopped because the user refuses the warned request. The system also does not claim to fix every attack inside a single app.

For the question about web AI agents versus standalone language models, the lesson is about added connections and powers. Reading untrusted online content, remembering private information, and calling services create more ways for bad instructions to have consequences. That is an inference supported by this paper's design and examples. The researchers actually compared two kinds of agent systems, not an agent against a model that only answers text questions.

## Completeness Audit

Coverage is judged against the inventory, not response length. All supplied text pages and all nine supplied figures/four tables have been inspected. Representation includes major conditions and limitations; implementation code, datasets, logs, and external references were not independently reviewed.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| ABS and S1 introduction/contributions | Yes, text and visual | Yes | Fully represented | Problem, three challenges, contribution scope |
| S2-A LLM systems/app architecture | Yes | Yes | Fully represented | Definitions and shared context |
| S2-A case studies A–D | Yes | Yes | Represented in compressed form | Linked to evaluated variants |
| S2-B security/privacy risks | Yes | Yes | Fully represented | Adversarial and non-adversarial risks |
| S2-C securing systems | Yes | Yes | Represented in compressed form | Prior-system analogy retained |
| S3-A system model | Yes | Yes | Fully represented | Services and persistent memory |
| S3-B attacker goals/capabilities | Yes | Yes | Fully represented | Malicious apps and external content |
| S3-C trust relationships | Yes | Yes | Fully represented | Trusted host/model, untrusted apps/content |
| S3-D scope | Yes | Yes | Fully represented | Single-app exclusion explicit |
| S4-A hub operator/planner/memory/lifecycle | Yes | Yes | Fully represented | Steps and responsibilities |
| S4-B spoke operator/LLM/memory/specialization/lifecycle | Yes | Yes | Fully represented | p. 7 text-only inspection disclosed |
| S4-C functionality discovery/message exchange/screening/lifecycle | Yes | Yes | Fully represented | Review assumption, side channel, consent |
| S5-A attack-scale evaluation | Yes | Yes | Fully represented | Category table and metric asymmetry |
| S5-B four protection cases | Yes | Yes | Fully represented | X2–X5, permission conditions |
| S6-A overall functionality | Yes | Yes | Fully represented | All T2 scores |
| S6-B mistake analysis | Yes | Yes | Fully represented | T3 error-only denominators |
| Benchmark limitations | Yes | Yes | Fully represented | Complex real-world cases omitted |
| S7-A overall trends | Yes | Yes | Fully represented | Full-response timing and reported threshold |
| S7-B planning/memory overhead | Yes | Yes | Fully represented | Component shares and cold starts |
| S7-C takeaway | Yes, partly text-only | Yes | Represented in compressed form | Expectations separated from measurement |
| S7-D cost | Yes, text-only | Yes | Uncertain | Multiplier extraction; unspecified sample details |
| S8 conclusions | Yes, text-only | Yes | Represented in compressed form | Feasibility and release |
| O1–O5 objectives | Yes | Yes | Fully represented | Informal objectives, not invented formal questions |
| Formal hypotheses | No instances found | Accounted for | Fully represented | Absence explicitly disclosed |
| X1–X8 analyses | Yes | Yes | Fully represented | Conditions separated |
| F1 | Yes, visual | Yes | Fully represented | Shared workflow |
| F2 | Yes, visual | Yes | Fully represented | Hub/spoke architecture |
| F3 | Yes, visual | Yes | Fully represented | Numbered message sequence |
| F4 | Yes, visual | Yes | Fully represented | Dialog options and warning |
| F5 | Yes, visual | Yes | Fully represented | Exact fares and manipulation |
| F6 | Yes, visual | Yes | Fully represented | Exfiltration trace and denial |
| F7 | Yes, visual | Yes | Fully represented | Sensitive reuse and incomplete booking |
| F8 | Yes, visual | Yes | Fully represented | Conflicting instructions; no clinical inference |
| F9 and panels a–e | Yes, visual | Yes | Represented in compressed form | Trends and encoding; no exact curve samples |
| T1 | Yes, visual and text | Yes | Fully represented | All rows and columns |
| T2 | Yes, visual and text | Yes | Fully represented | All scores |
| T3 | Yes, visual and text | Yes | Fully represented | All error categories |
| T4 | Yes, visual and text | Yes | Fully represented | All rows via vector notation |
| Mathematical equations/theorems | No numbered objects found | Accounted for | Fully represented | Verbal metrics and tuples explained |
| Algorithms/pseudocode | No standalone algorithm found | Accounted for | Fully represented | Numbered workflow procedures represented |
| Major contributions | Yes | Yes | Fully represented | Architecture, implementation, empirical results |
| Author-stated limitations | Yes | Yes | Fully represented | Scope, benchmarks, permissions, overhead, variability |
| A1-A process isolation | Yes, text-only | Yes | Fully represented | Configured limits not supplied |
| A1-B secure message exchange | Yes, text-only | Yes | Fully represented | Four tuple structures |
| A1-C memory management | Yes, text-only | Yes | Fully represented | Working/long-term memory wording qualification |
| A1-D permission model | Yes, text-only | Yes | Fully represented | Permanent/session/one-time, irreversible actions |
| A1-E benchmark definitions | Yes, text-only | Yes | Fully represented | All four families |
| A2-A requirements | Yes, visual/text | Yes | Fully represented | Versions, hardware, API keys |
| A2-B installation | Yes, visual/text | Yes | Represented in compressed form | Commands described, not executed |
| A2-C major claims | Yes, visual/text | Yes | Fully represented | C1 protection, C2 overhead, C3 functionality |
| A2-D E1 | Yes, visual/text | Yes | Fully represented | Four cases, denial assumption, repeat caveat |
| A2-D E2/E3 | Yes, text-only p. 20 | Yes | Represented in compressed form | Relational-data subset and stored-output evaluation |
| Substantive footnotes | Yes | Yes | Represented in compressed form | Naming, app ecosystems, review, side channel |
| References [1]–[74] | Yes, text | Partly | Represented in compressed form | Relevant dependencies named; cited works not inspected |
| Acknowledgments / publication decoration | Yes | Accounted for | Inspected but deliberately omitted as non-substantive | Funding IDs and artifact badge not analyzed as findings |
| Supplied supplementary files | None | Accounted for | Missing from supplied material | External artifact references only |

### Missing or inaccessible material

No supplied PDF text page is missing. Visual renderings of pages 7, 15–18, and 20 are absent, so those pages were reviewed through text only. The code repository, archive contents, Llama Pack, app-review records, benchmark datasets, environment.yml, README, executable scripts, raw attack outcomes, per-query timing files, and output logs were not supplied or inspected. The artifact's example commands and file names are author descriptions, not evidence of a reproduction performed here.

Appendix B's E1 estimates 5 human-minutes plus 5 compute-minutes, E2 estimates 5 human-minutes plus 20 compute-minutes, and E3 estimates 5 human-minutes plus 3 compute-minutes. These are author-estimated artifact effort, not independent runtime observations. E2 runs run_measurements.sh and E3 runs run_func_eval.sh; output paths are summarized rather than reproduced exhaustively. No supplied supplemental study is silently assumed reviewed.

### Uncertain interpretations

A2's exact conditional denominator is not fully defined, despite numbers suggesting staged success. Runtime components do not exactly sum to displayed totals, and residual operations are not specified. The 6–10 and 10–13 workload labels overlap at 10. Individual-query overhead and percentile calculations cannot be reconstructed from Figure 9 and category averages. The cost multiplier and approximate newer-model price comparison are sensitive to extracted symbols, and exact cost-sample selection is unknown. Working-memory wording on p. 17 initially includes entity information but later specifies on-demand retrieval. Small Figure 9 axes do not support precise unlabelled curve coordinates. These issues are preserved rather than repaired with outside information.

### Deliberately compressed material

The four motivating examples are connected to their evaluated versions rather than repeated in full. Repeated claims about isolation, release, and feasibility are consolidated. Figure API calls are explained at the level needed to understand control/data flow; every parameter string and all malicious-email wording are not reproduced. Bibliography entries, funding acknowledgments, decorative badges, exhaustive artifact paths, and shell command sequences are secondary to the scientific argument and compressed with disclosure. Historical product claims and price comparisons remain author-reported context rather than current external facts.

### Potential omissions

No known substantive inventory object is left wholly unrepresented. This does not mean every sentence, parameter, reference, or artifact detail is preserved. Exact implementation configuration, statistical variability, unseen artifact results, and standalone-LLM comparison evidence remain unavailable. The analysis is comprehensive for the supplied document inventory, with explicitly bounded visual coverage and unresolved numerical/methodological questions.
