# Iteration 4 source review

Starting state verified on 2026-10-10: 25 completed / 80 eligible pending /
7 excluded / 0 failed or deferred. All 25 starting pairs passed existing quality,
fingerprint and Markdown/JSON readback; catalog identities matched. Selection
balances 20 pending papers across 11 categories in ten two-paper batches;
see `iteration4_selection.json`. Prior 50 deliverable and 12 protected-input
fingerprints are retained in `iteration4_baseline.json`.

## Batch 1 — VisualWebArena and WebGPT

VisualWebArena source inspected: ACL 2024 Volume 1 Long Papers, printed pages
881–905 / 25 physical pages. Main Table 3 visually reviewed on page 8:
GPT-4V + SoM task success 16.37%; model benchmark has 910 tasks. Human performance
88.70% uses 230 sampled template tasks and seven participants (p.6), not the
same evaluation denominator. Text-only/caption/multimodal agents all retain web
actions: this is not a matched standalone-LLM security comparison. Table 2
execution checks and Figure 3 action trajectory are capability evidence;
unsuccessful legitimate tasks are not attack successes. New outputs pending.

WebGPT source inspected: arXiv:2112.09332v3, 1 June 2022, 32 physical pages.
Source text pp.1,5–7,9 and reviewer render p.7 checked. Reported 175B best-of-64
ELI5 preferences: 56% versus browser demonstrators / 69% versus Reddit answers;
ties count as 50%, references stripped for the latter with different judging
instructions/contractors. Main evaluation uses temperature 0.8 / max100 browsing
actions. TruthfulQA compares base GPT-3 with WebGPT, but automated judging for
GPT-3 versus human judging for WebGPT, different fine-tuning/rejection sampling,
and answer truncation mean this is not a matched security comparison. TruthfulQA
truthfulness/informativeness measures do not demonstrate prompt-injection ASR.
Browser search/click/quote workflow supplies retrieval and citation exposure;
security consequences require separate evaluation. New output pending.

Batch 1 completion: both outputs validated through retained-response retry.
VisualWebArena: 15 claims; 17 figures/6 tables represented. One quote restored
source hyphenation; 314 templates versus 230-task one-per-template human sample
and Figure 17 click [11] versus croissant comments [16] remain source concerns.
Post-submission GPT-4o result 19.78% is distinct from main GPT-4V SoM 16.37%.
WebGPT: 15 claims; 3 heading labels aligned to existing requirements, no missing
substantive sections. Exact quotations passed. Training, evaluator differences,
preference ties, reference overreliance and hypothetical live-web actions remain
qualified. Current state 27 complete / 78 pending / 7 excluded / 0 failed.
Prior 50 outputs and 12 protected fingerprints unchanged. No extra model calls
for these retained-output repairs.

## Batch 2 — AGENTVIGIL (AgentFuzzer mapping) and Context Manipulation

Source under AgentFuzzer filename is AGENTVIGIL arXiv:2505.05849v4, 14 June2025,
14 pages; retain stable mapping and actual title. Source hash f41a7b42c8e11de2
(full identity retained in selection); separately mapped AgentVigil source hash
is distinct, so do not rename/deduplicate by similar titles or count versions as
independent scientific replication. Source pp.1,5–9 and reviewer render p.8
reviewed. AgentDojo fuzz142/test173, 3 mutations/iteration over10 iterations,
quarter-task seed evaluation, top5-seed transfer union. VWA-adv text-trigger
fuzz99/test100, 10 mutations/iteration over10 iterations. Cumulative/prose70%
versus selected-prompt-table60% VWA-adv fuzzing remains unresolved; held-out
GPT-4o test59% is separate. AgentDojo repeat defense row12% versus baseline21%
contradicts blanket superiority language. Local Magento case demonstrates URL
navigation; do not infer completed download/exfiltration from broader prose.
No matched standalone-agent security control identified in supplied experiments.
New output pending.

Context Manipulation source inspected: ICML2025 Computer-use Agents workshop,
Patlan/Hebbar/Viswanath/Mittal, 10 pages. Source pp.1,3–8 and reviewer render p.8
checked. Systematic direct stored-context/plan modification requires attacker
memory access; earlier indirect-memory examples from related work do not prove
that this paper establishes end-to-end webpage-to-memory compromise. Plan
benchmark: 4 categories ×15 samples ×5 repetitions (300 runs per stated attack
condition, analyst-derived if used); WebVoyager-Privacy:45 tasks from9 domains×5,
repeat details not transferred from the other benchmark. Partial tool access
versus full data exfiltration are distinct endpoints in Figures5/6. Task alignment
35.6% versus context chaining53.3% privacy result differs by17.7 percentage points,
not17.7% relative. Strong/weak retrieval PI and plan/memory manipulation use
different access/frequency conditions. Task-aligned payloads were not evaluated
against Task Shield. No matched standalone-agent security comparison identified.

Batch 2 complete: AGENTVIGIL15 claims; Context Manipulation14 claims. Three/one
source-hyphenation repairs respectively; original responses/corrections retained.
Quality and final readback passed; no additional model calls for output repairs.
AGENTVIGIL generation recovered after two CLI stream reconnects; no usage limit.
29 complete /76 pending /7 excluded /0 failed. Prior50 output/protected12
fingerprints unchanged. Source concerns remain review flags, not blocked papers.

## Batch 3 — Autonomy Comes with Costs and SafeArena

AgentDoS source inspected: USENIX Security2026 Proceedings, cover p.1, main
paper starts physicalp.2, 21 pages total. Textpp.2,4,9–13 and reviewer renderp.13
checked. Natural-language requests invoke resource-intensive functionality;
static/grey-box testing sees code/traces, while deployment attacker has prompt
API access. Short-/long-/full-lifecycle retention creates different accumulation
budgets. Findings:36 vulnerabilities in16/20 applications;15 assignedCVEs.
Recall36/38=94.7% uses constructed discovered-plus-two-manual-miss set, not all
possible defects. Minimal Docker resources/default4GB RAM10GB disk, GPT-4.1,
temperature0,20min/sink and early skips qualify results. Table4 scheduling FN13
versus prose9 retained. Precision100% is author-reported manual confirmation,
not independent reproduction. 9.32M tokens/agent and estimated$44.3 use author's
August2025 pricing, not current prices. No matched standalone security comparator.
New outputs pending.

SafeArena source inspected: PMLR267 /ICML2025, 38 pages. Textpp.1,4–8 and
reviewer renderp.8 checked. Deliberate malicious-user requests with task-granted
permissions, not indirect injection into a benign request.250 safe/250 harmful
paired tasks across4sites/5categories. GPT-4o functional harmful TCR22.8% differs
from LLM-judged ARIA-4 34.7%; Qwen functional26.0% versus ARIA-4 27.3%. NSS uses
only corresponding safe-task successes as denominator, not all250 pairs. ARIA-3
attempted-but-failed differs from ARIA-4 completion and ARIA1/2 refusal. Human
annotation on150 human-designed harmful tasks for2models; kappa.96 between
humans, .82 model/human on human-agreed subset.49 selected initially refused
Claude tasks were manually jailbroken with≤3attempts/mean1.26; do not imply
benchmark-wide100%completed harm. Standalone control not identified; safety-
alignment transfer claim is interpretation from agent behavior, not matched
LLM/agent ablation. Automatic completion metrics can miss other undesirable
behavior; external classification defense proposed, not evaluated here.

Additional SafeArena analyst check: if the same250 paired functional outcomes
in Figure3 feed the binary NSS formula onp.5, GPT-4o safe34.4%=86 and harmful
22.8%=57 imply NSS≥1−57/86≈33.72%, whereas Table3 reports31.7%. Claude safe
21.2%=53 and harmful7.6%=19 similarly imply NSS≥64.15%, versus reported55.0%.
Thus published NSS cannot be reconstructed under that matching assumption.
A different reward/aggregation/subset may be used, but it is not established by
this check. Retain published values and flag missing aggregation explanation;
do not replace NSS with these bounds or label an inferred alternative as fact.

Batch3 complete: AgentDoS13 claims /SafeArena15 claims.3heading-label repairs
each and1SafeArena exact source-hyphenation repair; originals retained. SafeArena
NSS aggregation concern added explicitly as qualified analyst check, no reported
result replaced. Full existing quality and final readback passed.31complete /
74pending /7excluded /0failed. Prior50outputs/protected12fingerprints unchanged.
SafeArena recovered after1CLI reconnect. No additional model call for repairs.

## Batch 4 — PlanGuard and AgentRewardBench

PlanGuard source inspected: Gong/Deng, 7pages, publication venue/date not visibly
established. Textpp.1,3–6 and reviewer renderp.5 checked. Isolated planner sees
trusted user/tool definitions; hard rules exact-match or reject unauthorized tool;
LLM verifier reviews valid-tool argument differences using agent reasoning.
DeepSeek-V3.2 victim/planner/verifier; victim system deliberately instructed to
obey commands in tool outputs.1054 InjecAgent attack cases/17user tools/62attacker
tools, but split sizes/benign FPR denominator/repetition details unspecified.
Both Stage-I/full achieve0observed ASR; StageII reduces FPR27→.97%DH and38.01→
3.28%DS. Abstract aggregateASR72.8%/FPR1.49% not reconstructed without weights.
FPR is not end-to-end legitimate task completion. No quantified latency/cost or
adaptive campaign, no formal end-to-end impossibility proof. p.6 acknowledges
context-dependent argument verification lacks ground truth. Agent reasoning/
parameters supplied to semantic verifier remain potential attack-bearing inputs.
No matched standalone comparator. New output pending.

AgentRewardBench source inspected: COLM2025,23pages; textpp.1,4–8 and reviewer
renderp.7 checked.1302 trajectories/351unique tasks,196dev/1106test trajectories
and51dev/300test tasks;3binary labels/trajectory. Success, unintended side effect,
and repetition are separate. Best overall LLM success precision69.8%, not
accuracy;≈30.2%of predicted successes false, not30.2%of all trajectories.
Official rulesP83.8/R55.9/F1 67.1; GPT-4oA judgeP69.8/R83.1/F1 75.9. Human
agreement89.3% checked onGPT-4o WebArena subset, not all trajectories/labels.
GPT-4o human/rule task success35.9/17.4%VWA and42.3/25.6%WA are18.5/16.7pp
absolute gaps, not relative percentages. Table2 side-effect precision6.5–7.2%
is label/representation-specific. Existing judge implementations adapted to newer
backbones. No adversarial judge experiment or matched standalone susceptibility
control; misleading agent reasoning is observed evaluation failure. Findings
qualify measurement reliability without adding a new validation infrastructure.
New output pending.

## Batch 4 committed

PlanGuard (17 claims) and AgentRewardBench (16 claims) validated and committed from retained responses. Required headings and exact source hyphenation repaired; original responses retained. PlanGuard Figure 1 transfer detail checked visually; its extracted caption identifies the figure rather than transcribing image text. AgentRewardBench Tables 9–12 repeat Table 8 despite agent-specific captions; these are flagged, not counted as independent measurements. Figure 5 optimality prompt differs from three reported binary annotation dimensions.
Current state: 33 completed / 72 pending / 7 excluded / 0 failed.
All 50 previous output and 12 protected fingerprints unchanged.

## Batch 5 source review in progress

IRLbot identity: ACM Transactions on the Web3(3), Article8, June2009, DOI10.1145/1541822.1541823,34physical pages; authors Lee/Leonard/Wang/Loguinov. Earlier WWW2008 version distinguished. Sourcepp.1–4,26–31 checked. Crawl June9–August3,2007 with maintenance pauses:41.27active days, quad-CPU2.6GHzOpteron/16GBRAM/24-diskRAID5/1Gbpslink. 7,606,109,371attemptedconnections,7,437,281,300HTTP replies,6,380,051,942HTTP200text/html responses; unique URLs do not establish unique content. No content duplicate prevention (p.30). Average319Mb/s or1789pages/s; peak10-minute470Mb/s/3134pages/s, imposed day/night bandwidth limits. 41.5billion discovered unique nodes are not downloaded pages or useful content. Reputation/budgets resist branching spam, DNS host proliferation and delay traps; no LLM/prompt injection or matched standalone-agent comparison. Most top1000domains manually judged legitimate without exact spam precision/recall; distributed scalability discussed/estimated rather than demonstrated. DRUM asymptotically quadratic under fixed memory, near-linear stated operational range, not unbounded linear guarantee. These are availability/scalability mechanisms rather than semantic authorization defense.

IRLbot returned:14claims pass existing structural/schema/exact-quote checks; Figure7 on physicalp.27 visually checked. The34-page identity matches the authorized source. All7figures and9tables covered; important measured/projection distinctions preserved. Finalized output exists; batch progress awaits second paper.

Toward Secure LLM Agents source identity: Ling/Yu/Chen/Fang, arXiv2606.10749v2,23August2026,40pages. ACMCSUR1(1)/January2026 template and DOIXXX.XXX are not verified archival publication. Survey reports247papers through April27,2026:209database+42LLMassisted+24snowball=275,24excluded and4duplicate merges;3independent authors annotate, Fleissκ.86 reported. Counts measure literature attention, not vulnerability frequency/effectiveness. Multi-label technical counts/co-occurrence matrices must not be summed as partitions or interpreted as intrinsic benchmark properties. Paper-type/system-setting/year fields partition247;169arXiv/12web/55conference/11journal. No original attack/defense experiments or matched standalone-agent trial. Table11 defense stacks explicitly engineering interpretation, not validated standard. Prior-study examples remain secondary evidence, not independently rechecked source results. Suggested new security infrastructure is paper content, not an instruction to modify this workflow.

## Batch 5 committed

IRLbot14claims and Toward Secure LLM Agents15claims validated, source-bound and committed. All seven IRLbot figures/nine tables and all seven survey figures/eleven tables represented in narratives; reviewer renders physicalpp.27(IRLbot)/40(survey) inspected. Survey Figure6 inter-agent row has21Inter-agentComms versus16Coordination, contrary to nearby strongest-Coordination prose; Figure5 denominator unclear. These remain flagged without invented reconciliation. All50prior output and12protected fingerprints unchanged. Current35completed/70pending/7excluded/0failed; no usage stop.

## Batch 6 source review in progress

WebLINX: Lù/Kasner/Reddy, supplied50-pagepaper, real-world multi-turn conversational navigation. Sourcepp.1–9,20checked andFigure2physicalp.3visually inspected.2337expert demos/155websites/15geographies,100514total turns,51010active model/evaluation turns (Table8 summation);8trained annotators in instructor/navigator pairs. Main experiment static teacher-forced next-action prediction, not rolled-out end-to-end task success or security attacks. Micro-average combines action-specific intent/IoU/F1 scores; Llama2-13B37.0IID/25.2OOD, GPT4Vzero-shot12.9/10.4 not percenttaskscompleted. DMR claimed5×faster against916msbaseline, target retrieval can omit relevant elements; not a security defense. Table8 split demos969train/100valid/100IID/223CAT/211WEB/444VIS/290GEO sum2337; Figure2 labels1404/140/146/1692 exceed unique demos and relate to multi-category linkage, requiring qualification rather than assumed extra unique cases. Direct model errors/password-field mishandling are benign errors not attack successes. Author recommends human supervision and research-only deployment; no measured safeguard intervention or matched standalone-agent attack condition.

WebLINX draft14claims passes after three heading-label repairs; exact support quotations all matched. PreciseTable28scores37.09IID/25.21OOD differ slightly from main rounded Table4; use table-specific values. 402alternative-actionannotations across134validationturns, not full task trials. DMRMiniLM186ms versusDeBERTa916ms and OODRecall@10 51.87/54.78 remain retrieval-specific. No paid retry needed; commit awaits active batch end.

WebWalker identity: ACL2025longpapers10290–10305,16physicalpages, Wu etal. Sourcepp.1,3–8,13–14checked and mainTable3/Figure5p.6renderinspected.680QA pairs,340single/340multi, each80easy/140medium/120hard;1373pages not questions. Explorer selects sublinks/markdown, critic gathers memory and answers;15stepcap/top_p.8/zero-shot. GPT4oWebWalker37.50% versusReAct33.82/Reflexion35.29%; actioncount4.67vs3.83/4.27 is conditional on correct executions, not overall resource cost. Sixbackbonesintable despitetextnine. Qwen32BReflexion23.26% lower thanReAct25.44, so superiority notuniversal. No-retrievalGemini/o1baselines8.08/9.85 compareQA with differentbackbones, not matchedsecuritysusceptibility. Domainprose/figurepercentconflict, annotationexampleindustrytrackURL versusstudentworkshopgoldpath; flagratherthanguess. Qwen7BReActoverallAC2.99 is lowerthan allsixreported subgroupACvalues(min3.36), so weighting/aggregationunreconstructible. Official-source content not proof of instructiontrust. No attack/defenseexperiment.

## Batch 6 committed

WebLINX14claims andWebWalker15claims validated and source-bound, Markdown/JSONreadback passed; originalresponses retained. Required headings and one exacthyphenation repaired without paidretry. Relevant figures/tables individually inventoried in narratives. All50previous outputs/12protected inputsunchanged.37completed/68pending/7excluded/0failed. No matched standalone/web-agent securitycomparison in these two capabilitypapers.

## Batch 7 source review in progress

ToolHijacker actual PDFtitle Prompt Injection Attack to Tool Selection in LLM Agents, Shi/Yuan/Tie/Zhou/Gong/Sun,18pages. Sourcepp.1–2,6–8,10–12checked andp.12Figure8/TableXrenderinspected. Tool-library write inserts maliciousdocument; no-box assumesunknownvictimretriever/model/library/taskphrasing/topk, attacksoptimized onshadowtools/model. RetrievalR plusselectionS targetseparateboundaries. MetaTool199benigntools, ToolBench9650aftercleaning (original16464);10targettasks×100phrases/dataset, attacktraining5shadowphrases/task. ASR=malicioustoolselected, AHR=retrievedtopk, not toolcall/exfiltration/harm. GPT4o gradientfreeASR96.7%Meta/88.2%ToolBench; gradientbased92.2/83.9. TableIIAHR99.9/100%Meta forGF/GB versusabstract100generalclaim. StruQ/SecAlign fine-tunedtargets ASR97.5/99.6%MetaGF, attackedselectionaccuracy2.5/.3%; utilityproxy notfulltaskutility. Detection10maliciousdocs versus199/9650benign; FNR90%means9/10missednot900/1000tasks. Datasentinel90% exactly forgradientbased vs proseexceeding90; MetaPPLFPR1.01% versusheadline<1. Nativeplotglyphs corrupted, renderedFigure8supportsdeltaASR notabsoluteASR. No matched standalone-agent securitycomparison. Threatmodelallowsmalicioustoolimplementationbutreported endpointstopsatselection.

ToolHijacker returned15claims; structural/schema/quotechecks pass afterretainedheading/TH-C10hyphenationrepair. No harmful toolsdeveloped/deployedonline(ethicsstatement), important endpointqualification; non-target0/.11%malicioustoolselection not fullcorrectness. Fulltargettasks/attackerprompt referencedtechnicalreportabsent, notpretendedreviewed.

Hidden in Memory: Pulipaka/Hlebik/Raghav/Abdelnabi/Raina/Sheth/Fritz, ICML2026AIWILDworkshop,81pages. Sourcepp.1–9,50,57,71,77–79checked. Externaldocument attacker induces fabricateduser memory without directstorewrite, later absent.700injectionpairs(500behavior/200actions),400postinjectiongoals(200each; adjacent/distantqueries), stagewise decoupled tobalance models. ToolmanagedbehaviorGPT5.5IR99.8±.3%,Kimi95±1.9 notall700; toolactionGPT5.5IR91.5±3.8,Claude6.5±3.5. ExternalmanageradjacentagentRR94–98%, AUR60–89%conditionalretrieval. Intro erroneouslycalls60–89retrieval; use definitions/Table2. Table36coupled fixedattackexternalmanagerE2Eagent3–66%/behavior41–73.9%, distinctpipelinefivebackbones; do notmultiplymainTable1/Table2marginals orpoolregimes. E2Esem estimated using externalmanagerusage, notfulljointempiricalsemanticretrievaltrial. Provider-style100samplefullharnessswap GPT5.5IR97/3/1%GPT/Claude/Geminisetups, notmodelintrinsics orstandalonecontrol. DefenseACvsadaptiveAC+; GEPAKimiBehavior6.2→64.6,DeepSeektable25.2vsprose21.8unresolved. Benignsave70/cell×6models×2defenses840,write≥98.6%semanticmatch87.1–100%; no undefendedbaseline or ordinarydocument-memoryutility, so notproofnoutililtyloss. Production25selectedcases/provider validateinjectiononly notrandomgeneralASR orlaterharm. Judgecalibration50ratings/5annotators,QWK.7288behavior; mechanismprobes/attentionon separateopenmodelsettings areassociationnotcausal. No matchedtool-free/web-agent securitytrial.

## Batch 7 committed

ToolHijacker15claims andHidden in Memory15claims pass existingquality/sourcebinding andMD/JSONreadback. Relevantfigures/tablesrepresented with missingartifacts/partialvisualcoveragequalified. HiddenMemoryC13:agentjudgecountsclaimed/attempted/movementtowardgoal, notonlycompletedexecution; audit2falsepositives/80. Standardizeddownstreamgoalsdirectlysaved/fallbackothermodelparaphrase, so notindirectinjectionjointsuccess. These qualificationsappearinnarrative/record. All50prior outputand12protectedhashesunchanged.39completed/66pending/7excluded/0failed;14new.

## Batch 8 source review in progress

Overthinking Loops identityLee/Jang/Choi/Kim/Choi,12pages, MCPregistrycost attack. Sourcepp.1,3–7checkedandp.5Table1/Figure4renderinspected.14tools/3serversco-registered, ReAct100normal+14 versusnormal100, QwenCode44normal+14=58 (13builtin29Serena2Context7).5runs/config;CodeElo10randomproblems→7solvableallmodelswithoutadditionalMCP,selectionlimitsgeneralization. Session1000turns,20tooldepth/turn, exactforcedterminationbudgetsunclear. Totaltokensinput+output+appendedtooloutputs, notjustverbosity. QwenCodeMiniMax142.4×tokens/27.5×runtime averages;singlecasesGLM971.27×,MiniMax609.71×/180.12×runtime distinctdenominators. Nonterminationforcedstop nooutputisoperational/resourceattackeffect, notexfiltration. NoWaittoken-generationmitigation leavesDeepSeek15.37×AIME/GLM11.93×GPQA13.35×HumanEval; accuracy sometimesimproves,securitynotutilityrank. GLM4.6codingvs4.7ReActmigrationnotmatchedcrosssystem causalcomparison. Mixedvsattackonly existingtool-agent registrycontrol, no standalonebaseline. Interleaving explanationhypothesis; exponentialgrowthdiagramnotfittedlaw;guardrail alternativesuntested.

OverthinkingLoops14claims passexistingchecks afterheadingrepairs; originalresponsepreserved. DraftC13recomputesMiniMaxperproblemprintedratiosmean303.30×versussummedtokensratio142.35×matchingheadline, leavesEquation1meanratiosinconsistencyunresolved. NoWait15tokensclaimedvs17lexicalentriesflag. No scientificoverclaim of alldefensesfail.

ST-WebAgentBench: ICLR2026conferencepaper43pages,Levy/Wiesel/Marreed/Oved/Yaeli/Mashkif/Shlomov,IBM. Sourcepp.1,3–10,26–30checked andFigure2/Table3p.9renderinspected.375tasks/3057policyinstances/3apps:GitLab197ShoppingAdmin8SuiteCRM170including80modalitytasks,6STdimensions,commonGPT4obackbone3agents. CRvsCuPwithzeroviolations,partialanycheckdistinct. FigureAWMCR33.8/CuP20%,WebVoyager12.8/10.3,WorkArena26/15; headlinefewerthan2/3qualifiesaggregate, notWebVoyager10.3/12.8≈80.5% individually. pass@3anysuccessversusallpass@3allruns, formulaallpassrawcompletionbutresultsproseaddscompliance; one-suite/runwordingvs3attemptsunclear. RiskRatioformula violations/#policyinstances, nottaskdenominator orASR;AWM37consentbreaches/.44%prose cannotreconstructusing322instances andradar≈.44fraction. Appendixsystempromptintegration vs mainobservationappendingconflict. Simulatedautoapproval+fuzzyrequiredmessagechecksnotrealhumans/informedconsent. Policiesdelivered, notexperimentallyguaranteedenforcement; proposedcontrolleruntested. RobustnesssubsetadversarialUIinstructions butaggregatepolicyviolations mix benignerrors/conflict/security. 95%incidentcoverageclaimnoauditableincidentdenominator. Policyloadrho−.71observational binnedtasks, notrandomizedconstraintadditioncausaleffect. No matchedstandalonecontrol.

## Batch 8 committed

OverthinkingLoops14claims andST-WebAgentBench14claimsvalidated/source-bound, MD/JSONreadbackpassed. Retainedheadingrepairs only, noextra modelcalls. Figures/tablesrepresented; reviewerpage5/9renderschecked. Sourceuncertaintiespreservedincludingaggregation/riskdenominators/pass@3vsallpass/policyplacement, anduntestedcontroller. All50prior outputand12protectedhashesunchanged.41completed/64pending/7excluded/0failed;16new.

## Batch 9 source review in progress

StruQ:Chen/Piet/Sitawarin/Wagner,20pages, sourcepp.1–2,8–12checkedandp.10Table2/3renderinspected. Securetrustedprompt vsuntrusteddata frontendrecursivefilterreservedtokens plusstructuredinstructiontuningbaseLlama/Mistral7B3epochs.208AlpacaFarmdata-containingexamples/attack; fixedHackedoutputsuccess manuallyfalsepositivechecked, HackAPromptPWNEDvariant.805AlpacaEvalGPT4judgevsdavinci003utilityreference, not webtaskcompletion. MainLlamaTAP97→9%GCG97→58%,MistralTAP100→36/GCG99→56; manualresidual0–2%. Claimed<2%manualvsMistral2%table unresolved. UtilityLlama67.2→67.6%,Mistral80→78.7(-1.3pp) authorSE.7/significanceclaims no independentretest. WhiteboxGCGgradientaccess vs blackboxTAP/manual differentattackerpowers/budgets. Delimiter/front-endtested variantsnottheorem; model-onlyaugmentationablationswithoutfrontend distinctfromfullsystem. Algo1returnsTsnotTprime;Figure2HASHvsMARK inconsistency. Trustedpromptcontrolassumed; cannotdetectmalicioustrustedprompt. No agent/browser/standalonematchedsecuritycontrol. ToolHijackerStruQselectionfailureis differentprotocol/trainedtargetsandcannotpoolrankASRagainstthispaper.

StruQ draft16claims passesexistingqualityafter3headinglabels/struq_c14p14se-curehyphenationrepair. Allimportanttablemetrics/supportchecked, originalretained, no paidretry.

An Illusion of Progress: COLM2025,32pages, Xue/Qi/Shi/Song/Gou/Song/Sun/Su;Online-Mind2Web300tasks136sites. Sourcepp.1,3–10,20–21checkedandmainTable2p.6visuallyinspected.650oldMind2Webtasksreviewed47%invalid/outdatedtrajectories, not47%attackedfailures. Dataset167old+24rewritten+34live+75new=300;83easy143medium74hardbyhumanreferenceactions. StrongCAPTCHAtasks excluded;initialURL/noGooglesearchpromptrestrictagents. Searchagent51%100stratifiedWebVoyager vs22%100balanced33/34/33difficultyOnline, notsametaskdenom orsamecausalcontrol.6agentsalltrajectories2humanannotators+thirdresolve, humantaskcompletion30.7SeeAct28AgentE30BrowserUse29Claude3.556.3Claude3.761.3Operator. Previousselfreportsdifferentbenchmark/version/judging, deltasppnotrelative%. WebJudgeo4agreement85.7/7B87.0 vsGPT4o83.6; successgaps3.8/3.9/7.8pp averageabsolute, notconfidence/calibration. AgentRewardBenchreused1302trajectories, notindependentnewoutcomes; GPT4oprecision73.7/recall71.2/F172.4, o4precision82/recall47.8/F160.4, rule83.8/55.9/67.1, no alldimensionsdominance. Predictedpositiveprecisionnotaccuracy;nomaliciousjudgeinputtested. Efficiencymeanstep/referenceonlysuccess, Operator2.6× notfullresourcecost. Operatorfailurecategory57.7%filter/sort,notASR/compromisedharm. Figure4difficultymean31.6/15.4droparepp fromroundedgroups, notrelativepercent. Rewardmodeltrainingproposedfuture notdemonstrateddefense. No matchedstandaloneLLMattackcontrol.

Batch 9 committed: StruQ and An Illusion of Progress. Existing output identity/schema/section/page/quote checks passed (16 claims each). Retained heading labels corrected without model redispatch; source findings and protocol qualifications retained. Previous 50 outputs and 12 protected fingerprints unchanged. State: 43 complete / 62 pending / 7 excluded / 0 failed.

### Batch 10 crawler-trap source check
David/Delong/Filiol, Journal of Computer Virology and Hacking Techniques 17:185–198 (2021), physical PDF14 pages. Source pp6–10: 13 families ×500pages =6500 (nine regular, four trap families; notEvil collected at two time scales, two synthetic generators). Word-bigram distance-distribution interval overlap, not held-out classifier confusion matrix. At t=3 family overlap Handfish19.95%, Dottyback12.73% versus Bhattacharyya47.61%, Hellinger48.48%, Jensen–Shannon55.11%; merged-cluster Dottyback0.57% overlap does not prove0.57% false negatives or>99% operational detection. Cross-cluster impact Shark3.4%, Dottyback7.28% differs from merged-cluster metric. Paper p6 defers implementation/classification/operational tests to future work while later proposing dynamic trimmed clustering; do not claim an implemented live validated detector. The normal observation intervals and mean confidence intervals are conflated, pairwise normalization/formula conditions need qualification; no prompt injection, LLM agent or matched comparative security experiment.

### Batch 10 Toolformer source check
Supplied17-page arXiv2302.04761v1,9February2023. Self-supervised sample/execute/loss-filter APIcalls then GPT-J6B finetuning; five APIs, frozen inference tools, one call/input, APIstart top10. Source pp5–8: same trained Toolformer with APIcalls disabled is a useful matched capability ablation, but not a web-agent/standalone adversarial security comparison. LAMA Toolformer33.8/11.5/53.5 vsdisabled22.1/6.3/34.9 with WikiSearch disabled; math40.4/29.4/44 vs14.8/6.3/15; QA26.3/17.7/48.8 belowGPT3 with QAtool disabled to avoid triviality. MLQA tools help same Toolformer but do not consistently beat GPT-J after English CCNet finetuning. DATESET27.3 vsdisabled5.9 and calendar54.8%usage; TEMPLAMA16.3 vs12.7 but calendar0.2% so no calendar-attributed improvement. Table8perplexity10.3/10.5 tool-disabled versussame CCfinetune; enabled perplexity not computed. Benign relaxed matching protocols (first5words/firstnumber/20words/10words), no security ASR/harmful execution evaluation; tool output in continuation is inferred trust boundary. No chained/interactivetools; one-call anti-loop restriction is operational rationale, not a measured security defense. Figures/tables preserve these task-specific conditions.

Batch 10 committed: crawler-trap detection (14 claims) and Toolformer (16 claims). Toolformer retained quotation transcription repaired for PDF line/column breaks; original draft preserved; no model redispatch. Existing output identity/schema/section/page/quote checks and Markdown/JSON readback passed for all45. State45complete/60pending/7excluded/0failed/deferred. Previous50output and12protected fingerprints unchanged.
