# Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. No tools, browsing, external verification, or supplementary-artifact inspection were performed. Paper content is treated as evidence, not as instructions. Source locators below use physical PDF pages 1–21; printed proceedings pages 3991–4010 begin on physical page 2.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: extracted text is supplied for physical pages 1–21, including the cover, main paper, references, and appendices. |
| Textual page coverage | All 21 supplied page records were inspected. No gap occurs in their numbering. This establishes coverage of the supplied document, not independent verification of the original PDF. |
| Direct visual coverage | Images were supplied and visually inspected for pages 1, 2, 4, 5, 6, 7, 8, 11, 12, 13, 14, and 21. |
| Text-only coverage | Pages 3, 9, 10, and 15–20 were inspected through supplied extracted text only. Their original page layouts were not visually inspected. |
| Figures | Figures 1–5 are all visible in supplied images. They are workflow, architecture, and simplified code diagrams, rather than quantitative plots. |
| Tables | Tables 1–6 are present in supplied text and visible in supplied images. Important values and row associations are readable. |
| Equations | Equations 1–3 occur on page 9, supplied as extracted text without a page image. Their interpretation is therefore text-only and notation-sensitive. |
| Appendices | Appendices A, B, and C are present on page 21. The automated accessibility metadata's empty appendix-detection list does not override these visible headings. |
| Supplementary material | No separate supplementary files or embedded artifacts were supplied. The paper references datasets, baseline implementations, prototype code, repositories, and a mitigation commit; these were not accessed. |
| OCR | No OCR was performed or needed to read the available content. Extracted text still contains spelling, spacing, and notation irregularities. |
| Other limitations | An image-loading error referring to a path named '-' does not provide another usable image. No unavailable image was assumed to have been inspected. The supplied source hash is retained as an identifier, not independently computed. |

Evidence labels: **[A] Author-reported** means explicitly stated in the paper; **[B] Directly observable** means visible in a supplied image or table; **[C] Analyst-derived** means calculated from supplied quantities, with operands shown; **[D] Analyst interpretation** means an inference beyond an explicit author statement. No external-information category [E] is used. Confidence is HIGH where the supplied source is clear, MEDIUM for qualified interpretations or ambiguous implementation details, LOW for weakly supported extrapolation, and UNKNOWN for inaccessible information. Confidence describes support in this document, not independent confirmation of the research.

The analysis is a security and computer-systems reading, emphasizing the threat model, resource lifecycle, testing architecture, benchmark construction, experimental conditions, and limits on causal or comparative conclusions.

# 1. Plain-language orientation

**[A]** The paper studies how large language model (LLM) agents can become unavailable when ordinary-looking requests make their surrounding software consume too much memory or disk space. An agent can interpret a request, select a tool, download a document, parse it, and retain results for later conversation. These actions allocate real resources outside the language model itself. If allocations are too large or retained too long, the agent server can run out of resources and stop responding. This is a denial-of-service (DoS) vulnerability: an availability failure rather than necessarily a data theft or unauthorized-command attack. Sources: pp. 2–5, §§1–2.

The researchers identify three resource lifetimes: resources released after one interaction, resources retained until a chat session ends, and resources retained across sessions. They then build **AgentDoS**, a testing system that reads agent source code, identifies potentially dangerous operations, determines how long their resources persist, and uses an LLM to generate and refine natural-language test requests. It measures execution and resource consumption to choose more promising requests. Sources: pp. 3, 6–10.

**[A]** In a study of 20 open-source agents exposed as web services, AgentDoS found 36 previously undisclosed vulnerabilities affecting 16 applications. Fifteen Common Vulnerabilities and Exposures (CVE) identifiers had been assigned at the paper's reporting time. On a constructed benchmark of 38 verified vulnerabilities, it found 36, compared with 3 for an adapted AgentFuzz baseline. The resulting reported precision and recall were 100% and 94.7%. These figures are bounded by the authors' benchmark construction, deployment resources, testing time limits, and manual verification procedures; they do not establish all possible vulnerabilities in all agents. Sources: pp. 11–13.

**[D] Research relevance:** For the question 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?', the paper supplies a mechanism-based explanation: agents add tool execution, retained application state, downloaded artifacts, and resource-management decisions to language generation. Those additions create availability risks in the application layer. The paper does **not** conduct a controlled experiment comparing standalone LLMs with web agents, so it cannot establish a general numerical increase in vulnerability. Its central contribution is a lifecycle-aware detection method and empirical evidence of agent implementation weaknesses, not a universal ranking of agent and LLM security.

# 2. Document roadmap

The supplied inventory contains the following substantive structure. Original numbering is preserved so the explanation can be traced back to the source.

| Inventory ID | Original component | Physical pages | Role |
|---|---|---:|---|
| FRONT | Cover and title/author block | 1–2 | Identifies the paper and proceedings. |
| ABS | Abstract | 2 | States the problem, taxonomy, method, and headline findings. |
| S1 | §1 Introduction | 2–3 | Motivates resource-governance risks, identifies challenges, and lists contributions. |
| S2 | §2 Problem Statement | 3–5 | Establishes agent background, example, root causes, and threat model. |
| SS2.1 | §2.1 Background | 3–4 | Defines agent workflow and three resource lifecycles. |
| SS2.2 | §2.2 Motivation Example | 4–5 | Explains persistent downloaded files and previous detector limitations. |
| SS2.3 | §2.3 Problem Understanding | 5 | Attributes problems to retention and incomplete size limits. |
| SS2.4 | §2.4 Threat Model | 5 | Defines remote prompt-based attackers and benign deployments. |
| S3 | §3 Overall Ideas | 5–7 | Connects lifecycle analysis and semantic prompt generation. |
| SS3.1 | §3.1 Challenges & Key Insights | 5–6 | Explains why source logic and prompt semantics matter. |
| SS3.2 | §3.2 Approach Overview | 6–7 | Introduces operator modeling and dynamic fuzzing. |
| S4 | §4 AgentDoS Design | 7–10 | Gives the detailed detection method. |
| SS4.1 | §4.1 Vulnerable Operator Modeling | 7–8 | Locates, classifies, and filters resource-consuming operations. |
| SS4.1.1–3 | Candidate locating; lifecycle identifying; exploitability assessing | 7–8 | Defines static-analysis procedures and manual fallback. |
| SS4.2 | §4.2 Dynamic Fuzzing | 8–10 | Generates, scores, selects, and mutates prompts. |
| SS4.2.1–3 | Seed generation; scheduling; mutation | 8–10 | Contains Prompt 1–4 and Equations 1–3. |
| S5 | §5 Implementation | 10–11 | Reports CodeQL/Python implementation and instrumentation. |
| S6 | §6 Evaluation | 11–13 | Defines four research questions and experimental conditions. |
| SS6.1 | §6.1 Experimental Setup | 11 | Describes application selection and deployment. |
| SS6.2–5 | RQ1 purposes; RQ2 performance; RQ3 comparison; RQ4 ablation | 11–13 | Reports distinct analyses and results. |
| S7 | §7 Case Study | 13–14 | Explains short-lived and long-lived memory exhaustion. |
| S8 | §8 Related Work | 14 | Distinguishes agent, LLM-inference, and traditional DoS research. |
| S9 | §9 Discussion | 14–15 | Discusses stealth, resource-management tradeoffs, mitigation, and limitations. |
| S10 | §10 Conclusion | 15 | Restates the contribution and findings. |
| ETH | Ethical Considerations | 15–16 | Discusses disclosure, stakeholders, local testing, dual use, and access controls. |
| OPEN | Open Science | 16 | States artifact-release and conditional-access plans. |
| REF | References [1]–[86] | 16–20 | Supplies cited literature and artifact identifiers; citations were not externally validated. |
| A1–A3 | Appendices A Sink List, B Case Study, C Assigned CVEs | 21 | Supplies sink coverage, simplified case diagrams, and vulnerability classification. |

The paper title is **Autonomy Comes with Costs: Detecting Denial-of-Service Vulnerabilities Caused by Resource Abusing in LLM-based Agents**. Authors are Jiaqi Luo, Jiarun Dai, Fengyu Liu, Songyang Peng, Youkun Shi, Tong Bu, Geng Hong, Xudong Pan, and Yuan Zhang. Fudan University is the primary affiliation; Xudong Pan also has the Shanghai Innovation Institute affiliation. The supplied cover identifies the 35th USENIX Security Symposium, August 12–14, 2026, Baltimore, Maryland, USA. No keywords block is supplied.

# 3. Background and context

**[A] Agent versus model.** The paper describes an LLM as interpreting natural-language instructions and an agent as integrating that interpretation with external components, such as browsing or download tools. In Figure 1, the agent augments the user request with a system prompt describing available tools, obtains an LLM response, parses the planned action, executes the selected component, and returns an outcome. The agent's software therefore manages resources used by those actions. Source: p. 4, §2.1, Figure 1.

**[A] Resource lifecycle.** A lifecycle specifies when allocated resources are released. A short-lived resource lasts for one interaction; a long-lived resource lasts for a session; a full-lifecycle resource is not released through the modeled interaction/session cleanup. The distinction determines whether exhaustion must occur in one request or can accumulate over many requests. Garbage collection (GC) is the automatic reclamation mechanism invoked in the paper's memory examples; explicit deletion is relevant to disk artifacts. Sources: pp. 4, 7–8.

**[A] Fuzzing.** Here, fuzzing means generating and repeatedly changing test inputs until a vulnerability is exposed. A seed is an initial or retained candidate prompt. A sink is a selected resource-consuming operation or its callsite in source code. A call chain lists calls leading to that operation. A control-flow graph (CFG) describes possible execution paths. Taint analysis tracks whether inputs can influence a target operation. AgentDoS uses these structures to direct testing toward likely resource-abuse sites rather than generating arbitrary requests. Sources: pp. 3, 6–10.

**[A] Grey-box testing.** AgentDoS combines source-level analysis and execution feedback. It is not a prompt-only test of an opaque service: its detector needs source code and instrumentation. The attacker modeled in the paper, however, only needs ordinary remote interaction. Detector privileges and attacker privileges must be kept separate. Sources: pp. 5, 10, 15.

**[D] Beginner interpretation.** A language model can decide that a document should be fetched, but the agent's downloader, parser, history buffer, and cleanup code determine what that decision costs and what remains afterward. This paper's security problem is at that boundary between a plausible request and its real software consequences. It does not require assuming that the model is malicious or that all agent failures originate in prompt injection.

# 4. Research problem and gap

**Existing problem [A]:** Agents can autonomously perform resource-intensive work while lacking comprehensive resource governance. Large allocations can exhaust a server immediately; retained data can exhaust it gradually. The motivating example is a download capability intended for legitimate activities such as literature review, where downloaded files remain after sessions are recreated. Sources: pp. 2, 4–5.

**Root causes [A]:** The authors identify two: mismanaged resource lifecycles and missing or incomplete resource-size limits. Developers retain context or intermediate outputs because they cannot predict what later autonomous actions will need. A per-request timeout or per-session turn cap does not necessarily constrain total retained data. Conversely, strict caps can prevent legitimate tasks from finishing. Source: p. 5, §2.3.

**Shortcomings attributed to previous approaches [A]:** Many traditional DoS detectors focus on central processing unit (CPU) exhaustion. Memory-exhaustion or memory-leak tools generally do not generate semantically valid agent prompts or model the customized lifecycle logic of agents. AgentFuzz supplies functional prompt generation but is positioned as targeting taint-style vulnerabilities and lacking the resource-intensity and lifecycle modeling needed here. These are the paper's characterizations of prior work, not independently verified literature judgments. Sources: pp. 2, 5, 14.

**Research gap [A]:** A detector must solve two connected tasks: identify how a target resource is released and generate requests that both invoke the relevant component and impose enough load to exhaust that resource. Reaching a tool is insufficient if its workload remains small; repeating large requests is insufficient if cleanup resets the allocation after each turn. Sources: pp. 3, 6.

**Scope [A]:** The method primarily targets memory and disk resource exhaustion in open-source, Python-analyzable agent applications operated as web services. It does not present a comprehensive analysis of all security categories, CPU attacks, all programming languages, or commercial black-box agents. Sources: pp. 7, 10–11, 15.

# 5. Research questions, objectives, and hypotheses

The paper explicitly lists four evaluation questions on p. 11, §6.1:

1. **RQ1:** What are the purposes for which agents retain resources after a single chat?
2. **RQ2:** How effective and efficient is AgentDoS at detecting DoS vulnerabilities in real-world agents?
3. **RQ3:** How does AgentDoS perform in comparison to state-of-the-art approaches?
4. **RQ4:** What is the contribution of each component of AgentDoS to its overall performance?

The broader objectives are to characterize resource management, identify lifecycle-dependent exploitation mechanisms, and implement a detector that combines source analysis with semantic prompt refinement. Sources: pp. 2–3.

No formal statistical hypotheses, preregistered tests, or null/alternative hypothesis pairs are stated in the supplied work. The research question supplied for this review—why web AI agents might be more vulnerable than standalone LLMs—is an analytical framing external to the paper's own RQ1–RQ4, not an additional author-stated experiment.

# 6. Assumptions / Threat Model

**[A] Trusted conditions:** The agents and their developers are benign, and the execution environments have not been compromised. The adversary is remote and interacts under normal usage conditions, for example by sending prompts through a publicly accessible web interface. Specially crafted requests induce excessive memory or disk consumption, leading to DoS. Source: p. 5, §2.4.

The modeled attack does not require the adversary to modify agent source code or gain prior control of the deployment. Source access is a requirement of **AgentDoS as a testing tool**, explicitly discussed on p. 15, rather than a stated requirement of prompt-based exploitation. Likewise, instrumentation and resource monitoring are experimental/testing capabilities, not privileges silently granted to the remote attacker.

**[A] Lifecycle-dependent interaction:** A short-lived target must be exhausted within one interaction. A long-lived target can accumulate consumption within one session. A full-lifecycle target can retain data across newly created sessions. AgentDoS dispatches test requests accordingly. Sources: pp. 4, 7, 10.

**[A] Test environment:** All tested systems were downloaded open-source projects and deployed locally. The authors report no interaction with real-world systems or user data. Docker resource assignments deliberately emulate adverse deployment conditions by using stated minimum requirements or a fallback allocation. Sources: pp. 11, 15–16.

**[D] Boundary:** The supplied threat model does not quantify authentication requirements, rate limits, user quotas, concurrency, or production tenant isolation. Their absence from the description is not evidence that every real deployment lacks them. Similarly, the paper's discussion of third-party LLM-provider isolation is an author argument about the distinction between inference-layer and application-layer risks; it is not a verified guarantee about all providers. Source: p. 14, §8.

# 7. Methodology

## 7.1 Overall study design

The study combines implementation analysis, dynamic vulnerability testing, manual review, a constructed vulnerability benchmark, comparative testing, ablations, and illustrative case studies. Figure 3 divides AgentDoS into **Vulnerable Operator Modeling** and **Dynamic Fuzzing**, connected to an instrumented agent runtime and an availability oracle. Sources: pp. 6–13.

## 7.2 Candidate identification

AgentDoS locates predefined memory and disk sinks. Memory candidates include insertion into expandable containers, parsers that may consume large memory on deeply nested content, and network-fetch operations listed in Appendix A. Disk candidates include write operations. For class-member operations, the method traces to a caller to obtain context. It traverses backward from a sink to collect call paths and extracts the enclosing function as a code snippet. Rules attributed to LLMSmith address implicit calls in agent CFG extraction. Sources: p. 7, §4.1.1; p. 21, Table 5.

This step provides context useful to an LLM: class and method names indicate purpose, while code can reveal loops or large data operations. The chosen sink list bounds detector coverage. An operation outside that list is not shown to be systematically detected.

## 7.3 Lifecycle identification

Researchers manually identify APIs for single-turn chats and session deletion, then build forward CFGs. For memory, locally scoped variables are treated as short-lived; globally referenced variables reassigned during session deletion are treated as long-lived; other retained variables are treated as full-lifecycle. For disk, the method follows the written file path: deletion after the interaction means short-lived, deletion during session cleanup means long-lived, and no modeled deletion means full-lifecycle. Manual dynamic validation handles cases that static analysis cannot resolve, such as dynamic path construction. Sources: pp. 7–8, §4.1.2.

These are practical analysis rules, not a formal proof of resource reclamation for every possible program. The authors measure classification accuracy and acknowledge unresolved indirect calls as an error source. Source: p. 11, §6.2.

## 7.4 Exploitability filtering

The method checks whether user input can influence the operation and whether explicit size checks constrain it. It employs intra-procedural taint analysis for scalability. Short-lived parser operations are potential candidates if arguments propagate into them. Short-lived append operations are candidates when their surrounding loop count depends on user input. Retained memory operations are conservatively candidates whenever user input can reach them. Disk writes are candidates if function inputs affect written data. Backward analysis searches for size-related conditional checks restricting sink execution. Only records with **Controllable = True** and **Constraints = False** proceed. Source: p. 8, §4.1.3.

Table 1 records eight features: operator name, source location, resource type, lifecycle, associated snippet, call chain, controllability, and constraints. A retained candidate is potentially exploitable, not automatically a confirmed vulnerability.

## 7.5 Seed generation

AgentDoS captures the assembled system prompt dynamically by hooking the LLM invocation API. It sends a fixed 'hi' request and extracts the system-role field from invocation parameters. The authors state that the system prompt does not change with input and is extracted once per agent. The LLM receives that prompt and the extracted call chains. A one-shot example and stepwise reasoning instructions guide generation of a natural-language seed that matches the component's purpose. Prompt 1 illustrates a calculator request aligned with a calculator-to-append call chain. Sources: pp. 8–9, §4.2.1.

**[D] Qualification:** The once-per-agent extraction is an implementation assumption reported for this method. Its reliability for agents with input-dependent tools or system prompts is not tested in the supplied evaluation.

## 7.6 Feedback and scheduling

Each executed seed receives a functionality score based on CFG distance and an LLM semantic assessment, plus a resource score reflecting peak or residual resource usage. The semantic assessment evaluates clarity, conciseness, and alignment with target functionality. A final score combines functionality and resource consumption and subtracts the number of previous selections, discouraging repeated selection of the same seed. The highest-scoring seed is mutated next. Source: p. 9, §4.2.2, Equations 1–3.

For short-lived resources, the method measures peak usage during execution. For retained resources, the equation uses usage after prompt execution. The prose also refers to the completion of a 'single chat session'; that wording is ambiguous for long-lived resources whose accumulation requires keeping the session open. This ambiguity is retained rather than silently resolved.

## 7.7 Complementary mutation

The **Explorer** refines prompts until execution reaches the intended sink. It receives call chains, system prompts, prior prompts, execution traces, and functionality scores. The **Exploiter** then refines resource intensity using the relevant code and resource-consumption feedback. Each seed has its own mutation history, including prompts, reasoning, traces, and scores. The intent is to learn from prior unsuccessful and successful executions. Source: p. 10, §4.2.3.

The exploiter can refer to researcher-hosted files. The implementation describes deeply nested HTML and XML files of approximately 15 million layers and around 100 MB each, ten files of roughly 30 GB each, and one hundred smaller files of approximately 100 MB each. These are experimental workload resources, not descriptions of files an arbitrary real deployment necessarily permits. Source: p. 10, §5.

## 7.8 Execution and oracle

Short-lived and full-lifecycle targets receive prompts through new dialogue API instances; long-lived targets use a persistent session. Instrumentation records stack frames, execution proximity, and real-time resource usage. AgentDoS flags a potential vulnerability if the agent becomes unresponsive while a sink executes. For short-lived resources it outputs a final exploit prompt; for long-lived and full-lifecycle resources it outputs the dialogue sequence. Manual review then confirms reports. Sources: pp. 7, 10, 12.

The supplied work does not state a numerical response-time threshold defining 'unresponsive', a complete recovery protocol between tests, or an exhaustive diagnostic procedure separating all causes of unresponsiveness. These missing details limit reproduction of the oracle, without negating the reported manual confirmations.

## 7.9 Implementation and configuration

The prototype contains over 1.5 thousand lines of CodeQL and over 5.4 thousand lines of Python. CodeQL FunctionInvocation and BasicBlock APIs build call graphs; TaintTracking supports intra-procedural analysis. Results are exported in Static Analysis Results Interchange Format (SARIF) and parsed by Python. Python inspect supplies stack information and psutil monitors resources. Manual entry-point/startup identification and instrumentation are reported to take less than ten minutes per agent, once per agent. Sources: pp. 10–11.

Reported score parameters are k = 1, α = 0.5, and β = 0.5, selected after evaluation on a benchmark subset following prior work's settings. Both AgentDoS and tested agents use GPT-4.1 with temperature 0. Agents run in default configurations inside Docker; minimum specified resources are assigned. When unspecified, the fallback is 4 GB RAM, 10 GB disk, and a 64-core Intel CPU. AgentDoS runs separately on a machine with a 64-core Intel CPU and 256 GB RAM. Sources: pp. 10–11.

The paper reports no training/validation/test partition for applications, no numeric random seed, no repeated-run count, and no confidence intervals or hypothesis tests. Exact application revisions, complete dependency versions, and per-agent resource assignments are not enumerated in the supplied text.

# 8. Experiments / Analyses

## X1 — RQ1: lifecycle accuracy and retention purposes

**Purpose:** Understand why resources survive a single interaction and evaluate lifecycle classification. **Sample/setup:** All 20 applications undergo operator modeling. Researchers randomly sample 5% of sink callsites from each lifecycle stage and use Python weakref during execution to monitor lifetimes. They then inspect 148 retained-resource callsites from five well-known applications, spending approximately 12 person-hours. The five application identities and exact lifecycle-validation sample counts are not supplied. Source: pp. 11–12, §6.2.

**Results [A]:** 2,025 potential vulnerable operators: 1,566 short-lived, 286 long-lived, and 173 full-lifecycle, reported as 77.3%, 14.1%, and 8.6%. Lifecycle accuracy is 95.2%. Among analyzed long-lived resources, 27.4% store conversation context, 35.9% store session state or developer traces not subsequently sent to the LLM, and 36.7% initialize sessions. Among full-lifecycle resources, 37.9% are associated with downloaded files for later analysis and 62.1% serve developer operational purposes. Sources: Table 2 and §§6.2, pp. 11–12.

**Interpretation [A]:** Retention has functional purposes, including coherence and operations, while some retained data does not enter later LLM context. **Caveat [D]:** The percentages describe inspected callsite categories, not fractions of bytes, users, attacks, or all deployed agents. The supplied work does not give the separate denominators for the long-lived and full-lifecycle purpose percentages.

## X2 — RQ2: effectiveness, cost, and false-negative inspection

**Setup:** Each sink receives a 20-minute testing cap. Testing is abandoned if a sink has not been triggered during the preceding three minutes or if recent usage increase is below 20 MB: per-chat increase for short-lived resources, cumulative increase for the other lifecycles. All 20 applications are tested with manual instrumentation. Source: p. 12, §6.3.

**Results [A]:** 36 zero-day vulnerabilities, all manually reviewed as true positives; 16 affected applications and 15 assigned CVEs. Total fuzzing cost is 119.08 CPU hours, reported as 5.95 hours per application. Generation, scheduling, and mutation account for 17.1%, 14.2%, and 68.6% of runtime. Average LLM usage is 9.32 million tokens per agent, with an estimated $44.3 cost using August 2025 GPT-4.1 pricing. The wording suggests the cost follows the per-agent token average, but it is not a full cost-accounting table. Sources: pp. 3, 12, 15.

**False-negative analysis [A]:** The authors sample 103 unflagged sink callsites, described as 5%, and manually inspect code. Reported categories are 95.15% uncontrollable, 0.97% blocked by the model context-window limit, 1.94% impractical within feasible attack time due to input-size limits, and 1.94% genuinely vulnerable but missed. A RAGFlow example would reportedly require more than 24 hours because normal LLM outputs are approximately 2 KB. A missed SuperAGI example involves crafted filenames escaping a cleanup directory, allowing files to survive sessions. Source: p. 12.

**Caveat [D]:** Sampled inspection cannot establish that no other false negatives exist. The 20-minute cap and 20 MB early-stop rule define detection conditions and may exclude slow accumulation. Precision is measured on reported findings; recall is measured later against the constructed 38-case benchmark.

## X3 — RQ3: comparison with AgentFuzz

**Setup [A]:** The authors adapt AgentFuzz to use AgentDoS's potential sink locations and availability oracle while retaining its other components. The benchmark combines vulnerabilities detected by both tools with two discovered through false-negative review. It contains 38 verified vulnerabilities. AgentFuzz uses new sessions for prompts, so it cannot accumulate long-lived resources within a single session. Sources: pp. 12–13, §6.4.

**Results [A]:** AgentDoS: TP 36, FP 0, FN 2, precision 100%, recall 94.7%. AgentFuzz: TP 3, FP 0, FN 35, precision 100%, recall 7.9%. All three AgentFuzz findings overlap AgentDoS findings. Authors attribute five baseline misses to absent lifecycle modeling and the other 30 to insufficient resource-consumption scoring/mutation. Table 3, pp. 12–13.

**Caveat [D]:** This is an adapted baseline and a discovery-built benchmark, not an independent random sample with exhaustive ground truth. The reported improvement supports performance within this setup. It does not establish twelvefold superiority on every agent or every vulnerability category.

## X4 — RQ4: component ablation

**Setup [A]:** Three variants remove one component each: generation is replaced by predefined LLMSmith seeds, scheduling is replaced by random selection, and mutation is removed entirely. Other components remain. The same dataset and vulnerability-count metrics are used. Source: p. 13, §6.5.

**Results [A/B]:** Without generation: TP 31, FP 0, FN 7, recall 81.6%. Without scheduling: TP 25, FP 0, FN 13, recall 65.7%. Without mutation: TP 16, FP 0, FN 22, recall 42.1%. Full AgentDoS: TP 36, FP 0, FN 2, recall 94.7%. Every listed variant has 100% precision. Table 4, p. 13.

**Interpretation [A]:** Functional seeds help reach the sink, scheduling avoids wasting testing time on weak candidates, and mutation increases both target reachability and load. **Inconsistency:** Prose says the no-scheduling variant 'missed 9 vulnerabilities', whereas Table 4 gives FN 13. Nine is not the table's total misses; it is the detection reduction relative to full AgentDoS, 36 − 25. The source wording is not automatically corrected. The reported 65.7% recall is also not conventional one-decimal rounding of 25/38 × 100, which is approximately 65.789%. See §14.

## X5–X6 — case analyses

**X5 short-lived memory:** A local collection stores downloaded content repeatedly within one call and is reclaimed only after function termination. The depicted request repeats a file access 1,000 times in one chat. Eventual cleanup cannot prevent memory exhaustion before the call finishes. Sources: p. 13, §7; p. 21, Figure 4.

**X6 long-lived memory:** A history buffer stores user input, LLM plans, and tool outputs until session termination. Repeated database-result requests grow it within a session. Authors state that history is not sent to the model by default, so the model context limit does not cap that retained buffer. Sources: p. 14, §7; p. 21, Figure 5. The simplified code's zero-length slicing has an unresolved conflict with that prose, discussed below.

# 9. Results

The main supported result is the discovery of 36 confirmed vulnerabilities in this 20-application test corpus under the specified local deployments. That is distinct from the 2,025 potentially vulnerable operators found by static analysis: a candidate operator is not a proven exploit. Sources: pp. 11–12.

**[C] Affected-application fraction:** 16/20 × 100 = 80% of tested applications had at least one discovered vulnerability. This is a corpus fraction, not an estimate that 80% of all agents are vulnerable. Table 2 shows four applications with no discoveries: Quivr, Owl, Bisheng, and Taskweaver. A zero in that column means no vulnerability found by this study, not a proof of safety.

**[C] Detection comparisons:** 36/3 = 12 times as many vulnerabilities found by AgentDoS as AgentFuzz. Using exact counts, recall is 36/38 × 100 ≈ 94.7368% versus 3/38 × 100 ≈ 7.8947%. Their difference is 33/38 × 100 ≈ 86.8421 percentage points. Subtracting rounded displayed values gives 94.7 − 7.9 = 86.8 percentage points. This is not an 86.8% relative improvement. The exact count-based recall ratio is 12.

**[C] Ablation effects:** Relative to full AgentDoS, removing generation reduces discoveries by 36 − 31 = 5; removing scheduling by 36 − 25 = 11; removing mutation by 36 − 16 = 20. These reductions must not be confused with each variant's benchmark false negatives, which are 7, 13, and 22. Using displayed recall values, drops are 13.1, 29.0, and 52.6 percentage points, respectively.

**[A] Efficiency:** Mutation dominates reported runtime at 68.6%; its iterative interaction with both tested agents and the LLM is the authors' explanation. Runtime shares sum to 99.9%, consistent with independently rounded percentages. The CPU-hour total is not necessarily wall-clock elapsed time, and the supplied work does not provide enough accounting to equate them. Source: p. 12.

**[C] Appendix classification:** Counting Table 6's 36 rows gives 16 short-lived, 6 long-lived, and 14 full-lifecycle findings; by resource type, 17 concern memory and 19 disk. These are derived from the appendix rows, not the 1,566/286/173 candidate counts. Their sum checks are 16 + 6 + 14 = 36 and 17 + 19 = 36. Source: p. 21.

# 10. Figure-by-figure interpretation

## Figure 1 — Agent workflow and nested resource lifetimes

**Visual inspection:** p. 4. This is a schematic, with no axes, units, scale, or statistical uncertainty. A user supplies a download request to an agent application. The single-turn box shows system-prompt assembly, LLM interaction, and parsing/executing an action. The response returns to the user. A session box encloses multiple chats and long-lived resources; a larger application scope includes full-lifecycle resources. Short-lived resources sit within single-turn execution. The nested boundaries encode persistence, not relative resource quantities.

**Conclusion supported [A/B]:** Tool actions are executed by the surrounding agent, and different allocations survive different boundaries. The diagram makes clear why one-turn, same-session, and cross-session tests require different dispatch strategies. The workflow is explicitly simplified and should not be treated as a complete architecture for every tested agent.

## Figure 2 — Persistent downloads despite session limits

**Visual inspection:** p. 4; accompanying explanation p. 5. This is an annotated simplified code/attack-flow diagram. It shows available tools, a system prompt, a chat API, session memory and turn count, LLM-driven tool selection, download code, disk writing, and a new-session API. Numbered annotations identify user input, LLM response, tool invocation, and disk writing. The top arrow depicts 1,000 chats, each in a new session.

**Important values [A/B]:** The code checks chat count against 10 and uses a 30-second download timeout. The text estimates roughly 300 MB per download under that timeout; this is not a universal throughput calculation. The mechanism is that downloaded files persist even when session information is cleared. The figure's 1,000 repetitions illustrate a workload; no measured time-to-exhaustion is plotted.

**Caveat:** The nearby prose cites the timeout at line 23, while the displayed timeout is line 19. Lines 23–24 concern session creation/cleanup. This is a line-reference discrepancy; the timeout and retention mechanism remain readable. Simplified code also omits operational detail needed for a runnable reproduction.

## Figure 3 — AgentDoS architecture

**Visual inspection:** p. 6. Source code feeds Operator Modeling, which performs candidate location, lifecycle identification, and exploitability assessment. The prompt-input URL is also shown as an input. The Dynamic Fuzzing region contains seed generation, scheduling, mutation, and a seed pool. Seed generation receives call-chain and system-prompt context through an LLM. Scheduling uses execution traces and resource consumption. Mutation contains Explorer and Exploiter. Arrows link selected seeds, newly produced seeds, execution feedback, and the runtime environment.

The dashed Agent Runtime Environment contains instrumentation, Trace Recorder, and Resource Recorder; an Oracle leads to a vulnerability output. Boxes and arrow directions express stage membership and feedback, not timing measurements. **[A/B]** The diagram supports a closed testing loop in which execution informs future input selection. It does not itself specify the score formulas, early-stop thresholds, or oracle timeout; these are distributed across text.

## Figure 4 — Short-lived memory exhaustion before cleanup

**Visual inspection:** p. 21; interpretation p. 13. The diagram shows one chat requesting repeated access, paired with a function that initializes local all_docs, iterates URLs, fetches content, and extends the collection. A red marker highlights the retention operation. The displayed repetition count is 1,000; the arrow says single chat. There are no graph axes or memory measurements.

**[A/B]** The relevant contrast is temporal: memory can be reclaimed after the function ends, yet the function can run out of memory before reaching its end. The figure supports the short-lived mechanism and reported case confirmation, not a quantified rate of exploitation. The snippet is simplified, and the precise retrieved-object type is not specified sufficiently for independent execution.

## Figure 5 — Session history accumulation

**Visual inspection:** p. 21; explanation p. 14. A repeated request for database entries points to an agent. The code selects history, calls the LLM, executes a tool such as DBSearch, and appends input, response, and result to self.history. A red marker highlights the append. The diagram labels 1,000 repetitions, representing accumulation across conversation turns.

**[A]** The text says the buffer is cleared on session end and default history is not sent to the model, allowing growth without reaching the model's context ceiling. **Uncertainty:** The snippet shows self.history[-history_len:] with history_len defaulting to 0. Under the displayed slicing expression, negating zero leaves zero and a slice from index zero denotes the full sequence. This code-reading observation conflicts with the prose's no-history behavior unless omitted logic intervenes. The original implementation was not supplied or inspected, so the discrepancy remains unresolved. The caption also calls this an L** application while §7 calls the long-lived case L*.

All five substantive figures were visually inspected. The cover logos, sponsorship mark, publisher headers/footers, and artifact badge are accounted for as presentation/provenance features; they are not empirical measurements or independently validated artifact certifications.

# 11. Table-by-table interpretation

## Table 1 — Candidate operator record

Source: p. 8. Eight rows define stored features: Operator, Location, Type, Lifecycle, Snippet, Call Chain, Controllable, and Constraints. Type is Memory or Disk; Lifecycle uses the three categories; the last two fields are Boolean. This is a schema for analysis output rather than an experimental result. It explains which source evidence is passed downstream and why candidate filtering is not equivalent to vulnerability confirmation.

## Table 2 — Application corpus and candidate counts

Source: p. 11. Stars and lines of code (LoCs) use 'k' for thousands; these are paper-reported repository measures, not refreshed counts. CVEs/Vulns distinguishes assigned identifiers from discoveries. S/L/F counts refer to potential operator callsites, not confirmed vulnerabilities. Footnotes say CodeTabs supplied repository metrics and define the lifecycle categories.

| Application | Stars | LoCs | CVEs / vulnerabilities | S | L | F |
|---|---:|---:|---:|---:|---:|---:|
| AutoGPT | 176k | 81.5k | 7 / 7 | 26 | 0 | 4 |
| Dify | 104k | 140k | 0 / 1 | 259 | 7 | 4 |
| LangFlow | 81.4k | 96.6k | 0 / 4 | 123 | 49 | 2 |
| RagFlow | 60.1k | 75.1k | 0 / 2 | 235 | 40 | 5 |
| Autogen | 46.4k | 88.5k | 0 / 1 | 75 | 23 | 14 |
| Quivr | 38.1k | 6.1k | 0 / 0 | 11 | 1 | 2 |
| LangChatchat | 35.3k | 16.1k | 0 / 2 | 18 | 3 | 5 |
| Khoj | 30.4k | 35.8k | 0 / 1 | 52 | 3 | 0 |
| Kotaemon | 22.7k | 29.1k | 0 / 1 | 67 | 1 | 10 |
| GPT-Researcher | 22.1k | 12.5k | 0 / 3 | 30 | 7 | 9 |
| Owl | 17.2k | 15.2k | 0 / 0 | 25 | 0 | 6 |
| MaxKB | 16.9k | 42.8k | 0 / 1 | 80 | 15 | 7 |
| DB-GPT | 16.8k | 150.0k | 0 / 1 | 202 | 46 | 40 |
| SuperAGI | 16.4k | 27.7k | 3 / 3 | 48 | 17 | 4 |
| DeerFlow | 15.5k | 8.0k | 0 / 1 | 5 | 0 | 1 |
| Chuanhu | 15.4k | 10.0k | 0 / 1 | 18 | 18 | 3 |
| AgentZero | 10.6k | 15.2k | 0 / 1 | 21 | 13 | 9 |
| Bisheng | 9.0k | 144.3k | 0 / 0 | 217 | 23 | 27 |
| AgentScope | 7.5k | 53.4k | 5 / 6 | 24 | 17 | 9 |
| Taskweaver | 5.8k | 16.4k | 0 / 0 | 30 | 3 | 12 |
| Total | / | / | 15 / 36 | 1566 | 286 | 173 |

AutoGPT has the most findings, seven; AgentScope has six. Dify has the most short-lived candidates, 259; LangFlow the most long-lived candidates, 49; DB-GPT the most full-lifecycle candidates, 40. These extrema do not rank underlying security because candidate counts, code size, feature exposure, and detector coverage differ. The '/' entries mean no total is provided for stars or LoCs, not zero.

## Table 3 — Adapted baseline comparison

Source: p. 12, with setup on pp. 12–13. Rows compare AgentFuzz and AgentDoS; columns are true positives (TP), false positives (FP), false negatives (FN), precision, and recall. Values are 3/0/35/100%/7.9% versus 36/0/2/100%/94.7%. Both tie on observed precision; AgentDoS finds more cases. No error bars, intervals, statistical significance markers, or multiple-run dispersion appear. The denominator is the 38-case constructed benchmark, not all 2,025 candidates.

## Table 4 — Ablation outcomes

Source: p. 13. Rows remove generation, scheduling, or mutation and compare with full AgentDoS. Values are reproduced in §8. The strongest loss in detections occurs without mutation; all variants retain zero observed false positives. This table supports component usefulness under the same evaluation setup. It does not separately isolate Explorer versus Exploiter, each scoring term, or lifecycle modeling. The no-scheduling prose discrepancy and recall rounding discrepancy are preserved in §14.

## Table 5 — Sink coverage

Source: p. 21, Appendix A. Columns identify package, class, methods, and resource type. Memory rows include built-in list append/extend; set add/update; dictionary update; bs4 BeautifulSoup initialization; html5lib parsing; requests module and Session get/post/request; urllib3 PoolManager and module fetch methods; aiohttp ClientSession get/post/request; and httpx AsyncClient get/post/request. Disk rows include TextIOWrapper and aiofiles AsyncTextIOWrapper write/writelines.

The source prints 'buildins' and 'reqeust'; those spellings are noted rather than treated as verified executable API names. The list includes fetching operations as memory sinks as well as container/parser operations. No systematic coverage of all possible memory allocators or all languages is established. The table is a predefined modeling inventory, not measured vulnerability counts.

## Table 6 — Findings, lifecycle, resource, and CVE status

Source: p. 21, Appendix C. Each row is a discovered vulnerability. Masked CVE identifiers are retained as anonymized author reporting; 'Assigning' is not an already assigned identifier. The information can be compressed by application without losing lifecycle/resource counts:

| Application | Vulnerability classifications | Assigned CVE count |
|---|---|---:|
| AutoGPT | 6 short-lived disk; 1 short-lived memory | 7 |
| Dify | 1 full-lifecycle disk | 0 |
| Langflow | 3 short-lived memory; 1 full-lifecycle disk | 0 |
| Ragflow | 1 long-lived memory; 1 short-lived memory | 0 |
| Autogen | 1 short-lived memory | 0 |
| LangChatchat | 2 long-lived memory | 0 |
| Khoj | 1 short-lived memory | 0 |
| Kotaemon | 1 long-lived memory | 0 |
| GPT-Researcher | 3 full-lifecycle disk | 0 |
| MaxKB | 1 long-lived memory | 0 |
| DB-GPT | 1 full-lifecycle disk | 0 |
| SuperAGI | 3 full-lifecycle disk | 3 |
| DeerFlow | 1 full-lifecycle disk | 0 |
| Chuanhu | 1 short-lived memory | 0 |
| AgentZero | 1 short-lived memory | 0 |
| AgentScope | 2 short-lived memory; 4 full-lifecycle disk | 5 |

AutoGPT's masked identifiers are CVE-2025-3**36, 3**37, 3**23, 3**24, 3**22, 3**92, and 3**93. SuperAGI's are CVE-2025-4**99, 4**01, and 4**03. AgentScope's are CVE-2025-4**98, 4**90, 4**94, 4**26, and 4**32, with one further memory finding marked Assigning. The exact hidden digits cannot be recovered. Table 6 lists no uncertainty intervals or severity scores. The absence of four applications simply reflects their zero discovery counts in Table 2.

# 12. Diagram / Architecture Interpretation

The substantive diagrams are Figures 1–5; their individual contents are covered above. Their combined methodological meaning is a sequence of three mappings:

1. **Request to action:** Figure 1 maps a natural-language request through system-prompt assembly and LLM planning to actual tool execution.
2. **Action to retained allocation:** Figures 2, 4, and 5 map downloads or tool results to disk artifacts or memory collections, with different cleanup boundaries.
3. **Testing feedback to new requests:** Figure 3 maps source-derived candidate information and measured execution/resource feedback to seed generation, scheduling, and mutation.

**[D]** The important feedback loop is not merely 'generate a stronger prompt'. It distinguishes failure to reach a tool from failure to impose enough resource load after reaching it. Explorer addresses the first; Exploiter addresses the second. Lifecycle classification determines whether the next request should preserve a session or create a new one. The oracle observes service availability, while manual review supports the final vulnerability claim. These are different responsibilities and evidence sources.

There are no additional quantitative architecture panels or graphs. The diagrams provide illustrative control/data flow rather than latency, throughput, memory trajectories, or scalability measurements.

# 13. Equations and mathematical concepts

All three numbered equations are on physical p. 9 and were inspected through extracted text only. No theorem, lemma, proposition, formal proof, or numbered pseudocode algorithm is supplied.

## Equation 1 — Functionality score

The extracted formula is **Fs = x^(−k) + Ls**. Fs is the functionality score; x is the shortest CFG distance from the observed execution trace to the target sink; k weights that distance contribution; Ls is the LLM semantic score. The reported default k is 1. Smaller positive distances produce a larger reciprocal-distance contribution, while a larger semantic score also increases priority. The equation is a heuristic scheduling component, not a probability or calibrated success estimate.

The semantic score sums ratings across three dimensions. The prose says each ranges from 0 to 5, whereas Prompt 2 instructs 1 to 5. **[C]** The possible sums therefore differ: 0–15 under the prose versus 3–15 under the prompt. Prompt 2 calls the third dimension Relevance, while prose calls it functional consistency; these appear closely related but are not silently declared identical scoring implementations.

**Unresolved notation/implementation issue:** x = 0 would make x^(−1) undefined. The supplied work does not specify clipping, adding an offset, or another convention for an execution that reaches the sink. No such repair is invented here.

## Equation 2 — Resource-consumption score

For short-lived resources, **Rs = ((mm − mi) / mt) × 100**. Otherwise, **Rs = ((me − mi) / mt) × 100**. Here mm is maximum resource usage during the request, mi is initial usage, me is usage after prompt execution, and mt is total system resources of the relevant type. For a memory operator, memory is monitored; for a disk operator, disk usage is monitored.

The short-lived branch measures peak additional consumption; the retained branch measures what remains afterward. Subtraction removes the pre-request baseline, division normalizes by capacity, and multiplication by 100 expresses a percentage-scaled score. Units must be compatible within a calculation; memory and disk are not added into one physical amount. The score is not a classification probability. Behavior for negative deltas, sampling intervals, or capacity-denominator changes is not specified.

The prose's phrase 'after the completion of a single chat session' sits uneasily with measuring retained long-lived resources: terminating their session should release them by definition. The formula's definition of me instead says after a prompt. This is a terminology/measurement ambiguity, not proof that the implementation terminates the session before measurement.

## Equation 3 — Seed-selection score

**Ss = αFs + βRs − N**. Ss is final selection score, α and β weight functionality and resource consumption, and N counts how often the seed has already been selected. The reported defaults are α = β = 0.5. AgentDoS selects the seed with the greatest score.

The subtraction penalizes repeatedly selected seeds, supporting exploration. Equal coefficients do not establish equal empirical influence because Fs and Rs have different ranges. The supplied work does not give normalization beyond Equation 2, tie-breaking rules, a sensitivity analysis, or an optimality proof. The authors explicitly describe the parameters as tunable and identify further exploration as future work. Source: p. 10, §5.

Precision and recall are used as experimental metrics rather than numbered method equations. **[C]** The table counts permit reproduction as precision = TP/(TP + FP) and recall = TP/(TP + FN): 36/(36 + 0) = 100%; 36/(36 + 2) ≈ 94.7%. These count-based calculations explain the displayed results without claiming a formal statistical guarantee.

# 14. Interpretation and discussion

**RQ1:** Retained resources support conversation context, session operation, initialization, file analysis, and logging. Some retained state never enters subsequent LLM prompts. This matters because limiting model context is not necessarily a limit on application memory or stored artifacts. Sources: pp. 11–12.

**RQ2:** The detector found 36 manually confirmed cases, but it requires substantial testing and token expenditure and misses some sophisticated cleanup bypasses. Its 100% observed precision is a property of reviewed reports; its 94.7% recall is a property of the constructed benchmark. Source: p. 12.

**RQ3:** Lifecycle modeling and resource-focused mutations address different baseline failure modes. Issuing new-session requests cannot accumulate session-bound memory. Reaching a sink without imposing enough workload cannot demonstrate resource exhaustion. The five-versus-thirty baseline miss attribution supports this conceptual division, though it is author analysis rather than a factorial causal experiment. Source: p. 13.

**RQ4:** All three removed modules reduce detections, with the largest reduction when mutation is absent. The ablations support the combined design under the time cap, while not identifying every component interaction or the separate value of the two mutators. Source: p. 13.

**[A] Stealth and re-delegation:** Resource abuse may resemble legitimate file processing and need no overtly malicious action. An attacker can also bring usage near a limit so that a subsequent benign request triggers the visible failure. This latter scenario is discussed conceptually, not measured as a separate experiment with quantified detection difficulty. Source: p. 14, §9.

**[D] Relevance to standalone LLMs:** The strongest source-grounded answer is that agents introduce additional application-level allocation and persistence paths, with risks shaped by tool semantics and cleanup logic. The authors contrast this with inference-latency attacks on LLMs and argue that third-party providers often isolate model resources. The paper does not measure a standalone LLM comparator, does not test provider isolation, and does not show that all web agents are less secure than every standalone model. Source: p. 14, §8.

The consistency audit identifies these unresolved issues:

| Issue | Source evidence | Assessment |
|---|---|---|
| No-scheduling false negatives | Table 4: FN 13; §6.5 prose: missed 9 | Contradictory as total misses. Nine may reflect comparison to generation variant or a drafting error, but intent is unknown. Full-method detection loss is 11. |
| No-scheduling recall | Table 4: 25 TP, 13 FN, recall 65.7% | 25/38 × 100 ≈ 65.789%, normally 65.8% to one decimal. Preserve reported 65.7%. |
| Semantic-rating lower bound | p. 9 prose: 0–5; Prompt 2: 1–5 | Scoring-range discrepancy; actual implementation unknown. |
| Zero-distance scoring | Equation 1 with k = 1 | x = 0 needs an unspecified convention. |
| Residual-usage timing | p. 9 session-completion prose versus me after prompt execution | Relevant ambiguity for long-lived resource measurements. |
| Default history behavior | p. 14: history not sent; p. 21: slice with default zero | Simplified code conflicts with prose under the displayed expression; omitted logic might matter. |
| Download-timeout line reference | p. 5 cites line 23; Figure 2 shows timeout line 19 | Incorrect line reference, not an unreadable timeout. |
| Anonymization scope | pp. 15–16 claim affected applications fully anonymized; Tables 2/6 name projects | Named application-level results remain visible; selected examples and CVE digits are masked. |
| Long-lived case name | §7 uses L*; Figure 5 caption uses L** | Anonymized identifier mismatch; identity is not inferred. |

Seventeen of the twenty selected applications exceed 10,000 stars, whereas fifteen of the sixteen affected applications exceed that threshold. These are different denominators, not an inconsistency. The detected vulnerability count, application count, and CVE count also refer to different units and should not be conflated.

# 15. Contributions and novelty

**Conceptual [A]:** A three-part resource-lifecycle taxonomy ties cleanup timing to attack strategy and exposes why agent retention requires security analysis.

**Methodological/system [A]:** AgentDoS combines static sink identification, lifecycle classification, exploitability filtering, semantic seed generation, feedback-based scheduling, and complementary mutations. It selects session dispatch according to lifecycle and emits prompts or dialogue sequences as evidence.

**Implementation [A]:** The authors provide a CodeQL/Python prototype with source and runtime instrumentation, while access to its source is conditional according to their release statement.

**Empirical [A]:** The study reports 2,025 potential operator sites, 95.2% measured lifecycle accuracy, 36 confirmed vulnerabilities in 16 applications, and 15 assigned CVEs. A 38-case constructed benchmark and ablation results support detector comparisons within the studied setup.

**Novelty qualification:** Claims of the 'first systematic security study' and a novel framework are author claims. Closed-document analysis cannot independently establish priority across all prior literature. No theoretical novelty, new trained foundation model, or broadly representative vulnerability-prevalence estimate is established by the supplied evidence.

# 16. Limitations

## Authors' stated limitations

- **Source access:** AgentDoS cannot directly test black-box commercial agents. The authors suggest adapting resource-guided fuzzing when side-channel feedback is available. Source: p. 15, §9.
- **Static-analysis uncertainty:** Dynamic path construction can prevent automatic lifecycle classification, requiring manual dynamic validation; unresolved indirect calls cause classification errors. Sources: pp. 8, 11.
- **Unknown ground truth:** There is no public exhaustive vulnerability ground truth; false-negative analysis samples unflagged sites, and the benchmark is assembled from discoveries plus two manually found misses. Sources: pp. 12–13.
- **Observed misses:** More sophisticated payloads can bypass safeguards that AgentDoS does not overcome, illustrated by persistence through a path/cleanup boundary. Source: p. 12.
- **Testing feasibility:** Some small-output accumulation would take over 24 hours, beyond the 20-minute per-site window. Source: p. 12.
- **Parameter choice:** Hyperparameters are tunable and warrant further exploration. Source: p. 10.

## Additional evidence-based analyst observations [D]

The corpus is selected for popularity, recent maintenance, open-source availability, and web-service operation. It is not a random sample of agents. Only one base-model configuration is evaluated, and minimum-resource deployments deliberately favor adverse conditions. Exact revisions, run repetitions, oracle timing, resource-reset procedures, and complete model-cost accounting are not supplied. The external-file workloads are researcher-created and large relative to fallback resources; they demonstrate consequences when tools accept such inputs, not how frequently production users encounter them. Candidate filtering and fixed sink coverage may omit other allocation pathways. Several source/code/numeric inconsistencies remain unresolved. These observations are not presented as admissions by the authors.

# 17. Threats to validity

The following labels are **analyst methodological classifications [D]**, not a formal threats-to-validity section in the paper.

**Internal validity:** Instrumentation, source heuristics, and the unresponsiveness oracle may affect or incompletely characterize behavior. Manual confirmation improves confidence in reported cases, but no precise oracle timeout or full isolation/reset protocol is given. Benchmark-subset parameter selection is reported without its full selection procedure, so its influence on comparative outcomes cannot be quantified.

**Construct validity:** Unresponsiveness is an availability outcome, not a complete diagnostic description of resource exhaustion. The method measures memory/disk rather than every resource category. LLM semantic ratings are heuristic, and their rating-range discrepancy limits exact interpretation. Potential candidate counts should not be interpreted as verified vulnerabilities.

**External and ecological validity:** Findings apply most directly to these selected open-source web agents under local default configurations, GPT-4.1, and minimum/fallback resources. Production quotas, deployment changes, other models, rate limits, and isolation may alter outcomes. The paper's attacker capabilities are realistic at the interface level, but production prevalence and attack success frequency are not measured.

**Statistical conclusion validity:** No confidence intervals, significance tests, repeated-run variation, or exhaustive false-negative enumeration are reported. A twelvefold count/recall ratio is descriptive for 38 known cases, not a population estimate. The sampled classification accuracy lacks a fully specified count denominator and uncertainty estimate in the supplied text.

**Reproducibility:** The paper describes implementation components and workload sizes, but artifact code, revisions, and detailed environment manifests were not supplied to this analysis. Conditional prototype access can constrain independent replication. Artifact links and an availability badge indicate author-provided provenance claims; they do not establish that the analyst reproduced results.

# 18. Future work and open questions

## A. Explicit author proposals

The authors propose further hyperparameter exploration; adaptation to black-box testing using resource-related feedback such as latency or side channels; and continued collaboration on advanced mitigations. They suggest setting limits according to use cases, deduplicating retained data, continuously monitoring usage, alerting on abnormal patterns, and temporarily suspending storage to permit intervention. Sources: pp. 10, 15–16.

**Reported mitigation example [A]:** AutoGPT reportedly adds a 100 MB limit per download, a 1 GB limit per execution directory, and automatic deletion after task completion. These measures address both allocation size and retention. Their effectiveness is asserted in discussion; the paper does not provide a separate controlled post-fix benchmark. Source: p. 15.

## B. Additional open questions [D]

How does detection change across base models, resource budgets, and session policies? How should quotas preserve legitimate long tasks while preventing aggregate abuse? Can lifecycle and cleanup guarantees be tested without source access? Which allocations remain outside the sink list? How often does slow accumulation evade the early-stop rules? How do concurrency and tenant isolation affect shared availability? Can an independent benchmark reduce discovery-related selection bias? What are the tradeoffs between deduplication, retention utility, and cleanup correctness? These questions follow from the reported scope; no answers are invented.

# 19. Terminology and notation glossary

| Term | Meaning in this work |
|---|---|
| LLM | Large language model: interprets or generates natural language and plans actions in the agent workflow. |
| Agent | Application combining LLM interpretation with tools, execution logic, and retained state. |
| DoS | Denial of service: requests cause degraded responsiveness or unavailable functionality. |
| Resource governance | Control of allocations, limits, retention, and cleanup. |
| Short-lived | Released after one interaction; exhaustion must occur before that cleanup. |
| Long-lived | Retained across turns and released at session termination. |
| Full-lifecycle | Retained beyond modeled session cleanup; may persist unless explicitly cleaned. |
| Seed | Candidate natural-language test prompt held for execution or mutation. |
| Sink/callsite | Resource-consuming operation and its occurrence in source code. |
| CFG | Control-flow graph: representation of execution paths. |
| Call chain | Sequence of calls leading toward a target operation. |
| Taint analysis | Tracks whether inputs can influence an operation. |
| Intra-procedural | Analysis within a procedure/function rather than unrestricted whole-program propagation. |
| Grey-box fuzzing | Testing guided by internal analysis and execution feedback. |
| Explorer/Exploiter | Mutators focused respectively on reaching the component and increasing resource load. |
| Oracle | Rule used to flag likely vulnerability outcomes, here availability during sink execution. |
| GC | Garbage collection, used in the paper's memory-release account. |
| API | Application programming interface, including chat/session and model invocation interfaces. |
| CVE | Common Vulnerabilities and Exposures identifier; assignment count differs from discovery count. |
| TP/FP/FN | True-positive, false-positive, and false-negative findings relative to the evaluation benchmark. |
| Precision/recall | Correct fraction of reports / detected fraction of benchmark vulnerabilities. |
| LoCs | Lines of code, reported for application repositories. |
| SARIF | Static Analysis Results Interchange Format used for exported analysis. |
| Fs, Ls | Functionality score and summed LLM semantic score. |
| x, k | CFG distance and exponent parameter in Equation 1. |
| Rs | Resource-consumption score, normalized against relevant capacity. |
| mm, mi, me, mt | Peak, initial, final, and total-capacity resource amounts. |
| Ss, α, β, N | Selection score, its two weights, and prior selection count. |
| CoT | Chain-of-Thought, the paper's term for stepwise reasoning guidance during prompting. |
| HTML/XML | Document formats used for deeply nested parsing workloads. |
| RCE/SQL injection | Remote code execution / database-query injection, discussed as different vulnerability categories. |
| ReDoS/AC | Regular-expression DoS / algorithmic-complexity vulnerabilities in related-work discussion. |

# 20. Key numerical results

All numbers retain their reported conditions. Approximate workloads are not relabeled as exact measurements.

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| Tested applications | 20 | applications | Open-source web-service corpus | Author-reported | p. 11, §6.1 |
| Selected apps above 10k stars | 17 | applications | Whole corpus | Author-reported | p. 11 |
| Affected applications | 16 | applications | At least one discovered issue | Author-reported | pp. 3, 15 |
| Affected apps above 10k stars | 15 | applications | Among affected applications | Author-reported | p. 15 |
| Discovered vulnerabilities | 36 | vulnerabilities | AgentDoS local evaluation | Author-reported | p. 12 |
| Assigned identifiers | 15 | CVEs | Reporting-time status | Author-reported | pp. 12, 21 |
| Potential operators | 2025 | callsites | Static modeling output | Author-reported | p. 11 |
| Candidate lifecycles | 1566 / 286 / 173 | callsites | Short / long / full | Visually readable | p. 11, T2 |
| Lifecycle distribution | 77.3 / 14.1 / 8.6 | percent | Candidate sites | Author-reported | p. 11 |
| Lifecycle accuracy | 95.2 | percent | Sampled dynamic validation | Author-reported | p. 11 |
| Validation sample rate | 5 | percent | Each lifecycle stage | Author-reported | p. 11 |
| Purpose-analysis scope | 148; 5; approximately 12 | sites; apps; person-hours | Retained-resource analysis | Author-reported | p. 11 |
| Long-lived purposes | 27.4 / 35.9 / 36.7 | percent | Context / state / initialization | Author-reported | pp. 11–12 |
| Full-lifecycle purposes | 37.9 / 62.1 | percent | Downloaded files / operations | Author-reported | p. 12 |
| Benchmark | 38 | verified vulnerabilities | Tool discoveries plus two sampled misses | Author-reported | p. 13 |
| AgentDoS TP / FP / FN | 36 / 0 / 2 | cases | Constructed benchmark | Visually readable | p. 12, T3 |
| AgentFuzz TP / FP / FN | 3 / 0 / 35 | cases | Adapted baseline | Visually readable | p. 12, T3 |
| AgentDoS precision / recall | 100 / 94.7 | percent | Constructed benchmark | Visually readable | p. 12, T3 |
| AgentFuzz precision / recall | 100 / 7.9 | percent | Constructed benchmark | Visually readable | p. 12, T3 |
| No-generation TP / recall | 31 / 81.6 | cases / percent | Ablation | Visually readable | p. 13, T4 |
| No-scheduling TP / recall | 25 / 65.7 | cases / percent | Reported table values | Visually readable | p. 13, T4 |
| No-mutation TP / recall | 16 / 42.1 | cases / percent | Ablation | Visually readable | p. 13, T4 |
| Testing cap | 20 | minutes per site | Dynamic fuzzing | Author-reported | p. 12 |
| Early-stop window / threshold | 3 / 20 | minutes / MB | Trigger and growth heuristics | Author-reported | p. 12 |
| Total / mean fuzzing cost | 119.08 / 5.95 | CPU hours / hours per agent | 20 applications | Author-reported | p. 12 |
| Runtime shares | 17.1 / 14.2 / 68.6 | percent | Generation / scheduling / mutation | Author-reported | p. 12 |
| Average LLM usage | 9.32 million | tokens per agent | GPT-4.1 evaluation | Author-reported | p. 12 |
| Estimated associated model cost | 44.3 | US dollars | August 2025 pricing basis | Author-reported | p. 12 |
| Unflagged sample | 103 | sites | Described as 5% | Author-reported | p. 12 |
| Sample categories | 95.15 / 0.97 / 1.94 / 1.94 | percent | Uncontrollable / context-bound / impractical / missed | Author-reported | p. 12 |
| Example slow accumulation | approximately 2; over 24 | KB/output; hours | RAGFlow discussion | Author-reported | p. 12 |
| Default fallback resources | 4 / 10 / 64 | GB RAM / GB disk / CPU cores | When requirements unspecified | Author-reported | p. 11 |
| Tester hardware | 64 / 256 | CPU cores / GB RAM | Separate AgentDoS machine | Author-reported | p. 11 |
| Model / temperature | GPT-4.1 / 0 | configuration | Both tester and targets | Author-reported | p. 11 |
| Score parameters | 1 / 0.5 / 0.5 | k / α / β | Default configuration | Author-reported | p. 10 |
| Nested-file workload | approximately 15 million / 100 | layers / MB each | HTML and XML | Author-reported | p. 10 |
| Large/small file sets | 10 × roughly 30 GB; 100 × approximately 100 MB | files and size | Hosted test resources | Author-reported | p. 10 |
| Prototype sizes | over 1.5k / over 5.4k | lines of code | CodeQL / Python | Author-reported | p. 10 |
| Manual setup | less than 10 | minutes per agent | Entry-point instrumentation | Author-reported | p. 11 |
| Figure 2 turn check / timeout | >10 / 30 | chats / seconds | Simplified example | Visually readable | p. 4 |
| Timeout-size estimate | approximately 300 | MB | Motivating example, not universal rate | Author-reported | p. 5 |
| Depicted repetitions | 1000 | requests/accesses | Illustrative Figures 2, 4, 5 | Visually readable | pp. 4, 21 |
| AutoGPT mitigation limits | 100 / 1 | MB per download / GB per directory | Reported fix | Author-reported | p. 15 |
| Affected corpus fraction | 16/20 × 100 = 80 | percent | Tested corpus only | Analyst-derived | T2, pp. 11, 15 |
| Detection ratio | 36/3 = 12 | ratio | AgentDoS / AgentFuzz | Analyst-derived | p. 12, T3 |
| Exact-count recall difference | 33/38 × 100 ≈ 86.8421 | percentage points | Constructed benchmark | Analyst-derived | p. 12, T3 |
| Findings by lifetime | 16 / 6 / 14 | cases | Short / long / full | Analyst-derived | p. 21, T6 |
| Findings by resource | 17 / 19 | cases | Memory / disk | Analyst-derived | p. 21, T6 |

# 21. Claim–evidence map

| Claim | Evidence | Figure/table/experiment | Source | Qualification / evidence strength |
|---|---|---|---|---|
| Agent resources have distinct release boundaries | Three definitions and source-analysis procedure | F1, X1 | pp. 4, 7–8 | Strong support for the authors' taxonomy; not an exhaustive taxonomy of every system. |
| AgentDoS combines static modeling and dynamic prompt testing | Architecture and detailed procedures | F3, T1, E1–E3 | pp. 6–10 | Strong descriptive support; prototype not independently executed. |
| Lifecycle classification is accurate in tested sample | 95.2% reported accuracy | X1 | p. 11 | Sample-based; no uncertainty interval or exact validation denominator. |
| The system finds real resource-exhaustion issues | 36 manual confirmations, 16 affected apps | X2, T2, T6 | pp. 11–12, 21 | Strong author-reported local evidence; production prevalence unknown. |
| It outperforms adapted AgentFuzz here | 36 versus 3 TP on 38 cases | X3, T3 | pp. 12–13 | Strong within-benchmark descriptive comparison; constructed ground truth. |
| Each major fuzzing module helps | Detection falls to 31, 25, or 16 | X4, T4 | p. 13 | Supports component usefulness under cap; prose/table issue for scheduling. |
| Retention outside model context matters | State/log purpose analysis and long-lived case | X1, X6, F5 | pp. 12, 14, 21 | Supported mechanism, but simplified history code conflicts with default-behavior prose. |
| Size and cleanup controls address different causes | Reported AutoGPT size and directory cleanup changes | Discussion | p. 15 | Mitigation report, not controlled defense-effectiveness experiment. |
| Black-box application is limited | Explicit source-access limitation | Limitations | p. 15 | Strong author statement; suggested adaptation is future work. |
| Agents add application-layer risks beyond inference | Workflow and explicit related-work distinction | F1, §8 | pp. 4, 14 | Analyst relevance inference; no standalone-versus-agent experiment. |

# 22. Very simple explanation — Explain Like I'm 15

A chatbot can answer a question, but an agent can also act on the answer: download files, search a database, parse a webpage, and keep results for later. Those actions use the computer's memory and storage. The paper asks what happens when someone requests work that uses too much of those resources.

There are three ways to run out. One request can use too much before it finishes. Many requests in one conversation can fill a history buffer. Or files can remain after conversations end and gradually fill the disk. Cleaning something up eventually is not enough if it grows too large before cleanup, and limiting each request is not enough if leftovers keep accumulating.

The researchers built a tester that reads the agent's code to find these operations, then uses another language model to write and improve test requests. It checks both whether the request reaches the right tool and how much memory or storage it uses. In their 20-agent study, it found 36 confirmed problems. Its comparison and accuracy numbers apply to their particular tests and benchmark.

For your research question, this explains why giving a model tools and persistent state can introduce additional security problems: there is more software doing work and keeping data. But this paper does not directly test whether standalone models are generally safer. It demonstrates a specific added risk—resource exhaustion in the agent application—and shows why sensible limits and cleanup must cover the whole task and resource lifetime.

# Completeness Audit

This audit compares the explanation with the supplied-document inventory. 'Represented in compressed form' means the component's substantive role and findings are included, while repeated wording, secondary examples, or bibliographic detail are reduced. It does not mean the original artifact was reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Cover, title, authors, venue | Yes, visual + text | Yes | Represented in compressed form | Publication identifiers retained; decorative layout omitted. |
| Abstract | Yes, visual + text | Yes | Fully represented | Main problem, taxonomy, framework, counts. |
| §1 Introduction and contribution bullets | Yes; p. 3 text-only | Yes | Represented in compressed form | Motivation, challenges, novelty claims, headline results. |
| §2.1 Background | Yes | Yes | Fully represented | Agent workflow and three definitions. |
| §2.2 Motivation Example | Yes | Yes | Fully represented | Persistent files, limits, existing-detector argument, line-reference discrepancy. |
| §2.3 Problem Understanding | Yes | Yes | Fully represented | Retention, incomplete limits, autonomy tradeoff. |
| §2.4 Threat Model | Yes | Yes | Fully represented | Benign environment, remote ordinary interface, prompt-based load. |
| §3.1 Challenges and Insights | Yes | Yes | Represented in compressed form | Repeated introductory challenges consolidated. |
| §3.2 Approach Overview | Yes | Yes | Fully represented | Two phases and lifecycle-specific dispatch/output. |
| §4.1.1 Candidate locating | Yes | Yes | Fully represented | Sink list, call context, backward paths, implicit calls. |
| §4.1.2 Lifecycle identifying | Yes | Yes | Fully represented | Memory/disk rules and manual fallback. |
| §4.1.3 Exploitability assessing | Yes | Yes | Fully represented | Input influence, loop rules, size checks, Boolean filter. |
| §4.2.1 Seed generation | Yes; p. 9 text-only | Yes | Fully represented | Runtime prompt capture and one-shot guidance. |
| §4.2.2 Scheduling | Yes, text-only | Yes | Fully represented with uncertainty | Scores, selection penalty, formula ambiguities. |
| §4.2.3 Mutation | Yes, text-only | Yes | Fully represented | Independent histories, Explorer, Exploiter, workload resources. |
| Prompt 1 | Yes, visual + text | Yes | Represented in compressed form | Calculator example and functionality guidance. |
| Prompt 2 | Yes, text-only | Yes | Fully represented | Three ratings and lower-bound discrepancy. |
| Prompt 3 | Yes, text-only | Yes | Represented in compressed form | Explorer reasoning/feedback procedure. |
| Prompt 4 | Yes, text-only | Yes | Represented in compressed form | Exploiter resource links summarized; not executed. |
| §5 Implementation | Yes, mostly text-only | Yes | Fully represented | APIs, code sizes, instrumentation, parameters, files. |
| §6.1 Setup | Yes | Yes | Fully represented | Selection protocol, models, hardware, Docker. |
| §6.2 / RQ1 / X1 | Yes | Yes | Fully represented | Classification and purpose percentages with scope. |
| §6.3 / RQ2 / X2 | Yes | Yes | Fully represented | Caps, costs, findings, sampled misses. |
| §6.4 / RQ3 / X3 | Yes | Yes | Fully represented | Adapted baseline and benchmark construction. |
| §6.5 / RQ4 / X4 | Yes | Yes | Fully represented with inconsistency | Variants, results, scheduling discrepancy. |
| Formal hypotheses | None supplied | Yes | Absence recorded | No hypothesis testing invented. |
| §7 Case I / X5 | Yes | Yes | Fully represented | One-turn memory accumulation and confirmation. |
| §7 Case II / X6 | Yes | Yes | Fully represented with uncertainty | Session history and code/prose conflict. |
| §8 Related Work | Yes | Yes | Represented in compressed form | Three categories; individual external papers not reread. |
| §9 Discussion: stealth | Yes | Yes | Fully represented | Ordinary-looking resource abuse. |
| §9 Discussion: re-delegation | Yes | Yes | Fully represented | Conceptual benign-trigger scenario, not measured experiment. |
| §9 Discussion: resource management | Yes | Yes | Fully represented | Autonomy, context retention, security tradeoff. |
| §9 Mitigation | Yes; continuation text-only | Yes | Fully represented | Reported concrete limits and proposed monitoring/deduplication. |
| §9 Limitations | Yes, text-only | Yes | Fully represented | Source-access limit and black-box proposal. |
| §10 Conclusion | Yes, text-only | Yes | Represented in compressed form | Repeated headline findings consolidated. |
| Acknowledgement | Yes, text-only | Yes | Inspected but deliberately omitted as non-substantive to technical analysis | Funding and thanks not individually reproduced; corresponding-author note recorded here. |
| Ethical: disclosure/stakeholders | Yes, text-only | Yes | Represented in compressed form | Developer/user impacts, reporting, anonymization issue. |
| Ethical: local impact/dual use/access | Yes, text-only | Yes | Represented in compressed form | Isolated local tests and conditional prototype access. |
| Ethical: mitigations/decision | Yes, text-only | Yes | Represented in compressed form | Repeated defense and disclosure assurances consolidated. |
| Open Science | Yes, text-only | Yes | Fully represented | Dataset/baseline release and conditional code access. |
| References [1]–[86] | Yes, text-only | Yes | Represented in compressed form | Relevant citations categorized; full bibliography not duplicated. |
| Figure 1 | Yes, visually | Yes | Fully represented | Nested scopes and workflow. |
| Figure 2 | Yes, visually | Yes | Fully represented | Code, repetition, limits, persistence, reference error. |
| Figure 3 | Yes, visually | Yes | Fully represented | Architecture and feedback loop. |
| Figure 4 | Yes, visually | Yes | Fully represented | Short-lived memory mechanism. |
| Figure 5 | Yes, visually | Yes | Fully represented with uncertainty | Long-lived mechanism and slice discrepancy. |
| Table 1 | Yes, visually | Yes | Fully represented | All eight features. |
| Table 2 and footnotes | Yes, visually | Yes | Fully represented | All rows, units, counts, scope. |
| Table 3 | Yes, visually | Yes | Fully represented | All values and benchmark qualification. |
| Table 4 | Yes, visually | Yes | Fully represented | All values and inconsistencies. |
| Table 5 | Yes, visually | Yes | Represented in compressed form | All sink families/method groups; source spelling noted. |
| Table 6 | Yes, visually | Yes | Represented in compressed form | Every application classification/count and masked assigned ID represented. |
| Equations 1–3 | Yes, text-only | Yes | Fully represented with notation caveats | Original rendering unavailable; definitions and unresolved issues retained. |
| Numbered algorithm/pseudocode | None supplied | Yes | Absence recorded | Procedure and simplified code represented; no hidden algorithm inferred. |
| Major contributions | Yes | Yes | Fully represented | Conceptual, methodological, implementation, empirical. |
| Author-stated limitations | Yes | Yes | Fully represented | Separated from analyst observations. |
| Appendix A | Yes, visually | Yes | Fully represented in compressed form | Sink list. |
| Appendix B | Yes, visually | Yes | Fully represented | Both case diagrams. |
| Appendix C | Yes, visually | Yes | Fully represented in compressed form | Findings/status, no hidden CVE digits guessed. |
| Separate supplements/artifacts | Not supplied | No direct inspection | Missing from supplied material | Dataset package, baseline code, prototype, repositories, mitigation commit. |

## Missing or inaccessible material

No numbered text page is missing from the supplied 1–21 sequence. Original visual renderings for pages 3, 9, 10, and 15–20 were not supplied. The full PDF file was not opened, and its hash was not independently verified. Referenced datasets, benchmark/baseline artifacts, AgentDoS source, underlying agent revisions, the AutoGPT mitigation commit, and cited works were not reviewed. No separate supplement was supplied. The failed '-' image path provides no inspectable additional evidence.

## Uncertain interpretations

Equation 1's zero-distance convention; text-only exponent rendering; semantic score lower bounds; retained-resource measurement timing; Figure 5's default history slice; scheduling prose/table disagreement; scheduling recall rounding; timeout line-reference mismatch; anonymized case-name mismatch; and the scope of claimed full anonymization remain explicit uncertainties. Exact validation-sample denominators, repeated-run variation, oracle timeout, per-agent hardware details, and actual current artifact availability are not established.

## Deliberately compressed material

Repeated problem statements, challenge descriptions, conclusion language, and ethical assurances are consolidated. Full prompt templates are explained rather than copied. Table 6 rows are grouped by application while retaining lifecycle/resource multiplicities and masked assigned identifiers. Table 5 API families are grouped while preserving substantive sink coverage. Bibliographic entries, funding identifiers, logos, sponsorship, and pagination decorations are not duplicated. Ethical stakeholder effects are compressed to interruption, unavailable service, possible lost/incomplete work, operational costs, and reputational consequences; these are author-discussed impacts, not separately measured outcomes.

## Potential omissions

No known substantive section, research question, major experiment, figure, table, numbered equation, stated limitation, or appendix from the supplied inventory is left unrepresented. Representation is nevertheless partial where the source itself is ambiguous, implementation detail is absent, original equation/page images are unavailable, or referenced artifacts were not supplied. The report therefore claims inventory-based coverage of the supplied evidence, not complete recovery of the original research process, independent reproduction, or exhaustive knowledge of agent security.
