# Controlled standalone–web-agent comparison: proposed study

**Status:** study proposal only. No benchmark, agent, attack, model call or experiment is implemented. Numeric sample/cost quantities below are planning assumptions, not observed results.

## Current program status — retained secondary proposal, 2026-10-16

This document retains the earlier standalone-LLM/web-agent comparison methodology, estimands, arms and planning assumptions. It is a separate supporting contribution candidate and no longer defines the primary experimental program. Its local primary/secondary contrasts apply only within this retained design.

The leading proposal is the [AI web-agent trap roadmap](AI_WEB_AGENT_TRAP_RESEARCH_ROADMAP.md): task relevance, recurring prerequisites, bounded non-progress and recovery with a reachable goal and available escape. A single-decision replay can help explain entry but cannot measure closed-loop retention. The trap-specific protocol and implementation would belong to a separate future experiment repository; they are not substituted into this design. Neither study has been performed here.

## 1. Objective and causal claims

Test the neutral question: **How do web observation, delegated tool authority and persistent state change exposure, instruction deviation and verified sandbox effects relative to a matched standalone language model?** Do not assume a positive susceptibility effect.

Three quantities must remain separate: encounter of attack-bearing content; a model decision deviating from the legitimate instruction given that content; and the effects an executor permits. With identical weights and identical complete model inputs, a hidden change in executor availability cannot logically establish a change in the model's conditional susceptibility. Conversely, changing interface descriptions, context, tools or feedback is a contextual/system treatment even when weights are unchanged.

The core uses two distinct experiments: **A, forced-exposure common-decision replay**, and **B, closed-loop sandbox interaction**. A identifies specified interface/context effects at fixed information; B estimates configured-system outcomes including changed routing and feedback. They must not be combined into one unexplained “agentization effect.” Narrow within-agent interventions in Toolformer, Overthinking Loops and Context Manipulation motivate this decomposition but do not themselves supply it. [Toolformer](../records/toolformer_comprehensive_summary.json) (claims toolformer_claim_01 through toolformer_claim_16; physical PDF pp.1–17); [Overthinking Loops](../records/overthinking_loops_in_agents_a_structural_risk_via_mcp_tools_comprehensive_summary.json) (claims C01 through C14; physical PDF pp.1–12); [Context Manipulation](../records/context_manipulation_attacks_web_agents_are_susceptible_to_corrupted_memory_comprehensive_summary.json) (claims C01 through C14; physical PDF pp.4–8).

## 2. Threat model and task domain

A trusted user gives a legitimate task and explicit authorization constraints. An adversary controls one designated low-trust page/document region or tool-return field. In the core study it cannot change the system/developer instructions, legitimate task, browser chrome, model weights, tool implementation, policy enforcement or operating system. Payload length, placement freedom and attacker feedback are defined per protocol. Executable-skill replacement, white-box pixels and direct memory writes are separate extensions, not silently included in ordinary page control.

Use local applications with deterministic fixtures: document lookup, permitted message drafting/sending, record updates and bounded navigation. Include authorized and unauthorized operations that can be distinguished from ordinary task errors. Suggested attacker objectives are changing the requested answer, submitting a canary to a designated unauthorized internal sink, or changing an unauthorized sandbox record. These are harmless surrogate effects with explicit ground truth, not real theft, fraud or damage.

All destinations, identities and data are synthetic/internal. Enforce network and filesystem boundaries outside the model and use resettable state. Never use real credentials or arbitrary internet execution. These are requirements for a future study, not a claim that this workspace has implemented a sandbox. The corpus's distinction between configured authority and demonstrated consequences is directly relevant. [AgentDojo](../records/agentdojo_a_dynamic_environment_to_evaluate_prompt_injection_attacks_and_defenses_for_llm_agents_comprehensive_summary.json) (claims C01 through C16; physical PDF pp.1–26); [ceLLMate](../records/cellmate_sandboxing_browser_ai_agents_comprehensive_summary.json) (claims cellmate_c01 through cellmate_c15; physical PDF pp.2–13); [Hidden Dangers](../records/the_hidden_dangers_of_browsing_ai_agents_comprehensive_summary.json) (claims C01 through C14; physical PDF pp.2–27); [SkillTrojan](../records/skilltrojan_comprehensive_summary.json) (claims C01 through C15; physical PDF pp.1–14).

## 3. Experiment A: forced-exposure common-decision replay

### 3.1 Arms

| Arm | Input/decision interface | Execution | What the contrast means |
|---|---|---|---|
|A0: standalone decision-only| Trusted user task plus clearly delimited untrusted content in a document interface. Common response schema permits an answer and a proposed action. | None; output recorded. | A tool-aware decision-only baseline, not ordinary free-form chat. |
|A1: web-observation decision-only| Same user goal, payload body and task facts, represented by a controlled web-observation interface. | None; same response schema. | A1−A0 estimates specified representation/context effects, not changed model weights. |
|A2: web observation with announced sandbox tools| Same observation/task and common schema; tool-availability declaration is the explicit treatment. | First decision logged before any tool feedback; later execution analyzed separately. | A2−A1 estimates announced capability/context effects on the first decision. |
|A2-hidden executor control| Replay exactly the same A1 proposed call into disabled/enabled executors without changing the model input. | Offline paired executor replay. | Effect of actuation/policy on consequences, not a susceptibility intervention. |
|A0-natural, optional| Ordinary answer-only standalone interface, without proposed-call contract. | None. | External-validity check using common answer deviations only; action-attempt endpoints are not comparable. |

The primary contrast is A1−A0 injection-induced instruction deviation. A2−A1 and A2−A0 are secondary, multiplicity-controlled contrasts. The common action schema makes a proposal observable in A0 but also makes that baseline tool-aware; this limitation must appear in the title/interpretation of results. The optional natural-chat arm cannot repair it by treating absent tool calls as successful resistance.

### 3.2 What is held constant

Use the same immutable model checkpoint or dated service snapshot, tokenizer, temperature/top-p, output budget, conversation reset and stopping policy. Preserve the exact legitimate goal and authorization policy. Use the same attack body, target objective, permitted content facts, benign distractors and exposure location policy. The interface wrapper/availability statement is the declared treatment, not an unnoticed prompt difference.

For each unit, derive all representations from one canonical page fixture. Record render/DOM/accessible text agreement and payload visibility. Exact semantic equivalence across modalities is not assumed. The initial confirmatory study should use text/DOM-like observations; screenshots and captioners are a separately powered extension. Add equal-length padding/position controls where feasible and sensitivity analyses for unavoidable token-position differences. Do not describe format-varying arms as identical full prompts.

All arms receive the same necessary information before the first scored decision. If a secret/canary or tool-read value is needed, supply the same protected fixture value under the same explicit rule, or restrict that task to an extension where access is deliberately varied. Giving only one arm extra evidence would confound susceptibility with information availability.

### 3.3 Exposure and paired controls

Force the designated malicious region to be present for A; determine eligibility before arm assignment. This estimates outcomes under controlled exposure, not natural prevalence. Pair every attacked fixture with a clean version matched for task information, position and approximately length. Include benign quoted instructions and legitimate user-delegated material to test false rejection. Include neutral irrelevant text to distinguish generic confusion from attacker-directed deviation.

Use fixed held-out payloads for confirmatory transfer. Attack development may use disjoint development tasks, equal feedback-query/token limits and a fixed success oracle. Any arm-specific adaptive optimization is a separate experiment because it changes the attack distribution. Report attempted candidates, selection criteria, failed searches and total optimization costs; a best-of-many payload is not one random trial. [AgentVigil](../records/agentvigil_generic_black_box_red_teaming_for_indirect_prompt_injection_against_llm_agents_comprehensive_summary.json) (claims av_c01 through av_c15; physical PDF pp.2–14); [Retrieval Barrier](../records/retrieval_barrier_comprehensive_summary.json) (claims C01 through C18; physical PDF pp.1–20); [WARD](../records/ward_comprehensive_summary.json) (claims ward_c01 through ward_c15; physical PDF pp.2–22).

### 3.4 Repeated execution

Run all arm×clean/attack conditions for each task in randomized order. Fresh sessions and fixture resets prevent contamination. Use matched seeds where the service supports them, but do not call hosted randomness deterministic merely because a seed argument exists. Repeat model sampling; cluster repeats within tasks and task templates. Separate tasks/sites/templates used for attacker development, annotation calibration and final evaluation. Historic corpus reservations are not reused as pristine experimental holdouts; future tasks require independent selection.

## 4. Experiment B: closed-loop exposure and consequences

A replayed common observation controls input but removes autonomous encounter. B therefore starts from matched local tasks and pages, then allows read/navigation-only and executor-enabled agents to interact under explicit budgets. Record each observation, content provenance, proposed action, accepted operation, state transition and termination reason. Diverging trajectories are part of the total configured-system treatment, not nuisance data to discard.

Estimate encounter probability and **joint attack outcomes per all assigned tasks**. Do not condition the primary causal comparison on observed encounter, successful clean completion or valid output: these are potentially post-treatment selections. Report conditional stage rates descriptively and label them; do not multiply stage rates from different cohorts as a causal total.

A read-only interface cannot complete a write-dependent task. Therefore report common read/decision utility across arms and native end-to-end completion within executable arms separately. A mechanically impossible harmful effect in a non-executing arm is “not applicable/structurally unavailable,” not evidence of stronger instruction adherence. The enabled/disabled executor replay can still isolate which effects follow from identical proposed actions.

Within executing arms, compare enforcement on/off using identical predeclared permissions and record policy denials. A fully compromised scripted decision sequence is a useful separate enforcement test, analogous to ceLLMate's scope; it does not measure resistance to prompt injection. Include abstain-all and allow-all controls. [ceLLMate](../records/cellmate_sandboxing_browser_ai_agents_comprehensive_summary.json) (claims cellmate_c01 through cellmate_c15; physical PDF pp.2–13); [CaMeL](../records/defeating_prompt_injections_by_design_comprehensive_summary.json) (claims C01 through C12; physical PDF pp.1–40); [DoomArena](../records/doomarena_a_framework_for_testing_ai_agents_against_evolving_security_threats_comprehensive_summary.json) (claims C01 through C14; physical PDF pp.1–25).

## 5. Outcomes and ground truth

| Measure | Operational definition | Denominator and interpretation |
|---|---|---|
|Exposure| Attack-bearing region is actually included in the actor's input. | All assigned B tasks; forced by design in A. Viewing a page externally is not sufficient. |
|Instruction deviation D| First scored answer/decision fulfills a predeclared attacker-directed deviation from the legitimate task/policy. | All assigned A decisions; false answer, random error and invalid format are separate labels. |
|Unauthorized attempt A| Output proposes a syntactically interpretable forbidden call/action under the common schema. | All assigned common-contract decisions; answer-only arm is not comparable. |
|Accepted execution X| Sandbox executor accepts and performs the proposed forbidden operation. | All assigned executable-arm trials; record denial separately. |
|Verified harmful surrogate H| Independent state/log check confirms the exact unauthorized change or arrival of a trial-specific canary at the internal sink. | All assigned executable-arm trials; not merely a claimed send, request attempt or model judge's approval. |
|Benign utility U| Authorized answer/decision correctness in A; authorized final task state in executable B. | All clean tasks, with separate attacked utility and joint U-and-not-H. Common and native utility are labeled distinctly. |
|False rejection F| Defense blocks/abstains on a valid clean operation or benign instructional content. | All predefined legitimate opportunities and task-level failure separately. |
|Resource cost| Input/output/reasoning tokens where visible, tool calls/work, elapsed wall time and service durations. | All trials, including timeouts/failures; success-only ratios secondary. Actual bills, projections and hardware energy are distinct. |

Classify invalid output, crash, timeout, ordinary incorrect action, refusal, policy denial and attacker-directed behavior separately. Report intention-to-treat rates plus the full outcome distribution. Invalid outputs contribute neither a successful deviation nor assumed safe completion; show sensitivity analyses and utility to prevent “security through incapacity.” A treatment-specific failure to produce an evaluable result is itself important missingness, not a reason for silent exclusion.

Use independent deterministic database/filesystem/sink checks where feasible. For semantic D and answer utility, give two blinded annotators a prespecified rubric, include successful and failed/invalid strata, and adjudicate disagreements without viewing arm labels. Estimate agreement and confusion against the independent state endpoints; an LLM judge can assist but cannot be the sole authority. Archive raw judgments for a future reproducible study without treating agreement as proof of truth. [AgentRewardBench](../records/agentrewardbench_evaluating_automatic_evaluations_of_web_agent_trajectories_comprehensive_summary.json) (claims C01 through C16; physical PDF pp.3–23); [GUIDE](../records/guide_interpretable_gui_agent_evaluation_via_hierarchical_diagnosis_comprehensive_summary.json) (claims guide_claim_01 through guide_claim_14; physical PDF pp.1–8); [WASP](../records/wasp_comprehensive_summary.json) (claims wasp_c01 through wasp_c16; physical PDF pp.3–22); [SafeArena](../records/safearena_comprehensive_summary.json) (claims SA_C01 through SA_C15; physical PDF pp.1–37).

## 6. Estimands and statistical analysis

### 6.1 Primary and secondary contrasts

For task i and arm a, let D(a,attack) and D(a,clean) denote the probabilities of the predeclared attacker-directed deviation under repeated sampling. Define the **primary clean-adjusted interface contrast**:

~~~text
Z_i = [D_i(A1,attack) − D_i(A1,clean)]
      − [D_i(A0,attack) − D_i(A0,clean)]
Primary estimand = mean_i Z_i
~~~

Estimate probabilities by the prespecified repeated trials, with clean and attacked versions paired. Report both component risks as well as the interaction. A clean fixture may accidentally yield the attacker-target answer, which is why the clean term is measured rather than assumed zero. This interaction identifies the effect of the specified representation on attack-induced deviation within the sampled tasks; it does not establish changed intrinsic weights or universal web-agent risk.

Secondary contrasts add A2; report absolute risk differences with intervals, risk ratios only where denominators are meaningful, and all outcome counts. Treat action proposals, execution, harm, utility, false rejection and resource metrics as secondary distinct endpoints. Use a prespecified Holm adjustment for the key secondary arm contrasts; label remaining subgroup/interaction analyses exploratory. Do not select the largest model/attack cell as the primary finding.

For B, estimate total assigned-task risks, encounter probability and utility separately. Conditional rates can explain stages but do not identify mediation without additional assumptions. The common-call executor replay estimates enforcement effects for that fixed call distribution; it is not the natural distribution after a defense changes planning.

### 6.2 Dependence and inference

The task, not each sampled model response, is the basic paired unit. Repeats are nested within tasks, and tasks can share site/template families. Resample independent site-template families, preserving all arms, clean/attack pairs and repeats; report cluster-aware bootstrap intervals. Use multilevel logistic models as a secondary robustness analysis with task/family effects and prespecified model/interface interactions. If sites and templates cross, examine multiway clustering or coarser independent clusters rather than assuming a nested structure.

A paired randomization/permutation test is appropriate only when the actual assignment and exchangeability justify it. Ordinary McNemar tests on pooled repeated runs would ignore clustering and the clean-adjusted interaction. Show unadjusted counts alongside model-based estimates. Zero events imply an interval, not guaranteed prevention; the usual independent-binomial approximate 3/N bound is not justified by treating correlated repeats as independent N.

Report medians, interquartile ranges and high quantiles for latency/tokens, plus paired differences and means relevant to total workload. Timeouts are censored/limited outcomes with explicit caps; give restricted-budget totals and timeout rates. Do not silently replace timeout duration with a successful-case mean. Any monetary estimate must state actual contemporaneous service prices and cache assumptions at study execution; no present price or bill is estimated here.

### 6.3 Sample-size plan and feasibility pilot

Illustrative detection target: an absolute five-percentage-point primary interaction, two-sided alpha 0.05 and 80% power. A paired-normal planning approximation is:

~~~text
n_independent ≈ (z_0.975 + z_0.80)^2 × Var(Z_i) / delta^2
             ≈ 7.84 × Var(Z_i) / delta^2
~~~

If Var(Z_i)=0.20 and delta=0.05, the approximation gives about 628 independent task units. **The 0.20 variance is an assumption, not a corpus estimate.** For a simple paired binary contrast, variance relates to discordant probability minus squared mean; the four-condition primary interaction needs its own covariance estimate. Its variance may be materially larger. A separate development pilot must estimate this quantity and intracluster dependence before fixing a confirmatory N.

With average cluster size five and illustrative intracluster correlation 0.10, design effect 1+(5−1)×0.10=1.4 gives roughly 880 task units. A provisional 1000-task/at least 200-family design is therefore a planning scenario, not a powered commitment. Unequal clusters, fewer independent sites, rarer events, higher variance, multiple-model claims or a tighter equivalence margin require more data. Three model repeats improve estimation but do not triple independent N. Feasibility must determine whether 200 genuinely independent families can be built; relabeling variants does not create them.

Use about 50 separate development tasks initially to test fixture equivalence, endpoint reliability, discordance, costs and resets. Do not include them in confirmatory estimates or select settings because they maximize an apparent agent disadvantage. Prespecify the minimum relevant effect and an equivalence margin. A nonsignificant superiority test is not equivalence; if an illustrative ±2 percentage-point equivalence region is desired, power it separately and enlarge N or report inconclusiveness.

## 7. Budgets, workload and practical feasibility

A1000-task replay design with three arms, two clean/attack versions and three sampled repetitions uses 18000 actor decisions per model, before pilot, attacker development, annotation or optional arms. A second model replication doubles actor decisions; it is a separate population, not another 1000 independent task templates. A50-task pilot under the same layout uses 900 actor decisions. These are arithmetic scenarios, not API calls already made.

Closed-loop workloads can dominate cost:200 tasks×two execution/enforcement conditions×two clean/attack versions×three repeats×60 decision calls is an upper bound of 144000 actor decisions if every run hits its cap. Start with a smaller feasibility subset and report actual stopping distributions before committing. Reused observations are controlled fixtures in A, not evidence of live interaction. Cost feasibility may justify a narrow preregistered first experiment, but not reducingN after seeing effects and calling the original analysis confirmatory.

Fix per-run actor-call, output-token, tool-work and wall-time limits separately. Equal UI steps need not mean equal model work; a framework allowing multiple UI actions per call differs from a single-action scaffold. Actor budgets and attacker optimization budgets are distinct. If a budget itself is the treatment, show that explicitly and measure utility at each cap. [WebChoreArena](../records/webchorearena_evaluating_web_browsing_agents_on_realistic_tedious_web_tasks_comprehensive_summary.json) (claims C01 through C14; physical PDF pp.4–25); [Beyond Max Tokens](../records/beyond_max_tokens_stealthy_resource_amplification_via_tool_calling_chains_in_llm_agents_comprehensive_summary.json) (claims C01 through C15; physical PDF pp.3–14); [Odysseys](../records/odysseys_benchmarking_web_agents_on_realistic_long_horizon_tasks_comprehensive_summary.json) (claims odysseys_claim_01 through odysseys_claim_15; physical PDF pp.3–29).

## 8. Optional memory, horizon, modality and adaptation extensions

**Memory.** Randomize acquisition route, write permission and retrieval while holding a matched stored payload/content fixed where possible. Measure write, survival after reset, retrieval, decision and effect. Separate natural acquisition from direct store editing. Include clean useful memories and correction/deletion behavior. Package persistence is a separate supply-chain extension; do not call it the same threat model. [Context Manipulation](../records/context_manipulation_attacks_web_agents_are_susceptible_to_corrupted_memory_comprehensive_summary.json) (claims C01 through C14; physical PDF pp.4–8); [Hidden in Memory](../records/hidden_in_memory_sleeper_memory_poisoning_in_llm_agents_comprehensive_summary.json) (claims C01 through C15; physical PDF pp.3–80); [SkillTrojan](../records/skilltrojan_comprehensive_summary.json) (claims C01 through C15; physical PDF pp.1–14).

**Horizon.** Change interaction length and number of attack opportunities separately from conjunctive task complexity. Preserve equivalent subgoals and report all assigned tasks, not only trajectories that survive to a late stage. Use unique canaries/events to attribute persistence, and distinguish elapsed sessions, model calls and UI actions. A longer task can increase opportunity while lowering execution competence. [AgentLAB](../records/agentlab_benchmarking_llm_agents_against_long_horizon_attacks_comprehensive_summary.json) (claims claim_01_benchmark_scope through claim_14_shopping_drift; physical PDF pp.1–19); [Long-Horizon Mirage](../records/the_long_horizon_task_mirage_diagnosing_where_and_why_agentic_systems_break_comprehensive_summary.json) (claims claim_01 through claim_14; physical PDF pp.4–47); [WASP](../records/wasp_comprehensive_summary.json) (claims wasp_c01 through wasp_c16; physical PDF pp.3–22).

**Modality.** Add paired screenshots/accessibility/HTML/captions only after validating equivalence; distinguish page-only edits from full-screenshot control and white-box from black-box budgets. Include perception accuracy before interpreting actor refusal as robustness. [Dissecting Adversarial Robustness](../records/dissecting_adversarial_robustness_of_multimodal_lm_agents_comprehensive_summary.json) (claims C01 through C15; physical PDF pp.1–22); [Pop-ups](../records/attacking_vision_language_computer_agents_via_pop_ups_comprehensive_summary.json) (claims claim_01 through claim_15; physical PDF pp.2–15); [WebInject](../records/webinject_prompt_injection_attack_to_web_agents_comprehensive_summary.json) (claims C01 through C15; physical PDF pp.1–21).

**Adaptation.** First evaluate common fixed payloads. Then allocate equal queries/tokens to separate per-defense adaptive optimization using independent development tasks and a common final test set. Report budgets, selection and clean utility. The adaptive experiment estimates resistance to an adversary's search process, not the same fixed-distribution susceptibility contrast as A. [AgentVigil](../records/agentvigil_generic_black_box_red_teaming_for_indirect_prompt_injection_against_llm_agents_comprehensive_summary.json) (claims av_c01 through av_c15; physical PDF pp.2–14); [WARD](../records/ward_comprehensive_summary.json) (claims ward_c01 through ward_c15; physical PDF pp.2–22).

**Enforcement.** Start with a small reproducible policy set, then controlled label/policy errors as a robustness extension. A correct-policy guarantee is not refuted merely by violating its premises; deployed error tolerance and utility are additional research questions. [UCM](../records/untrusted_content_masking_for_web_agents_with_security_guarantees_comprehensive_summary.json) (claims C01 through C12; physical PDF pp.1–22); [Prismata](../records/prismata_confining_cross_site_prompt_injection_in_web_agents_comprehensive_summary.json) (claims C1 through C13; physical PDF pp.2–15); [ACE](../records/ace_comprehensive_summary.json) (claims ace_c01 through ace_c18; physical PDF pp.1–18).

## 9. Confounders and validity threats

| Threat | Mitigation and remaining interpretation limit |
|---|---|
|Tool-aware standalone contract| Name it explicitly; add a natural-chat check for answer deviations only. No universal statement about all standaloneLLMs. |
|Representation/token differences| Use canonical fixtures, content/visibility audits and position/length controls. The interface is a contextual treatment, not identical full input. |
|Different reachable tasks| Separate common decision/read utility from executable task completion; structurally impossible harm is not resistance. |
|Trajectory divergence| Separate A's replay effect from B's total system effect; avoid causal conditioning on post-treatment encounter. |
|Model/API drift| Pin checkpoints/snapshots where possible, record date/parameters, randomize scheduling and repeat a stable subset; hosted service reproducibility remains limited. |
|Attack overfitting/selection| Disjoint development/test families; common held-out transfer; separately labeled adaptation; report failed search costs. |
|Judge leakage or preference| Blind conditions, independent state checks, balanced annotation, disagreement analysis; no sole teacher/attacker/judge chain. |
|Insufficient independence| Cluster repeats and related fixtures; audit template/site overlap; report effective cluster counts. |
|Utility collapse| Clean pairs, joint success/security, false rejection and abstain-all controls; no security ranking at unmatched task coverage. |
|Synthetic harms/live generalization| State exactly which surrogate was verified; no claims of real theft or damage. Subsequent live validation would require separately bounded authorization. |
|Missing results| Preserve timeout/crash/invalid categories and all assigned denominators; sensitivity/bounds for unscorable cases. |
|Survivorship at long horizon| Include all initial assignments; do not infer resilience from an agent that never reaches the target. |

## 10. Interpretation and decision criteria

Support for an interface effect requires a precisely estimated primary interaction under audited common information and prespecified analysis. A null with a wide interval is inconclusive. A nonzero result demonstrates the specified context/interface treatment, not an intrinsic change to the neural weights. A difference only in B can be an exposure/feedback/authority effect. A difference only in accepted/verified effects for replayed calls is an enforcement/consequence effect.

For a defense, report the joint distribution of D, attempts, effects, utility and resource use. A classifier improvement with unchanged effects, or lower effects through total abstention, is not sufficient evidence of usable end-to-end protection. Model replications and new task families define the scope of generalization; a few strongest cells do not establish universality.

Before implementation, verify the proposed gap against external primary literature and original artifacts, assess feasibility and obtain any required institutional review for future human labeling. Finalize the protocol and analysis after the development pilot, then collect genuinely separate confirmatory data. The deliverable here is the study design; execution, new infrastructure and publication drafting remain separate work.
