# Iteration 3 source review

Starting state: fifteen valid completed papers, ninety pending, seven B02–B08
exclusions. Thirty completed-output fingerprints and twelve historical/runner/
schema fingerprints are saved in `iteration3_baseline.json`. Selection reasons
and source identities are in `iteration3_selection.json`.

Review is proportional, selected source evidence, not exhaustive sentence/visual
verification or independent human scientific validation. Attack outcomes retain
victim configuration, attacker control, endpoint and denominator. No standalone
vulnerability ordering is inferred from unrelated capability scores.

## AdvAgent

Read source abstract, attack metric and main/transfer/defense results. Visually
inspected physical p.6 (Table 1 and the evaluation definition). Reviewed all
fifteen structured claims, comparison fields, results, limitations and validity.
Step success requires an exact adversarial triplet: operation and target element
are preserved while the argument changes. Hidden aria-label content influences
HTML grounding rather than necessarily changing the screenshot. The four-domain
440-task corpus is split 240 training/200 test; 97.5 +/-2.0 and 99.8 +/-0.3 describe
domain-average results/variation, not repeated-run uncertainty or realized harm.
Reuse and transfer start with successful attacks and retain their conditional
sampling. Three prompt-based defenses do not establish failure of all defenses.
Five figures, six tables and two algorithms are represented in the output.

Four headings were restored without body edits. C10's exact line-break
hyphenation was restored. Original raw response and correction notes retained;
all fifteen claim groups pass the existing checks. No completed stock purchase
or matched standalone-LLM vulnerability comparison is claimed.

## EIA source review (generation pending)

Read attack construction, 177 selected action-step dataset, ASR definition,
main results, full-request variant and mitigation. Visually inspected physical
pp.7 and 9: Table 1 and Figures 3-4. Peak 70% is GPT-4V/MI/P+1, not an
average over positions/models; peak 16% uses visible Relaxed-EIA full-request
injection. ASR requires injected-element selection and typed-value similarity
>0.95. Next-step functional-integrity measurements do not establish whole-task
completion. Automatic submission is described, but the aggregate ASR does not
separately quantify server-side exfiltration. VirusTotal non-detection is scoped
to the tested traditional tool. Prompt warnings leave similar ASR in the tested
settings; supervision advice is a proposal, not an evaluated containment defense.

## Batch one readback

Both deliverables exist, Markdown equals record narrative, source identity and
progress fingerprints match, and existing quality checks pass: 15 AdvAgent and
14 EIA supported claim groups. EIA represents all 28 figures and Table 1; key
results and all fourteen claims reviewed against selected evidence. Its reported
MI variance 0.461 is retained and flagged (displayed-cell population variance
approximately 0.04614); aggregation wording also remains unresolved.
Counts after batch: 17 completed, 88 pending, 7 excluded, 0 failed. Catalog has
17 records. All starting deliverables and protected fingerprints remain intact.

## Pop-ups source review (generation pending)

Read threat model, model/task settings, metrics and main results; visually
inspected physical p.4 Table 1 and Figure 3. Five dated victim model versions,
50 selected OSWorld tasks and 72 VisualWebArena tasks; default attack assumes
true user query and precise coordinates/SoM ID, with weaker alternatives tested.
ASR is clicks per injected step; TASR is tasks with at least one such click.
Clicks are suppressed in execution: malware download, redirect and realized
harm are author-proposed consequences rather than tested endpoints. SR/OSR
remain task completion metrics. Step-wise defense Table 8 has 5.9% ASR but
32% TASR and 8% SR vs18% OSR; removing Please click raises ASR10.4/TASR44.

## Pop-ups retained-response checks

All fifteen structured claims and comparison fields reviewed. Three section
labels restored; five evidence quotations restored source hyphenation/line breaks,
without changing scientific claims. Original retained; existing quality checks
pass. Ten tables and ten figures are represented. Physical p.7 defense tables
visually checked in addition to p.4. Headline aggregation and introductory
25%-relative defense wording remain flagged rather than silently reconciled.

## AgentDojo source review (generation pending)

Read four stateful simulated environments, tools, task/security definitions,
metrics and defenses; visually checked physical p.20 Tables 3-5. 97 user tasks,
27 injection targets, 629 user/injection pairs. 70 tools in Table1 caption versus
74 in main prose and sum of rows; tool filter prose7.5% versus Table5 6.84%.
GPT4o no-defense ASR differs across model/attack/defense tables:47.69/57.7/57.69;
retain protocol context. Targeted attacker-goal fulfillment and complement of
utility under attack have different meanings. Attack-induced utility failure
is not necessarily fulfillment of a malicious goal. Tool filtering helps when
read-only user tasks can drop write tools; not a guarantee when necessary tools
also permit the malicious goal (17% of test cases per prose).

## Batch two readback

Pop-ups and AgentDojo finalized through existing runner. Markdown/narrative,
source identity, completed fingerprints and quality checks passed (15 and16
claim groups). Reviewed all AgentDojo claims, comparison fields and main tables;
21 figures/five tables represented. Discrepant source numbers retained; no
scientific replication claim. Counts19 completed/86 pending/7 excluded/0failed;
catalog19. All starting outputs and protected fingerprints unchanged.

## SecureWebArena source review (generation pending)

Read threat model, task construction, metrics, annotation and main results.
Visually checked physical p.6 Table2. Malicious users control goal text;
environmental attackers control DOM/CSS/content but not chrome/system prompt.
330 tasks: five cases/vector/environment with six jailbreak variants,55 per
environment; nine agents yield2970 trajectories/8910 stage decisions. RVR uses
initial generated reasoning judged by GPT4o (85.5% agreement on200 traces);
BCR expert trajectories (kappa0.88 on10% dual annotation); PDR state logs.
Pop-up PDR76.67–100% belongs to this final-outcome protocol, not the Pop-ups
paper's suppressed-click rate. No tested defense or standalone control; category
differences and case-study root-cause labels are observational interpretations.
Table2 includes unusual20.20/23.30 entries; retain reported precision. Live
Amazon/Wikipedia limited to two user-level attacks; no live environmental test.

## SecureWebArena retained-response checks

All twelve claims and comparison fields reviewed; four source-hyphenation quotes
restored, original retained. Existing quality checks pass. Seven figures/four
tables represented; Table2 key rates and stage/annotation semantics checked.
Prose incorrectly attributes GUI80/76.67 pop-up rates to AdInject (Table2 both
3.33); summary flags this and live wording/denominator inconsistencies.

## WASP source review (generation pending)

Read attacker capabilities, URL/plain-text templates, scaffoldings, metrics and
main results. Visually checked physical p.7 Table2. Attacker may add issues/posts/
comments but cannot edit layout, add pop-ups or modify others' comments. Default
knows legitimate task; task-agnostic variants tested. URL fragment persists in
current-URL context even without long history. Authors report84 attack tasks and
37 utility tasks; per-environment wording needs qualification against21 total
goals. Intermediate ASR uses GPT4o trace judgment; end-to-end checks final state.
o1 system-role tool loop85.7% intermediate/16.7% final vs developer58.3/15.5;
not matched standalone control. Zero final success can reflect weak capability.
No defense credited as universally effective from one prompt/hierarchy variant.

## Batch three readback

WASP16/SecureWebArena12 claim groups pass existing checks; completed source/
output fingerprints and Markdown-narrative readback passed. All WASP claims and
comparison fields reviewed; three figures/seven tables represented. Denominators
and conditional arithmetic retained; source inconsistencies flagged.
Counts21 completed/84 pending/7 excluded/0failed;catalog21. All starting outputs
and protected files unchanged.

## Spotlighting source review (generation pending)

Read models, synthetic1000-document keyword-payload metric, transformations,
security results and utility tests; visually checked physical pp.7 and9.
Text-davinci003, June2023 GPT3.5/GPT4 attemperature1. ASR strict keyword-only
response differs from affirmative-response rate, not a browser side-effect.
Datamarking GPT3.5 summarization3.10% (prose below3 discrepant), Q&A8.0%;
GPT4 Q&A1%; Text0030%. GPT3.5 encoding summarization0/Q&A1.8%, but poorer
SQuAD/IMDB/WiC/BoolQ utility versus GPT4. No adaptive attack robustness proof,
no browser-agent versus standalone control; zero observed is not impossibility.

## Spotlighting retained-response checks

All15 claims/comparison fields reviewed. Three heading labels restored with
original retained; quotations already passed. Nine numbered figures and an unnumbered scoring
table represented. Numerical/task utility results and limitations preserved.

## IsolateGPT source review (generation pending)

Read attacker scope, trust assumptions, benchmark/security metric and case-study
permission assumptions. Visually checked physical p.10 TableI.1598 attacks,
including544 added system-data scenarios; paired systems bothGPT4. Vanilla
20.2% ASR differs from Isolate7.6% permission-dialog frequency and100% warnings
conditional on appearances. Protection depends on refusing malicious permission
flows; appendix reproduction explicitly assumes warning rejection. Within-app
injection compromise out of scope; cross-app propagation is target. Trusted hub/
operator/hosting and explicit mediated collaboration are architecture assumptions,
not a guarantee against arbitrary compromised operators or user approvals.
Performance103 queries,20single/20multiple/21collaboration/42noapp.

## Batch four readback

Spotlighting15/IsolateGPT14 supported claim groups pass existing checks; source/
output fingerprints and Markdown-narrative readback passed. All IsolateGPT claims
and comparison fields reviewed; nine figures/four numbered tables represented.
Fare example physicalp.11 visually checked ($57 vs$51.80, derived$5.20);
warning/permission scope and cold-start timing limitations remain explicit.
Counts23 completed/82 pending/7 excluded/0failed;catalog23. All starting outputs
and protected files unchanged.

## ceLLMate source review (generation pending)

Read trusted-browser assumptions, HTTP enforcement, policy selection datasets
and scripted security case. Visually checked physicalp.11 Tables1/2. Chrome
extension requires no malicious competing extension; agent cannot change
browser settings/access local files/devtools; single-turn scope.219 selection
tasks:149retail/36travel/24versioncontrol. Domain text132zero versus table136
zero-domain denominator; retain discrepancy. Retail argument accuracy84.38/
81.25/96.88% (32cases), not policy selection96.64/97.32/99.32%(149cases).
12 GitLab automation scripts emulate fully compromised agent; all12blocked
for disallowed goals under selected read/write-issue policy. This is enforcement
emulation, not live prompt-injection ASR; misuse inside allowed comment actions
is explicitly outside evaluation. Complete HTTP interception/sitemap and correct
policy are conditions, not automatically proven for every website.

## Final batch and operational stop

ceLLMate: all15 claims/comparison fields reviewed; three headings/five exact
quotations repaired with original retained. Eleven figures/two numbered tables
represented; selected Table1/2 visual evidence, security scope, key counts and
latency arithmetic reviewed. Existing quality and final readback pass.

Task Shield: extraction retained, no model response or completed deliverables.
Existing CLI reported account usage exhaustion; runner classified it as
OPERATIONAL_USAGE_LIMIT, left paper pending and stopped model dispatch. Provider
message said try again at1:47PM; timezone/actual restored capacity not established.
No new model calls after this stop. ceLLMate finalization reused retained output.

Iteration outcome:15 starting+9new=24completed,81eligible pending,7excluded;
0failed,1selected deferred(TaskShield). This is an operational interruption,
not a scientific failure or a completed ten-paper iteration.

## Task Shield completion review — 2026-10-10

This addendum supersedes the pending status in the historical stop note above.
The targeted runner generated the Task Shield response; one nonexact quotation
(claim_05, physical page 7) was repaired by restoring source line-break
hyphenation. Original response, correction notes and prior usage-limit log are
retained in the paper evidence directory. Added exact supporting passages for
the pre-execution call boundary (p.5) and the main Table 2a row (p.8). Claim_04
explicitly separates the reported one-trial setup from analyst interpretation.
Retained-output retry passed existing validation without another model call.

Reviewed the source identity and all 12 structured claims/comparison fields,
ordered comprehensive sections, 7 figures/7 tables, physical page references,
main GPT-4o/mini metrics, ablations and latency values. Selected reviewer renders:
pages 5, 8 and 14. The main 2.07% ASR/69.79% attacked utility result is scoped to
GPT-4o under Important Instructions on AgentDojo; mini values are 2.23%/54.53%.
Clean utility, attacked utility and target ASR remain separate endpoints.
Exact denominators are not supplied; do not transfer AgentDojo's separately
reported case counts into this paper as established evaluation counts.

Retained source concerns: T2a/T4 Slack utility 64.76/50.48%; restatement prose
63.8→43.8 versus T3 full-shield 50.48→43.80%; nonuniform defender-capacity trends;
threshold/prompt-schema ambiguities detailed in narrative section 14. No measured
adaptive campaign, standalone comparator or open-source evaluation. Input Shield
versus full shield trades utility/latency against residual ASR in the mini Slack
condition, without establishing universal superiority.

Final readback: 25 complete, 80 pending, 7 excluded, 0 failed/deferred. Previous
24 output pairs preserved. Updated synthesis distinguishes semantic alignment,
input screening/provenance, app isolation, capability filtering and HTTP
authorization. No cross-paper ASR ranking or independent scientific certification.
See [completion validation](iteration3_completion_validation.json).
