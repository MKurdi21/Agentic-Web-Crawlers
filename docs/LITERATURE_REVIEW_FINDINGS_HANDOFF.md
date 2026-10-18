# Topic Search — Literature Review Findings and Research Direction

**Evidence-synthesis handoff (2026-10-18).** This is a current research interpretation of the completed Topic Search literature work, not a newly conducted experiment, a claim of global novelty or a replacement for the underlying paper records. This repository handoff condenses the existing synthesis for review; it does not replace the detailed evidence map or roadmap. The 00/01/02 continuity files are intended for separate manual ChatGPT Project replacement; their existing tracked repository copies are unchanged by this integration.

**Frozen research foundation commit:** `0b917043b94539932d25d5f1d3afd63e814cde02`. **Existing annotated tag:** `research-foundation-2026-10-17-v1` (object `dbe3e84f53e3ff4e25e23c5396e1432e068d2555`). The 123-paper extension is maintained on `research/literature-extension-2026-10-17`; actual Git HEAD and the local completion receipt identify its committed state. The frozen tag is unchanged. **Proposed experiment:** not implemented. The 11-paper extension was processed 2026-10-17–18, retaining selected source versions rather than claiming an exhaustive current search.

## Executive conclusion

Our completed literature survey supports that autonomous LLM-based web agents operate across different trust boundaries from standalone answer-only LLMs: they encounter untrusted site content during navigation, may invoke actions on behalf of users, and can retain working or persistent state. Adversarial pages and tool output can redirect observed behavior; repeated interaction, resource expenditure and downstream side effects are distinct risks. **It does not follow that the same model is universally more susceptible to injection given the same malicious content and controlled context.** The 123-record corpus contains no otherwise-matched study that settles that universal claim, though this is not a proof that no such work exists elsewhere.

The project's primary problem is therefore **not** the broad claim that web agents are inherently more vulnerable. Our target is a **crawler-trap analogue for goal-directed web agents**: a hostile but controlled web environment that draws an agent into repeated, task-relevant actions that produce little or no verifiable progress, while the legitimate goal and an exit remain available.

The leading **untested** mechanism is a *task-dependent recurring-prerequisite trap*. For example, a synthetic document service could repeatedly request apparently necessary verification before showing a requested item, while a legitimate path remains reachable. This is an illustration of a study design, not an attack demonstrated by this project.

## 1. Corpus and strength of evidence

- The authoritative completed corpus contains **123 canonical PDFs**, **123 comprehensive Markdown summaries** and **123 typed JSON records**, plus **five exact duplicate PDF archives**. It has no ordinary Research Mode papers left pending, failed, excluded or deferred.
- The preserved original 112 report **1,668 structured claims**; the 11 additions report **151**, for **1,819 total**. Each addition has source identity/structure/schema/page/quotation checks, analyst review and an acceptance receipt. The existing **16 tests** passed after a minimal inventory-count compatibility repair; completion and commit state are distinct and are recorded by Git and the documentation audit. These recorded checks establish *traceability and byte preservation within their checked scope*—not independent scientific replication or verification of every causal claim.
- The 123 records are **not 123 independent experimental units**. Studies with related versions, including AgentVigil/AgentFuzzer and versions of *Mind the Web*, must not be used to inflate independent support.
- Evidence includes primary empirical studies, benchmarks, reviews, conceptual work and benign-capability studies. Those categories answer different questions. Only evidence that actually manipulates an adversary or security endpoint supports an attack-effect claim.
- Empirical outcomes often have different denominators and endpoint definitions. Initial content ingestion, next-action deviation, click, proposed tool call, verified side effect, attack budget exhaustion, crash, long-horizon noncompletion, and resource amplification must be reported separately. Avoid a pooled, context-free "attack success rate".

Source locations: [research catalog](../research/catalog.md), [full literature review](../research/synthesis/COMPREHENSIVE_LITERATURE_REVIEW.md), [evidence map](../research/synthesis/THEMATIC_EVIDENCE_MAP.md), [comparison matrix](../research/synthesis/SECURITY_COMPARISON_MATRIX.md), [initial findings](../research/synthesis/INITIAL_RESEARCH_FINDINGS.md), [Research Mode handoff](RESEARCH_MODE_HANDOFF.md).

## 2. Core security findings

### 2.1 Three quantities must not be confused

**Exposure:** whether malicious material reaches the agent's observation during a task. Web browsing, external search, tool results, screenshots/accessibility views and memory retrieval alter encounter opportunities.

**Susceptibility conditional on exposure:** whether the same model, under a controlled decision interface, elevates an untrusted instruction over its legitimate task constraints. A navigation-capable system is not thereby proven intrinsically easier to manipulate at the model level.

**Consequences after manipulation:** whether a proposed deviation becomes an accepted browser/tool action or a verified effect, how much unproductive work occurs, and whether the original task can still be completed. Tools, authorization policies, state and task duration affect this layer.

This decomposition is critical to both the earlier standalone-versus-agent research proposal and the new trap-focused roadmap. The former is a **retained secondary study**; the latter measures repeated closed-loop behavior and requires an interactive victim agent.

### 2.2 Adversarial information can cross authority boundaries

An adversarial page may falsely claim that completing a new subtask is required by the user’s objective. That is different from a trusted user asking the agent to follow a verification workflow. Report whether attacker control is limited to a comment, a whole page/site, a tool-result body, a tool definition, or direct internal memory modification. Stronger attacker tiers must not be silently combined with page-only attacks.

Perception also matters. DOM text, accessibility trees, screenshots and multimodal summaries expose different attack surfaces. Agent memory can preserve or retrieve misleading content beyond its original presentation. These findings support threat-model selection, but do not prove that every trap variant works.

### 2.3 Resource and availability failures require context

Published studies describe tool loops, prolonged reasoning, misleading chains, and expenditure of tokens, requests and time. However, **benign** long tasks can also contain necessary retries or repeated visits. A count of URLs, elapsed time or tokens alone cannot establish malicious retention. A site must be shown to induce *excess* non-progress relative to appropriate controls.

A capped execution cannot establish a literally infinite loop. Premature safe stop may reduce exposure yet sacrifice legitimate task completion. A useful defense must be evaluated against both adversarial workflows and legitimately iterative work.

### 2.4 Security boundaries and defenses have different assumptions

Input hardening, guards and detectors, task-alignment checks, plan-consistency checks, tool-access policy, sandboxing and information-flow controls protect different stages. Detection accuracy is not equivalent to preventing an executed action. Formally motivated defenses are conditional on correct labels, trusted policy, actual enforcement and permitted utility. Model-level compliance, executor control, false refusal, latency and benign-task success should be tracked independently.

A defense that avoids the trap by refusing all work is a negative control, not an adequate browser agent.

## 3. Closest prior art: distinction and novelty limits

| Work | Demonstrated or documented scope | Relevance and limitation for our hypothesis |
|---|---|---|
| [Classical crawler traps](../research/records/detection_of_crawler_traps_formalization_and_implementation_defeating_protection_on_internet_and_on_the_tor_network_comprehensive_summary.json) / [IRLbot](../research/records/irlbot_scaling_to_6_billion_pagesand_beyond_comprehensive_summary.json) | Crawl/link structure, dynamic URLs, repeated traversal and scheduling. | Topology-only comparison; conventional crawlers lack the same natural-language legitimate task. |
| [Cloudflare AI Labyrinth](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/) | Product documentation for linked decoy material offered to noncompliant AI crawlers. | A real deployed crawler trap, but not a controlled browser-agent semantic-retention study. |
| [POTEMKIN / *How Adversarial Environments Mislead Agentic AI?*](https://arxiv.org/abs/2604.18874) | Adversarial tool-output environments; *The Maze* uses fabricated reference networks, cycles and dead ends. | Already demonstrates navigational trap mechanisms in agents; changing the interface to webpages alone is a weak novelty argument. |
| [*It's a TRAP!* (ICML 2026)](https://proceedings.mlr.press/v306/korgul26a.html) | Persuasive web-page injections and task redirection on realistic tasks. The local record reports **948 redirections / 3,780 attacked runs (about 25%)** across six models; **639 step-cap terminations** are separate. | Task-related persuasion is prior art. Initial redirection alone is not prolonged retention/recovery; Figure 15 also illustrates chained continuation. Results are protocol-specific. |
| [Honeyval](https://arxiv.org/abs/2605.29963) | LLM-backed HTTP honeypots evaluated against AI hacking agents; reports interaction-length and detection/cost tradeoffs. | Agent engagement/retention is not a new idea. Legitimate-user browser goal progress and recoverability are a more focused distinction. |
| [LoginTrap](https://arxiv.org/abs/2608.04741) | Webpage context makes login appear a plausible prerequisite to task continuation. | Deceptive task prerequisites are already demonstrated; a repeated-prerequisite mechanism by itself is insufficient novelty. |
| [WebStep](https://arxiv.org/abs/2606.15673v2) | Canonical placed workshop process-evaluation version; public numerical examples differ and Appendix SafePass can precede final commitment. | Ground-truth process/progress measurement is an existing methodological technique, to be adapted rather than claimed as invented. |

POTEMKIN, TRAP, Honeyval, LoginTrap and the placed WebStep version are canonical records; Cloudflare remains supplemental. LoopTrap now supplies recursive verification/circular-dependency and continuation-poisoning precedent (pp.3–4/19–21), and Compliance Trap supplies memory-consumption schedules and a 2×2 identifiability/groundability design (pp.4–9/23). No broad prerequisite, factorial or progress-oracle novelty is supported. The [evidence bridge](../research/synthesis/TRAP_EXPERIMENT_LITERATURE_EVIDENCE_BRIDGE.md) and [extension report](../research/extensions/2026-10-17/LITERATURE_EXTENSION_COMPLETION_REPORT.md) cover all 11 additions, exact versions, discrepancies and proposed Protocol V1.1 clauses. The [focused comparison](../research/synthesis/THEMATIC_EVIDENCE_MAP.md#focused-trap-comparison) retains supplemental competitors.

Unresolved POTEMKIN thresholds/cohorts, TRAP location aggregates, AgentLAB aggregates, Task Shield utility and SafeArena normalization remain explicit in the [source-discrepancy register](../research/synthesis/THEMATIC_EVIDENCE_MAP.md#10-unresolved-discrepancies-and-alternative-readings). No replacement aggregate or reconciliation is inferred.

These sources are a mix of original scholarly papers and official product documentation. Their authors' reported numbers and mechanisms are **not** results independently reproduced by Topic Search. Novelty must be verified by comparing experimental interventions, outcome oracles, controlled variables and available artifacts—not by comparing names or abstracts.

## 4. Current research gap and hypotheses

**Working question:** *Under a page-only adversary with public task context, does task-relevant framing of a recurring prerequisite produce additional non-progress interaction, and change escape or recovery, relative to equivalent neutral framing on the same solvable website?*

**Proposed contribution (unproven):** isolate the **interaction of task relevance and recurrence**, observe both **entry and continued retention**, independently verify whether legitimate progress occurs, and test whether a **progress-aware escape intervention** reduces excess work without degrading utility. None of these component ideas is individually claimed to be new. Competitors may already cover parts of the combination.

| | Finite prerequisite workflow | Recurring prerequisite workflow |
|---|---|---|
| Neutral framing | Benign structure/wording reference | Topology-control recurrence |
| Task-relevant framing | Task-semantics control without recurrence | Candidate semantic recurrence trap |

- **H1 (primary):** the task-relevant recurring condition produces more bounded decoy-directed choices without a newly verified legitimate subgoal than the neutral recurring condition.
- **H2 (supporting interaction):** the task-relevance effect is larger when prerequisites recur than in finite workflows.
- **H3 (later exploratory defense):** progress-aware retry or escape rules can reduce excess non-progress work while preserving performance on truly iterative legitimate tasks.

The website graph, visible exits, real goal, authorized task facts, approximate text volume, link placement, delays, budgets, agent model/scaffold and observation interface should be matched as far as feasible. Finite-versus-recurring transition changes must be explicit. Use independent page/server state to assess *actual* task progress—not the attacker's displayed "step completed" message.

## 5. Threat model and observable outcomes

The **primary attacker** controls a designated synthetic local site's page contents and bounded session transitions, using only public task category/object information. It does **not** control the legitimate user instruction, browser tool schema, internal model state, evaluator goal predicate, operating system or external destinations. Cross-session memory, adaptive generation, full private-task knowledge and direct tool-result control remain separate, labeled extensions.

The primary evaluator should distinguish:

- **Opportunity/exposure:** the target content actually reaches the agent, versus merely being served.
- **Behavioral entry:** the agent chooses a decoy-directed first step.
- **Bounded non-progress burden (primary):** number of decoy-directed actions producing no verified new legitimate subgoal across *all assigned episodes*.
- **Retention:** decoy-directed actions/time after entry, with termination by recovery/exit/crash/cap reported separately. Conditional entrant analysis is descriptive unless entry is randomized.
- **Escape vs recovery:** leaving or safely stopping is not completing the original user task; verify both.
- **Utility and resources:** legitimate goal completion on clean/finite tasks, false stop, requests, model calls, tokens, elapsed time and cap hits.
- **Stages of any side effect:** proposed action, executed action, server-verified effect; none is required for the primary navigation-trap pilot.

Repeat samples are clustered within task/site families. Proposed pilot counts are feasibility planning, not independent scientific replications or meaningful sample-size guarantees. Report denominators with raw counts, uncertainty and per-template outcomes; do not drop hard tasks after seeing attack outcomes. If the task-relevance effect is null when topology is controlled, the semantic-trapping hypothesis is not supported in that setting.

## 6. What the literature does not establish

The completed evidence base does **not** establish any of the following as a proven result of Topic Search:

- A universal intrinsic susceptibility advantage/disadvantage of web agents relative to standalone LLMs.
- A universal numerical vulnerability multiplier or defensible pooled cross-study ASR.
- That persistent memory, multimodality or full agent autonomy necessarily increases every attack's effectiveness.
- That the proposed recurring-prerequisite trap is original, deployable or effective.
- That source fingerprints, quote matching, model agreement, or a clean Git checkout independently validates scientific conclusions.
- That123 canonical records correspond to 123 independently replicated studies.
- That a site showing repeated status messages caused the agent's internal reasoning state (rather than simply producing correlated observed actions).

## 7. Status, next bounded tasks and publication boundary

**Done:** 123 admitted canonical sources with 123 accepted summary/record pairs; 151 new typed claims;198 source-bound18-dimension extraction entries; integrated thematic synthesis and an experiment evidence bridge. The original 112 sources, outputs, evidence and historical state are preserved within the executed readback scope. The existing frozen tag remains unchanged. Current output acceptance is literature use with reported limitations, not independent scientific replication.

**Not done:**independent human scientific validation; exhaustive visual inspection of every page; global novelty verification; raw-artifact reproduction; previously outstanding mathematical presentation/privacy/license/backup review; agent-trap implementation, fixture, experiment, pilot or separate experimental repository.

**Next bounded tasks:**review the proposed contribution and Protocol V1.1 clauses against the [evidence bridge](../research/synthesis/TRAP_EXPERIMENT_LITERATURE_EVIDENCE_BRIDGE.md), obtain human assessment, and separately authorize any experiment implementation. Local documentation synchronization and three commits were separately authorized; their completion is established by Git and the external completion receipt. This does not authorize publication, new tags or experiments. No tag creation or movement is needed. The 00/01/02 manual Project replacement and mathematical rendering review remain separate; their tracked source bytes were preserved.

### Preservation and privacy qualifications

The following foundation-era archival/privacy qualifications are retained as dated context. This extension did not re-audit off-workspace archives, auxiliary refs, remote visibility or independent backups.

All 794 formerly tracked historical engineering paths remain available via previous Git history and verified external quarantine/archive maps; 3,627 formerly untracked retired paths were quarantined. The 23 engineering archives are verified selected slices, **not complete historical execution closures**. The 202 exact-path ignored historical files still physically exist and must not be represented as deleted or committed. Most have byte-exact or LF-normalized historical equivalents reachable through local auxiliary Git refs, which is a **distribution privacy risk**. Two already-tracked private-review paths also remain unchanged and require separate distribution review. The 2,786 paper-generation evidence files remain intact but are not all included in the 548-file committed tree; two earlier exact research-runner/test versions remain unrecovered. Current archive/backup/quarantine copies share one Google Drive failure domain and are not independent disaster-recovery backups. A local remote-tracking reflog also records an earlier “update by push” to the foundation commit; this is not privacy clearance or proof of current remote visibility. No network publication action is part of this integration. None of these limitations is removed by creating a Git tag.

### Document authority and update rules

For a factual or numerical claim, refer to the underlying canonical PDF, corresponding `research/records/*.json` source-located claims, and the original summary. Do not quote a report's high-level inference as a substitute for the reported protocol. The user explicitly authorized this11-paper expansion of the 112-paper foundation to 123 records. Future discoveries remain supplemental until separately admitted under an authorized extension. Preserve original historical reports and their dated states; update current entry documents through reviewed commits only.

**Authoritative directions:** [trap roadmap](../research/synthesis/AI_WEB_AGENT_TRAP_RESEARCH_ROADMAP.md), [literature review](../research/synthesis/COMPREHENSIVE_LITERATURE_REVIEW.md), [evidence map](../research/synthesis/THEMATIC_EVIDENCE_MAP.md), [research gaps](../research/synthesis/RESEARCH_GAPS_AND_HYPOTHESES.md) (current H1–H3 and retained secondary comparison framing), [controlled comparison design](../research/synthesis/CONTROLLED_COMPARISON_STUDY_DESIGN.md) (secondary), [foundation handoff](RESEARCH_FOUNDATION_HANDOFF.md), [Research Mode handoff](RESEARCH_MODE_HANDOFF.md).

## NotebookLM reconciliation and current documentation

The [reconciliation](../research/supplemental/notebooklm/NOTEBOOKLM_RECONCILIATION.md) binds both unchanged raw exports to the existing corpus: 123 workbook, 121 CSV and 122 reference-sheet identity matches; 4,140 entries; 80 targeted assertion checks; 31 problematic identifiers; 3,172 NOT_CHECKED entries. These are different evidence classes, not thousands of independently validated findings. The [gap assessment](../research/supplemental/notebooklm/NOTEBOOKLM_GAP_ASSESSMENT.md) narrows possible contribution claims and retains the ten-clause amendment table as a proposal. No Protocol V1.2 exists or is approved. Source-supported endpoint and version qualifications are integrated into the review, evidence map and roadmap; detailed unchecked cells stay supplemental. The [documentation audit](DOCUMENTATION_SYNCHRONIZATION_AUDIT.md) records current versus historical guidance and remaining manual Project updates.
