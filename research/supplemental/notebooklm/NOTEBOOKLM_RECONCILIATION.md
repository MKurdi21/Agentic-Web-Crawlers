# NotebookLM evidence-table reconciliation

**Current documentation note — 2026-10-18:** the three corpus-side D2 labels identified below were corrected to ASR in a separately source-verified review. CORPUS-01–03 retain the intake classification as historical evidence; none of the 3,172 NOT_CHECKED entries is promoted. Both raw exports are approved for local Git tracking only, not publication. The ten amendment clauses remain proposals; no Protocol V1.2 is created or approved. The original intake/preservation/readback narrative below describes the earlier reconciliation task. See the [current documentation audit](../../../docs/DOCUMENTATION_SYNCHRONIZATION_AUDIT.md) for subsequent synchronization.

Completed 2026-10-18T20:11:38.558200+00:00. Status: reconciliation complete within the explicit review scope below; stop for scientific review. Neither NotebookLM status labels nor this reconciliation constitute independent human scientific validation.

## Findings and review scope

The workbook evidence sheet maps to all 123 canonical record identities. The CSV maps to 121, omitting BrowseComp and The Long-Horizon Task Mirage. The workbook reference sheet contains 122 identities and omits WebCloak. No unmatched table title identifies a new paper for automatic admission. Known versions of Mind the Web and AgentVigil/AgentFuzzer remain linked study families, not independent replications.

**Coverage:** all cells in both visible worksheets and the CSV were parsed and retained in the crosswalk. All 366 row identities were reconciled (123+121+122 reference rows). Scientific checking was prioritized:40 assertion templates were reviewed against both evidence tables (80 targeted checks) across 18 papers. All 123 canonical physical title pages were read. Selected methods/results/appendix pages of the 18 prioritized sources were inspected from canonical PDFs and their hashes checked; existing records/summaries and the 198-entry extension evidence map supplied additional context. TRAP physical p.7 and Silent Failures physical p.5 were newly rendered and visually inspected. This is not a full scientific revalidation of every cell or all 123 papers.

The 4,140-row [CSV crosswalk](NOTEBOOKLM_SOURCE_CROSSWALK.csv) distinguishes identity matches, original source cells, targeted assertions, identifier audits and corpus-side corrections. All 3,660 source cells are retained once. **3,172 cells remain NOT_CHECKED scientifically.** A matched identity is not a validated finding. Related record-claim IDs are navigation candidates sharing page ranges, not a claim that every listed record claim independently entails the assessment.

## Inputs and byte preservation

| Actual file in raw/ | Bytes | SHA-256 before and after |
|---|---:|---|
| `Comprehensive Evidence Table of AI Agent Literature Review - Table 1.csv` | 271183 | `4286dd4414cb5c5c3c292d81260fb775a7d528904defe4957065ed6eea8b1efe` |
| `Agentic Web Traps Literature Evidence Table.xlsx` | 137842 | `d33fb6c3d13288dd1626566ff9c1b768fb62add7a5b4e823cb7a9e2b1a5c2239` |

Both files remain at their original paths. Neither file was moved, renamed, replaced, saved through Excel or duplicated. Derived analysis was kept separate. Workbook inspection used read-only ZIP/XML; CSV inspection used the CSV parser with UTF-8-SIG and preserved original field values. No formulas were evaluated or external links followed.

| Table | Header row | Data rows | Columns | Formula cells |
|---|---:|---:|---:|
| CSV |1|121|14|0|
| Table 1 |1|123|14|0|
| Source References |1|122|2|0|

Both Excel worksheets are visible. There are no comments, embedded objects or external-link parts in the workbook package, and no defined names. The CSV has 122 physical lines including its header and no multiline records. No separate field dictionary is supplied.

## Field definitions and source-reference semantics

- `Paper`/`Paper Identity` is bibliographic prose, sometimes mixing title, authors, year, venue and identifier. Match the title/family first; audit the accompanying metadata separately.
- `Findings`/`Key Findings` are NotebookLM renditions of claimed results. Preserve condition, denominator, action stage, privilege and evidence maturity. A source quotation does not validate the whole composite cell.
- `Author Limitations` attempts attribution to authors. `Inferred Gaps (AHRQ Type)`, `Inferred Research Gaps`, controls, untested scenarios and research questions are NotebookLM interpretation unless corroborated as explicit author statements. AHRQ labels are not author-defined experimental variables or validated novelty decisions.
- `Internal Contradictions` often mixes genuine numerical conflicts with tradeoffs, nested outcomes, different conditions and scoped non-goals. Coexistence is not contradiction.
- `Cross-Paper Contradictions`/comparisons do not establish causal disagreements when tasks, access, models or endpoints differ. Broad comparison cells outside the prioritized checks remain NOT_CHECKED.
- `Exact Supporting Evidence/Citations`, `Supporting Citations` and `Cross-Check Evidence` are assertions to inspect, not independent provenance receipts. Some include misattributed IDs, placeholders and imprecise page references.
- `Verification Status` contains Verified/VERIFIED or SOURCE-VERIFIED. No original per-cell independent verification receipts accompany those labels; this reconciliation does not inherit them.
- `Source` and reference-sheet `Index` are file-local labels. They are neither canonical paper IDs nor stable cross-file keys.

## Matching, duplicates and numeric-ID failures

Full titles, explicit short-title aliases, source filenames, inspected title pages and version/family metadata were used. Fuzzy suggestions were manually resolved for shortened names (Go-Browse, VisualWebArena, DoomArena, Task Shield, ceLLMate and AI Agent Traps). Row position never selected the study.

Each evidence table maps to distinct canonical records under the documented version candidates. There are no duplicate canonical identity rows within either table after reconciliation. However, punctuation-normalized Mind-the-Web titles collide across the 13-page preprint and 17-page proceedings source; AgentFuzzer’s filename contains a 14-page Generic AgentVigil manuscript, while the other14-page AgentVigil PDF bears Automatic in its title. These two known families must not be pooled as independent studies. Exact version association remains QUALIFIED where NotebookLM metadata is insufficient; a spelling or numeric label alone does not establish byte equivalence.

| Namespace | Reused Source ID | Evidence rows and identities |
|---|---|---|
| CSV | 49 | 50: Defending Against Indirect Prompt Injection Attacks With Spotlighting; 51: Dissecting Adversarial Robustness of Multimodal LM Agents; 52: How Adversarial Environments Mislead Agentic AI? |
| CSV | 62 | 63: Autonomy Comes with Costs: Detecting Denial-of-Service Vulnerabilities Caused by Resource Abusing in LLM-based Agents; 64: SecAlign: Defending Against Prompt Injection with Preference Optimization; 65: The Impact of Crawl Policy on Web Search Effectiveness |
| CSV | 89 | 90: Prompt Injection Attack to Tool Selection in LLM Agents; 91: ReAct: Synergizing Reasoning and Acting in Language Models; 92: ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents |
| Table 1 | 42 | 43: LASER: LLM Agent with State-Space Exploration for Web Navigation; 44: Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems; 45: WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections |
| Table 1 | 107 | 108: BEARCUBS: A benchmark for computer-using web agents; 109: WebCloak: Characterizing and Mitigating Threats from LLM-Driven Web Agents as Intelligent Scrapers |

The CSV has 115 unique numeric labels for 121 rows; the workbook evidence sheet has 120 for 123 rows. Across 113 numeric labels appearing in both tables,104 map to different study sets. This demonstrates incompatible namespaces, not 104 additional scientific contradictions.

**Wrong workbook joins:** Table 1 row44 Source42 resolves to LASER rather than Retrieval Barrier; row45 Source42 resolves to LASER rather than WARD; row109 Source107 resolves to BEARCUBS rather than WebCloak. The raw reference list is preserved and these three joins are CONTRADICTED in the crosswalk.

## Bibliographic identifier audit

There are31 explicitly flagged entries:18 supplied numeric arXiv IDs disagree with the locally bound title-page/admission identity, and 13 are placeholders. VERSION_MISMATCH here includes a misattributed or unusable identifier; it does not assert that an alternative online version was fetched. Years may differ legitimately between preprint and proceedings; undetermined dates are not silently corrected. For example, the AI Agent Traps year varies across tables and remains unresolved by a blanket year substitution.

| Workbook row | Matched study | Supplied identifier | Local bound identity |
|---|---|---|
| 2 | Defeating Prompt Injections by Design | `2503.10566` | 2503.18813 |
| 9 | PlanGuard: Defending Agents against Indirect Prompt Injection via Planning-based Consistency Verification | `2503.18666` | 2604.10134 |
| 20 | WEBLINX: Real-World Website Navigation with Multi-Turn Dialogue | `2402.08752` | 2402.05930 |
| 21 | Prismata: Confining Cross-Site Prompt Injection in Web Agents | `2506.08837` | 2607.08147 |
| 23 | AgentVigil: Generic Black-Box Red-teaming for Indirect Prompt Injection against LLM Agents | `2501.XXXXX` | 2505.05849 |
| 26 | SafeArena: Evaluating the Safety of Autonomous Web Agents | `2410.xxxxx` | No own arXiv ID established from the local title page; use source hash/publication identity |
| 29 | AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks | `2602.xxxx` | 2602.16901 |
| 45 | WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections | `2604.15231` | 2605.15030 |
| 47 | How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation | `2605.xxxxx` | 2606.16821 |
| 51 | Untrusted Content Masking for Web Agents with Security Guarantees | `2607.xxxxx` | No own arXiv ID established from the local title page; use source hash/publication identity |
| 55 | BrowseSafe: Understanding and Detecting Prompt Injection Within AI Browser Agents | `2503.XXXXX` | 2511.20597 |
| 57 | Silent Failures in Agentic Security Evaluation: A Validated Harness for Tool-Call Mediation Under Indirect Prompt Injection | `2510.XXXXX` | 2609.32691 |
| 59 | Honeyval: A Comprehensive Evaluation Framework for LLM-powered HTTP Honeypots | `2602.00000` | 2605.29963 |
| 64 | Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents | `2508.07575` | 2601.10955 |
| 66 | LoopTrap: Termination Poisoning Attacks on LLM Agents | `2602.15763` | 2605.05846 |
| 67 | A Framework for Studying AI Agent Behavior: Evidence from Consumer Choice Experiments | `2505.11584` | 2509.25609 |
| 75 | One Polluted Page Is Enough: Evaluating Web Content Pollution in Generative Recommenders | `2601.08584` | 2606.13610 |
| 83 | When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents | `2605.06812` | 2607.01641 |
| 88 | A Survey on Autonomy-Induced Security Risks in Large Model-Based Agents | `2603.xxxxx` | No own arXiv ID established from the local title page; use source hash/publication identity |
| 91 | Breaking Agents: Compromising Autonomous LLM Agents Through Malfunction Amplification | `2403.02691` | 2407.20859 |
| 92 | Odysseys: Benchmarking Web Agents on Realistic Long Horizon Tasks | `2504.12516` | 2604.24964 |
| 93 | SnapGuard: Lightweight Prompt Injection Detection for Screenshot-Based Web Agents | `2602.XXXXX` | 2604.25562 |
| 94 | WebRollback: Enhancing Web Agents with Explicit Rollback Mechanisms | `2503.XXXXX` | No own arXiv ID established from the local title page; use source hash/publication identity |
| 95 | WebWalker: Benchmarking LLMs in Web Traversal | `2501.XXXXX` | No own arXiv ID established from the local title page; use source hash/publication identity |
| 96 | AdvAgent: Controllable Blackbox Red-teaming on Web Agents | `2409.11295` | 2410.17401 |
| 107 | CELLMATE: Sandboxing Browser AI Agents | `2502.01822` | 2512.12594 |
| 108 | BEARCUBS: A benchmark for computer-using web agents | `2503.02888` | 2503.07919 |
| 111 | Why Do LLM-based Web Agents Fail? A Hierarchical Planning Perspective | `2510.02418` | 2603.14248 |
| 112 | A Systematic Survey of Security Threats and Defenses in LLM-Based AI Agents: A Layered Attack Surface Framework | `2603.xxxxx` | 2604.23338 |
| 113 | Commercial LLM Agents Are Already Vulnerable to Simple Yet Dangerous Attacks | `2502.xxxxx` | 2502.08586 |
| 116 | Identifying AI Web Scrapers Using Canary Tokens | `2604.02544` | 2605.13706 |

The local identity column uses the canonical physical title page where present and the explicit extension admission family metadata otherwise. An associated arXiv family ID does not prove byte-equivalence with a placed proceedings PDF. Generic project/arXiv links do not resolve WebStep’s workshop/public-version numerical differences. Other unstated authors, dates, DOI claims and URLs were not globally revalidated.

## Consequential content checks

Each row below identifies a scoped assertion review. The crosswalk reviewed_assertion is an analyst-defined check or experimental interpretation, not necessarily verbatim NotebookLM wording. It does not imply that the raw cell asserts every possible overgeneralization. Classification applies to that stated check; raw_value preserves the original cell. The CSV supplies both original cells, source hashes, exact coordinates, physical pages and a short supporting excerpt. Nxx-C refers to the CSV cell and Nxx-X to the workbook cell; these paired checks are not independent studies.

| Check | Paper / physical pages | Classification | Assessment |
|---|---|---|
| N01 | [It’s a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](../../records/its_a_trap_task_redirecting_agent_persuasion_benchmark_for_web_agents_comprehensive_summary.json), pp.7 | CSV:QUALIFIED; workbook:CONTRADICTED | 735/948 and 213/948 are successful-case shares. Use the separate paired GoMail experiment for a controlled button-versus-link comparison; do not divide successful shares to estimate an unconditional causal effect. |
| N02 | [It’s a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](../../records/its_a_trap_task_redirecting_agent_persuasion_benchmark_for_web_agents_comprehensive_summary.json), pp.6,8,13,15 | QUALIFIED | Primary single-click scoring omits downstream success, but the paper reports639 cap terminations and illustrates chained continuation. This leaves a narrower recovery/semantic-topology comparison unresolved; it does not establish the first recurring prerequisite. |
| N03 | [It’s a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents](../../records/its_a_trap_task_redirecting_agent_persuasion_benchmark_for_web_agents_comprehensive_summary.json), pp.6 | QUALIFIED | Clean utility and attacked redirection concern different conditions and endpoints. They can coexist without logical inconsistency. |
| N04 | [A Whole New World: Creating a Parallel-Poisoned Web Only AI-Agents Can See](../../records/a_whole_new_world_creating_a_parallel_poisoned_web_only_ai_agents_can_see_comprehensive_summary.json), pp.5,6,7 | CSV:NOT_IN_SOURCE; workbook:QUALIFIED | The author says all cases succeeded for three listed Cursor/model configurations. Trial counts, measured detector accuracy, human/scanner detection and transmission verification are absent. Do not reconstruct n=3 trials or100% per-attempt ASR. |
| N05 | [A Whole New World: Creating a Parallel-Poisoned Web Only AI-Agents Can See](../../records/a_whole_new_world_creating_a_parallel_poisoned_web_only_ai_agents_can_see_comprehensive_summary.json), pp.6,8,9 | QUALIFIED | The source proposes randomization/sanitization/isolation but does not evaluate them. The demonstrated permission tier includes a shell/environment secret, distinct from page-only browser actions. |
| N06 | [LoopTrap: Termination Poisoning Attacks on LLM Agents](../../records/looptrap_termination_poisoning_attacks_on_llm_agents_comprehensive_summary.json), pp.1,11,16,21 | QUALIFIED | Tables4/6 report different finite aggregate metrics;25x is an author headline, not an identified independently inspected peak trace. Finite capped amplification does not prove nontermination, browser dwell, preserved correctness or verified wasted work. |
| N07 | [LoopTrap: Termination Poisoning Attacks on LLM Agents](../../records/looptrap_termination_poisoning_attacks_on_llm_agents_comprehensive_summary.json), pp.4,12 | QUALIFIED | Physicalp.12 already proposes an independent sandboxed verifier. Recursive decomposition/dependency chains are existing mechanisms onp.4. A tested semantic-versus-topology/recovery contrast could differ; the checker idea itself is not new. |
| N08 | [LoopTrap: Termination Poisoning Attacks on LLM Agents](../../records/looptrap_termination_poisoning_attacks_on_llm_agents_comprehensive_summary.json), pp.3,11,12,16,21 | QUALIFIED | Source/retained review records strict-versus-inclusive2x success, a changed-answer example, NoProfile and category/aggregate conflicts. The no-conflict label is incomplete; do not silently correct source values. |
| N09 | [Where Did It Go Wrong? Process-Level Evaluation of Web Agents with Semantic State Tracking](../../records/where_did_it_go_wrong_process_level_evaluation_of_web_agents_with_semantic_state_tracking_comprehensive_summary.json), pp.5,18 | QUALIFIED | Appendixp.18 explicitly applies SafePass to all terminal success rates, accepting an informed critical decision point without final commit. Semantic-state tracking is prior art; safe stopping/readiness and executed goal completion need separate outcomes. |
| N10 | [Where Did It Go Wrong? Process-Level Evaluation of Web Agents with Semantic State Tracking](../../records/where_did_it_go_wrong_process_level_evaluation_of_web_agents_with_semantic_state_tracking_comprehensive_summary.json), pp.3,5,8,17,18 | QUALIFIED | This is already the paper contribution. Attacked solvable tasks with independently validated non-progress/recovery remain a different proposed setting, not a global novelty conclusion. |
| N11 | [Silent Failures in Agentic Security Evaluation: A Validated Harness for Tool-Call Mediation Under Indirect Prompt Injection](../../records/silent_failures_in_agentic_security_evaluation_a_validated_harness_for_tool_call_mediation_under_indirect_prompt_injection_comprehensive_summary.json), pp.4,5 | SUPPORTED | Table I/Figure2 explicitly label D2 as ASR on 258 attack runs. D3 instead concerns FRR over 282 benign runs. This correct NotebookLM statement conflicts with an FRR mislabel in three existing corpus synthesis/report passages. |
| N12 | [Silent Failures in Agentic Security Evaluation: A Validated Harness for Tool-Call Mediation Under Indirect Prompt Injection](../../records/silent_failures_in_agentic_security_evaluation_a_validated_harness_for_tool_call_mediation_under_indirect_prompt_injection_comprehensive_summary.json), pp.3,4,5,6,7 | QUALIFIED | This is a source-reported audit of one harness and specified scenarios, not proof that all prior studies are invalid. Schema validity alone cannot establish delivered exposure, scorer validity or verified goal utility. |
| N13 | [Silent Failures in Agentic Security Evaluation: A Validated Harness for Tool-Call Mediation Under Indirect Prompt Injection](../../records/silent_failures_in_agentic_security_evaluation_a_validated_harness_for_tool_call_mediation_under_indirect_prompt_injection_comprehensive_summary.json), pp.3,5,7 | QUALIFIED | A corrected rate in static scenarios and a warning against generalizing to adaptive attacks are compatible. Actual source discrepancies include39/38 missing-payload wording and displayed10.3−6.7 versus+3.5pp. |
| N14 | [LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents](../../records/logintrap_uncovering_task_agnostic_phishing_style_indirect_prompt_injection_attacks_against_llm_based_web_agents_comprehensive_summary.json), pp.7,8,9 | QUALIFIED | Keep backbones and architectures separate. LER is login entry; ASR is sensitive-field input, not uniformly verified submission/exfiltration. PER is any success within 3tasks×3repeats, not 100% per-run success or sustained retention. |
| N15 | [LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents](../../records/logintrap_uncovering_task_agnostic_phishing_style_indirect_prompt_injection_attacks_against_llm_based_web_agents_comprehensive_summary.json), pp.7,8 | QUALIFIED | Entry and input are nested stages with different predicates. Their gap is a measured attrition mechanism, not conflicting estimates of the same event. |
| N16 | [The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory](../../records/the_compliance_trap_diagnosing_how_ai_agents_consume_conflicting_memory_comprehensive_summary.json), pp.5,6,7,22 | QUALIFIED | WebArena compliance/DPC and MemTrap divergence-conditioned metrics use different subsets. Table22 persistent-conflict realignment45–61% can coexist with 1.3% final success. Irreversibility is an interpretation, not an isolated causal proof for every failure. |
| N17 | [The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory](../../records/the_compliance_trap_diagnosing_how_ai_agents_consume_conflicting_memory_comprehensive_summary.json), pp.14,23,24 | QUALIFIED | AppendixTable 23 already crosses identifiability and groundability,32tasks/cell/model. Proposed task-relevance×recurrence differs only if its interventions/endpoints demonstrably differ. System/footer memory injection is not proof of webpage-only delivery. |
| N18 | [The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory](../../records/the_compliance_trap_diagnosing_how_ai_agents_consume_conflicting_memory_comprehensive_summary.json), pp.5,14,22,25 | QUALIFIED | Trajectory realignment and recovered state/goal are distinct constructs. Also retain actual varying validN, Gemini scope and Table29 caption/row conflicts rather than pooling recovery ranges. |
| N19 | [Honeyval: A Comprehensive Evaluation Framework for LLM-powered HTTP Honeypots](../../records/honeyval_a_comprehensive_evaluation_framework_for_llm_powered_http_honeypots_comprehensive_summary.json), pp.6,8,16 | QUALIFIED | 82.6 versus 30.6 are mean HTTP requests, not browser decisions or information yield. Baseline GeminiCLI configurations include detection above40%; FPR, model pairing, fidelity and prompts matter. Convince102.6 requests/TPR.45 is a different condition. |
| N20 | [Honeyval: A Comprehensive Evaluation Framework for LLM-powered HTTP Honeypots](../../records/honeyval_a_comprehensive_evaluation_framework_for_llm_powered_http_honeypots_comprehensive_summary.json), pp.8 | QUALIFIED | These are different objectives, so both increases are a tradeoff, not an inconsistency. CarefulPI also lowers functional fidelity. No one metric establishes overall superiority. |
| N21 | [Honeyval: A Comprehensive Evaluation Framework for LLM-powered HTTP Honeypots](../../records/honeyval_a_comprehensive_evaluation_framework_for_llm_powered_http_honeypots_comprehensive_summary.json), pp.4,5,8,12 | QUALIFIED | Resource-free decoys make exploit goals impossible; controls test real exploitability and simulated fidelity separately. Budgets are per side,50ReAct iterations/1h CLI, and cost estimates omit long-context tiers. Solvable legitimate browser recovery is distinct, while AI-agent engagement itself is prior art. |
| N22 | [Machine-Readable Ads: Accessibility and Trust Patterns for AI Web Agents interacting with Online Advertisements](../../records/machine_readable_ads_accessibility_and_trust_patterns_for_ai_web_agents_interacting_with_online_advertisements_comprehensive_summary.json), pp.1,5,6,7 | QUALIFIED | The abstract uses viewport language; TableVI gives maximum scroll-action counts3/2/5 and the page10 target is unreached. No conversion proves a universal two-viewport bound. Accessibility/choice observations are not automatically malicious ASR. |
| N23 | [Machine-Readable Ads: Accessibility and Trust Patterns for AI Web Agents interacting with Online Advertisements](../../records/machine_readable_ads_accessibility_and_trust_patterns_for_ai_web_agents_interacting_with_online_advertisements_comprehensive_summary.json), pp.6,8,9 | QUALIFIED | Supplied dummy credentials prevent real transactions. The 10/10,10/10,7/10 counts show goal-contingent synthetic subscription behavior, not a real financial-loss endpoint. |
| N24 | [WebRollback: Enhancing Web Agents with Explicit Rollback Mechanisms](../../records/webrollback_enhancing_web_agents_with_explicit_rollback_mechanisms_comprehensive_summary.json), pp.3,4,8 | QUALIFIED | Main full-success blocks improve, but partial scores and untuned smaller models have exceptions. Fewer explicit state switches does not establish fewer model calls, tokens or latency; uncertainty notation is unspecified. |
| N25 | [WebRollback: Enhancing Web Agents with Explicit Rollback Mechanisms](../../records/webrollback_enhancing_web_agents_with_explicit_rollback_mechanisms_comprehensive_summary.json), pp.2,3,5,9,10 | SUPPORTED | Actual implementation returns to recordedURLs; appendix limits destinations to saved checkpoints. The authors explicitly acknowledge irreversible payment/email limitations. Adversarial recovery remains untested. |
| N26 | [Why Do LLM-based Web Agents Fail? A Hierarchical Planning Perspective](../../records/why_do_llm_based_web_agents_fail_a_hierarchical_planning_perspective_comprehensive_summary.json), pp.3,5,7,19 | QUALIFIED | One extra replanning round improves reported outcomes, but no equal-budget continuation control or significance test is supplied. Author judge agreement is41/50 postconditions and 43/50 final judgments, not error-free ground truth. |
| N27 | [Why Do LLM-based Web Agents Fail? A Hierarchical Planning Perspective](../../records/why_do_llm_based_web_agents_fail_a_hierarchical_planning_perspective_comprehensive_summary.json), pp.5,6,7,20,21 | QUALIFIED | PDDL baseline35.6 versus 36.4, NL matched70.6 versus 79.6, Claude redundancy23.6 versus 25.6 and a model-label conflict are retained. Missing reference steps after replanning may also reflect remaining-plan versus full-plan comparison. |
| N28 | [A Framework for Studying AI Agent Behavior: Evidence from Consumer Choice Experiments](../../records/a_framework_for_studying_ai_agent_behavior_evidence_from_consumer_choice_experiments_comprehensive_summary.json), pp.3,6,7,9,16,18 | QUALIFIED | Human comparison uses Original products and another interface; matched-rating/price regimes change pair composition. Percentage-point choice shifts under nudges are not security ASR, sustained trapping, checkout or welfare loss. |
| N29 | [A Framework for Studying AI Agent Behavior: Evidence from Consumer Choice Experiments](../../records/a_framework_for_studying_ai_agent_behavior_evidence_from_consumer_choice_experiments_comprehensive_summary.json), pp.3,4,6 | QUALIFIED | Randomized nudges/attribute matching are already the methodology. No-image binary choice differs from an interactive solvable trap. A new claim must concern a distinct causal contrast/outcome. |
| N30 | [RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks](../../records/recurguard_runtime_monitoring_for_reasoning_token_consumption_attacks_comprehensive_summary.json), pp.10,11,12,13,14 | QUALIFIED | These are specified primary-model attacks with exposed reasoning/cancellation. Sonnet summary and Opus hidden-trace conditions differ; C1 retains11.9x amplification with roughly50% joint miss. |
| N31 | [RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks](../../records/recurguard_runtime_monitoring_for_reasoning_token_consumption_attacks_comprehensive_summary.json), pp.7,12,14 | QUALIFIED | Theorem2 concerns full TP evasion and explicitly does not bound the C1 partial-evasion setting. A mathematical condition is not a general trusted browser-task progress oracle. |
| N32 | [RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks](../../records/recurguard_runtime_monitoring_for_reasoning_token_consumption_attacks_comprehensive_summary.json), pp.10,12 | QUALIFIED | Detection and false positives use different populations/threshold behavior; this is a security/utility tradeoff, not an internal logical contradiction. |
| N33 | [Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents](../../records/beyond_max_tokens_stealthy_resource_amplification_via_tool_calling_chains_in_llm_agents_comprehensive_summary.json), pp.6,7,9,13,14 | QUALIFIED | 658.10x is a token ratio;561.18x uses reported energy totals whose per-query aggregation is unclear. Aggregate trajectories can exceed the 16384 per-generation cap across multiple generations. Original single-turn/single-tool stubbed tasks constrain transfer. |
| N34 | [Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents](../../records/beyond_max_tokens_stealthy_resource_amplification_via_tool_calling_chains_in_llm_agents_comprehensive_summary.json), pp.4,14 | QUALIFIED | The attack changes tool feedback during the chain and returns the original benign payload on valid termination. These are different stages, and live data correctness is not verified by deterministic placeholders. |
| N35 | [How Adversarial Environments Mislead Agentic AI?](../../records/how_adversarial_environments_mislead_agentic_ai_comprehensive_summary.json), pp.6,7,8,17 | QUALIFIED | The engagement criterion requires paper retrieval AND reference traversal. Main cohort reports8/450 engaged and 7/8 trapped; other appendix cohorts differ. Do not infer the conditional result by dividing unrelated headline rates. |
| N36 | [How Adversarial Environments Mislead Agentic AI?](../../records/how_adversarial_environments_mislead_agentic_ai_comprehensive_summary.json), pp.5,6,15,16 | QUALIFIED | The paper tests reference-graph traps, minimal-pair credibility framing and defense/utility tradeoffs. It does not settle the proposed matched task-semantics×recurrence browser experiment. Preserve source cohort/threshold conflicts. |
| N37 | [AI Agent Traps](../../records/ai_agent_traps_comprehensive_summary.json), pp.3,4,15,16 | SUPPORTED | This is a classification/agenda paper using cited evidence of uneven maturity, not six newly executed experiments or a quantitative sustained-retention benchmark. |
| N38 | [When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents](../../records/when_agents_do_not_stop_uncovering_infinite_agentic_loops_in_llm_agents_comprehensive_summary.json), pp.8,9,10 | QUALIFIED | 74 alerts,68 manually confirmed failures and 47 projects are the study counts. Impact categories are assigned to findings, not measured real-world bills. Baseline-only false negatives and pruning variability qualify coverage. |
| N39 | [Defeating Prompt Injections by Design](../../records/defeating_prompt_injections_by_design_comprehensive_summary.json), pp.5,18,24,25,33,40 | QUALIFIED | Threat-model non-goals, policy trust, approval and side channels remain. The implementation is not formally verified; utility/overhead depend on model/table, and source overhead figures conflict. This is not a matched standalone comparison. |
| N40 | [Defeating Prompt Injections by Design](../../records/defeating_prompt_injections_by_design_comprehensive_summary.json), pp.5,24,25 | QUALIFIED | A scoped guarantee and an explicitly excluded channel are compatible. Distinguish formal-model assumptions, implemented enforcement and measured outcomes. |

## Corpus-side correction identified at intake and subsequently applied

The NotebookLM D2 ASR statement is corroborated by Silent Failures physical p.5, Table I/Figure2 and the existing record’s claim_05. At intake, three existing documents incorrectly called21.7%→1.2% FRR: [comprehensive review](../../synthesis/COMPREHENSIVE_LITERATURE_REVIEW.md), line147; [thematic map](../../synthesis/THEMATIC_EVIDENCE_MAP.md), line49; [extension completion report](../../extensions/2026-10-17/LITERATURE_EXTENSION_COMPLETION_REPORT.md), line60. D2 is **ASR**, over 258 attack runs. D3 is **FRR**, over 282 benign runs,10.3%→6.7%. The structured record is correct. Those documents were left unchanged by the original reconciliation; a subsequent source-verified review corrected exactly the three labels to ASR. CORPUS-01–03 retain the original error assessment and do not assert that the error remains in current text.

This also limits the authority of earlier synthesis prose: source PDFs outrank a matching summary, a model label, a schema pass or this reconciliation.

## Classification and readback accounting

| Classification | All crosswalk entries | Interpretation |
|---|---:|---|
|SUPPORTED|714|Scoped identity/reference consistency or an explicitly corroborated assertion; not blanket scientific approval.|
|QUALIFIED|215|Partial support with material scope, endpoint, family, inference or protocol qualifications.|
|CONTRADICTED|7|Incompatible identifier join, rate definition or corpus metric label.|
|NOT_IN_SOURCE|1|The specific asserted rate/guarantee is not established by the supplied paper; not a worldwide falsehood claim.|
|VERSION_MISMATCH|31|Misattributed/placeholder bibliographic identifier relative to the bound source.|
|NOT_CHECKED|3172|Read and retained but not scientifically adjudicated.|

These totals include metadata and repeated source cells. They are not counts of validated scientific claims. The 80 targeted assertion checks comprise 72 QUALIFIED, 6 SUPPORTED, 1 CONTRADICTED and 1 NOT_IN_SOURCE results. Thirty-one identifier reviews and three corpus corrections are separate.

## Research implications and review boundary

See [gap assessment](NOTEBOOKLM_GAP_ASSESSMENT.md) for established mechanisms, narrower unresolved gaps, candidate missing literature and ten proposed Protocol V1.1 amendments. Prior art already covers navigation traps, task-compatible prerequisites, continuation poisoning, semantic process tracking, factorial diagnosis, rollback and harness audits. No first-trap, first-progress-oracle or first-factorial claim is supported. The specific solvable page-only semantic×recurrence/recovery comparison remains a proposal whose novelty and feasibility require human methods review.

## Preservation report

All 616 pre-existing Git-visible files in the intake baseline were rehashed before writing the deliverables and matched. This scope includes all 123 canonical PDFs,246 existing summaries/records, five exact archives, active synthesis/catalog/progress artifacts, historical tracked guidance and the raw inputs. Ignored runtime caches, quarantines and external backups were not comprehensively rehashed.

HEAD remains `0b917043b94539932d25d5f1d3afd63e814cde02`. Frozen tag object remains `dbe3e84f53e3ff4e25e23c5396e1432e068d2555` and target `0b917043b94539932d25d5f1d3afd63e814cde02`. The existing14-file uncommitted extension work and other pre-existing files were preserved. No summaries/JSON were regenerated, no experiment or agent/model run occurred, and nothing was staged, committed, pushed or published.

Only the three requested deliverables are authorized new repository files. Final validation below records the after-write readback. Stop for scientific review; proposed protocol clauses have not been applied.

## Executed final readback

Validated at 2026-10-18T20:18:15.376160+00:00. Readback confirmed 4,140 uniquely identified crosswalk entries and 80 targeted assertion rows (72 QUALIFIED, 6 SUPPORTED, 1 CONTRADICTED, 1 NOT_IN_SOURCE). The preceding validation confirmed all 3,660 retained source-cell values against the parsed inputs, the 80 assertion evidence excerpts against cited PDF text, and referenced record claim IDs. Those values and excerpts were unchanged by the final classification edits. The 3,172 NOT_CHECKED entries retain their uncertainty. All 153 local Markdown file links resolve; the roadmap external-reference heading is present.

All 616 pre-existing baseline files, including both raw inputs, retain their intake SHA-256 hashes. The Git-visible file-set difference is exactly the three requested outputs. HEAD and the frozen tag object are unchanged; the staging area is empty. These checks establish preservation within the stated baseline scope, not scientific approval of unchecked cells.

Stop for scientific review.
