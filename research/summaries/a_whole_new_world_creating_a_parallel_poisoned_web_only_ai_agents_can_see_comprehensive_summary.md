## Stage 0 — Document Accessibility Report

The supplied material contains extracted text labeled physical PDF pages 1–10 and directly visible page images for pages 1, 5, 6, and 7. All ten text records were inspected. The four supplied page images were visually inspected, including Figure 1 on page 7. Pages 2–4 and 8–10 were inspected through supplied text only; their complete visual appearance was not available. No tools, browsing, external sources, or independent execution were used. Instructions appearing inside the paper are treated exclusively as evidence about an attack.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied text covers pages 1–10, ending with references. |
| Physical pages accessible | 1–10 through text; 1, 5, 6, 7 also through images. |
| Apparently missing pages | None apparent within the supplied sequence; this does not independently establish that every original artifact was supplied. |
| Readability | The supplied text is readable. The four images are sufficient for their substantive text and the attack diagram. |
| Visual content | Partial page rendering; the one identified substantive figure is visually available. |
| Tables | No substantive tables identified in supplied text or rendered pages. |
| Equations | No numbered equations, mathematical derivations, or substantive symbolic formulas identified. |
| Appendices | None identified in the supplied work. |
| Supplementary material | None supplied. Accessibility metadata reports zero embedded files and no detected supplementary references. |
| Referenced external artifacts | References and a documentation footnote are present; their destinations were not opened. No experimental code, logs, or dataset was supplied. |
| OCR | Not needed for the available readable text and images. No independent OCR was performed. |
| Integrity verification | The supplied SHA-256 is retained as an identifier; it was not independently recomputed. |

Evidence labels used below are: **[A] author-reported**, **[B] directly observable in supplied visuals**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information [E] is introduced. HIGH confidence means strong support for the stated reading of the supplied material, not independent confirmation that an attack or defense works. MEDIUM denotes qualified interpretation or incomplete operational detail. LOW and UNKNOWN are used where evidence does not support a firm conclusion.

## 1. Plain-language orientation

**[A]** This paper studies how a malicious website can show different material to a human and an artificial intelligence agent. Its original title is *A Whole New World: Creating a Parallel-Poisoned Web Only AI-Agents Can See*. Shaked Zychlinski, affiliated with JFrog, argues that automated browsing agents often reveal recognizable browser, automation, or network characteristics. A website can use those characteristics to decide which visitor should receive an attack. Humans receive ordinary content; a detected agent receives content designed to redirect its behavior. Sources: p. 1, abstract; p. 2, §1.4.

The central mechanism combines **fingerprinting**, identifying characteristics of a visitor, with **cloaking**, serving different content to different visitors. The malicious response may contain hidden instructions, or it may openly demand an apparently necessary action, such as authenticating with a secret available in the agent's environment. The latter is important: this paper is not limited to invisible text embedded in an otherwise identical page. Sources: p. 2, §1.4; p. 5, §3.2.2.

**[A]** The author reports a small demonstration using an internal API documentation website and Cursor with Claude 4 Sonnet, GPT-5 Fast, and Gemini 2.5 Pro. The agent-facing page requested authentication using an environment variable. The reported outcome is that the attack succeeded in all cases. The paper does not give a trial count, measured fingerprinting accuracy, detailed outcome criteria, or statistical analysis. Source: p. 6, §4.

**[D] Research relevance:** The paper helps explain why a web agent may face risks beyond those faced by a standalone text-generating model: an agent retrieves attacker-controlled material, makes decisions from it, and can act through tools that may reach sensitive resources. However, this paper does not directly compare web agents with standalone large language models. It establishes neither a numerical vulnerability difference nor a general ranking across those system classes. Its central contribution is an agent-targeted delivery mechanism and an illustrative demonstration, rather than a controlled comparative study.

## 2. Document roadmap

The document is a cybersecurity technical paper with a conceptual attack model, related-work discussion, small experimental demonstration, proposed defenses, and future research agenda. It is not a systematic review, large benchmark, mathematical theory paper, or controlled comparison of standalone models and agents.

| Inventory ID | Original component | Physical pages | Role |
|---|---|---:|---|
| M1 | Title, author, affiliation, identifier | 1 | Identifies the work and author. |
| AB1 | Abstract | 1 | States mechanism, claimed consequences, and significance. |
| S1 | §1 Introduction | 1–2 | Motivates agentic systems and web exposure. |
| SS1.1 | §1.1 The Rise of Agentic LLMs | 1 | Explains tools and the sense-plan-act loop. |
| SS1.2 | §1.2 The Web as an Attack Surface | 1–2 | Introduces external content as a manipulation channel. |
| SS1.3 | §1.3 An Overview of Website Fingerprinting and Cloaking | 2 | Defines the two enabling techniques. |
| SS1.4 | §1.4 The Attack | 2 | States the thesis and alternative malicious page forms. |
| S2 | §2 Background and Related Work | 2–4 | Connects browser detection, cloaking, and agent attacks. |
| SS2.1.1–3 | Browser fingerprinting; agent fingerprintability; website cloaking | 2–3 | Lists identifying attributes and delivery techniques. |
| SS2.2.1–3 | Indirect prompt injection; RAG and memory poisoning; autonomous hacking | 4 | Describes attack effects and related capabilities. |
| FN1 | Public bot-documentation footnote | 3 | Example supporting the public-declaration argument. |
| S3 | §3 The Attack | 4–6 | Specifies adversary and attack workflow. |
| SS3.1 | §3.1 Threat Model | 4 | States goals, capabilities, and knowledge. |
| SS3.2.1–2 | Fingerprinting; serving cloaked content | 5 | Describes the two stages and routing decision. |
| SS3.3 | §3.3 Execution Flow: Hijacking the Agent | 5–6 | Gives a six-step illustrative sequence. |
| X1 / S4 | §4 Experiment | 6 | Reports the internal-site demonstration. |
| F1 | Figure 1 | 7 | Visually contrasts human and agent paths. |
| S5 | §5 Discussion and Countermeasures | 6, 8 | Interprets risk and proposes defenses. |
| SS5.1 | §5.1 Security Implications | 6 | Discusses scale, stealth, and misuse of the trusted agent. |
| SS5.2.1–2 | Agent-side; network and server-side defenses | 8 | Lists five defensive approaches. |
| S6 | §6 Conclusion and Future Work | 8–9 | Summarizes the argument and open research needs. |
| SS6.1–2 | Conclusion; future work | 8–9 | Calls for pipeline security and four research directions. |
| REF1 | References | 9–10 | Bibliographic support; not independently verified. |

The first-page identifier is arXiv:2509.00124v1, with a displayed date of 29 Aug 2025 and subject label cs.CR. These are transcribed metadata, not independently checked publication facts. No conference or journal publication venue is identified for this paper in the supplied material.

## 3. Background and context

**[A] Large language model (LLM):** The paper contrasts sophisticated text generation with agentic use, where a model is connected to tools. It does not give a formal model definition, parameter count, or training account. Its focus is what happens when model reasoning participates in an operational system. Source: p. 1, §1.1.

**[A] Agent and sense-plan-act loop:** An agent observes an environment, reasons about a next step, and executes an action. Examples include browsing websites, executing code, interacting with application programming interfaces (APIs), clicking, and filling forms. This cycle is the route by which external material can affect subsequent actions. Source: p. 1, §1.1.

**[A] Browser fingerprinting:** A site collects attributes such as browser headers, fonts, screen resolution, plugins, and language settings to distinguish visitors. The paper also discusses graphics-related fingerprinting and automation-specific signs. These are candidate identifying signals; the paper supplies no measurement of how reliably a particular combination distinguishes its experimental agents. Sources: pp. 2–3, §§1.3, 2.1.

**[A] Cloaking:** A server changes what it returns according to the visitor's identity or characteristics. The paper describes traditional uses involving search engine optimization and phishing, then redirects this logic toward AI agents. A benign response to a human inspector does not, under this mechanism, establish what a targeted agent received. Source: p. 2, §§1.3–1.4.

**[A] Indirect prompt injection (IPI):** Instructions are placed in external content rather than supplied as the legitimate user's request. The paper describes them as overriding the original task when an agent processes the content. This is distinct from an authorized user asking for a different task. Source: p. 4, §2.2.1.

**[A] Retrieval-augmented generation (RAG):** Agents may use retrieved external knowledge to inform their responses. The paper discusses poisoning retrieved documents or memory as another possible consequence of targeted content delivery. It cites AgentPoison for delayed harmful behavior; it does not experimentally test that mechanism here. Source: p. 4, §2.2.2.

**[D] Connecting these terms:** Fingerprinting selects a target, cloaking delivers a selected response, and prompt injection or a deceptive prerequisite tries to change the agent's behavior. These are separate functions. Identifying an agent alone does not demonstrate compromise, and a successful prompt injection alone does not demonstrate selective cloaking.

## 4. Research problem and gap

**Existing problem [A]:** Agents interact with untrusted web material while carrying out legitimate tasks. The threat can therefore originate in retrieved content, not merely in the user's prompt. The author associates this with unauthorized data disclosure, malware-related actions, and other unwanted behavior. Sources: pp. 1–2, §1.2.

**Shortcomings of previous approaches according to the author [A]:** The paper argues that conventional human inspection and ordinary security crawlers may see only a benign version of a site. It also argues that prompt-level safety is insufficient when the entire observation-to-action pipeline can be manipulated. These are author positions, not results from a reported head-to-head evaluation of existing security products. Sources: p. 2, §1.4; p. 6, §5.1; p. 8, §6.1.

**Research gap [A/D]:** The author positions predictable agent fingerprints as enabling targeted cloaking. The claimed gap is attention to an agent-specific delivery channel that combines established techniques. Interpreting this as a gap in comprehensive measurement is reasonable, but the paper itself does not systematically establish how much prior work overlooked this combination. Its related-work section is narrative rather than a reproducible literature search.

**Motivation [A]:** Agents' useful capabilities become dangerous when a hostile page can steer them. A malicious site can wait for visits instead of requiring the legitimate user to provide an overtly malicious instruction. Sources: p. 4, §2.2; p. 6, §5.1.

**Scope:** The implemented example concerns an internal documentation site, agent detection, and an environment-variable authentication request in Cursor. Broader claims about browser history, cookies, malware, misinformation, memory poisoning, or autonomous hacking extend beyond the reported experimental detail. The paper discusses those consequences but does not demonstrate each one.

## 5. Research questions / objectives / hypotheses

There are no formally enumerated research questions or hypotheses in the supplied paper. The following are informal author objectives and thesis statements, not newly invented formal hypotheses.

- **O1 [A]:** Describe and formalize an attack that combines agent fingerprinting with website cloaking. Sources: p. 1, abstract; p. 4, §3.
- **O2 [A]:** Explain how a site distinguishes agent traffic and chooses a malicious response. Source: p. 5, §3.2.
- **O3 [A]:** Demonstrate the mechanism through an agent-facing authentication request on an internal site. Source: p. 6, §4.
- **O4 [A]:** Discuss countermeasures and future research. Sources: pp. 8–9, §§5.2, 6.2.
- **Central thesis [A]:** A malicious website can reliably distinguish an AI agent from a human and use that distinction to deliver an agent-exclusive payload. Source: p. 2, §1.4. Reliability is asserted, but no detection reliability measurement is supplied.

**User's research question [D]:** Why are web AI agents more vulnerable than standalone LLMs? This paper provides a proposed mechanism relevant to that question: web exposure introduces attacker-controlled observations, and tool use can convert manipulated reasoning into actions. It does not isolate these factors experimentally or establish that every agent is more vulnerable than every standalone model. The comparison remains an analyst inference with important scope limits.

## 6. Assumptions / threat model

**Attacker goal [A]:** Hijack a web-browsing LLM agent into unauthorized action. Listed examples include data exfiltration, malware installation, and social media manipulation. Stealth is a secondary goal: the attack should remain invisible to the human user and evade ordinary crawlers. Source: p. 4, §3.1.

**Attacker capabilities [A]:** The adversary controls a web server, can examine incoming requests, can implement server-side selection logic, and can craft malicious content. The attacker may create a visually benign page containing a hidden payload. The paper also explicitly allows a completely different page, including an authentication demand. Sources: p. 4, §3.1; p. 2, §1.4.

**Attacker knowledge [A]:** Knowledge may concern common automation framework signatures or a particular commercial agent's fingerprint. The paper does not require prior knowledge of a particular user's secret value. Source: p. 4, §3.1.

**Environmental assumptions [A/D]:** The agent must visit the attacker-controlled site and receive the targeted response. For the environment-variable scenario, the agent must have a route to the relevant environment variable and must be willing or permitted to use it in the requested interaction. The latter requirements follow from the described action; the paper does not separately specify the permission system, approval settings, or exact access path used in the demonstration. Sources: p. 2, §1.4; p. 6, §4.

**Trust boundaries [D]:** The important boundary is between untrusted website material and authorized agent behavior. A second boundary concerns the agent's access to local or sensitive resources. The example fails securely only if the web request cannot cause inappropriate access or disclosure; the paper reports that its tested setup did not maintain that boundary. This is a conceptual interpretation, not an implementation audit.

**Unknown or unspecified exclusions:** The supplied work does not enumerate a full list of excluded attacker powers. It does not require an attacker to alter model weights, directly control the system prompt, or compromise the user's machine before the visit, but these are not presented as a formal exclusion list. No classifier threshold, acceptable error rate, or complete attacker-cost model is defined.

## 7. Methodology

The methodology has three levels: a background taxonomy of possible fingerprints, a general two-stage attack procedure, and one reported experimental instantiation. Keeping those levels separate prevents the full taxonomy from being mistaken for an implemented detection system.

**Fingerprint candidates [A]:** The paper lists HTTP headers such as User-Agent and Accept-Language; screen, font, plugin, and color-depth properties; Canvas and WebGL-related signatures; automation framework artifacts; browser extension identifiers or resources; non-human interaction patterns; model-response fingerprinting; and publicly declared bot identities. Sources: pp. 2–3, §2.1. The model-fingerprinting discussion cites LLMmap but does not implement or evaluate it in this study.

**Stage one: detection [A]:** A fingerprinting script checks automation artifacts, known agent User-Agent values or IP addresses, anomalous browser properties, IP and autonomous system number (ASN) information, and behavioral cues. The text does not give source code, a feature vector, a trained classifier, a decision formula, or a measured false-positive/false-negative rate. Source: p. 5, §3.2.1.

**Stage two: response selection [A]:** Human-like visitors, known security crawlers, and unidentifiable visitors receive the legitimate default page. Visitors strongly identified as agents receive the cloaked page. This default matters: ambiguous visitors are described as receiving benign content, supporting stealth at the possible cost of missing some agents. No numerical operating point is reported. Source: p. 5, §3.2.2.

**Six-step workflow [A]:** A user gives a benign task; the agent visits the hostile site; the site fingerprints and serves the targeted page; the agent ingests malicious instructions; its behavior is redirected; and it may complete the original task afterward to conceal the deviation. The browser-history and cookie scenario illustrates this general sequence. It is not the same as the internal-site experiment. Sources: pp. 5–6, §3.3.

**Experimental implementation [A]:** An internal website serves API documentation to benign visitors and an authentication request to identified agents. The request asks for a particular environment variable and explicitly identifies a shell command for retrieving it. Cursor is the agent application, with three named model configurations. Source: p. 6, §4.

**Unreported configuration:** The supplied work does not specify Cursor version, model API identifiers, sampling settings, model snapshots, browser engine/version, operating system, hardware, site framework, detector implementation, complete user prompt, full malicious response, permission settings, environment setup, trial repetitions, random seeds, or logging method. It provides no training procedure, preprocessing, annotation protocol, dataset split, baseline system, statistical test, confidence interval, or runtime/cost measurement. Some items would not be necessary for a conceptual argument, but their absence limits replication of the empirical claim.

## 8. Experiments / analyses

### X1 — Internal documentation-site authentication demonstration

**Purpose [A]:** Validate the proposed attack by presenting a malicious authentication prerequisite only to detected agents. **Setup [A]:** An internal site has a benign API documentation response and a server-side detection script. The targeted response asks the agent to validate itself using a specific environment variable. Figure 1 illustrates the benign and malicious paths. Source: p. 6, §4; p. 7, Figure 1.

| Condition ID | Reported application | Reported powering model | Reported result | Missing detail |
|---|---|---|---|---|
| X1a | Cursor | Claude 4 Sonnet, Anthropic | Included in the statement that all cases succeeded | Trial count and trace absent |
| X1b | Cursor | GPT-5 Fast, OpenAI | Included in the statement that all cases succeeded | Trial count and trace absent |
| X1c | Cursor | Gemini 2.5 Pro, Google | Included in the statement that all cases succeeded | Trial count and trace absent |

**Variables and comparison [D]:** The named model configuration varies across the listed cases. The site also distinguishes benign and agent-facing responses, but no controlled human-versus-agent result table is reported. The documentation page functions as the benign branch of the design, not as a quantified experimental baseline.

**Data/sample:** There is one described internal website and three listed model configurations. The number of independent runs is not stated. The paper supplies no collection of websites, task corpus, or participant sample. **Metric:** Success is reported qualitatively without an operational definition. **Statistics:** None reported.

**Result [A]:** The author says the attack succeeded in all cases. **Caveat [D]:** This supports a reported demonstration under the listed setup. It does not supply enough information to calculate a per-attempt attack success rate, uncertainty interval, detection rate, or model ranking. Nor does it establish whether success required automatic tool execution, user approval, or particular permissions.

### Other analyses, without separate experimental evidence

The fingerprint taxonomy, six-step cookie/history scenario, memory-poisoning discussion, and mitigation list are conceptual or literature-based portions of the paper. They are not additional experiments conducted in the supplied study. No ablation, defense test, alternative-agent-application test, or standalone-LLM comparison is reported.

## 9. Results

**R1 — Reported feasibility in the demonstration [A].** The internal authentication attack is reported successful for all listed Cursor/model cases. Source: p. 6, §4. Evidence strength: an author-reported qualitative demonstration, without traces or repeated-trial accounting.

**R2 — Selective content delivery [A/B].** The methodology describes a benign default response and an agent-specific response; Figure 1 depicts the corresponding green and red paths. Sources: p. 5, §3.2.2; p. 7, Figure 1. The figure clarifies intended behavior but is not a measurement of classifier performance or field deployment.

**R3 — Different-page attacks are in scope [A].** A targeted response may be entirely different from the benign page. This supports an authentication-pretext interpretation of the experiment. Sources: p. 2, §1.4; p. 5, §3.2.2. It qualifies the abstract's narrower wording about a visually identical page with hidden instructions.

**R4 — Broader consequences remain proposed or attributed to related work [A/D].** Exfiltrating browser data, installing malware, poisoning memory, and misusing autonomous hacking capabilities appear as examples, threats, or cited background. They are not all empirical findings of X1. Sources: p. 4, §2.2; pp. 5–6, §3.3.

**R5 — Defense effectiveness is unmeasured [D].** The work proposes several defenses but reports no defense-versus-attack results. It therefore cannot establish a numerical security benefit or utility cost for any listed mitigation. Source basis: p. 8, §5.2, compared with the single experiment on p. 6.

**Numerical discipline:** Three named configurations are not three documented independent trials. The wording about all cases does not justify converting the result into a general 100% success rate. There are no reported absolute improvements, percentage-point differences, relative improvements, latency ratios, or costs to calculate.

## 10. Figure-by-figure interpretation

### Figure 1 — Benign documentation path versus agent authentication path

**Inspection status:** Directly visually inspected on supplied page 7, with the caption and nearby experiment text also inspected. This is a conceptual flow diagram, not a quantitative plot. It has no axes, units, numerical scale, error bars, confidence intervals, statistical markers, or measured values.

**Components [B]:** A user icon appears at upper left and an agent icon at upper right. A task strip beneath them asks for an app designed using documentation on malicious.com. Both are connected toward a central server labeled malicious.com. A document object labeled Doc File appears below. A separate authentication box lies on the agent branch and requests a private API key.

**Encoding [B]:** Green arrows identify the benign human path; red arrows identify the agent path. The user-side green route reaches the central server and then the documentation object. The agent-side red route reaches the same server, passes through the authentication box, and then rejoins the documentation destination. Arrow direction presents a sequence of interactions; it should not be read as a complete network protocol trace.

**Caption [A]:** The benign page is served to the user, whereas a detected agent must authenticate using a specific environment variable before receiving the actual documentation. The caption explicitly connects this sequence to concealment from the user. Source: p. 7, Figure 1.

**Interpretation [D]:** The diagram illustrates a task-dependent prerequisite: the agent is offered the legitimate destination after a sensitive action. This is more specific than a generic instruction to abandon the user's task. The agent can apparently continue toward the legitimate goal while taking the unauthorized step, making final task completion an unreliable sign that no deviation occurred.

**Caveats:** The visual shows neither the detection script nor the actual transmission containing the secret. It does not show a filesystem, shell, permission prompt, request payload, or log. Its arrows do not prove successful exfiltration. There are no separate labeled panels. The icons communicate roles rather than experimental observations; their decorative details are not substantive evidence.

## 11. Table-by-table interpretation

No substantive author-created table appears in the supplied text or the four rendered pages. There is no results matrix, dataset table, configuration table, or defense comparison to interpret. Tables in this analysis are analyst-organized summaries, not reproduced paper tables.

This absence has a practical consequence: the short statement of experimental success is not accompanied by tabulated trial counts or per-condition metrics. That is an observation about the supplied reporting, not evidence that additional measurements were never performed outside the document.

## 12. Diagram / architecture interpretation

Figure 1 is the paper's only identified substantive architecture or flow object. To avoid counting it as a second experiment, this section explains its relationship to the methodology rather than treating it as additional evidence.

**Input:** A legitimate user's documentation-dependent task and a visitor request to the server. **Selection point:** The server classifies the requester. This decision is described in §3.2 but not drawn as an explicit diamond. **Benign output:** Documentation without the sensitive prerequisite. **Targeted output:** An authentication demand followed by access to documentation. Sources: p. 5, §3.2; p. 7, Figure 1.

**Control flow [D]:** The attack changes the route the agent follows to complete the user's task. **Sensitive-data flow [A/D]:** The text identifies an environment variable as the authentication material, but the diagram does not specify the receiving endpoint, exact request, or storage. **Processing stages:** Recognition, targeted response, attempted secret use, and eventual documentation delivery. **Feedback:** No repeated loop or recurring challenge is depicted; it would be unsupported to describe this example as an experimentally studied retention trap or repeated prerequisite sequence.

The paper separately proposes planner-executor isolation as a defensive architecture. That proposal is described in text on page 8, not implemented or illustrated in a second supplied figure. The distinction matters because the attack diagram depicts the vulnerable interaction, while the defense is an untested architectural suggestion.

## 13. Equations and mathematical concepts

No major equations, losses, optimization objectives, formal probability models, lemmas, propositions, theorems, or proofs are supplied. The claim that the work formalizes a threat model refers to a structured description of goals, capabilities, and knowledge, not to a mathematical security proof.

Code-like strings in the text identify browser properties, request attributes, domains, and an environment-variable retrieval example. They are not equations. The dollar-prefixed secret name denotes an environment variable in the described shell context, not a mathematical symbol. Model version numbers are labels, not measured numerical quantities.

**[C] Simple count only:** The experiment lists Claude 4 Sonnet, GPT-5 Fast, and Gemini 2.5 Pro; counting these entries gives 3 model configurations. The calculation is 1 + 1 + 1 = 3. It does not reveal the number of attempts, successful runs, or independent samples. No further derived performance statistic is justified.

## 14. Interpretation and discussion

**Author interpretation [A]:** Useful agents must interact with untrusted data, and that interaction is a compromise vector. By combining fingerprinting with cloaking, an attacker can build a benign experience for humans and a malicious experience for AI agents. The author therefore advocates protecting the full sense-plan-act pipeline. Sources: p. 6, §5; p. 8, §6.1.

**Answering the user's research question [D]:** The work suggests three connected reasons web agents can face additional risk. First, their observations can be selected by an adversary rather than being limited to a direct user exchange. Second, their browser or network identity may help an attacker choose an agent-specific payload. Third, tool access can turn acceptance of that payload into an external action involving sensitive resources. These are mechanisms relevant to comparative vulnerability, not a measured comparison with standalone LLMs.

**Important condition [D]:** Harm depends on what tools and permissions the agent actually has. A webpage's instruction does not itself establish that a particular agent can read arbitrary secrets or execute code. The paper's broad illustrative scenarios assume the relevant access; its experiment omits the detailed permission configuration needed to assess that assumption precisely.

**Text–text scope check:** The abstract describes a visually identical malicious page, while §1.4 and §3.2.2 explicitly allow a completely different page. These statements can be read as a narrow initial description followed by a broader attack family. The authentication experiment belongs to the broader family; the supplied evidence does not establish visual identity of the two experimental responses.

**Methods–results check:** The detection section lists many possible signals, but the experiment reports only a server-side identifying script. Which signals actually drove X1 remains unknown. Consequently, the paper's assertion of reliable distinguishability is not supported by a supplied classifier evaluation.

**Claim–evidence check:** The work describes broad stealth and scale advantages. It does not report a scanner comparison, user detection study, internet-scale deployment, or cost analysis. The evidence supports the proposed mechanism more strongly than universal claims about invisibility or scalability.

**Related-work boundary:** Cited work on IPI, memory poisoning, autonomous hacking, fingerprinting, and adaptive crawling supports the author's framing. Those references were not independently read here. Their reported capabilities must not be recast as experiments reproduced by this paper.

## 15. Contributions and novelty

**Conceptual contribution [A]:** Agent-specific cloaking combines established browser fingerprinting and selective content delivery to create an attack channel aimed at autonomous browsing systems. The author claims novelty for this combination. Sources: p. 1, abstract; p. 4, §3. Independent novelty verification is outside this closed-document analysis.

**Methodological contribution [A]:** A structured threat model, two-stage mechanism, and six-step execution scenario explain how an otherwise benign user task can lead to unauthorized action. Sources: pp. 4–6, §3.

**Implementation and empirical contribution [A]:** The internal documentation-site example reports successful attacks under three listed Cursor/model configurations. Source: p. 6, §4. The implementation is described but not supplied as runnable source.

**Defensive and agenda contribution [A]:** The paper organizes agent-side and ecosystem-side mitigations and proposes further work on fingerprint catalogs, sanitization, detection, and benchmarks. Sources: pp. 8–9, §§5.2, 6.2.

**Not established:** There is no new model training algorithm, formal theorem, released dataset, measured benchmark suite, or experimentally validated defense in the supplied material. The main novelty claim concerns attack delivery and framing rather than invention of fingerprinting, cloaking, or prompt injection individually.

## 16. Limitations

### Authors' stated limitations

No dedicated limitations section appears. The author does explicitly state that broader network/server-side defenses are harder to implement universally. The future-work section also identifies needs for systematic fingerprint knowledge, improved sanitization, large-scale detection, and robustness benchmarks. These are acknowledged challenges and open work, not an explicit retrospective discussion of experimental sample size or reproducibility. Sources: p. 8, §5.2.2; p. 9, §6.2.

### Additional evidence-based analyst observations

**[D] Limited empirical breadth:** One internal-site scenario and one agent application are described. Three named powering models broaden the configurations but do not establish breadth across applications, real websites, tasks, or permission environments.

**[D] Unknown denominator:** No attempt count or repetition schedule is reported. All-cases success cannot be assigned a population success probability from this account.

**[D] Detection is underspecified:** The paper supplies candidate signals but no experimental detector code, thresholds, error rates, or evidence separating agent detection from generic automation detection.

**[D] Success is underspecified:** No trace establishes exactly which actions occurred, whether a secret reached the server, how the value was checked, or whether approval intervened.

**[D] Broad consequences exceed the experiment:** Malware execution, memory poisoning, autonomous hacking, and browser-data theft are discussed without corresponding experiments in this paper.

**[D] Defenses are untested:** Recommendations do not include measured attack reduction, usability effects, task performance costs, or adaptive-attacker tests.

**[D] Comparative inference remains limited:** No standalone LLM baseline is present, so the user's comparative question cannot be answered with an effect size or controlled causal conclusion from this paper.

## 17. Threats to validity

The following labels are analyst-applied methodological categories, not headings or admissions from the author.

| Validity dimension | Evidence-based concern | Consequence |
|---|---|---|
| Internal validity | Full prompts, permissions, and traces are absent. | It is difficult to isolate which system features enabled the reported action. |
| Construct validity | Success and reliable detection are not operationally defined. | Different interpretations of compromise or recognition cannot be distinguished. |
| Statistical conclusion validity | Trial counts, repetitions, and uncertainty are absent. | No reliable rate, interval, significance test, or model ranking follows. |
| External validity | One internal website and Cursor are reported. | Results cannot be generalized to all web agents or arbitrary websites. |
| Ecological validity | The documentation task and environment are sparsely described. | Resemblance to everyday deployment settings cannot be fully assessed. |
| Reproducibility | Detector, site code, exact configurations, and logs are not supplied. | The demonstration cannot be independently reconstructed from the supplied detail alone. |
| Comparative validity | No standalone model condition exists. | The paper does not directly establish an agent-versus-standalone vulnerability difference. |

**[D] Shared application context:** Because all listed cases run through Cursor, observed outcomes may reflect the interaction of model behavior, application instructions, tool integration, and permissions. The evidence does not isolate the model as the sole source of vulnerability. This is not a claim that Cursor alone caused the outcome; the causal allocation remains unknown.

## 18. Future work and open questions

### A. Future work explicitly proposed by the author

1. **Fingerprinting common body of knowledge:** Systematically catalog major commercial and open-source agent fingerprints to understand the problem and inform randomization defenses. Source: p. 9, §6.2.
2. **Universal sanitization frameworks:** Develop context-aware methods that neutralize IPI while preserving useful information. Source: p. 9, §6.2.
3. **Large-scale cloaking detection:** Deploy anti-cloaking crawlers to assess whether agent-targeted cloaking is already occurring and generate threat intelligence. Source: p. 9, §6.2.
4. **Adversarial robustness benchmarks:** Standardize evaluation of resilience to cloaking and IPI and compare defensive measures. Source: p. 9, §6.2.

### B. Additional open questions logically remaining from the study

**[D]** How accurately does a concrete detector distinguish agents from ordinary automation, humans, and security crawlers? Which identifying features are necessary? How do errors affect stealth and targeting? These questions remain because the detector is not measured.

**[D]** Which permissions and approval settings allow the authentication pretext to cause secret access or disclosure? Does the agent reject the same request when tool access is restricted? These questions separate language-level persuasion from operational capability.

**[D]** How do the same payloads behave when provided to a standalone model, an agent without sensitive tools, and an agent with those tools? Such conditions would be needed to test the user's comparison directly; they are not reported here.

**[D]** Can proposed defenses preserve legitimate task completion while blocking deceptive prerequisites, including pages whose malicious demand is fully visible? What are the costs and failure modes? These are unresolved evaluation questions, not recommendations to execute new experiments as part of this analysis.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning within the paper | Boundary or qualification |
|---|---|---|
| LLM | Large language model, used for language-based reasoning or generation | No training details supplied. |
| AI agent | Model-based system that observes, plans, and acts using tools | Tool access varies; not every capability is guaranteed. |
| Sense-plan-act | Observe an environment, choose a next step, execute it | The paper's operational pipeline. |
| API | Application programming interface | Documentation provides the experiment's legitimate task material. |
| Fingerprint | Combination of identifying browser or network characteristics | Uniqueness and accuracy are not measured here. |
| Cloaking | Serving different content to different visitor classes | The selective delivery mechanism. |
| User-Agent | Request attribute identifying a browser or client | One possible detection signal. |
| HTTP | Hypertext Transfer Protocol, referenced through headers and requests | No detailed protocol analysis supplied. |
| HTML | Hypertext Markup Language, the page content/structure discussed | Actual agent input representation is not fully documented. |
| DOM | Document Object Model, mentioned in connection with browser properties | No formal definition is supplied by the paper. |
| IP | Internet Protocol address | Used as a possible origin or identity signal. |
| ASN | Autonomous system number | Listed as network information; not expanded in the source. |
| Headless browser | Browser configuration discussed as potentially showing unusual properties | Detailed operating mode not reported for X1. |
| IPI | Indirect prompt injection | Malicious instructions arrive through outside material. |
| RAG | Retrieval-augmented generation | External knowledge helps ground responses. |
| Memory poisoning | Malicious retrieved information affects stored knowledge or later behavior | Discussed through cited work, not tested here. |
| Exfiltration | Unauthorized transfer of sensitive information outward | Broad goal; exact X1 transmission trace absent. |
| Environment variable | Named value accessible in a process environment | The experiment's requested authentication material. |
| SEO | Search engine optimization | Background context for historical cloaking. |
| Planner-executor isolation | Separate high-level privileged reasoning from low-privilege exposure to web content | Proposed defense without experimental validation. |
| Honeypot-agent | A decoy agent intended to reveal suspicious website requests | Proposed ecosystem-side detection approach. |
| Living off the land | The author's analogy for using the victim's own trusted agent as an attack tool | Not a separately measured outcome. |

Graphics terms such as Canvas and WebGL and named frameworks are retained as source terminology. They identify possible fingerprinting surfaces; their external technical specifications are outside the supplied evidence.

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Accessible page records | 10 | physical PDF pages | Supplied text pages 1–10 | Directly observable supplied input | Input/page sequence |
| Visually inspected pages | 4 | page images | Pages 1, 5, 6, 7 | Directly observable supplied input | Supplied images |
| Described attack stages | 2 | stages | Fingerprinting, then cloaked delivery | Author-reported | p. 4, §3 |
| Enumerated execution steps | 6 | steps | Benign command through concealment | Author-reported | pp. 5–6, §3.3 |
| Listed powering-model configurations | 3 | configurations | Claude 4 Sonnet; GPT-5 Fast; Gemini 2.5 Pro | Analyst-derived: 1 + 1 + 1 | p. 6, §4 |
| Described experimental site | 1 | internal website | API documentation/authentication example | Author-reported singular setup | p. 6, §4 |
| Reported experimental outcome | All cases succeeded | Qualitative statement | Listed Cursor/model cases; attempts unspecified | Author-reported | p. 6, §4 |
| Independent run count | Not specified | runs | X1 | UNKNOWN | p. 6, §4 |
| Detection accuracy | Not specified | No metric supplied | Fingerprinting | UNKNOWN | pp. 5–6, §§3.2, 4 |
| Attack success rate with denominator | Not specified | No rate supplied | X1 | UNKNOWN | p. 6, §4 |
| Defense performance | Not specified | No metric supplied | Proposed mitigations | UNKNOWN | p. 8, §5.2 |

The model labels contain digits, but those digits are not accuracy, sample size, or experimental measurements. No percentages or effect sizes have been inferred from the qualitative outcome. No graph requires approximate visual numerical estimation.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Agents introduce web interaction into model operation | Description of tools and sense-plan-act | Conceptual framing | p. 1, §1.1 | Explicit author account; no standalone comparison. |
| A site can target agents using recognizable attributes | Fingerprint taxonomy and central thesis | Attack method | pp. 2–3, §§1.4, 2.1 | Reliability asserted, not measured. |
| Attacker controls response selection | Server-control threat model | §3 architecture | p. 4, §3.1 | Explicit capability assumption. |
| Ambiguous and benign visitors receive benign content | Default-path description | Two-stage mechanism | p. 5, §3.2.2 | No error-rate evaluation. |
| Agent response can be an entirely different page | Explicit scope statement | Attack construction | p. 5, §3.2.2 | Broadens abstract's visually identical example. |
| Internal site requested an environment variable | Experimental description | X1; F1 | pp. 6–7 | Request clear; complete transmission trace absent. |
| Reported success spans listed model cases | Qualitative all-cases statement | X1a–X1c | p. 6, §4 | No trial denominator or independent validation. |
| Documentation follows authentication | Red path and caption | F1 | p. 7 | Conceptual visual, not event log. |
| Defenses include isolation and sanitization | Proposed mitigation list | No defense experiment | p. 8, §5.2 | Effectiveness unmeasured. |
| Comparative relevance concerns exposure and tools | Combined account of web interaction and sensitive action | Analyst synthesis | pp. 1, 6 | Analyst inference; no direct standalone baseline. |

### Defensive proposals represented in compressed form

**[A] Fingerprint randomization** changes identifying browser properties to make agents harder to recognize. **[A] Input sanitization** treats retrieved material as untrusted, with examples including removing hidden elements and separating external data from instructions. **[A] Planner-executor isolation** places direct web interaction in a low-privilege component that returns structured data to a privileged planner. Source: p. 8, §5.2.1.

**[A] Anti-cloaking crawlers** vary their apparent identities to reveal targeted material; the paper cites PhishParrot as related work. **[A] Proactive deception** uses honeypot-agents to flag inappropriate requests, drawing an analogy to CHeaT while changing the protective target. Source: p. 8, §5.2.2. These are proposals or cited capabilities, not defenses evaluated by X1. In particular, an author statement that a mechanism prevents IPI should not be read as a demonstrated guarantee in this paper.

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an assistant to read a website's instructions so it can help you build an app. You open the website and see ordinary documentation. The assistant opens the same address, but the website recognizes that it is an automated agent and gives it a different page. That page says it must provide a private key before it can continue.

The danger is that the assistant may treat the website's demand as a legitimate part of your task. If it has access to the key and permission to use the necessary tools, it may take a sensitive action you never requested. The website can then provide the documentation, so the assistant still produces useful work and you may not notice the extra step.

The paper reports that this kind of attack worked in an internal demonstration using Cursor with three named model configurations. It does not tell us how many times each configuration was tested or provide detailed logs. We should therefore understand the result as a reported example of the danger, not proof that every agent always fails.

For the question about agents versus standalone language models, the important idea is that agents can encounter hostile information on their own and may have tools that act on it. That gives an attacker a possible route from a misleading webpage to a real action. This paper illustrates that route, but it does not run a direct comparison proving how much more vulnerable agents are.

## Completeness Audit

The coverage denominator is the inventory in §2 plus the substantive objectives, claims, experiment conditions, and defenses extracted from those items. All ten supplied text pages were inspected; visual inspection is explicitly limited to pages 1, 5, 6, and 7. No claim of whole-document visual inspection is made.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| M1: title/author/affiliation/arXiv label | Yes, text and image | Yes | Fully represented | Contact email omitted as non-substantive. |
| AB1: abstract | Yes, text and image | Yes | Represented in compressed form | Scope and broad consequences retained. |
| S1: Introduction | Yes | Yes | Fully represented substantively | Individual phrasing compressed. |
| SS1.1: agentic systems | Yes, text and image | Yes | Fully represented | Tools and iterative loop explained. |
| SS1.2: web attack surface | Yes; p. 2 text only | Yes | Fully represented | External-data threat retained. |
| SS1.3: fingerprinting/cloaking overview | Yes, text only | Yes | Fully represented | Historical examples compressed. |
| SS1.4: attack thesis | Yes, text only | Yes | Fully represented | Reliability assertion qualified; different-page scope retained. |
| S2: Background and Related Work | Yes, text only | Yes | Represented in compressed form | Cited findings remain author-attributed. |
| SS2.1.1: browser attributes | Yes, text only | Yes | Represented in compressed form | Header, device, and graphics categories retained. |
| SS2.1.2: agent fingerprints | Yes, text only | Yes | Fully represented substantively | Framework, extension, behavior, model, public declarations retained. |
| FN1: public bot documentation | Yes, text only | Yes | Represented in compressed form | Footnote role stated; destination unvisited. |
| SS2.1.3: cloaking techniques | Yes, text only | Yes | Represented in compressed form | User-Agent, IP, and JavaScript distinctions covered through method/background. |
| SS2.2.1: IPI | Yes, text only | Yes | Fully represented | Harmful example not treated as an instruction. |
| SS2.2.2: RAG/memory poisoning | Yes, text only | Yes | Fully represented substantively | Not misclassified as an experiment. |
| SS2.2.3: autonomous hacking | Yes, text only | Yes | Represented in compressed form | Cited capability and potential misuse retained. |
| S3: attack overview | Yes | Yes | Fully represented | Two-stage structure retained. |
| SS3.1: threat model | Yes, text only | Yes | Fully represented | Goals, capabilities, knowledge separated. |
| SS3.2.1: detection | Yes, text and image | Yes | Fully represented | Signals and missing classifier details identified. |
| SS3.2.2: cloaked delivery | Yes, text and image | Yes | Fully represented | Benign fallback and targeted branch retained. |
| SS3.3: six-step flow | Yes, text and images | Yes | Represented in compressed form | All six roles represented; illustrative scenario distinguished from X1. |
| X1 / S4: experiment | Yes, text and image | Yes | Fully represented | Setup, model labels, result, unknown conditions retained. |
| X1a–X1c: model conditions | Yes, text and image | Yes | Fully represented | No invented per-model statistics. |
| F1: attack diagram and caption | Yes, directly visual | Yes | Fully represented | Components, colors, paths, and limits discussed. |
| S5 and SS5.1: discussion/security implications | Yes, text and image | Yes | Fully represented substantively | Stealth/scale claims separated from measurements. |
| SS5.2.1: agent-side defenses | Yes, text only | Yes | Fully represented substantively | Three proposals retained; not called validated. |
| SS5.2.2: ecosystem defenses | Yes, text only | Yes | Fully represented substantively | Two proposals and implementation difficulty retained. |
| S6 and SS6.1: conclusion | Yes, text only | Yes | Represented in compressed form | Pipeline-wide security argument retained. |
| SS6.2: future work | Yes, text only | Yes | Fully represented | All four directions retained. |
| REF1: references | Yes, text only | Yes | Represented in compressed form | Roles summarized; full bibliography not duplicated. |
| Explicit formal research questions | No such item identified | Yes, absence stated | Not present in supplied material | User's question kept separate. |
| Explicit formal hypotheses | No such item identified | Yes, absence stated | Not present in supplied material | Thesis not recast as a formal test. |
| O1–O4 and central thesis | Yes | Yes | Fully represented | Informal objectives labeled. |
| Major contributions | Yes | Yes | Fully represented | Conceptual, methodological, demonstration, defensive agenda. |
| Author-stated limitations | Limited explicit material | Yes | Fully represented as available | No invented author admissions. |
| Substantive tables | None identified | Yes, absence stated | Not present in supplied material | Analyst tables are separate. |
| Major equations/theorems | None identified | Yes, absence stated | Not present in supplied material | No invented formalism. |
| Algorithms/pseudocode | No formal listing identified | Yes | Procedural flow represented | Numbered workflow covered; no source code supplied. |
| Appendices | None identified | Yes, absence stated | Not present in supplied material | No appendix review claimed. |
| Supplied supplementary material | None supplied | Yes, absence stated | Not present in supplied material | No supplement review claimed. |

### Missing or inaccessible material

Full visual renderings of pages 2–4 and 8–10 were not supplied, although their text was available. Experimental site code, detector code, exact prompts, complete page responses, tool traces, transmission records, permission settings, and repeated-run records were not supplied. The paper's external references and documentation footnote were not accessed. No appendix or supplementary file was supplied or identified as a required missing companion artifact.

### Uncertain interpretations

The meaning of experimental success is not operationally specified. The exact detector and its accuracy are unknown. The number of attempts and role of any approvals are unknown. The experimental malicious page's visual similarity to the benign response is not established. The broad full-HTML ingestion description in §3.3 does not establish the exact representation used by every tested Cursor/model configuration. The work does not establish how often agent-targeted cloaking occurs in the real world.

### Deliberately compressed material

Repeated claims about stealth, scale, and agent power were consolidated. Harmful example prompts were described rather than repeatedly reproduced. Historical cloaking examples were compressed: the source distinguishes User-Agent-based crawler handling, IP-based targeting, and JavaScript-execution differences. Bibliographic entries were inspected but not transcribed in full; named related approaches are represented according to their role in the paper. Decorative icon details, page furniture, contact information, and repeated headers were omitted as non-substantive.

### Potential omissions

No known substantive component of the supplied inventory is left without representation or an explicit accessibility/absence status. This is a bounded coverage conclusion about the supplied text and four images. It is not a claim that the original work was independently verified, every original visual page was reviewed, external references were checked, or the reported experiment was reproduced.
