# Stage 0 — Document Accessibility Report

The supplied work is available as extracted text for physical PDF pages 1–25. Rendered page images are supplied for pages 1–4, 6–9, 12, and 15–25: 20 visually inspected pages. Pages 5, 10, 11, 13, and 14 were inspected through supplied text only. No tools, browsing, external sources, or additional local files were used. The supplied content was treated as evidence rather than instructions.

| Accessibility item | Assessment |
|---|---|
| Main document | Available as supplied text across pages 1–25 |
| Apparent page continuity | All physical pages 1–25 have text; no intervening page is absent |
| Completeness beyond this document | Not established; no independent PDF or artifact verification |
| Visual coverage | Partial document rendering; all four numbered figures and all 29 numbered tables are visible on supplied rendered pages |
| Tables | Readable overall; small typography requires caution, especially confidence intervals and superscripts |
| Equations | Principal formulas readable in supplied text and rendered pages; typography normalized below |
| Appendices | A–G present, despite the accessibility metadata reporting no detected appendix pages |
| Supplementary artifacts | No separate code, task files, memory corpus, prompts, or trace annotations supplied |
| Referenced absent artifact | `analysis/gate_annotation_results.json`, named on p. 19; release materials promised on p. 15 |
| OCR | Not needed for this analysis because extracted text and readable renderings are supplied |
| Other limitation | Supplied metadata is descriptive, not proof of experimental reproducibility or source authenticity |

Evidence labels used throughout: **[A] author-reported**, **[B] directly observable in a supplied visual**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information [E] is introduced. Unless explicitly marked otherwise, descriptions of the study and its results are [A], with tables cross-checked visually where available. Confidence is HIGH for clearly readable reported quantities, MEDIUM for qualified methodological interpretations, and UNKNOWN where the source leaves a contradiction unresolved.

## Document inventory established before synthesis

**Title:** The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory. **Authors:** Yixiong Chen, Xinyi Bai, and Alan Yuille. **Affiliations:** Johns Hopkins University and Cornell University. **Publication information supplied:** preprint, arXiv:2607.10608v1, dated 12 July 2026. No accepted venue is supplied. **Type:** empirical artificial-intelligence agent study combining a diagnostic framework, controlled browser experiments, a benchmark contribution, and policy ablations. No keywords, theorem statements, proof sequence, or numbered pseudocode algorithms are supplied.

Main sections are Abstract; §1 Introduction; §2 Related Work; §3 Method, including §3.1 Entry–Propagation–Recovery diagnostics, §3.2 Compliance under conflicting memory, and §3.3 Testbeds and protocol; §4 Results, including §§4.1–4.4; §5 Discussion; §6 Conclusion; References; and Appendices A–G. Appendix E contains E.1 trace annotation, E.2 factorial experiments, and E.3 delivery-channel analysis. Appendix F contains F.1 cross-family validation and F.2 short-horizon control.

Visual inventory: Figures 1–4, including substantive panels 1A/1B, 3a/3b, and 4a/4b; Tables 1–29. Mathematical inventory: conditional Damage Per Compliance, the four-gate helpful-lift expression, propagation factor, action-history momentum, cumulative entry probability, conditional recovery probability, and oracle-gap closure. Experiment inventory: full-WebArena retrieval pre-check; schedule intervention; judged compliance; action-divergence robustness; trajectory recovery; MemTrapBench persistent conditions; diagnostic-family comparisons; irrelevant-memory control; grounding and commitment analyses; novelty/preference analysis; full-distribution format comparison; pilot replication; trace annotation; conflicting and helpful factorials; delivery-channel ablation; cross-family check; MiniWoB++ short-horizon control; retry policy comparison; and retry-content ablation. These items form the coverage denominator used at the end.

# 1. Plain-language orientation

This paper asks what happens after an artificial-intelligence agent receives a memory from earlier experience. A memory might tell a browser agent how to submit a product review, configure accounts, or complete a refund. Such advice can be helpful, irrelevant, or plausible but wrong for the current task. The paper studies how that advice changes the agent’s actions over time, rather than primarily studying how memories are stored or retrieved.

The central contribution is **Entry–Propagation–Recovery (E-P-R)**: examine when memory first changes an action, whether the change continues through later actions, and whether the agent can correct its course. The researchers hold memory passages fixed while changing when they are shown, compare memory-assisted runs with paired no-memory runs, and evaluate both existing WebArena tasks and their controlled MemTrapBench browser tasks.

The main finding is a **compliance trap**. On the selected WebArena diagnostic pool, different models follow conflicting recommendations at broadly similar rates, 63–72%, but stronger-baseline models lose more success after doing so. On the judged compliant subset, no-memory success ranges from 23.4% to 49.0%, whereas conflicting-memory success ranges from 17.0% to 30.9%. Thus, a model can possess greater task-solving capability while still surrendering much of that advantage when it follows wrong advice. These are conditional results, not a universal law about model size. [A; pp. 4–7, Table 2]

The controlled benchmark adds an important qualification: agents sometimes return to baseline-like actions after a detour but still fail because an earlier wrong action has already damaged the task outcome. Recovery of behavior and recovery of success must therefore be measured separately. [A; pp. 20–22]

**Relevance to the requested security question [D]:** the work supports a mechanism by which web agents can turn misleading contextual information into a sequence of consequential actions. It does **not** directly compare browser agents with standalone large language models, measure a browser-versus-chat vulnerability ratio, or establish that all web agents are more vulnerable. Its contribution is evidence about memory-conditioned browser behavior under controlled interventions.

# 2. Document roadmap

The abstract and introduction establish the distinction between memory supply and memory consumption. Figure 1 makes that distinction visually. Related Work organizes prior studies into memory systems, reasoning and correction, trajectory evaluation, and misleading context. Method defines the intervention variables, E-P-R, compliance metrics, models, datasets, and paired comparisons. Figure 2 depicts the proposed trajectory mechanism.

Results first establish that retrieved memory does not uniformly help on the full WebArena distribution, then inspect schedule effects on a selected memory-sensitive subset, characterize conditional damage, and validate the pattern on MemTrapBench. Discussion examines delivery channel, trajectory length, and a simple failure-conditioned retry policy. The conclusion argues for evaluating memory throughout a trajectory.

Appendix A supplies implementation and authoring details. B defines metrics and compliance subsets. C extends the WebArena analyses. D explains benchmark construction and task accounting. E adds trace annotation and factorial/channel probes. F investigates model-family and short-horizon boundaries. G separates retry policy effects from the contribution of helpful memory. References occupy pp. 10–13 and are treated as author-provided bibliographic context, not independently verified evidence.

# 3. Background and context

A **large language model (LLM)** generates the agent’s next response or action. A **browser agent** repeatedly observes a page, chooses an action, and receives a new observation. A **trajectory** is this ordered action-and-observation history. Here, observations use the BrowserGym **accessibility tree (AXTree)**, a structured representation of page elements, rather than an evaluated screenshot-based perception pipeline. This distinction matters: the paper concerns browser interaction, but its experiments do not establish the same numerical effects for every visual agent architecture. [A; pp. 5, 14]

**Memory** means a short external textual passage inserted into the agent context during an episode. It is not a change to model weights. Helpful memory gives task-correct guidance; conflicting memory gives plausible task-wrong guidance; cross-task memory gives advice for another task on the same website. The latter is a control for extra text and related vocabulary.

**Grounding** means mapping advice onto actionable elements in the current page state. A recommendation may sound reasonable yet refer to an unavailable label or a value that cannot be read where the memory claims. **Compliance** is narrower than merely taking a different action: the judged action must plausibly execute the recommendation. **Divergence** means the memory and no-memory action traces differ under the authors’ action comparison. **Recovery** can mean returning to baseline-like actions or ultimately succeeding; these are distinct constructs.

Related Work positions existing memory methods mainly on the supply side: writing reflections, distilling experience, compiling workflows, or organizing memory stores. It positions static misleading-context and knowledge-conflict studies as related but different from a multi-step agent trajectory. These are the authors’ characterizations; the cited outside papers were not independently reviewed here. [A; p. 3]

# 4. Research problem and gap

**Existing problem:** retrieved experience can be ignored, followed too literally, used at an inappropriate state, or retained after it becomes harmful. Better retrieval alone does not determine how an imperfect agent policy consumes a passage. [A; pp. 1–2]

**Shortcoming attributed to previous approaches:** many memory systems optimize what reaches context and assume the agent can decide how to use it. Final task success can reveal an outcome without locating the stage where the memory changed behavior. [A; pp. 1–3]

**Research gap:** a trajectory-level account of where memory first affects action, how the effect persists, and whether correction succeeds. The authors propose diagnostic measurements rather than a new retrieval architecture or trained defense.

**Motivation:** a plausible memory can redirect a browser agent through a well-formed but incorrect workflow. The danger need not appear as a parser error. The agent may successfully operate interface controls while failing the user’s actual goal. [A; pp. 5, 14]

**Scope:** controlled textual-memory consumption by browser agents, with helpful, conflicting, and irrelevant controls. The broader security interpretation concerns misleading inputs influencing actions, but the paper does not present a complete adversarial campaign, attacker optimization procedure, credential-exfiltration evaluation, or comparison with standalone LLMs. [D; bounded by pp. 3–5, 9]

# 5. Research questions, objectives, and hypotheses

The introduction explicitly asks how long-horizon agents consume retrieved memory across a multi-step trajectory and which stage determines whether it helps or hurts. This is the central research question, not a question about standalone LLM superiority or inferiority. [A; p. 2]

The stated objectives are to formulate memory consumption as a trajectory problem, introduce E-P-R, identify the compliance trap, and provide MemTrapBench plus a paired WebArena protocol separating broad average effects from mechanism diagnosis. [A; p. 2]

Additional explicit appendix questions ask why conflicting memory enters easily; whether the pattern survives different memory formats; whether it survives a different model family; whether it appears when trajectories are too short for propagation and recovery; and whether retry gains come from memory content or another attempt. [A; pp. 16–17, 22–24]

The paper does not provide a separately enumerated preregistered hypothesis list. Its tested expectations include amplification under repeated exposure, a role for entry and grounding, and a long-horizon boundary. These are reported experimental propositions rather than invented formal hypotheses. [A/D; pp. 6, 20–23]

# 6. Assumptions / Threat Model

The study’s operational model is a browser policy exposed to externally supplied textual guidance. The intervention controls both the content and the visibility schedule of the memory. Helpful and conflicting passages are matched in style; conflicting passages are designed to recommend feasible-looking but task-wrong behavior. WebArena memories reference real elements on the same site. [A; pp. 5, 14]

The primary comparison assumes matching task and environment seed, a shared interface, and greedy decoding. The authors aim to isolate the effect of memory rather than differences in retrieval quality. The no-memory trace is the behavioral counterfactual, not a guarantee of an optimal or successful trajectory. [A; pp. 4, 14]

**Security interpretation [D]:** the relevant asset is correct execution of the user’s browser task. The demonstrated influence surface is inserted memory text, including text placed at an observation footer. A hypothetical adversary able to supply such a passage could exploit the same type of decision influence, but the paper does not measure how often a real attacker can poison a memory store or win retrieval. It does not specify a full attacker privilege hierarchy, acquisition cost, stealth constraint, or adaptive attack budget.

The channel experiment compares system-prompt placement with observation-footer placement. It does not separately test every tool-output format, arbitrary website injection, persistent memory-store compromise, or cross-agent poisoning. The authors’ broader channel interpretation should therefore be distinguished from the actual two-channel manipulation. [A/D; pp. 8, 22, 24]

# 7. Methodology

## Intervention design and pairing

For each task/model cell, the authors run one no-memory trajectory and memory-conditioned trajectories under specified content/schedule combinations using the same environment seed. The primary outcome is the paired success-rate difference. Early memory is visible only at the first decision; persistent memory is visible at every decision; late memory is withheld until step 3. Early exposure probes entry, persistent exposure probes amplification, and late exposure probes resistance from an already formed history. Late injection is complementary to recovery, not a direct interchangeable measurement of it. [A; pp. 3–4]

## Models, interface, and inference

The named main models are Qwen3.5-9B, Qwen3.5-27B, Gemma-4-E4B-it, Gemma-4-26B-A4B-it, and Gemini-3-Flash. Tables sometimes shorten the larger Gemma name to Gemma-4-26B or Gemma-4-26B-it; this report preserves that naming variation rather than assuming an additional model. Three open-weight models, excluding Gemma-4-E4B, appear in the main MemTrapBench accounting. [A; pp. 5, 8, 18, 21]

Appendix A reports BrowserGym/WebArena, AXTree observations, a predefined ReAct action space such as click/type/scroll/navigate, a maximum of 15 steps, and a 600-second timeout. Four open-weight models use vLLM v0.19.0 on NVIDIA A6000 48 GB GPUs, bfloat16, prefix caching, context length 8,192 tokens, and maximum generation 2,048 tokens per step. Temperature is 0 and top_p is 1.0. Tensor parallelism is 1 for Qwen3.5-9B and 2 for the other listed open-weight models. Gemini uses the Google Generative AI API at temperature 0. The appendix says Gemini is queried on MemTrapBench only, which conflicts with the reported WebArena Gemini results; this remains unresolved. [A; p. 14 versus pp. 6–7]

## Task pools and construction

WebArena contributes 684 non-map tasks across five self-hosted website types: shopping, shopping administration, forum, code repository, and encyclopedia. Another 128 map tasks are excluded because geolocation is outside the intended memory-consumption focus. The 77-task diagnostic subset retains tasks whose binary result changes between any pair of no-memory, early-helpful, and early-conflicting runs on either Qwen model. This is outcome-based selection, so absolute effect sizes are not representative full-distribution estimates. [A; p. 14]

MemTrapBench is a controlled HTML/JavaScript browser benchmark with 231 main tasks, median horizon 15 steps, plus a separately reported 16-task pilot. Its four diagnostic families are DECOY, UPTAKE, GROUNDING, and OVERRIDE. They respectively emphasize a prominent wrong option, an alternate route behind Advanced, memory advice lacking the relevant visible label, and advice to ignore explicit environmental correction. Tasks have known correct and wrong paths. Construction includes no-memory and persistent-conflicting rollouts to check those paths. The authors distinguish this construction checking from selecting tasks by downstream evaluation outcomes. [A; pp. 5, 17–18]

Eight structural templates include a filter-detail-form-confirm pilot, multi-step wizard, report builder, cross-reference flow, bulk configuration, configure-and-verify navigation, multi-tab partial submission, and nested modal bypass. Main tasks use S2–S8; S1 is the pilot. Interactive elements expose button semantics and ARIA labels through the AXTree. [A; pp. 17–18]

## Memory authoring

WebArena passages are hand-authored. MemTrapBench tasks and memory trios are drafted by Claude Opus 4.7 and manually reviewed. The same DO/DON’T structure is used, with NOTE sections in the WebArena pair audit. Across 77 WebArena pairs, mean character lengths are 619 versus 622, word counts 103.7 versus 100.8, all pairs share structural elements, and confidence-language frequency is 0.03 instances per task on both sides. MemTrapBench passages are matched to 500–1,200 characters. These controls reduce measured stylistic confounds; they do not prove all semantic confounds absent. [A/D; pp. 14, 18]

## Metrics and statistics

Success rate is the proportion of tasks completed successfully. Recommendation Compliance Rate (RCR) is the proportion judged to execute the first primitive of the conflicting recommendation at the first exposed decision. Gemini-3-Flash at temperature 0 judges the conflicting DO excerpt, no-memory action and URL, and conflicting action with before/after URLs. Responses are YES, NO, or UNCLEAR; the strict subset contains YES. The judge must distinguish a merely different action from one more aligned with the memory. An unchanged URL after clicking is not automatically failure because a menu can expand in place. [A; pp. 4, 15]

Damage Per Compliance (DPC) compares paired success within the selected compliant subset. A coarser action-divergence subset is also examined. Divergence checks action verb or targeted element identifier, while type-text differences alone do not count in Appendix A; Appendix B uses looser action-string language, so exact implementation equivalence is not fully established from prose. [A/D; pp. 14–16]

Paired contrasts use 10,000-iteration sign-flip permutation tests and paired bootstrap percentile confidence intervals with 10,000 resamples. Appendix A adds Holm–Bonferroni correction for families with more than two conditions. The authors do not pool models. No learning train/validation/test split is described for a newly trained model because the contribution is an evaluation protocol rather than training a new policy. Code and trace artifacts were not supplied for independent reproduction. [A; pp. 5, 14–15]

# 8. Experiments / Analyses

| ID | Purpose and manipulation | Data and controls | Main result and caveat |
|---|---|---|---|
| X1 | Test whether online retrieval uniformly helps | 684 WebArena tasks; two Qwen models; unconditional versus relevance-gated memory | −1.9/+1.7 pp unconditional; −2.3/−1.7 pp gated; mixed effects, not blanket memory harm; Tables 1, 17 |
| X2 | Diagnose exposure schedule | Selected WebArena pool; helpful/conflicting; early/persistent/late | Persistent conflict hurts all five plotted models; Qwen27B persistent versus early p=0.013; selection inflates possible magnitude; Fig. 3 |
| X3 | Separate recommendation following from conditional cost | WebArena judged subsets, model-specific N | RCR 63–72%; DPC 2.1–25.5 pp; only Qwen27B and Gemini intervals exclude zero; Table 2 |
| X4 | Check coarse divergence robustness | Four open-weight WebArena models | DPC 5.3–22.7 pp; only Qwen27B interval excludes zero; Table 8 |
| X5 | Measure trajectory entry and recovery | Qwen traces plus four-model recovery tables | Early cumulative divergence; persistent-conflict recovery about 13% for Qwen versus about 31% for Gemma; Fig. 4, Tables 9–11 |
| X6 | Validate on constructed tasks | 231 MemTrapBench tasks; helpful/conflicting/cross-task | Helpful +25.5 to +30.7 pp; conflict −9.5 to −26.0 pp; action-divergence DPC intervals exclude zero for four models; Table 3 |
| X7 | Locate diagnostic differences | Four MemTrapBench families | DECOY gives largest conflict loss; GROUNDING largest helpful gain; low starting success limits detectable loss; Table 4 |
| X8 | Test context-content specificity | Cross-task memories on both testbeds | Small comparison effects relative to conflict; WebArena Gemma control is +4.5 pp, exceeding one caption’s ±3 pp description; Tables 3, 13 |
| X9 | Examine grounding, commitment, and novelty | WebArena page-state and baseline-preference analyses | Late advice more groundable; strong-model URL commitment can resist conflict; weak-preference conflict adoption exceeds helpful by 24.6–40.6 pp; Tables 14–16 |
| X10 | Test memory-format dependence | Full 684-task distribution; four formats | Qwen9B negative and Qwen27B positive for M1–M3; gating negative for both; only M3 p<0.05 for both; Table 17 |
| X11 | Check pilot and accounting | 247 total tasks; 16 pilot separate | 5,928 three-model/eight-condition trials; zero reported task drops; pilot conflict losses −18.8 to −31.2 pp; Tables 19–20 |
| X12 | Distinguish action and outcome recovery | 4,851 annotated non-baseline traces | Many traces recover behaviorally while persistent-conflict success is 1.3% in all three displayed main models; Tables 21–22 |
| X13 | Manipulate entry and grounding | 32 DECOY tasks/cell/model; 2×2 persistent-conflict design | Grounding main effects −29.7/−23.4 pp; entry significant only for Qwen; Table 23 |
| X14 | Compare helpful factorial | Same task design, Qwen27B | Helpful cells gain 0–6.2 pp; estimated interaction approximately zero; Table 24 |
| X15 | Test placement | Same memory in system prompt versus observation footer | Conflict changes by at most 0.5 pp; helpful gains attenuate 4.4–16.0 pp; Tables 5, 25 |
| X16 | Check model-family boundary | 611 common valid WebArena tasks | Gemma3-27B −3.4 pp versus Qwen27B +1.7 pp for online memory; not a standalone-model comparison; Table 26 |
| X17 | Check short-horizon boundary | MiniWoB++, 12 tasks, three seeds, seven conditions reported | Conflict effects small, including Gemma +3.9 pp; median horizon differs across source passages; Tables 6, 27 |
| X18 | Compare simple policies | WebArena helpful injection and oracle | Retry improves Qwen27B to 50.6%, but adds a second attempt and uses outcome feedback; Tables 7, 12, 28 |
| X19 | Separate retry content from another attempt | MemTrapBench retry without/with helpful memory | Table rows show +2.0–2.7 pp without memory versus +19.7–31.2 pp with helpful memory; caption/prose ranges disagree; Table 29 |

These experiments are linked rather than interchangeable. Broad online-memory averages, selected-subset diagnostics, constructed traps, and conditional-subset damage answer different questions. Their denominators and metrics must remain attached to each result.

# 9. Results

**Finding 1: memory usefulness depends on the consumer and condition.** On all 684 non-map WebArena tasks, unconditional retrieval yields −1.9 pp for Qwen9B and +1.7 pp for Qwen27B. Relevance gating changes these to −2.3 and −1.7 pp. This supports a need to inspect consumption; it does not establish that memory is generally harmful. [A; p. 6, Table 1]

**Finding 2: persistent conflict is consistently damaging in the selected schedule experiment.** Figure 3 reports persistent-conflict deltas of −9.1, −20.8, −4.0, −4.8, and −14.9 pp across Qwen9B, Qwen27B, Gemma-E4B, Gemma-26B, and Gemini respectively. Nearby summary Table 6 gives −4.5 pp for Gemma-26B under its stated paired pool; these figures should not be silently substituted. For Qwen27B, persistent conflict is worse than early conflict with p=0.013. [A/B; pp. 6, 9]

**Finding 3: similar recommendation compliance can coexist with different conditional damage.** Table 2’s judged-compliance DPC is +2.1 pp for Gemma-E4B, +7.1 for Gemma-26B, +9.4 for Qwen9B, +18.5 for Gemini, and +25.5 for Qwen27B. Positive DPC denotes lost success because the formula subtracts conflicting success from baseline success. Only the last two 95% intervals exclude zero. The prose describes damage using negative changes, creating a sign-convention mismatch with the positive DPC table; this report uses positive DPC and negative overall success deltas consistently. [A; p. 7]

**Finding 4: the controlled benchmark shows both large benefit and large harm.** Table 3 baseline/helpful-delta/conflict-delta triplets are 10.8%/+25.5/−9.5 for Qwen9B; 22.5%/+30.7/−21.2 for Qwen27B; 12.1%/+29.9/−10.8 for Gemma26B; and 32.9%/+29.4/−26.0 for Gemini. Deltas are percentage points. The positive control is important: these passages can help under the same general setup. [A/B; p. 8]

**Finding 5: recovery is multidimensional.** In Table 22, Qwen27B persistent-conflict traces have 55.4% reported recovery but only 1.3% task success; its helpful condition has 69.7% recovery and 53.2% success. This does not mean recovery causes failure: it shows that the action-realignment metric is insufficient to certify salvaged outcomes. [A/D; p. 22]

**Finding 6: grounding matters under intervention.** In the conflicting factorial, replacing actionable UI references with nonexistent alternatives raises cell success. Grounding main effects are −29.7 pp, 95% CI [−45.1, −13.8], for Qwen27B and −23.4 pp, [−38.7, −8.3], for Gemma26B. The manipulation supports a causal role for the tested prompt-level grounding intervention, with scope limited to 32 constructed DECOY tasks per cell. [A; pp. 21, 23]

**Finding 7: channel prominence affects benefit more than measured conflict damage.** Footer placement retains nearly the same conflict losses, while Qwen27B helpful gain falls from +30.7 to +14.7 pp. This is a 16.0 pp attenuation; the authors report a 52% reduction. It is not a 52-percentage-point loss. [A; pp. 22, 24]

**Finding 8: failure-conditioned helpful retries are promising diagnostics, not a deployed defense.** Table 29 gives retry-helpful success of 30.5%, 53.7%, and 43.2% for Qwen9B, Qwen27B, and Gemma26B. Retry-no-memory success is 12.8%, 25.1%, and 14.8%. The table’s explicit memory-content gaps are 17.7, 28.6, and 28.4 pp. The policy assumes a failure signal and an additional attempt. [A; pp. 24–25]

# 10. Figure-by-figure interpretation

## Figure 1 — Supply versus consumption, p. 2

This is a two-panel conceptual diagram, not a measured plot. Panel A stacks past trajectories, write/store, retrieve, and memory in prompt, connected downward. It describes the supply pipeline. Panel B shows a horizontal gray no-memory trajectory from start through later decisions to outcome. A blue retrieved-memory box points to a decision where a blue alternative path branches downward and continues through later states. The arrows communicate influence and temporal sequence; circles are states/decision points, not reported sample counts. The figure supports the choice to inspect behavior after retrieval, without itself demonstrating harm or an effect size. [B]

## Figure 2 — E-P-R framework, p. 4

Conflicting and helpful document icons feed an agent icon. The trajectory proceeds left to right through Entry, Propagation, and Recovery. A dashed gray baseline runs through the middle. A red trajectory departs upward, can continue to failure marked by a red cross, or bend back toward the baseline as correction. A blue trajectory departs downward and continues to success marked by a green check. Labels identify first changed action, schedule effect, and self-correction. Colors encode conceptual trajectory types, not probabilities; no quantitative axes or confidence intervals are present. The illustration explains the mechanism the experiments probe and should not be mistaken for experimental proof. [B]

## Figure 3 — WebArena schedule effects, p. 6

Two grouped bar-chart panels compare five models along the horizontal axis. Panel a shows helpful memory in blue shades; panel b shows conflicting memory in red shades. Within each model, shades encode early, persistent, and late exposure. The vertical axis is change in success rate, in percentage points, on a linear scale; zero separates improvement from harm. The helpful panel’s displayed ticks run approximately −2.5 to 17.5; the conflict panel includes positive values and extends below −20. These are plotting bounds, not statistical intervals. Exact bar labels are available, so no estimated bar height is needed for the principal results.

Early/persistent/late helpful labels are Qwen9B +2.6/+5.2/+0.0; Qwen27B −1.3/+1.3/+0.0; Gemma-E4B +2.7/+10.7/+1.3; Gemma26B +1.6/+7.9/+12.7; Gemini +6.8/+4.1/+6.8 pp. Conflicting labels are Qwen9B −7.8/−9.1/−5.2; Qwen27B −7.8/−20.8/−3.9; Gemma-E4B +0.0/−4.0/+4.0; Gemma26B −1.6/−4.8/+3.2; Gemini +1.4/−14.9/−6.8 pp. [B]

No uncertainty bars are displayed. The caption identifies a 77-task subset, with Gemini n=74. Other tables use other valid subsets. Persistent conflict is the only plotted condition below zero for every model. Helpful persistence is not universally the best schedule: Gemma26B’s late helpful label is larger. The caption’s cross-task-within-±3-pp statement conflicts with Table 13’s +4.5 pp Gemma control. [A/B]

## Figure 4 — Entry and recovery curves, p. 7

Panel a is cumulative divergence: horizontal axis step t, shown from 0 to 14; vertical axis P(t_entry≤t), 0–1, linear. Panel b uses the same step scale and a conditional cumulative recovery probability, P(re-aligned by t | diverged), also 0–1. Red dashed curves are conflicting memory, blue solid curves helpful memory; the two models have distinct line shades. The legend lists Qwen9B n=49 and Qwen27B n=44 for the plotted comparisons. No error bands are shown.

The left curves rise early and level high. The right curves stay lower, with helpful curves above conflicting curves. The caption reports entry probability 0.86–0.94 by step 7; surrounding prose instead places that range by step 14. The exact endpoint timing is therefore disputed within the paper. The reported recovery comparison is approximately 27–42% helpful versus 7–15% conflicting. Tables 9–11 provide related recovery values but are not assumed to share identical plotted denominators. [A/B]

# 11. Table-by-table interpretation

All tables below were inspected in supplied images and extracted text. Values are author-reported; percentage-point changes are distinguished from absolute percentages. Tables without uncertainty estimates should not be read as demonstrating significance merely because their point estimates differ.

| Table; page | Comparison, important values, and interpretation | Statistical information and caveats |
|---|---|---|
| 1; 6 | Two Qwen models, unconditional versus relevance-gated full-WebArena retrieval. Deltas −1.9/−2.3 pp for 9B and +1.7/−1.7 for 27B. Gating does not produce a uniform gain. | No intervals in this table; related p-values appear in Table 17. |
| 2; 7 | Five model rows; N, RCR, compliant count, paired baseline/conflict SR, DPC. N=75/67/77/75/77; compliant counts 47/42/53/54/51. RCR 63/63/69/72/66%. Largest DPC Qwen27B 25.5 pp, smallest Gemma-E4B 2.1. | CIs: [−10.6,+14.9], [−4.8,+19.1], [−3.8,+22.6], [+3.7,+33.3], [+11.8,+39.2]. Only Gemini/Qwen27B exclude zero. Conditional subsets differ by model. |
| 3; 8 | Four models on 231 main tasks. Helpful gains +25.5,+30.7,+29.9,+29.4; conflict −9.5,−21.2,−10.8,−26.0; cross-task −2.6,+1.3,+0.9,−1.7 pp. | Action-divergence DPC 10.2/26.6/14.1/28.6 pp; CIs [5.4,15.7]/[19.6,33.5]/[8.3,19.9]/[21.9,35.2]; all p<.001. This subset differs from Table 2 RCR. |
| 4; 8 | Four diagnostic families and four models, each with helpful/conflict deltas. DECOY losses −24.2,−35.5,−25.8,−43.5 pp. GROUNDING helpful gains +66.7,+73.7,+57.9,+68.4 pp. | Baselines constrain losses: GROUNDING starts at 0.0/1.8/1.8/17.5%. Its conflict deltas 0.0/−1.8/−1.8/−15.8 cannot be interpreted independently of those floors. |
| 5; 8 | Three open-weight models, conflict delta system/footer: −9.5/−10.0, −21.2/−20.8, −10.8/−10.4 pp. | Largest placement difference 0.5 pp; no equivalence-test interval supplied. |
| 6; 9 | Benchmarks at reported median steps 3/7/15. Qwen27B conflict losses −2.9/−20.8/−21.2; Qwen9B 0.0/−9.1/−9.5; Gemma +3.9/−4.5/−10.8 pp. | Cross-benchmark association, not a within-task randomized horizon manipulation; short-horizon median conflicts with p. 23. |
| 7; 9 | No memory/always-helpful/retry-helpful. WebArena Qwen27B 40.3/41.6/50.6%; MemTrap Qwen27B 22.5/53.2/53.7%; Gemma 12.1/42.0/43.2%. | A retry uses additional opportunity and a failure signal. No CI displayed. |
| 8; 16 | Coarse-divergence robustness: subset counts 56/65/57/66 for Gemma-E4B/Qwen9B/Gemma26B/Qwen27B. DPC 5.4/9.2/5.3/22.7 pp. | CIs [−5.4,16.1]/[−1.5,20.0]/[−3.5,14.0]/[12.1,34.9]; p=.56/.17/.45/<.001. No Gemini row, limiting the claimed match to Table 2. |
| 9; 16 | Persistent helpful/conflict and late conflict recovery. Persistent conflict: Gemma-E4B 32.4%, Qwen9B 12.7%, Gemma26B 31.4%, Qwen27B 13.0%. | Conditional recovery among diverged traces; repeats selected Table 11 rows. Architecture-level explanation is author interpretation, not isolated architecture manipulation. |
| 10; 16 | Propagation factor and action-history momentum. Conflict PF Qwen9B 1.2, Gemma26B 4.8, Qwen27B 2.4; Gemma-E4B dash. Helpful PF 4.1/2.9/2.0/dash. | Dashes mean early-effect magnitude <2 pp. Ratios unstable near zero; negative helpful momentum for Gemma26B indicates late effect exceeds early. |
| 11; 17 | Six memory/schedule recovery rows across four models. Late helpful recovery 30.5/35.5/33.9/43.6%; early conflicting 25.7/22.9/33.8/22.4%. | Full table shows low Qwen recovery is particularly persistent-conflict-specific rather than universal across conditions. |
| 12; 17 | All-valid schedule subsets n=73/70/76. Baseline/persistent/oracle: 31.5/37.0/46.6, 42.9/42.9/52.9, 32.9/35.5/47.4%. Wasted gains 9.6/10.0/11.8 pp. | Perfect per-task outcome knowledge; different pool from Table 28. Oracle is a reference bound for fixed one-attempt schedule selection. |
| 13; 18 | Same-site irrelevant control: +1.3/−2.6/+4.5 pp versus conflict −9.1/−20.8/−4.5 for Qwen9B/Qwen27B/Gemma26B. Baselines 30.7/43.1/32.5%. | Supports content specificity within controls tested; +4.5 contradicts Fig. 3’s ±3 pp summary. |
| 14; 18 | Groundability 0–1 at injection and step 3, persistent/late, helpful/conflict. Early injection helpful ≈0.09–0.10, conflict 0.13; late helpful 0.47/0.54/0.51, conflict 0.35/0.36/0.35. | Page-state measure, not success probability. One persistent step-3 Qwen9B comparison is 0.52 helpful versus 0.53 conflict, so helpful is not higher in every cell. |
| 15; 19 | URL commitment and switching under late memory. Gemma26B commitment helpful/conflict 33.3/84.6%, switching 33.3/0.0%; Qwen27B commitment 50.0/69.2%. | Qwen9B reverses the commitment direction, 62.5/46.7%. Do not generalize the stronger-model pattern to every row. |
| 16; 19 | Adoption by weak/strong baseline preference. Weak-preference helpful/conflict means 54.6/86.1%, reported gap +31.5 pp; strong means 34.9/42.9%, gap +8.0. | Weak gaps +26.4,+24.6,+34.4,+40.6 pp. Precise preference-classification threshold is not supplied in the visible prose. |
| 17; 20 | Full 684-task M1/M2/M3/C1 format deltas. 9B −1.3/−1.2/−1.9/−2.3; 27B +0.7/+1.0/+1.7/−1.7 pp. | p pairs .121/.265, .250/.114, .046/.011, .103/.183. C1 score≥3. Claimed monotonic amplification is not exact for 9B M1 versus M2. |
| 18; 20 | Four task illustrations: refund destination, role-scoped two-factor authentication, quarterly orders, and issue resolution label. Columns pair misleading action with correct path. | Illustrative benchmark examples, not independent measured results. Compressed here after inspection. |
| 19; 21 | Accounting: 16+231=247 tasks; all memory trios authored; each of three models evaluated on all eight conditions; 5,928 trials; zero task drops. | Gemini persistent runs are additional to this three-model count. Zero task drops does not explain all later analysis-specific denominator changes. |
| 20; 21 | Pilot n=16. Baselines 37.5/43.8/25.0%; persistent conflict −31.2/−31.2/−18.8 pp. Helpful persistent 0.0/+6.2/+25.0. | Pilot separately reported, with author-stated ceiling caveat. Small pilot; no intervals shown. |
| 21; 22 | Qualitative four-gate comparison. Helpful novelty on 34–41% of tasks; conflict novel by construction; RCR 63–69%, EDR upper bound 75–86%. | The RCR range describes open-weight rows, whereas all-five-model Table 2 reaches 72%. Not a standalone quantitative causal decomposition table. |
| 22; 22 | Twelve model/condition rows of adopted@1, diverged, recovered, success. Persistent-conflict success 1.3% for all three; recovery 61.0/55.4/45.0%. | Low adopted@1 need not mean no later strategic influence. Caption recovery range 55–80% excludes several displayed values. |
| 23; 23 | Conflict factorial, 32 tasks/cell/model. Qwen cell SR multi/unavailable 62.5, multi/groundable 31.2, single/unavailable 40.6, single/groundable 12.5%. Gemma 50.0/18.8/34.4/18.8%. | Qwen entry CI excludes zero; Gemma entry does not. Grounding CIs exclude zero for both. Gemma’s two groundable cells tie, qualifying the prose’s unique worst-cell implication. |
| 24; 23 | Helpful factorial Qwen27B; baseline 65.6%; four cell SRs 65.6/68.8/68.8/71.9%; deltas 0/+3.1/+3.1/+6.2 pp. | Entry and grounding main effects each +3.1 pp, interaction ≈0; two middle cells tie. No intervals shown. |
| 25; 24 | Expanded channel comparison. Helpful system/footer gains 25.5/19.0, 30.7/14.7, 29.9/25.5 pp; repeats conflict Table 5. | Helpful attenuation 6.5/16.0/4.4 pp; tested on three models, not all agents or channels. |
| 26; 24 | 611 common valid tasks. Qwen9B/27B deltas −2.0/+1.7; Gemma3 4B/12B/27B +1.0/−0.3/−3.4 pp. | Gemma27B p=.001, 10,000-iteration sign flip. Rounded 12B percentages 16.2→16.0 do not reconstruct −0.3 exactly; retain reported delta. |
| 27; 25 | Short-horizon model baselines 38.9/40.0/36.1%; persistent conflict 0/−2.9/+3.9 pp; persistent helpful −8.3/−3.9/0. | Only six displayed result conditions including baseline; prose says seven temporal conditions. Late-conflict outcome not displayed. |
| 28; 25 | WebArena policies; Qwen9B/27B baseline 29.9/40.3%; retry 35.1/50.6%; oracle 40.3/48.1%. Retry closures 50/133%. | Closure is delta divided by oracle delta. Late-helpful-valid subset n=70–76; 133% is not superiority to all policies under equal opportunity. |
| 29; 25 | MemTrap retry rows: no-memory 10.8/22.5/12.1%; retry-no-memory 12.8/25.1/14.8%; retry-helpful 30.5/53.7/43.2%. Helpful retry recovery 22/40/35%, no-memory 2/3/3%. | Row gains without memory +2.0/+2.6/+2.7 contradict caption +2.6–5.6. Denominators vary: Qwen9B 211–213, Qwen27B 231, Gemma229. |

# 12. Diagram / Architecture

Figures 1 and 2 are the substantive diagrams; their components and arrows are described in Section 10. Together they show a supply pipeline feeding a policy whose future trajectory can branch. No additional implemented system architecture, retrieval server design, memory database schema, or trained controller is specified as the proposed contribution.

The experimental workflow is: choose task and model; hold the initial environment seed fixed; run the baseline; insert matched memory under a chosen schedule; record actions and outcome; compare paired success; identify action divergence or judged compliance; calculate conditional damage and recovery. This sequence is reconstructed directly from the method, not presented as separately numbered author pseudocode. [A; pp. 4–5, 14–15]

MemTrapBench adds explicit environmental structure: actionable targets and decoys are exposed through the AXTree, while task goals distinguish correct from wrong paths. OVERRIDE includes a correction signal that the memory tells the agent to ignore. These are controlled browser environments, not evidence that a production memory architecture was deployed. [A; pp. 5, 17–20]

# 13. Equations and mathematical concepts

## E1 — Damage Per Compliance, pp. 4, 15

**DPC(C) = (1/|C|) Σᵢ∈C (yᵢ⁰ − yᵢᶜ).**

C is the selected subset, |C| its size, yᵢ⁰ the no-memory task-success outcome, and yᵢᶜ the conflicting-memory outcome for the same task. For headline WebArena results, C is the RCR YES subset. Both outcomes are paired within the same behavior-selected set. The summation totals lost success and the division averages it. Positive values mean damage; multiplying a fractional difference by 100 expresses percentage points. An empty-subset convention is not supplied. This is an evaluation statistic, not a training loss.

The paired construction avoids comparing an all-task baseline to a selectively compliant conflict subset. It does not turn the compliant subset into a random sample of all tasks. For MemTrapBench Table 3, C is explicitly the action-divergence subset despite other prose calling both tables RCR-based; that inconsistency is retained.

## E2 — Helpful-lift gate chain, pp. 5, 15, 19

**Δ_helpful = P(novel) · P(adopt | novel) · P(ground | adopt) · P(lift | ground).**

The intended meaning is that useful advice must add something new, be adopted, be mapped to the current environment, and improve final success. A failure at any gate can remove benefit. Appendix B gives the conditioned adoption term; §3.3 abbreviates it as P(adopt). The work uses the expression as a mechanistic decomposition. Exact event definitions, all conditioning dependencies, and a complete numerical reconstruction of the product are not supplied in the displayed tables. It should therefore not be expanded into an independently proved probability identity beyond the authors’ stated operational framing. [A/D]

## E3 — Propagation factor, p. 16

**PF = Δ_persistent^paired / Δ_early^paired.**

This ratio compares final paired success effects under repeated versus first-step exposure. With effects of the same sign, PF>1 means larger magnitude under persistent exposure. It is not a count of repeated mistakes or a direct per-step transition probability. Dashes are used when |Δ_early|<2 pp because division by a small effect is unstable. Negative or near-zero denominators require caution.

## E4 — Action-history momentum, p. 16

**AHM = 1 − Δ_late^paired / Δ_early^paired.**

Values near 1 mean late injection has little effect relative to early injection; values near 0 mean similar effects. Values below zero can occur if late injection has a larger same-direction effect. It is a normalized schedule comparison, not physical momentum or a guaranteed probability bounded by 0 and 1.

## E5 — Entry and recovery probabilities, p. 7

**P(t_entry≤t)** is the cumulative probability that the first divergence has happened by step t. **P(re-aligned by t | diverged)** conditions on having diverged and measures whether baseline-like action alignment has occurred by t. These outputs concern trajectories; neither alone guarantees final success.

## E6 — Oracle-gap closure, p. 25

**Closure = policy paired Δ / schedule-oracle paired Δ.**

The authors express the ratio as a percentage. An oracle chooses the best fixed helpful schedule per task with outcome foreknowledge. Retry is adaptive and can use a second attempt, so closure above 100% does not violate a mathematical optimum over an identical policy/resource class. No optimization theorem is proved.

**Analyst-derived example [C]:** Table 2’s displayed Qwen27B percentages give 49.0−23.5=25.5 percentage points, matching its DPC. Using the displayed Gemma26B values gives 38.1−30.9=7.2 pp, whereas the table reports 7.1 pp. Rounded component percentages can explain such a small mismatch, but unrounded outcomes are absent; the report retains the author’s 7.1 pp rather than replacing it.

# 14. Interpretation and discussion

The findings answer the paper’s central question by shifting attention from memory availability to policy behavior. A passage can be relevant-looking and well-formed yet still redirect the agent toward an incorrect goal. Repeated availability can preserve that influence, and later action correction may arrive too late to repair the outcome. Helpful memory has more opportunities to lose value: it may be redundant, ignored, not yet groundable, or insufficient to improve an already competent baseline. [A; pp. 7–9, 19–22]

The stronger-model result is conditional. It requires a higher baseline, comparable compliance, and a low post-compliance floor. The full-distribution Qwen27B gains and Gemma3 scaling differences prevent a simple assertion that model size monotonically increases vulnerability. Likewise, MemTrapBench’s 1.3% persistent-conflict success floor for the three displayed open-weight models is distinct from WebArena’s 17–31% judged-compliance floor. [A; pp. 7–8, 22–24]

## Cross-reference and consistency findings

1. **Gemini evaluation scope:** §3.3 names all five models on both testbeds; Appendix A says Gemini API use is on MemTrapBench only; Figure 3 and Table 2 report Gemini WebArena results. The supplied text does not resolve this methods–results conflict. [pp. 5–7, 14]
2. **Compliance subset:** Table 3 explicitly uses action divergence, but §§3.2/B describe Tables 2 and 3 as RCR-based. The caption and exact per-table condition are preserved; cross-table metric identity is not assumed. [pp. 5, 8, 15]
3. **LLM disclosure:** p. 15 says LLM tools were not used to score any outcome, while the same page describes an LLM judge for recommendation compliance. This may distinguish final task scoring from diagnostic classification, but the distinction is not explicitly reconciled.
4. **Entry timing:** Figure 4 caption gives the 0.86–0.94 range by step 7; prose gives it by step 14. Early entry is supported qualitatively; the precise timing claim is inconsistent. [p. 7]
5. **DPC sign:** Table 2 reports positive damage, while prose describes −2.1 to −25.5 pp. These can describe opposite-signed success change, but the naming is inconsistent. [p. 7]
6. **Short horizon:** Table 6 says MiniWoB median 3 steps; F.2 says approximately 2. Table 27’s Gemma persistent-conflict change is +3.9 pp, outside prose phrasing of −2.9 to 0 when interpreted as all effects. [pp. 9, 23, 25]
7. **Retry inconsistency:** Table 29 rows show retry-no-memory gains +2.0/+2.6/+2.7 pp and helpful recovery 22/40/35%; caption/prose gives +2.6–5.6 and 35–40%. The row data and Qwen9B exception are retained. [pp. 24–25]
8. **Recovery summary:** Table 22 caption says 55–80% recovered, but cells include 45.0% and 53.3%; persistent-helpful recovery also includes 60.6%, outside p. 20’s 69–78% summary. [pp. 20, 22]
9. **Format monotonicity:** p. 17/Table 17 say M1<M2<M3 amplification, but 9B deltas −1.3, −1.2, −1.9 do not follow strict monotonic magnitude. Only the broader directional pattern is supported. [pp. 17, 20]
10. **Controls and pools:** Figure 3’s ±3 pp cross-task summary conflicts with Table 13’s +4.5 pp. Tables 12 and 28 use different valid pools and baselines. Table 29’s reduced denominators are not fully explained despite zero reported benchmark task drops. [pp. 6, 17–18, 21, 25]
11. **Factorial interpretation:** Table 23’s Gemma groundable cells tie at 18.8%, qualifying the statement that the single/groundable condition is uniquely worst. The small positive interaction estimates support limited interaction on the reported additive scale; they do not alone prove a universal multiplicative model. [pp. 21, 23]
12. **Helpful Gemma rationale:** p. 21 justifies omitting Gemma’s helpful factorial by referring to small helpful gains in Table 3, which instead shows +29.9 pp overall. The rationale may concern the narrower DECOY subset, but that reconciliation is not stated.

These discrepancies do not erase the clearly reported main contrasts, but they reduce confidence in overly precise global summaries or claims of a fully unified metric implementation.

# 15. Contributions and novelty

**Conceptual:** the paper distinguishes consuming memory from supplying it and identifies a compliance trap linking uptake, low conditional success, and baseline capability. This is the authors’ novelty claim, not independently established priority over the outside literature. [A; pp. 1–2]

**Methodological:** E-P-R, paired schedule interventions, recommendation-specific compliance judging, conditional DPC, and separation of trajectory versus task recovery provide a diagnostic vocabulary and measurement protocol. The factorial design adds controlled tests of prompt-level entry/grounding manipulations. [A; pp. 4, 15, 20–23]

**Benchmark:** MemTrapBench supplies constructed browser tasks spanning four diagnostic families and multiple structural templates, with a separately accounted pilot. It is explicitly a mechanism probe rather than a replacement coverage benchmark. [A; pp. 17–18]

**Empirical:** results connect harmful exposure, persistent amplification, family differences, channel comparisons, short-horizon boundaries, and failure-conditioned helpful retries. No new trained agent, retrieval algorithm, security theorem, or production defense is delivered. [A; p. 9]

# 16. Limitations

## Authors’ stated limitations

First, long-horizon evidence comes only from web-browsing agents. Transfer to terminal/coding agents or embodied agents is untested; action spaces, modalities, and feedback may alter the gates. Second, the work characterizes leverage points but does not propose or train a new memory-management paradigm, controller, retriever, or training intervention. [A; p. 9]

The authors also acknowledge that the 77-task outcome-sensitive selection can inflate effect sizes; frame MemTrapBench as a mechanism probe rather than coverage benchmark; flag small-baseline constraints on GROUNDING harm; distinguish action recovery from irreversible outcome damage; identify the retry evidence as diagnostic rather than a deployment recipe; and warn that small WebArena samples can produce oracle overshoot. [A; pp. 7–9, 14, 17, 20, 24]

## Additional evidence-based analyst observations

[D] The research question about web agents versus standalone LLMs is not directly tested. No matched standalone response condition exists. The short-horizon browser control is not an equivalent substitute.

[D] Task construction deliberately creates plausible wrong routes and memory recommendations; resulting prevalence estimates should not be treated as real-world frequencies of hostile memory encounters. Construction rollouts also deserve scrutiny when interpreting complete independence from model behavior, even though they differ from the explicit WebArena outcome filter.

[D] Recommendation compliance uses an LLM judge, while no human-agreement estimate or calibration confusion matrix is supplied. Raw target identifiers can inflate coarse divergence, and first-action adoption is not equivalent to eventual strategic uptake.

[D] Selected subsets, valid-run pools, and success rounding complicate direct cross-table reconstruction. The source’s internal inconsistencies limit confidence in exact universal claims. The missing trace JSON, task corpus, prompts, and code prevent independent verification of annotations, enforcement semantics, and all denominators.

# 17. Threats to validity

These validity labels are analyst organization [D], not necessarily the authors’ terminology.

**Internal validity:** matched seeds, fixed passages, matched style, controls, and paired tests help isolate memory effects. However, prompt rewrites alter several linguistic attributes, multi-memory entry manipulation adds distractors, and the factorial does not manipulate only an abstract scalar called entry. Baseline trace divergence can also reflect element-identifier differences rather than recommendation following.

**Construct validity:** RCR is closer to following advice than generic action disagreement, but it depends on judge interpretation. Baseline re-alignment measures resemblance to a potentially unsuccessful trace, not necessarily genuine task-correct recovery. A final success floor and a divergence-based conditional floor are different constructs.

**External/ecological validity:** AXTree browser tasks, hand-authored or model-drafted passages, and constructed traps support mechanism diagnosis. They do not establish real deployment attack prevalence, visual-agent behavior, uncontrolled web reliability, or attacker success at obtaining memory placement.

**Statistical conclusion validity:** paired tests and intervals are reported, including correction in Appendix A. Some selected-subset intervals include zero. Small factorial cells and the 16-task pilot constrain precision; ratio metrics become unstable near zero; captions occasionally overgeneralize their displayed cells.

**Reproducibility:** detailed software/hardware settings help, but absent artifacts and the Gemini-scope discrepancy prevent complete replay from the supplied document alone. Retry variation despite near-deterministic baseline framing is not fully explained. No independent execution was performed in this closed-document analysis.

# 18. Future work and open questions

## A. Explicit author-proposed directions

The authors leave to future work a functioning memory-management design that uses the diagnosed asymmetry, evaluation of transfer to terminal or embodied agents, and policies that predict memory usefulness before failure rather than waiting to retry. They hope E-P-R and MemTrapBench guide the design and evaluation of safer memory systems. [A; pp. 9, 24]

## B. Additional open questions [D]

Would the same base model show greater susceptibility as a browser agent than in a matched standalone response task? How much damage comes from propagation, irreversible environment transitions, and repeated presentation separately? Can a policy reduce conflicting uptake without suppressing helpful guidance? How reliable are the compliance and recovery annotations under human review? Would the channel pattern persist for genuinely retrieved website content rather than a controlled footer? Can horizon be varied within the same tasks to separate length from benchmark identity? What accounts for missing-valid-run pools and retry variability? These remain open rather than implied author findings.

# 19. Terminology and notation glossary

| Term | Beginner-friendly meaning |
|---|---|
| LLM | Large language model supplying the policy’s text/action decisions |
| Agent policy | Rule implemented by the model and interface for selecting the next action |
| Memory supply | Writing, storing, retrieving, and delivering experience |
| Memory consumption | How delivered advice affects subsequent decisions |
| E-P-R | Entry–Propagation–Recovery trajectory diagnostic |
| Entry | First memory-exposed action change or recommendation uptake, depending on metric |
| Propagation | Carrying an initial influence into later actions |
| Recovery | Returning to baseline-like behavior; separately, salvaging final success |
| AXTree | Accessibility-tree representation of a web page |
| UI | User interface, including buttons, forms, labels, and menus |
| ARIA | Accessibility-label mechanism named by the authors for exposing actionable targets |
| ReAct | Named reasoning-and-action interface used by the agents; action examples are supplied, full prompting is not |
| RCR | Recommendation Compliance Rate, based on a recommendation-specific LLM judgment |
| DPC | Damage Per Compliance, paired success loss within a selected subset |
| EDR | Coarser action-divergence proxy; an explicit full expansion is not supplied here |
| C_RCR / C_EDR | Judged-compliant / action-divergent task subsets |
| SR | Success rate, a percentage of tasks succeeding |
| pp | Percentage points, absolute difference between percentages |
| CI | Confidence interval, here paired bootstrap percentile interval |
| PF | Propagation factor, persistent-effect divided by early-effect |
| AHM | Action-history momentum, normalized resistance to late memory |
| bid | Target element identifier used in action comparison; the source does not expand the letters |
| DO/DON’T | Structured recommended and discouraged actions in a memory passage |
| DECOY | Diagnostic with a prominent plausible wrong option |
| UPTAKE | Diagnostic with an alternate route behind an Advanced control |
| GROUNDING | Diagnostic involving unavailable or mismatched memory-referenced information |
| OVERRIDE | Diagnostic testing advice to ignore an explicit correction |
| E+/E− | Single target memory / target plus three distractor memories in the factorial |
| G+/G− | Existing UI references / rewritten nonexistent UI references |
| M1/M2/M3/C1 | Raw reflection / workflow / contrastive DO-DON’T / quality-gated M3 |
| Retry-on-fail | No-memory attempt followed by helpful-memory attempt only after failure |
| Schedule oracle | Retrospective best fixed helpful schedule per task, using outcome knowledge |

# 20. Key numerical results

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| Full WebArena pool | 684 | tasks | Non-map distribution | Author-reported | p. 14, A |
| Excluded maps | 128 | tasks | Geolocation exclusion | Author-reported | p. 14, A |
| Diagnostic WebArena pool | 77 | tasks | Outcome-sensitive selection | Author-reported | pp. 5, 14 |
| Main MemTrapBench | 231 | tasks | S2–S8 | Author-reported | pp. 18, 21 |
| Separate pilot | 16 | tasks | S1 | Author-reported | Table 20 |
| Three-model trials | 5,928 | trials | 247×8×3 | Author-reported | Table 19 |
| Annotated traces | 4,851 | traces | 3×231×7 | Author-reported | p. 19, E.1 |
| RCR range | 63–72 | % | Five-model WebArena judged compliance | Author-reported | Table 2 |
| Qwen27B conditional DPC | 25.5 [11.8,39.2] | pp, 95% CI | Persistent conflict, judged subset | Author-reported | Table 2 |
| Gemini conditional DPC | 18.5 [3.7,33.3] | pp, 95% CI | Persistent conflict, judged subset | Author-reported | Table 2 |
| Qwen27B main conflict delta | −21.2 | pp | MemTrapBench persistent | Author-reported | Table 3 |
| Gemini main conflict delta | −26.0 | pp | MemTrapBench persistent | Author-reported | Table 3 |
| Main helpful delta range | +25.5 to +30.7 | pp | Four-model MemTrapBench persistent | Author-reported | Table 3 |
| Qwen27B divergence DPC | 26.6 [19.6,33.5] | pp, 95% CI | MemTrapBench action-divergence subset | Author-reported | Table 3 |
| Persistent conflict success | 1.3 | % | Each of three displayed main models | Author-reported | Table 22 |
| Qwen27B conflict recovery | 55.4 | % | MemTrapBench trajectory recovery | Author-reported | Table 22 |
| Qwen27B grounding effect | −29.7 [−45.1,−13.8] | pp, 95% CI | DECOY conflict factorial | Author-reported | Table 23 |
| Channel difference maximum | 0.5 | pp | Conflict system versus footer | Author-reported | Table 25 |
| Qwen27B helpful attenuation | 16.0 | pp | Footer versus system | Author-reported | Table 25 |
| Qwen27B retry-helpful success | 53.7 | % | MemTrapBench | Author-reported | Table 29 |
| Qwen27B memory-content retry gap | 28.6 | pp | Helpful retry minus no-memory retry | Author-reported | Table 29 footnote |
| DPC arithmetic example | 49.0−23.5=25.5 | pp | Displayed Qwen27B conditional rates | Analyst-derived | Table 2 |

No approximate graph readings are used as exact numerical results. The graph’s labeled bars are represented in Section 10; this reference table deliberately concentrates on the major quantities rather than duplicating all 29 tables.

# 21. Claim–evidence map

| Claim | Evidence | Figure/table/experiment | Source | Qualification / evidence strength |
|---|---|---|---|---|
| Consumption must be inspected after retrieval | Fixed-memory, varied-schedule paired design | X2; Fig. 2 | pp. 3–5 | HIGH for design; broader novelty not independently verified |
| Persistent conflict can amplify harm | Qwen27B early −7.8 versus persistent −20.8 pp; p=.013 | Fig. 3; X2 | p. 6 | HIGH for selected pool; not population prevalence |
| Similar compliance can yield different conditional damage | RCR 63–72%; DPC 2.1–25.5 pp | Table 2; X3 | p. 7 | HIGH reported; only two model intervals exclude zero |
| Pattern extends to constructed tasks | Conflict −9.5 to −26.0 pp and positive helpful control | Table 3; X6 | pp. 7–8 | HIGH reported; constructed benchmark scope |
| Recovery of actions need not salvage outcomes | Conflict recovery 45–61% with success 1.3% | Table 22; X12 | pp. 20, 22 | HIGH reported; recovery definition matters |
| Grounding intervention changes outcomes | Both grounding-effect CIs exclude zero | Table 23; X13 | pp. 21, 23 | HIGH within factorial; limited tasks/manipulations |
| Tested placement leaves conflict damage similar | System/footer maximum difference 0.5 pp | Tables 5, 25; X15 | pp. 8, 24 | HIGH observed; all-channel invariance untested |
| Short-horizon effect is weaker | MiniWoB persistent conflict 0/−2.9/+3.9 pp | Tables 6, 27; X17 | pp. 9, 25 | MEDIUM broader horizon inference; benchmark confounding |
| Helpful retries add more than no-memory retries | Reported row gaps 17.7/28.6/28.4 pp | Table 29; X19 | p. 25 | HIGH row evidence; caption contradictions and different valid pools |
| Paper informs a web-agent security mechanism | Misleading memory can direct multi-step browser actions | Methods; Tables 3, 22 | pp. 5, 20–22 | MEDIUM analyst inference; no standalone LLM comparison |

# 22. Very simple explanation — Explain Like I’m 15

Imagine a browser assistant trying to finish a complicated online task. Someone gives it a note saying how the task should be done. The note may be helpful, or it may confidently describe the wrong route. The researchers study when the assistant starts following that note, whether it keeps following it, and whether it can recover.

They find that being good at the task does not automatically make the assistant good at rejecting bad advice. In one selected set of browser tasks, different models followed wrong recommendations at similar rates. The stronger assistants sometimes lost more success because they had more ability to lose when the advice redirected them. This does not mean bigger models are always less safe.

The paper also separates looking corrected from actually fixing the task. An assistant might return to sensible-looking actions after submitting the wrong form, but the earlier submission may already have made success impossible. Watching the whole sequence reveals problems that a single final score or one corrected action can hide.

For the question about web agents versus standalone language models, this paper explains one possible source of extra risk: misleading information can influence a chain of actions in an environment. But it does not run a fair browser-versus-standalone comparison, so it cannot establish how much more vulnerable web agents are, or whether that difference always exists.

# Completeness Audit

The audit uses the inventory established before synthesis. **Represented in compressed form** means inspected and substantively accounted for, while detailed repeated cells or prose were condensed. It does not mean every source sentence was reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/preprint metadata | Yes, text+visual p. 1 | Yes | Fully represented | No venue invented |
| Abstract | Yes | Yes | Represented in compressed form | Orientation and main findings |
| §1 Introduction | Yes | Yes | Represented in compressed form | Problem, gap, contributions |
| §2 Related Work, all four categories | Yes | Yes | Represented in compressed form | External papers not independently reviewed |
| §3 Method overview | Yes | Yes | Fully represented | Content/schedule intervention |
| §3.1 E-P-R | Yes | Yes | Fully represented | Late exposure distinguished from recovery |
| §3.2 Compliance/DPC | Yes | Yes | Fully represented | Judging, subset, formula, sign |
| §3.3 Models/memories/statistics/testbeds | Yes, p. 5 text only | Yes | Represented in compressed form | Scope contradictions disclosed |
| §4.1 Retrieval pre-check | Yes | Yes | Fully represented | X1, Tables 1/17 |
| §4.2 Schedule effects | Yes | Yes | Fully represented | Exact Fig. 3 labels included |
| §4.3 Compliance trap | Yes | Yes | Fully represented | Conditional estimates and uncertainty |
| §4.4 MemTrapBench validation | Yes | Yes | Fully represented | Distinct divergence subset retained |
| §5 Placement/horizon/retry discussion | Yes | Yes | Represented in compressed form | Broader claims qualified |
| §5 stated limitations | Yes | Yes | Fully represented | Both explicit limitations |
| §6 Conclusion | Yes | Yes | Represented in compressed form | No new defense attributed |
| Central research question | Yes | Yes | Fully represented | Consumption across trajectories |
| Appendix explicit questions | Yes | Yes | Fully represented | Novelty, format, family, horizon, retry |
| Formal hypothesis list | Not present | Absence stated | Missing from supplied material | No list manufactured |
| X1–X19 experiment register | Yes | Yes | Represented in compressed form | All distinct analyses registered |
| Figure 1A | Yes, visual | Yes | Fully represented | Supply pipeline |
| Figure 1B | Yes, visual | Yes | Fully represented | Branching trajectory |
| Figure 2 | Yes, visual | Yes | Fully represented | E-P-R diagram |
| Figure 3a | Yes, visual | Yes | Fully represented | Helpful bar labels, axes, encoding |
| Figure 3b | Yes, visual | Yes | Fully represented | Conflict bar labels, axes, encoding |
| Figure 4a | Yes, visual | Yes | Fully represented | Cumulative entry; timing discrepancy |
| Figure 4b | Yes, visual | Yes | Fully represented | Conditional recovery, no uncertainty bands |
| Table 1 | Yes, visual+text | Yes | Fully represented | Full-distribution pre-check |
| Table 2 | Yes, visual+text | Yes | Fully represented | Compliance, counts, DPC, all CIs |
| Table 3 | Yes, visual+text | Yes | Fully represented | Main conditions, DPC, all CIs |
| Table 4 | Yes, visual+text | Yes | Represented in compressed form | Key family extremes and baseline floors |
| Table 5 | Yes, visual+text | Yes | Fully represented | All conflict placement pairs |
| Table 6 | Yes, visual+text | Yes | Fully represented | All benchmark/model deltas |
| Table 7 | Yes, visual+text | Yes | Fully represented | All policy successes |
| Table 8 | Yes, visual+text | Yes | Fully represented | Counts, DPC, CIs, p-values |
| Table 9 | Yes, visual+text | Yes | Represented in compressed form | Persistent conflict emphasized; repeats Table 11 |
| Table 10 | Yes, visual+text | Yes | Represented in compressed form | Ratios, instability, interpretation |
| Table 11 | Yes, visual+text | Yes | Represented in compressed form | All conditions accounted; repeated cells condensed |
| Table 12 | Yes, visual+text | Yes | Fully represented | All baseline/persistent/oracle values |
| Table 13 | Yes, visual+text | Yes | Fully represented | All control comparisons |
| Table 14 | Yes, visual+text | Yes | Represented in compressed form | Ranges, late conditions, exception |
| Table 15 | Yes, visual+text | Yes | Represented in compressed form | Strong-model contrasts and reversal |
| Table 16 | Yes, visual+text | Yes | Represented in compressed form | Means and all weak-preference gaps |
| Table 17 | Yes, visual+text | Yes | Fully represented | Formats, deltas, p-values, threshold |
| Table 18 | Yes, visual+text | Yes | Represented in compressed form | All four illustrative tasks |
| Table 19 | Yes, visual+text | Yes | Fully represented | Accounting and zero drops |
| Table 20 | Yes, visual+text | Yes | Represented in compressed form | Pilot baselines and primary effects |
| Table 21 | Yes, visual+text | Yes | Fully represented | Four gate roles and ranges |
| Table 22 | Yes, visual+text | Yes | Represented in compressed form | Recovery/success distinction, adoption caveat |
| Table 23 | Yes, visual+text | Yes | Fully represented | All cell success, main-effect intervals, ties |
| Table 24 | Yes, visual+text | Yes | Fully represented | All cells and additive summary |
| Table 25 | Yes, visual+text | Yes | Fully represented | Helpful attenuation and repeated conflict |
| Table 26 | Yes, visual+text | Yes | Represented in compressed form | All reported deltas and significance |
| Table 27 | Yes, visual+text | Yes | Represented in compressed form | Main controls; unshown condition flagged |
| Table 28 | Yes, visual+text | Yes | Represented in compressed form | Policies, baseline, oracle, closure caveats |
| Table 29 | Yes, visual+text | Yes | Fully represented | Main rows, recovery, gaps, denominators, conflicts |
| E1 DPC | Yes | Yes | Fully represented | Symbols and assumptions |
| E2 Four-gate chain | Yes | Yes | Fully represented | Conditional notation variation noted |
| E3 PF | Yes | Yes | Fully represented | Ratio caveats |
| E4 AHM | Yes | Yes | Fully represented | Possible negative values |
| E5 entry/recovery probabilities | Yes | Yes | Fully represented | Trajectory versus success |
| E6 oracle closure | Yes | Yes | Fully represented | Policy-class caveat |
| Numbered algorithms/theorems | Not present | Absence stated | Missing from supplied material | Workflow is prose, not invented pseudocode |
| Three introduction contributions | Yes | Yes | Fully represented | Conceptual, methodological, benchmark/empirical |
| Appendix A | Yes, p. 14 text only; p. 15 visual | Yes | Represented in compressed form | Implementation, audit, examples, disclosure |
| Appendix B | Yes | Yes | Fully represented | Metrics, judging, robustness |
| Appendix C | Yes | Yes | Represented in compressed form | Tables 9–17 all covered |
| Appendix D | Yes | Yes | Represented in compressed form | Eight templates and task accounting |
| Appendix E.1 | Yes | Yes | Represented in compressed form | Trace signals and absent JSON |
| Appendix E.2 | Yes | Yes | Fully represented | Conflicting/helpful factorials |
| Appendix E.3 | Yes | Yes | Fully represented | Delivery-channel ablation |
| Appendix F.1 | Yes | Yes | Fully represented | Cross-family boundary |
| Appendix F.2 | Yes | Yes | Fully represented | Short-horizon boundary and discrepancies |
| Appendix G | Yes | Yes | Represented in compressed form | Retry policy, content, oracle interpretation |
| References 1–52 | Yes, mostly text only | Yes | Inspected but deliberately omitted as repetitive/non-substantive | Categories and paper positioning retained; bibliography not retranscribed |
| Substantive footnotes/table notes | Yes where supplied | Yes | Represented in compressed form | Denominators, tests, dashes, thresholds, closure |
| Separate supplementary material | No separate files supplied | Absence stated | Missing from supplied material | No claim of artifact inspection |
| Trace annotation JSON | No | Absence stated | Inaccessible | Referenced file not provided |
| Code/tasks/memories/prompts release | No | Absence stated | Inaccessible | Promise of release is not artifact access |

## Missing or inaccessible material

No physical page within the supplied 1–25 text sequence is missing. Visual renderings of pages 5, 10, 11, 13, and 14 are absent, so their layout and any unextracted objects cannot be independently inspected visually. The named trace annotation JSON and promised code, tasks, memory passages, and prompts are absent. No independent experimental logs or supplementary archive were supplied. Absence of separate artifacts limits reproduction, not the ability to read the supplied main text.

## Uncertain interpretations

Unresolved issues include Gemini’s actual WebArena evaluation configuration; whether Table 3 uses judged compliance anywhere beyond its explicitly stated divergence subset; exact Figure 4 entry timing; MiniWoB median horizon; retry-no-memory ranges and recovery summaries; varying valid-run denominators; exact preference and groundability operationalization; and whether all broader channel, architecture, and multiplicative-gate claims follow from the narrower manipulations. Numerical rows are retained where prose disagrees, without claiming the rows are independently verified ground truth.

## Deliberately compressed material

The bibliography, repeated recovery rows, repeated channel results, illustrative memory passages, and secondary per-condition cells are compressed. All numbered figures and tables have individual coverage entries. No attempt is made to reproduce the complete 4,851-trace annotation, which was not supplied. The full numerical tables are represented through their principal comparisons, uncertainties, exceptions, and role in the argument rather than a transcription of every cell.

## Potential omissions

No known numbered figure, numbered table, main section, substantive appendix, or major equation in the established inventory is entirely unrepresented. This is coverage of the supplied paper, with disclosed compression and unresolved source inconsistencies; it is not a claim that every sentence, numerical cell, external reference, or absent implementation artifact has been preserved or verified.
