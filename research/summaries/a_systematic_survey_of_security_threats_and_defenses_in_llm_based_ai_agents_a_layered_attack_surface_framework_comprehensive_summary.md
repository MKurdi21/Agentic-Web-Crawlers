## Stage 0 — Document Accessibility Report

The complete supplied extracted text covers physical PDF pages 1–58. All 58 page records contain substantial text. Direct visual renderings are supplied for 37 pages: 1–16, 19, 21, 24, 26, 28–29, 33–41, and 53–58. The remaining 21 pages were inspected as supplied text only: 17–18, 20, 22–23, 25, 27, 30–32, and 42–52. Thus textual coverage is full within the supplied document, while visual coverage is partial. Page numbers below refer to physical PDF pages, which match the printed numbering in these materials.

All eight numbered figures and all fifteen numbered tables have supplied visual renderings and readable extracted text. Small labels were cross-checked against the extracted text; exact matrix values come from labeled cells and tables, not estimates of shading. Major mathematical expressions are readable, although extracted superscripts and mathematical formatting sometimes degrade. For example, the rendered Appendix D establishes that the robustness runs use 10^4 iterations, rather than the unformatted extraction '104'. No OCR was performed or needed for this analysis. No tools, browsing, or external source verification were used.

Appendices A–F are present on pp. 53–58. The full theorem proof and supplementary files are absent. Referenced absent artifacts include supplementary/corpus_coding.csv, verify_coding.py, robustness_analysis.py, CODING_EXAMPLES.md, PROOF_THEOREM1.md, and the abom/ schema, validator, examples, and tests. Their existence and contents are author-reported, not independently inspected. No embedded files are reported in the supplied accessibility metadata. The metadata's automated appendix detection is incomplete: direct reading identifies six appendices, not merely the detected pages 13 and 57.

Evidence labels used throughout: [A] author-reported; [B] directly observable in supplied visuals; [C] analyst-derived, with calculation; [D] analyst interpretation. No [E] external information is introduced. Confidence expresses confidence in the source-grounded reading, not independent validation of cited studies. HIGH applies to clear statements and readable tables; MEDIUM applies to qualified synthesis; LOW or UNKNOWN applies where contradictory reporting or absent artifacts prevents resolution.

## 1. Plain-Language Orientation

This is a systematic survey and systematization of knowledge about the security of artificial intelligence agents built around large language models (LLMs). An LLM generates language. An agent additionally plans sequences of actions, reads outside material, remembers information, invokes tools, and sometimes delegates to other agents. The author's central argument is that these additions introduce security failures that cannot be understood by studying harmful text generation alone. A malicious web page can become an instruction, an instruction can become persistent memory, and that memory can influence a later tool action. Each step may look ordinary when examined separately. [A, pp. 1–3]

The work reviews 116 papers and organizes them using the Layered Attack Surface Model (LASM): seven architectural layers crossed with four attack temporalities. The architectural question is where an attack operates; the temporal question is what separates installation of the attack from its harmful effect. This produces 28 analytical cells. The author reports that only 9 of 144 paper-cell assignments fall in the delayed, system-level region L5–L7 × T3–T4. The work also reports seven cells without claimed defense coverage and no T3/T4 coverage among ten tabulated benchmarks. Several details of these findings conflict with other supplied passages, so their precise scope requires qualification. [A/B, pp. 12, 16, 34–39]

For the research question 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?', the most relevant explanation is architectural: outside web content becomes a recurring input during execution; tools turn decisions into consequential actions; memory allows compromise to persist; and delegation propagates influence. This is an analyst inference from the survey's architecture and cited examples, not a vulnerability ratio established by this paper. The survey is not an original controlled experiment comparing the same model with and without web-agent capabilities. It does cite another study reporting lower safety compliance with tool access, but does not provide enough experimental detail to reconstruct that comparison. [D, grounded in pp. 1, 8, 16–24, 32]

## 2. Document Roadmap

The inventory uses the original numbering. §1 introduces the problem, five research questions, five contributions, scope, and shortcomings attributed to existing surveys. §2 is the analytical foundation: §2.1 explains search, selection, coding, caveats, and the 2026 extension; §2.2 defines agent components, principal hierarchy, actor classes, and threat model; §2.3 defines LASM, defense non-transferability, temporal classes, and the coverage matrix.

§3 surveys single-agent layers: §3.1 foundation-model attacks and defenses; §3.2 cognitive attacks and defenses; §3.3 memory lifecycle, retrieval poisoning, temporal escalation, and defenses; §3.4 tool execution, indirect injection, capability creep, autonomous exploitation, and defenses. §4 covers system layers: §4.1 multi-agent trust chains, collusion, Byzantine behavior, and defenses; §4.2 Model Context Protocol security, supply chains, the Agent Bill of Materials, and defenses; §4.3 insider threats, accountability, drift, and governance gaps.

§5 maps defense classes, joint recipes, benchmark coverage, and evaluation recommendations. §6 identifies five gaps, their dependencies, five future directions, and comparisons with previous surveys. §7 concludes. References occupy pp. 42–53. Appendices A–F cover limitations/reproducibility, coding rules, theorem, robustness, taxonomy-to-defense comparison, and an action-log schema. Figures 1–8 and Tables 1–15 are individually accounted for below. No standalone algorithm or pseudocode listing is supplied. The ABOM JSON example and action-log record are specification examples, not evaluated algorithms.

## 3. Background and Context

An attack surface is the set of places through which an adversary can influence a system. A trust boundary separates information or actors with different authority. A principal is an instruction source, such as a developer, operator, user, or external environment. The proposed hierarchy is Developer ≻ Operator ≻ User ≻ Environment: higher-ranked instructions should take precedence in conflicts. Principal trust inversion occurs when low-authority environmental content is treated as authoritative. [A, pp. 8–9]

Prompt injection places instructions where the system should be processing data. Indirect prompt injection places them in material encountered during a legitimate task, such as a web page, email, document, database record, or tool response. It need not involve access to the user's conversation. Jailbreaking instead concerns bypassing the model's learned safety constraints. In an agent, a jailbreak can affect tools and actions, so the consequence may exceed harmful text. [A, pp. 16–17, 22]

Retrieval-Augmented Generation (RAG) retrieves outside information to inform generation. The survey distinguishes retrieval relevance from trustworthiness: a malicious document can rank highly because it is relevant. Persistent memory adds a second issue: retrieved content can be stored and reused later. A memory entry has a write, read, consolidate, and share lifecycle; each operation can introduce or spread compromise. [A, pp. 19–21]

Chain-of-thought (CoT) is a stated reasoning sequence. The survey warns that stated reasoning may not faithfully describe the computation producing a decision. It therefore treats readable explanations as insufficient evidence of trustworthy action. Reinforcement Learning from Human Feedback (RLHF), Direct Preference Optimization (DPO), and Constitutional AI are discussed as alignment methods; the survey argues that they are useful but insufficient for the broader agent system. [A, pp. 8, 17–18]

The Model Context Protocol (MCP) is described as an interface for discovering, authenticating, and invoking external tools. A Software Bill of Materials (SBOM) lists software dependencies. The proposed Agent Bill of Materials (ABOM) extends that inventory to models, prompts, memory initialization, and tool endpoints. These are author-proposed distinctions within this paper, not externally verified assessments of standards. [A, pp. 26–29]

## 4. Research Problem and Gap

The existing problem is that increasingly capable agents operate across information sources, sessions, permissions, and organizational actors. Security failures can emerge from authorized actions composed into an unauthorized outcome. The author identifies three defining properties: emergence, composition across components, and extended time between installation and harm. [A, pp. 1–2]

According to the author, existing type-centric taxonomies group attacks under names such as injection or poisoning without identifying the component at which a defense must act. They also omit temporal structure, underrepresent higher-layer threats, and sometimes stop before recent MCP and governance developments. These are the survey's claims about prior work; the referenced surveys were not independently reviewed here. [A, pp. 2–3, 41]

The gap is both conceptual and empirical: designers lack a framework connecting threat descriptions to control placement, and the surveyed research concentrates on immediate lower-layer attacks rather than delayed system-level failures. LASM and temporality are proposed to expose that distribution. The author's severity–effort interpretation is stronger than the directly tabulated evidence because no reproducible numerical severity scale or correlation coefficient is supplied. [A/D, pp. 12, 16]

The scope includes security challenges arising from LLM-based agentic architecture. It excludes non-agentic bias/toxicity analysis, classical adversarial machine learning against non-LLM vision/tabular models, human AI misuse literature, and physical hardware security. Autonomous exploitation is included to characterize the offensive capability enabled by agents and the resulting authorization/containment needs. [A, p. 3]

## 5. Research Questions / Objectives / Hypotheses

The paper explicitly states five research questions. RQ1 asks whether the attack surface can be decomposed into layers with distinct trust boundaries and defense leverage points. RQ2 asks whether agentic attacks have temporal structure invisible to type-centric taxonomies and what minimal classification captures it. RQ3 asks where research is concentrated or absent and how severity relates to effort. RQ4 asks whether defense coverage matches attack coverage and where defenses are absent. RQ5 asks which gaps are engineering problems and which require fundamental research. [A, p. 2]

The corresponding objectives are to define LASM, define T1–T4, map a literature corpus, map defenses and benchmarks, and organize future work by dependencies and difficulty. The paper states no separate formal statistical hypotheses. The four Empirical Findings are synthesis conclusions, not preregistered hypotheses tested in a new experimental campaign. RQ1/RQ2 receive conceptual answers; RQ3/RQ4 receive coding-based descriptive answers; RQ5 receives an author judgment about research and engineering prerequisites.

## 6. Assumptions / Threat Model

The system model contains foundation model, planning/reasoning, memory, tool execution, multi-agent communication, and orchestration/environment infrastructure. LASM then treats ecosystem and governance as additional analytical surfaces: ecosystem surrounds runtime components, while governance observes and constrains the stack. The layers need not be physically separate machines or neural modules. L1 and L2 may share weights while representing different intervention targets. [A/B, pp. 7–11]

The attacker model has four dimensions. Position is external, semi-trusted principal, or supply-chain actor. Knowledge is black-box input/output access, gray-box architecture knowledge without weights, or white-box full access. Goals are confidentiality, integrity, or availability. Persistence is one-shot or sustained. Figure 4 further places session-level persistence between one-shot and persistent categories; its goal axis explicitly has no severity ordering. [A/B, pp. 9–10]

Six actor classes can fail independently: developer, operator, user, peer agent, supply-chain actor, and environment. For example, operators select tools and logging policies; environmental attackers can plant retrieved content; supply-chain attackers can compromise checkpoints or packages. The model does not assume every actor is honest. Individual attack subsections specify narrower combinations, such as black-box environmental injection or white-box training-time backdoors. [A, pp. 9, 15–30]

The theorem makes substantially narrower assumptions than the overall survey: a pure defense reads only one representation, and a localized attack leaves every other representation's input distribution unchanged. Consequently, a causal cross-layer attack does not automatically satisfy its premise. Emergent reward hacking and drift may have no external attacker at all; the paper explicitly accommodates these under integrity/alignment failures. [A, pp. 18, 30, 56]

## 7. Methodology

This is a systematic literature review inspired by Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA), combined with conceptual modeling, formal argument, descriptive coding, and sensitivity analysis. It is not a meta-analysis pooling comparable experimental effect sizes. Four databases were searched: IEEE Xplore, ACM Digital Library, arXiv categories cs.CR/cs.AI/cs.LG, and Google Scholar. Forward/backward tracing used three seed papers. [A, pp. 4–6]

Agent query terms were AI agent, LLM agent, autonomous agent, multi-agent, agentic AI, and tool-augmented LLM. Security terms were security, attack, adversarial, prompt injection, jailbreak, poisoning, safety, trust, and vulnerability. The reported period is January 2021–April 2026, split into January 2021–April 2025 and May 2025–April 2026. Exact database-specific query syntax, dates of individual searches, and full retrieval exports are not supplied. [A, pp. 4–5]

Peer-reviewed papers at named major venues qualify without a citation threshold. For preprints/non-top-tier work through December 2024, at least 20 citations are required. January 2025–April 2026 preprints can qualify through direct contribution to identified gap areas. Exclusions are non-agentic safety, non-LLM adversarial ML, technically noncontributing position papers, and duplicates. The gap exception admitted 26 of 44 papers from January 2025–April 2026; 18 met the citation threshold. This asymmetric selection is acknowledged and matters to interpreting coverage. [A, p. 5]

Screening retrieved 1,634 records: 1,247 in phase one and 387 in phase two. Deduplication left 1,121, title/abstract screening left 313, and full-text screening left 116. Exclusions were respectively 513, 808, and 197. These arithmetic transitions are internally consistent. The corpus categories are 38 L1–L4 attack papers, 26 L5–L6 attack papers, 16 governance/alignment papers, 18 defense papers, 13 benchmark/evaluation papers, and 5 comparison surveys; they sum to 116. [A/C, pp. 5–6]

One author coded papers into layer/temporality cells. The main contribution determines layer; multi-layer and multi-temporality coding are allowed. Ambiguous cases receive lower-layer/faster-temporality assignments. T3 nominally requires an explicit memory write used in a future session. T4 covers drift without a discrete payload or dormant payloads in weights/training data. Appendix B provides decision tests, but its sleeper-agent example conflicts with these restrictions. No formal inter-rater reliability was measured. [A, pp. 5, 7, 54–55]

The defense mapping uses 15 proposed mechanism archetypes and records layer and temporality coverage. The paper says the archetypes preceded classification. Claimed coverage is projected onto a matrix, without a new common benchmark establishing effectiveness. Robustness analysis perturbs coding through leave-one-out, random paper dropping, cell perturbation, and role ablation. Hardware, runtime environment, random seeds, code versions, and complete perturbation procedures are not supplied in the main text. No new training/test split or model-training hyperparameter set applies to the survey itself. [A, pp. 33–36, 56–57]

## 8. Experiments / Analyses

**X1 — Literature screening and distribution.** Purpose: establish the review corpus. Data: 1,634 retrieved records, 116 retained papers. Outcome: screening counts and publication distribution, Figure 2/Table 2. No randomized comparison or significance test is reported. The author describes exponential growth, but supplies no fitted growth model. The 2026 count covers four months, unlike the full 2025 year. [A/B, pp. 5–7]

**X2 — Architecture × temporality coding.** Purpose: answer RQ3. Unit: paper-cell assignment, not unique paper or attack incident. Table 5 contains 144 assignments. The selected high-layer/delayed zone contains 9 versus 135 elsewhere, yielding 6.3% as reported. Its six cells are not a random sample of all possible threats. Severity is qualitatively interpreted, not a measured dependent variable with statistical inference. [A/B, pp. 12, 15–16]

**X3 — L4 root-cause synthesis.** Purpose: explain tool-execution attacks. The author states that all documented attack instances across 27 L4 assignments can be explained by unmarked tool outputs entering planning context. Supporting examples include web injection, coding-file injection, function hijacking, and shared-context cross-tool contamination. No incident-by-incident coding table establishing universality is supplied, and nearby prose says 'nearly all' rather than 'every'. [A, pp. 21–23]

**X4 — Defense coverage projection.** Purpose: answer RQ4. Fifteen Table 7 defense classes are expanded across their listed layers and temporalities. Figure 8 reports seven zero cells. This measures listed class coverage, not success rates. Its printed values at L3×T3 and L7×T3 do not transparently match a literal expansion of Table 7; the discrepancy is discussed below. [A/B, pp. 33–36]

**X5 — Benchmark inventory.** Purpose: identify what can be measured. Ten Table 9 benchmarks have only T1/T2 entries. The survey reports no delayed-threat benchmark among them. Several additional benchmark-like works appear elsewhere, while the broader corpus contains 13 benchmark/evaluation papers, so the ten-row table should not silently be equated with every evaluation paper discussed. [A/D, pp. 18, 27, 32, 37–38]

**X6 — Five-case taxonomy comparison.** Purpose: show defense-placement distinctions. Table 15 compares Postmark MCP, Copilot project-file remote code execution, PoisonedRAG, infectious jailbreak, and Greedy Coordinate Gradient attacks. Two are described as real incidents. This is a conceptual case comparison, not a controlled trial measuring whether LASM-guided teams outperform other designers. OWASP assignments include author interpretation, and the PoisonedRAG label contradicts nearby prose. [A/B, pp. 12–13, 57–58]

**X7 — Ambiguity sensitivity.** Eight low-confidence papers are alternatively coded. Largest reported single-cell shift is ±2 at L2×T3. Appendix B says the selected-zone baseline is 8 and changes by at most ±2, whereas current Table 5 says 9. The exact alternative assignments are absent, so the discrepancy cannot be resolved. [A, pp. 55–56]

**X8 — Four robustness protocols.** Table 14 reports leave-one-out 5.56–6.94%; 10% paper-drop bootstrap 95% interval 4.81–7.48%; cell perturbation with p=0.10, 95% interval 5.83–8.33%; and role-ablation range 4.76–7.62%. The repeated stochastic procedures use 10^4 runs. These assess sensitivity to the specified perturbations, not systematic coding bias, source authenticity, or a severity correlation. [A/B, pp. 56–57]

**X9 — Cited-study evidence synthesis.** The survey reports diverse attack and defense results from other works. Their datasets and metrics differ, so they cannot be pooled into one agent vulnerability rate. The main directly web-related number is ARE's 67% attack success with perturbations affecting less than 5% of webpage pixels. Other important conditions are catalogued in Sections 9 and 20. No cited experiment was reproduced here. [A, pp. 16–32]

## 9. Results

The most directly supported corpus result is the Table 5 distribution. L1 has 32 assignments; L2 22; L3 25; L4 27; L5 15; L6 12; L7 11. Temporal totals are T1=63, T2=42, T3=21, T4=18. The selected delayed system-level zone is 3+1+1+0+1+3=9 assignments. Analyst-derived: 9/144×100=6.25%, which explains the rounded 6.3%. These are overlapping assignments, not 144 independent studies. [A/B/C, p. 16]

The author interprets this as inverse severity–effort alignment: high-impact threats receive little attention. That interpretation is plausible within the framework but not statistically demonstrated by the counts alone. The survey supplies no severity scores, uncertainty for severity, or correlation coefficient. Long-term memory corruption is sometimes invoked as part of the high-risk narrative even though native L3 memory attacks lie outside the chosen L5–L7 zone. [A/D, pp. 12, 19]

The second result is an explanatory claim: L4 failures share principal trust inversion. For a web agent, a page or file is legitimate task data but can contain malicious instructions. If those instructions acquire authority, the agent can revise plans or invoke tools on the attacker's behalf. The paper cites greater-than-60% injection success in realistic multi-tool scenarios, 50–80% success against production coding agents, and 75% vulnerability in specified LangChain/LlamaIndex cross-tool settings. These are different cited outcomes with incomplete common experimental detail. [A, pp. 22–23]

The defense result is seven zero cells out of 28. Analyst-derived: 7/28×100=25% of the framework's cells. This is not a 25% compromise probability. The seven are L1×T2/T3/T4, L4×T4, L5×T4, and L6×T3/T4. Contrary to the paper's statement that only three contain attacks, Table 5 gives positive counts in six of these seven. Whether those counts represent defense/theory papers rather than attack instances requires the unavailable per-paper role coding. [A/B/C/D, pp. 16, 34–36]

The benchmark result is 0 of 10 tabulated benchmarks covering T3 or T4. The source supports a gap within this table and corpus. Statements that delayed progress is universally unmeasurable are stronger: targeted experiments and other metrics might still exist, and the supplied review does not establish an exhaustive universal negative. The author itself acknowledges nonexhaustive search and excluded industry evidence. [A/D, pp. 5–7, 37–38]

Other cited results illustrate mechanisms rather than estimate population prevalence: MINJA 98.2% memory-injection success; PoisonedRAG greater than 90% targeted corruption with as few as five documents in a corpus of 10,000+; AgentPoison greater than 80% success below 0.1% poison rate; A-MemGuard greater than 95% mitigation with approximately 15% throughput overhead; and 92.5% sleeper detection accuracy on known implementations. These are condition-specific secondary reports, not new LASM experiments. [A, pp. 7, 19–21]

## 10. Figure-by-Figure Interpretation

**Figure 1 — Survey dependencies, p. 4.** This is a flow diagram without numerical axes. Methodology and background lead into LASM; LASM feeds layer surveys; these feed defense, evaluation, gaps, and future directions. Related work and conclusion sit downstream. Boxes and arrows encode conceptual dependencies, not a chronological experimental pipeline. Its role is navigation, supporting Table 1's audience paths. [B]

**Figure 2 — Publication distribution, p. 6.** A vertical bar chart has years 2021–2026 on the x-axis and number of papers on a linear y-axis with labeled ticks 0, 20, 40. Violet bars show a rise into 2024, then lower raw counts for 2025 and partial-year 2026. The caption supplies exact counts 31 for 2025 and 22 for January–April 2026. Earlier heights are visually approximate and are not converted into exact yearly counts here. No error bars, confidence intervals, or fitted exponential curve appear. The author's growth interpretation should be distinguished from what raw unequal-duration bars establish. [A/B]

**Figure 3 — Agent architecture and trust inversion, p. 8.** Foundation feeds planning/reasoning; planning connects upward to memory and laterally to tool execution, which connects upward to multi-agent interface. Ecosystem and governance occupy separate boxes above. The principal-hierarchy box marks the environment untrusted. The dashed red return arrow from tool execution toward reasoning depicts environmental input acquiring authority. Its security meaning is the feedback loop: actions produce observations that can influence subsequent actions. It is a simplified schematic, not a complete interface specification. [B]

**Figure 4 — Adversarial capability axes, p. 10.** Four horizontal categorical rows show position, knowledge, CIA goal, and persistence. Green-to-yellow-to-red boxes encode progression for position, knowledge, and persistence. The CIA row explicitly has no implied severity order. There are no numerical units or metric distances. Examples in the caption locate GCG as external/white-box/integrity/one-shot and sleeper agents as supply-chain/white-box training-side/integrity/persistent-T4b. [A/B]

**Figure 5 — LASM structure, p. 11.** Five colored horizontal runtime bands L1–L5 sit inside an L6 deployment-artifact enclosure. A red vertical L7 governance box sits alongside. Dotted lines indicate observation through logs and traces; a dashed policy arrow indicates enforcement back into the stack. Each runtime layer is labeled with a representation and trust boundary. This figure clarifies that governance is cross-cutting and ecosystem is enclosing, so seven layers are not simply seven serial processing steps. [B]

**Figure 6 — Three cross-layer chains, p. 13.** Three horizontal panels show temporal escalation, sleeper activation, and infectious jailbreak. Panel 1 runs L4 injection → L3 write → future L3 read → L7 unattributable harm. Panel 2 runs L6 poisoned fine-tuning → L1 weight trigger → deployment activation → L2 biased reasoning. Panel 3 runs compromised agent → legitimate peer message → alignment override → relay to more peers. Solid arrows denote same-session causality; red dashed arrows mark cross-session or cross-stack gaps. These are canonical mechanisms, not measured attack-frequency plots. [B]

**Figure 7 — Research coverage heatmap, p. 15.** Columns are categorical temporalities T1–T4; rows run L1 at the bottom through L7 at the top. Printed cell counts match Table 5. Purple opacity is count/14×0.75; it encodes literature volume, not attack probability or severity. A dashed red rectangle selects L5–L7 × T3–T4. The figure labels T4 'Drift' although the definition also includes dormant backdoors. Its caption warns that two of three L7×T4 papers are also weight-layer/alignment papers, so the cell overstates dedicated governance research. [A/B]

**Figure 8 — Claimed defense coverage, p. 36.** Same categorical grid; green opacity scales to maximum class count four at L4×T1. Red crosses mark seven zeros. Printed rows are L1=(3,0,0,0), L2=(1,1,2,2), L3=(2,2,3,1), L4=(4,3,1,0), L5=(1,2,1,0), L6=(3,2,0,0), L7=(2,2,3,2). These are defense classes claiming coverage, not validated protection. The caption says L4×T4 has two attack papers, whereas Table 5 says three assignments. Literal Table 7 expansion also raises two count discrepancies discussed in Section 14. [A/B/C]

## 11. Table-by-Table Interpretation

**Table 1 — Audience roadmaps, p. 4.** Four rows target system designers, security researchers, regulators/policy readers, and practitioners/security-operations analysts. Columns are audience and suggested reading path. Bold marks essentials and parentheses mark context. It is navigational rather than evidential. Unresolved internal labels such as tab:lasm remain visible in the designer row. [A/B]

**Table 2 — Screening, p. 6.** Rows track retrieval and exclusion stages; columns are records and exclusions. Counts are 1,247+387=1,634; 513 duplicates removed; 808 title/abstract exclusions; 197 full-text exclusions; final 116. Dashes mean no exclusion count is supplied for that row, not a measured zero. This table supports corpus construction, not search exhaustiveness. [A/B/C]

**Table 3 — Actor classes, p. 9.** Rows list six actors; columns describe trust and affected layers. Developers expose L1/L2/L7, operators L4/L6/L7, users L4/L5, peers L5, supply-chain actors L1/L6, and environment L4/L3. The trust labels mix ordered roles and role-bound/no-assumed-trust categories; the text explicitly says actors are not totally ordered. [A/B]

**Table 4 — Layer definitions, p. 14.** Each row gives layer, name, trust boundary, representative threats, defense leverage, and CIA goals. Integrity is primary throughout. Confidentiality also appears at L1/L3/L4/L6, availability at L4. This is a qualitative control-placement table, without performance rankings. The central mappings are foundation→alignment/adversarial training; cognition→plan verification; memory→access/consensus/provenance; tools→filtering/sandboxing/least privilege; coordination→authentication/collusion detection; ecosystem→ABOM/signing; governance→monitoring/interpretability/regulation. [A/B]

**Table 5 — Paper-cell matrix, p. 16.** Exact T1/T2/T3/T4 rows are L1 13/9/4/6; L2 9/7/3/3; L3 8/9/6/2; L4 13/8/3/3; L5 7/4/3/1; L6 8/3/1/0; L7 5/2/1/3. Row totals are 32/22/25/27/15/12/11; columns 63/42/21/18; grand total 144. Largest cells are L1×T1 and L4×T1, tied at 13; the sole zero is L6×T4. These are assignments across a mixed-role corpus, not necessarily attack-paper counts. [A/B]

**Table 6 — ABOM fields, p. 29.** Four groups cover model, runtime prompt, tools/MCP, and software packages. Required fields include model identity/version, system-prompt hash/origin, tool identity/version/hash/permissions, and inherited package/license/vulnerability metadata. Optional fields include model hash/attestation, fine-tuning provenance, alignment method, initial memory hash, manifest signature, and last audit. The CycloneDX column indicates available equivalents. Optional hashes/signatures limit what mere schema compliance guarantees. No attack mitigation experiment accompanies this specification. [A/B/D]

**Table 7 — Fifteen defense classes, p. 35.** Classes are safety training, adversarial fine-tuning, input/output filtering, prompt-injection detection, tool sandboxing, memory access control, memory consensus, memory invariants, inter-agent authentication, collusion detection, MCP signing, ABOM auditing, behavioral monitoring, human review, and interpretability. Columns assign mechanism, layers, temporalities, and limitations. Crucial caveats include adaptive bypasses, false positives, compromised signers, known-encoding dependence, cross-session logging needs, and component-only interpretability. Human review is explicitly an operational procedure. These entries are claimed coverage, not comparable effect estimates. [A/B]

**Table 8 — Seven joint recipes, p. 37.** Rows cover indirect injection; cross-session poisoning; MCP compromise; infectious jailbreak; sleeper backdoors; steganographic collusion; and insider/alignment failure. Columns give layer/time, ordered controls, and residual risk. Examples: web/file/email injection requires instruction–data separation, output filtering, sandboxing, and irreversible-action confirmation. Memory poisoning requires role-based access control, consensus, write provenance, and trust-scored retrieval. All listed controls are intended jointly. Residual risks include persistent variants, dishonest agreement, compromised signed vendors, novel encodings, and unseen triggers. The recipes are prescriptions, not tested complete solutions. [A/B]

**Table 9 — Ten benchmarks, p. 38.** HarmBench covers L1/T1; AgentBench L2–L4/T1–T2; InjecAgent L4/T1; AgentDojo L4/T1–T2; AgentSecBench L2–L4/T1–T2; ASB L2–L4/T1–T2; AgentHarm L1–L4/T1–T2; ARE L1/L4/T1; WIPI L4/T1–T2; Colosseum L5/T1–T2. Years span 2023–2025. Limitations distinguish task-completion evaluation, single-session tests, missing memory, or missing multi-agent evaluation. AgentBench is explicitly described as lacking adversarial evaluation, qualifying the blanket description of all ten as security benchmarks. [A/B]

**Table 10 — Five gaps, p. 39.** Cross-session benchmarks at L3×T3 are engineering; emergent-misalignment detection at L7×T4 is fundamental; general collusion detection at L5×T1–T2 is fundamental; ABOM/MCP standardization at L6×T1–T2 is standards/coordination; accountability at L7×T1–T4 is multidisciplinary. Its statement that L7×T4 has zero defense coverage conflicts with Figure 8's value two. Claimed versus effective coverage may explain the author's intent, but the table does not state that distinction there. [A/B/D]

**Table 11 — Future approaches, p. 40.** Formal security models target gaps 2/3/5; runtime attestation targets gap 5; temporal anomaly infrastructure targets 1/2; multi-stakeholder governance targets 4/5; defensive autonomous agents extend beyond the gap list. Traditions include cryptography, formal methods, trusted computing, statistics/distributed systems, law/standards, and ML systems. These are proposals with no measured comparative ranking. [A/B]

**Table 12 — Survey comparison, p. 41.** Ten prior entries and this survey are compared by paper count, architecture depth, temporal classes, cross-layer figures, memory security, MCP/supply chain, formal propositions, and public coding. This survey's row reports 116 papers, seven layers, four classes, one cross-layer figure, and positive coverage/public-artifact indicators. Other counts are approximate. Circle and dash symbols are not explicitly defined in the caption; their exact intended distinction remains uncertain. The comparison is author-reported, not an independent literature audit. [A/B]

**Table 13 — Limitations, p. 54.** Nine rows classify single-coder assignment, cutoff, search bias, fixed architecture, preliminary MCP statistics, conceptual ABOM, published-only defenses, unvalidated logs, and informal steganographic bound. Three rows are medium severity; six are low; none is marked high. The cutoff row still says April 2025 and seven new entries, conflicting with the main two-phase 2026 account and 22 additions. [A/B]

**Table 14 — EF1 robustness, p. 56.** Four rows provide protocol-specific ranges or 95% intervals and mark all stable. Baseline is 9/144, rounded 6.3%. Leave-one-out and role-ablation are ranges; bootstrap and cell perturbation use bracketed 95% intervals. These should not all be called confidence intervals. Role ablation's 4.76% minimum lies below Table 13's advertised 4.81% overall bound. [A/B]

**Table 15 — Defense placement comparison, p. 58.** Five cases compare OWASP label, implied type-label defense, LASM layer, proposed defense, and control gap. Postmark and Copilot share LLM07 but map to L6 and L4. PoisonedRAG is labeled LLM03 and L3/T3; infectious jailbreak and GCG are LLM01 and L5/T2 and L1. The caption instead groups attacks 3–5 as LLM01. Assignments are explicitly closest-fit author interpretations of the 2023 taxonomy, limiting claims about what official taxonomies necessarily prescribe. [A/B]

## 12. Diagram / Architecture Interpretation

The figures collectively describe a feedback system. A user goal enters planning; the model generates an action; a tool interacts with the outside world; the resulting content returns to planning; memory can preserve selected content; and peers can receive derived messages. Ecosystem artifacts configure what tools, models, and templates participate. Governance records and constrains actions across that process. The dangerous pathway is the promotion of encountered content into authority, followed by persistence or action. [A/B, Figures 3/5/6]

The HelpDesk-Agent example connects these interfaces. A receipt PDF contains a hidden instruction to approve future refunds above $500 without verification. It becomes a memory entry during ordinary triage. Six weeks later, retrieval contributes to a fraudulent $2,000 refund; escalation to Billing-Agent can transmit contaminated context as authenticated information. These numbers are an illustrative author scenario, not a measured production incident or experiment. The earlier sleeper-finance case is likewise hypothetical: a production marker activates biased recommendations. [A, pp. 19, 21, 24]

The accountability chain on p. 31 is a separate text-only diagram: developer/model+prompt → operator/configuration → user/query → agent/k steps → external tools → irreversible action. Its point is distributed responsibility. The action-log schema proposes joining records through parent-step identifiers, session IDs, content hashes, authorization paths, reversibility, and deployment identity. That provides a concrete data model for attribution, but does not demonstrate that logging reconstructs causal intent correctly. [A/D, pp. 31, 57]

## 13. Equations and Mathematical Concepts

**E1 — Principal hierarchy, p. 8:** P=(p1 ≻ p2 ≻ … ≻ pn). P is an ordered list of instruction sources; pi ≻ pj means pi's instructions take precedence in conflicts. This is a normative ordering, not a numeric trust score or probability. The paper's developer/operator/user/environment example instantiates it.

**E2 — Layer definition, p. 11:** L=(L1,…,L7). Each Li has analytical unit Ci, trust boundary Bi, representation Ri, threat set Ti, and defense leverage set Di. Ri ∩ Rj=∅ for i≠j asserts disjoint representation domains. This is a modeling assumption: it does not mean components never exchange information or influence one another.

**E3 — Non-transferability, pp. 12/56:** the main proposition states that a pure layer-i defense has baseline detection/blocking probability against a layer-j-localized attack. Appendix C gives the clearer identity Pr[d alerts under a]=Pr[d alerts under no attack]. Here d is a deterministic alert function of layer-i input Xi, and a changes only layer-j inputs. The proof uses Xi conditioned on a equal in distribution to Xi without attack, so the same function receives statistically indistinguishable input. Zero detection power means no discrimination beyond the no-attack alert rate; it does not require literal zero alerts.

The proof sketch invokes a projection πi selecting the observed representation. Xi and Xj are introduced as representation-specific inputs, but their full sample spaces and joint stochastic system are not formally specified in the supplied sketch. The main proposition's baseline is described as probability without the defense, whereas Appendix C compares alert probability without the attack. These are different formulations and should not be silently equated. Appendix C also explicitly excludes multi-representation defenses and agent-mediated cross-layer effects. The absent full proof prevents further assessment.

**E4 — Coverage sum, p. 12:** U={L5,L6,L7}×{T3,T4}; sum over U of P(Li,Tk)=9 and sum outside U=135. P counts coded papers in a cell, not probability despite its letter. Analyst-derived: total 9+135=144 and fraction 9/144=0.0625. The product symbol means all six layer/time combinations in the selected zone.

**E5 — Temporality, pp. 13–14:** τ(a) classifies an attack by installation-to-execution structure. T1 has gap zero within one inference call; T2 spans turns within a session; T3 requires a persistent-memory write and future-session use, with j>i for sessions si and sj; T4 is not bounded by session structure. T4a has continuous drift without a discrete payload; T4b has a dormant trigger in training/weight artifacts. 'Infinite' drift gap is qualitative language, not a measured time estimate.

**E6 — Semantic privilege escalation, p. 23:** effect(a1 ◦ … ◦ an) exceeds intended authorization although each effect(ai) is individually authorized. ai is a tool action and composition denotes their combined sequence. The definition exposes the difference between checking each call and checking the resulting plan. No computable authorization algebra or algorithm is supplied.

**E7 — Covert-channel scaling, p. 25:** capacity is described as proportional to n·H(X), where n is message length in tokens and H(X) is per-token entropy conditioned on the legitimate task. The intended meaning is that legitimate linguistic variation provides room for hidden coordination. No exact constant, channel model, or proved error bound is supplied; Table 13 calls the argument informal. The expression motivates a research gap, not a validated universal impossibility theorem.

**E8 — Visual encodings and log domains, pp. 15/57:** Figure 7 opacity=count/14×0.75; Figure 8 opacity scales to class count four. The action schema constrains action_type to tool_call/msg_send/mem_write/plan_revise/terminate and reversibility to revertible/costly/irrevocable. These are presentation and specification rules rather than learned objectives. No original optimization loss or executable algorithm is introduced.

## 14. Interpretation and Discussion

RQ1 is answered through a useful control-placement abstraction, with a theorem whose premises make its conclusion narrow. RQ2 is answered through structural temporal classes, particularly memory persistence versus dormant weight triggers. RQ3 receives clear volume counts but a qualitative severity claim. RQ4 receives claimed defense and benchmark maps with reporting inconsistencies. RQ5 receives a dependency-based agenda, whose difficulty judgments remain author assessments. [A/D]

For web agents, the strongest source-grounded causal explanation is repeated exposure plus authority plus action. Browsing supplies attacker-controlled text and images after the initial user prompt. Planning lets those observations redirect a sequence. Tools give the sequence consequences. Memory can outlive the session. Peer communication can spread influence. Ecosystem initialization may introduce malicious instructions before a user message. This explains additional failure pathways; it does not prove every agent is less secure than every standalone LLM. [D, pp. 8, 16–28]

Several consistency findings materially affect interpretation:

1. **Multiplicity arithmetic:** p. 55 says 26 papers occupy two cells and two occupy three, alongside 116 papers and 144 assignments. Analyst-derived: 88 single-cell papers plus 26×2 plus 2×3 equals 146, not 144. The exact distribution cannot be recovered without the CSV.
2. **System-layer temporal majority:** p. 24 says L5–L7 account for the majority of T3/T4 threats. Table 5 gives only nine such assignments versus total 21+18=39; 9/39=23.08% analyst-derived. Different threat-versus-assignment units could matter, but no distinct supporting threat tally is supplied.
3. **Zero-defense attack counts:** the seven zero-defense coordinates have Table 5 values 9,4,6,3,1,1,0. Six are positive, while EF3 says three contain documented attacks. The matrix mixes paper roles, so this is unresolved rather than automatically a proven count error. Figure 8's L4×T4 caption says two attack papers while Table 5 says three assignments.
4. **Defense projection:** literal expansion of Table 7 gives memory access control plus consensus at L3×T3, plus invariants, for three, matching Figure 8. At L7×T3 it gives behavioral monitoring, human review, and interpretability, also three, matching Figure 8. However, at L3×T1/T2 Table 7 supports two each, also matching. Thus the printed matrix is reproducible under the table's listed intervals; no extra unlisted defense is needed. The apparent ambiguity is effectiveness, not these cell arithmetic totals.
5. **L7×T4:** Table 10 says zero defense coverage; Figure 8 says two claimed classes. The prose says coverage is overstated, but does not explicitly reconcile zero versus two.
6. **Coding exceptions:** Appendix B's sleeper example first says L7 implications are discussion rather than contribution, then includes L7×T4. It also includes L1×T3 through persistent weights despite the explicit T3 memory-write requirement. Figure 7 acknowledges overlapping governance coding. These undermine an uncomplicated reading of the rules.
7. **Version/cutoff drift:** main text gives April 2026 and 22 new papers; Table 13 retains April 2025 and seven entries; Appendix B retains selected-zone count eight. These appear to be unreconciled reporting versions, but that diagnosis is analyst interpretation.
8. **Taxonomy labels:** Appendix E and Table 15's caption group PoisonedRAG with LLM01; its actual row says LLM03. Table 15 uses the 2023 OWASP taxonomy while reference [51] names the 2025 edition.
9. **Reference integrity:** text names for [89], [132], [134], [168], [170], and [172] do not match the corresponding supplied bibliography authors. References [43]/[44] duplicate a title; [139]/[140] share a title and arXiv identifier but differ in authors. The bibliography ends at [180] although p. 6 reports 186 entries. These are internal observations, not external citation validation.
10. **Robustness scope:** Table 13 says 4.81–8.33%, but role ablation reaches 4.76%. The 'below 9% across all runs' statement is stronger than the displayed 95% intervals alone demonstrate. The absent script prevents checking tails or the ±0.8 percentage-point claim.

These issues do not erase the architecture argument. They lower confidence in exact corpus reproducibility, universal quantifiers, severity rankings, and claims that the proposed schema closes measured gaps. The paper's own caveats support treating its maps as a structured research synthesis rather than a validated security guarantee.

## 15. Contributions and Novelty

Conceptual contributions are LASM's seven control surfaces and the orthogonal T1–T4 classification. Methodological contributions are explicit layer/time decision rules and corpus mapping. The theoretical contribution is the conditional non-transferability proposition/theorem with proof sketch. Empirical synthesis contributions are four numbered findings about volume, L4 root cause, defense asymmetry, and benchmark coverage. Prescriptive contributions are fifteen defense classes, seven joint recipes, and five dependency-organized gaps. [A, pp. 3, 11–16, 33–41]

Artifact contributions are claimed for coding CSV, re-derivation and robustness scripts, and an ABOM schema/validator with two examples and twelve tests. These are not inspected. ABOM and action logs are conceptual/specification proposals; the paper does not supply an evaluated runtime enforcement system. There is no new model architecture, trained model, attack benchmark dataset, or security tool implementation demonstrated in the supplied main document. Novelty relative to other literature is the author's comparison in Table 12, not independently established here.

## 16. Limitations

### Authors' stated limitations

Search terms miss work framed without agent vocabulary, explicitly including 'LLM-driven web crawler'. Citation thresholds and venue preferences create selection bias. Conference talks, advisories, vendor red-team reports, and much industry material are excluded, with selected incident exceptions. The corpus is nonexhaustive. Coding is single-author, lacks formal inter-rater reliability, and has uncertain cell assignments. Perturbation analysis does not capture systematic coding bias. [A, pp. 5–7, 57]

LASM assumes a deployment architecture and requires per-deployment applicability. MCP percentages come from a study described in the body as a preliminary preprint. ABOM is not a ratified standard; action logs are unvalidated proposals. The steganographic information-theoretic argument is informal. Defense coverage is published/claimed coverage, not a deployment census or demonstrated effectiveness. Interpretability is component-level, human review scales poorly, and T4 defense claims lack benchmark validation. [A, pp. 26, 28, 35, 54]

### Additional evidence-based analyst observations

Counts have unresolved version and coding inconsistencies. Coverage cells combine attacks, defenses, benchmarks, theory, and comparison surveys, making 'attack coverage' an imprecise shorthand. No operational severity scoring supports a statistical inverse correlation. Literature absence does not establish zero real-world defense capability. No controlled web-agent-versus-standalone experiment is conducted by this paper. Broad statements about all evaluations, no defensive agents, or universal regulatory absence exceed what its nonexhaustive corpus can conclusively establish. [D]

The paper describes its first three introductory scenarios as production incidents, but some later caseboxes are plainly hypothetical. These evidence types must remain separate. An authenticated or hashed component can still be malicious; the paper's own recipe residuals acknowledge this. Accordingly, ABOM enumeration and signed logs should not be interpreted as proof of benign semantics or faithful intent. [A/D, pp. 2, 19, 21, 37, 57]

## 17. Threats to Validity

The following labels are analyst classifications of source-grounded concerns. **Internal validity:** this is a descriptive synthesis, so its main vulnerabilities are inconsistent coding and reporting rather than treatment-confounding in an original experiment. Missing per-paper assignments prevent checking whether classification decisions produce the stated matrices. **Construct validity:** assignment volume is used as research effort; claimed class coverage as defense coverage; qualitative examples as severity. These constructs are related but not interchangeable. [D]

**External validity/generalizability:** the selected venues, citation thresholds, vocabulary, and cutoff restrict transfer to all web agents, industry systems, and later deployments. Results from one visual-agent benchmark or one toolchain should not become a general vulnerability percentage. **Statistical conclusion validity:** descriptive counts and robustness intervals do not establish a severity correlation or independent observations, since papers can occupy multiple cells. [D]

**Ecological validity:** simulations, hypothetical HelpDesk/sleeper cases, controlled poisoning experiments, and real incidents supply different evidence. The paper explicitly qualifies simulated drift around 1,000 interactions as environment-dependent. **Reproducibility:** screening counts and aggregate matrices are supplied, but exact queries, role coding, alternative assignments, seeds, scripts, and full proof are unavailable in this input. A claimed twelve-test schema suite does not validate security effectiveness. [A/D, pp. 31, 53–57]

## 18. Future Work and Open Questions

### A. Author-proposed work

Gap 1 is multi-session benchmarking with memory serialization, replay, ground truth, and future-session behavior metrics. The evaluation recommendation is at least five session transitions between injection and exploitation. Gap 2 is detection of emergent misalignment using longitudinal datasets, statistical monitoring, and causal separation of drift from legitimate adaptation. Gap 3 is detection of collusion using previously unseen encodings. Gap 4 is ABOM standardization, automated generation, and MCP certification. Gap 5 is trajectory attribution, formal plan verification, liability allocation, and accountable action records. [A, pp. 38–40]

Proposed approaches are formal security models and composition theorems; runtime attestation tied to verified principals; persistent tamper-evident logs and deployment-specific baselines; stakeholder governance; and defensive autonomous agents. The dependency account prioritizes benchmarks, pursues standards and accountability in parallel, and treats misalignment/collusion as longer-term research. The paper calls gaps 1/4/5 near-term tractable while Table 10 classifies gap 5 as multidisciplinary; these are judgments, not delivery estimates. [A, pp. 39–42]

### B. Additional questions remaining from this analysis

Can independent coders reproduce the matrix under strictly enforced T3/T4 rules? How does the distribution change when paper roles and unique incidents are separated? What explicit severity rubric would support or reject the inverse-correlation claim? Can identical models be compared under standalone, browsing-only, tool-action, memory, and delegation conditions? Which proposed controls reduce harm under adaptive attacks while preserving legitimate completion and reporting false positives? These are analyst-derived research questions, not experiments already conducted by the author. [D]

## 19. Terminology and Notation Glossary

| Term | Meaning in this analysis |
|---|---|
| LLM | Large language model, the language-generating core. |
| AI agent | Model-based system that perceives, maintains state, plans, and acts through tools or peers. |
| LASM | Layered Attack Surface Model: seven analytical security layers. |
| L1 / L2 / L3 | Foundation / cognitive planning / memory. |
| L4 / L5 / L6 / L7 | Tool execution / coordination / ecosystem / governance. |
| T1 / T2 | Same-inference effect / persistence within one session. |
| T3 | Persistent-memory write exploited in a later session. |
| T4a / T4b | Payload-free drift / dormant training-or-weight trigger. |
| Principal | Actor or source with instruction authority. |
| Trust inversion | Lower-authority environmental material treated as authoritative. |
| RAG | Retrieval-Augmented Generation, retrieval of outside context for generation. |
| CoT | Chain-of-thought, a stated reasoning trace. |
| MCP | Model Context Protocol, the paper's tool-connection protocol surface. |
| SBOM / ABOM | Software / Agent Bill of Materials. |
| CIA | Confidentiality, integrity, availability: security goals. |
| RBAC | Role-based access control; permission restrictions by role. |
| BFT | Byzantine fault tolerance, resistance to faulty/malicious participants. |
| GCG | Greedy Coordinate Gradient, a cited adversarial-suffix method. |
| OOD | Out of distribution, outside the training/evaluation distribution. |
| FPR / AUROC | False-positive rate / area under the receiver-operating-characteristic curve. |
| TEE | Trusted execution environment, proposed substrate for attestation. |
| PRISMA / SoK | Systematic-review reporting framework / systematization of knowledge. |
| DAG | Directed acyclic graph; used for research-gap prerequisite structure. |
| Li, Ri, Bi, Di | Layer, representation, trust boundary, and defense set/leverage points. |
| P(Li,Tk) | Number of coded papers in a layer/time cell, not a probability. |
| U | Selected six-cell zone L5–L7 × T3–T4. |
| τ(a) | Temporality class of attack a. |
| H(X) | Per-token entropy in the informal covert-channel argument. |

## 20. Key Numerical Results

All cited-study values below are author-reported secondary results. They were not independently verified against the original cited works.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Search period | Jan 2021–Apr 2026 | dates | Two-phase reported search | Author-reported | pp. 4–5 |
| Retrieved / retained | 1,634 / 116 | records / papers | Screening | Author-reported | Table 2, p. 6 |
| Duplicates / abstract / full-text exclusions | 513 / 808 / 197 | records | Consecutive stages | Author-reported | Table 2 |
| Main corpus categories | 38/26/16/18/13/5 | papers | Attacks L1–4 / attacks L5–6 / governance / defenses / evaluation / surveys | Author-reported | p. 5 |
| Recent-paper exception | 26 of 44 | papers | Jan 2025–Apr 2026; 18 met citation threshold | Author-reported | p. 5 |
| Architecture/time grid | 7×4=28 | cells | LASM | Author-reported | pp. 1, 11–14 |
| Coded assignments | 144 | assignments | 116 overlapping papers | Visually readable | Table 5 |
| Selected-zone share | 9/144=6.25% | percent | Rounds to reported 6.3% | Analyst-derived | Table 5, p. 16 |
| Zero-defense share | 7/28=25% | percent of cells | Claimed class coverage, not attack risk | Analyst-derived | pp. 34–36 |
| Delayed benchmark coverage | 0 of 10 | benchmarks | Table 9, T3/T4 | Author-reported | pp. 37–38 |
| ARE attack success | 67% | success rate | Less than 5% webpage-pixel perturbation | Author-reported | p. 16 |
| MINJA injection | 98.2% | success rate | Query-only memory injection | Author-reported | p. 7 |
| PoisonedRAG | >90% | targeted corruption | As few as 5 documents in 10,000+ corpus | Author-reported | p. 20 |
| AgentPoison | >80% | attack success | Poison rate below 0.1% | Author-reported | p. 20 |
| A-MemGuard | >95%; ~15% | mitigation; throughput overhead | Consensus memory validation | Author-reported | p. 21 |
| Multi-tool injection | >60% | attack success | Cited leading-model scenarios | Author-reported | p. 22 |
| Coding-agent injection | 50–80% | attack success | Cited production model families | Author-reported | p. 22 |
| Cross-tool contamination | 75% | vulnerability rate | LangChain/LlamaIndex settings | Author-reported | p. 23 |
| One-day exploitation | 87% vs 0% | exploit success | GPT-4 agent vs listed comparators; denominator absent | Author-reported | p. 23 |
| Infectious spread | >1,000,000 | peer agents | Cited repeated visual-agent relay | Author-reported | p. 24 |
| Collusion | 74.4% | success | Experimental paired-agent deception; attribution inconsistent | Author-reported | p. 25 |
| Collusion probe | 1.00 | AUROC | In-distribution only; shift degrades | Author-reported | p. 25 |
| MCP preliminary flaws | 43/43/33/5% | servers | OAuth / command injection / outbound access / poisoning; exact denominator absent | Author-reported | pp. 26–27 |
| MCP toxicity | 73% | mean attack success | Cited malicious-server response setting | Author-reported | p. 27 |
| MCP benchmark sizes | 14/6; 8 | categories/agents; clients | Two cited benchmark descriptions | Author-reported | p. 27 |
| Malicious servers | 47 | servers | Cited public registries; bibliographic mismatch | Author-reported | p. 27 |
| Fine-tuning poisoning | 100 | examples | As few as, cited instruction-tuning attack | Author-reported | p. 27 |
| Insecure completion | ~40% | scenarios | Cited code-completion study | Author-reported | p. 27 |
| Sleeper detection | 92.5% | accuracy | Known implementations only | Author-reported | p. 19 |
| Drift timescale | ~1,000 | interactions | Simulation; order-of-magnitude caveat | Author-reported | p. 31 |
| Agent safety compliance | <60% | task instances | Cited tool-enabled tasks; comparison details absent | Author-reported | p. 32 |
| Cross-session monitoring | <20% | deployments | Cited enterprise survey; denominator absent | Author-reported | p. 32 |
| Lost audit evidence | ≥30% | causal evidence | All evaluated frameworks, as reported | Author-reported | p. 32 |
| T3 evaluation recommendation | ≥5 | session transitions | Injection to exploitation; proposed protocol | Author-reported | p. 38 |
| Leave-one-out range | 5.56–6.94% | selected-zone share | n=116 | Visually readable | Table 14 |
| Paper-drop interval | 4.81–7.48% | 95% interval | 10% drop, 10^4 runs | Visually readable | Table 14 |
| Cell perturbation interval | 5.83–8.33% | 95% interval | p=0.10, 10^4 runs | Visually readable | Table 14 |
| Role-ablation range | 4.76–7.62% | selected-zone share | Drop survey / context role | Visually readable | Table 14 |
| Claimed ABOM tests | 12 | tests | Absent supplementary suite | Author-reported | pp. 1, 53 |

The illustrative $500 threshold, six-week delay, and $2,000 refund belong to the HelpDesk scenario, not an observed loss distribution. Figure 2's early-year bar heights are deliberately not turned into exact values. No approximate visual estimate is used as a key quantitative result.

## 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Analysis | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Agents add state, plans, tools, and peer interactions | Explicit architecture and definitions | Figures 3/5 | pp. 1, 7–11 | HIGH for reported architecture; no universal deployment census |
| External content can cross into instruction authority | Principal hierarchy and injection examples | X3, Figure 3 | pp. 8–9, 22–23 | HIGH for mechanism described; universality is stronger |
| Review contains 116 papers | Screening arithmetic | X1, Table 2 | pp. 5–6 | HIGH for reported counts; search exports absent |
| Selected delayed high-layer zone has 9/144 assignments | Exact six-cell sum | X2, Table 5 | pp. 12, 16 | HIGH aggregate reading; coding inconsistencies lower reproducibility |
| Pure defenses cannot discriminate unobserved localized changes | Distribution-invariance proof sketch | E3, Appendix C | pp. 12, 56 | Conditional result; excludes cross-layer observations/effects |
| Claimed defenses leave seven zero cells | Listed classes and heatmap | X4, Tables 7/ Figure 8 | pp. 34–36 | HIGH for claimed coverage; not measured protection |
| No T3/T4 benchmark among ten tabulated entries | All listed time labels stop at T2 | X5, Table 9 | pp. 37–38 | HIGH table finding; universal absence unverified |
| EF1 remains small under listed perturbations | Four protocol summaries | X8, Table 14 | pp. 56–57 | MEDIUM; scripts absent, bias excluded |
| Different attack mechanisms need different control locations | Five defense-placement cases | X6, Table 15 | pp. 57–58 | MEDIUM; labels conflict and prescriptions untested |
| Web agents have additional compromise pathways | Browsing feedback, pixels, tools, persistence | X9, Sections 3–4 | pp. 16–28 | Analyst inference; no new controlled standalone comparison |
| ABOM/logging make gaps concrete | Proposed field lists and records | Tables 6/8, Appendix F | pp. 28–29, 37, 57 | HIGH specification reading; effectiveness not validated |

## 22. Very Simple Explanation

A standalone language model mostly writes an answer. A web agent can read a page, decide what to do next, click or call a tool, remember what happened, and continue later. The paper argues that these extra abilities create extra ways to be tricked. A page that should count only as information can contain instructions that the agent mistakenly treats as orders.

Memory makes the problem last longer. The agent might save a bad instruction today and act on it weeks later. Tools make the consequences larger: a mistaken sentence can become a payment, a file change, or a message. Other agents can spread the bad instruction through apparently legitimate communication. Checking only the first prompt or final answer misses much of this process.

The paper proposes a map with seven places where attacks can happen and four ways their effects unfold over time. Its literature tables suggest that researchers study immediate attacks much more than delayed system-level failures. But the map contains inconsistent counts and classifications, and its suggested defenses are often proposals rather than proven protections. It helps explain why web agents can have additional vulnerabilities; it does not establish a single number showing how much more vulnerable they are than standalone models.

## Completeness Audit

The denominator is the supplied 58-page document: seven major numbered sections, their substantive subsections, five research questions, eight figures, fifteen tables, eight mathematical/specification concepts identified above, nine synthesis analyses, five contribution groups, and six appendices. Text-only pages are not counted as visually inspected. Coverage is substantive representation rather than preservation of every sentence or citation.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, author, abstract, keywords, corresponding-author footnote | Yes, visual/text | Yes | Represented in compressed form | Kexin Chu, University of Connecticut; arXiv:2604.23338v2, 6 May 2026; no publication venue established for this paper |
| §1 framing, scope, contributions, existing-work limitations | Yes | Yes | Fully represented | Orientation, problem, questions, novelty |
| §2.1.1 search strategy | Yes | Yes | Fully represented | Databases, terms, periods |
| §2.1.2 inclusion/exclusion | Yes | Yes | Fully represented | Thresholds and recent-gap exception |
| §2.1.3 screening/coding/statistics | Yes | Yes | Fully represented | Counts, units, role categories, coding |
| §2.1.4 caveats / §2.1.5 extension | Yes | Yes | Fully represented | Biases and conflicting versions retained |
| §2.2.1 components | Yes | Yes | Fully represented | Architecture and memory types |
| §2.2.2 hierarchy/actors / §2.2.3 threat model | Yes | Yes | Fully represented | Actor table and four dimensions |
| §2.3.1 design/definition/proposition/EF1 | Yes | Yes | Fully represented | Assumptions and proof limits |
| §2.3.2 temporality | Yes | Yes | Fully represented | T1–T4a/b and coding conflicts |
| §3.1.1 jailbreak / §3.1.2 multimodal | Yes | Yes | Represented in compressed form | Mechanisms and web result retained |
| §3.1.3 extraction/IP / §3.1.4 defenses | Yes, partly text-only | Yes | Represented in compressed form | Extraction, prompt exposure, filtering/training limits |
| §3.2.1 planning / §3.2.2 CoT | Yes, text-only for pp. 17–18 | Yes | Represented in compressed form | Goal manipulation and unfaithful traces |
| §3.2.3 reward hacking / §3.2.4 sleepers / §3.2.5 defenses | Yes | Yes | Represented in compressed form | Drift versus trigger distinction and metrics |
| §3.3.1 memory architecture/lifecycle | Yes, p. 20 text-only | Yes | Fully represented | Write/read/consolidate/share and privacy |
| §3.3.2 RAG poisoning | Yes, text-only | Yes | Fully represented | Main results and conditions |
| §3.3.3 temporal escalation / §3.3.4 defenses | Yes | Yes | Fully represented | Illustrative status and overhead preserved |
| §3.4 introductory EF2 / §3.4.1 injection | Yes, text-only pp. 22–23 | Yes | Fully represented | Mechanism, outcomes, scope caveat |
| §3.4.2 capability creep / §3.4.3 exploitation / §3.4.4 defenses | Yes, text-only | Yes | Represented in compressed form | Definition, 87% comparison, controls |
| §4.1.1 trust chains | Yes | Yes | Fully represented | Network propagation and signing limitation |
| §4.1.2 collusion / §4.1.3 Byzantine agents | Yes, p. 25 text-only | Yes | Represented in compressed form | Hidden coordination, informal bound, stochastic/dynamic fault caveats |
| §4.1.4 defenses | Yes | Yes | Fully represented | Diversity, authentication, isolation |
| §4.2.1 MCP | Yes, p. 27 text-only | Yes | Fully represented | Preliminary and later study claims separated |
| §4.2.2 supply chains | Yes | Yes | Represented in compressed form | Checkpoints, packages, skills, templates |
| §4.2.3 ABOM / §4.2.4 defenses | Yes | Yes | Fully represented | Fields, attestation, conceptual status |
| §4.3 role / §4.3.1 insider | Yes, partly text-only | Yes | Represented in compressed form | Emergent failures and temporal distinctions |
| §4.3.2 accountability / §4.3.3 drift | Yes, text-only | Yes | Fully represented | Chain, causal limits, simulation caveat |
| §4.3.4 governance | Yes, text-only pp. 31–32 | Yes | Represented in compressed form | Logging, oversight, liability, certification; legal claims remain unverified author reports |
| §5.1 archetypes/mapping | Yes | Yes | Fully represented | Defense corpus discrepancy retained |
| §5.1.1–5 filtering/memory/sandbox/authentication/monitoring | Yes | Yes | Fully represented | Class mappings and limitations |
| §5.1.6 depth / §5.1.7 coverage / §5.1.8 recipes | Yes | Yes | Fully represented | Joint controls, residual risks, seven zeros |
| §5.2 synthesis | Yes | Yes | Fully represented | Infrastructure prerequisites |
| §5.3.1 benchmarks / §5.3.2 evaluation issues / §5.3.3 recommendations | Yes | Yes | Fully represented | Adaptive attackers, false positives, ≥5 transitions |
| §6.1 gaps / §6.2 dependencies | Yes | Yes | Fully represented | Five nodes and qualifications |
| §6.2.1–5 future directions | Yes | Yes | Represented in compressed form | Every direction and target retained |
| §6.3 comparison | Yes | Yes | Represented in compressed form | Author positioning, not outside validation |
| §7 conclusion / competing-interest declaration | Yes, p. 42 text-only | Yes | Represented in compressed form | Security as system problem; author declares no competing interests |
| RQ1 / RQ2 / RQ3 / RQ4 / RQ5 | Yes, each | Yes, each | Fully represented | Explicit answers and evidence limits |
| Formal hypotheses | None identified | Yes | Fully represented | No separate statistical hypotheses supplied |
| X1 screening / X2 coding / X3 root cause | Yes | Yes | Fully represented | Distinct analyses, not new controlled experiments |
| X4 defense / X5 benchmark / X6 taxonomy comparison | Yes | Yes | Fully represented | Coverage and label limitations |
| X7 sensitivity / X8 robustness / X9 cited experiments | Yes | Yes | Represented in compressed form | Protocols and important outcomes retained |
| F1 / F2 / F3 / F4 | Yes, visually | Yes, individually | Fully represented | Figure section includes encodings and caveats |
| F5 / F6 / F7 / F8 | Yes, visually | Yes, individually | Fully represented | All panels and matrix meanings accounted for |
| T1 / T2 / T3 / T4 / T5 | Yes, visually | Yes, individually | Fully represented | Counts and conceptual mappings |
| T6 / T7 / T8 / T9 / T10 | Yes, visually | Yes, individually | Fully represented | Schema, classes, recipes, benchmarks, gaps |
| T11 / T12 / T13 / T14 / T15 | Yes, visually | Yes, individually | Fully represented | Directions, comparisons, limits, robustness, labels |
| E1 hierarchy / E2 layer definition / E3 theorem | Yes | Yes | Fully represented | Notation and assumptions |
| E4 coverage / E5 temporal classes / E6 composition | Yes | Yes | Fully represented | Operands and meanings |
| E7 covert scaling / E8 encodings and schema domains | Yes | Yes | Fully represented | Informal/proposed status explicit |
| Standalone algorithms/pseudocode | None identified | Yes | Fully represented | JSON/schema examples are specifications |
| Five claimed contribution groups | Yes | Yes | Fully represented | Conceptual, temporal, empirical, prescriptive, agenda |
| Appendix A / Table 13 limitations | Yes | Yes | Fully represented | All nine limitation categories |
| Appendix B.1–B.4 | Yes | Yes | Fully represented | Rules, worked examples, sensitivity conflicts |
| Appendix C | Yes | Yes | Fully represented | Supplied sketch only; full proof absent |
| Appendix D | Yes | Yes | Fully represented | All four protocols and limits |
| Appendix E | Yes | Yes | Fully represented | Label contradiction explicit |
| Appendix F | Yes | Yes | Fully represented | Identity, principals, context, action, reasoning, integrity |
| References pp. 42–53 | Yes, mostly text-only | Yes | Represented in compressed form | Used for internal cross-checks; not independently followed |
| Supplementary CSV/scripts/proof/examples/ABOM tests | No | Absence represented | Missing from supplied material | No execution or review claimed |

### Missing or inaccessible material

The original cited studies, search exports, per-paper coding CSV, re-derivation script, robustness implementation, alternative codings, two supplementary worked examples, full theorem proof/corollaries, and ABOM schema/validator/examples/tests were not supplied. Exact experimental settings behind many secondary statistics are therefore unavailable. Visual page layouts for the 21 text-only pages cannot be assessed, although their supplied text was inspected.

### Uncertain interpretations

Unresolved issues include 144 versus multiplicity-implied 146 assignments; defense corpus 18 versus 15; selected-zone baseline eight versus nine; cutoff/extension differences; the precise role distinction behind 'three' attacked zero-defense cells; L7×T4 zero versus two claimed defenses; inconsistent PoisonedRAG OWASP labels; bibliography count and author mismatches; the theorem's baseline wording; and robustness ranges versus universal run claims. Table 12's circle/dash distinction is undefined. These are reported rather than repaired. Confidence is HIGH that the conflicting passages exist, but LOW or UNKNOWN about the intended corrected values.

### Deliberately compressed material

Repeated descriptions of trust inversion, defense-in-depth, and the selected sparse zone are consolidated. Individual citation histories, every model-family name, foundational-reference details, and repetitive inline takeaways are compressed. The named attack families, major numerical conditions, all visual objects, all substantive sections, and all author-stated limitation categories remain represented. Legal discussion is summarized as the author's argument without introducing current legal advice or external verification.

### Potential omissions

No known substantive inventory object is left wholly unrepresented within the supplied material. This does not mean every sentence, citation, field example, or secondary illustration is reproduced. Supplementary evidence remains unreviewed, and absent experimental details prevent complete reconstruction of the cited studies. The report is comprehensive relative to the stated inventory, not a claim of independently verified scientific completeness.
