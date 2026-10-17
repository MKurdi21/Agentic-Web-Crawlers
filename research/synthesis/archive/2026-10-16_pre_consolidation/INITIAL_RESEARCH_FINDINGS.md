# Initial research findings

Preliminary synthesis from112 validated canonical Research Mode records:
93 prior completions plus19 final19-continuation additions.
All112 canonical output pairs are complete;0 pending,0 excluded,0 failed.
This is not a final literature review, a novelty claim, or independent human
scientific validation. The matrix separates measured attacks, author risks,
analyst-inferred surfaces and hypotheses. Citations identify physical PDF pages
and source-backed record claim IDs; linked artifacts outside supplied papers
were not treated as inspected evidence.

## 1. Interaction with external environments

The architectural papers support a recurring observation–decision–action loop.
ReAct adds thoughts to context between environment actions; AutoWebGLM combines
page representation, task, location and history; BrowserGym exposes an
observation/action/reward interface through Chromium and Playwright. These are
architectural descriptions, not evidence of adversarial compromise.
[ReAct, react_c01, pp.3–4](../records/react_comprehensive_summary.json),
[AutoWebGLM, autowebglm_c02, pp.3–4](../records/autowebglm_comprehensive_summary.json),
[BrowserGym, BG-C02, p.5](../records/browsergym_comprehensive_summary.json).

Interfaces vary materially. SeeAct first generates screenshot-based intentions
and then grounds them into elements. Mind2Web evaluates independent steps on
cached pages using ground-truth histories. MMINA uses ordered multihop completion.
These settings cannot be treated as interchangeable free-running agents.
[SeeAct, seeact_c01/c03, pp.3–4](../records/seeact_comprehensive_summary.json),
[Mind2Web, mind2web_c04/c08, pp.7,10](../records/mind2web_comprehensive_summary.json),
[MMINA, mmina_c02/c03, p.3](../records/mmina_comprehensive_summary.json).

Iteration 4 adds two different external-information interfaces. VisualWebArena
uses screenshots/accessibility trees/captions and SoM IDs to connect observations
to browser actions. Its 16.37% GPT-4V SoM result on 910 tasks is legitimate task
success, not ASR; the 88.70% human result uses a separate 230-task sample. Its
later GPT-4o SoM result is 19.78%, a distinct model/evaluation addition.
WebGPT instead exposes a restricted text browser with search, existing-link
navigation and quotation collection, trained with demonstrations and human
preferences. Its hypothetical Wikipedia-editing concern is not an observed
exploit and is excluded by the implemented action set. **Analyst inference:**
these architectures differ in both observation exposure and possible action
consequences; browser integration alone does not imply unrestricted write access.
[VisualWebArena, vwa_c01–08/10–13, pp.1,3–9,13,15–17](../records/visualwebarena_comprehensive_summary.json),
[WebGPT, webgpt_c01/06–11/14, pp.1–11,17–18](../records/webgpt_comprehensive_summary.json).

WebLINX adds multi-turn user dialogue to DOM/screenshot grounding and structured actions; its static demonstrations assess next-action similarity, not completed task outcomes. WebWalker adds an explorer–critic loop, accumulating page information in critic memory and optionally appending that memory to RAG evidence. These define candidate information/action/state boundaries, but neither paper tests attacker control or defenses. [WebLINX record](../records/weblinx_comprehensive_summary.json), weblinx_c01–14; pp.1–9,27–32. [WebWalker record](../records/webwalker_comprehensive_summary.json), ww_c01–15; pp.3–9,13–16.

Go-Browse adds structured exploration and model-judged successful trajectories for training. Its webpage-observation and action-execution boundaries are relevant architectural evidence; the paper tests task solving rather than adversarial susceptibility. Its bounded feasibility attempts and training-data selection should not be read as proof that failed tasks are impossible or as a security evaluation. [Go-Browse](../records/go_browse_comprehensive_summary.json), GB-C02, GB-C12–GB-C13, physical pp.3–6,15 and full-paper negative finding.

## 2. Entry of untrusted information

Potential inputs include retrieved pages, HTML/DOM-derived descriptions,
screenshots, tool results, downloaded document text, email and persistent memory.
The indirect-injection study demonstrates that a third party can place commands
in inference-time data without directly participating in the victim conversation.
Its synthetic memory demonstration stores an injection and reintroduces it when
memory is later read. The general architectural pathway is analyst inference;
the selected injection behaviors are demonstrations with stated environments.
[Indirect Prompt Injection, C01/C02/C08/C09, pp.2–3,7](../records/indirect_prompt_injection_real_world_comprehensive_summary.json).

WebVoyager can parse downloaded PDFs into observations. That expands described
input routes, but its paper does not test an attack through that route. A webpage
or file becoming model input is not by itself proof that attacker instructions
will override the legitimate goal.
[WebVoyager, WV-C12/C13, pp.3–13](../records/webvoyager_comprehensive_summary.json).

## 3. Conversion of outputs into actions

Model-selected elements, operations and values become browser events; some
interfaces accept raw executable Python, while others map model output onto
restricted action primitives. BrowserGym explicitly discusses arbitrary
untrusted-code risks. LASER's state-permitted functions constrain the available
interface, but its study does not test an authorization guarantee. Thus
restricting an action vocabulary should not be equated with validating whether
a particular action serves the authorized user's goal.
[BrowserGym, BG-C03/C04, pp.7–8](../records/browsergym_comprehensive_summary.json),
[LASER, laser_claim_15, p.12](../records/laser_comprehensive_summary.json),
[SeeAct, seeact_c14, p.5](../records/seeact_comprehensive_summary.json).

Consequences depend on permission and evaluation restrictions. WebArena describes
logged-in state-changing tasks; its credential listing is a setup detail, not
evidence of credential theft. ReAct excludes real purchases and edits; LASER stops
Amazon trials at the decision to buy; SeeAct uses safety review and prohibits
sensitive final actions. These conditions qualify deployment inferences.
[WebArena, WA_C13/WA_C15, pp.4–6,18](../records/webarena_comprehensive_summary.json),
[ReAct, react_c10/c11, p.10](../records/react_comprehensive_summary.json),
[LASER, laser_claim_11, p.5](../records/laser_comprehensive_summary.json),
[SeeAct, seeact_c09/c10, pp.9,14](../records/seeact_comprehensive_summary.json).

AgentDoS adds **availability consequences** from ordinary tool functionality and
resource retention, rather than measuring a prompt-injection takeover rate. It
reports 36 confirmed vulnerabilities affecting 16 of 20 web-service agents;
recall 36/38 concerns a constructed discovered-plus-manual-miss defect set.
Short-lived resources can be exhausted within a turn; session-retained and
persistent artifacts permit longer accumulation. Minimal Docker resources,
20-minute sink budgets and early skipping qualify findings. **Analyst inference:**
authorized-looking tool requests can still exhaust host resources, so input
maliciousness and resource authorization/cleanup are distinct defense concerns.
[AgentDoS, C01–09/12, pp.4–14](../records/autonomy_comes_with_costs_detecting_denial_of_service_vulnerabilities_caused_by_resource_abusing_in_llm_based_agents_comprehensive_summary.json).

IRLbot adds an earlier non-LLM example of environment-controlled resource load: dynamic branching, host proliferation and intentional HTTP/DNS delays can impede a crawler. Its2007 single-server crawl produced6.38billion HTML responses over41.27active days, while41.5billion addresses were discovered, not downloaded. Reputation budgets and deferred queues support operational progress; they do not enforce semantic instruction authority. Extrapolation to web-agent availability is analyst inference. [Record](../records/irlbot_scaling_to_6_billion_pagesand_beyond_comprehensive_summary.json), irlbot_c01–14; pp.3–4,26–31.

## 4. Experimentally demonstrated mechanisms

The starting indirect-injection paper provides selected examples of unauthorized
instruction redirection, propagation through synthetic messages, memory
persistence, and injected influence on later search/API retrieval. Real-network,
prepared-tool, local-file and synthetic-search settings must remain distinct.
It does not provide an overall trial denominator, so reported demonstration
success is not a general 100% ASR.
[Indirect Prompt Injection, C05/C06/C08–C13, pp.5–9](../records/indirect_prompt_injection_real_world_comprehensive_summary.json).

Formalizing Prompt Injection evaluates naive, escape-character, context-ignoring,
fake-completion and combined attacks across instruction/data NLP tasks. Its GPT-4
combined average ASV of 0.75 is a mixed task-score average, not a deployed-agent
compromise probability. Role separation in the tested system/user arrangement
was insufficient for those tested attacks; it does not show that every possible
separation or containment mechanism fails.
[Formalizing Prompt Injection, C02–C05/C15, pp.4–6,8–10](../records/formalizing_prompt_injection_comprehensive_summary.json).

AdvAgent demonstrates argument redirection through hidden target-element
aria-label content in SeeAct grounding. Its exact adversarial-triplet endpoint
retains the operation and selected element while changing the argument. The
97.5%/99.8% domain-average rates use the selected 200-task test split; displayed
variation is across domains, not uncertainty from repeated trials. EIA instead
injects fields and misleading descriptions to redirect private-value entry. Its
70% specific-PII peak and 16% full-request peak use different opacity, placement
and attack strategies. Neither percentage measures an independently audited
end-to-end harmful transaction.
[AdvAgent, C01–C15, pp.3–8,12–13](../records/advagent_controllable_blackbox_red_teaming_on_web_agents_comprehensive_summary.json),
[EIA, eia_claim_01–07/09/12, pp.4–9,24,28](../records/eia_environmental_injection_attack_on_generalist_web_agents_for_privacy_leakage_comprehensive_summary.json).

Pop-ups demonstrates visual/accessibility instructions steering clicks, including
when generated thoughts still describe the intended action. Its default attacker
has the true user query and exact coordinates/SoM ID; weaker access variants
change success. Clicks are suppressed rather than redirected, so malicious-click
success is not malware execution. AgentDojo measures malicious tool actions in
simulated mutable applications, using 629 user/attacker-goal pairs and state-based
checks. Utility failures and attacker-goal fulfillment are separate endpoints.
Low malicious-goal success can reflect weak tool competence rather than sound
trust separation.
[Pop-ups, claim_01–06/10–12/15, pp.2–10](../records/attacking_vision_language_computer_agents_via_pop_ups_comprehensive_summary.json),
[AgentDojo, C02–C07/C16, pp.1–7,20](../records/agentdojo_a_dynamic_environment_to_evaluate_prompt_injection_attacks_and_defenses_for_llm_agents_comprehensive_summary.json).

WASP shows that contributor-level content can be sufficient for browser-agent
hijacking without site-layout control. URL-fragment instructions persist through
the current URL, creating an additional state carrier. Its85.7% intermediate
versus16.7% final success for one o1 configuration illustrates the difference
between diversion and completed harm. SecureWebArena diagnoses initial reasoning,
unsafe behavior and final delivery separately; its76.67–100% pop-up PDR range
is a final-outcome measure under broader environment control, not comparable
to Pop-ups' suppressed-click ASR. Its malicious-user vectors also differ from
third-party environmental injection. No cross-paper vulnerability ranking follows.
[WASP, wasp_c01–08/14/16, pp.3–9,18](../records/wasp_comprehensive_summary.json),
[SecureWebArena, C01_dual_source_threat_model/C02_benchmark_counts/C03_layered_evaluation/C05_popup_success/C08_live_scope, pp.3–8](../records/securewebarena_a_holistic_security_evaluation_benchmark_for_lvlm_based_web_agents_comprehensive_summary.json).
Ordinary task failures, inaccurate answers and calibration errors are not
substitutes for an attacker objective and corresponding outcome measurement.

AGENTVIGIL v4 adds adaptive black-box search over external-content injections,
using helper-model mutations, coverage-aware scores and MCTS-inspired selection.
Its AgentDojo o3-mini 71% fuzzing result uses 142 cases; the 65% transfer result
uses 173 test cases and selected-prompt union, not a single unconstrained trial.
VWA-adv has different budgets and 99/100 fuzz/test cases; selected-prompt GPT-4o
ASRs of 60/59% differ from prose's 70% fuzzing claim. These unresolved aggregation
and defense-superiority inconsistencies remain explicit. A local shopping review
case establishes redirected navigation; wider malware/exfiltration consequences
are not thereby demonstrated. The stable AgentFuzzer filename maps to an actual
AGENTVIGIL v4 PDF, so it is not counted as a separate named scientific replication.
[AGENTVIGIL, C01_indirect_external_content–C14_research_relevance, pp.1–9,12,14](../records/agentfuzzer_generic_black_box_fuzzing_for_indirect_prompt_injection_against_llm_agents_comprehensive_summary.json).

Context Manipulation evaluates a distinct **stored-context write boundary**.
Directly editing the agent's history or plan can insert task-related pretexts,
with context chaining moving Plan Injection Benchmark privacy ASR from 35.6%
to 53.3% (17.7 percentage points, analyst-derived). Its four categories each use
15 samples repeated five times; the separate WebVoyager-Privacy suite has 45
tasks with less clearly specified repeat details. Tool access and completed
exfiltration are separate endpoints. The acquisition of memory write access is
assumed/motivated, not an end-to-end webpage-to-storage compromise experiment.
**Analyst interpretation:** low-trust content and mutable plans can both influence
an agent, but require different attacker capabilities and preservation boundaries.
[Context Manipulation, C01–10/12–14, pp.4–8](../records/context_manipulation_attacks_web_agents_are_susceptible_to_corrupted_memory_comprehensive_summary.json).

SafeArena supplies a separate malicious-user misuse condition with permissions
already granted. Its 250 harmful/250 paired safe tasks help separate capability
from refusal, but functional harmful completion and trajectory judge ratings
are distinct: GPT-4o has 22.8% functional harmful TCR versus 34.7% ARIA-4. ARIA-3
attempted-but-failed tasks are not completed harm. All 49 selected, initially
refused Claude tasks were manually jailbroken within three attempts; that result
is conditional on selection, not benchmark-wide 100% harmful completion. Priming
also changes starting state and remaining-task wording, complicating a single-
factor interpretation. No matched standalone security comparison is supplied.
[SafeArena, SA_C01–10/13, pp.3–8,14–15](../records/safearena_comprehensive_summary.json).

AgentRewardBench shows that observed action completion and evaluator approval can diverge without an adversary. Its 1,302 trajectories span 351 tasks, four agents and five benchmarks. GPT-4o(A)'s success precision69.8% implies30.2% false positives among predicted successes, not all trajectories. Official rules have precision83.8% but recall55.9%; neither comparison establishes attack detection. Agent-specific appendix tables repeat all-agent contents and remain unresolved. [Record](../records/agentrewardbench_evaluating_automatic_evaluations_of_web_agent_trajectories_comprehensive_summary.json), C01–16; pp.4–9,17–23.

ToolHijacker distinguishes retrieval of a malicious tool document from selecting that tool. Its GPT-4o gradient-free selection ASR96.7% on MetaTool and88.2% on ToolBench uses10targettasks×100phrases per dataset. It does not demonstrate subsequent harmful tool execution. The attack crosses documentation/retrieval/selection boundaries; malicious retrieval alone is insufficient, as its R-only ablation shows. [Record](../records/toolhijacker_comprehensive_summary.json), TH-C01–15; pp.2–12,14–18.

Hidden in Memory demonstrates an external-content route into persistent fabricated user state, unlike a direct memory-store write assumption. Its700injectionpairs and400standardized downstream goals expose different stages. Standardized goal-adjacent agent usage60–89% is conditional on available poisoned memory; the coupled external-manager agent3–66% rates use a separate fixed-attack protocol. Crucially, its agent judge counts claims, attempts and goal pursuit, so neither metric is solely completed harmful execution. Selected production validation checks injection transfer only. [Record](../records/hidden_in_memory_sleeper_memory_poisoning_in_llm_agents_comprehensive_summary.json), C01–15; pp.1–9,43–50,71–72,79–81.

Overthinking Loops shows availability/cost harm under malicious registry additions with fixed queries and model parameters. Its Qwen-Code headline142.35×tokens/27.49×runtime differs from per-problem extremes and has an unresolved aggregation convention. Accuracy can remain similar while costs rise, so performance alone does not capture resource harm. Normal-versus-mixed agents supply a registry intervention control, not a standalone comparison; production-versus-ReAct severity differences are confounded by tools, task horizon and GLM versions. [Record](../records/overthinking_loops_in_agents_a_structural_risk_via_mcp_tools_comprehensive_summary.json), C01–14; pp.3–7,10–12.

ST-WebAgentBench separates completion from zero-policy-violation completion: AWM33.8/20%, WebVoyager12.8/10.3%, WorkArena26/15% under the described pass@3 setup. Aggregate violations include benign hallucination, consent failures, hierarchy errors and environmental injection; they are not a single attack success measure. Risk-ratio denominators and source prose/figures disagree, simulated consent is auto-approved, and policy-load associations do not isolate a causal defense effect. [Record](../records/st_webagentbench_comprehensive_summary.json), C01–14; pp.4–10,26–30,36–43.

## 5. Experimentally supported defenses

WARD provides source-reported evidence for a parallel multimodal guard and staged
training under listed protocols. At adaptive trial budget ten, sample success is
5.62%/3.12% for its two variants, whereas attempt success is 0.62%/0.34%. These
metrics have different denominators. Dataset-specific 100% recall is not a claim
of universal protection; pixel-level attacks and task-aligned fabricated content
remain limitations, and benign utility testing uses particular trajectories.
[WARD, ward_c02/c04–c09/c11/c12, pp.3,6–9,16,21–22](../records/ward_comprehensive_summary.json).

The formal injection benchmark illustrates security/utility tradeoffs: one naive
LLM detector has zero observed false negatives for the displayed combined attacks
but rejects large fractions of clean data in some tasks. Known-answer detection
is attack-dependent and its interpretation is scoped to the evaluated prompt.
These results cannot support either a universal defense ranking or a universal
claim that all defenses are ineffective.
[Formalizing Prompt Injection, C09–C12, pp.13–14](../records/formalizing_prompt_injection_comprehensive_summary.json).

Prompt warnings do not reliably block the tested AdvAgent/EIA variants: AdvAgent
reports Gemini ASR 88.8–89.8% under three prompt defenses, and EIA's three
warning prompts yield similar curves to its default setup. This is evidence
about those defense families and configurations, not all defenses. EIA's
VirusTotal non-detection and proposed supervision advice do not establish a
tested agent-containment guarantee. Its Table 1 variance and aggregation wording
remain unresolved source concerns.
[AdvAgent, C01–C15, pp.3–8,12–13](../records/advagent_controllable_blackbox_red_teaming_on_web_agents_comprehensive_summary.json),
[EIA, eia_claim_08–10/14, pp.7–9](../records/eia_environmental_injection_attack_on_generalist_web_agents_for_privacy_leakage_comprehensive_summary.json).

Pop-ups shows that step-wise warning prompts can reduce step-level click ASR
without eliminating task-level exposure:5.9% ASR versus32% TASR in its tested
GPT-4-Turbo screen setting, increasing to10.4%/44% with a simple attack variant.
AgentDojo's tool filter reduces targeted ASR to6.84% in Table 5's defense experiment,
versus57.69% for that table's no-defense configuration. Necessary-tool overlap
and unavailable advance planning limit it. Detector7.95% targeted ASR accompanies
a benign-utility drop to41.49%, illustrating a different tradeoff. These numbers
are protocol-specific and are not rankings against WARD or webpage attacks.
[Pop-ups, claim_09/10/14, pp.2–7](../records/attacking_vision_language_computer_agents_via_pop_ups_comprehensive_summary.json),
[AgentDojo, C08–C12/C14, pp.4–26](../records/agentdojo_a_dynamic_environment_to_evaluate_prompt_injection_attacks_and_defenses_for_llm_agents_comprehensive_summary.json).

WASP's tested warning prompt trades lower attack rates for lower utility in
some configurations. Its tool-role hierarchy configurations remain vulnerable,
but model/scaffolding changes confound a general defense comparison. SecureWebArena
does not test a defense intervention; different model-category outcomes are not
a causal defense ablation. Source count, rate and category-label discrepancies
remain flagged in these records rather than repaired by speculation.
[WASP, wasp_c06/09–13/15, pp.5–10,21–22](../records/wasp_comprehensive_summary.json),
[SecureWebArena, C06_gui_attack_discrepancy/C07_stage_attenuation/C10_author_limitations, pp.6–9](../records/securewebarena_a_holistic_security_evaluation_benchmark_for_lvlm_based_web_agents_comprehensive_summary.json).

Spotlighting provides source-reported evidence that input provenance cues can
reduce synthetic keyword-only takeover. Datamarking has different rates by task
and model (GPT-3.5 summary3.10%, Q&A8%); encoding GPT-3.5 reaches0%/1.8% in those
attack tests but impairs ordinary-task utility. These are document experiments,
not browser-side harm rates. Dynamic marking and stronger adversarial variants
remain proposals without a quantitative adaptive robustness result.
[Spotlighting, spotlighting_c02–14, pp.3–13](../records/defending_against_indirect_prompt_injection_attacks_with_spotlighting_comprehensive_summary.json).

IsolateGPT offers a different boundary: process/app context and memory isolation,
mediated cross-app communication, deterministic operators and permission checks.
It compares two GPT-4 agentic systems. Its1598-scenario evaluation reports
Vanilla20.2% attack success versus Isolate 7.6% permission appearances, with
warnings on100% of those appearances. The latter is not ASR. Case-study protection
requires refusing warned permissions; within-app injection compromise is outside
scope. No human-user study establishes how often users make the required decision.
[IsolateGPT, claim_02_isolation_method/claim_03_attack_sample/claim_04_security_metrics/claim_05_user_screening/claim_06_permission_condition/claim_07_scope_limit, pp.5–10,19](../records/isolategpt_an_execution_isolation_architecture_for_llm_based_agentic_systems_comprehensive_summary.json).

ceLLMate demonstrates a browser-side authorization boundary at HTTP requests
and semantic actions, independent of the model's low-level click/type sequence.
Its12 GitLab automation scripts emulate a fully compromised agent; all forbidden
goals are blocked under the selected policies. This is enforcement evidence,
not an end-to-end prompt-injection resistance rate. Correct trusted sitemaps and
policies, complete interception, trusted browser operation and agent confinement
are conditions. Harmful comment content remains possible when commenting is
a permitted action. Policy selection accuracy also differs from joint argument
accuracy and cannot substitute for enforcement correctness.
[ceLLMate, cellmate_c02–08/12–14, pp.3–13](../records/cellmate_sandboxing_browser_ai_agents_comprehensive_summary.json).

These defenses address different boundaries: provenance cues help models treat
input as data; guards screen observations; isolation restricts cross-component
propagation; authorization restricts executable effects. This categorization is
analyst interpretation of the cited designs, not a universal effectiveness order.
Task Shield adds an experimentally evaluated **user-goal alignment boundary**.
It extracts actionable instructions from user, assistant and tool messages,
compares candidate directives with the trusted user-task set, and flags zero
aggregate contribution. Tool outputs remain present with corrective feedback;
misaligned outgoing calls can be prevented before execution. In its AgentDojo
Important Instructions experiment, GPT-4o ASR changes from 47.69% to 2.07% and
utility under attack from 50.08% to 69.79%; clean utility is 73.20%. GPT-4o-mini
reports 2.23% ASR and 54.53% attacked utility. These are one-trial-per-task,
synthetic benchmark results; exact case denominators and security uncertainty
estimates are not supplied. No measured adaptive campaign or matched standalone
control establishes broader protection or a web-agent vulnerability gap.
[Task Shield, claim_01–06/09–12, pp.1–9,15](../records/the_task_shield_enforcing_task_alignment_to_defend_against_indirect_prompt_injection_in_llm_agents_comprehensive_summary.json).

Its ablation demonstrates a scoped trade-off: on GPT-4o-mini Slack, Input Shield
has 63.80% attacked utility and 4.76% ASR versus full Task Shield's 50.48% and
0.95%; median latencies are 18.78 versus 62.56 seconds. Table 2a reports GPT-4o
Slack utility of 64.76%, while Table 4's GPT-4o-defender row reports 50.48%; the
paper does not explain the difference. The restatement prose also compares
63.8% with 43.8%, although Table 3 assigns 63.80% to Input Shield and 50.48% to
the full shield. These discrepancies remain review flags, not reconciled results.
[Task Shield, claim_05/07/08; narrative sections 11/14, pp.7–8,13–14](../records/the_task_shield_enforcing_task_alignment_to_defend_against_indirect_prompt_injection_in_llm_agents_comprehensive_summary.json).

**Analyst comparison of enforcement boundaries:** Task Shield checks semantic
contribution to user goals at both input and action stages. WARD screens external
observations for injection; Spotlighting marks provenance within a shared model
input channel. IsolateGPT separates app contexts/processes and mediates cross-app
communication and permissions. ceLLMate authorizes semantic HTTP actions outside
the agent using trusted sitemaps and policies. AgentDojo's evaluated tool filter
restricts capabilities, its detector can abort on suspicious tool input, and its
repeated-prompt defense reminds the model of the task. These boundaries target
different failure paths: goal relevance, malicious input, source identity,
cross-app propagation, or permitted action. A semantic contribution judgment is
not equivalent to deterministic authorization; permitted-action misuse and
checker deception remain distinct concerns. The papers' ASRs and other endpoints
are not pooled or ranked.
[Task Shield, claim_02/03/09, pp.4–5,9](../records/the_task_shield_enforcing_task_alignment_to_defend_against_indirect_prompt_injection_in_llm_agents_comprehensive_summary.json),
[WARD, ward_c02/04/12, pp.3,6–7,21–22](../records/ward_comprehensive_summary.json),
[Spotlighting, spotlighting_c02/14, pp.3–4,10–11](../records/defending_against_indirect_prompt_injection_attacks_with_spotlighting_comprehensive_summary.json),
[IsolateGPT, claim_02_isolation_method/claim_05_user_screening/claim_07_scope_limit, pp.5–9](../records/isolategpt_an_execution_isolation_architecture_for_llm_based_agentic_systems_comprehensive_summary.json),
[ceLLMate, cellmate_c02–04/08, pp.5–8,12](../records/cellmate_sandboxing_browser_ai_agents_comprehensive_summary.json),
[AgentDojo, C08–10, pp.8–9,20](../records/agentdojo_a_dynamic_environment_to_evaluate_prompt_injection_attacks_and_defenses_for_llm_agents_comprehensive_summary.json).

Capability filters, human assistance and omitted sensitive actions in
non-security studies are not credited as experimentally validated attack defenses.

The new adaptive/context studies qualify defense expectations without providing
cross-paper rankings. AGENTVIGIL evaluates its selected attacks against specific
input-oriented defenses, with nonzero residual ASR and baseline exceptions;
security-only results do not establish preserved utility. Context Manipulation
finds that SECURE/SANDWICH retrieved-content defenses do not protect directly
corrupted plans/history under its tested conditions. **Analyst hypothesis:**
semantic relevance checks need evaluation against task-related malicious plan
extensions; this paper did not test Task Shield, WARD, IsolateGPT or ceLLMate.
Storage-integrity proposals and stronger-model suggestions remain untested here.
[AGENTVIGIL, C09_defense_effects/C10_ablation_joint, pp.6–8](../records/agentfuzzer_generic_black_box_fuzzing_for_indirect_prompt_injection_against_llm_agents_comprehensive_summary.json),
[Context Manipulation, C02/07–11, pp.4,7–8](../records/context_manipulation_attacks_web_agents_are_susceptible_to_corrupted_memory_comprehensive_summary.json).

AgentDoS reports resource-governance mitigations (download/directory caps and
cleanup) without a separate controlled security/utility evaluation. SafeArena's
NSS attempts capability normalization using successful paired safe tasks as its
denominator, not all harmful requests. Published GPT-4o/Claude NSS values cannot
be reconstructed from the main functional totals under the same-pair binary
formula assumption; reward/subset aggregation remains unresolved. Reported NSS
values are retained without correction. These issues limit metric interpretation;
neither refusal alone nor task failure proves absence of all undesirable effects.
[AgentDoS, C10/13, pp.13,15](../records/autonomy_comes_with_costs_detecting_denial_of_service_vulnerabilities_caused_by_resource_abusing_in_llm_based_agents_comprehensive_summary.json),
[SafeArena, SA_C04–07/11; narrative section14, pp.4–9](../records/safearena_comprehensive_summary.json).

PlanGuard separates a planner receiving trusted user instructions/tool definitions from the executing agent. Within 1,054 InjecAgent attack cases and an explicitly compliance-inducing DeepSeek-V3.2 setup, Stage-I and full defense report zero observed ASR, compared with56.90% direct harm/88.67% data stealing vanilla ASR. Semantic verification lowers reported FPR to0.97/3.28%, but the benign denominator is unclear and FPR is not end-to-end utility. The abstract1.49% aggregate cannot be reconstructed from the supplied weights. Adaptive parameter manipulation remains a theoretical concern; context-dependent argument correctness lacks ground truth and no latency cost is quantified. Zero observed attacks does not prove universal prevention. [Record](../records/planguard_defending_agents_against_indirect_prompt_injection_via_planning_based_consistency_verification_comprehensive_summary.json), PG_C01–17; pp.1–6.

ToolHijacker tests fine-tuned StruQ/SecAlign selection models, with residualASR84.6–99.6% under its task-aligned tool-document protocol; this is not comparable to other papers' answer-output or browser-action ASR. Its detectorFNR uses10malicious documents per dataset. Hidden in Memory's GEPA defense is model/attack-dependent: Kimi behaviorIR6.2→64.6% under adaptiveAC+. High benign direct-save performance on70requests per cell lacks an undefended baseline and does not test ordinary document-memory utility. Its probes show separability in separate open-weight settings, not proven live prevention. [ToolHijacker record](../records/toolhijacker_comprehensive_summary.json), TH-C08–10; pp.11–12,16. [Memory record](../records/hidden_in_memory_sleeper_memory_poisoning_in_llm_agents_comprehensive_summary.json), C08–10; pp.8–9,57,59–61,71–72.

Overthinking Loops' NoWait experiment leaves substantial mixed-registry amplification under its own normal baseline, supporting a limit of token-generation suppression against cyclic tool calls. Alternative structural defenses remain untested. ST-WebAgentBench evaluates policy-aware agents but does not experimentally validate its proposed controller; scoring-dimension removal changes the metric rather than deploying/removing a defense. [Loop record](../records/overthinking_loops_in_agents_a_structural_risk_via_mcp_tools_comprehensive_summary.json), C09–10; p.6. [Policy record](../records/st_webagentbench_comprehensive_summary.json), C05,C13; pp.9,41–43.

## 6. Untested standalone-LLM comparisons

The available records do not establish a controlled general vulnerability ordering
between browser agents and standalone LLMs. BrowseComp compares accuracy and
calibration across model configurations, with model versions and task-oriented
training differences. Bearcubs compares information-seeking accuracy under
unequal time allowances and dates. MMINA's standalone-model terminology denotes
capability baselines, not a security control. None of these scores can quantify
the added effect of browser integration on adversarial compromise.
[BrowseComp, browsecomp_c06–c08/c14, pp.6–9](../records/browsecomp_comprehensive_summary.json),
[Bearcubs, bearcubs_c06/c07/c15, pp.3–10](../records/bearcubs_comprehensive_summary.json),
[MMINA, mmina_c14, pp.5–8](../records/mmina_comprehensive_summary.json).

IsolateGPT compares isolated and nonisolated GPT-4-based agentic systems;
ceLLMate compares authorization behavior and policy prediction; Spotlighting
tests document-processing LLMs. None supplies a matched browser-agent versus
tool-free standalone vulnerability estimate. AgentDojo and WASP also use different
capability and compromise endpoints, so lower attacker-goal completion need not
mean stronger instruction separation.
[IsolateGPT, claim_04_security_metrics/claim_12_research_relevance, pp.1–5,10](../records/isolategpt_an_execution_isolation_architecture_for_llm_based_agentic_systems_comprehensive_summary.json),
[ceLLMate, cellmate_c07/08/15, pp.12–13](../records/cellmate_sandboxing_browser_ai_agents_comprehensive_summary.json),
[Spotlighting, spotlighting_c04/12/15, pp.1–2,5,11–12](../records/defending_against_indirect_prompt_injection_attacks_with_spotlighting_comprehensive_summary.json),
[AgentDojo, C07/C16, pp.1–3,7](../records/agentdojo_a_dynamic_environment_to_evaluate_prompt_injection_attacks_and_defenses_for_llm_agents_comprehensive_summary.json),
[WASP, wasp_c08/14, pp.3–9](../records/wasp_comprehensive_summary.json).

A mechanism-based interpretation is supported more narrowly: external data can
supply unauthorized instructions, and successful influence can have additional
consequences when connected to actions or memory. The size and direction of a
matched causal vulnerability difference remain hypotheses requiring measurement.
No global novelty claim is made.

The Iteration 4 comparison check distinguishes WebGPT's base-GPT-3 control from
a matched security experiment. It reports TruthfulQA answer-quality improvement,
but changes fine-tuning, selection and judging (automated GPT-3 versus human
WebGPT evaluation). No attacker-controlled injection outcome establishes a
standalone-versus-web-agent susceptibility difference. VisualWebArena's text-only
and multimodal configurations all remain browser agents. Neither paper empirically
answers the central security comparison. Preference ratings, truthfulness,
benign task success and attack outcomes remain separate quantities.
[WebGPT, webgpt_c02–04/11/14, pp.3–11](../records/webgpt_comprehensive_summary.json),
[VisualWebArena, vwa_c06/07/12/13, pp.3–9](../records/visualwebarena_comprehensive_summary.json).

Neither PlanGuard nor AgentRewardBench supplies otherwise matched standalone-LLM/web-agent attack configurations. The former compares tool-agent defenses under a scoped injection protocol; the latter compares benign trajectory evaluators. These results support trust-boundary and outcome-measurement questions without isolating the causal effect of web-agent architecture.

Toward Secure LLM Agents offers a secondary synthesis of247papers organized by information flow, delegated authority and persistent state. It supports a mechanism-based architectural distinction but supplies no original matched security comparison. Its ASR129/utility22/latency8/cost7 counts describe metric reporting, not pooled outcomes. Technical labels overlap, benchmark heatmaps measure paper co-occurrence, and proposed defense stacks are explicitly unvalidated engineering interpretations. The survey reinforces questions about long-horizon effects and compositional controls without empirically resolving the central comparison. [Record](../records/toward_secure_llm_agents_comprehensive_summary.json), C01–15; pp.4–24,36–40.

WebWalker's closed-book Gemini/o1 accuracies8.08/9.85% do not create a matched standalone security baseline: backbones/configurations differ and the measured endpoint is benign factual QA. Its37.50% GPT-4o WebWalker accuracy and successful-case action count4.67 cannot be interpreted as ASR or complete operational cost. WebLINX's model/modality comparisons likewise measure static next-action scores, with training and representations changing. Neither addition empirically answers the central comparative security question.

Neither ToolHijacker nor Hidden in Memory compares otherwise matched standalone and web-agent security configurations. The latter's provider setup swap changes prompts, memory interfaces/placement and document rendering together; GPT-5.5IR97/3/1% on a100sample subset demonstrates harness sensitivity, not a tool-free versus agent causal effect. Conditional memory usage and malicious-tool selection must remain distinct from completed harmful actions.

Overthinking Loops controls registry additions in existing agents; ST-WebAgentBench compares three GPT-4o-backed agent implementations. Neither includes an otherwise matched standalone LLM and web-agent security condition. These contribute operational and compliance evidence without answering the comparative causal question.

## 7. Emerging research questions

These are analyst-proposed questions, not results already demonstrated:

- With the same model, legitimate instructions and attacker budget, how does
  browser/tool access change both instruction susceptibility and harmful effects?
- Which boundaries prevent external data from gaining instruction authority,
  and which prevent a manipulated model from exercising an unauthorized action?
- How do screenshot, HTML, document, tool-output and memory routes differ under
  matched delivery constraints and adaptive attacker effort?
- How do guards affect benign task completion, false rejection, latency and
  utility when the attacker changes strategy after observing the defense?
- Do observed attacks persist across tasks, resets or site changes, and what
  constitutes a demonstrably completed harmful action rather than an action proxy?
- How reliable are attack evaluators and claimed defenses when victim traces,
  execution-side effects, source provenance and response-only judging disagree?

The [comparison matrix](SECURITY_COMPARISON_MATRIX.md) preserves protocol and
scope differences rather than pooling incompatible attack percentages.

StruQ gives a concrete data/instruction separation mechanism: frontend reserved-token filtering and structured instruction tuning. Its exact-string ASR on 208 data examples remains 58% for Llama GCG and 56% for Mistral GCG, despite much lower manual-attack results. TAP and GCG have different query/compute budgets and should not be pooled. AlpacaEval win rates on 805 comparisons are a separate utility proxy; they do not establish browser task preservation. BIPIA comparisons use different starting models and the long-context GCG resource limitation is unavailable evidence. [StruQ record](../records/struq_defending_against_prompt_injection_with_structured_queries_comprehensive_summary.json), struq_c01–16, pp.8–14.

An Illusion of Progress strengthens the distinction between claimed completion and interaction evidence. On 300 live tasks across 136 websites, human success ranges from 28.0% to Operator's 61.3%; these are benign capability results, not attack success. WebJudge-o4-mini's 85.7% decision agreement and 3.8pp average success-rate gap are evaluator metrics. On reused AgentRewardBench trajectories, precision82.0% accompanies recall47.8%, illustrating a judge tradeoff rather than universal superiority. Search-only baseline comparisons use different benchmark tasks; success-only step efficiency excludes failed runs. The paper supplies no matched standalone/web-agent security experiment. [Illusion record](../records/an_illusion_of_progress_assessing_the_current_state_of_web_agents_comprehensive_summary.json), claim_01–16, pp.3–10,19–21,26,30.

Classical crawler traps provide an earlier example of environment-controlled navigation and resource waste. The 2021 crawler-trap paper evaluates 13 families of 500 pages using content distances and interval-overlap measures. Dottyback's 0.57% merged-cluster overlap is not an observed false-negative rate; the text's near-perfect detection interpretation exceeds the supplied prediction-count evidence. Implementation and operational testing are explicitly deferred on p.6. The proposed robust clustering is therefore a research mechanism, not a validated defense for LLM agents. [Crawler-trap record](../records/detection_of_crawler_traps_formalization_and_implementation_defeating_protection_on_internet_and_on_the_tor_network_comprehensive_summary.json), C04–14, pp.6–12.

Toolformer inserts tool responses into generation context and learns calls through continuation-loss filtering. An irrelevant search result can nevertheless reduce perplexity, showing that the selection proxy is not equivalent to semantic usefulness; adversarial exploitability remains untested. The same trained model's tools-enabled/disabled comparison isolates a capability contribution under task-specific restrictions (e.g., LAMA Wikipedia search disabled, QA tool disabled on QA benchmarks). DATESET improves27.3−5.9=21.4 score points, while TEMPLAMA barely uses the calendar. Its one-call cap and lack of chained/interactive tools distinguish it from long-horizon web agents. This is a matched tool-use capability ablation, not a controlled security comparison between otherwise matched standalone LLM and web-agent configurations. None of the twenty additions establishes that central comparative security question empirically. [Toolformer record](../records/toolformer_comprehensive_summary.json), toolformer_claim_02–16, pp.3–11,17.

## Full-corpus continuation — first 16 additions

The capability additions expand evidence for shopping, enterprise interaction, extraction and long-horizon research architectures. They expose observations, source selection, code generation and judging as distinct places where errors or untrusted content could enter a system. These are analyst-inferred surfaces, not measured compromises. WebShop’s 500-task evaluation and WorkArena’s 330 evaluations measure task performance; Mind2Web 2’s 99.03% node-judge accuracy comes from 15 selected tasks and excludes total failures. WebDancer/WebSailor training and multi-run comparisons do not isolate the security effect of agentization. [WebShop](../records/webshop_comprehensive_summary.json), webshop_c01–12, pp.4–10; [WorkArena](../records/workarena_comprehensive_summary.json), workarena_c01–17, pp.1–21; [Mind2Web 2](../records/mind2web_2_comprehensive_summary.json), m2w2_c01–15, pp.1–51; [WebDancer](../records/webdancer_comprehensive_summary.json), WD_C01–14, pp.1–24; [WebSailor](../records/websailor_comprehensive_summary.json), websailor_c01–15, pp.1–23.

AutoScraper and WebScraper illustrate extraction-code pipelines rather than evaluated security defenses. Three seed pages, DOM reduction, XPath/code generation and synthesis determine extraction utility. Synthesis can worsen some AutoScraper results; WebScraper’s news/ecommerce results have different task definitions. They do not establish adversarial robustness or a universal advantage of one architecture. [AutoScraper](../records/autoscraper_comprehensive_summary.json), autoscraper_c01–15, pp.5–19; [WebScraper](../records/webscraper_comprehensive_summary.json), webscraper_c01–16, pp.2–6.

The published AgentVigil record is a version-family member of the earlier AgentFuzzer material, not an independent replication. Its top-five union rates, optimization/test splits and adaptive-defense optimization differ. The published adaptive repeat result must not be pooled with nonadaptive repeat outcomes or treated as a paired causal improvement. Benign utility remains missing. [AgentVigil](../records/agentvigil_generic_black_box_red_teaming_for_indirect_prompt_injection_against_llm_agents_comprehensive_summary.json), av_c01–15, pp.2–14.

Commercial-agent demonstrations show stronger action-side evidence in selected controlled cases: form submission and downloading/running a test executable. Their 10/10 results are conditional on specific encounters or setups; PaperQA’s 100/100 concerns one fabricated retrieved document in a synthetic corpus. SearchGeo and FORGE primarily measure malicious endorsement or recommendation under assumed ranked exposure, not completed installation, purchase or compromise. Unsafe LLM Search measures risky recommendations and classifier outcomes, with ambiguous URLs and differing denominators. These endpoint distinctions matter more than a pooled attack-success ranking. [Commercial agents](../records/commercial_llm_agents_are_already_vulnerable_to_simple_yet_dangerous_attacks_comprehensive_summary.json), C01–14, pp.1–10; [SearchGeo](../records/searchgeo_comprehensive_summary.json), searchgeo_c01–15, pp.1–22; [FORGE](../records/forge_comprehensive_summary.json), forge_c01–16, pp.1–26; [Unsafe search](../records/unsafe_llm_search_comprehensive_summary.json), unsafe_search_c01–16, physical pp.1–21.

Retrieval Barrier separates entering the retrieval context from downstream harmful action. Optimized placement can succeed while a particular attack fails: the GPT-4o CEM email target has recall1.0 and ASR0.02, whereas tool broadcasting is0.92. Single/multi-agent code outcomes also differ, but payload and framework adaptation prevent isolating agent count as the cause. The missing theorem proof and source count discrepancies remain unresolved. [Retrieval Barrier](../records/retrieval_barrier_comprehensive_summary.json), C01–18, pp.1–20.

VPI-Bench explicitly separates attack attempts from full objective completion, both divided by all evaluated tasks. High attempts with zero completion can reflect execution limitations; this does not prove attack recognition. Its CUA/BUA comparison changes tasks and resources, so the large rate differences cannot identify one defense’s causal effect. WAAA extends the trust-boundary account to ordinary deceptive interfaces and agent-mediated cross-origin actions; it does not demonstrate a native browser isolation exploit. Ten-run per-class trials, delegation wording, custom tools, unsupported capabilities and version changes constrain the claims. Proposed architectural defenses remain untested. [VPI-Bench](../records/vpi_bench_visual_prompt_injection_attacks_for_computer_use_agents_comprehensive_summary.json), vpi_claim_01–17, pp.2–21; [WAAA](../records/waaa_web_adversaries_against_agentic_browsers_comprehensive_summary.json), waaa_c01–14, pp.4–14.

Canary tokens add evidence about source exposure and attribution rather than compromise. Token appearances after a site becomes unavailable or restricted do not determine cache location, prove a new crawl, establish robots violations or show training memorization. Threshold ambiguities and attribution assumptions remain open. [Canary Tokens](../records/canary_tokens_comprehensive_summary.json), canary_claim_01–15, pp.4–16.

Defense evidence continues to show security/utility tradeoffs with incompatible evaluation endpoints. FORGE’s warning and classifier measures include brand-recommendation rejection costs; Unsafe LLM Search’s false positives are a classification measure, not demonstrated browsing-task utility. VPI-Bench’s defensive prompts have mixed outcomes and no complete clean-task utility study. Source/table inconsistencies are preserved in the records and [source review](../CORPUS_COMPLETION_REVIEW.md).

**Controlled standalone-LLM versus web-agent comparison:** none of these 16 additions provides an otherwise matched adversarial comparison holding the model, legitimate instructions, exposure and attacker budget fixed. Reasoning toggles, direct-URL versus post exposure, CUA/BUA, traditional search and adapted single/multi-agent setups answer different questions. The central comparative security question remains empirically unresolved by this addition set. The mechanisms support qualified research hypotheses about exposure and authority; they do not establish a universal susceptibility multiplier or consequences of compromise.

## Full-corpus continuation — additions 17–20

WebCloak reverses the usual agent-as-victim threat model: a website owner disrupts scraping pipelines operated by malicious users. Dynamic DOM obfuscation and hidden optimized semantic cues exploit structural and interpretation dependencies. Selected high-recall pages show mean88.7% to0% extraction recall, but full-benchmark baselines differ and knowledgeable adaptive attempts are nonzero (L2S0.20%, Crawl4AI1.58%, Browser-Use0%). Thirty-five-user visual/experience measures and loading costs do not establish accessibility or authorized-agent utility. The DeepSeek0-versus2.9% conflict, text-asset aggregation and Mac Chrome FCP/LCP mismatch remain unresolved. Embedded artifact badges/meta-review are supplied documents, not independent reproduction here. [WebCloak](../records/webcloak_characterizing_and_mitigating_threats_from_llm_driven_web_agents_as_intelligent_scrapers_comprehensive_summary.json), C01–16, physical pp.1–20.

WebInject adds a nontextual environmental route: source-controlled pixel perturbations influence screenshot-based next-action output. White-box model access, selected target prompts/monitors and randomized histories frame the result; exact-action ASR.963–.975 is not proof of a completed harmful workflow. The screenshot baseline is adapted to page-only control, so its zero result does not refute the original screenshot-control threat model. Phi-4’s aggregate.963 conflicts with the equal mean.9725 derived from its ten dataset cells. Human stealth and closed-source transfer are not established. [WebInject](../records/webinject_prompt_injection_attack_to_web_agents_comprehensive_summary.json), C01–C15 and physical pp.3–9,12–21.

When AI Meets the Web supplies controlled evidence that integration practices can undermine role boundaries: attacker-supplied history can become privileged messages, and scraped UGC can enter trusted context. Its 17-plugin inventory and Common Crawl marker deployments differ from functional chatbots. The13/100 exposure result is a selected functional P1 e-commerce sample; live219/300 prompt-leak labels lack ground-truth prompts. Local ten-run cells isolate several role/insertion/prompt configurations but change message layout and provider support; system-role cells have onlyfiveOpenAImodels. Hardening application task constraints does not reliably secure tool arguments. UGCBuster’s30-page detection study and reported40–75% attack reduction lack a full adaptive defense/utility evaluation; absolute-versus-relative reduction is unspecified. [Plugin study](../records/when_ai_meets_web_comprehensive_summary.json), claim_01–14, physical pp.3–14,18–20.

AgentLAB illustrates how tool composition, intermediate dependencies and persistent preferences can extend attacks over time. One-shot versus adaptive multi-turn comparisons change strategy and budget; success-only turn counts omit failures. Full-objective success is the author’s endpoint, with internal model judging and claimed programmatic checks; supplied demonstrations are not independent execution receipts. Its GPT-5.1 overall69.9% differs from the five-cell mean60.18%, and risk/category and Llama task-injection counts conflict. Claude0% applies to task injection, while tool chaining remains73.3%. Defense outcomes vary by model/family and lack reported benign utility despite paired benign cases. [AgentLAB](../records/agentlab_benchmarking_llm_agents_against_long_horizon_attacks_comprehensive_summary.json), claim_01_benchmark_scope through claim_14_shopping_drift, physical pp.1–19.

The first20 continuation additions strengthen the architectural hypotheses: environmental observations, preprocessing, role assignment, action authority and persistent state create distinguishable exposure and consequence pathways. None supplies an otherwise matched standalone-LLM versus web-agent adversarial comparison. These mechanisms do not establish a universal vulnerability gap, and unlike endpoints remain unsuitable for pooled attack-rate ranking. Strong adaptive defense tests, ground-truth execution evaluation and matched security/utility studies remain open research needs.


## Full-corpus continuation — additions21–22

AI Agent Traps organizes exposure by perception, reasoning, memory/learning, action, multi-agent dynamics and human oversight. Its Table1 contains18 named mechanism rows plus the human-overseer family description; this is a conceptual inventory, not experimental validation. The cited partial-commandeering, exfiltration, memory and orchestration rates have distinct endpoints and protocols. Systemic and human mechanisms are unevenly supported; compositional fragment traps are explicitly more hypothetical. Proposed mitigation pathways are not evaluated here. [AI Agent Traps](../records/ai_agent_traps_comprehensive_summary.json), C01–C14, physical pp.1–16.

Breaking Agents makes availability and task disruption explicit endpoints. In the emulator, clean failure15.3% rises to59.4% under loop injection; these are author-judged failed tasks, not independently confirmed harmful actions. Direct user-input, external email/CSV and memory results differ: Gmail external content is vulnerable in tested conditions while CSV and memory variants show zero observed attacks, which does not prove general robustness. The two-agent propagation cases assume control of an upstream agent and do not measure population-scale resource damage. Self-examination measures anomaly detection rather than recovered utility. The36-versus38 toolkit inventory and defense-table references remain unresolved. [Breaking Agents](../records/breaking_agents_compromising_autonomous_llm_agents_through_malfunction_amplification_comprehensive_summary.json), C01–C14, physical pp.1–13.

Neither addition supplies an otherwise matched standalone-LLM/web-agent adversarial comparison. The now22 continuation additions support distinct exposure and consequence mechanisms; they do not establish a universal comparative vulnerability rate.


## Full-corpus continuation — additions23–24

RecurGuard separates resource harms, detector visibility and workload costs. On the primary model it detects99/100 OverThink and46/50 ExtendAttack instances; its fully held-out clean certificate is0/150 SQuAD false positives, with reported Wilson upper bound below2.5%. Longer-task profiles partly reuse calibration examples. Topical C1 attacks retain11.9x amplification at approximately50% joint miss; full C4 evasion retains2.2x overhead. QDM is post-hoc and attack-informed in development, while RecurGuard requires exposed reasoning and cancellation for measured token savings. Provider-summarized and hidden traces constrain applicability; these are not otherwise matched standalone/web-agent security tests. [RecurGuard](../records/recurguard_runtime_monitoring_for_reasoning_token_consumption_attacks_comprehensive_summary.json), C01–C14, physical pp.2–14.

ACE provides an architectural contrast: trusted query-only abstract planning precedes independent app matching, static lattice information-flow checks and isolated rule-based execution. It prevents attacker-app invocation in1054 adapted INJECAGENT cases; benchmark utility measures expected-app invocation rather than full answer correctness. In2000 ASB trials, three designated attacker apps are invoked and classified by the authors as legitimate task matches. Those calls must remain visible rather than be converted to zero raw invocation. AppendixB explicitly denies a formal Python/runtime privacy-soundness guarantee and acknowledges escaped-worker or forged-message risks. Utility varies by model, with relational overall81.0/85.7/66.7% for GPT4o/GPT4.1/hybrid; step accuracy is distinct. Caption, aggregation and runtime discrepancies remain flagged. This supports control/data separation as a defense mechanism under stated trust assumptions, not universal immunity or an isolated effect of agentization. [ACE](../records/ace_comprehensive_summary.json), ace_c01–ace_c18, physical pp.1–18.

None of the24 continuation additions supplies an otherwise matched standalone-LLM/web-agent adversarial comparison. The central comparative question remains unresolved by this addition set.


## Full-corpus continuation — additions25–26: Mind the Web version family

The published 17-page paper and undated 13-page manuscript are versions of one study. Their task-aligned attack pipeline validates candidates by browser interaction before offline SFT/DPO. The manuscript uses approximately1500 candidates/~300 SFT examples/12000 preference pairs and reports61%/82% SFT/DPO ASR; the publication uses2000/~400 and64%/85%. Both compare attack generators rather than matched standalone and agent victims. Duplicated payload/model-transfer rates are not independent replication. [Published record](../records/mind_the_web_the_security_of_web_use_agents_5a834c4e_comprehensive_summary.json), C03–C09, physical pp.5–8; [manuscript record](../records/mind_the_web_the_security_of_web_use_agents_comprehensive_summary.json), claim_03–claim_08, physical pp.4–8.

The attack mechanism couples untrusted task-helpful instructions with existing browser authority. Camera/microphone access requires pre-granted permissions; authenticated operations and local-file access depend on deployment state. Automated rates come from Browser-Use, while the other four agents have manual demonstrations without per-agent repeated-test denominators. Operator P9 requires a manually added permission-bypass phrase. The ParaBank transfer is a demo transaction, and Comet evidence establishes directory access/preparation to transmit rather than confirmed external receipt. These are distinct consequences, not a pooled five-agent harmful-action rate. [Published record](../records/mind_the_web_the_security_of_web_use_agents_5a834c4e_comprehensive_summary.json), C01,C07–C10,C18, physical pp.3–8; [manuscript record](../records/mind_the_web_the_security_of_web_use_agents_comprehensive_summary.json), claim_01,claim_07–claim_11, physical pp.3–12.

The publication's judge reports92% accuracy, but uniform versus stratified sampling and97% positive fulfillment versus94% precision remain inconsistent. A P6 trace scores0.65 despite eventual task completion, so binary ASR can include temporary diversion. The isolated task/action judge and replay/fuzzing defense have qualitative demonstrations without quantified benign utility or adaptive robustness. Its judge calibration and implemented-defense observations are absent from the supplied manuscript and must not be imported into that version. An analyst concern that untrusted action arguments might indirectly influence a judge is an untested hypothesis, not a demonstrated bypass. [Published record](../records/mind_the_web_the_security_of_web_use_agents_5a834c4e_comprehensive_summary.json), C11–C14, physical pp.6,10–11,15–16; [manuscript record](../records/mind_the_web_the_security_of_web_use_agents_comprehensive_summary.json), claim_12,claim_15, physical pp.4–8.

None of the26 continuation additions supplies an otherwise matched standalone-LLM/web-agent adversarial comparison. Completion counts describe canonical output pairs rather than independent study counts. The central comparative question remains unresolved.


## Full-corpus continuation — additions27–31; usage-limit checkpoint

External evidence can influence both factual conclusions and subsequent navigation. POTEMKIN measures contamination and phantom traversal, while TRAP measures click/redirect diversion. These endpoints do not establish completed credential theft, exfiltration or real financial loss. TRAP’s 948 successes among3780 runs are distinct from639 step-cap terminations. Its 77.5% button share uses successful attacks as its denominator; the paired email experiment provides a narrower interface comparison. Table5/Table15 location aggregates remain unresolved. [Record](../records/its_a_trap_task_redirecting_agent_persuasion_benchmark_for_web_agents_comprehensive_summary.json), trap_claim_01, trap_claim_02, trap_claim_03, trap_claim_04, trap_claim_05, trap_claim_06, trap_claim_07, trap_claim_08, trap_claim_09, trap_claim_10, trap_claim_11, trap_claim_12, trap_claim_13, trap_claim_14, trap_claim_15, trap_claim_16.

POTEMKIN’s contamination and engagement rates use different denominators and cohorts. The defense evidence includes utility reductions and inconsistent Table A5/Figure A2 threshold descriptions. Low attack engagement by an error-prone agent is not evidence of stronger security. Conditional retrieval exposure is an important trust-boundary hypothesis, but this is not an otherwise matched standalone-versus-agent experiment. [Record](../records/how_adversarial_environments_mislead_agentic_ai_comprehensive_summary.json), C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16.

Firewalls implement task-aware input/output filtering at tool boundaries, with variable security/utility tradeoffs. AgentDojo residual ASR is nonzero for several model/configuration pairs; lower ASR does not imply restored task completion. Original-versus-fixed ASB comparisons also change defense rows and benchmark/scoring conditions, preventing attribution to a single repair. Fixed attacks do not establish adaptive robustness. [Record](../records/indirect_prompt_injections_are_firewalls_all_you_need_or_stronger_benchmarks_comprehensive_summary.json), C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16.

The serverless study supports resource-amplification concerns through a local load experiment and separate function timings. Its large monetary figures are projections using historical pricing and stated assumptions, not measured victim losses or LLM-agent billing experiments. This offers an architectural analogy for repeated costly actions; applying it to agent loops remains an analyst interpretation requiring direct evaluation. [Record](../records/denial_of_wallet_defining_a_looming_threat_to_serverless_computing_comprehensive_summary.json), C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15.

GUIDE improves post-hoc GUI trajectory evaluation under its tested conditions. Its95.80% industrial accuracy describes the evaluator, not the acting agent’s task success. Hierarchical segmentation can reduce diagnostic context, but neither faithful explanations nor attack robustness follows from evaluator agreement alone. No adversarial defense or matched standalone comparison was tested. [Record](../records/guide_interpretable_gui_agent_evaluation_via_hierarchical_diagnosis_comprehensive_summary.json), guide_claim_01, guide_claim_02, guide_claim_03, guide_claim_04, guide_claim_05, guide_claim_06, guide_claim_07, guide_claim_08, guide_claim_09, guide_claim_10, guide_claim_11, guide_claim_12, guide_claim_13, guide_claim_14.

Across the31 continuation additions, no otherwise matched standalone-LLM/web-agent adversarial comparison was identified. Version-family duplication remains excluded from independent-replication claims. The central comparative research question remains unresolved by this addition set. At that historical usage-limit checkpoint, FocusAgent was pending and contributed no completed-record evidence. It completed in the all112 continuation below.


## All112 continuation — 16 additions after reservation retirement (2026-10-15)

The current92 completed records include16 additions after the user retired B02–B08 reservations for ordinary research and discontinued Phase4B. This is literature analysis, not historical holdout validation. Completion still denotes existing structural/schema/identity/quotation checks and focused analyst review, not independent scientific reproduction. Twenty canonical papers remain; this remains preliminary.

**Exposure, interpretation and consequence require separate endpoints.** Multimodal attacks can succeed at a captioner while failing to achieve the acting agent's objective: Dissecting Adversarial Robustness reports GPT4o caption success92% versus agentASR31% in a selected forced-exposure cohort. Captioner access, self-captioning, victim policy and attack-aware adaptation change the threat model. BrowseSafe instead classifies constructed HTML: its Qwen30BA3B F1.904, precision.978 and recall.841 do not measure stopped harmful agent actions or preserved task utility. ReNNervate uses internal response attention and reports high in-distribution detection accuracy, but unseen cross-task and adaptive attacks retain substantial successes; collecting response attention is not itself proof that a consequential tool action is blocked in time. [Dissecting](../records/dissecting_adversarial_robustness_of_multimodal_lm_agents_comprehensive_summary.json), physical pp.3–8 and appendix; [BrowseSafe](../records/browsesafe_understanding_and_preventing_prompt_injection_within_ai_browser_agents_comprehensive_summary.json), pp.3–11; [ReNNervate](../records/rennervate_comprehensive_summary.json), pp.4–13. Exact claim locators are in the linked records.

**Defense success depends on both architecture and assumptions.** CaMeL separates trusted planning from parsing of untrusted data using restricted programs, capabilities and provenance policies. The formal property does not establish a verified interpreter or unconditional protection for every policy/model configuration. Its main o3 utility77.3 versus native84.5 and nonzero entries in the949-attack table remain visible. SecAlign's preference training hardens structured instruction/data boundaries, reducing main Instruct-model attack rates from89 to1% and97 to8% on the specified208-case security test. The base Llama exception14%, task benchmark losses, and marker-output endpoint preclude universal security or utility claims. These are complementary architectural/model interventions, not controlled evidence that agentization alone increases susceptibility. [CaMeL](../records/defeating_prompt_injections_by_design_comprehensive_summary.json), main pp.3–13 and security/utility appendix; [SecAlign](../records/secalign_defending_against_prompt_injection_with_preference_optimization_comprehensive_summary.json), pp.3–8,12–15.

**Low ASR can coexist with severe utility loss.** FocusAgent's bundled retrieval pruning and warning reduce popup ASR90.4/81.6% to1/0.9%, while corresponding task success is only2/1.8%. A warning-only comparison can have higher utility. MELON tests a different629-attack AgentDojo protocol: GPT4o BU68.04/UA58.78/ASR.24 differs from augmented76.29/68.72/.32. UA here requires both correct task completion and no malicious success; it must not be combined with unrelated marginal success metrics. The paper's probabilistic ensemble bound assumes independent bounded trials and does not automatically certify its deployed single-mask implementation. Proposed calls in masked re-execution are not executed malicious actions. Its66 diagnostic cases do not reconcile directly with22 successes inferred from one table pass. [FocusAgent](../records/focusagent_simple_yet_effective_ways_of_trimming_the_large_context_of_web_agents_comprehensive_summary.json), pp.5–11 and appendix; [MELON](../records/melon_provable_defense_against_indirect_prompt_injection_attacks_in_ai_agents_comprehensive_summary.json), pp.3–9,13–20.

**Resource abuse has multiple evidence levels.** IAL-SCAN identifies potential code-level infinite agent loops:68 confirmed among74 alerts supports alert precision, not a population vulnerability rate, full recall or observed victim bills. Beyond Max Tokens directly measures tool-mediated output-token amplification in stubbed environments. Ratios depend on model/tool/task and its main six-call target cannot be pooled with a one-call cap protocol. Output tokens, total reported energy, cache occupancy and concurrent benign throughput are different outcomes; historical-price projections would be different again. Hard caps still bound calls/tokens. The visibly decreasing ASR with increasing displayed caps and table transcription issues are preserved rather than replaced by the paper's contrary narrative. [IAL-SCAN](../records/when_agents_do_not_stop_uncovering_infinite_agentic_loops_in_llm_agents_comprehensive_summary.json), pp.3–10; [Beyond Max Tokens](../records/beyond_max_tokens_stealthy_resource_amplification_via_tool_calling_chains_in_llm_agents_comprehensive_summary.json), pp.3–11.

**Benign difficulty does not measure adversarial compromise.** WorkArena++'s composed workflows, AndroidWorld's randomized mobile tasks and Odysseys' live long-horizon tasks expose memory, planning, observation and action demands. Their task failures are not attack successes. Human cohorts, per-model action scaffolds, task subsets and budgets differ. Odysseys' Opus perfect-task rate rises from44.5% at100 model calls to76.5% at200, qualifying any general plateau claim; its Qwen extension uses only76 matched hard tasks. An archived June2024 schedule receiving a successful rubric judgment does not establish a correct current answer. These benchmarks motivate controlled security/utility studies without supplying them. [WorkArena++](../records/workarena_plus_comprehensive_summary.json), pp.3–9 and appendix; [AndroidWorld](../records/androidworld_comprehensive_summary.json), pp.3–10 and appendix; [Odysseys](../records/odysseys_benchmarking_web_agents_on_realistic_long_horizon_tasks_comprehensive_summary.json), pp.5–10,22–29.

**Traditional crawling provides bounded analogies.** Crawl Policy studies conditional URL-availability relevance ceilings, and Web Crawling surveys frontier, deduplication, refresh, spam and trap mechanisms. Neither reports LLM prompt-injection susceptibility. Measuring What the Crawler Sees estimates crawler-visible persistence and coverage under a dynamic-urn/core-shell model. Its cross-projection comparison is not external ground truth; plotted fit triples disagree, and normalization, curvature and asymptotic-inversion concerns remain analyst mathematical qualifications. Policy choice, true population change, missed sampling and identifier dormancy require separate causal tests. Applying these ideas to agent loops or trust selection is an interpretation, not a tested defense. [Crawl Policy](../records/the_impact_of_crawl_policy_on_web_search_effectiveness_comprehensive_summary.json), pp.3–7; [Web Crawling](../records/web_crawling_comprehensive_summary.json), sections and physical-page locators in record; [Measuring](../records/measuring_what_the_crawler_sees_discovery_curves_core_persistence_and_shell_dynamics_in_longitudinal_web_crawls_comprehensive_summary.json), pp.3–13.

**Coverage gaps are conditional on the taxonomy and audited snapshot.** Talk Is (Not) Cheap maps six benchmarks to six of24 target/technique cells when partial coverage counts, or four cells without partials. This is neither25% of real-world risks nor evidence75% of attacks succeed. InjecAgent and AgentDojo occupy the same two cells, contradicting a literal zero-overlap claim. The507 leaves include author-added placeholders; paper mentions, technique groups, unique groups and novelty counts have different denominators and unresolved discrepancies. No proposed disruption benchmark is actually run here. [Taxonomy audit](../records/talk_is_not_cheap_a_taxonomy_and_benchmark_coverage_audit_for_llm_attacks_comprehensive_summary.json), pp.3–10,15–27.

Across these16 additions, no controlled security experiment compares otherwise matched standalone-LLM and web-agent configurations. This is an observation about this addition set and the supplied evidence, not a claim that none exists anywhere. The core research question remains unresolved: expanded exposure, persistent state and action authority are supported mechanisms, while a universal increase in attack susceptibility requires matched trials separating backbone, task, exposure, permissions, attacker control, budget and outcome definition. Important open questions include adaptive robustness, accurate user-intent and trust labels, action-level harm verification, long-horizon effects, real utility/cost tradeoffs, and risk estimation under changing environments. Canonical output counts remain distinct from independent study counts; AgentVigil/AgentFuzzer and both Mind the Web versions retain their duplication qualifications.


### Historical93-record snapshot — Prismata and the previous usage-limit stop

Prismata combines a task-only origin policy, structural-provenance labeling, top-down Biba propagation, masked observations and an identifier-action gate. Its informal confinement argument depends on reliable trusted structure and the permitted action interface; text masking does not establish screenshot safety or correctness of within-permission decisions. Across three main attack templates, meanASR85.5 to0.7% accompanies attacked task success4.5 to23.0%, while benign task success falls29.9 to26.6%. The average is not a universal pooled risk estimate, and link/form interaction endpoints should not be promoted into observed credit-card theft. The21-goal WASP comparison and20-task adaptive experiments have different protocols and denominators. [Prismata](../records/prismata_confining_cross_site_prompt_injection_in_web_agents_comprehensive_summary.json), physical pp.3–10,15.

The residual15 structurally uninformative actionable paths among90,408 labeled untrusted paths are conditional on discarding79 links under assumptions including non-state-changing same-origin GET requests. This is a structural sample fraction, not a probability of compromise. Language-model labels and a single-expert20-observation check do not establish universally correct provenance. Reported component request durations sum to greater computational service demand, but asynchronous execution prevents reading that sum directly as measured end-to-end wall latency. Cached cost$1.105 to$1.623 is across20 tasks, not per task; different cache savings may overlap. These costs and the benign-utility loss remain part of the defense tradeoff. [Prismata](../records/prismata_confining_cross_site_prompt_injection_in_web_agents_comprehensive_summary.json), physical pp.5–10.

Prismata supplies no otherwise matched standalone-LLM/web-agent security experiment. Across the17 additions since the all112 restart, the comparative question remains unresolved under that criterion. SnapGuard encountered an actual OPERATIONAL_USAGE_LIMIT before producing a validated record and contributes no completed evidence here. Processing stopped further model dispatch; preliminary source preparations for pending papers remain outside this synthesis. The92-record preceding addendum is a historical batch boundary; current coverage is93 canonical output pairs,19 pending,0 excluded,0 failed. This is an operational interruption, not a scientific failure.

## Final19 continuation — evidence qualifications from the first eight additions

SnapGuard: Screenshot detector; local variance plus OCR/rules. 948 benign/2185 malicious images; macro FPR .09, mean TPR .66, F1 .75; CPU1.81s. Not a live-agent action/utility test; target .05 FPR differs from observed configuration rates; missing appendices; template venue metadata. [Source record, snapguard_c01–c13; pp.1–10](../records/snapguard_lightweight_prompt_injection_detection_for_screenshot_based_web_agents_comprehensive_summary.json).

Untrusted Content Masking: Owner-labeled DOM masking; isolated typed-answer queries. 12 strengthened WASP goals: UCM0 ASR versus17±8 baseline; main utility uses three different models/100 tasks. Guarantee assumes correct complete labels; four hard templates use human-approved free text; potential query overrides are simulated; no matched standalone comparator. [Source record, C01–C12; pp.1–25](../records/untrusted_content_masking_for_web_agents_with_security_guarantees_comprehensive_summary.json).

WebAgentGuard: Parallel reasoning guard on HTML/screenshot/goal. Integrated attack rates fall in reported settings; 8B in-domain recall98.4%; mean guard3.24s. Mean latency below agent mean does not prove zero paired wall-time overhead; positive-only benchmarks give recall, not full accuracy; utility losses remain; fixed-suffix test is not adaptive robustness. [Source record, C01–C14; pp.1–18](../records/webagentguard_a_reasoning_driven_guard_model_for_detecting_prompt_injection_attacks_in_web_agents_comprehensive_summary.json).

Long-Horizon Mirage: Benign multi-domain horizon extension and failure diagnosis. Over700 tasks/3100 trajectories; three runs with mean±SD. Caps and compositional conjunctions confound horizon; examples include authored micro-scenarios; annotator protocol conflicts; benign failure is not successful attack. [Source record, claim_01–claim_14; pp.1–47](../records/the_long_horizon_task_mirage_diagnosing_where_and_why_agentic_systems_break_comprehensive_summary.json).

WebChoreArena: Tedious benign web tasks with memory/calculation demands. 532 instances/117 templates; BrowserGym GPT5 task success48.3%. Human50.2% uses117 template instances, not same532; frameworks have different action budgets; ablations and live-web set use different cohorts; no adversarial test. [Source record, C01–C14; pp.1–29](../records/webchorearena_evaluating_web_browsing_agents_on_realistic_tedious_web_tasks_comprehensive_summary.json).

Autonomy-Induced Security Risks: Survey; autonomy taxonomy and proposed R2A2 controls. No original attack/utility experiment; expected CMDP constraint is conditional. Autonomy levels differ from defense levels; expected cost budget does not guarantee zero unsafe actions; proposed combined stack untested; no matched standalone experiment. [Source record, C01–C15; pp.1–20](../records/a_survey_on_autonomy_induced_security_risks_in_large_model_based_agents_comprehensive_summary.json).

TrustAgent: Survey of intrinsic/extrinsic components and five trust dimensions. 119 references include duplicate/version entries; no new attack experiment. Citation/benchmark attribution errors flagged; secondary metrics remain separate; architectural hierarchy is not measured security ordering; no own matched comparison. [Source record, C01–C14; pp.1–11](../records/a_survey_on_trustworthy_llm_agents_threats_and_countermeasures_comprehensive_summary.json).

Layered Attack Surface Model: Seven layers by four temporal classes; literature/defense mapping. 116 papers/144 reported assignments; selected zone9/144; seven zero-defense cells. Assignments not incident risk; multiplicities imply146; table/figure defense counts conflict; theorem assumes unchanged other-layer distributions and gives no incremental discrimination, not zero absolute alerts; supplements absent. [Source record, claim_01_architecture–claim_14_multiplicity; pp.1–58](../records/a_systematic_survey_of_security_threats_and_defenses_in_llm_based_ai_agents_a_layered_attack_surface_framework_comprehensive_summary.json).

Together these additions support architectural explanations and conditional defenses, not a universal numerical vulnerability gap. None supplies its own otherwise matched standalone-LLM versus web-agent adversarial experiment. Secondary tool-access comparisons in the surveys require the original protocols before treating configurations as matched.

### Final19 batch5: design scope and offensive capability

SoK Attack and Defense Landscape: 128-paper review; seven continuous design dimensions; three adversary classes/six vectors. No new common-protocol attack/defense experiment. Exposure and consequences are different; nine versus seven risks and three versus four defense categories conflict; cutoff versus late citation unresolved; no own matched standalone comparator. [Source record and claim page locators](../records/sok_attack_and_defense_landscape_of_agentic_ai_systems_comprehensive_summary.json).

AWE: Context-specialized autonomous web-app pentester; memory reset per target. 54/104 versus published MAPTA80/104; mean solve53.1s versus190.8s; XSS20/23 versus13/23. Different backbones and published baseline prevent architecture attribution; $7.73/54≈.143 differs from reported.113; no own test of agents susceptibility to injection. [Source record and claim page locators](../records/awe_comprehensive_summary.json).


### Final19 batch6: component backdoors and deceptive interfaces

BackdoorAgent: Component replacement across planning, memory and tools; instrumented runtime. GPT aggregate ASR43.58/77.97/60.28%; DeepSeek tools42.20 exceeds memory38.91. No dataset sizes, seeds or aggregation weights; abstract persistence is not a longitudinal measure; high ASR can coexist with high task ACC; prose/table mismatches flagged. [Source record, C01 through C14 and physical page locators](../records/backdooragent_comprehensive_summary.json).

Don’t Click That / DUDE: Static screenshot grounding plus evaluator/reflection; stage1 training separately ablated. Qwen SR6.5→33.5/DFR2→0; UI-TARS SR43.5→35.5 with evaluator. Trap click is not completed harm;200/210 test sizes and3-step versus larger counts conflict; stage gains not uniform; unexplained53.8% headline; no own matched standalone comparison. [Source record, claim_01 through claim_14 and physical page locators](../records/dont_click_that_teaching_web_agents_to_resist_deceptive_interfaces_comprehensive_summary.json).


### Final19 batch7: attack environments and conventional crawling

DoomArena: Environment wrappers inject configurable attacks into tau-Bench, WebArena and OSWorld. Browser judge conditions report0 ASR and0 attacked-task success; combined attacks have narrower triggered cohorts. Different environments/goals/control and model versions are not matched; URL redirect is not proven exfiltration; restricted LlamaGuard category; no own standalone comparison. [Source record, C01 through C14 and physical page locators](../records/doomarena_a_framework_for_testing_ai_agents_against_evolving_security_threats_comprehensive_summary.json).

EvoCrawl: Classical evolutionary web scanner with server DB feedback, manual users and fitness weights. Reported59% mean coverage increase; known XSS6/8 versus2/8;8 new reports have differing vendor/privilege status. Coverage is not application-line fraction; Drupal97151 versus61303 and Dokuwiki ablation−21 conflict with universal prose; privileged feedback; historical version/fix conflicts; no LLM comparator. [Source record, evocrawl_c01 through evocrawl_c14 and physical page locators](../records/evocrawl_comprehensive_summary.json).


### Final19 batch8: API capability and indirect-injection evaluation

Gorilla: Fine-tuned Llama7B with API cards, retrieval-aware training and AST evaluation. No-document accuracy59.13/71.68/83.79 across catalogs;100 manual examples78% API accuracy/72% program execution. Capability not attack success; API counts and metric tables conflict; HF criteria differ by model; headline gains use different baselines; no adversarial standalone/agent experiment. [Source record, gorilla_c01 through gorilla_c13 and physical page locators](../records/gorilla_comprehensive_summary.json).

InjecAgent: Forced compromised tool response;1054 base/enhanced cases; simulated intermediate data-stealing output. GPT4 ASR-valid23.6→47 versus ASR-all23.3→46.8; Llama70B ASR-valid86.9/88.2. Parsed harmful calls are not production delivery; validity changes denominator; no full user-task utility; function-calling prose reverses model rates; no matched standalone comparator. [Source record, C01 through C16 and physical page locators](../records/injecagent_benchmarking_indirect_prompt_injections_in_tool_integrated_large_language_model_agents_comprehensive_summary.json).


### Final19 batch9: executable skills and browsing implementation boundaries

SkillTrojan: Persistent installed executable packages; fragmented encrypted payload and runtime reconstruction. GPT5.2 EHR ACC89.3/ASR97.2; open-model native-stack accuracy losses1.9–6pp. Stronger attacker access than page editing; absent EHR N and uncertainty; QwenVL ASR26.7 below AgentPoison37.6; static scanner results are narrow; no matched standalone comparison. [Source record, C01 through C15 and physical page locators](../records/skilltrojan_comprehensive_summary.json).

Hidden Dangers of Browsing AI Agents: MAESTRO mapping plus BrowserUse authorization and credential-leak cases. Author reports URL-check CVE2025-47241 in.1.44 fixed.1.45; no repeated-trial ASR. Historical fix status not checked live; URL bypass and prompt injection are distinct components; sample PoC does not measure combined-chain reliability; cited capability/defense rates are secondary; no matched standalone test. [Source record, C01 through C14 and physical page locators](../records/the_hidden_dangers_of_browsing_ai_agents_comprehensive_summary.json).


### Final19 batch10: YuraScanner — final canonical record

YuraScanner combines LLM-generated workflows with conventional vulnerability detection. Of2361 generated tasks,1818 are valid,667 fully complete and448 partially complete;61.3% combines full and partial, whereas full completion is36.69% of valid or28.25% of all generated tasks. The55.19% form gain augments baseline coverage with Yura-only discoveries; it does not establish Yura-alone superiority. The15 reports represent13 unique issues, with vendor/privilege and potential-XSS qualifications. This measures attacks on web applications, not attacks compromising the agent. [Source record, yura_c01 through yura_c15; physical pp.1–16](../records/yurascanner_comprehensive_summary.json).

## Full112 completion — cross-paper implications and unresolved comparison

**Analyst synthesis:** the final19 additions reinforce distinct exposure, authority and consequence pathways. Browser screenshots/DOM can carry instructions; memories and installed executable skills extend persistence; tool execution gives an output operational effect. These mechanisms do not imply that every added component raises attack susceptibility under every protocol. Conventional scanner and pentester findings describe offensive capability against applications, while WebChoreArena/Mirage describe benign task difficulty. They cannot serve as comparative agent-compromise rates. [UCM, C01–C12, pp.1–25](../records/untrusted_content_masking_for_web_agents_with_security_guarantees_comprehensive_summary.json), [SkillTrojan, C01–C15, pp.1–14](../records/skilltrojan_comprehensive_summary.json), [Mirage, claim_01–14, pp.1–47](../records/the_long_horizon_task_mirage_diagnosing_where_and_why_agentic_systems_break_comprehensive_summary.json).

Security endpoints remain distinct: SnapGuard/WebAgentGuard classification metrics do not by themselves prove prevented tool-action harm; DUDE observes deceptive screenshot clicks; InjecAgent parses calls with simulated intermediate retrieval; SkillTrojan uses reconstruction/execution markers and specified side effects. DoomArena's redirects and task-specific goals have their own definitions. Rates must retain exposure, attacker privileges, validity denominator, budget and actual outcome. [SnapGuard, snapguard_c01–13, pp.1–10](../records/snapguard_lightweight_prompt_injection_detection_for_screenshot_based_web_agents_comprehensive_summary.json), [DUDE, claim_01–14, pp.1–23](../records/dont_click_that_teaching_web_agents_to_resist_deceptive_interfaces_comprehensive_summary.json), [InjecAgent, C01–C16, pp.1–36](../records/injecagent_benchmarking_indirect_prompt_injections_in_tool_integrated_large_language_model_agents_comprehensive_summary.json).

Defense evidence is conditional. UCM's control-flow separation assumes correct labels and restricted query outputs; hard-task recovery can require user-approved free text. Parallel guard mean runtimes do not prove zero added latency for every action. DoomArena demonstrates that aborting can suppress both attacks and useful completion; DUDE and SkillTrojan retain utility losses against relevant controls. These observations motivate matched security/utility and adaptive evaluations; they do not validate a universal combined defense stack. [UCM, C01–C12, pp.1–25](../records/untrusted_content_masking_for_web_agents_with_security_guarantees_comprehensive_summary.json), [WebAgentGuard, C01–C14, pp.1–18](../records/webagentguard_a_reasoning_driven_guard_model_for_detecting_prompt_injection_attacks_in_web_agents_comprehensive_summary.json), [DoomArena, C01–C14, pp.1–25](../records/doomarena_a_framework_for_testing_ai_agents_against_evolving_security_threats_comprehensive_summary.json).

Survey architecture/temporality maps help formulate research questions, but paper-cell coverage is not incidence, severity or proven protection. LASM's9/144 assignments and seven zero-defense cells have coding/count conflicts; its conditional theorem requires unchanged observations at other layers. Autonomy's expected-cost constraints do not guarantee zero unsafe actions, and TrustAgent's reference count is not a count of independent experiments. Longitudinal compromise, calibrated action harm, correct provenance labeling and useful adaptive defenses remain open questions. [LASM, claim_01_architecture through claim_14_multiplicity, pp.1–58](../records/a_systematic_survey_of_security_threats_and_defenses_in_llm_based_ai_agents_a_layered_attack_surface_framework_comprehensive_summary.json), [Autonomy, C01–C15, pp.1–20](../records/a_survey_on_autonomy_induced_security_risks_in_large_model_based_agents_comprehensive_summary.json), [TrustAgent, C01–C14, pp.1–11](../records/a_survey_on_trustworthy_llm_agents_threats_and_countermeasures_comprehensive_summary.json).

**Controlled comparison status:** none of the final19 papers supplies its own otherwise matched standalone-LLM versus web-agent adversarial security experiment. The reviewed corpus supports mechanisms and scoped attack/defense findings, but does not establish a universal causal susceptibility multiplier. Secondary tool-access comparisons require the original protocols before accepting matched configurations. This is a conclusion about the reviewed evidence, not a claim that no such study exists elsewhere. Attack exposure, susceptibility and consequences must be measured separately.

**Version and history qualification:**112 canonical records are not112 independent studies. AgentVigil/AgentFuzzer and both Mind the Web versions retain their existing family qualifications; five exact archived duplicates remain outside the112. Ordinary Research Mode access after B02–B08 retirement does not validate the historical experiment. Earlier usage-limit snapshots above are preserved history and are superseded by this completion state. These are source-grounded analyst summaries with lightweight validation, not independent human scientific verification.
