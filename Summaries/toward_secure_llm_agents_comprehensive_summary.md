# *Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation*

**Authors:** Yuchen Ling, Shengcheng Yu, Zhenyu Chen, and Chunrong Fang  
**Publication:** *ACM Transactions on Software Engineering and Methodology*, January 2026, 42 pages

## 1. Background and Context

Large language model agents are moving beyond conversation into software systems that plan, browse websites, manipulate files, execute code, invoke tools, maintain memory, monitor progress, and coordinate with other agents. This changes the security problem fundamentally.

In a text-only application, failure usually produces bad or unsafe text. In an agent, the same underlying weakness can instead:

- Redirect a workflow.
- Select or misuse a privileged tool.
- Execute unsafe code or commands.
- Leak sensitive information.
- Corrupt temporary or persistent memory.
- Cause irreversible external actions.
- Spread malicious instructions to other agents.

The defining issue is **delegated authority**: agents act using permissions granted by users or organizations. An attacker may not possess those permissions directly but can exploit the agent to browse, execute, store, modify, or communicate on the attacker’s behalf.

The paper therefore treats LLM-agent security as a software and systems security problem, not merely prompt safety. Its central concerns are control-flow integrity, trust boundaries, capability and privilege control, provenance, state integrity, runtime mediation, containment, and monitoring.

An LLM agent is defined by its participation in an **agentic loop**: interpreting goals, planning, selecting an action, invoking tools, updating state, observing progress, and possibly coordinating with humans or other agents. Web agents, coding agents, memory-based assistants, embodied agents, and multi-agent workflows can all be analyzed through this common structure.

Three properties make these systems especially difficult to secure:

1. **Data–control ambiguity:** Natural-language context mixes user goals, retrieved evidence, web content, tool feedback, intermediate plans, summaries, and messages. Content that should be treated only as untrusted data may be interpreted as an instruction.

2. **Delegated authority:** An attacker can influence an agent that has greater permissions than the attacker.

3. **Persistence and propagation:** Contamination may survive in memory, reappear in later tasks, or spread through inter-agent communication.

The field is growing rapidly but remains fragmented across attacks, defenses, applications, benchmarks, metrics, and terminology. Prompt injection receives the most attention, while memory integrity, privilege misuse, and multi-agent propagation are increasingly important but less systematically studied. Existing evaluations also emphasize immediate attacks in bounded tasks, leaving long-horizon, stateful, and deployment-sensitive risks underrepresented.

---

## 2. Research Goal and Objectives

The paper’s main goal is to synthesize research on LLM-agent security using one lifecycle-based, systems-oriented framework. It analyzes a curated corpus of **247 papers** and asks how information, authority, and persistent state interact across an agent’s operation.

The four research questions are:

1. **RQ1 — Scope and modeling:** How should LLM-agent security be scoped and modeled as a software systems problem?

2. **RQ2 — Threat surfaces and attacks:** Which threat surfaces and attack families dominate current research?

3. **RQ3 — Defenses and tradeoffs:** Which defenses have been proposed, and what costs, assumptions, and failure modes do they introduce?

4. **RQ4 — Evaluation and benchmark gaps:** How is agent security evaluated, and what is missing from current benchmarks and empirical methods?

The authors aim to move beyond a list of attacks by connecting:

- Where untrusted information enters.
- How it changes plans and decisions.
- When an agent crosses a capability boundary.
- How contamination persists in memory.
- How failures propagate among agents.
- Where defenses intervene.
- What benchmarks and metrics actually measure.

---

## 3. Methods (Approach/Design)

### Study design

This is a structured literature review and systems-oriented synthesis. It combines database retrieval, LLM-assisted search expansion, citation snowballing, manual screening, bibliographic normalization, structured coding, descriptive counting, and cross-sectional analysis.

### Search period and sources

The search covers work published from **January 1, 2023, through April 27, 2026**. Six sources were searched:

- ACM Digital Library
- IEEE Xplore
- Scopus
- Web of Science
- arXiv
- Google Scholar

The search combined three concept groups:

- LLM-related terms.
- Agent-related terms, including tool-using, web, coding, browser, computer-use, memory-augmented, embodied, multi-agent, and agentic-workflow systems.
- Security-related terms, including prompt injection, jailbreaks, memory poisoning, tool misuse, exfiltration, access control, sandboxing, monitoring, guardrails, benchmarks, and red teaming.

Database syntax was adapted while preserving the same conceptual groups.

### LLM-assisted candidate expansion

The review used **GPT-5.4 with web search** as a bounded retrieval assistant. Given the current seed papers, titles, keywords, and dates, it suggested:

- Semantically related papers using different vocabulary.
- Query variants and benchmark aliases.
- Synonym normalization.
- Potentially missing branches such as memory poisoning, instruction hierarchy, Model Context Protocol tooling, and multi-agent governance.

The model did not decide inclusion. Every candidate was manually checked against a bibliographic source.

### Citation snowballing

Backward and forward citation searches were conducted from representative seed papers, early benchmarks, and prior surveys. This helped recover papers discoverable through system lineage, benchmark reuse, or architectural influence rather than exact keyword matches.

### Selection criteria and flow

A paper was included only if LLM-agent security was a substantive topic and it involved an explicit agentic surface, such as:

- Tool invocation or external action.
- Planning.
- Persistent memory or state.
- Runtime infrastructure.
- Embodied interaction.
- MCP or skill interfaces.
- Multi-agent communication.

Generic prompt-injection, LLM safety, privacy, or governance work was excluded when it lacked an explicit agentic execution loop. Capability-only benchmarks and autonomous-system papers without a central security question were also excluded.

The reported selection flow was:

- **275 records** entered detailed relevance auditing.
- **25** were excluded after title/abstract or full-text screening.
- **251** were provisionally retained.
- **4** duplicate versions or preprint–publication pairs were merged.
- **247 papers** formed the final corpus.

The supplied figures contain an apparent arithmetic inconsistency: 275 minus 25 equals 250, although Table 1 reports 251 provisionally retained. The paper does not explain this discrepancy.

The auditable workbook contains four sheets:

- Final corpus.
- Relevance audit.
- Exclusion log.
- Notes on inclusion-boundary decisions.

The artifact supports auditing of screening, exclusion, normalization, and final coding. It does not preserve complete engine-specific hit counts, all query-session logs, or every LLM prompt, so exact retrieval replay is not claimed.

### Coding framework

Each paper was coded for:

- Bibliographic metadata.
- Primary paper type.
- Single-agent or multi-agent setting.
- Research topic.
- Task scenario.
- Threat model.
- Threat surface.
- Lifecycle stage.
- Attack and defense methods.
- Benchmarks.
- Evaluation metrics.

Primary paper type and system setting were single-label fields used only for coarse distributions. Technical dimensions were multi-label because one paper could cover several surfaces, stages, benchmarks, or methods.

Important operational distinctions included:

- **Web content:** Human-readable material fetched from browsing environments.
- **Retrieved content:** Search or retrieval-augmented-generation evidence.
- **Tool outputs:** Responses produced by explicitly invoked tools or APIs.
- **Files/code:** Repositories, scripts, configuration files, or attachments.
- **Memory/scratchpads:** Temporary or persistent state generated or reused by an agent.
- **Planning:** Task decomposition or trajectory generation.
- **Decision:** Commitment to a next action or delegation target.
- **Tool execution:** Actual invocation of an external capability.

### Reliability and interpretation

The final labels and audit records are preserved, but coder-specific parallel annotations were not. Consequently:

- No inter-rater agreement statistic is reported.
- Counts are not treated as uncertainty-free.
- Explicit definitions were used for consequential labels.
- Technical overlap was preserved through multi-label coding.
- Most counts are interpreted as **research attention**, not validated effectiveness, real-world prevalence, or deployment importance.

The authors distinguish:

- **Research popularity:** Frequency in the corpus.
- **Evidential strength:** Quality, replication, and stability of empirical evidence.
- **Deployment importance:** Potential real-world consequences.

Most reported statistics directly measure only the first.

### Figure 1: Review and analytical framework

Figure 1 links four layers:

1. A hybrid pipeline producing **247 curated papers** through retrieval, LLM-assisted exploration, snowballing, manual screening, and structured coding.
2. A lifecycle model spanning input, planning, decision, tool execution, output, memory/state, and coordination, interpreted through information flow, delegated authority, and persistent state.
3. RQ1–RQ4.
4. Engineering outcomes: trust boundaries, privilege control, state management, and deployment assurance.

---

## 4. Results and Findings

### 4.1 Corpus growth, venues, paper types, and system settings

#### Figure 2(a): Publication years

The corpus grew rapidly:

- **2023:** 3 papers.
- **2024:** 42 papers, **17.0%**.
- **2025:** 121 papers, **49.0%**.
- **2026 through April 27:** 81 papers, **32.8%**.

The sharpest increase occurred between 2024 and 2025. The partial 2026 count indicates continued activity but is not a complete annual total.

#### Table 2: Venues

The corpus is heavily preprint-based:

- arXiv: **169 papers, 68.42%**.
- Web-published industry reports, blogs, and advisories: **12, 4.86%**.
- ICLR: **12, 4.86%**.
- ACL: **10, 4.05%**.
- EMNLP: **8, 3.24%**.
- NeurIPS: **6, 2.43%**.
- ICML: **5, 2.02%**.
- NDSS: **3, 1.21%**.
- NAACL and COLM: **2 each, 0.81%**.
- Numerous security, software-engineering, robotics, AI, ethics, and journal venues contribute one paper each.

The source table separately includes another one-paper ICML entry, suggesting a venue-normalization duplication in the supplied table. Overall, the distribution is a long tail without a stable disciplinary or archival center.

Among **66 attack papers**, 47 are arXiv preprints; among **64 defense papers**, 48 are preprints. These frequencies therefore show where effort is concentrated, not which attacks or defenses are mature.

#### Figure 2(b): Primary paper type

- Attack: **66, 26.7%**.
- Defense: **64, 25.9%**.
- Benchmark: **47, 19.0%**.
- Survey: **32, 13.0%**.
- Evaluation: **26, 10.5%**.
- Report: **12, 4.9%**.

Attack and defense papers total **130**, or **52.63%**, showing that mitigation research has developed nearly in parallel with attack discovery. The substantial benchmark segment also reflects fragmentation because studies use different threat models, tasks, attacker assumptions, and success criteria.

#### Figure 2(c): System setting

- Single-agent: **200 papers, 80.97%**.
- Multi-agent: **47 papers, 19.03%**.

Multi-agent papers nevertheless increased from **9.52% of 2024 papers** to **23.97% in 2025**, remaining **17.28%** in the partial 2026 corpus. This indicates sustained interest in delegation, message passing, role separation, and cross-agent propagation.

### 4.2 RQ1: Scope and systems model

The paper models an agent as:

\[
A=\langle I,P,D,T,M,O,C\rangle
\]

where:

- \(I\): inbound context and observations.
- \(P\): planning over possible trajectories.
- \(D\): commitment to an action or delegation step.
- \(T\): tool or environment execution.
- \(M\): temporary or persistent memory/state.
- \(O\): visible outputs and side effects.
- \(C\): coordination with humans, monitors, or peer agents.

Security problems arise through transitions: low-authority content entering \(I\) may corrupt \(P\), change \(D\), trigger privileged \(T\), poison \(M\), or spread through \(C\).

The most common research topics were:

- Tool-use security: **156 papers**.
- Runtime defense: **88**.
- Prompt-injection security: **75**.
- Multi-agent security: **63**.
- Memory safety: **32**.

#### Table 3: Major lifecycle dimensions

- Planning: **227 papers**.
- Input: **225**.
- Tool execution: **209**.
- Decision: **166**.
- Memory: **82**.
- Monitoring: **58**.
- Inter-agent communications: **35**.
- Coordination: **20**.
- Output, reported in the text: **151**.

Major threat surfaces included:

- User prompts: **82**.
- Web content: **55**.
- Tool outputs: **54**.
- Retrieved content: **37**.
- Memory/scratchpads: **25**.
- Files/code, planning loops, and inter-agent channels: each appeared in at least **25 papers**.

These findings show that direct prompting is only one part of the problem. Agent security is dominated by cross-stage control processes involving external content, tools, state, and communication.

#### Figure 3: Lifecycle-by-surface matrix

The heat map reports the following co-occurrences across input, planning, decision, tool execution, output, memory, monitoring, inter-agent communication, and coordination:

- **User prompts:** 82, 82, 60, 76, 49, 36, 7, 5, 1.
- **Web content:** 53, 53, 35, 51, 33, 19, 12, 3, 1.
- **Tool outputs:** 50, 54, 41, 54, 30, 20, 15, 1, 0.
- **Retrieved content:** 36, 35, 26, 35, 21, 13, 9, 1, 1.
- **Memory/scratchpads:** 19, 23, 11, 20, 11, 25, 5, 5, 4.
- **Inter-agent channels:** 19, 21, 15, 7, 11, 9, 5, 21, 16.
- **Files/code:** 26, 24, 15, 25, 20, 4, 9, 2, 0.
- **Planning loops:** 20, 25, 17, 18, 13, 6, 7, 7, 2.

User prompts, web content, and tool outputs concentrate in input, planning, and tool execution. Memory/scratchpads align most strongly with memory, while inter-agent channels align with inter-agent communication and coordination.

**RQ1 answer:** LLM-agent security is best modeled as the interaction of information flow, delegated authority, and persistent state across lifecycle transitions. Prompt injection is often a planning/execution problem, memory poisoning is delayed control-flow corruption, and multi-agent coordination is a trust-and-propagation problem.

### 4.3 RQ2: Threat surfaces and attack families

#### Prompt injection and control-flow hijacking

Prompt injection dominates:

- Prompt injection as a threat model: **142 papers**.
- Indirect prompt injection: **86**.
- Unsafe user instructions: **43**.
- Malicious tools: **34**.
- Data exfiltration: **31**.
- Memory poisoning: **24**.
- Coordination failures: **14**.

Prompt injection matters because task-relevant but non-authoritative content—such as web pages, retrieval results, files, or tool responses—can be mistaken for executable instructions.

Scenario-specific counts include:

- Web browsing: prompt injection **71**, indirect prompt injection **44**.
- Software engineering: prompt injection **32**, indirect prompt injection **16**.
- Multi-agent collaboration: prompt injection **44**, memory poisoning **14**, coordination failures **14**.

In the system model:

- Prompt injection primarily attacks \(I\rightarrow P\) and \(I\rightarrow D\).
- Malicious tools and exfiltration become operational at \(D\rightarrow T\) and \(T\rightarrow O\).
- Memory poisoning targets \(I/T\rightarrow M\), followed later by \(M\rightarrow P\).
- Coordination attacks propagate through \(C\rightarrow P\) and \(C\rightarrow D\).

#### Persistence and state integrity

Memory poisoning appears in **24 papers**, while memory safety is a topic in **32**. Once contaminated information is stored, it can survive the original interaction and influence later planning.

Memory security therefore concerns whether the system can correctly:

- Record and assess provenance.
- Remember or forget.
- Assign trust.
- Quarantine suspicious state.
- Revoke previously trusted state.
- Prevent delayed reactivation.

#### Multi-agent propagation

Only 47 papers are primarily multi-agent, but multi-agent security appears as a topic in 63 papers. Collaborative systems add message-integrity failures, role confusion, delegation errors, amplification, covert communication, and topology-sensitive contagion.

#### Figure 4: Three propagation patterns

1. **Mediated external injection:** Web content (**55 papers**), tool outputs (**54**), and retrieved content (**37**) feed into input (**225**), planning (**227**), and tool execution (**209**).

2. **Delayed memory activation:** A memory/scratchpad surface (**25**) enters stored state; the memory stage appears in **82 papers** and may later influence planning (**227**) before action/tool execution (**209**).

3. **Multi-agent spread:** One compromised agent transmits contamination through peer agents, coordination (**20**), and eventually an external effect.

#### Scenario concentration and consequence

The most studied scenarios were:

- Web browsing: **93 papers**.
- Software engineering: **63**.
- Finance tools: **34**.
- Healthcare assistance: **28**.
- Embodied robotics: **28**.

The paper warns that frequency and consequence differ. Finance, healthcare, and robotics may have stronger confidentiality, integrity, or physical consequences despite receiving less attention than web and software agents. Healthcare studies visibly include memory poisoning, exfiltration, and malicious tools; embodied-agent studies emphasize jailbreaks and unsafe instructions.

**RQ2 answer:** Prompt injection and indirect, tool-mediated control-flow hijacking remain the empirical center, but the threat model is expanding toward persistent state corruption, authority misuse, and multi-agent propagation.

### 4.4 RQ3: Defense strategies and tradeoffs

Defenses fall into three broad groups.

#### Source handling and instruction ordering

Instruction hierarchies and guardrails try to stop low-authority content from becoming control. They are relatively simple and inexpensive but remain model-mediated: they depend on the model or wrapper preserving source distinctions under paraphrase, composition, and tool restatement.

#### Runtime scrutiny

Runtime monitoring, policy enforcement, guard agents, and anomaly detection inspect plans, tool calls, or execution traces near the point where harm occurs. They better match agent behavior than prompt-only filters but add latency, complexity, extra model calls, false positives, and dependence on policy quality and observability.

#### Capability control and containment

Access control, information-flow control, context isolation, and sandboxing constrain what compromised reasoning can influence. They directly protect authority boundaries, but require fine-grained permissions, trusted mediation, explicit provenance, typed interfaces, and infrastructure support.

#### Table 5: Defense families and tradeoffs

- **Input-trust management (\(I\rightarrow P,D\)):** Protects mixed-trust input and control flow; may fail when source distinctions are obscured.
- **Runtime monitoring/guard agents (\(P\rightarrow D\rightarrow T\rightarrow O\)):** Detect unsafe plans, tool calls, and policy violations; adds latency and can block benign behavior.
- **Access control/least privilege (\(D\rightarrow T\rightarrow O\)):** Limits privilege escalation and unsafe capability use; requires practical permission granularity.
- **Information-flow/state isolation (\(I\leftrightarrow M\), \(M\rightarrow P\), \(T\rightarrow M\)):** Addresses memory poisoning and cross-context leakage; difficult in long-horizon and collaborative systems without provenance or typed interfaces.
- **Execution containment (\(T\rightarrow O\)):** Limits post-compromise damage; may reduce autonomy or compatibility and increase engineering costs.
- **Topology-aware multi-agent containment (\(C\rightarrow P,D,C\)):** Limits contagion, role confusion, and coordination failures; requires message/topology visibility and remains vulnerable to covert channels.

Defenses cluster most strongly around \(I\rightarrow P\) and \(D\rightarrow T\). Protection for memory \(M\) and coordination \(C\) is thinner.

#### Figure 5: Layered defense stack

The proposed synthesis contains:

- **Instruction handling:** 2 instances—guardrails (1), instruction hierarchy (1).
- **Planning validation:** 11—runtime monitoring (6), policy enforcement (3), anomaly detection (2).
- **Tool gating:** 13—access control (8), information-flow control (5).
- **State protection:** 2—context isolation (2).
- **Execution containment:** 2—sandboxing (2).

Planning validation and tool gating receive the most attention. Explicit gaps are:

- Provenance.
- Revocation.
- Inter-agent trust.
- Topology-aware containment.

#### Table 6: Scenario-oriented minimum stacks

- **Browser/web agents:** Input-trust management, runtime plan/action checks, tool gating or confirmation, and containment for high-authority actions. Open problems include realistic source separation and useful indirect-injection defenses.

- **Coding agents:** Least privilege for files, shells, and packages; monitoring of dangerous calls; isolated execution. Open problems include secure-by-default tool APIs, dependency/skill provenance, and regression testing of long tool chains.

- **Memory-based assistants:** Provenance-aware state isolation, revocation or trust decay, and checks before memory-derived action. Open problems include trust labels, delayed-trigger testing, and realistic memory benchmarks.

- **Multi-agent workflows:** Role-scoped authority, communication monitoring, topology-aware containment, and per-agent privilege control. Open problems include covert collusion, message provenance, distributed rollback, and graph-wide incident containment.

Four recurring tradeoffs are scope, trust assumptions, overhead, and utility loss. Stronger controls generally require more mediation and complexity and may reduce autonomy or task completion.

**RQ3 answer:** The field contains useful components but lacks a stable, compositional security stack tailored to different architectures and deployment risks.

### 4.5 RQ4: Evaluation and benchmark gaps

#### Benchmark landscape

The most reused benchmarks were:

- AgentDojo: **30 occurrences, 12.82% of benchmark annotations**.
- InjecAgent: **11, 4.70%**.
- MMLU: **5, 2.14%**.
- ASB: **4, 1.71%**.
- SafeAgentBench: **4, 1.71%**.
- R-Judge: **3, 1.28%**.
- OSWorld: **3, 1.28%**.
- JailbreakBench: **3, 1.28%**.

Because benchmark coding is multi-label, percentages use total benchmark annotations rather than papers. Even AgentDojo accounts for only 12.82%, indicating strong fragmentation.

AgentDojo and InjecAgent measure prompt injection in tool-integrated workflows. ASB extends toward memory poisoning and backdoors. SafeArena and WASP emphasize unsafe task acceptance and web risk; OS-Harm covers computer-use actions. AgentDyn and AgentLeak move toward dynamic or multi-agent environments. Most reusable benchmarks still emphasize input, planning, decision, and tool execution rather than memory and coordination.

#### Metrics

- Attack Success Rate: **129 papers**.
- Success Rate: **59**.
- Accuracy: **41**.
- Utility: **22**.
- Recall: **19**.
- F1: **15**.
- Precision: **14**.
- Refusal Rate: **13**.
- False Positive Rate: **13**.
- Latency: **8**.
- Cost: **7**.

Attack Success Rate captures immediate compromise but often misses utility loss, delayed harm, and deployment cost. Success Rate measures task completion but not alignment. Accuracy misses action risk and system consequences. Utility misses detailed safety failures. Detection metrics omit latency, cost, task utility, or downstream tradeoffs. Refusal Rate does not show whether refusal was appropriate. False Positive Rate omits task success and delayed compromise. Latency and cost do not establish whether added controls improve protection.

The central imbalance is that evaluations often ask whether an agent can be broken, but less often whether it remains useful, governable, affordable, and secure over repeated deployment.

#### Figure 6: Benchmark co-occurrence matrix

The matrix compares eight benchmarks across threat surfaces, lifecycle stages, scenarios, and reporting fields. It counts papers in which each benchmark co-occurs with a code; it does not directly measure the benchmark’s intrinsic coverage.

AgentDojo and InjecAgent show the densest associations with user/web-facing input, planning, tool execution, and web or software-engineering scenarios. Coverage becomes thin for memory, inter-agent communication, coordination, multi-agent scenarios, and embodied or specialized domains. Reporting is sparser still: utility is uneven, latency is rare, and cost is nearly absent.

**RQ4 answer:** Evaluation is active but not standardized enough for deployment assurance. Stronger evaluation should:

1. Cover multiple threat surfaces.
2. Jointly measure safety and utility.
3. Include long-horizon memory corruption and delayed activation.
4. Test privilege-sensitive external actions.
5. Report latency, cost, and oversight burden.

No statistical significance tests or experimental p-values are reported because this is a coded literature synthesis rather than a controlled experiment.

---

## 5. Analysis and Interpretation

The authors interpret agent security as a problem of **transitions**, not isolated components. The crucial question is not only what information an agent sees, but what it is permitted to do because it saw that information.

Several formerly separate problems become variations of the same underlying mechanism:

- Prompt injection turns untrusted input into planning or decision control.
- Tool attacks exploit the transition from decisions to privileged execution.
- Memory poisoning stores contamination and reactivates it later.
- Multi-agent attacks propagate compromised control through coordination channels.

The survey’s strongest descriptive conclusions are:

1. Prompt injection and tool-mediated control-flow hijacking remain the empirical center of research.
2. Persistence and propagation—especially memory reuse and multi-agent coordination—are the clearest expanding concerns.
3. Defense and evaluation are less consolidated than attack research.

The authors argue that the field needs to move from demonstrating attacks toward **secure agent engineering**. Architectural defaults should include explicit trust boundaries, provenance, authority scopes, containment, and fallback behavior.

For software engineering, this implies:

- Requirements should specify which tools may be used, under what provenance conditions, which actions need confirmation, what state may cross tasks, and what rollback follows compromise.
- Coding agents should use least-privilege file/shell/package access, provenance-aware file handling, typed tool contracts, isolated execution, and auditable approval boundaries.
- MCP tools, skills, plugins, and repositories create supply-chain-like risks, complicated by ambiguity between data and executable control.
- One-off red-team tests should become repeatable security regression suites covering prompt injection, malicious tool outputs, poisoned memory, and communication failures.
- Runtime policy engines, monitors, telemetry, replay, incident triage, and containment are necessary because failures can be stateful and delayed.
- Updating prompts, tools, policies, and orchestration must not silently broaden authority.

Relative to eight representative prior surveys, the paper rates itself as having an **explicit** search protocol, **central** lifecycle framing, **broad** coverage of tools/runtime, memory/state, and multi-agent systems, and **dedicated** benchmark and software-engineering assurance synthesis. The claimed novelty lies in integrating these dimensions, not merely reviewing more topics.

---

## 6. Contributions and Novelty

The paper’s main contributions are:

- A curated and auditable corpus of **247 LLM-agent-security papers** assembled through database retrieval, bounded LLM-assisted expansion, citation snowballing, manual screening, and normalization.
- A lifecycle model connecting input, planning, decisions, tools, outputs, memory, monitoring, and coordination.
- A semi-formal agent representation, \(A=\langle I,P,D,T,M,O,C\rangle\), that makes information flow, authority, and persistence explicit.
- A synthesis of attacks as recurring propagation patterns: mediated entry, delayed state activation, and inter-agent spread.
- A defense analysis organized by intervention point, protected asset, trust assumptions, utility cost, overhead, and composability.
- A layered defense-stack interpretation highlighting strong coverage around planning and tool gating but weak coverage for provenance, revocation, state, and coordination.
- A benchmark analysis connecting threat surfaces, lifecycle stages, scenarios, metrics, and reporting gaps.
- A software-engineering agenda focused on trust-boundary requirements, secure APIs, regression assurance, runtime verification, and deployment-specific assurance cases.

---

## 7. Limitations and Caveats

The paper identifies several threats to validity.

### Construct validity

Threat surfaces overlap because web content, retrieval, tool outputs, files, and memory can all contain untrusted text. Planning, decisions, and tool execution may also be tightly interleaved. Explicit definitions and multi-label coding reduce but do not eliminate judgment-sensitive boundaries.

### Internal validity

Screening, coding, and harmonization involved human interpretation. The workbook preserves final labels and audit records, but coder-specific parallel annotations were not retained, so no inter-rater agreement can be calculated.

### External validity

The six-source search, snowballing, and LLM-assisted expansion may still miss unusual terminology, unpublished industrial artifacts, or adjacent system names. Publication bias is unavoidable.

The corpus is unstable because **169 of 247 papers (68.42%)** are arXiv preprints. Titles, methods, claims, and bibliographic identities may change before formal publication.

### Conclusion validity

Frequency does not measure empirical strength, real-world prevalence, consequence, effectiveness, or deployment readiness. Benchmark clusters can create a misleading appearance of consensus. All rankings should therefore be treated as descriptive research-attention patterns.

### LLM-assisted retrieval bias

GPT-5.4 may favor highly visible papers, popular terms, or easily searchable benchmarks. Its role was restricted to candidate suggestions and normalization, followed by manual verification.

### Reproducibility

The artifact records the final screened corpus, exclusions, and coding but lacks complete search-engine hit counts, all session logs, and every candidate-expansion prompt. Screening and normalization are auditable; exact retrieval replay is not.

### Architectural and evaluation limitations

- Single-agent systems dominate the corpus, potentially underrepresenting multi-agent-specific risks.
- Benchmarks concentrate on short-horizon prompt injection and tool use.
- Memory, coordination, delayed effects, privilege-sensitive actions, latency, cost, and operational oversight are sparsely measured.
- Defense components have not been validated as a universally composable stack.
- The paper’s scenario-specific defense stacks are literature-based engineering interpretations, not established standards.

---

## 8. Future Work or Open Questions

The paper identifies five major priorities.

### Provenance-aware state management

Systems need to record where state came from, what authority it carries, and when it should decay, be quarantined, or be revoked. Promising directions include memory labels, trust decay, provenance models, and delayed-trigger testing.

### Secure tool governance

Agent frameworks should expose fine-grained capability scopes, least privilege, confirmation rules, safe tool APIs, trusted mediation, and isolated execution as first-class features.

### Multi-agent trust management

Future systems need role-scoped authority, message-integrity controls, message provenance, topology-aware containment, distributed rollback, and incident response across an agent graph. Covert collusion and hidden propagation channels remain unresolved.

### Lifecycle-wide evaluation

Benchmarks should cover multiple surfaces and longer horizons, including persistent memory, delayed activation, coordination, and actions with meaningful external consequences. Safety and utility should be assessed jointly.

### Deployment-oriented assurance

Evaluations should consistently report latency, cost, false positives, utility, fallback behavior, and oversight burden. The authors propose deployment-specific **assurance cases** that combine threat modeling, privilege analysis, runtime controls, benchmark evidence, and incident-containment expectations.

The broader open question is how to compose strong controls without making agents unusably slow, rigid, expensive, or incapable of completing legitimate tasks.

---

## 9. High-Level Takeaway (Plain Language)

LLM agents are not merely chatbots: they can browse, remember, use tools, execute commands, and communicate with other agents. That means a malicious web page, tool response, or memory entry can influence real actions, persist into future tasks, or spread across a workflow.

After reviewing 247 papers, the authors find that prompt injection remains the most studied threat, but memory poisoning and multi-agent spread are becoming increasingly important. Existing defenses—such as monitoring, access control, information-flow restrictions, and sandboxing—are useful but do not yet form a complete, dependable security stack. Benchmarks are similarly fragmented and rarely measure long-term effects, utility, cost, and realistic deployment consequences.

The paper’s core message is that secure agents require engineered limits on authority, clear trust boundaries, traceable and revocable memory, runtime containment, and realistic evaluation—not just better prompts or filters.