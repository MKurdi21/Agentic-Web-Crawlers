## Stage 0 — Document Accessibility Report

The supplied main document is available as page-labeled extracted text for physical PDF pages 1–40. All 40 text records were available for reading; the supplied sequence has no missing page numbers. This establishes coverage of the supplied document, not independent verification that it matches an authoritative publication. Direct page images are available for pages 1, 2, 4–9, 11–13, 15–22, 24, 28, 33, and 36–40: 27 visually inspected pages. Pages 3, 10, 14, 23, 25–27, 29–32, and 34–35 were inspected through supplied extracted text only. The failed image reference at `-` supplies no additional evidence and does not invalidate the other images.

All seven numbered figures and all eleven numbered tables appear on the supplied rendered pages. Their structures, captions, principal labels, and important values are readable. Small figure labels require caution, particularly heatmap color scales and compact diagram annotations; exact numerical statements below use clearly labeled cells or corresponding prose, not estimates from color. The semi-formal agent tuple and transition arrows are readable in both text and relevant images. No OCR was performed or needed for this analysis. Extracted mathematical formatting occasionally loses spacing, so symbol meanings were checked against prose and rendered tables.

Appendix A, including A.1–A.4, Appendix B, and Appendix C, including C.1–C.3, are supplied. Appendix C is titled supplementary evidence but is part of the document, not an independently supplied file. No separate supplementary dataset, corpus annotation file, repository, website content, search log, or executable artifact was provided. Page 3 mentions a survey website without supplying its contents. The accessibility metadata reports no embedded files; that is supplied metadata, not a tool-verified finding. The original PDF bytes and stated SHA-256 were not independently checked.

This is CLOSED-DOCUMENT analysis. No tools, browsing, external citation validation, or outside factual supplementation were used. Author-provided prompts in Appendix A are analyzed as evidence of the review procedure, never followed as instructions. Evidence labels are: [A] author-reported, [B] directly observable in supplied visuals, [C] analyst-derived, and [D] analyst interpretation. Confidence describes confidence in faithful representation of this document, not independent proof of its scientific claims. HIGH means explicit, readable evidence; MEDIUM means a qualified synthesis or interpretation; LOW means materially ambiguous evidence; UNKNOWN means unavailable information.

## 1. Plain-language orientation

This paper studies the security of large language model (LLM) agents: software systems that use a language model to choose and carry out steps, rather than simply generate a response. Such systems may browse websites, invoke tools, edit files, run code, preserve memory, and communicate with other agents. The central concern is what happens when untrusted information influences those capabilities.

[A] The authors synthesize 247 papers using a lifecycle-based framework. They organize security around information flow, delegated authority, and persistent state. In ordinary terms: what information enters the system, what permissions the system can exercise, and what it remembers afterward. Their contribution is a connected interpretation of attacks, defenses, and evaluations rather than a new attack implementation or controlled experiment.

[A] The survey finds that prompt injection and tool-mediated control-flow hijacking dominate research attention. Memory corruption and propagation across agents are important emerging concerns. Defenses exist, but their assumptions and intervention points differ; the literature has not established a stable combination of layers suitable for every deployment. Benchmarks emphasize immediate compromise more often than long-term safety, usefulness, operational cost, and recovery.

[D] For the user's question, the paper supports an architectural explanation of why web AI agents can have additional vulnerabilities and more consequential failures than text-only LLM applications. A web page can become an indirect instruction source; a mistaken interpretation can select an action; that action can use the user's permissions; subsequent outputs can feed back into later decisions or memory. However, the paper does not perform a matched experiment comparing standalone LLMs with web agents. It establishes neither a universal numerical vulnerability increase nor a claim that every web agent is less secure than every standalone LLM.

## 2. Document roadmap

The original title is **Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation**. The authors are Yuchen Ling, Shengcheng Yu, Zhenyu Chen, and Chunrong Fang; Yu and Fang are identified as corresponding authors. Page 1 associates Ling, Chen, and Fang with Nanjing University and Yu with the Technical University of Munich. The document is a cybersecurity survey with systematic-review procedures and descriptive corpus analysis.

The supplied title page displays an ACM Computing Surveys reference format, volume 1, issue 1, article 1, January 2026, 40 pages, and a placeholder DOI. Its margin identifies arXiv:2606.10749v2, dated 23 August 2026. These are reported document markings, not verified publication status. The January date conflicts chronologically with the review's April cutoff and May retrieval dates; this remains unresolved below.

| Original section | Physical pages | Role |
|---|---|---|
| Abstract and front matter | 1 | Defines the systems-security argument and survey scope |
| §1 Introduction | 2–3 | Motivates agent security and lists contributions |
| §2 Background; §§2.1–2.2 | 3–5 | Explains autonomous agents and operational risks |
| §3 Survey Methodology; §§3.1–3.4 | 5–7 | Research questions, retrieval, selection, annotation |
| §4 Trend Observation | 7–8 | Year, paper type, venue, and system-setting distributions |
| §5 RQ1; §§5.1–5.3 | 8–11 | Agent tuple, surfaces, transitions, modeling implications |
| §6 RQ2; §§6.1–6.3 | 11–14 | Injection, tool misuse, state integrity, propagation |
| §7 RQ3; §§7.1–7.3 | 14–16 | Defense families, enforcement, isolation, tradeoffs |
| §8 RQ4; §§8.1–8.4 | 16–19 | Benchmark reuse, metrics, stronger evaluation |
| §9 Discussion; §§9.1–9.4 | 19–23 | Prior-survey positioning and engineering priorities |
| §10 Threats to Validity | 23 | Category, annotation, search, preprint, retrieval biases |
| §11 Conclusion | 23–24 | Reiterates the shift toward governable systems |
| Acknowledgments; References | 24–35 | Funding and 255 numbered bibliographic entries |
| Appendix A; A.1–A.4 | 36–37 | Query, expansion prompt, exclusions, reliability, rubric |
| Appendix B | 38 | Normalized venue distribution |
| Appendix C; C.1–C.3 | 39–40 | Two co-occurrence matrices and scenario defense stacks |

The inventory contains four explicit research questions, seven figures, eleven tables, one principal semi-formal tuple, and transition notation. There are no formal hypotheses, numbered mathematical theorems, proofs, pseudocode algorithms, or newly executed attack/defense experiments reported in this survey. The substantive analyses are corpus construction, annotation reliability, distributions, lifecycle/surface synthesis, threat synthesis, defense synthesis, benchmark/metric synthesis, and prior-survey positioning.

## 3. Background and context

[A] An LLM agent is defined by an agentic loop rather than by a particular application. A model participates in interpreting goals, planning, selecting tools, executing actions, updating state, monitoring progress, or coordinating with other agents (§2.2, pp. 4–5). Autonomy can be partial: the survey includes autonomous and semi-autonomous workflow components.

A **prompt injection** introduces instructions intended to redirect the model's behavior. **Indirect prompt injection** places those instructions in something the agent encounters while doing its task, such as a web page, retrieval result, file, or tool response. The key issue is source authority: relevant content is not necessarily authorized to direct the agent. The authors distinguish data from control and low-authority observations from privileged instructions (§§5.1–5.2, pp. 9–10).

**Delegated authority** means the agent acts with permissions provided by a user or organization. The attacker may lack those permissions but influence a decision made by the agent that possesses them. **Control-flow hijacking** means redirecting the sequence of planning and action. **Persistent state** means retained information that can influence future interactions. **Memory poisoning** corrupts that state so later decisions reuse contamination. **Data exfiltration** means leaking sensitive information through outputs, tools, or external services. **Containment** limits the effects of a compromise even when its initial entry was not prevented.

[A] The paper distinguishes nine lifecycle labels: Input, Planning, Decision, Tool Execution, Output, Memory, Monitoring, Inter-agent Comms, and Coordination. These annotation labels are related to, but not identical with, the seven elements of its agent tuple. Monitoring and the two coordination-related labels provide finer annotation detail than the tuple's broad coordination element. A paper can receive multiple lifecycle labels.

[D] An illustrative web-agent failure path is: a page provides useful task data together with a hostile instruction; the agent treats the instruction as a planning requirement; it chooses a tool action outside the user's intended task; the action produces an external effect. This is an explanatory illustration of the authors' model, not a specific newly measured incident in this paper.

## 4. Research problem and gap

**Existing problem [A].** Once language-model outputs guide tools, files, state, and external actions, failure extends beyond problematic generated text. The system can perform unauthorized operations, disclose information, corrupt memory, or spread malicious instructions (§1, p. 2; §2.2, p. 5).

**Shortcomings attributed to earlier approaches [A].** The literature is fragmented across attack names, defense layers, domains, and evaluation settings. Previous surveys provide useful specialized coverage but often organize topics separately, without the combined lifecycle model, annotation transparency, defense tradeoff analysis, benchmark synthesis, and deployment-assurance perspective sought here (§1, p. 3; §9.1, pp. 19–20). This is the authors' positioning, not an independently verified assessment of all prior surveys.

**Research gap [A].** The authors seek a common account of how information becomes control, control becomes action, and action produces durable consequences. They want threats, defenses, and evaluations compared by the transitions they affect, rather than merely listed as disconnected techniques.

**Motivation [A].** Fast literature growth and evolving deployment capabilities create a need for synthesis. The field's terminology, threat models, evaluation protocols, and deployment assumptions remain unsettled. Immediate attack success in bounded settings is insufficient to justify trust in long-running systems.

**Scope [A].** The review focuses on security with an explicit agentic surface. It is broader than prompt security and narrower than generic artificial-intelligence safety. Web agents are one substantial scenario alongside coding, memory-augmented, embodied, finance, healthcare, and multi-agent systems. It does not treat every failure of an LLM-enabled application as an agent-security problem (§5, p. 8).

## 5. Research questions, objectives, and hypotheses

The four explicit questions appear in §3.1, p. 6:

1. **RQ1 — LLM Agent Security Scope and Modeling:** How can LLM agent security be scoped and modeled as an agentic systems security problem?
2. **RQ2 — Threat Surfaces and Attack Families:** What threat surfaces and attack families dominate current research on LLM agent security?
3. **RQ3 — Defense Strategies and Tradeoffs:** What defense mechanisms have been proposed to secure LLM agents, and what tradeoffs do they introduce?
4. **RQ4 — Evaluation Practices and Benchmark Gaps:** How is LLM agent security evaluated, and what gaps remain in existing benchmarks and empirical methodologies?

[A] RQ1 supplies common vocabulary. RQ2–RQ4 are interdependent: threats determine defense targets and benchmark failure modes; defenses depend on safety/utility measures and reshape assumptions; evaluations expose coverage gaps and assess defensive effectiveness. Figure 2 makes these relationships explicit.

The objectives are to curate and annotate a corpus; connect surfaces to lifecycle stages; explain dominant and emerging propagation patterns; classify defenses by intervention, asset, assumption, and tradeoff; and inspect benchmark coverage, reuse, metrics, and realism. No formal hypotheses are specified, and no hypothesis significance tests are reported.

[D] The user's web-agent-versus-standalone question is an analytical application of these objectives. It is not one of the paper's formal RQs. Its most direct evidence comes from §§1–2 and RQ1's data/control and authority distinctions, supplemented by RQ2's web scenario counts and Appendix C.2's browser defense recommendations.

## 6. Assumptions / Threat Model

[A] The system model assumes a language model is embedded in surrounding orchestration, tools, state stores, permission mechanisms, monitors, and possibly human oversight. Security behavior emerges from their interaction. Model decisions can vary with sampling, prompt composition, retrieved content, retained state, and model updates even when surrounding code is unchanged (§1, p. 2; §2.1, p. 4).

The review does **not** specify one uniform attacker capability set for all 247 papers. It synthesizes heterogeneous threat models. Supported entry paths include hostile user instructions, malicious web content, poisoned retrieval, misleading tool outputs or metadata, files/code, memory corruption, and inter-agent messages. Supported consequences include unsafe action selection, privilege misuse, information leakage, delayed compromise, and workflow-level propagation.

[A] The principal boundary assumption is that task relevance does not confer authority. A fetched page or tool output may be useful evidence without being permitted to change the user's goal, grant permissions, or issue instructions. The agent's ability to execute or communicate is the source of operational leverage. Memory changes the time scale of attack effects, while communication changes their distribution across agents.

Trusted components depend on the defense family. Instruction ordering remains model- or wrapper-mediated. Runtime enforcement depends on observable trajectories and adequate policies. Access control depends on permission granularity and capability scoping. Isolation and sandboxing depend on supporting infrastructure. Communication defenses depend on message or topology visibility. The survey does not establish that these enforcement components are always trustworthy or immune to attack (Table 3, p. 15).

No shared attacker budget, universal white-box/black-box assumption, fixed maximum number of steps, common permission configuration, or identical target model is reported. It would be incorrect to combine corpus frequencies as if every study used the same attacker or deployment conditions.

## 7. Methodology

### Review design and retrieval

[A] This is a manually screened and annotated literature survey, not a source-code audit or pooled experimental meta-analysis. The declared search window is 1 January 2023 through 27 April 2026 (§3.2, p. 6). The hybrid retrieval pipeline has three inputs: database search, LLM-assisted expansion, and backward/forward citation snowballing.

The six named sources are ACM Digital Library, IEEE Xplore, Scopus, Web of Science, arXiv, and Google Scholar (§3.2, p. 7). The rationale is cross-disciplinary coverage and timeliness: relevant work spans security, systems, software engineering, machine learning, and natural language processing (NLP), with unstable terminology and recognizable framework/benchmark names.

Appendix A.1, p. 36, supplies a Boolean template with three AND-connected groups. The first includes large language model, language model, and LLM. The second includes agent, tool-using agent, web agent, coding agent, browser agent, computer-use agent, memory-augmented agent, embodied agent, multi-agent, and agentic workflow. The third includes security, safety, prompt injection, jailbreak, memory poisoning, tool misuse, data exfiltration, access control, sandboxing, runtime monitoring, guardrail, benchmark, and red teaming. Phrase syntax and field selectors are adapted to search interfaces while normalized concept groups are retained.

[A] GPT-5.4 with web search is used as a bounded retrieval assistant. It suggests lexically distant papers, query variants, aliases, and missing branches. It does not decide inclusion. Candidate identities and relevance are manually checked. The assistant receives seed metadata and concept groups; its requested output includes title, year, venue/source, relevance reason, and discovery cue, with uncertainty flagged. No model sampling settings, exact tool configuration, execution log, or complete list of suggestions is supplied. This report describes the paper's use of that model without externally verifying it.

Backward snowballing traces earlier attack, defense, and benchmark foundations. Forward snowballing finds later reuse and extension. Representative seeds include surveys and benchmarks; the rationale is recovery of architectural or benchmark lineage that exact keyword overlap may miss.

### Screening and normalization

[A] The initial pool has 209 database records, 42 expansion records, and 24 snowballing records. Screening removes 24 of 275 records; normalization merges four duplicate versions or preprint/publication pairs; 247 studies remain (§3.3, p. 7). [C] The reconciliation is 209 + 42 + 24 = 275; 275 − 24 − 4 = 247. Here four is the reported reduction in record count during identity normalization, not a count of four additional substantive exclusions.

Eligibility requires substantive LLM-agent security and an explicit surface such as planning, tools, external action, persistent state, runtime infrastructure, embodied interaction, Model Context Protocol (MCP) or skill interfaces, or multi-agent communication. Screening uses titles, abstracts, and full text when necessary. Table 8 partitions exclusions into generic prompt-security work without an agentic loop (12), broad indirectly relevant safety/privacy/governance work (5), autonomous/agentic work where security is not central (4), and capability-oriented benchmarks (3). Their sum is 24.

### Annotation and synthesis

[A] Three authors independently annotate all 247 papers. Fields include bibliographic metadata, primary paper type, system setting, topic, scenario, threat model, attack surface, lifecycle stage, benchmark, metric, and attack/defense method (§3.4, p. 7). Paper type and system setting are single-label; technical dimensions are multi-label. Each controlled multi-label category is encoded as a binary present/absent decision for agreement calculation.

The reported overall Fleiss' κ is 0.86 before harmonization. Table 9 gives field values: primary paper type 0.90; system setting 0.96; lifecycle stage 0.84; threat surface 0.81; attack family 0.80; defense method 0.78; benchmark usage 0.87; evaluation metric 0.82. Disagreements are discussed jointly, with final synthesis using harmonized labels. These values concern annotation agreement, not correctness of the reviewed experiments or consensus on defensive effectiveness.

The supplied paper reports no training/test splits, target-agent hyperparameters, hardware benchmark configuration, repeated attack runs, confidence intervals for pooled attack effectiveness, or common experimental baseline. Such details are not applicable as a single configuration to this review. Reviewed benchmark scores are not pooled into a cross-system performance estimate. The survey's quantitative findings are primarily coded-paper counts and descriptive distributions.

## 8. Experiments / Analyses

The paper reports analyses rather than new attack experiments. They must be kept distinct.

| ID | Analysis and purpose | Data/setup | Measures and evidence | Caveat |
|---|---|---|---|---|
| X1 | Corpus construction: establish review sample | Three retrieval routes, screening, identity normalization | 275 candidates → 247 retained; Table 8 | Recall and exclusions are not independently reproducible from the paper alone |
| X2 | Annotation reliability: assess coding consistency | Three independent annotations of 247 studies | κ = 0.86 overall; Table 9 field values | Agreement is pre-harmonization; final labels are adjudicated |
| X3 | Trend observation: characterize literature | Single-label year/type/setting and normalized venue identity | Figure 3; Table 10 | Counts describe research activity, not real-world risk |
| X4 | RQ1 modeling: relate entry surfaces to stages | Multi-label surface/lifecycle codes | Table 1; Figure 6 | Cell sums are not distinct-study totals |
| X5 | RQ2 threats: identify families and propagation | Threat-model codes and scenario co-occurrences | Table 2; Figure 4; web scenario counts | Threat-model, topic, and attack-method fields differ |
| X6 | RQ3 defenses: locate protection and gaps | Defense categories and engineering synthesis | Table 3; Figure 5; Table 11 | No universal stack or pooled efficacy experiment |
| X7 | RQ4 evaluation: inspect reuse and reporting | Benchmark and metric annotations | Tables 4–5; Figure 7 | Reuse is not benchmark quality or intrinsic coverage |
| X8 | Prior-survey positioning | Eight referenced surveys plus this review | Table 6; Appendix A.4 rubric | Qualitative, author-assigned emphasis ratings |

[A] X3 finds 3 papers in 2023, 42 in 2024, 121 in 2025, and 81 collected in the partial 2026 window. X4 finds Planning and Input particularly common. X5 identifies prompt injection as the dominant threat-model label and persistence/propagation as important expansions. X6 identifies concentration around plan scrutiny and tool gating. X7 identifies fragmented reuse and sparse utility/latency/cost reporting. X8 supports the authors' claim of a combined relational perspective, not an objective leaderboard of survey quality.

There are no manipulated independent variables, randomized controls, common intervention arms, formal experimental hypotheses, or shared attack-success outcomes for these analyses. Their evidence is descriptive classification plus reasoned synthesis. The register does not relabel reviewed experiments as experiments performed by the survey authors.

## 9. Results

### Literature composition

[A] The 247-paper sample is temporally concentrated: 121 studies are assigned to 2025 and 81 to the partial 2026 collection period. The latter represents 32.79% of the corpus; it is not a full-year total or an annual growth estimate (§4, p. 7). Primary types are Attack 66, Defense 64, Benchmark 47, Survey 32, Evaluation 26, and Report 12. Attack plus defense account for 52.63% (§4, p. 8).

Single-agent systems account for 200 papers (80.97%); multi-agent systems for 47 (19.03%). Multi-agent annual shares are 9.52% in 2024, 23.97% in 2025, and 17.28% in partial 2026. These support growing attention to coordination, but the sequence is not monotonically increasing. Figure 3 rounds percentages to one decimal place; the prose provides greater precision.

### Lifecycle and surface results

[A] Research-topic frequencies are Tool-use Security 156, Runtime Defense 88, Prompt Injection Security 75, Multi-agent Security 63, and Memory Safety 32 (§5, p. 9). Lifecycle counts are Planning 227, Input 225, Tool Execution 209, Decision 166, Output 151, Memory 82, Monitoring 58, Inter-agent Comms 35, and Coordination 20.

Threat surfaces include User Prompts 82, Web Content 55, Tool Outputs 54, Retrieved Content 37, and Memory/Scratchpads 25. Files/Code, Planning Loop, and Inter-agent Channels each occur in at least 25 papers (§5.1, p. 9). Multi-label counts overlap. A count of 55 Web Content papers and 54 Tool Outputs papers cannot be added to obtain 109 distinct affected studies.

### Threat families and deployment conditions

[A] Table 2 reports Prompt Injection 142, Indirect Prompt Injection 86, Unsafe User Instructions 43, Malicious Tools 34, Data Exfiltration 31, Memory Poisoning 24, and Coordination Failures 14. These are threat-family/threat-model annotation frequencies, not attack success rates, incident prevalence, or severity rankings. The paper separately describes normalized attack-method prominence without supplying corresponding method counts here (§6.1, pp. 11–12).

Web Browsing has 93 scenario-coded papers. Within scenario/threat co-occurrences, Prompt Injection appears 71 times and Indirect Prompt Injection 44 times. Software Engineering has 63 scenario papers, with corresponding threat counts 32 and 16. Finance Tools has 34 scenario papers; Healthcare Assistance and Embodied Robotics each have 28 (§6.2, p. 13). Multi-agent Collaboration co-occurs with Prompt Injection 44 times, Memory Poisoning 14, and Coordination Failures 14. Because technical fields are multi-label, these are overlapping observations, not mutually exclusive failure categories.

[A] The authors emphasize consequence asymmetry: frequently studied scenarios are not necessarily those with the most costly consequences. Finance, healthcare, and embodied actions may involve stronger confidentiality, integrity, or physical-world stakes. This is their interpretive synthesis, not a numerical harm comparison.

### Defense and evaluation results

[A/B] Figure 5 shows layer totals of Instruction Handling 2, Planning Validation 11, Tool Gating 13, State Protection 2, and Execution Containment 2. The figure's categories and counts are distinct from the broad Runtime Defense topic count of 88; the paper does not fully specify their denominator or subset relationship. The defensible result is concentration within the displayed normalized categories, not a claim that only 30 corpus papers address defense.

AgentDojo is reused in 30 papers and InjecAgent in 11; Table 4 reports annotation shares of 12.82% and 4.70%. These percentages use total benchmark annotations, not 247 papers. Metric counts are Attack Success Rate 129, Success Rate 59, Accuracy 41, Utility 22, Recall 19, F1 15, Precision 14, Refusal Rate 13, False Positive Rate 13, Latency 8, and Cost 7 (Table 5).

The results support an imbalance in what is measured. They do not show that a specific defense causes a particular reduction in attack success or that any named benchmark is inadequate for its own intended scope.

## 10. Figure-by-figure interpretation

### Figure 1 — Analytical framework of the survey, p. 5

[B] This is a four-band workflow diagram, not a statistical chart. Blue labels identify review design, unified framework, research questions, and synthesis outcomes. The top pipeline moves through retrieval, LLM-assisted expansion, snowballing, manual screening, and structured labeling, with 247 curated papers prominently shown. The central flow connects Input → Planning → Decision → Tool Execution → Output. Memory/state and coordination are connected below, showing their cross-cutting relationship to the main sequence. Information flow, delegated authority, and persistent state frame the system interpretation.

The lower bands connect RQ1–RQ4 to trust boundaries, privilege control, state management, and deployment assurance. There are no axes, units, error bars, or measured effect sizes. The figure supports methodological coherence: the same lifecycle lens structures corpus coding and synthesis. It does not depict a deployed security architecture tested by the authors.

### Figure 2 — Relationships among research questions, p. 6

[B] RQ1 is a blue upper box supplying the systems vocabulary. RQ2, RQ3, and RQ4 form a lower triad inside a dashed enclosure: threats/failure, defenses/constraints, and evaluation/evidence. Bidirectional relationships state that threats define defense targets and benchmark failures; defenses reshape assumptions; evaluations reveal gaps and assess effectiveness; defenses require safety/utility metrics.

There are no numerical axes or statistical quantities. The figure explains why an attack taxonomy cannot be interpreted independently of defensive assumptions and evaluation coverage. Arrow direction expresses conceptual dependence, not causal effects estimated from data.

### Figure 3 — Corpus distributions, p. 8

[B] Three pie charts show (a) publication year, (b) primary paper type, and (c) system setting. Each uses categorical colors and labeled counts/percentages. Panel (a) emphasizes 42 papers in 2024, 121 in 2025, and 81 in partial 2026; the tiny 2023 slice corresponds to 3, as stated in prose. Panel (b) shows Attack 66, Defense 64, Benchmark 47, Survey 32, Evaluation 26, and Report 12. Panel (c) shows Single-agent 200 and Multi-agent 47.

These are composition percentages of 247 papers, not longitudinal incidence rates. Pie charts have no x/y axes, error bars, or confidence intervals. Rounded visual labels such as 81.0% and 19.0% agree with the prose's 80.97% and 19.03%. The figure supports fast growth and uneven architectural coverage, with a partial-year caveat for 2026.

### Figure 4 — Three attack propagation patterns, p. 13

[B] Panel (a) connects Web Content (55), Tool Outputs (54), and Retrieved Content (37) to Input (225), Planning (227), and Tool Execution (209). Panel (b) connects Memory Surface (25) to Stored State (82), Later Planning (227), and Action (209). Panel (c) shows a compromised agent reaching three peers, then Coordination (20), then External Effect. Distinct panels separate mediated entry, delayed memory activation, and message-level spread.

The arrows are schematic paths. Counts refer to corpus annotations for different nodes; they are not counts of attacks observed traversing an entire path. The figure reports no transition probabilities, elapsed time, propagation rates, or measured peer infection likelihood. It supports the author's distinction among entry, persistence, and distributed amplification.

### Figure 5 — Defense layers and coverage gaps, p. 16

[B] Five blue horizontal layers show Instruction Handling 2; Planning Validation 11; Tool Gating 13; State Protection 2; Execution Containment 2. Subcategories are Guardrails 1 and Instruction Hierarchy 1; Runtime Monitoring 6, Policy Enforcement 3, Anomaly Detection 2; Access Control 8 and Information-flow Control 5; Context Isolation 2; Sandboxing 2. A red dashed gap area lists Provenance, Revocation, Inter-agent trust, and Topology-aware containment.

The figure has no performance axis or protective-strength scale. Layer ordering represents engineering intervention points. The displayed counts support relative concentration among these categories. Their exact coding denominator is not explicit in the supplied explanation. The visual therefore cannot establish a total defense prevalence or effectiveness ranking.

### Figure 6 — Lifecycle-by-surface heatmap, p. 39

[B] Rows are eight threat surfaces; columns are nine lifecycle stages. Labeled cells are exact paper-level co-occurrence counts. Blue shading supplies an additional magnitude cue; the accompanying legend uses uneven numerical reference points, so this report makes no assumption of a linear perceptual color scale. No error bars or significance markers appear. The matrix is transcribed in its original column order:

| Surface | Input | Planning | Decision | Tool execution | Output | Memory | Monitoring | Inter-agent comms | Coordination |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| User Prompts | 82 | 82 | 60 | 76 | 49 | 36 | 7 | 5 | 1 |
| Web Content | 53 | 53 | 35 | 51 | 33 | 19 | 12 | 3 | 1 |
| Tool Outputs | 50 | 54 | 41 | 54 | 30 | 20 | 15 | 1 | 0 |
| Retrieved Content | 36 | 35 | 26 | 35 | 21 | 13 | 9 | 1 | 1 |
| Memory / Scratchpads | 19 | 23 | 11 | 20 | 11 | 25 | 5 | 5 | 4 |
| Inter-agent Channels | 19 | 21 | 15 | 7 | 11 | 9 | 5 | 21 | 16 |
| Files / Code | 26 | 24 | 15 | 25 | 20 | 4 | 9 | 2 | 0 |
| Planning Loop | 20 | 25 | 17 | 18 | 13 | 6 | 7 | 7 | 2 |

The matrix shows cross-stage involvement of direct prompts and mediated content. Memory/Scratchpads peaks at Memory 25; Inter-agent Channels peaks at Inter-agent Comms 21, with Coordination 16. An important text–figure discrepancy is that nearby prose says Inter-agent Channels align most strongly with Coordination. In the visible row, Inter-agent Comms is larger. The conceptual relation to coordination may be broad, but the strongest displayed cell is not the Coordination column. This report preserves both rather than correcting the authors silently.

### Figure 7 — Benchmark co-occurrence heatmap, p. 40

[B] Rows are eight benchmarks. Twenty-one columns are grouped into Threat Surface, Lifecycle, Scenario, and Reporting. Six surface columns cover User, Web, Tool Out, Retrieved, Memory, Inter-agent; six lifecycle columns cover Input, Plan, Tool Execution, Memory, Inter-Comms, Coordination; six scenario columns cover Web, Software Engineering, Multi-agent, Embodied, Finance, Health; three reporting columns cover Utility, Latency, Cost. Blue shades and exact cell labels encode counts; there is no statistical uncertainty or benchmark-quality score.

For compactness, each row below preserves those four groups in order:

| Benchmark | Surface counts: U/W/T/R/M/IA | Lifecycle: I/P/T/M/IC/C | Scenario: W/SE/MA/E/F/H | Reporting: U/L/C |
|---|---|---|---|---|
| AgentDojo | 7/15/23/11/3/0 | 26/29/30/10/1/0 | 13/3/3/1/20/2 | 16/4/0 |
| InjecAgent | 5/2/5/3/2/0 | 11/10/11/4/1/0 | 5/1/3/2/4/2 | 1/0/0 |
| MMLU | 0/0/0/0/0/2 | 3/3/3/1/2/5 | 4/0/1/5/0/0 | 1/0/0 |
| ASB | 1/4/4/0/1/0 | 3/4/4/3/0/0 | 1/1/0/0/3/1 | 3/1/0 |
| SafeAgentBench | 1/0/0/0/0/0 | 3/4/4/1/0/0 | 0/1/1/4/0/1 | 0/0/0 |
| R-Judge | 1/0/2/1/0/0 | 3/3/3/0/0/0 | 2/1/0/0/2/0 | 0/0/0 |
| OSWorld | 1/2/0/1/0/0 | 3/3/3/0/0/0 | 1/1/0/0/0/0 | 0/0/0 |
| JailbreakBench | 2/0/0/0/0/2 | 3/3/1/2/2/2 | 1/1/3/0/0/0 | 0/0/0 |

AgentDojo's notable cells include Tool Outputs 23, Input 26, Planning 29, Tool Execution 30, Finance 20, Utility 16, and Latency 4. InjecAgent has Input 11, Planning 10, Tool Execution 11, and Utility 1. All displayed Cost cells are zero. That does not mean cost is absent from the whole corpus: Table 5 reports Cost in seven papers. The matrix includes only these reused benchmark rows.

[A] Each cell describes papers where a benchmark label co-occurs with another annotation. It is not an intrinsic property of benchmark tasks. For example, a study may use MMLU alongside other evaluations in a multi-agent setting. The row cannot be read as proof that MMLU itself contains particular security scenarios. The authors make this distinction explicit.

## 11. Table-by-table interpretation

### Table 1 — Core modeling dimensions, p. 9

Rows combine selected lifecycle stages and threat surfaces; columns give paper counts and why each matters. Planning 227 and Input 225 emphasize interpretation and sequencing; Tool Execution 209 emphasizes capability crossing; Decision 166 connects reasoning to behavior; Memory 82 makes delayed compromise possible. Surface rows list User Prompts 82, Web Content 55, Tool Outputs 54, Retrieved Content 37, and Memory/Scratchpads 25. This is a selected descriptive table, not an exhaustive partition or performance comparison. No baseline, significance test, or uncertainty interval appears.

### Table 2 — Threat families and propagation, p. 12

Seven rows pair counts with common surfaces/scenarios and propagation patterns. Prompt Injection 142 redirects planning/action selection; Indirect Prompt Injection 86 enters through mediated content; Unsafe User Instructions 43 concerns harmful task acceptance; Malicious Tools 34 concerns tool-mediated reasoning/invocation; Data Exfiltration 31 concerns information leakage; Memory Poisoning 24 concerns delayed reuse; Coordination Failures 14 concerns amplification through delegation. The largest count denotes research prominence, not the most successful or severe attack. Overlap prevents summing rows into a unique-study total.

### Table 3 — Defense families and tradeoffs, p. 15

Six rows cover input-trust management, runtime monitoring/guard agents, access control/least privilege, information-flow/state isolation, execution containment, and topology-aware multi-agent containment. Columns identify tuple transitions, protection goals, and failure modes. Input handling depends on source distinctions surviving paraphrase and restatement; runtime monitoring can add latency or over-block; access control needs permission granularity; state isolation needs provenance or typed interfaces; containment can reduce autonomy and compatibility; topology defenses require message/topology visibility and may fail against covert collusion. There are no numerical efficacy scores, rankings, or universal best method.

### Table 4 — Benchmark reuse, p. 17

Counts and annotation shares are AgentDojo 30/12.82%; InjecAgent 11/4.70%; MMLU 5/2.14%; ASB 4/1.71%; SafeAgentBench 4/1.71%; R-Judge, OSWorld, and JailbreakBench each 3/1.28%. Shares use total benchmark annotations because one paper can use multiple benchmarks. The table supports weak concentration of reuse. It does not compare attack rates or rank benchmark scientific quality. The total annotation denominator is not printed explicitly; reconstructing it from rounded percentages would be an analyst derivation, so no exact denominator is asserted here.

### Table 5 — Metrics and what they miss, p. 18

Eleven rows contrast common measures with omitted dimensions. Attack Success Rate 129 captures immediate attacker objectives but may miss utility, delayed harm, and cost. Success Rate 59 captures completion but not alignment. Accuracy 41 captures labeled correctness but not action consequences. Utility 22 misses fine-grained safety failures. Recall 19 misses precision/tradeoffs; F1 15 misses latency/cost/task usefulness; Precision 14 misses missed attacks/long-term effects. Refusal Rate 13 does not establish appropriate refusal; False Positive Rate 13 does not establish broader task success. Latency 8 and Cost 7 measure overhead without proving protection. These are metric usage counts, not metric values measured on one agent.

### Table 6 — Positioning against prior surveys, p. 20

Eight referenced surveys are compared with this survey across Search Protocol, Lifecycle Framing, Tools/Runtime, Memory/State, Multi-agent, Benchmark Synthesis, and Systems/Assurance Framing. Reference rows are [35], [58], [55], [47], [221], [177], [159], and [143]. Most earlier search/lifecycle ratings are Partial; [58] is Limited for both and [177] has No lifecycle framing. Tools/runtime is Broad for [35], [55], [221], and [159]. Memory/state is Broad for [159]; multi-agent is Broad for [143]. Benchmark synthesis is Limited in most rows and No for [58] and [47]. This survey is rated Explicit, Central, Broad, Broad, Broad, Dedicated, Dedicated.

Appendix A.4 defines these qualitative labels. They assess analytical emphasis, not overall quality or factual correctness. Prior-survey strengths are complementary; the authors do not claim previous work has no value or no coverage. Exact bibliography titles are not reproduced here because the table's reference IDs provide the document's own traceability.

### Table 7 — Research priorities, p. 21

Five challenges connect current evidence gaps with proposed directions. Provenance-aware state management calls for authority tags, trust decay, revocation, and replayable histories. Secure tool governance calls for capability scoping, effect typing, confirmation, and reversible execution. Multi-agent trust management calls for role-scoped authority, message integrity, trust attenuation, and topology containment. Lifecycle evaluation calls for longer horizons and step-level traces. Deployment assurance calls for combined threat models, runtime controls, telemetry, fallback, and empirical evidence. This is a forward-looking agenda, not tested intervention results.

### Table 8 — Exclusions, p. 36

The four mutually assigned reasons have counts 12, 5, 4, and 3, totaling 24. Unlike most technical annotation tables, these rows partition the excluded records. The table clarifies why generic prompt-security and capability-only work can inform background without entering the agent-security sample. It does not provide individual excluded titles or adjudication histories.

### Table 9 — Annotation reliability, p. 37

Eight fields show encoding, Fleiss' κ, and boundary-resolution focus. System setting is highest at 0.96; primary type is 0.90; benchmark usage 0.87; lifecycle 0.84; metric 0.82; surface 0.81; attack family 0.80; defense method lowest at 0.78. More granular, overlapping fields demand finer judgments. Values are before harmonization; final synthesis uses adjudicated labels. No confidence intervals, chance-model details, or per-label agreement counts are supplied. The overall 0.86 should not be interpreted as identical reliability across fields.

### Table 10 — Normalized publication venues, p. 38

The 247-paper partition is Informal 181 (73.28%), Conference 55 (22.27%), Journal 11 (4.45%). Informal entries are arXiv 169 (68.42%) and Web 12 (4.86%). Conference counts are ICLR 12, ACL 10, EMNLP 8, NeurIPS 6, ICML 5, NDSS 3, COLM 2, NAACL 2; AAAI, ACM MM, AIES, ICSE, IJCAI, ICRA, and ACM CCS each 1. Journal rows each contain one paper: ICT Express, AI, Information Fusion, Information Sciences, ACM Computing Surveys, High-Confidence Computing, Frontiers in Computer Science, Journal of Systems and Software, Future Generation Computer Systems, Journal of Artificial Intelligence Practice, and Foundations and Trends in Privacy and Security.

Findings papers are grouped with parent ACL-family venues; workshops are grouped only when the relationship is explicit. Duplicate/preprint-publication identities count once under final normalization. Venue identity differs from primary paper function. The table reports 66 formal papers across 26 outlets; it is not evidence that informal studies are false or that archival studies are deployment-ready.

### Table 11 — Scenario-oriented defense stacks, p. 39, qualification p. 40

Browser/web agents need input-trust management, runtime plan/action checks, gating or confirmation, and containment for high-authority actions. Coding agents need least privilege for file/shell/package operations, monitoring, and isolated execution. Memory assistants need provenance-aware isolation, revocation/decay, and checks before memory-derived action. Multi-agent workflows need role-scoped authority, communication monitoring, topology containment, and per-agent privilege control.

Open problems differ: source separation and useful injection defenses for browsers; tool APIs, dependencies/skills, and long-chain regression for coding; trust labels and delayed-trigger realism for memory; covert collusion, message provenance, distributed rollback, and graph-wide containment for multi-agent systems. Page 40 explicitly calls the table an engineering interpretation rather than a validated standard. Its heading's word 'Minimal' must therefore not be read as a formally proven sufficient or necessary control set.

## 12. Diagram / Architecture Interpretation

The substantive diagrams are Figures 1, 2, 4, and 5; their individual content is accounted for above. Together they form a reasoning architecture for the survey, not a delivered software system.

Figure 1 connects corpus inputs to annotation, then lifecycle analysis, then RQs and engineering themes. The principal information/control sequence is Input → Planning → Decision → Tool Execution → Output. Memory can preserve prior information and feed later planning; coordination brings monitors, humans, or peer agents into the loop. Figure 2 establishes dependency among analysis questions. Figure 4 separates three security paths: external mediation, temporal persistence, and distributed propagation. Figure 5 locates defensive interventions from interpretation through execution and highlights gaps outside the densest studied transitions.

[A] The paper emphasizes transitions because a component can be individually useful yet unsafe when its output acquires a different kind of authority. A retrieval result becoming a planning constraint, a tentative plan becoming a tool call, or a stored trace becoming trusted context can each cross a meaningful boundary (§5.2, p. 10).

[D] For web agents, the architecture-based vulnerability explanation has four connected parts: repeated exposure to external content; interpretation of that content alongside task instructions; action selection under delegated permissions; and possible reuse of resulting tool feedback or state. Memory and multiple agents are conditional amplifiers, not defining requirements for every browser agent. The paper does not imply that a browser agent necessarily has shell access, unrestricted memory, or multi-agent delegation.

No implementation diagram supplies service endpoints, concrete schemas, policy syntax, enforcement code, hardware, or a fully executable control plane. The proposed security control plane is a research direction encompassing provenance, permissions, memory lifecycle, communication boundaries, runtime policy, telemetry, and recovery (§9.2, p. 21).

## 13. Equations and mathematical concepts

### E1 — Semi-formal agent tuple, §5, p. 8

The principal expression is **A = ⟨I, P, D, T, M, O, C⟩**. It is a structured representation of an agent, not a numerical computation or optimization objective.

| Symbol | Author-defined meaning | Plain-language role |
|---|---|---|
| A | LLM agent representation | The combined system under analysis |
| I | Inbound context and observations | What the agent receives or sees |
| P | Planning over candidate trajectories | Possible sequences of steps |
| D | Commitment to a next action or delegation | Which step the system chooses |
| T | Tool or environment execution | Carrying out the chosen operation |
| M | Transient or persistent state | What the system retains |
| O | Externally visible outputs and side effects | What other systems/users observe |
| C | Coordination channels with monitors, humans, or peers | How control-related communication occurs |

Angle brackets denote the collection of conceptual elements. The expression has no numeric inputs, scalar output, constraints, loss function, proof, or learned parameters. It provides vocabulary for identifying attack entry and defensive intervention. Importantly, tuple order places M before O, whereas Figure 1's main horizontal path leads from T to O with memory below; the tuple is a collection of roles, not a prescribed chronological execution order.

### E2 — Transition notation, pp. 12 and 15

Arrows identify influence or intervention paths, not estimated probabilities. Injection primarily targets I → P and I → D. Malicious tools/exfiltration become operational at D → T and T → O. Memory poisoning targets I/T → M followed by M → P. Coordination failures affect C → P and C → D. I/T means either information input or tool execution as a source; P/D/T in Table 11 groups possible destinations. Bidirectional I ↔ M indicates interaction between context and stored state. No formal transition function or state-space semantics is defined.

### E3 — Fleiss' κ, pp. 7 and 37

[A] Fleiss' κ is used as an inter-annotator agreement statistic, reported overall and by field. The supplied document explains categorical versus binary-vector encoding and pre-harmonization calculation but does not give the statistic's formula or complete raw agreement data. No external formula is introduced here. The reported number describes agreement among three annotators, not causal security effects.

### Reproducible arithmetic [C]

The corpus reconciliation is 209 + 42 + 24 − 24 − 4 = 247. Publication-year counts sum to 3 + 42 + 121 + 81 = 247. Paper-type counts sum to 66 + 64 + 47 + 32 + 26 + 12 = 247. Setting counts sum to 200 + 47 = 247. Venue subtotals sum to 181 + 55 + 11 = 247. These checks confirm internal arithmetic consistency; they do not validate search completeness or annotation accuracy.

## 14. Interpretation and discussion

**RQ1 answer [A].** Security should be modeled as interaction among information flow, delegated authority, and persistent state. The importance of the tuple is its attention to transitions. Prompt injection can disrupt planning and execution, memory poisoning can become delayed control-flow compromise, and coordination can become a trust/propagation problem (§5.3, p. 11).

**RQ2 answer [A].** Prompt injection and indirect control-flow hijacking dominate current research, while threat models expand toward persistent state corruption, authority abuse, and inter-agent propagation (§6.3, p. 14). Dominance is a literature finding, not a universal incident ranking.

**RQ3 answer [A].** Defenses span instruction handling, monitoring, access control, information-flow control, and containment. They concentrate around input-to-planning and decision-to-execution, while memory and coordination are less consistently protected. Different assumptions and overhead prevent one technique from forming a stable universal stack (§7.3, p. 16).

**RQ4 answer [A].** Evaluation is active but insufficiently standardized for deployment assurance. The authors recommend multiple surfaces, joint safety/utility reporting, longer horizons, privilege-sensitive scenarios, and consistent latency/cost/oversight reporting (§8.4, p. 19).

[D] The strongest answer to 'Why are web AI agents more vulnerable than standalone LLMs?' is conditional and structural. Web agents create an additional path from attacker-controlled observations to actions under another party's authority. They also face repeated multi-source context and possible state reuse. This can broaden entry points, impact, and persistence. The survey does not measure the probability increase caused by each capability, and vulnerability probability must be distinguished from consequence severity.

### Cross-reference and consistency findings

The corpus arithmetic, primary-type totals, setting totals, and venue totals reconcile. Figure 3's rounded percentages agree with prose. Different counts for Prompt Injection Security topic (75), Prompt Injection threat model (142), and web-scenario co-occurrence (71) refer to different coding fields, not contradictory estimates. Likewise Multi-agent Security topic 63 differs legitimately from the single-label multi-agent setting count 47.

Four issues remain unresolved. First, page 1's January 2026 publication formatting precedes the April 2026 search cutoff, May 2026 reference retrieval dates, and August 2026 arXiv version marking. The placeholder DOI reinforces uncertainty about bibliographic status; no external repair was attempted. Second, Appendix C.1's Inter-agent Channels prose emphasizes Coordination, but its largest displayed cell is Inter-agent Comms 21 versus Coordination 16. Third, Figure 5's category counts are not linked to a fully specified denominator or coding subset. Fourth, page 17 initially describes a second tier with ASB/SafeAgentBench at four followed by a list including MMLU, while Table 4 gives MMLU five. The exact table counts are preserved; the informal tier prose should not override them.

## 15. Contributions and novelty

[A] **Conceptual contribution:** a lifecycle/surface framework connecting information, authority, and persistence, with the semi-formal tuple locating attacks, defenses, and evaluation.

[A] **Methodological contribution:** a curated 247-study corpus built through hybrid retrieval, manual screening, identity normalization, and independent multi-label annotation with reported agreement and operational boundary discussion.

[A] **Descriptive empirical contribution:** distributions of year, primary type, setting, venue, topics, stages, surfaces, threat families, benchmark reuse, and metric reporting. These characterize literature attention rather than security effectiveness.

[A] **Synthesis contribution:** linking attack propagation to defensive intervention and benchmark coverage; identifying memory/coordination gaps; and organizing tradeoffs around architecture and deployment stakes.

[A] **Engineering contribution:** scenario-oriented defense guidance and a research agenda for provenance, privilege control, secure orchestration, regression testing, runtime verification, assurance cases, compositional evaluation, and recovery.

The paper reports no new trained model, attack algorithm, implemented universal defense, theorem, benchmark task dataset, or comparative agent-versus-standalone experiment as its own central contribution. The corpus may be an important review resource, but raw annotation files and website content were not supplied. Novelty relative to earlier literature remains the authors' claim; the supplied work supports their stated comparison rubric without independently verifying every earlier survey.

## 16. Limitations

### Authors' stated limitations

[A] Category overlap makes constructs judgment-sensitive: web/retrieval/tool/file/memory content can all be untrusted text, and planning/decision/execution may be tightly interleaved (§10, p. 23). Manual screening and labeling introduce interpretation despite independent annotation and discussion. Search/publication biases can miss unusual terminology, unpublished industrial artifacts, and adjacent system names. A preprint-heavy sample is timely but unstable because titles, claims, and experimental designs can change. LLM-assisted expansion can favor visible benchmarks, popular terminology, and publicly retrievable papers.

[A] Earlier sections also warn that primary paper type compresses multifunction studies, single-agent dominance can underrepresent delegation risks, frequency does not indicate consequence or readiness, and the 2026 count is partial (§4, pp. 7–8). Defenses have varied trust assumptions and costs; a universal stack is unsupported (§7.2, p. 16). Benchmark co-occurrences are not intrinsic benchmark properties (Appendix C.3, p. 40). Table 11 is an engineering interpretation, not a validated standard.

### Additional evidence-based analyst observations

[D] The document lacks a controlled standalone-LLM comparison and cannot quantify a general web-agent vulnerability multiplier. Raw annotations, exact search executions, screening decisions, and assistant outputs are absent, limiting independent reproduction. No formal risk-of-bias appraisal of each included experiment is supplied. Counts therefore treat heterogeneous evidence as research occurrences without establishing comparable evidential strength.

[D] Figure 5's denominator ambiguity limits conclusions about defense prevalence. Table 4's benchmark annotation denominator is described but not explicitly totaled. The overall κ aggregation procedure and uncertainty intervals are not provided. Publication-date markings are internally difficult to reconcile. Appendix C.1 has the noted prose/cell discrepancy. These observations are analyst findings; they are not presented as author admissions.

## 17. Threats to validity

**Construct validity [A].** Categories can overlap semantically and operationally. Multi-label coding and explicit distinctions mitigate this but do not eliminate judgment. The threat-surface/lifecycle matrix should therefore be read as a coded representation, not a natural partition of agent behavior.

**Internal validity [A].** Screening and annotation rely on human judgment. Three independent annotators, conservative boundaries, version normalization, κ reporting, and joint resolution reduce subjectivity. They do not independently establish that every retained paper is correctly interpreted or that agreement implies truth.

**External validity [A].** Six sources, snowballing, and expansion improve coverage but cannot ensure exhaustive discovery. Heavy arXiv representation creates version instability. The review's cutoff bounds its claims; the paper does not describe the entire field beyond that collection period.

**LLM-assisted retrieval bias [A].** The assistant can over-suggest popular/publicly visible work. Its restricted candidate-only role and manual verification address inclusion reliability but cannot prove that obscure candidates were not missed.

**Statistical conclusion validity [D].** There is no pooled efficacy estimate or inferential test of agent vulnerability. Descriptive counts are internally meaningful when their coding field and denominator are retained. They cannot support significance claims, causal capability effects, or uncertainty-free comparisons of security performance.

**Ecological validity [D], grounded in the authors' evaluation critique.** Short-horizon bounded benchmarks may omit real permission configurations, persistent contamination, changing environments, operational overhead, and recovery. This is a limitation of deployment conclusions drawn from the reviewed ecosystem, not a new experiment demonstrating a particular benchmark's failure.

**Reproducibility [D].** The query template, selection rules, agreement values, and normalization rules improve auditability. Without raw corpus data and search logs, an independent reader can reproduce the arithmetic and understand categories but cannot regenerate all counts or assess every individual inclusion decision.

## 18. Future work and open questions

### A. Explicit author proposals

The authors propose provenance-aware memory with source/authority tags, expiration or decay, quarantine, revocation, and replayable histories. They propose first-class tool permissions, capability scoping, effect typing, confirmations, and reversible or containable execution. Multi-agent work should address role separation, message integrity, trust attenuation, and topology-aware containment (§9.2; Table 7).

Evaluation should use longer horizons, multiple surfaces, explicit privilege context, step-level traces, recovery outcomes, and joint safety/utility measures. Version-aware regression should replay hostile tool outputs, injection traces, poisoned states, and communication failures across model, prompt, tool, policy, memory, and orchestration updates (§8.3, pp. 18–19; §9.3, pp. 21–22).

Deployment-oriented assurance cases should combine threat modeling, privilege analysis, runtime controls, benchmark evidence, telemetry, and incident expectations for a specific environment. Compositional evaluation should test whether controls remain meaningful together. Recovery studies should measure suspicious-state detection, rollback, memory quarantine, decision-trace reconstruction, and continued operation under reduced authority (§9.4, pp. 22–23).

### B. Additional open questions [D]

What is the measurable contribution of browsing, tool permissions, repeated interaction, memory, and delegation to vulnerability under matched conditions? Which capability configurations amplify attack probability, and which mainly amplify consequence? How much useful task completion is retained when source-aware mediation and permission restrictions are combined? Can provenance remain intact through summaries and tool restatements? What evidence is sufficient to claim safe recovery after contamination? These follow from the supplied framework but are not answered by the survey's descriptive counts.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning within this analysis |
|---|---|
| LLM | Large language model; the language-processing component used for interpretation and decisions |
| LLM agent | A system using an LLM within an action/state/coordination loop |
| Agentic loop | Repeated interpretation, planning, choice, execution, feedback, and state update |
| Prompt injection | Instructions intended to redirect model/agent behavior |
| Indirect prompt injection | Such instructions embedded in encountered content rather than only direct user input |
| Threat surface | Where hostile influence enters or which asset it touches |
| Lifecycle stage | When or where within the agent workflow that influence acts |
| Data-control ambiguity | Difficulty keeping useful content separate from authorized instructions |
| Delegated authority | Permissions exercised by an agent on a user's or organization's behalf |
| Privilege boundary | A boundary governing what capabilities an actor may exercise |
| Least privilege | Restricting capabilities to the authority needed for the task |
| Control-flow integrity | Preserving the intended and authorized sequence of decisions/actions |
| Tool gating | Checking or restricting a selected tool action before execution |
| Provenance | Information about where content/state came from and its authority |
| Memory poisoning | Contamination retained and reused in future reasoning or action |
| Scratchpad | Intermediate or retained agent state; included with memory surfaces here |
| Revocation | Withdrawing previously granted trust or authority |
| Trust decay | Reducing trust in stored information over time or changed conditions |
| Information-flow control | Restricting how information can move and affect other contexts/actions |
| Context isolation | Separating contexts to limit leakage or contamination |
| Sandboxing | Restricting an execution environment to limit side effects |
| Guard agent | A secondary agent/component checking plans, actions, or policies |
| Topology-aware containment | Limiting propagation with awareness of connections among agents |
| Snowballing | Finding earlier references and later citing/extending studies |
| Multi-label annotation | Allowing one paper to receive several technical labels |
| Harmonization/adjudication | Resolving independent annotation disagreements before synthesis |
| Fleiss' κ | Reported statistic describing agreement among the three annotators |
| Attack Success Rate | Measure of whether attacks achieve their specified objective |
| Utility | Useful task behavior retained under defensive constraints |
| F1 | Named classification measure balancing precision and recall; no formula supplied |
| Telemetry | Execution evidence recorded for monitoring, diagnosis, and evaluation |
| Assurance case | Deployment-specific argument joining assumptions, controls, and evidence |
| MCP | Model Context Protocol, named as a tool/protocol ecosystem in the paper |
| API | Application programming interface, used for tool and framework boundaries |
| CI/CD | Continuous integration/continuous delivery, the development workflow context named by the paper |
| ReAct | Referenced reasoning-and-acting approach; its full algorithm is not supplied |
| A, I, P, D, T, M, O, C | Agent tuple and its elements, defined in section 13 above |

Benchmark names such as AgentDojo, InjecAgent, MMLU, ASB, and OSWorld are identifiers of referenced resources. The paper spells out Agent Security Bench for ASB in its bibliography. Expansions or implementation details of benchmark acronyms not defined in the supplied work are not supplied from outside knowledge.

## 20. Key numerical results

All sources below use physical PDF pages. Values are annotation/sample descriptors unless expressly stated otherwise.

| Quantity/result | Value | Unit | Condition/context | Status | Source |
|---|---:|---|---|---|---|
| Final review corpus | 247 | papers | After screening and identity normalization | Author-reported | p. 7, §3.3 |
| Database / expansion / snowballing | 209 / 42 / 24 | candidate records | Three retrieval routes | Author-reported | p. 7, §3.3 |
| Initial candidate pool | 275 | records | Before exclusion/normalization | Author-reported | p. 7, §3.3 |
| Exclusions / normalization reduction | 24 / 4 | records | Different removal operations | Author-reported | p. 7, §3.3 |
| Corpus arithmetic | 275 − 24 − 4 = 247 | records/papers | Reconciliation of reported operands | Analyst-derived | p. 7, §3.3 |
| Annotators | 3 | authors | Independently annotate all 247 papers | Author-reported | p. 7, §3.4 |
| Overall agreement | 0.86 | κ | Before harmonization | Author-reported | pp. 7, 23 |
| Field agreement range | 0.78–0.96 | κ | Defense method to system setting | Author-reported endpoints | p. 37, Table 9 |
| Year counts | 3 / 42 / 121 / 81 | papers | 2023 / 2024 / 2025 / partial 2026 | Author-reported | pp. 3, 7–8 |
| Partial-2026 corpus share | 32.79 | % of papers | Collected by 27 April 2026 | Author-reported | p. 7 |
| Attack / defense paper types | 66 / 64 | papers | Primary single-label function | Author-reported | pp. 7–8, Fig. 3 |
| Attack + defense share | 52.63 | % of papers | 130 of 247 | Author-reported | p. 8 |
| Benchmark / survey / evaluation / report | 47 / 32 / 26 / 12 | papers | Primary types | Author-reported | p. 8 |
| Single-agent / multi-agent | 200 / 47 | papers | Primary system setting | Author-reported | p. 8 |
| Setting shares | 80.97 / 19.03 | % of papers | Single-agent / multi-agent | Author-reported | p. 8 |
| arXiv / Web | 169 / 12 | papers | Normalized dissemination source | Author-reported | p. 38, Table 10 |
| Informal / conference / journal | 181 / 55 / 11 | papers | Partition of 247 | Author-reported | p. 38, Table 10 |
| Tool-use Security topic | 156 | papers | Multi-label topic | Author-reported | p. 9 |
| Planning / Input / Tool Execution | 227 / 225 / 209 | papers | Lifecycle labels | Author-reported | p. 9 |
| Decision / Output / Memory | 166 / 151 / 82 | papers | Lifecycle labels | Author-reported | p. 9 |
| Monitoring / Inter-agent Comms / Coordination | 58 / 35 / 20 | papers | Lifecycle labels | Author-reported | p. 9 |
| User / Web / Tool Output / Retrieved surfaces | 82 / 55 / 54 / 37 | papers | Multi-label threat surfaces | Author-reported | p. 9, Table 1 |
| Prompt Injection / Indirect Prompt Injection | 142 / 86 | papers | Threat-model/family field | Author-reported | pp. 11–12, Table 2 |
| Malicious Tools / Data Exfiltration | 34 / 31 | papers | Threat-family annotations | Author-reported | p. 12, Table 2 |
| Memory Poisoning / Coordination Failures | 24 / 14 | papers | Threat-family annotations | Author-reported | p. 12, Table 2 |
| Web Browsing / Software Engineering | 93 / 63 | papers | Scenario labels | Author-reported | p. 13 |
| Web prompt / indirect injection | 71 / 44 | co-occurrences | Within Web Browsing scenario | Author-reported | p. 12 |
| AgentDojo / InjecAgent reuse | 30 / 11 | papers | Benchmark labels | Author-reported | p. 17, Table 4 |
| Their benchmark annotation shares | 12.82 / 4.70 | % of annotations | Not a 247-paper denominator | Author-reported | p. 17, Table 4 |
| Attack Success Rate / Success Rate / Accuracy | 129 / 59 / 41 | papers | Metric usage | Author-reported | p. 18, Table 5 |
| Utility / Latency / Cost | 22 / 8 / 7 | papers | Metric usage | Author-reported | p. 18, Table 5 |
| Refusal / False Positive Rate | 13 / 13 | papers | Metric usage | Author-reported | p. 18, Table 5 |
| AgentDojo utility / latency / cost cells | 16 / 4 / 0 | co-occurrences | Eight-benchmark matrix | Visually readable | p. 40, Fig. 7 |
| Inter-agent Channels comms / coordination | 21 / 16 | co-occurrences | One surface row, two lifecycle columns | Visually readable | p. 39, Fig. 6 |

No approximate visual estimates, pooled attack-success percentages, relative effectiveness improvements, or p-values are reported in this analysis. Rounded visual percentages are kept distinct from more precise prose values.

## 21. Claim–evidence map

| Claim | Evidence | Figure/table/analysis | Source | Qualification/evidence strength |
|---|---|---|---|---|
| Agent security extends beyond unsafe text | Tools, state, and external effects can realize harm | RQ1; conceptual model | pp. 2, 5, 8–11 | HIGH fidelity to explicit author framing; no matched causal experiment |
| Corpus has 247 normalized papers | Retrieval and removal counts reconcile | X1; Table 8 | pp. 7, 36 | HIGH reported arithmetic; raw records absent |
| Annotation has reported agreement | Three authors; overall κ 0.86; field values | X2; Table 9 | pp. 7, 37 | HIGH reporting confidence; agreement is not source truth |
| Injection dominates research attention | Threat counts 142 and 86 | X5; Table 2 | pp. 11–12 | HIGH descriptive support; not operational incidence |
| Web browsing is a major scenario | Scenario 93; injection co-occurrences 71/44 | X5 | pp. 12–13 | HIGH count fidelity; labels overlap |
| Persistent memory creates delayed risk | Memory Poisoning 24; Memory stage 82; reuse path | Fig. 4b; Table 2 | pp. 12–13 | HIGH author support; no pooled delayed-trigger rate |
| Multi-agent security adds propagation concerns | Collaboration co-occurrences and peer topology | Fig. 4c | p. 13 | HIGH author interpretation; no uniform spread probability |
| Defenses have different assumptions and costs | Six family tradeoff descriptions | Table 3 | pp. 15–16 | HIGH conceptual support; no measured universal stack |
| Evaluation underreports operational dimensions | Metric counts 129 vs 22/8/7 | Table 5; Fig. 7 | pp. 17–18, 40 | HIGH usage-count support; not proof every benchmark omits them |
| Scenario stacks are guidance rather than standards | Explicit qualification | Table 11 | pp. 39–40 | HIGH; no sufficient-security guarantee |
| Review conclusions have search/coding limitations | Four validity categories | §10 | p. 23 | HIGH author acknowledgment |
| Web agents have additional architectural exposure | External content → decisions → privileged actions | RQ1/RQ2 applied to user question | pp. 2, 5, 10–12 | MEDIUM analyst inference; no numerical standalone comparison |

## 22. Very simple explanation — Explain Like I'm 15

A text-only language model mainly gives you words. A web agent can also use those words to decide what website to open, what tool to call, and what action to take. That means a misleading instruction can affect something outside the conversation.

A website may contain information the agent needs, but that does not mean the website gets to tell the agent what its job is. The danger described by this paper is that useful information and hostile instructions can enter the same reasoning process. If the agent mistakes the hostile part for an authorized instruction, it may use the user's permissions to do the wrong thing.

The problem can last longer if the agent remembers contaminated information, and it can spread if another agent trusts a compromised message. Those extra features are not present in every web agent, but when they are present they add more places where trust must be managed.

The researchers reviewed 247 papers. They found lots of attention to prompt injection, but less consistent protection and testing for memory, coordination, useful task completion, cost, and recovery. Their message is to build systems that keep track of sources, limit permissions, check important actions, and contain failures. The review explains why web agents can have broader security exposure; it does not measure how much more vulnerable they are than standalone models.

## Completeness Audit

The denominator is the supplied 40-page inventory, not response length. Every major section and substantive subsection is accounted for below; representation is sometimes compressed and explicitly bounded.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, abstract, keywords | Yes, text and image p. 1 | Yes | Fully represented | Affiliations and corresponding authors included; metadata uncertainty preserved |
| §1 Introduction | Yes | Yes | Represented in compressed form | Problem, motivation, contributions, website mention included |
| §2 Background; §2.1 Rise; §2.2 Risks | Yes | Yes | Represented in compressed form | Autonomy, probabilistic control, delegated effects included |
| §3 Methodology; §3.1 RQs | Yes | Yes | Fully represented | All four explicit questions and their relationships |
| §3.2 Search Strategy | Yes | Yes | Fully represented | Sources, window, assistant role, snowballing, rationale |
| §3.3 Literature Selection | Yes | Yes | Fully represented | Candidate counts, normalization, boundaries |
| §3.4 Annotation and Analysis | Yes | Yes | Fully represented | Fields, label encoding, independent coding, agreement |
| §4 Trend Observation | Yes | Yes | Fully represented | Years, types, settings, venues, interpretation caveats |
| §5 RQ1; §5.1 Stages/Surfaces | Yes | Yes | Fully represented | Tuple, lifecycle counts, surface definitions |
| §5.2 Modeling Implications; §5.3 RQ1 Answer | Yes, p. 10 text-only and p. 11 image/text | Yes | Represented in compressed form | Transition-centered analysis and boundary principles |
| §6 RQ2; §6.1 Injection | Yes | Yes | Fully represented | Threat-model versus method distinctions and scenario counts |
| §6.2 State/Propagation; §6.3 RQ2 Answer | Yes, p. 14 text-only | Yes | Fully represented | Memory, coordination, consequence asymmetry |
| §7 RQ3; §7.1 Families | Yes, p. 14 text-only and p. 15 image/text | Yes | Fully represented | Six defense families and trust/overhead caveats |
| §7.2 Enforcement/State; §7.3 RQ3 Answer | Yes | Yes | Fully represented | Coverage gaps and no universal stack |
| §8 RQ4; §8.1 Benchmarks | Yes | Yes | Fully represented | Reuse denominator and named suite roles compressed |
| §8.2 Metrics | Yes | Yes | Fully represented | All Table 5 counts and coverage limits |
| §8.3 Stronger Evaluation; §8.4 RQ4 Answer | Yes | Yes | Represented in compressed form | Traces, utility, horizons, regression, overhead |
| §9 Discussion; §9.1 Prior Surveys | Yes | Yes | Represented in compressed form | Table/rubric represented; repeated literature citations compressed |
| §9.2 Secure Engineering | Yes | Yes | Fully represented | State, tools, orchestration, control plane |
| §9.3 Practice Implications | Yes | Yes | Represented in compressed form | Requirements, coding workflows, regression, runtime operations |
| §9.4 Next-stage Priorities | Yes | Yes | Fully represented | Assurance, composition, recovery |
| §10 Threats to Validity | Yes, text-only p. 23 | Yes | Fully represented | All four author categories preserved |
| §11 Conclusion | Yes, p. 23 text-only and p. 24 image/text | Yes | Represented in compressed form | Main conclusions integrated without repetition |
| RQ1, RQ2, RQ3, RQ4 | Yes | Yes | Fully represented | Questions, evidence, and answers connected |
| Formal hypotheses | No such item reported | Accounted for | Not present in supplied work | None manufactured |
| X1–X8 analyses | Yes | Yes | Fully represented | Analysis register separates review operations from experiments |
| New attack/defense experiments | No such item reported | Accounted for | Not present in supplied work | Reviewed studies not relabeled as survey experiments |
| Figures 1–2 | Yes, visually and text | Yes | Fully represented | Framework and RQ dependencies |
| Figure 3, all three panels | Yes, visually and text | Yes | Fully represented | Exact counts, rounded shares, partial year |
| Figure 4, all three panels | Yes, visually and text | Yes | Fully represented | Entry, delayed activation, propagation |
| Figure 5 | Yes, visually and text | Yes | Fully represented with uncertainty | All displayed counts; denominator limitation |
| Figure 6 | Yes, visually and text | Yes | Fully represented | Entire numerical matrix and prose discrepancy |
| Figure 7 | Yes, visually and text | Yes | Fully represented | Entire numerical matrix in grouped compact notation |
| Tables 1–3 | Yes, visually and text | Yes | Fully represented | Modeling, threats, defense goals/tradeoffs |
| Tables 4–5 | Yes, visually and text | Yes | Fully represented | All reuse and metric rows |
| Table 6 | Yes, visually and text | Yes | Represented in compressed form | Dimensions, row IDs, decisive distinctions, rubric caveat |
| Tables 7–9 | Yes, visually and text | Yes | Fully represented | Agenda, exclusions, all reliability values |
| Table 10 | Yes, visually and text | Yes | Represented in compressed form | All venue counts; repeated per-venue percentages compressed |
| Table 11 | Yes, visually and text | Yes | Fully represented | All four classes and explicit non-standard qualification |
| E1 tuple; E2 transitions; E3 κ | Yes | Yes | Fully represented within source definitions | κ formula not supplied; no external mathematics added |
| Algorithms, theorems, proofs | No such items reported | Accounted for | Not present in supplied work | Search procedure is described, not invented pseudocode |
| Major contributions | Yes | Yes | Fully represented | Conceptual, methodological, descriptive, synthesis, engineering |
| Author-stated limitations | Yes | Yes | Fully represented | §10 and distributed caveats included |
| Appendix A.1 | Yes | Yes | Represented in compressed form | Query groups and assistant prompt purpose; prompt not executed |
| Appendix A.2 | Yes | Yes | Fully represented | All exclusion categories/counts |
| Appendix A.3 | Yes | Yes | Fully represented | Field encoding, disagreement resolution, reliability |
| Appendix A.4 | Yes | Yes | Represented in compressed form | Qualitative rating meanings and application |
| Appendix B | Yes | Yes | Fully represented in substantive content | Identity normalization and venue/function distinction |
| Appendix C.1–C.3 | Yes | Yes | Fully represented | Matrices, scenario stacks, cell semantics, tradeoffs |
| Corresponding-author footnote | Yes | Yes | Fully represented | Yu and Fang identified |
| Copyright/contact/footer material | Yes where supplied | Accounted for | Inspected but deliberately omitted as non-substantive detail | Contact addresses and permissions not needed for scientific interpretation |
| Acknowledgments | Yes | Briefly accounted for | Represented in compressed form | China national R&D funding, grant 2024YFF0908000 |
| References [1]–[255] | Yes, supplied text; images for selected pages | Function represented | Deliberately compressed as bibliographic material | No outside papers read; individual results not inferred from titles |
| Separate supplementary artifacts | Not supplied | Absence represented | Missing from supplied material | Appendix C reviewed; separate files not claimed |
| Survey website and raw corpus labels | Not supplied | Absence represented | Missing from supplied material | Cannot inspect content or independently recompute coding |

### Missing or inaccessible material

No page in the supplied 1–40 extracted-text sequence is missing. Thirteen pages lack supplied page images and therefore have text-only coverage. No separate corpus dataset, annotation ledger, search execution log, exclusion list by title, assistant retrieval outputs, website contents, repository implementation, or underlying reviewed-paper full texts were supplied. No claim is made to have inspected those artifacts. The failed `-` image reference contains no usable evidence. Original PDF bytes and hash identity remain unverified.

### Uncertain interpretations

The January 2026 ACM-format markings, placeholder DOI, April cutoff, May reference retrieval dates, and August arXiv version cannot be reconciled into confirmed publication status from this document alone. Figure 5's count denominator/subset is insufficiently specified. Appendix C.1's Inter-agent Channels interpretation does not match its largest displayed cell. Table 4 and informal benchmark-tier prose are not perfectly aligned for MMLU. Fine heatmap color mapping is not inferred beyond labeled cells. No causal or numerical web-agent-versus-standalone comparison is available.

### Deliberately compressed material

Repeated framing about information, authority, persistence, and deployment assurance was consolidated. Long citation clusters, individual bibliography entries, venue name expansions already available in Table 10, and repeated per-outlet percentages were compressed. Table 6's qualitative cells were summarized around their principal distinctions rather than reproduced as a second complete matrix. Appendix A's retrieval prompt was explained rather than quoted in full. Contact addresses, permission boilerplate, page headers/footers, and decorative diagram icons were treated as non-substantive. All seven substantive figures and eleven tables nevertheless receive individual interpretation.

### Potential omissions

No known major section, substantive subsection, research question, numbered visual/table, principal notation, contribution, or stated limitation in the supplied inventory is left unaccounted for. This does not mean every sentence or cited work is reproduced, nor that the survey corpus has been independently validated. Exact boundary rules and raw decisions not supplied cannot be recovered by explanation. The result is a comprehensive representation of the supplied work with disclosed compression and uncertainty, not a claim of lossless reproduction or externally verified completeness.
