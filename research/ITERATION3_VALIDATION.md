# Iteration 3 validation and continuation report

**Operationally paused:** nine of ten selected papers completed. Task Shield
hit `OPERATIONAL_USAGE_LIMIT`; no further model dispatch occurred.

| Measure | Observed |
|---|---|
| Initial completed | 15 |
| Newly completed | 9 |
| Total completed / catalog records | 24 |
| Remaining eligible pending | 81 |
| Excluded holdouts | 7: B02–B08 |
| Failed | 0 |
| Selected deferred | 1: Task Shield, operational usage limit |
| Canonical / archived duplicates | 112 / 5 |

## New deliverables

Each linked pair exists and passes the existing checks. The original fifteen
summary/record pairs are byte-identical to the starting snapshot.

| Paper | Markdown summary | Structured record | Claim groups |
|---|---|---|---|
| AdvAgent: Controllable Blackbox Red-teaming on Web Agents | [Summary](summaries/advagent_controllable_blackbox_red_teaming_on_web_agents_comprehensive_summary.md) | [Record](records/advagent_controllable_blackbox_red_teaming_on_web_agents_comprehensive_summary.json) | 15 |
| Attacking Vision-Language Computer Agents via Pop-ups | [Summary](summaries/attacking_vision_language_computer_agents_via_pop_ups_comprehensive_summary.md) | [Record](records/attacking_vision_language_computer_agents_via_pop_ups_comprehensive_summary.json) | 15 |
| EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage | [Summary](summaries/eia_environmental_injection_attack_on_generalist_web_agents_for_privacy_leakage_comprehensive_summary.md) | [Record](records/eia_environmental_injection_attack_on_generalist_web_agents_for_privacy_leakage_comprehensive_summary.json) | 14 |
| AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents | [Summary](summaries/agentdojo_a_dynamic_environment_to_evaluate_prompt_injection_attacks_and_defenses_for_llm_agents_comprehensive_summary.md) | [Record](records/agentdojo_a_dynamic_environment_to_evaluate_prompt_injection_attacks_and_defenses_for_llm_agents_comprehensive_summary.json) | 16 |
| SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents | [Summary](summaries/securewebarena_a_holistic_security_evaluation_benchmark_for_lvlm_based_web_agents_comprehensive_summary.md) | [Record](records/securewebarena_a_holistic_security_evaluation_benchmark_for_lvlm_based_web_agents_comprehensive_summary.json) | 12 |
| WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks | [Summary](summaries/wasp_comprehensive_summary.md) | [Record](records/wasp_comprehensive_summary.json) | 16 |
| CELLMATE: Sandboxing Browser AI Agents | [Summary](summaries/cellmate_sandboxing_browser_ai_agents_comprehensive_summary.md) | [Record](records/cellmate_sandboxing_browser_ai_agents_comprehensive_summary.json) | 15 |
| Defending Against Indirect Prompt Injection Attacks With Spotlighting | [Summary](summaries/defending_against_indirect_prompt_injection_attacks_with_spotlighting_comprehensive_summary.md) | [Record](records/defending_against_indirect_prompt_injection_attacks_with_spotlighting_comprehensive_summary.json) | 15 |
| IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic Systems | [Summary](summaries/isolategpt_an_execution_isolation_architecture_for_llm_based_agentic_systems_comprehensive_summary.md) | [Record](records/isolategpt_an_execution_isolation_architecture_for_llm_based_agentic_systems_comprehensive_summary.json) | 14 |

## Validation

All 24 completed records were rechecked with the existing JSON schema, required
ordered headings, source identity, physical page bounds and exact source quotations.
Markdown equals the record narrative and progress fingerprints match each source,
summary and record. Catalog membership equals the 24 validated completed identities.
New papers contain 132 supported claim groups; all completed papers contain 366.

Selected important quantitative claims and figures/tables were checked against
extracted source evidence and selected rendered pages. Publication identity and
authors were checked in each new paper’s first-page evidence. Review notes distinguish
author claims, demonstrations, analyst inference and untested hypotheses. This is
lightweight selected-evidence review, not exhaustive entailment checking, replication
or independent human scientific validation.

Executed tests: 10 Research Mode tests and 4 summary-state tests passed. No code,
schema, runner or architecture change was made. Retained model responses needing
heading or exact-quote corrections have their original response and correction notes
in ignored evidence. Successful retries reused those responses, without new model calls.

Preservation: all 30 previous deliverable fingerprints and all 12 protected-file
fingerprints are unchanged. All 105 eligible PDF hashes match inventory and the
existing checkpoint. Reserved B02–B08 PDFs were not opened; historical experimental
artifacts/checkpoints were not regenerated or revised. B02 remains consumed/incomplete
with primary accepted and verifier/adjudication NOT_RUN; B03–B08 remain untouched.

## Scientific extraction concerns

- EIA: reported MI variance and aggregation wording conflict with displayed values;
  action-step leakage and next-step continuity do not establish whole-task integrity.
- Pop-ups: headline aggregation and defense-relative-percentage wording are unresolved;
  malicious clicks are suppressed, so actual redirect/download harm is not measured.
- AgentDojo: tool counts, no-defense baselines, attack union and tool-filter rates conflict
  across source tables/prose; each reported protocol remains separate.
- SecureWebArena: GUI AdInject prose uses pop-up table values; live-test allocation and
  some stage/outcome prose remain ambiguous. Model-category differences are observational.
- WASP: per-environment scenario wording and o1 developer template aggregation disagree;
  intermediate judge diversion and final-state attacker goals use different endpoints.
- Spotlighting: 3.10% versus below-3% prose conflict; keyword attacks and model-dependent
  encoding utility do not establish browser containment or adaptive robustness.
- IsolateGPT: permission appearances and warning rates are not attack-success rates;
  case-study defense depends on users refusing warned requests.
- ceLLMate: zero-domain denominator and one latency percentage conflict. Blocking twelve
  scripted forbidden goals is enforcement emulation; permitted-action misuse is excluded.

No incompatible ASRs are pooled or ranked. These records do not establish a matched
general vulnerability ordering between browser agents and standalone tool-free LLMs.

## Synthesis

[Security comparison matrix](synthesis/SECURITY_COMPARISON_MATRIX.md): 24 papers,
12 requested columns, source-backed record references and physical-page scopes.
[Initial research findings](synthesis/INITIAL_RESEARCH_FINDINGS.md): seven requested
topics, preliminary and source-grounded. All 67 synthesis links resolve; matrix
record coverage matches the catalog. Task Shield contributes no unvalidated findings.

## Deferred paper and resume

Task Shield has retained extraction and a generation log, but no model response,
Markdown deliverable or structured record. Progress remains pending with
`operational_interruption: OPERATIONAL_USAGE_LIMIT`. Provider text said try again
at 1:47 PM; its timezone and actual restored capacity were not established.

Once capacity is available, finish the selected paper with the existing runner:

```powershell
research/.venv/Scripts/python.exe -B scripts/research_mode.py --limit 2 --paper the_task_shield_enforcing_task_alignment_to_defend_against_indirect_prompt_injection_in_llm_agents_comprehensive_summary.md
```

This targets the one remaining selected paper and skips completed outputs. After
it validates, the expected state is 25 completed / 80 pending / 7 excluded; that
state has not been observed in this iteration. General subsequent processing:

```powershell
research/.venv/Scripts/python.exe -B scripts/research_mode.py --limit 2
```

Run one invocation at a time. Stop dispatch again if a usage limit recurs.

Evidence: [validation JSON](iteration3_validation.json),
[source review notes](ITERATION3_REVIEW.md), [selection](iteration3_selection.json),
[catalog](catalog.md), [progress](progress.json),
[handoff](../docs/RESEARCH_MODE_HANDOFF.md).

## Completion addendum — 2026-10-10

The paused report above is a historical snapshot. Task Shield has now completed
through the existing targeted runner. **Current state: 25 completed, 80 eligible
pending, 7 excluded (B02–B08), 0 failed, 0 deferred.** Iteration 3 is complete:
15 starting papers + all 10 selected additions. This resume added one paper.
Inventory remains 112 canonical papers / five archived duplicates.

- [Task Shield comprehensive summary](summaries/the_task_shield_enforcing_task_alignment_to_defend_against_indirect_prompt_injection_in_llm_agents_comprehensive_summary.md)
- [Task Shield structured record](records/the_task_shield_enforcing_task_alignment_to_defend_against_indirect_prompt_injection_in_llm_agents_comprehensive_summary.json)
- [Completion validation JSON](iteration3_completion_validation.json)
- [Updated 25-paper security matrix](synthesis/SECURITY_COMPARISON_MATRIX.md)
- [Updated preliminary findings](synthesis/INITIAL_RESEARCH_FINDINGS.md)

All 25 output pairs passed the existing ordered-section, minimum-depth, schema,
source-identity, physical-page and exact-support-quotation checks, plus
Markdown/JSON and progress-fingerprint readback. Task Shield contains 12 claim
groups and 14 supporting quotations; all seven numbered figures, seven numbered
tables, major definitions/equations and Algorithm 1 are represented. Selected
architecture/main-result/ablation/capacity/latency evidence was checked against
extracted source text and reviewer-rendered pages 5, 8 and 14. Source identity is
ACL 2025, Volume 1 Long Papers, printed pages 29680–29697 (physical pages 1–18),
by Feiran Jia, Tong Wu, Xin Qin and Anna Squicciarini. Source SHA-256:
`057ff02152c0bb61892b08abdc80f7af22416c03819e526878091ee87d3bf1e6`.

The generation succeeded on one targeted attempt. Its initial validation failed
because one quotation omitted a line-break hyphenation. The original response
and correction notes are retained; the correction was validated through
`--retry-failed --paper` using retained output, with no additional model call.
The earlier usage-limit log is retained separately. No additional papers were
processed. The temporary validation failure has been resolved; no failed paper
remains in current progress.

All 48 prior output fingerprints and 12 protected-input fingerprints remain
unchanged. All 105 eligible source hashes match the historical checkpoint.
No reserved PDF was opened; B02 consumption and B03–B08 exclusion remain
unchanged. No code, schema, architecture or historical checkpoint was changed.
The paused `iteration3_validation.json` remains intact. The catalog contains 25
validated identities; the matrix has 25 rows/12 columns and all 76 synthesis local links
resolve. Total claim groups: 378; Iteration 3 additions: 144.
The existing tests were rerun: 10 Research Mode and 4 summary-state tests passed.

Important concerns remain explicit: exact attack/task denominators and security
uncertainty are not supplied; one trial per task, GPT-family models and synthetic
AgentDojo conversations limit generalization. GPT-4o Slack utility differs between
Table 2a (64.76%) and Table 4 (50.48%); the restatement prose uses Input Shield's
63.80% rather than full Task Shield's 50.48% as a comparator. Defender-capacity
trends and prompt/threshold ambiguities remain flagged in the narrative. No
measured adaptive campaign or matched standalone-LLM comparison is claimed.
Full-shield latency is substantial. No replication, independent human scientific
validation or exhaustive entailment review was performed. Cross-paper metrics
are not pooled or ranked.

Processing stops at this milestone. When separately continuing the corpus,
run one invocation at a time from the repository root:

```powershell
research/.venv/Scripts/python.exe -B scripts/research_mode.py --limit 2
```
