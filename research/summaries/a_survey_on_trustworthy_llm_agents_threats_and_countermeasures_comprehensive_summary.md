## Stage 0 — Document Accessibility Report

The supplied work is accessible as extracted text for physical PDF pages 1–11 and as page images for pages 1–8, 10, and 11. Physical page 9 is text-only in this review. Physical PDF numbering is used throughout; the printed proceedings page numbers run from 6216 to 6226. The publication citation on physical page 2 specifies an 11-page paper, consistent with the supplied sequence. No page in that sequence is missing from the supplied text. This establishes coverage of the supplied paper, not the existence or completeness of any separate research artifacts.

The supplied images were visually inspected directly. Figures 1–6 and Table 1 are present on the rendered pages. Their overall organization, major labels, arrows, and categorical encodings are visible. Some small lettering inside the densely packed diagrams is difficult to read confidently; extracted labels and nearby prose help identify their meaning, but do not establish independent visual readability of every tiny label. Table 1's categorical checkmarks and crosses can be read from its image, whereas the extracted table text loses those symbols and some alignment. No OCR or tools were used. No native PDF, underlying images beyond those supplied, executable implementation, or external repository was opened.

Appendix A, 'Trustworthiness Definition,' is present on page 11, despite the supplied automated accessibility metadata reporting no detected appendix pages. Direct inspection takes precedence over that detection result. No separate supplementary file is supplied. The paper advertises a GitHub study collection on page 1; its contents and availability are not assessed here. No displayed mathematical equations, formal theorems, or numbered algorithms appear in the supplied paper. Code-like fragments inside Figure 4 are illustrations, not a proposed mathematical method or executable artifact reviewed here.

Evidence labels used below: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information is introduced. HIGH confidence means the relevant supplied evidence is explicit and readable; it does not independently validate the cited studies. Statements about those studies are reports of what this survey says. The supplied hash is retained as source metadata and was not independently computed.

## 1. Plain-language orientation

This paper surveys the trustworthiness of agents built around large language models, or LLMs. An LLM is the central language-processing and reasoning component. An agent adds capabilities such as remembering previous interactions, retrieving stored information, selecting tools, and acting in an environment. A multi-agent system, or MAS, connects several agents through communication and coordination. These additions make the system useful for more complicated tasks, while introducing more places where misleading information, unsafe instructions, or failures can enter. [A; pp. 1–2]

The authors organize this problem through **TrustAgent**, a survey framework. It separates internal components—brain, memory, and tools—from external relationships—with other agents, environments, and users. Within those components it examines attacks, defenses, and evaluation methods. It also distinguishes safety, privacy, truthfulness, fairness, and robustness, with additional considerations such as accountability and transparency. The central contribution is this organizing framework and its synthesis of existing work, rather than a newly tested security system. [A; pp. 1–2, 8, 11]

For the requested question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?', the survey supplies several mechanisms: extra input interfaces, retrieval from potentially corrupted memory, multi-turn accumulation of adversarial context, tool execution, environmental exposure, and communication that can spread malicious effects. Tools also allow a bad decision to become an external action. These mechanisms explain how agent capabilities can create additional security exposure. **Their combination into an answer specifically about web agents is analyst inference.** This paper is broader than web security and does not conduct its own controlled agent-versus-standalone-LLM experiment. [A/D; pp. 2–8]

Its main synthesis is that safeguards and tests designed around a model's isolated response are insufficient for the full range of agent interactions. It identifies scarce tool defenses, incomplete memory evaluation, limited direct evaluation of inter-agent interactions, and a need for dynamic testing. These are qualitative literature assessments, not measured universal vulnerability rates. [A; pp. 4–8]

## 2. Document roadmap

The document inventory is: title and author information; abstract; classification and keywords; §1 Introduction; Table 1; §2 Intrinsic Trustworthiness; §§2.1–2.3 on brain, memory, and tools; §3 Extrinsic Trustworthiness; §§3.1–3.3 on other agents, environments, and users; §4 Conclusion; references [1]–[119]; Appendix A; and Figures 1–6. There are no explicit formal research questions, hypotheses, original experimental result tables, mathematical propositions, or numbered algorithms. [A/B]

| Inventory ID | Original item | Physical pages | Function |
|---|---|---:|---|
| FRONT | Title, abstract, metadata, author footnotes | 1–2 | Establish scope and contribution |
| S1 | §1 Introduction | 2 | Motivate agent-specific trustworthiness and position the survey |
| T1 | Table 1 | 2 | Compare survey coverage |
| F1 | Figure 1 | 3 | Combine modular, technical, and dimensional taxonomy |
| S2 | §2 Intrinsic Trustworthiness | 2–6 | Organize internal component risks |
| SS21 | §2.1 Trustworthy LLM as Brain | 2–4 | Attacks, defenses, evaluation, insight |
| F2 | Figure 2 | 3 | Illustrate brain operation and security paradigms |
| SS22 | §2.2 Trustworthy Memory in Retrieval | 4–5 | Long-/short-term memory risks and safeguards |
| F3 | Figure 3 | 5 | Illustrate memory workflow and attack entry points |
| SS23 | §2.3 Trustworthy Tool for Action | 6 | Tool manipulation, abuse, defenses, testing |
| F4 | Figure 4 | 6 | Show tool-call stages and evaluation approaches |
| S3 | §3 Extrinsic Trustworthiness | 7–8 | Organize relationships with external entities |
| SS31 | §3.1 Agent-to-Agent Interaction | 7 | Cooperative/infectious attacks and defenses |
| F5 | Figure 5 | 7 | Depict communication-based attacks and graph defenses |
| SS32 | §3.2 Agent-to-Environment Interaction | 8 | Physical and digital application environments |
| F6 | Figure 6 | 8 | Contrast environments, action chains, and risks |
| SS33 | §3.3 Agent-to-User Interaction | 8 | Discuss trust calibration and transparency |
| S4 | §4 Conclusion | 8 | Restate taxonomy and research gaps |
| REF | References [1]–[119] | 9–11 | Identify cited works; not their complete evidence |
| A1 | Appendix A: Trustworthiness Definition | 11 | Define dimensions and give examples |

The repeated attack–defense–evaluation–insight structure applies to the brain, memory, tools, and inter-agent sections. The environment section deliberately uses application categories because the authors consider existing solutions fragmented. The user section synthesizes interaction concerns without duplicating the earlier catalogs. [A; pp. 2, 7–8]

The original title is **A Survey on Trustworthy LLM Agents: Threats and Countermeasures**. Its authors are Miao Yu, Fanci Meng, Xinyun Zhou, Shilong Wang, Junyuan Mao, Linsey Pan, Tianlong Chen, Kun Wang, Xinfeng Li, Yongfeng Zhang, Bo An, and Qingsong Wen. It appears in the Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2, KDD '25, August 3–7, 2025, Toronto, Canada, with DOI 10.1145/3711896.3736561. Keywords are LLM-based Agent, Multi-agent System, and Agent Safety. Yu and Meng are identified as equal contributors; Li and Wen as corresponding authors. Affiliations, email addresses, permissions, and repeated running headers are bibliographic material and are compressed here. [A; pp. 1–2]

## 3. Background and context

The paper's system model centers on an LLM **brain**: the component that reasons, makes decisions, and integrates information from other modules. An agent's additional components provide memory, action, and interaction. This is a functional decomposition, not a single implementation that every surveyed system necessarily follows. [A/D; pp. 2–3]

**Long-term memory** stores information that may later be retrieved. The paper associates it with **retrieval-augmented generation**, or RAG: retrieving relevant stored material to support generation. A **vector database** stores searchable numerical representations, called embeddings, of information. **Short-term memory** retains current dialogue context or task logs. The same persistence that helps an agent continue a task can preserve malicious content or accumulate a harmful sequence across turns. [A; pp. 4–5]

A **tool** is a means of obtaining information or acting outside the central model: examples include a search engine, application programming interface, sensor, robot, or interface-control mechanism. An **application programming interface**, or API, exposes callable functionality. Tool use involves planning, selection, and execution, each of which can introduce attack interfaces. [A; p. 6]

A **jailbreak** attempts to bypass the brain's aligned safeguards with adversarial prompts. **Prompt injection** places malicious instructions where the agent may encounter them, attempting to override its intended instructions. **Indirect prompt injection** reaches the system through retrieved or external material rather than only a direct user request. A **backdoor** associates triggers with malicious behavior; the survey discusses both compromised outputs and compromised intermediate reasoning. These mechanisms overlap with the location of the attack: for example, a poisoned memory item may carry a prompt injection. [A/D; pp. 3–5]

Appendix A defines **safety** around preventing harmful actions; **privacy** around protecting data and autonomy; **truthfulness** around accurate information; **fairness** around impartial treatment and equitable resources; and **robustness** around stable behavior under adversarial or uncertain conditions. These categories are related rather than mutually exclusive: a malicious tool call can harm privacy, safety, and robustness simultaneously. That cross-category reading is an analyst interpretation of the taxonomy. [A/D; p. 11]

## 4. Research problem and gap

**Existing problem.** Adding memory, tools, environments, and other agents expands what an LLM-based system can do and the information it processes. The authors state that this expands the attack surface and complicates trustworthiness evaluation. The relevant security object becomes the interacting system rather than only the core model. [A; pp. 1–2]

**Attributed shortcomings of earlier work.** The introduction says earlier trustworthy-LLM surveys emphasize alignment standards or evaluation perspectives, while some agent surveys concentrate on security/privacy or the LLM brain. The authors argue that this misses challenges from additional modules and MAS interactions. These are their assessments of prior literature; the supplied paper does not independently reproduce all earlier surveys' analyses. [A; p. 2]

**Research gap.** A component-aware synthesis is needed that relates attacks, defenses, and evaluations across single LLMs, individual agents, and MAS, and across several meanings of trustworthiness. Table 1 supports this positioning by coding survey coverage, not by measuring which taxonomy produces better security outcomes. [A/B; p. 2]

**Motivation and scope.** The authors seek to guide development and future research by distinguishing the mechanisms and risks of each component. Their scope includes physical settings such as robotics and digital settings such as networks, healthcare, and social media. It therefore supports a web-agent security discussion only as one application of a larger framework. [A/D; pp. 2, 8]

**Boundary.** The paper's statement 'MAS > Single Agent > LLM' is a cited performance hierarchy. It is not a measured security hierarchy, a universal theorem, or a numerical estimate of additional agent risk. Capability and security exposure should not be conflated. [A/D; p. 2]

## 5. Research questions, objectives, and hypotheses

No formally numbered research questions or testable hypotheses are stated. The following are author objectives, reconstructed from their explicit contribution and framework descriptions rather than invented experimental questions. [A; pp. 1–2]

1. Extend trustworthy-LLM discussion to agents and MAS by decomposing their internal components and external relationships.
2. Organize existing techniques for compromising, protecting, and evaluating those components.
3. Cover multiple trustworthiness dimensions, with definitions in Appendix A.
4. Identify module-specific vulnerabilities and future research directions.

The user-supplied research question is separate: **Why are web AI agents more vulnerable than standalone LLMs?** This review uses it as an analytical lens. The survey explicitly contrasts some agent interactions with static or single-LLM settings and reports a cited sandbox study finding higher risk with tool access. It does not itself perform a matched empirical comparison of web agents and standalone LLMs. Its strongest relevance is explanatory: it identifies added pathways through which risk can arise. [A/D; pp. 3–6]

## 6. Assumptions / Threat Model

The survey contains multiple threat models distributed across its categories, rather than one formal adversary with a fixed budget and permissions. Its broad system model is a reasoning brain connected to memory, tools, and external interactions. The assets discussed include private data, intended task behavior, safe tool execution, correct information, communication integrity, resource availability, and user trust. [A/D; pp. 2–8, 11]

| Attack setting | Access or capability described | Asset or behavior at risk | Important condition |
|---|---|---|---|
| Brain jailbreak | Adversarial direct or multi-turn prompts | Safeguards and intended responses | Successful bypass is attack-specific |
| Indirect injection | Malicious content in retrieved or external inputs | Task adherence and reasoning | Content must be encountered and influence the brain |
| Brain backdoor | Trigger insertion associated with training or compromised behavior | Outputs or intermediate reasoning | Different access from ordinary input-only attacks |
| Memory poisoning | Inject malicious material into long-term storage | Future retrieval and truthfulness | Relevant retrieval helps activate the attack |
| Memory privacy attack | Queries or embedding-related access | Stored private information | Access differs across cited techniques |
| Memory misuse | Crafted sequence retained across turns | Safety alignment | Depends on dialogue context or distributed triggers |
| Tool manipulation | Influence planning, selection, commands, or tool set | Sensitive or malicious execution | Requires usable tool interfaces |
| Tool abuse | Use agent capabilities against outside entities | External systems and resources | Agent has relevant tools and task capability |
| Inter-agent attack | Malicious participants or manipulated communication | Coordination, truthfulness, availability | Communication enables influence or spread |

The brain attack section excludes misalignment attacks that modify internal model parameters on the grounds that attackers typically lack such access. However, it also reviews training-associated backdoors. This is a scope tension: it should not be flattened into a claim that every surveyed attack assumes a fully black-box adversary. The paper does not unify these permissions. [A/D; pp. 3–4]

The survey does not specify a universally trusted tool registry, a trusted memory writer, fixed user authorization rules, attacker knowledge, maximum poisoned-document fraction, or a common number of compromised agents. Defenses introduce guard models, guard agents, or graph detectors, but there is no general proof that those components are trusted or immune to compromise. These are absent specifications, not demonstrated defense failures. [D; pp. 4–7]

## 7. Methodology

This is a **qualitative, taxonomy-driven survey of AI security and trustworthiness**, not a new experiment or meta-analysis. Its method is to explain each component's role, group the relevant literature by mechanism, describe representative studies, and draw module-specific insights. The main organizing axes are modular location, technical purpose, and trustworthiness dimension. [A; pp. 1–2]

The modular axis has three internal components—brain, memory, tool—and three external relationships—agent, environment, user. The technical axis emphasizes attack, defense, and evaluation. The dimensional axis explicitly names five core dimensions, while Figure 1 and Appendix A also retain an 'Others' category. Thus 'five core dimensions' does not mean the authors exclude accountability, ethics, transparency, or explainability. [A/B; pp. 2–3, 11]

For literature-review reproducibility, important details are **not supplied**: search databases, search strings, search dates, eligibility criteria, screening procedure, reviewer agreement, a study-selection flowchart, and a formal quality/risk-of-bias assessment. The reference list ends at [119], but that is not a documented count of unique eligible studies or independently screened experiments. Duplicate and versioned entries further prevent interpreting the final reference number as a systematic-review sample size. [B/D; pp. 9–11]

No common dataset, train/validation/test split, preprocessing pipeline, annotation protocol, model version, hyperparameter set, hardware configuration, random seed, replication count, statistical test, confidence interval, or significance threshold is reported for an original TrustAgent experiment. This is appropriate to recognize as the nature of the contribution; those fields cannot be filled from the named methods' titles. [B/D]

The advertised repository is a categorized collection of surveyed studies. Its contents, revision, licensing, and reproducibility support are unknown in closed-document mode. The paper's taxonomy and prose are the evidence used here. [A; p. 1]

### Component-level extraction

**Brain attacks:** jailbreak, prompt injection, and backdoor. The survey discusses optimized adversarial suffixes, agent-generated multi-round jailbreaks, privacy-oriented attack agents, collaborative jailbreak optimization, image-mediated infectious attacks, retrieved malicious instructions, multimodal perturbations, and backdoors affecting outputs or intermediate reasoning. [A; pp. 3–4]

**Brain defenses:** alignment through training/reward or feedback mechanisms; single-model filters monitoring input/output; and multi-agent shields using debate, review, or role-specialized collaboration. Examples include StruQ, ShieldLM, GuardAgent, AgentGuard, and AutoDefense. These are technique families, not a head-to-head ranking. [A; p. 4]

**Memory defenses:** detection of suspicious retrieved content; prompt modification to discourage leakage or rewrite risky requests; and output intervention. TrustRAG uses K-means clustering on retrieved embeddings; another cited approach uses Mahalanobis-distance thresholds. RobustRAG's isolate-then-aggregate method produces separate responses for retrieved passages and combines them, with the stated favorable condition that malicious passages are a minority. No numerical threshold or certified bound is supplied here. [A; p. 5]

**Tool defenses:** GuardAgent executes guardrail code through APIs for task plans; AgentGuard identifies unsafe tool workflows and generates constraints. The authors describe this area as notably sparse. [A; p. 6]

**Inter-agent defenses:** collaborative debate, voting, auditing, filtering, and adversarial interaction; or topology-based methods that change communication structure and detect anomalies in discourse graphs. The survey names GPTSwarm and G-Safeguard in the latter category. [A; p. 7]

## 8. Experiments / Analyses

There are no original TrustAgent experiments to register. The following register separates its substantive literature analyses and cited evaluation approaches. Setups and outcomes remain the survey's descriptions; underlying study protocols were not supplied. [A/D]

| Analysis ID | Purpose and material | Conditions or measures | Main outcome and caveat |
|---|---|---|---|
| X1 | Compare TrustAgent with prior surveys, Table 1 | Object, multiple dimensions, modularity, techniques, MAS | Positions coverage; no security performance test |
| X2 | Synthesize brain security, §2.1 | Attack families; focused versus broad evaluation | Interaction increases interfaces; benchmark descriptions are heterogeneous |
| X3 | Synthesize memory security, §2.2 | Poisoning, leakage, misuse; retrieval and attack metrics | Persistent/retrieved data create risks; no pooled effect size |
| X4 | Synthesize tool security, §2.3 | Manipulation versus abuse; static data versus sandbox | Action interfaces introduce risk; defenses described as scarce |
| X5 | Synthesize inter-agent security, §3.1 | Cooperation, infection, graph defenses | Communications can amplify harm; direct interaction-specific evaluation remains limited |
| X6 | Review environments, §3.2 | Physical versus digital applications | Risks depend on roles and constraints; no shared workload |
| X7 | Review user interaction, §3.3 | Trust calibration, personalization, explanation | Identifies interaction gaps; no user experiment reported |
| X8 | Define trustworthiness, Appendix A | Five core dimensions plus other concerns | Conceptual guidance; not an operational measurement instrument |

**Focused brain assessments** include InjecAgent and AgentDojo for indirect prompt injection, AgentBackdoorEval for backdoor scenarios, RedAgent for context-sensitive red teaming, and RiskAwareBench for physical risk awareness. **General assessments** include S-Eval, BELLS, Agent-SafetyBench, Agent Security Bench, AgentHarm, and R-Judge. The survey does not give common models, controls, or scores across them. [A; p. 4]

**Memory evaluation** includes attack success rate and retrieval effectiveness. PoisonedRAG is described as using precision, recall, and F1-score for malicious-text retrieval. AgentPoison uses retrieval attack success rate, ASR-r. Other work quantifies retrieved private data; RAG-Thief uses chunk recovery rate and semantic similarity. These measure different stages and outcomes, so one must not treat a retrieval rate as a final harmful-action rate. [A/D; p. 5]

**Tool dataset testing** uses adversarial queries and tool-invocation cases. ToolSword covers input attacks, execution-time misdirection/risky cues, and output feedback/error conflicts. InjecAgent tests indirect injections during tool use. **Sandbox simulation** instead models interactive execution: ToolEmu uses an LLM emulator and an LLM evaluator; HAICosystem uses role-playing simulations and scenario-specific checklists. The survey reports higher tool-agent risk from HAICosystem but supplies no magnitude, uncertainty, or matched condition table. [A; p. 6]

**Inter-agent evaluation** names SafeAgentBench/SafeAgentEnv, R-Judge, and JAILJUDGE, while subsequently stating that research strictly focused on evaluating inter-agent interactions was not found. This distinction is best preserved: broadly relevant agent or multi-agent evaluation exists, but the authors identify a narrower interaction-specific gap. It is not evidence that no agent benchmark exists. [A/D; p. 7]

## 9. Results

The paper's results are conceptual synthesis and research-gap identification. It contains no original accuracy, attack success, latency, cost, or defense improvement measurements. [B]

**Finding 1: more interaction creates more entry points.** The brain receives textual and visual inputs from internal and external modules. The authors explicitly connect this information flow to additional attacker interfaces. This supports a mechanism-based explanation of agent exposure, not a quantified probability that a particular agent will be compromised. [A; pp. 2–3]

**Finding 2: memory creates persistence and accumulation.** Long-term poisoning can continue influencing generation until removed; short-term memory can retain a sequence that gradually bypasses alignment or distributes backdoor triggers. Relevant retrieval and dialogue history are important conditions. [A; pp. 4–5]

**Finding 3: tools connect reasoning errors to actions.** Planning, selection, and execution expose attack interfaces, and tool abuse can target external entities. The survey discusses websites and real-world systems, but reports no matched browser-agent risk ratio. [A; p. 6]

**Finding 4: communication can propagate compromise.** Cooperative attacks coordinate malicious agents; infectious attacks spread malicious effects through messages or multimodal material. CORBA is described as resource-draining and self-propagating; image-based attacks are described as contagious. Network structure can also be used defensively. [A; p. 7]

**Finding 5: evaluation coverage is uneven.** Static datasets are criticized for failing to capture dynamic interactions; memory evaluation lacks systematic reliable benchmarks in the authors' assessment; tool defense research is scarce; direct inter-agent evaluation is underdeveloped. These claims are literature judgments without a documented systematic search denominator. [A/D; pp. 4–7]

**Finding 6: user trust is part of the security problem.** The user section emphasizes dynamic trust adjustment, explanation, privacy, personalization risks, and the limited treatment of multi-agent trust dynamics. It does not provide measured user susceptibility or trust-calibration effectiveness. [A; p. 8]

The numerical facts on page 4 describe benchmarks: AgentHarm has 110 explicitly malicious tasks; R-Judge covers 27 risk scenarios; S-Eval has four hierarchical levels and eight risk dimensions. These are scope descriptors from different cited resources. They are not sample sizes from one experiment and cannot be combined into an overall agent-risk estimate. [A]

## 10. Figure-by-figure interpretation

### Figure 1 — TrustAgent taxonomy, page 3

**Purpose and panels.** This is a three-part conceptual diagram: trustworthiness dimensions at left, technical categories in the middle, and system modules/relationships at right. It is not a statistical plot. There are no axes, units, scales, uncertainty bars, or measured values. [B]

The left panel uses separate boxes for safety, privacy, truthfulness, fairness, robustness, and other concerns. The listed examples include unsafe action chains, password theft, misinformation, resource monopolization, interaction fragility, and accountability. These examples illustrate breadth; they are not a frequency distribution or a validated exhaustive list. [A/B]

The middle panel uses red for attack, green for defense, and blue for evaluation. It maps brain attacks to jailbreak/injection/backdoor; memory attacks to poisoning/leakage/misuse; tool attacks to manipulation/abuse; and inter-agent attacks to infection/cooperation. Defense entries include alignment, filters, multi-agent shields, memory interventions, and topological/cooperative approaches. Some remaining modules are labeled undeveloped. That graphic shorthand should not be strengthened into a measured absence of all related research. [A/B]

The right panel shows memory storage/retrieval, an LLM brain, and tools for action, connected to agents/MAS and external relationships. External boxes cover other agents, users, and environments. Arrows communicate interactions and information exchange rather than numerical causal weights. Small model/framework names serve as examples, not evaluated baselines. [B]

### Figure 2 — Brain workflow and security paradigms, page 3

The upper-left material illustrates reasoning and decision structures, including chain-like and branching thought paths, with methods leading toward a final goal. The attack panel contrasts benign versus adversarial prompts, injected data, and backdoor-related behavior. Its defensive panel shows alignment, input/output filtering, and collaborative guarding. Its evaluation panel contrasts focused assessments with general benchmarks spanning task areas. [A/B]

Red/green/blue again distinguish attack/defense/evaluation. No plotted score or relative effect size is encoded. The figure's value is in locating interventions around the brain: prompts and observations enter, reasoning produces an output or decision, and monitoring can occur before or after processing. Fine labels in this dense image are less confidently readable than its main structure. The adjoining §§2.1.1–2.1.3 provide the reliable detail. [B]

### Figure 3 — Memory workflow and attack points, page 5

The workflow panel shows a query being embedded and used for retrieval from long-term memory; retrieved context helps construct a prompt, a response is produced, and dialogue memory is updated. Short-term dialogue memory forms a separate continuity path across interaction. [B]

The red attack panel distinguishes poisoned stored text leading to a wrong answer, retrieval of private information leading to a privacy-bearing response, and a multi-turn sequence ending in an unsafe response after earlier safe ones. The green defense panel groups detection, prompt modification, and output intervention; blue evaluation labels distinguish attack success from retrieval success. [A/B]

This is a process diagram without numerical axes or estimated rates. The safe-to-unsafe sequence illustrates an attack pattern, not the number of turns needed in general. Exact retrieval outcomes or defense effectiveness cannot be inferred from arrow placement. The prose explicitly supplies the minority-malicious-passage condition for the isolate-then-aggregate example. [A/B; §2.2.2]

### Figure 4 — Tool calling and security evaluation, page 6

The upper workflow connects tool documentation—name, description, parameter, and example—to planning, selection, and execution. Tool examples include arithmetic, a string-counting code fragment, and retrieval of HTML/text. These illustrate different tool functions rather than benchmark correctness results. [B]

The red panel places attacks around tool selection, injected tool content, forged commands, and malicious tasks. Its tool-misuse illustration contrasts a refused hacking request without tool action with an action path affecting a server. This supports the distinction between generating content and executing consequential behavior, but is schematic rather than an experiment with a measured success rate. [A/B]

The green defense panel lists verified API, proper call, safe use, and direct return. The blue evaluation panel contrasts constructed datasets with sandbox simulation involving tasks, tools, environments, simulated action, and evaluators. No axes, units, or confidence intervals occur. The diagram uses 'Tool Misuse,' while the prose names the broader category 'Tool Abuse'; these related labels should not be mistaken for independently tested categories. [A/B]

### Figure 5 — Agent-to-agent threats and defenses, page 7

The upper red panel contrasts cooperative attacks, where malicious agents coordinate against a target, with infectious attacks, where harmful text or images compromise additional agents. The lower green panel contrasts collaborative defense with topological defense. [B]

Collaborative defense shows an initial response entering a group process involving debate, detection, voting, or auditing, producing a conclusion and revised safe response. Topological defense shows an initial network, classification/detection, and pruning toward a safer topology. Agent colors distinguish benign and malignant roles. A graph neural network is shown as a detector using conversational context. [A/B]

The arrows depict information flow and intervention, not a measured propagation probability. Network layouts are illustrations, not a specified production graph or a controlled topology comparison. No exact detection score, pruning cost, or remaining attack success is labeled. [B]

### Figure 6 — Environments and action chains, page 8

This figure separates physical applications—robotics, autonomous driving, industrial control—from digital applications including network, healthcare, finance, and social media. It depicts tools as the bridge through which agents interact with environments. [B]

A physical example follows perception, planning, and pulling over, with risks such as poor visibility and sudden obstacles. A digital shopping example follows website visit, registration, and purchase, with phishing, password leakage, and an unwanted product as potential risks. These are author illustrations, not reported incidents or measured failure frequencies. [A/B]

A risk panel groups outcomes such as stolen money, rumor spread, accidents, and machine failure; a mitigation panel lists approaches such as fine-tuning, reasoning, and workflow changes. The arrows show multistage dependencies: an unsafe observation or decision can affect subsequent action. There are no axes, units, scales, numerical comparisons, or error bars. [B]

## 11. Table-by-table interpretation

### Table 1 — Comparison between TrustAgent and other surveys, page 2

The table compares seven cited surveys with TrustAgent. Columns describe the object of study, multi-dimensional coverage, modular organization, technical scope, and MAS coverage. Checkmarks and crosses encode categorical coverage judgments. There are no numerical units, uncertainty estimates, statistical tests, or performance scores. [A/B]

| Survey row | Object | Multi-dimensional | Modular | Techniques | MAS |
|---|---|---|---|---|---|
| Liu et al. [55] | LLM | Yes | No | Attack/Evaluation | No |
| Huang et al. [37] | LLM | Yes | No | Evaluation | No |
| He et al. [34] | Agent | No | No | Attack/Defense | No |
| Li et al. [51] | Agent | Yes | No | Attack | No |
| Wang et al. [79] | Agent | No | No | Attack | No |
| Deng et al. [21] | Agent | No | Yes | Attack/Defense | Yes |
| Gan et al. [28] | Agent | Yes | No | Attack/Defense/Evaluation | No |
| TrustAgent | LLM + Agent | Yes | Yes | Attack/Defense/Evaluation | Yes |

The check/cross transcription is based on the supplied visual, because extracted text omits the symbols. The footnotes expand Atk, Def, and Eval as attack, defense, and evaluation, and MAS as multi-agent system. [B]

The table supports the authors' claim that their survey combines features not jointly marked for the other rows. Gan et al. already receive all three technique categories; Deng et al. already receive modular and MAS coverage. Therefore the novelty claim concerns the combination and organization of coverage, not exclusive invention of each individual feature. Calling TrustAgent the 'best' survey would exceed what the table demonstrates: no quality score or independent validation rubric is given. [A/D]

## 12. Diagram / Architecture

All six figures are conceptual diagrams, already individually audited above. This section connects them into the survey's system-level interpretation rather than repeating their captions.

An agent's information path runs from user tasks and environmental observations to retrieval and brain processing, then to selected tools and external action. Long-term memory supplies retrieved context; short-term memory carries dialogue or task history forward. External outcomes can become later observations, creating repeated interactions. Other agents add communication paths around this loop. [A/B; Figures 1–6]

Attack categories correspond to different intervention points along these paths. Prompt injection changes information encountered by the brain; memory poisoning changes material available for later retrieval; tool manipulation changes which action interface is used or how; infectious attacks exploit messages that influence additional agents. Tool abuse is different in emphasis: the agent itself becomes a means of attacking an external target. [A/D; §§2.1–3.1]

Defense categories similarly sit at different points: alignment influences the brain's behavior, input/output monitors examine exchanged content, memory defenses filter or rewrite retrieved/query material, tool guards check plans or calls, and graph defenses alter or monitor communication. The figures do not establish that combining these defenses yields a particular security guarantee. [A/B/D]

**Analyst interpretation for web agents:** a browser-oriented task can combine several of these paths at once: web-derived input, task history, tool decisions, and external actions. The survey's separate examples make that interpretation plausible, but it does not provide a unified browser-agent architecture with specified permissions and verified end-to-end protection. [D; pp. 3–8]

## 13. Equations and mathematical concepts

No displayed research equations, losses, proofs, theorems, or formal security bounds are supplied. Consequently, there are no equation symbols or proof dependencies to reconstruct. The paper's main technical objects are categories, workflows, and named evaluation measures. [B]

The expression 'MAS > Single Agent > LLM' on page 2 is the authors' cited capability/performance ordering, not a quantified equation. No task distribution or numerical margin accompanies it. [A]

The memory section names **precision, recall, and F1-score**, but does not give their equations, exact positive-class definitions, or reported values. It names **attack success rate (ASR)**, **retrieval ASR (ASR-r)**, **chunk recovery rate (CRR)**, and **semantic similarity (SS)**. Their qualitative roles are described, but denominators and implementation choices are not fully specified in this survey. No external metric formulas are inserted here. [A; p. 5]

**K-means clustering** is reported as grouping retrieved embeddings for suspicious-document detection. **Mahalanobis distance** is reported as a query-document distance used with a filtering threshold. The survey supplies no distance formula, covariance specification, cluster count, or numerical cutoff. **Graph neural networks (GNNs)** are named for discourse-graph anomaly detection. **Linear Temporal Logic** is named for a robotics constraint module. Formal semantics and training details are not provided. [A; pp. 5, 7–8]

Reasoning acronyms such as chain of thought, tree of thought, and graph of thought appear in the figures, but their algorithms are not developed. Code-like arithmetic and string-counting examples in Figure 4 illustrate tools rather than a paper-specific algorithm. [B]

## 14. Interpretation and discussion

The paper's conceptual answer is that agent trustworthiness depends on interfaces and interactions as well as on the core model. An LLM brain may be exposed to more sources of information; memory preserves those influences; tools turn decisions into actions; and communication can multiply their effects. This connects the authors' component analyses without treating every module as equally risky in every deployment. [A/D]

For web-agent security, this yields four useful distinctions. First, **entry-point expansion** concerns where an attacker can place influential content. Second, **persistence** concerns whether malicious content remains available across retrievals or turns. Third, **action consequence** concerns what the agent can do after being misled. Fourth, **propagation** concerns whether compromised behavior can influence other agents. These four analytical labels are this review's synthesis, not a named taxonomy in the paper. [D]

The evidence is strongest for identifying plausible and surveyed mechanisms. It is weaker for establishing their relative frequency, comparative severity, or combined risk. There is no common experimental baseline that isolates the added effect of memory, tools, environment, or multiple agents while holding the underlying LLM constant. The paper therefore supports 'additional vulnerabilities and potentially greater consequences,' but not 'all web agents are always more vulnerable by a known amount.' [D]

Several source inconsistencies affect confidence in details. Page 5 calls ASB [106] a memory-detection example, whereas the reference list identifies [106] as Agent-SafetyBench and [102] as Agent Security Bench. Page 6 prints 'InjectAgent [98],' whereas the bibliography names Injecagent. The web-attack paragraph attributes both autonomous website hacking and one-day vulnerability exploitation to [24], whose supplied title concerns autonomous website hacking. These issues do not erase the high-level taxonomy, but underlying-study attribution should remain provisional. [B/D]

The text also describes all-dimensional coverage while its detailed catalogs primarily emphasize security, privacy, and robustness-related mechanisms. Appendix A supplies broader fairness and accountability examples, but no balanced evidence counts by dimension. That is an analyst observation about presentation, not an author-admitted failure. [D]

## 15. Contributions and novelty

**Conceptual contribution:** a modular view connecting three intrinsic components and three extrinsic relationships. This helps prevent reducing agent security to prompt behavior alone. [A; pp. 1–2, 8]

**Methodological contribution:** a technique-oriented organization of attacks, defenses, and evaluation, applied repeatedly to major components and paired with five core trustworthiness dimensions. The environment section adapts the organization to physical/digital settings. [A; pp. 2–8]

**Synthesis contribution:** representative methods are grouped into mechanisms such as memory poisoning, tool manipulation, cooperative attack, and topological defense. The paper also identifies component-specific gaps and future directions. [A]

**Resource contribution:** the authors advertise an online categorized study collection. Its contents are not reviewed. No new dataset, benchmark implementation, trained model, algorithmic security guarantee, or original measured defense improvement is established by the supplied paper. [A/B]

The word 'TrustAgent' also appears in reference [36], whose title is a different cited work. This report uses TrustAgent to mean the present survey framework unless explicitly referring to a reference. Name overlap is not evidence that the survey itself implements the cited system. [B/D; pp. 1, 9]

## 16. Limitations

### Authors' stated limitations and field gaps

The authors identify static datasets as insufficient for the brain's dynamic external interactions (§2.1.4); memory attacks as often task- or context-specific and poorly generalizing (§2.2.4); memory evaluation as lacking systematic reliable benchmarks (§2.2.3–2.2.4); tool defense research as notably scarce (§2.3.2); and tool chains as a growing challenge (§2.3.4). [A; pp. 4–6]

They describe agent-to-agent evaluation as immature and report not finding research strictly focused on evaluating those interactions (§3.1.3–3.1.4). Environment solutions are characterized as fragmented and lacking a systematic framework (§3.2). User-interaction research is said to overlook how users adjust trust, with multi-agent trust dynamics largely unexplored (§3.3). [A; pp. 7–8]

These are predominantly limitations of the surveyed research field. The paper does not provide a separate formal limitations section evaluating its own review procedure. That distinction matters: one should not attribute the analyst's methodological concerns below to the authors. [B/D]

### Additional evidence-based analyst observations

The absence of a reported search/screening protocol limits reproducibility and makes coverage bias difficult to assess. No formal study-quality assessment distinguishes stronger evidence from illustrative claims. Heterogeneous threat models are discussed together without a common attacker capability model. No pooled effect estimate or controlled comparison establishes how much additional risk an agent module creates. [D]

Bibliographic duplicates, some mismatched references, and terminology variation lower confidence in selected study-specific descriptions. Fine diagram labels cannot all be independently read at the supplied size. The paper's repository and underlying cited papers were not supplied or reviewed, so detailed experimental conditions cannot be recovered from them. [B/D]

## 17. Threats to validity

The following validity labels are analyst assessments, not headings or formal claims used by the authors.

**Internal validity:** there is no original causal experiment to evaluate. More importantly, the survey cannot isolate whether a reported problem arose from the underlying LLM, the added module, permissions, task difficulty, or the tested defense. [D]

**Construct validity:** trustworthiness spans several different outcomes. Correct information, refusal of harmful requests, successful safe action, privacy protection, and stable multi-agent coordination are not interchangeable measurements. A retrieval attack metric or judge score does not automatically measure end-to-end web security. [D; §§2.1.3–3.1.3, Appendix A]

**External and ecological validity:** static prompts, emulated tools, role-playing sandboxes, physical robots, and digital workflows represent different environments. The survey itself argues for more dynamic evaluation. Neither an LLM-emulated sandbox nor one domain-specific benchmark automatically establishes deployment-wide risk. [A/D; pp. 4, 6, 8]

**Statistical conclusion validity:** the paper supplies no pooled statistics, confidence intervals, or original effect sizes. Statistical superiority of a defense or a universal vulnerability ordering cannot be inferred. The benchmark sizes on page 4 characterize coverage, not a combined statistical test. [D]

**Reproducibility and generalizability:** missing review search details and inaccessible underlying protocols constrain reproduction of the synthesis. An attack requiring write access to memory cannot automatically be generalized to an agent whose memory writes are inaccessible to that adversary. Conversely, an agent with no multi-agent communication does not acquire an infectious communication channel merely because the taxonomy contains one. These are conditional readings of the survey's mechanisms. [D]

## 18. Future work and open questions

### A. Explicitly proposed by the authors

For the brain, develop collaborative mechanisms through which agents monitor and validate each other's actions, and dynamic evaluations that better simulate changing external interactions. [A; p. 4]

For memory, improve protection at the vector-database end, use privacy measures such as query rewriting or fine-tuning, develop multi-round adversarial dialogue training, and establish reliable benchmarks for poisoning, leakage, and misuse. [A; p. 5]

For tools, review tools before integration, simulate execution in isolation before actual use, develop attacks reflecting tool characteristics, and extend research from single calls to chains of calls. These are proposed directions, not defenses validated by this paper. [A; p. 6]

For inter-agent systems, study automated targeted infectious attacks, anti-propagation defenses, topology-based approaches, and dynamic LLM/agent detectors and evaluators. For users, develop adaptive trust calibration and better feedback mechanisms while addressing multi-agent trust dynamics. [A; pp. 7–8]

### B. Additional open questions from this analysis

How much risk does each added web-agent capability contribute when the underlying LLM, tasks, and permissions are held constant? Which entry points are actually available to an attacker in a particular deployment? Can a defense reduce harmful execution without merely preventing legitimate task completion? How should experiments separate initial injection, retrieval, execution, and propagation success? [D]

How can evaluators measure both private-data exposure and action consequences across a full multi-step workflow? How robust are guard agents or graph detectors when the information they inspect is itself adversarial? These questions follow from the architecture and evaluation gaps; they are not new findings established in this survey. [D]

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| LLM | Large language model; the agent's central language/reasoning component |
| Agent | LLM-based system with added memory, tools, or environmental interaction |
| MAS | Multi-agent system; several interacting agents |
| Brain | Core reasoning and decision-making module |
| Intrinsic trustworthiness | Trustworthiness of brain, memory, and tools |
| Extrinsic trustworthiness | Trustworthiness of interaction with agents, environments, and users |
| RAG | Retrieval-augmented generation; generation supported by retrieved material |
| Embedding | Numerical representation used to store or retrieve information |
| Long-term memory | Persistently stored information available for retrieval |
| Short-term memory | Current dialogue context or task history |
| Jailbreak | Attempt to bypass aligned safeguards using adversarial prompts |
| Prompt injection | Malicious instructions embedded in information encountered by the system |
| Backdoor | Trigger-linked malicious behavior, including output or reasoning changes |
| Memory poisoning | Malicious stored content that can influence later retrieval/generation |
| Embedding inversion | Attempt to reconstruct source information from its embedding |
| Memory misuse | Exploiting retained dialogue/history to bypass safety |
| Tool manipulation | Inducing malicious behavior through tool-call stages |
| Tool abuse | Using agent tool capabilities to attack outside entities |
| Cooperative attack | Multiple malicious agents coordinate to compromise behavior |
| Infectious attack | Malicious effects spread through interactions to other agents |
| Alignment | Shaping behavior toward human values or constraints |
| Guardrail agent | Agent that checks plans, actions, or constraints for another agent |
| Multi-agent shield | Collaborative agents used to improve a target's trustworthiness |
| Topological defense | Protection using the structure of communication connections |
| GNN | Graph neural network; named for detecting discourse-graph anomalies |
| Sandbox simulation | Controlled or emulated interaction used to examine risks |
| API | Application programming interface; callable external functionality |
| ASR / ASR-r | Attack success rate / retrieval attack success rate |
| CRR / SS | Chunk recovery rate / semantic similarity in data-theft evaluation |
| CoT | Chain of thought; sequential intermediate reasoning shown conceptually |
| Trust calibration | Adjusting a user's trust in response to agent behavior |

Names such as AutoGen, MetaGPT, ChatDev, and particular reasoning structures appear as examples. The paper does not define every depicted acronym or fully document those frameworks. Their names are not treated as additional reviewed implementations. [B]

## 20. Key numerical results

This table distinguishes structural counts and benchmark descriptions from original measured results. No defense improvement percentages, comparative vulnerability ratios, or error bars are supplied.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Paper length | 11 | pages | Publication citation; supplied physical sequence | Author-reported | p. 2 |
| Core agent components/relationships | 6 | categories | Brain, memory, tools; agents, environment, users | Author-reported | p. 8, §4 |
| Core trustworthiness dimensions | 5 | dimensions | Safety, privacy, truthfulness, fairness, robustness; Others also retained | Author-reported | p. 2; p. 11 |
| AgentHarm size | 110 | explicitly malicious tasks | Evaluation of agent misuse across harmful categories | Author-reported | p. 4, §2.1.3 |
| R-Judge coverage | 27 | risk scenarios | Multi-turn agent interaction records | Author-reported | p. 4, §2.1.3 |
| S-Eval hierarchy | 4 | hierarchical levels | Multi-dimensional, open-ended safety evaluation | Author-reported | p. 4, §2.1.3 |
| S-Eval coverage | 8 | risk dimensions | Same benchmark description; not eight agent modules | Author-reported | p. 4, §2.1.3 |
| Prior-survey rows in Table 1 | 7 | rows | Liu, Huang, He, Li, Wang, Deng, Gan | Analyst-derived: counted named rows | p. 2, Table 1 |
| Total substantive figures | 6 | figures | Numbered Figures 1–6 | Analyst-derived: counted identifiers | pp. 3, 5–8 |
| Reference identifier range | 1–119 | numbered entries | Includes duplicate/versioned records; not unique study count | Visually readable/text-readable | pp. 9–11 |

There are no approximate numerical estimates from figure positions because the figures are conceptual diagrams. The 'one million' phrase in the title of reference [31] is not promoted into a validated survey result: the main discussion reports exponential infectious spread without supplying that study's experimental conditions. [A/D; pp. 3, 9]

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Analysis | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Added modules expand the attack surface | Explicit introduction and brain discussion | F1, X2 | pp. 2–3 | HIGH for author position; no effect size |
| TrustAgent is a modular, technique-oriented survey | Taxonomy description and contribution list | F1, T1, X1 | pp. 1–3 | HIGH; conceptual rather than experimental |
| Poisoned memory can persistently influence behavior | Memory-poisoning description | F3, X3 | pp. 4–5 | HIGH; depends on storage/retrieval and removal |
| Short-term history can support gradual safety bypass | Memory-misuse mechanisms | F3, X3 | p. 5 | HIGH; context- and technique-dependent |
| Tool phases expose threat interfaces | Planning/selection/execution discussion | F4, X4 | p. 6 | HIGH; tool availability and permissions matter |
| Tools enable external abuse | Tool-abuse examples | F4, X4 | p. 6 | HIGH as survey report; underlying studies not reproduced |
| Inter-agent communication can spread malicious effects | Cooperative/infectious attack discussion | F5, X5 | p. 7 | HIGH for reported mechanism; no common propagation rate |
| Dynamic evaluation is needed | Brain insight and sandbox discussion | X2, X4 | pp. 4, 6 | HIGH as author recommendation |
| Tool defenses and memory benchmarks are limited | Explicit gap statements | X3, X4 | pp. 5–6 | HIGH as author assessment; search denominator absent |
| User trust needs dynamic calibration | User-interaction synthesis | X7 | p. 8 | HIGH as proposed direction; no user-study result |
| Web-agent risk can combine entry, persistence, action, propagation | Cross-component synthesis | F1–F6 | pp. 3–8 | MEDIUM; explicitly analyst inference |
| No original matched web-agent/LLM comparison is reported | Paper design and absence of such protocol/results | Inventory, X1–X8 | pp. 2–8 | HIGH for this supplied paper; not a claim about all cited work |

## 22. Very simple explanation — Explain Like I'm 15

A language model can answer a question. An agent gives that model extra abilities: it can remember things, look things up, use tools, and sometimes take actions. A group of agents can also pass information to one another. This paper asks how to keep those larger systems trustworthy.

Each extra ability creates another way for something to go wrong. Bad information can be stored and retrieved later. A harmful instruction can arrive inside material the agent reads. A tool can turn a mistaken decision into an action. In a group, one compromised agent can influence others. The paper organizes attacks and defenses around these different places.

For web agents, the useful lesson is to examine the whole task, including what the agent reads, remembers, and is allowed to do. **That application to the user's web-agent question is an analyst interpretation.** The paper does not measure a universal amount by which web agents are less secure than ordinary chat models. It mainly provides a map of mechanisms and explains why defenses and tests need to cover interacting systems.

## Completeness Audit

The inventory, rather than output length, is the denominator for this audit. All supplied main-text sections and Appendix A are represented. Detailed cited-study catalogs and dense visual examples are compressed with disclosure. The review is not a verification of the underlying literature or the advertised repository.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| FRONT: title, authors, publication, abstract, keywords | Yes, text and images | Yes | Represented in compressed form | Affiliations/emails and permissions compressed |
| S1: §1 Introduction | Yes, text and image | Yes | Fully represented at substantive level | Problem, gap, positioning, contributions |
| T1: Table 1 | Yes, visually and textually | Yes | Fully represented | Categorical rows transcribed; no performance ranking |
| S2: §2 Intrinsic Trustworthiness | Yes | Yes | Fully represented | Internal decomposition explained |
| SS21: §2.1 brain role | Yes | Yes | Fully represented | Reasoning/input integration |
| §2.1.1 Attacks | Yes | Yes | Represented in compressed form | Three families and access caveat retained |
| §2.1.2 Defenses | Yes | Yes | Represented in compressed form | Alignment, filter, shield |
| §2.1.3 Evaluation | Yes | Yes | Represented in compressed form | Focused/general; important counts retained |
| §2.1.4 Insight | Yes | Yes | Fully represented | Collaborative protection and dynamic evaluation |
| SS22: §2.2 memory role | Yes | Yes | Fully represented | Long-/short-term distinction |
| §2.2.1 Attack | Yes | Yes | Represented in compressed form | Poisoning, leakage, misuse and conditions |
| §2.2.2 Defense | Yes | Yes | Represented in compressed form | Detection, prompt modification, output intervention |
| §2.2.3 Evaluation | Yes | Yes | Fully represented at supplied detail | Metrics named; no invented formulas or values |
| §2.2.4 Insight | Yes | Yes | Fully represented | Generalization, protection, training, benchmarks |
| SS23: §2.3 tool role | Yes | Yes | Fully represented | Information gathering and external action |
| §2.3.1 Attack | Yes | Yes | Represented in compressed form | Manipulation subtypes and abuse |
| §2.3.2 Defense | Yes | Yes | Fully represented | GuardAgent/AgentGuard and scarcity claim |
| §2.3.3 Evaluation | Yes | Yes | Represented in compressed form | Dataset testing/sandbox and conditions |
| §2.3.4 Insight | Yes | Yes | Fully represented | Tool review, isolation, tool chains |
| S3: §3 Extrinsic Trustworthiness | Yes | Yes | Fully represented | Three interaction categories |
| SS31: §3.1 agent interaction role | Yes | Yes | Fully represented | Cooperation, competition, debate |
| §3.1.1 Attack | Yes | Yes | Represented in compressed form | Cooperative and infectious mechanisms |
| §3.1.2 Defense | Yes | Yes | Represented in compressed form | Collaborative/topological methods |
| §3.1.3 Evaluation | Yes | Yes | Represented in compressed form | Named resources and narrow-gap qualification |
| §3.1.4 Insight | Yes | Yes | Fully represented | Automation, anti-propagation, graph evaluation |
| SS32: §3.2 environment role | Yes | Yes | Fully represented | Fragmentation and environment-centric organization |
| §3.2.1 Physical Environment | Yes | Yes | Represented in compressed form | Robotics, driving, industrial control |
| §3.2.2 Digital Environment | Yes | Yes | Represented in compressed form | Networks, healthcare, social media |
| SS33: §3.3 user interaction | Yes | Yes | Fully represented | Calibration, personalization, transparency, feedback |
| S4: §4 Conclusion | Yes | Yes | Fully represented | Six components, taxonomy, gaps |
| F1: taxonomy | Yes, visually | Yes | Represented in compressed form | Main panels/encodings; tiny labels partly uncertain |
| F2: brain | Yes, visually | Yes | Represented in compressed form | Mechanisms/panels; no empirical plot |
| F3: memory | Yes, visually | Yes | Represented in compressed form | Workflow, attack paths, interventions |
| F4: tools | Yes, visually | Yes | Represented in compressed form | Call sequence, attacks, dataset/sandbox |
| F5: agent interactions | Yes, visually | Yes | Represented in compressed form | Cooperative/infectious, collaboration/topology |
| F6: environments | Yes, visually | Yes | Represented in compressed form | Physical/digital examples and risks |
| A1: Appendix A | Yes, text and image | Yes | Fully represented at conceptual level | Five dimensions and additional concerns |
| REF: references [1]–[119] | Yes; p. 9 text-only | Partly | Represented in compressed form | Bibliographic evidence and selected discrepancies |
| Formal research questions/hypotheses | Checked | Yes, absence recorded | No such objects identified | User question kept separate |
| Original experiments | Checked | Yes, absence recorded | No such objects identified | Literature analyses registered instead |
| Major equations/theorems/algorithms | Checked | Yes, absence recorded | No such objects identified | Schematic code fragments distinguished |
| Major contributions | Yes | Yes | Fully represented | Conceptual, organizational, synthesis, resource |
| Author-stated field limitations | Yes | Yes | Fully represented | Kept separate from analyst observations |
| Equal-contribution/corresponding-author footnotes | Yes | Yes | Represented in compressed form | Authorship roles retained |
| Separate supplementary material | Not supplied | Absence recorded | Missing from supplied material | No reviewed supplement claimed |
| Advertised GitHub collection | Mention inspected only | Access limitation recorded | Inaccessible in this closed-document review | No repository contents inferred |

### Missing or inaccessible material

No main-paper page is absent from the supplied text. Page 9 lacks a supplied visual rendering, so its bibliography was reviewed textually only. The advertised study repository and full cited papers are not supplied. There are no separate supplied supplementary files or executable artifacts. Their absence prevents assessing underlying study protocols, code, or repository completeness.

### Uncertain interpretations

Small figure lettering is not uniformly readable; descriptions prioritize visible structure, captions, extracted labels, and adjacent prose. No exact numerical result is inferred from the diagrams. The exclusion of parameter-modification misalignment attacks alongside training-associated backdoors leaves attacker-access assumptions nonuniform. Selected reference mappings are uncertain: ASB [106] on page 5 conflicts with the supplied bibliography; the neuro-symbolic attribution to [25] on page 4 does not match that reference's supplied title; and [104]'s title concerns ontology alignment rather than plainly documenting the human-belief description attached to it. These are source-internal attribution concerns, not external citation validation.

Additional source mismatches include the use of Audit-LLM in a broader hallucination/safety/robustness discussion while its supplied title specifies log-based insider-threat detection; BLAST's supplied title refers to cooperative multi-agent deep reinforcement learning while it is discussed within a broader agent-brain backdoor category; and the truthfulness paragraph in Appendix A using resource-draining CORBA as an example. These observations reduce confidence in the precision of selected examples without requiring a guessed correction. The duplicate Agent-SafetyBench entries [106]/[107] and versioned AgentDojo entries [19]/[20] also mean reference numbering is not a unique-study count.

### Deliberately compressed material

Individual studies with repetitive examples of the same mechanism are grouped into attack, defense, and evaluation families. The environment catalog is compressed as follows: robotics uses constraints, safe planning, and unsafe-action pruning; autonomous-driving examples concern perception-attack mitigation and safety-critical scenario generation; industrial-control examples concern validation, reprompting, and code verification; digital examples concern autonomous web attacks, task-specific evaluation, medical privacy/robustness, and social-media detection/compliance. These categories preserve the distinct application analyses without reproducing every sentence.

Appendix A's illustrative named examples are compressed into definitions and cross-referenced mechanisms. Tiny illustrative framework names, icons, repeated headers, author contact details, copyright language, and the complete bibliography are not reproduced. Figures' major panels and flows are represented, but their decorative icons and repeated example labels are deliberately omitted as secondary. No proposed experimental result is hidden by this compression because the paper supplies no original result series.

### Potential omissions

No known substantive main section, subsection, numbered figure, table, or appendix from the inventory is left unrepresented. Fine figure labels remain partly uncertain, and complete study-by-study detail is deliberately compressed. Completeness is therefore claimed only for the identified structure and major supplied content at the disclosed level of compression; it does not extend to inaccessible artifacts, validation of cited studies, or recovery of unreadable microtext.
