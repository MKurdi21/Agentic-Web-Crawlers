# Security comparison reference

## Scope and reading guide

All **112 canonical paper records** have exactly one primary profile. Five exact archived PDF duplicates are outside this count. Primary placement reflects the main evidentiary contribution; secondary source tags preserve overlap. The taxonomy is editorial, not an effectiveness or severity ranking. An attack paper may also evaluate defenses.

Each profile uses eight consistent fields in a two-column table. Source links lead to the unchanged structured records and comprehensive narratives. Claim IDs and physical PDF page references remain traceable. Findings are author-reported unless labeled analyst inference; survey metrics are secondary evidence. Missing information remains missing. “Not evaluated” is not proof of safety.

Attack success rate (ASR), benign task success, detector accuracy, intermediate action and completed harm are different endpoints. Simulated/live outcomes, model/system access, attacker budgets and denominator definitions must remain separate; incompatible percentages are not pooled or ranked. Utility retains its source-defined meaning.

The reviewed evidence does not establish a universal otherwise matched standalone-language-model versus web-agent vulnerability rate. Comparator fields distinguish security experiments from capability ablations and agent-versus-agent defense tests. Exposure, model susceptibility and consequences enabled by permissions/state are separate questions. See the [thematic findings](INITIAL_RESEARCH_FINDINGS.md).

**Study families:** the canonical AgentFuzzer filename maps to an AGENTVIGIL v4 PDF related to the published AgentVigil record. The two Mind the Web records are versions of one study. Separate profiles preserve version-specific evidence; shared results are not independent replication. Source names remain unchanged.

## Trap-focused reading path — current priority, 2026-10-16

The leading research proposal studies task-dependent recurring prerequisites, bounded non-progress, escape and recovery in solvable web tasks; the [roadmap](AI_WEB_AGENT_TRAP_RESEARCH_ROADMAP.md) and [H1–H3](RESEARCH_GAPS_AND_HYPOTHESES.md) define the proposal. No trap experiment has started. The standalone-comparator field remains a useful secondary field, not the primary program.

Read the existing traditional-crawling profiles first, then POTEMKIN, It's a TRAP!, Breaking Agents, AgentLAB, Overthinking Loops and Beyond Max Tokens. Use architecture profiles to reconstruct observation/action privileges; use benign long-horizon and evaluator profiles to distinguish trapping from ordinary failure. Goal-contribution checks and RecurGuard motivate recovery/resource questions without proving trap defenses. The [focused evidence map](THEMATIC_EVIDENCE_MAP.md#focused-trap-comparison) supplies selected competitor dimensions, including supplemental external work outside this register. All 112 eight-field profiles below retain their source text, numbers, versions and unresolved discrepancies.

## Thematic navigation

- [Agent architectures and capabilities](#agent-architectures-and-capabilities) — 30 records
- [Web-agent attacks and retrieval manipulation](#web-agent-attacks-and-retrieval-manipulation) — 15 records
- [Visual and multimodal manipulation](#visual-and-multimodal-manipulation) — 5 records
- [Tool, execution and component attacks](#tool-execution-and-component-attacks) — 3 records
- [Memory and persistent compromise](#memory-and-persistent-compromise) — 2 records
- [Long-horizon and resource attacks](#long-horizon-and-resource-attacks) — 7 records
- [Benchmarks and evaluation methods](#benchmarks-and-evaluation-methods) — 13 records
- [Defenses and containment](#defenses-and-containment) — 21 records
- [Surveys and security background](#surveys-and-security-background) — 8 records
- [Web application testing and traditional crawling](#web-application-testing-and-traditional-crawling) — 8 records

## Agent architectures and capabilities

These studies primarily measure legitimate capabilities. Candidate trust boundaries are analyst interpretations unless a security experiment is explicitly identified.

### [AndroidWorld](../records/androidworld_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Benign mobile capability; M3A/Simple agents in local Android emulator. Secondary source tags: benchmark |
| Inputs and attacker control | App screenshots/trees. No attacker tested |
| Trust boundary and mechanism | Inference: observations to UI/file state. Randomized local app tasks |
| Measured endpoint and conditions | 116 templates/20apps; main M3A text30.6 vs SoM25.4 |
| Defense and utility | No security defense evaluated |
| Major limitations | Seeds/action budgets/human subsets differ; app failure not security compromise; mobile rather than web |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | AW-C01 through AW-C18; physical source pages in claim locators |

### [AutoScraper](../records/autoscraper_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Extraction architecture; XPath generation, DOM pruning, synthesis. Secondary source tags: progress-evaluation, scraping, web-agent |
| Inputs and attacker control | Three seed pages and DOM. Not evaluated |
| Trust boundary and mechanism | Generated extraction code to data. Not evaluated |
| Measured endpoint and conditions | None; extraction F1 and coverage |
| Defense and utility | Not evaluated |
| Major limitations | Supervised/zero-shot inputs differ; synthesis sometimes worsens F1; dataset and runtime bookkeeping conflicts |
| Standalone-versus-agent comparator | No matched security comparator |
| Source locators | autoscraper_c01, autoscraper_c02, autoscraper_c03, autoscraper_c04, autoscraper_c05, autoscraper_c06, autoscraper_c07, autoscraper_c08, autoscraper_c09, autoscraper_c10, autoscraper_c11, autoscraper_c12, autoscraper_c13, autoscraper_c14, autoscraper_c15; physical pp.5,6,7,8,9,10,11,12,13,14,15,16,17,18,19 |

### [AutoWebGLM](../records/autowebglm_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Trained browser agent; ChatGLM3-6B; HTML simplification and browser actions. Secondary source tags: web-agent |
| Inputs and attacker control | HTML/OCR, location and interaction history. Not evaluated |
| Trust boundary and mechanism | Inference: page representation → prompt → browser execution. Not evaluated |
| Measured endpoint and conditions | None; navigation scores only |
| Defense and utility | HTML simplification is not tested as a security defense |
| Major limitations | Environment-specific training; differing candidate counts; missing uncertainty |
| Standalone-versus-agent comparator | No security comparison; model task baselines |
| Source locators | autowebglm_c02/c07/c15; pp.3–4,8,1–12 |

### [Bearcubs](../records/bearcubs_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Information-seeking benchmark; Computer-use and retrieval agents. Secondary source tags: benchmark, web-agent |
| Inputs and attacker control | Live pages, multimedia, alternative sources. Not evaluated |
| Trust boundary and mechanism | Inference: source selection → evidence → answer. Not evaluated |
| Measured endpoint and conditions | None; answer/provenance failures are not compromises |
| Defense and utility | Curation and workaround filtering are not measured defenses |
| Major limitations | 111 tasks; unequal dates/time allowances; provenance/count inconsistencies |
| Standalone-versus-agent comparator | Zero-shot LLM accuracy, not matched security |
| Source locators | bearcubs_c01/c04/c06/c07/c10/c14/c15; pp.3–10 |

### [BrowseComp](../records/browsecomp_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Difficult retrieval benchmark; Browsing and non-browsing model configurations. Secondary source tags: benchmark |
| Inputs and attacker control | Web evidence and multiple sampled answers. Not evaluated |
| Trust boundary and mechanism | Inference: retrieval/synthesis → answer/confidence. Not evaluated |
| Measured endpoint and conditions | None; calibration error is not attack success |
| Defense and utility | No security defense evaluated |
| Major limitations | 1,266 questions; task-oriented training; human denominators differ; unknown calibration formula |
| Standalone-versus-agent comparator | Yes, accuracy/calibration configurations; model/training differences confound security inference |
| Source locators | browsecomp_c05–c08/c13/c14/c16; pp.4–6,9 |

### [BrowserGym](../records/browsergym_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Environment/integration framework; Chromium/Playwright, GenericAgent and action mapping. Secondary source tags: information-seeking, web-agent |
| Inputs and attacker control | DOM/AXTree, screenshots, chat and execution errors. Discussed, not experimentally attacked |
| Trust boundary and mechanism | Inference: page data → generated code → browser/shared state. Author risks: arbitrary code and prompt injection |
| Measured endpoint and conditions | No measured attack outcome; qualitative quantity-setting error |
| Defense and utility | Action mapping, URL protection, warnings discussed; no security ablation |
| Major limitations | Mixed validators; skipped/reused results; shared-state interference |
| Standalone-versus-agent comparator | Six browser-agent backbones, no standalone security control |
| Source locators | BG-C02–C04/C10–C15; pp.5,7–8,17–18,26,31–33 |

### [Go-Browse](../records/go_browse_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Data collection/training; Graph exploration, task proposers, solvers and VLM judge. Secondary source tags: web-agent |
| Inputs and attacker control | Accessibility trees, screenshots and interaction traces. Not evaluated |
| Trust boundary and mechanism | Inference: proposed task/judge → retained trajectory → training. Not evaluated |
| Measured endpoint and conditions | None; task-solving and transfer results |
| Defense and utility | No security defense evaluated |
| Major limitations | Success-only training; unclear judge accuracy; transfer/count discrepancies |
| Standalone-versus-agent comparator | Browser-agent capability comparisons |
| Source locators | GB-C02/C08/C12/C13; pp.6,16,3–15 |

### [Gorilla](../records/gorilla_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Agent architectures and capabilities; Fine-tuned Llama7B with API cards, retrieval-aware training and AST evaluation. Secondary source tags: tool-use |
| Inputs and attacker control | Analyst inference: candidate surfaces include API documentation appended to a prompt, the retriever/API database, generated repository and model arguments, and supporting execution code. The authors do not define these as attack surfaces or evaluate attacker control, prompt injection, privilege misuse, data theft, or malicious repositories. |
| Trust boundary and mechanism | Closed-document analysis of all 22 supplied text pages and 16 supplied page renderings. The paper constructs APIBench, generates instruction–API pairs with GPT-4, fine-tunes LLaMA-7B with and without documentation, compares four retrieval settings, evaluates selected API structure using AST matching, and includes constraint, documentation-change, manual-execution, prompting, DocPrompting, and base-model analyses. |
| Measured endpoint and conditions | No-document accuracy59.13/71.68/83.79 across catalogs;100 manual examples78% API accuracy/72% program execution |
| Defense and utility | Fine-tuning/retrieval/AST checking improve capability under listed conditions, not validated attack prevention.100 manual generations yield78% API accuracy/72% program execution. |
| Major limitations | Capability not attack success; API counts and metric tables conflict; HF criteria differ by model; headline gains use different baselines; no adversarial standalone/agent experiment |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | gorilla_c01 through gorilla_c13; physical pages in locators |

### [LASER](../records/laser_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | State-space navigation; State-specific prompts and function actions. Secondary source tags: web-agent |
| Inputs and attacker control | Shopping observations and retained items. Not evaluated |
| Trust boundary and mechanism | Inference: rationale → function/arguments → website state. Not evaluated |
| Measured endpoint and conditions | Author risk: consequential real actions |
| Defense and utility | State-permitted functions are not tested authorization guarantees |
| Major limitations | Shopping-only; 500/200/100 samples differ; stops before real buying |
| Standalone-versus-agent comparator | No security comparator |
| Source locators | laser_claim_02/03/06/10/11/15/16; pp.2–5,12 |

### [Long-Horizon Mirage](../records/the_long_horizon_task_mirage_diagnosing_where_and_why_agentic_systems_break_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Agent architectures and capabilities; Benign multi-domain horizon extension and failure diagnosis. Secondary source tags: long-horizon, progress-evaluation |
| Inputs and attacker control | Analyst inference only: webpage observations, dynamic UI state, action interfaces, retained interaction history, and intermediate artifacts are relevant places to investigate manipulation or policy violation. The supplied study specifies no attacker-controlled surface, attacker capability, exploit, or attack-success rate. |
| Trust boundary and mechanism | HORIZON constructs progressively extended tasks across WebArena, AgentBench OS, MAC-SQL databases, and IsaacSim embodied simulation. More than 700 tasks yield 3100+ trajectories. GPT-5-mini and Claude-4-Sonnet are tested across domains, full GPT-5 additionally on embodied tasks, and a GPT-5 judge assigns failures using a seven-category taxonomy. Success curves use three runs with standard deviations; human validation reports κ = 0.61 and κ = 0.84 on 40-trajectory studies. |
| Measured endpoint and conditions | Over700 tasks/3100 trajectories; three runs with mean±SD |
| Defense and utility | No security defense evaluated; proposed hierarchical planning/verification/memory remedies are untested. Benign four-domain tasks use different caps. |
| Major limitations | Caps and compositional conjunctions confound horizon; examples include authored micro-scenarios; annotator protocol conflicts; benign failure is not successful attack |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | claim_01–claim_14; pp.1–47 |

### [Mind2Web](../records/mind2web_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Offline action benchmark; MindAct ranker plus action-prediction model. Secondary source tags: web-agent |
| Inputs and attacker control | Cached HTML/DOM and ground-truth histories. Not evaluated |
| Trust boundary and mechanism | Inference: webpage snippets → operation prediction. Not evaluated |
| Measured endpoint and conditions | Author concerns: sensitive transactions and misuse |
| Defense and utility | HTML filtering/fake collection clicks are not validated deployment defenses |
| Major limitations | Independent-step scoring; cached alternative paths; GPT-4 subset/top-ten restrictions |
| Standalone-versus-agent comparator | Model task comparisons only |
| Source locators | mind2web_c02–c06/c08–c13; pp.6–7,10,19 |

### [Mind2Web 2](../records/mind2web_2_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Research benchmark; Long-horizon browser research and graph judge. Secondary source tags: information-seeking |
| Inputs and attacker control | Live sites, research answers and traces. Not evaluated |
| Trust boundary and mechanism | Sources to answer; judge to accepted evidence. Not evaluated |
| Measured endpoint and conditions | None; 130 tasks, three runs; human comparison uses30 tasks |
| Defense and utility | Not evaluated |
| Major limitations | Judge99.03% node accuracy from15 selected tasks excludes total failures; credibility assumed |
| Standalone-versus-agent comparator | No matched security comparator |
| Source locators | m2w2_c01, m2w2_c02, m2w2_c03, m2w2_c04, m2w2_c05, m2w2_c06, m2w2_c07, m2w2_c08, m2w2_c09, m2w2_c10, m2w2_c11, m2w2_c12, m2w2_c13, m2w2_c14, m2w2_c15; physical pp.1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51 |

### [MMINA](../records/mmina_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Multihop multimodal benchmark; Text, image/caption and history-conditioned agents. Secondary source tags: benchmark, long-horizon, multimodal |
| Inputs and attacker control | Partial webpages, images/captions and replayed trajectories. Not evaluated |
| Trust boundary and mechanism | Inference: observation/history → action; ordered hop completion. Not evaluated |
| Measured endpoint and conditions | None; hop/task failure is not attack success |
| Defense and utility | Memory augmentation is not tested as a security defense |
| Major limitations | Offline-site exceptions; hop-count tensions; small long-task groups |
| Standalone-versus-agent comparator | Source calls model baselines standalone; no security comparison |
| Source locators | mmina_c02–c05/c07–c14; pp.3,7–8,12–14 |

### [Odysseys](../records/odysseys_benchmarking_web_agents_on_realistic_long_horizon_tasks_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Long-horizon benign capability; General computer-use models with Chrome/OS access. Secondary source tags: benchmark, long-horizon, web-agent |
| Inputs and attacker control | Live sites and auxiliary system tools. No attacker tested |
| Trust boundary and mechanism | Inference: retrieved content and workarounds to actions/answers. 200 tasks/1225 rubrics; partial and perfect scoring |
| Measured endpoint and conditions | Opus perfect44.5% at100 calls;76.5% at200 |
| Defense and utility | No security defense evaluated |
| Major limitations | Step means model calls, not equal UI actions; 86/200 arithmetic mismatch; 76-task Qwen subset; old archived schedule scored success is not current factual correctness |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | odysseys_claim_01 through odysseys_claim_15; physical source pages in claim locators |

### [ReAct](../records/react_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Architecture/capability; Reasoning-and-action language agent. Secondary source tags: None assigned |
| Inputs and attacker control | Retrieved observations; Wikipedia; simulated environments. Not evaluated |
| Trust boundary and mechanism | Inference: observation → reasoning context → action. Not evaluated |
| Measured endpoint and conditions | None; harmful-action concerns are author risks |
| Defense and utility | No tested security defense; selected human correction example |
| Major limitations | Wikipedia edits and real purchases excluded; one correction example is not a rate |
| Standalone-versus-agent comparator | No matched security comparator |
| Source locators | react_c01/c10–c13; pp.3–4,10,14–15 |

### [SeeAct](../records/seeact_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Grounding/capability; GPT-4V plans with automated or human grounding. Secondary source tags: multimodal, web-agent |
| Inputs and attacker control | Screenshots; HTML candidate representations. Not evaluated |
| Trust boundary and mechanism | Inference: intended action → selected element → browser event. Not evaluated |
| Measured endpoint and conditions | Potential harmful actions reported without incidence rate |
| Defense and utility | Human safety checks/restricted tasks are evaluation conditions, not measured attack defenses |
| Major limitations | Oracle assistance; pop-up closure; restricted 90-task live tests |
| Standalone-versus-agent comparator | GPT-4 comparator is also a web agent |
| Source locators | seeact_c01/c03/c05/c09–c11/c14; pp.3–6,9,14–15 |

### [Toolformer](../records/toolformer_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Self-supervised API-use architecture/capability; GPT-J6B samples, executes, loss-filters APIcalls; five tools; response inserted before continuation. Secondary source tags: tool-use |
| Inputs and attacker control | QA/search/translation/calendar/calculator output. No evaluated attacker |
| Trust boundary and mechanism | API response → continuation context (inferred trust boundary). No demonstrated attack; irrelevant retrieved content can reduce loss |
| Measured endpoint and conditions | LAMA33.8/11.5/53.5 vsdisabled22.1/6.3/34.9; DATESET27.3vs5.9 under distinct task restrictions |
| Defense and utility | One-call cap limits loops by design; no adversarial effectiveness test |
| Major limitations | Tool/task exclusions; relaxed answer matching; no chained/interactive tools; tool-enabled perplexity unavailable; no security/utility tradeoff test |
| Standalone-versus-agent comparator | Same trained model tools-enabled/disabled capability ablation; no matched web-agent security comparison |
| Source locators | toolformer_claim_01–16; pp.1–11,17 |

### [VisualWebArena](../records/visualwebarena_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Visually grounded capability benchmark; Text, caption-augmented and multimodal browser agents; SoM element IDs. Secondary source tags: benchmark, multimodal, web-agent |
| Inputs and attacker control | Screenshots, accessibility trees, image captions, user images, URLs/tabs. No evaluated attacker; risk discussion only |
| Trust boundary and mechanism | Environment observations → model planning → persistent browser/application actions (analyst-inferred security surface). No measured injection; benign looping, premature stopping and state errors are reliability failures |
| Measured endpoint and conditions | 910 model tasks; GPT-4V SoM 16.37% task success, later GPT-4o SoM 19.78%; humans 88.70% on separate 230-task sample |
| Defense and utility | Sandboxed research environment advised; no evaluated defense effect |
| Major limitations | Model-specific viewport/token budgets; human sample/template count ambiguity; SoM demo wrong target ID; no attack evaluation or security uncertainty |
| Standalone-versus-agent comparator | Text/multimodal browser-agent comparison, no tool-free security control |
| Source locators | vwa_c01–15; pp.1,3–9,13,15–17,19–20,25 |

### [WebArena](../records/webarena_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Browser benchmark; Logged-in, state-changing agents in website replicas. Secondary source tags: benchmark, web-agent |
| Inputs and attacker control | Accessibility trees and benchmark websites. Not evaluated |
| Trust boundary and mechanism | Inference: authenticated observations → action; credentials → execution. Not evaluated |
| Measured endpoint and conditions | None; benchmark permissions identify potential consequences |
| Defense and utility | No attack defense evaluated |
| Major limitations | Human sampling differs; logged-in credentials are not evidence of theft |
| Standalone-versus-agent comparator | Browser-agent/task baselines only |
| Source locators | WA_C02/C04/C13/C15; pp.4–6,17–18 |

### [WebChoreArena](../records/webchorearena_evaluating_web_browsing_agents_on_realistic_tedious_web_tasks_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Agent architectures and capabilities; Tedious benign web tasks with memory/calculation demands. Secondary source tags: benchmark, long-horizon, web-agent |
| Inputs and attacker control | ANALYST INFERENCE: candidate components for future examination include webpage observations through accessibility trees and screenshots, information retained in memory or summaries, browser navigation and state-changing actions, optional scratchpad/calculator interfaces, and cross-site login context. These are documented interaction components, not experimentally established attack surfaces or demonstrated exploits in this study. |
| Trust boundary and mechanism | A manually constructed 532-task benchmark over four simulated WebArena websites and cross-site settings, with 117 templates, overlapping capability labels, observation requirements, textual/URL/functional scoring, five principal proprietary LLMs in two agent frameworks, human evaluation, and fifteen separately registered empirical analyses including supplementary appendix experiments. |
| Measured endpoint and conditions | 532 instances/117 templates; BrowserGym GPT5 task success48.3% |
| Defense and utility | Memory/calculator interventions measure utility, not security. Human117-template cohort differs from model532-instance cohort. |
| Major limitations | Human50.2% uses117 template instances, not same532; frameworks have different action budgets; ablations and live-web set use different cohorts; no adversarial test |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | C01–C14; pp.1–29 |

### [WebDancer](../records/webdancer_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Research-agent training; Search/visit, SFT and RL. Secondary source tags: information-seeking |
| Inputs and attacker control | Search snippets and summarized pages. Not evaluated |
| Trust boundary and mechanism | External text to trained reasoning/actions. Not evaluated |
| Measured endpoint and conditions | None; GAIA103/WebWalker680 capability results |
| Defense and utility | Not evaluated |
| Major limitations | Pass@1 versus multi-run metrics; inconsistent trajectory filtering; same-set greedy results not held out |
| Standalone-versus-agent comparator | Model baselines differ; no matched security comparator |
| Source locators | WD_C01, WD_C02, WD_C03, WD_C04, WD_C05, WD_C06, WD_C07, WD_C08, WD_C09, WD_C10, WD_C11, WD_C12, WD_C13, WD_C14; physical pp.1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24 |

### [WebGPT](../records/webgpt_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Browser-assisted long-form QA; Fine-tuned GPT-3; text browser, human feedback and reward-model selection. Secondary source tags: information-seeking, web-agent |
| Inputs and attacker control | Bing results, linked webpage text, selected quotes/references. No evaluated injection attacker; author discusses source unreliability/reward manipulation risks |
| Trust boundary and mechanism | Retrieved evidence → answer/reward judgments; permitted search/link actions limit live effects. Cherry-picked evidence or manufactured-reference scenarios discussed; Wikipedia editing hypothetical and unavailable in implementation |
| Measured endpoint and conditions | 175B best-of-64: 56% preference vs demonstrators, 69% vs Reddit under different procedures; ties half; TruthfulQA 75% truthful/54% truthful-and-informative |
| Defense and utility | Reference collection aids review; restricted actions limit side effects; no injection defense evaluation |
| Major limitations | Reward/reference reliability, overreliance, changing web; hallucination reduction not directly tested; separate preference denominators/protocols |
| Standalone-versus-agent comparator | Base GPT-3 comparison measures answer quality with different training/judging, not matched attack susceptibility |
| Source locators | webgpt_c01–15; pp.1–11,17–18,24–28 |

### [WebLINX](../records/weblinx_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Conversational navigation capability; Dense Markup Ranker top10 elements plus history/screenshots; structured browser actions. Secondary source tags: long-horizon |
| Inputs and attacker control | Real-world DOM, screenshots, multi-turn user dialogue. No tested attacker |
| Trust boundary and mechanism | Observations/grounding → action strings → browser interface (inferred risk). Selected wrong target, credential-field confusion and history mistakes; not attacks |
| Measured endpoint and conditions | 2337demos/155sites; static next-action micro-scores; Llama2-13B37.09IID/25.21OOD Table28; DMR186vs916ms with lower OODRecall@10 |
| Defense and utility | Human supervision/research-only deployment advised; no intervention effectiveness measured |
| Major limitations | Static teacher-forced states; one finetuning run/config; alternate-action134turn sample; final real purchases/bookings stopped; score/table inconsistencies |
| Standalone-versus-agent comparator | Modality/training comparisons, no matched standalone security control |
| Source locators | weblinx_c01–14; pp.1–9,20,27–32,47–50 |

### [WebSailor](../records/websailor_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Research-agent training; SailorFog, RFT, DUPO. Secondary source tags: web-agent |
| Inputs and attacker control | Web graph and search/visit observations. Not evaluated |
| Trust boundary and mechanism | Web evidence to reconstructed reasoning/training. Not evaluated |
| Measured endpoint and conditions | None; capability benchmark scores |
| Defense and utility | Not evaluated |
| Major limitations | Post-hoc thought reconstruction is not online faithful reasoning; subset/aggregation and speedup conditions incomplete |
| Standalone-versus-agent comparator | No matched security comparator |
| Source locators | websailor_c01, websailor_c02, websailor_c03, websailor_c04, websailor_c05, websailor_c06, websailor_c07, websailor_c08, websailor_c09, websailor_c10, websailor_c11, websailor_c12, websailor_c13, websailor_c14, websailor_c15; physical pp.1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23 |

### [WebScraper](../records/webscraper_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Scraping architecture; Browser extraction with Python execution. Secondary source tags: multimodal, scraping, tool-use, web-agent |
| Inputs and attacker control | News/ecommerce DOM and screenshots. Not evaluated |
| Trust boundary and mechanism | Web observation to generated extraction code. Not evaluated |
| Measured endpoint and conditions | None; URL/content extraction scores |
| Defense and utility | Not evaluated |
| Major limitations | Eight sites/30 runs; coder-model inconsistency; visual news bars lack exact values; no significance evidence |
| Standalone-versus-agent comparator | No matched security comparator |
| Source locators | webscraper_c01, webscraper_c02, webscraper_c03, webscraper_c04, webscraper_c05, webscraper_c06, webscraper_c07, webscraper_c08, webscraper_c09, webscraper_c10, webscraper_c11, webscraper_c12, webscraper_c13, webscraper_c14, webscraper_c15, webscraper_c16; physical pp.2,3,4,5,6 |

### [WebShop](../records/webshop_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Shopping benchmark; IL/RL browser shopping agent. Secondary source tags: web-agent |
| Inputs and attacker control | Synthetic product pages. Not evaluated |
| Trust boundary and mechanism | Page descriptions to actions. Not evaluated |
| Measured endpoint and conditions | None; 500-task capability evaluation |
| Defense and utility | Not evaluated |
| Major limitations | 1.181M products vs12,087 instructions; trial averages, simulated purchases, conflicting trajectory counts |
| Standalone-versus-agent comparator | No matched security comparator |
| Source locators | webshop_c01, webshop_c02, webshop_c03, webshop_c04, webshop_c05, webshop_c06, webshop_c07, webshop_c08, webshop_c09, webshop_c10, webshop_c11, webshop_c12; physical pp.1,2,3,4,5,6,7,8,9,10 |

### [WebVoyager](../records/webvoyager_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Multimodal live browsing; Selenium browser agent with seven actions. Secondary source tags: multimodal, web-agent |
| Inputs and attacker control | Screenshots, element labels, parsed PDFs, errors/history. Not evaluated |
| Trust boundary and mechanism | Inference: external page/file → prompt → executed action. Not evaluated |
| Measured endpoint and conditions | Author risks: malicious downloads, private-data submission, fake requests |
| Defense and utility | Monitoring/non-login selection; no tested attack defense |
| Major limitations | Judge agreement ≠ reliability; non-login tasks; response-trusting judge rule |
| Standalone-versus-agent comparator | Text-only and All Tools task baselines, not security controls |
| Source locators | WV-C05/C07/C10–C14; pp.7,10,13,15 |

### [WebWalker](../records/webwalker_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Traversal QA capability; Explorer selects subpage URLs; critic accumulates memory/answers; memory-augmented RAG. Secondary source tags: benchmark, information-seeking, web-agent |
| Inputs and attacker control | Web markdown, clickable HTML buttons, URLs, critic memory. No tested attacker |
| Trust boundary and mechanism | Page → observation/action → memory → final QA/RAG (inferred security boundaries). Benign wrong location/reasoning/step exhaustion; no attack outcomes |
| Measured endpoint and conditions | 680QA/1373pages;15stepcap; GPT4o37.50%accuracy vsReAct33.82/Reflexion35.29;4.67actions only successful cases |
| Defense and utility | Critic/memory improve scoped QA, not tested security defense |
| Major limitations | Domain/table/example conflicts; ninevs sixmodels; Qwen7BReActoverallAC below subgroupmeans; uncalibratedGPT4judge; no complete cost denominator |
| Standalone-versus-agent comparator | No-retrievalGemini/o1comparedifferent models' QA, not matched security control |
| Source locators | ww_c01–15 and narrative§14; pp.3–9,13–16 |

### [WorkArena](../records/workarena_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Enterprise benchmark; BrowserGym/ServiceNow tasks. Secondary source tags: benchmark |
| Inputs and attacker control | DOM, screenshots, enterprise state. Not evaluated |
| Trust boundary and mechanism | Observation to enterprise actions. Not evaluated |
| Measured endpoint and conditions | None; 330 evaluations across33 tasks, not19,912 tests |
| Defense and utility | Not evaluated |
| Major limitations | Model and seed differences; task success is utility, not security; conflicting WebArena scores |
| Standalone-versus-agent comparator | No matched security comparator |
| Source locators | workarena_c01, workarena_c02, workarena_c03, workarena_c04, workarena_c05, workarena_c06, workarena_c07, workarena_c08, workarena_c09, workarena_c10, workarena_c11, workarena_c12, workarena_c13, workarena_c14, workarena_c15, workarena_c16, workarena_c17; physical pp.1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21 |

### [WorkArena++](../records/workarena_plus_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Compositional benign capability; ServiceNow BrowserGym workflows. Secondary source tags: benchmark |
| Inputs and attacker control | Authenticated task UI and optional hints. No attacker tested |
| Trust boundary and mechanism | Inference: observations to state-changing actions. Knowledge-work composition |
| Measured endpoint and conditions | 341 workflows/682 L2-L3 tasks; main235 per level |
| Defense and utility | No measured security defense |
| Major limitations | All main L3 scores zero; human selected cohort differs; task failure is not attack success |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | WA-C01 through WA-C14; physical source pages in claim locators |

## Web-agent attacks and retrieval manipulation

External-content influence, retrieval exposure and task-aligned redirection differ in attacker control and completed consequences.

### [AdvAgent](../records/advagent_controllable_blackbox_red_teaming_on_web_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Black-box webpage attack; SeeAct with GPT-4V or Gemini-1.5-flash. Secondary source tags: adaptive-attack, web-agent |
| Inputs and attacker control | Screenshot and HTML candidate grounding. Modify target aria-label; train attacker with black-box action feedback; no victim weights/logits |
| Trust boundary and mechanism | Hidden HTML attribute → action argument; intended operation/element retained. Environment-specific SFT/DPO prompts redirect typed arguments |
| Measured endpoint and conditions | Domain-mean exact adversarial-triplet ASR 97.5% +/-2.0 GPT-4V and 99.8% +/-0.3 Gemini; 200 test tasks after 240 training tasks. Domain variation, not repeated-run uncertainty |
| Defense and utility | Three prompt defenses leave Gemini ASR 88.8–89.8% in tested settings |
| Major limitations | Offline step grounding; transfer/reuse conditional on successful attacks; no completed purchase/harm; four domains |
| Standalone-versus-agent comparator | No matched standalone security comparator |
| Source locators | C01–C15; pp.3–8,12–13 |

### [AgentVigil (published)](../records/agentvigil_generic_black_box_red_teaming_for_indirect_prompt_injection_against_llm_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Attack optimization; AgentDojo and VisualWebArena agents. Secondary source tags: adaptive-attack, prompt-injection |
| Inputs and attacker control | Replaced tool results/page content. Selected tool/page injection |
| Trust boundary and mechanism | Untrusted content to agent instruction/actions. MCTS fuzzing and payload transformation |
| Measured endpoint and conditions | Selected top-five union: AgentDojo o3-mini65% test; VWA GPT-4o59% test |
| Defense and utility | Evaluates detectors, repeats, delimiters; adaptive repeat differs |
| Major limitations | Same version family as AgentFuzzer; not independent replication;173/100 test tasks differ; missing benign utility |
| Standalone-versus-agent comparator | No matched standalone comparator |
| Source locators | av_c01, av_c02, av_c03, av_c04, av_c05, av_c06, av_c07, av_c08, av_c09, av_c10, av_c11, av_c12, av_c13, av_c14, av_c15; physical pp.2,3,4,5,6,7,8,9,12,13,14 |

### [AGENTVIGIL v4 (AgentFuzzer mapping)](../records/agentfuzzer_generic_black_box_fuzzing_for_indirect_prompt_injection_against_llm_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Adaptive black-box injection search; Tool-calling AgentDojo and multimodal VWA-adv agents. Secondary source tags: adaptive-attack, prompt-injection |
| Inputs and attacker control | Tool-output placeholders / text triggers; shopping review. External-content control and binary success feedback; helper-model mutation, no target internals |
| Trust boundary and mechanism | External attacker content → model planner → evaluated attacker objective. Seed corpus, adaptive ASR/coverage scoring, MCTS-inspired selection and five mutation operators |
| Measured endpoint and conditions | AgentDojo fuzz142/test173; o3-mini fuzz71%/test65% vs38/34% baseline. VWA-adv fuzz99/test100; GPT-4o selected-prompt60/59%, prose fuzz70% unresolved; transfer top5 prompt union |
| Defense and utility | Tested detector/repeat/delimiter and safety/paraphrase/combined defenses leave scoped residual ASR; utility costs not quantified |
| Major limitations | File alias differs from actual v4 title; budgets/splits/union matter; superiority has exceptions; appendix rates/coverage algorithm conflicts; local URL case not completed malware/exfiltration proof |
| Standalone-versus-agent comparator | No matched standalone security comparator |
| Source locators | C01_indirect_external_content–C15_derived_agentdojo_gain; pp.1–9,12,14 |

### [Commercial LLM Agents](../records/commercial_llm_agents_are_already_vulnerable_to_simple_yet_dangerous_attacks_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Case-study attacks; Commercial browsing/computer-use and research agents. Secondary source tags: None assigned |
| Inputs and attacker control | Reddit post, retrieved synthetic paper, malicious page. Controlled exposed page/document |
| Trust boundary and mechanism | Content to forms/downloads/research answers. Direct and indirect instruction deception |
| Measured endpoint and conditions | 10/10 form submission conditional on encounter;10/10 test executable run;100/100 PaperQA retrieval |
| Defense and utility | Defenses proposed, not evaluated |
| Major limitations | Synthetic/local experiments; no infection or physical harm demonstrated; several case denominators absent |
| Standalone-versus-agent comparator | Direct URL differs from encountered-post protocol |
| Source locators | C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14; physical pp.1,2,4,5,6,7,8,10 |

### [FORGE](../records/forge_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Search manipulation; Twelve primary search models. Secondary source tags: web-agent |
| Inputs and attacker control | Top-three replaced search pages. Assumed fixed retrieval placement |
| Trust boundary and mechanism | Retrieved marketing claims to recommendation. Fake brand recommendation attack |
| Measured endpoint and conditions | 225 queries/model;13.3–73.8% recommendation, mean42.7% |
| Defense and utility | Warnings, classifiers and reasoning toggles; rejection costs separate |
| Major limitations | No demonstrated purchase; language and rank subsets differ; Rec definition and backend tables conflict |
| Standalone-versus-agent comparator | Reasoning ON/OFF is not standalone versus agent |
| Source locators | forge_c01, forge_c02, forge_c03, forge_c04, forge_c05, forge_c06, forge_c07, forge_c08, forge_c09, forge_c10, forge_c11, forge_c12, forge_c13, forge_c14, forge_c15, forge_c16; physical pp.1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26 |

### [How Adversarial Environments](../records/how_adversarial_environments_mislead_agentic_ai_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Tool-output manipulation; Browsing/retrieval agents and Reflexion. Secondary source tags: None assigned |
| Inputs and attacker control | Retrieved documents and linked phantom pages. Controlled fake content and links |
| Trust boundary and mechanism | External text to belief and navigation. Belief contamination and phantom traversal |
| Measured endpoint and conditions | DR excludes abstentions; ER/BW track phantom engagement |
| Defense and utility | Perplexity and spot checks; utility cost |
| Major limitations | Table A5/Figure A2 thresholds and utility conflict; error-heavy cohorts; no observed victim harm |
| Standalone-versus-agent comparator | None |
| Source locators | C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16 |

### [Indirect Prompt Injection in Real-World Applications](../records/indirect_prompt_injection_real_world_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Attack mechanisms; LLM-integrated retrieval/tools; selected Bing/Copilot and synthetic systems. Secondary source tags: prompt-injection |
| Inputs and attacker control | Retrieved pages, code, email/search and memory. Control potential inference-time inputs; no target-model control or required direct conversation access |
| Trust boundary and mechanism | Third-party data → unauthorized instruction; output → later retrieval/memory. Selected demonstrations of instruction redirection, propagation, persistent memory and search reinforcement |
| Measured endpoint and conditions | Qualitative intended-behavior demonstrations; no trial denominator or global ASR |
| Defense and utility | Proposed defenses not established as robust |
| Major limitations | Prepared tool interfaces and synthetic search differ from real-network demonstrations; context-sensitive Copilot |
| Standalone-versus-agent comparator | No matched numerical standalone comparison |
| Source locators | C01/C02/C05/C06/C08–C13/C18/C20; pp.2–10 |

### [Mind the Web — manuscript](../records/mind_the_web_the_security_of_web_use_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Task-aligned prompt injection; Five browser deployments; Browser-Use automated and four manual. Secondary source tags: web-agent |
| Inputs and attacker control | Third-party content on controlled sites and dedicated live test accounts. Remote visible-content modification; task knowledge; permissions/session dependent |
| Trust boundary and mechanism | Untrusted page text to privileged browser actions. Malicious instructions disguised as task-helpful guidance; offline SFT/DPO after interactive preprocessing |
| Measured endpoint and conditions | Generator12/54/61/82/63% ASR;100 trials/experiment; repeated transfer rates |
| Defense and utility | Proposed oversight, execution constraints and task-aware reasoning; no quantified tests |
| Major limitations | 1500 candidates/~300 SFT/12000 pairs; undated supplied manuscript; no published-version judge calibration; Sonnet naming conflict; demo-bank $10000 is not real financial loss; Operator P9 manually adapted |
| Standalone-versus-agent comparator | None; generator baselines are not standalone victims |
| Source locators | claim_01, claim_02, claim_03, claim_04, claim_05, claim_06, claim_07, claim_08, claim_09, claim_10, claim_11, claim_12, claim_13, claim_14, claim_15, claim_16; physical pp.1–13 |

### [Mind the Web — published](../records/mind_the_web_the_security_of_web_use_agents_5a834c4e_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Task-aligned prompt injection; Five browser deployments; Browser-Use automated and four manual. Secondary source tags: web-agent |
| Inputs and attacker control | Third-party content on controlled sites and dedicated live test accounts. Remote visible-content modification; task knowledge; permissions/session dependent |
| Trust boundary and mechanism | Untrusted page text to privileged browser actions. Malicious instructions disguised as task-helpful guidance; offline SFT/DPO after interactive preprocessing |
| Measured endpoint and conditions | Generator12/54/64/85/63% ASR;100 trials/experiment; repeated transfer rates |
| Defense and utility | Task/action judge with session replay/fuzzing; qualitative only |
| Major limitations | 2000 candidates/~400 SFT; judge sampling/precision conflicts; partial deviation may count as success; Comet delivery unconfirmed; demo-bank $10000 is not real financial loss; Operator P9 manually adapted |
| Standalone-versus-agent comparator | None; generator baselines are not standalone victims |
| Source locators | C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16, C17, C18; physical pp.1–17 |

### [Retrieval Barrier](../records/retrieval_barrier_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Retrieval and downstream attack; BEIR embedding search, RAG, email tools. Secondary source tags: prompt-injection |
| Inputs and attacker control | One poisoned document and retrieved content. Query-aware document insertion |
| Trust boundary and mechanism | Retrieval placement to instructions and tools. Optimized embeddings/prefix and downstream injection |
| Measured endpoint and conditions | Recall distinct from harm; GPT-4o CEM email.02, phishing.66, broadcast.92, code.04 single/.72 multi |
| Defense and utility | No complete evaluated defense |
| Major limitations | FiQA-only eight-model result; theorem proof absent; per-task5 runs; Figure9 model counts conflict |
| Standalone-versus-agent comparator | Adapted multi-agent payload/framework; no matched standalone comparator |
| Source locators | C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16, C17, C18; physical pp.1,2,3,4,5,6,7,8,9,10,11,12,13,14,19,20 |

### [SearchGeo](../records/searchgeo_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Search manipulation; Thirteen primary search configurations. Secondary source tags: information-seeking, web-agent |
| Inputs and attacker control | Controlled ranked search snippets/pages. Fixed first-query/rank placement |
| Trust boundary and mechanism | Forced retrieval exposure to endorsement. Generative answer optimization and malicious recommendations |
| Measured endpoint and conditions | 264 attacked plus44 clean cases/model; endorsement0–31.4%; not executed harm |
| Defense and utility | OpenClaw guard variants and18/26 probes |
| Major limitations | Silent54/359 failures; modified system conditions differ; command generation does not prove installation |
| Standalone-versus-agent comparator | No matched standalone comparator |
| Source locators | searchgeo_c01, searchgeo_c02, searchgeo_c03, searchgeo_c04, searchgeo_c05, searchgeo_c06, searchgeo_c07, searchgeo_c08, searchgeo_c09, searchgeo_c10, searchgeo_c11, searchgeo_c12, searchgeo_c13, searchgeo_c14, searchgeo_c15; physical pp.1,2,3,4,5,6,7,8,9,10,13,18,19,22 |

### [TRAP](../records/its_a_trap_task_redirecting_agent_persuasion_benchmark_for_web_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Task-redirecting persuasion; Browser agents on six synthetic cloned services. Secondary source tags: benchmark, web-agent |
| Inputs and attacker control | Visible links, buttons and injected text. One injected placement/interface per task combination |
| Trust boundary and mechanism | Page content to navigation action. Task-aligned persuasion and interface affordances |
| Measured endpoint and conditions | 948/3780 click-and-redirect successes; no downstream-harm rate |
| Defense and utility | No implemented defense evaluation |
| Major limitations | Button success shares are not category ASR; transfer conditioned on source success; Table5/Table15 aggregate discrepancy; updated models use five sites |
| Standalone-versus-agent comparator | None |
| Source locators | trap_claim_01, trap_claim_02, trap_claim_03, trap_claim_04, trap_claim_05, trap_claim_06, trap_claim_07, trap_claim_08, trap_claim_09, trap_claim_10, trap_claim_11, trap_claim_12, trap_claim_13, trap_claim_14, trap_claim_15, trap_claim_16 |

### [Unsafe LLM Search](../records/unsafe_llm_search_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Production search safety; Seven AI search engines. Secondary source tags: information-seeking, web-agent |
| Inputs and attacker control | Malicious URLs and query responses. Risk sampling and two fictional configuration cases |
| Trust boundary and mechanism | URL recommendation to possible downstream exposure. Malicious sources and page guidance |
| Measured endpoint and conditions | Main-risk queries up to41/100; classification risk, not actual harmful execution |
| Defense and utility | 46-response DSR conversion; HTML classifier P.838/R.807/F1.822 |
| Major limitations | 2024/25 snapshot; uncertain URLs; differing denominator protocols; benign FP13/121 not established utility cost |
| Standalone-versus-agent comparator | Traditional search task comparison is not matched LLM/agent |
| Source locators | unsafe_search_c01, unsafe_search_c02, unsafe_search_c03, unsafe_search_c04, unsafe_search_c05, unsafe_search_c06, unsafe_search_c07, unsafe_search_c08, unsafe_search_c09, unsafe_search_c10, unsafe_search_c11, unsafe_search_c12, unsafe_search_c13, unsafe_search_c14, unsafe_search_c15, unsafe_search_c16; physical pp.1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21 |

### [WAAA](../records/waaa_web_adversaries_against_agentic_browsers_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Web adversary taxonomy; Playwright-MCP and BrowserOS; four-model trial matrix. Secondary source tags: web-agent |
| Inputs and attacker control | Attacker markup, script, screenshots/HTML. Gadget/page control; selected custom code/file tools |
| Trust boundary and mechanism | Agent bridges sites and invokes authorized external tools. Confusion, injection, URL inference, prompt leaks, integration misuse |
| Measured endpoint and conditions | Ten runs per tested class/model; SQ-1 navigation10/10;13 numeric rows versus14 claimed |
| Defense and utility | BrowseSafe missed4 selected pages; architectural defenses untested |
| Major limitations | Native SOP exploit not established; unsupported I-1/I-2 untested; delegation prompt/version effects; metadata and60/20/38 counts conflict |
| Standalone-versus-agent comparator | No matched standalone comparator |
| Source locators | waaa_c01, waaa_c02, waaa_c03, waaa_c04, waaa_c05, waaa_c06, waaa_c07, waaa_c08, waaa_c09, waaa_c10, waaa_c11, waaa_c12, waaa_c13, waaa_c14; physical pp.4,5,6,9,10,11,12,14 |

### [When AI Meets the Web](../records/when_ai_meets_web_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Web chatbot plugin security; Seventeen plugins and11-model local simulation. Secondary source tags: prompt-injection, web-agent |
| Inputs and attacker control | Browser-supplied history; scraped reviews; RAG. Nonprivileged user request tampering or permitted UGC |
| Trust boundary and mechanism | Attacker-controlled roles/content to privileged messages/tools. History forgery, unsafe role insertion, context/tool hijack |
| Measured endpoint and conditions | Ten runs/cell; specified tool call/URLs;live219/300heuristic prompt-leak union |
| Defense and utility | Role isolation, wrapping, hardened tool instructions;UGCBusterprototype |
| Major limitations | SelectedP1live sample;13/100exposure notattackrate;system role only5models;adaptive/utility evidence incomplete |
| Standalone-versus-agent comparator | Role/insertion controls are not standalone-versus-agent |
| Source locators | claim_01, claim_02, claim_03, claim_04, claim_05, claim_06, claim_07, claim_08, claim_09, claim_10, claim_11, claim_12, claim_13, claim_14; physical pp.3,4,5,6,7,8,9,10,11,12,13,14,15,20 |

## Visual and multimodal manipulation

Pixel, HTML/accessibility and caption control differ. WebCloak reverses the victim perspective to the scraper.

### [Dissecting Adversarial Robustness](../records/dissecting_adversarial_robustness_of_multimodal_lm_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Multimodal adversarial agents; Captioner or self-captioning web agent. Secondary source tags: multimodal |
| Inputs and attacker control | Attacker-edited page images/captions. Forced attack exposure; captioner access differs |
| Trust boundary and mechanism | Image interpretation to action. Adversarial caption/image optimization |
| Measured endpoint and conditions | GPT4o caption attack agentASR31% vs captionASR92% |
| Defense and utility | Reflexion and attack-aware optimizations studied |
| Major limitations | 200 solvable selected tasks; hybrid white/black-box threat model; textual/caption success differs from completed goal |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | C01 through C15; physical source pages in claim locators |

### [EIA](../records/eia_environmental_injection_attack_on_generalist_web_agents_for_privacy_leakage_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Environmental privacy-leakage attack; SeeAct; GPT-4V and two Llava backbones. Secondary source tags: prompt-injection, web-agent |
| Inputs and attacker control | Attacker-modified HTML; screenshots; private task/history. Control webpage elements, text/aria labels, placement, opacity and automatic submission; no prior task/history knowledge |
| Trust boundary and mechanism | Environmental field → grounding/generation → typed private content. Invisible FI/MI influences grounding; visible Relaxed-EIA also changes screenshot-based generation |
| Measured endpoint and conditions | 177 curated offline action steps; peak specific-PII ASR 70% GPT-4V/MI/P+1; full-request peak 16% GPT-4V/FI text/P−3/opacity 0.2. ASR requires injected-element selection and value similarity >0.95 |
| Defense and utility | Three warning prompts leave similar ASR; human supervision proposed, not tested |
| Major limitations | Peaks are not pooled averages; next-step integrity is not whole-task integrity; no separate aggregate server-exfiltration rate; Table 1 variance/aggregation anomaly |
| Standalone-versus-agent comparator | No matched standalone security comparator |
| Source locators | eia_claim_01–14; pp.4–9,17,24,28,32 |

### [Pop-ups](../records/attacking_vision_language_computer_agents_via_pop_ups_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Visual/accessibility attack; OSWorld screen/SoM and VisualWebArena SoM agents; five closed VLMs. Secondary source tags: multimodal |
| Inputs and attacker control | Pop-up pixels, ALT/a11y descriptions, user/task context. Default knows user query, coordinates/tag ID and framework; weaker knowledge variants evaluated |
| Trust boundary and mechanism | Untrusted attention hook/instruction → executable click. Task-related hooks plus click commands, OK banner and adversarial ALT |
| Measured endpoint and conditions | Step ASR80–100% OSWorld-Screen,88.7–95.3% OSWorld-SoM,62.1–78.4% VWA; 50/72 selected tasks. Clicks suppressed; no redirect/download endpoint |
| Defense and utility | Step-wise prompt:5.9% step ASR/32% task TASR; variant10.4%/44%; task utility8/10% vs18% benign |
| Major limitations | Ideal default access; closed versions; missing repeat intervals; headline aggregation and defense-percentage discrepancy |
| Standalone-versus-agent comparator | No matched standalone security comparator |
| Source locators | claim_01–15; pp.2–10,12–15 |

### [WebCloak](../records/webcloak_characterizing_and_mitigating_threats_from_llm_driven_web_agents_as_intelligent_scrapers_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Website-owner anti-scraping defense; L2S/LNC/LWA extraction pipelines. Secondary source tags: scraping, web-agent |
| Inputs and attacker control | 237 offline snapshots; image DOM and hidden text. Novice/intermediate scraper user; selected prompt adaptation |
| Trust boundary and mechanism | Parsing/semantic interpretation to extraction. Dynamic structural obfuscation and defensive semantic injection |
| Measured endpoint and conditions | Selected27-page mean88.7% recall to0; adaptive KA nonzero0.20/1.58/0 |
| Defense and utility | Dual-layer anti-scraping; not agent-safety defense |
| Major limitations | Offline preprocessing;10-page audio/text;35-user utility; baseline/DeepSeek/load-time conflicts |
| Standalone-versus-agent comparator | No otherwise matched standalone comparator |
| Source locators | C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16; physical pp.4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 |

### [WebInject](../records/webinject_prompt_injection_attack_to_web_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | White-box visual injection; Five screenshot-driven open-weight models. Secondary source tags: prompt-injection, web-agent |
| Inputs and attacker control | Page rendering and ICC-transformed screenshots. Full source control, weights, target monitor/prompts |
| Trust boundary and mechanism | Source-controlled pixels to next-action output. U-Net mapping surrogate and constrained PGD |
| Measured endpoint and conditions | Exact next-action ASR.963–.975 over ten datasets; not executed harmful outcomes |
| Defense and utility | Detection/adversarial training proposed, not tested |
| Major limitations | 212real+500synthetic; random histories; adapted screenshot baseline;Phi4aggregate.963versusderived.9725 |
| Standalone-versus-agent comparator | No otherwise matched standalone comparator |
| Source locators | C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15; physical pp.1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21 |

## Tool, execution and component attacks

Tool-document selection, component-local backdoors and installed executable skills require different privileges.

### [BackdoorAgent](../records/backdooragent_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Tool, execution and component attacks; Component replacement across planning, memory and tools; instrumented runtime. Secondary source tags: None assigned |
| Inputs and attacker control | Author-reported: planning artifacts, external memory or retrieval content, and tool/environment feedback. Attacks modify one component or its outputs, which may influence later context and state. Agent Web includes multimodal perception and action, with interface misdirection such as incorrect purchases described as a harm example. |
| Trust boundary and mechanism | A modular stage-aware runtime with injection hooks, component-local attack wrappers, configurable agent execution, and structured trajectory logging; benchmark evaluations across QA, Code, Web, and Drive; seven named attacks; clean task accuracy, attack success rate, and attacked task accuracy; family aggregation, poisoning-ratio and token-overhead analyses, and exploratory probability-based detection. |
| Measured endpoint and conditions | GPT aggregate ASR43.58/77.97/60.28%; DeepSeek tools42.20 exceeds memory38.91 |
| Defense and utility | Exploratory probability-based detection, not deployed action containment. Seven attacks across QA/Code/Web/Drive use heterogeneous access; key datasets/N/weights/seeds absent. |
| Major limitations | No dataset sizes, seeds or aggregation weights; abstract persistence is not a longitudinal measure; high ASR can coexist with high task ACC; prose/table mismatches flagged; no otherwise matched standalone adversarial test |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | C01 through C14; physical pages in locators |

### [SkillTrojan](../records/skilltrojan_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Tool, execution and component attacks; Persistent installed executable packages; fragmented encrypted payload and runtime reconstruction. Secondary source tags: None assigned |
| Inputs and attacker control | Installed skill packages combining natural-language specifications and executable scripts; conditional skill instructions, tool-output fields, run-local trajectories, fragment-emitting actions, and an attacker-modified verification action. Persistence resides in installed packages; reconstruction state is single-run only. Payload consequences depend on execution permissions. |
| Trust boundary and mechanism | Encrypt and partition an attacker-selected payload into indexed fragments; modify skill instructions and actions for trigger-conditioned emission; collect fragments during normal workflow execution; verify completeness, reconstruct by index, decrypt, and execute a side effect. Evaluate clean ACC and triggered ASR on EHR SQL and SWE-Bench Verified, plus scanner, fragmentation, encoding, trigger-prevalence, native-skill, and cross-framework analyses. |
| Measured endpoint and conditions | GPT5.2 EHR ACC89.3/ASR97.2; open-model native-stack accuracy losses1.9–6pp |
| Defense and utility | Two narrow static-scanner settings; native-stack utility losses1.9–6pp. Installed executable-package control differs from page edits; persistence resides in packages, fragments are run-local. |
| Major limitations | Stronger attacker access than page editing; absent EHR N and uncertainty; QwenVL ASR26.7 below AgentPoison37.6; static scanner results are narrow; no matched standalone comparison |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | C01 through C15; physical pages in locators |

### [ToolHijacker](../records/toolhijacker_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Tool-document injection; Two-stage retriever and selection LLM; R/S shadow optimization. Secondary source tags: prompt-injection, tool-use |
| Inputs and attacker control | Third-party tool names/descriptions in library. Library document insertion; no target queries/weights/library access; shadow models |
| Trust boundary and mechanism | Untrusted documentation → retrieved candidate → selected tool. Optimize retrieval relevance then tool-choice instructions |
| Measured endpoint and conditions | 10tasks×100phrases/dataset; GPT4oGFASR96.7%Meta/88.2%ToolBench, GB92.2/83.9; ASRselection, AHRretrieval |
| Defense and utility | StruQ/SecAlign residual84.6–99.6% scoped selectionASR; detector10maliciousdocs/dataset, gradientfreeFNR100% |
| Major limitations | No harmful tool deployment/execution; small ablations/detector/human samples; non-targetASR notfullutility; technicalreport tasks/prompts absent; table/prose conflicts |
| Standalone-versus-agent comparator | No matched standalone security control |
| Source locators | TH-C01–15; pp.2–12,14–18 |

## Memory and persistent compromise

Direct writes differ from environmental instructions that later enter memory; conditional memory usage is not completed harm.

### [Context Manipulation](../records/context_manipulation_attacks_web_agents_are_susceptible_to_corrupted_memory_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Stored-context / plan corruption; Browser-use controller versus Agent-E planner/executor; GPT-4o/mini. Secondary source tags: memory, web-agent |
| Inputs and attacker control | Stored history/plans; retrieved web data as a separate vector. Direct context write assumed; original task, browser observations, system/code protected in restricted evaluation |
| Trust boundary and mechanism | Application-managed memory/plan → planner authority → browser actions. Noncontextual, task-aligned and context-chained malicious plan/history edits |
| Measured endpoint and conditions | Plan benchmark4×15 samples×5 runs; opinion94.7% versus factual18.7% task-aligned ASR; privacy35.6→53.3% (17.7pp). Separate45-task privacy suite; tool access versus full exfiltration distinct |
| Defense and utility | SECURE/SANDWICH reduce retrieved-content injection but tested context corruption persists; reported Agent-E46% / Browser-use63% scoped privacy outcomes, endpoint ambiguities retained |
| Major limitations | Storage access acquisition not established end-to-end; unspecified privacy repetitions/judge/model snapshots; headline endpoint/greater-than80% wording conflicts; hierarchy not isolated causally; Task Shield not tested |
| Standalone-versus-agent comparator | Agent architecture/attack-vector comparison, no standalone control |
| Source locators | C01–14; pp.4–8 |

### [Hidden in Memory](../records/hidden_in_memory_sleeper_memory_poisoning_in_llm_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | External-content sleeper memory poisoning; Model-managed or external memory writer; semantic/LLM/full-context retrieval; later tool/behavior generation. Secondary source tags: memory |
| Inputs and attacker control | Uploaded/web/repository content → fabricated user memory. Externalcontent control, no directstoreaccess, absentlater; actor–critic reusablepayload/adaptivevariant |
| Trust boundary and mechanism | External data → persistent user state → later retrieved authority/action pursuit. Induce user-memorywrite, retrieve after originalpayloadgone, assimilate into behavior/tools |
| Measured endpoint and conditions | 700injectionpairs500behavior/200actions; GPT5.5toolbehaviorIR99.8±0.3%; standardizedadjacentagentAUR60–89% conditionalavailablememory; coupledexternalmanageragentE2E3–66% distinct |
| Defense and utility | GEPA/spotlighting modeldependent/adaptivelybrittle; KimiBehavior6.2→64.6%IR; benigndirectsave70/cell notbaselinefullutility; probesexperimental |
| Major limitations | Broadjudge countsclaims/attempts/pursuit, notonlycompletedharm; standardizedmemoryfallback; semanticE2Eestimated; selectedproduction25cases; bundledsetup and sourceconflicts |
| Standalone-versus-agent comparator | Providerharnessswap, no matched tool-free/web-agent security control |
| Source locators | C01–15; pp.1–9,14–18,31–32,43–50,57,71–72,79–81 |

## Long-horizon and resource attacks

Task disruption, tokens, runtime and projected money are separate outcomes. Denial of Wallet is a non-LLM analogy.

### [AgentLAB](../records/agentlab_benchmarking_llm_agents_against_long_horizon_attacks_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Long-horizon security benchmark; Tool-enabled agents in28environments,644tasks. Secondary source tags: benchmark, long-horizon |
| Inputs and attacker control | User prompts, tool outputs, persistent preferences. User or environment control;task injection privileged traces |
| Trust boundary and mechanism | External input to action chains and later memory retrieval. Intent/tool-chain/drift/task/memory adaptive strategies |
| Measured endpoint and conditions | Full-objective ASRauthorreported;Claude task0butchain73.3%;GPT5aggregation unresolved |
| Defense and utility | SR/LG/RP/DD effects scoped by attack;no reported benign utility |
| Major limitations | Familydenominators absent;success-onlyT2S;9versus10risks;GPT5overall69.9versusderived60.18 |
| Standalone-versus-agent comparator | One-shot/multi-turn agents, not matched standalone comparison |
| Source locators | claim_01_benchmark_scope, claim_02_threat_surfaces, claim_03_multi_agent_method, claim_04_tool_chaining_results, claim_05_one_shot_comparison, claim_06_turn_metric_condition, claim_07_turn_ablation, claim_08_defense_conditions, claim_09_task_injection_privilege, claim_10_memory_access, claim_11_overall_arithmetic, claim_12_preliminary_scope, claim_13_web_agent_relevance, claim_14_shopping_drift; physical pp.1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19 |

### [Autonomy Comes with Costs / AgentDoS](../records/autonomy_comes_with_costs_detecting_denial_of_service_vulnerabilities_caused_by_resource_abusing_in_llm_based_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Resource-exhaustion availability; 20open-source web-service agent applications; static/grey-box detector. Secondary source tags: resource-exhaustion |
| Inputs and attacker control | Prompt APIs, file-download/parse tools, session artifacts. Remote prompt API access; benign agent/developer and uncompromised environment; detector has source/traces |
| Trust boundary and mechanism | User requests → tool/operator execution → host memory/disk retention. Exhaust short-lived resources within a turn, long-lived within session, persistent across sessions |
| Measured endpoint and conditions | 36confirmed vulnerabilities in16/20agents,15CVEs; recall36/38 constructed defect set versus adapted AgentFuzz3/38;119.08CPUhours,9.32Mtokens/agent |
| Defense and utility | Reported AutoGPT100MB/download,1GB/execution-directory and task-end deletion; no separate controlled defense-utility trial |
| Major limitations | Minimal-resource Docker/GPT-4.1 settings,20min/sink/early skips; constructed recall denominator; scheduling FN13table versus9prose; source access required |
| Standalone-versus-agent comparator | No matched standalone control; added resource-lifecycle surface is mechanism inference |
| Source locators | C01–13; pp.4–15 |

### [Beyond Max Tokens](../records/beyond_max_tokens_stealthy_resource_amplification_via_tool_calling_chains_in_llm_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Resource amplification; Tool-calling agents with stub MCP servers. Secondary source tags: resource-exhaustion, tool-use |
| Inputs and attacker control | Malicious server descriptions/progress/errors. Control of server-side descriptions and returns |
| Trust boundary and mechanism | Untrusted tool metadata/output to further paid inference. Adaptive interaction-chain continuation |
| Measured endpoint and conditions | Output-token ratios up to31.43x/58.10x in named tool/model cells |
| Defense and utility | Token/call caps and content detectors tested |
| Major limitations | Stubbed environment; no production losses; six-call and one-call targets incompatible; visible cap trend contradicts prose; token/energy/throughput distinct |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | C01 through C15; physical source pages in claim locators |

### [Breaking Agents](../records/breaking_agents_compromising_autonomous_llm_agents_through_malfunction_amplification_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Malfunction amplification; Emulated ReAct and LangChain Gmail/CSV. Secondary source tags: None assigned |
| Inputs and attacker control | Instructions, email/CSV, memory and upstream agents. Black-box core; stronger memory/upstream-control variants |
| Trust boundary and mechanism | External instructions to repeated or irrelevant action. Loop and incorrect-function injection; perturbation/demonstration |
| Measured endpoint and conditions | Task failure: baseline15.3%, loop59.4%; not verified harmful action |
| Defense and utility | Policy/malfunction self-examination detects prompts; no protected-task utility |
| Major limitations | Emulator144cases versus two implemented agents; toolkit inventory and table references inconsistent; cell denominators absent |
| Standalone-versus-agent comparator | None; core-model swaps are not agentization control |
| Source locators | C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14; physical pp.1–13 |

### [Denial of Wallet](../records/denial_of_wallet_defining_a_looming_threat_to_serverless_computing_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Resource and billing exposure; OpenFaaS testbed plus AWS timing. Secondary source tags: resource-exhaustion |
| Inputs and attacker control | Incoming serverless requests. External request load |
| Trust boundary and mechanism | Public request to metered execution. Invocation amplification and sustained low-rate abuse |
| Measured endpoint and conditions | Local invocation/load measurements; projected historical bills |
| Defense and utility | WAF qualitative rerun; evasion proposals untested |
| Major limitations | Projected cost is not observed financial loss; emulator and AWS memory settings differ; no LLM experiment |
| Standalone-versus-agent comparator | None |
| Source locators | C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15 |

### [IAL-SCAN](../records/when_agents_do_not_stop_uncovering_infinite_agentic_loops_in_llm_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Availability/static analysis; Agent-loop code detector. Secondary source tags: None assigned |
| Inputs and attacker control | Repository Python source. No runtime adversary tested |
| Trust boundary and mechanism | Loop termination and cost authority. Static potential infinite-loop patterns |
| Measured endpoint and conditions | 74 alerts;68 confirmed;6 false positives |
| Defense and utility | Detector, not runtime containment |
| Major limitations | 6549 repositories;91.9% alert precision;90.7% discovered-union coverage is not corpus recall; no observed financial loss |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | IAL_C01 through IAL_C14; physical source pages in claim locators |

### [Overthinking Loops](../records/overthinking_loops_in_agents_a_structural_risk_via_mcp_tools_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | MCP resource/cost attack; ReAct100tools;QwenCode44tools;14maliciousadditions across3servers. Secondary source tags: resource-exhaustion, tool-use |
| Inputs and attacker control | Third-party metadata and return instructions. Co-register cycletools; models/userqueries fixed; autonomoussettings |
| Trust boundary and mechanism | Tool-visible text → repeated/cyclic calls → cumulative tokens/runtime. Repetition, forced refinement and distraction loops |
| Measured endpoint and conditions | 5runs/config;7screenedCodeElo tasks; headlineMiniMax142.35×tokens/27.49×time, case609.71×/180.12×; forcedtermination/nooutput |
| Defense and utility | NoWait-enablednormal/mixedstill15.37×DeepSeekAIME; registryfiltering/strictercapsuntested |
| Major limitations | Meanratios vs ratiosums conflict; narrowselectedtasks; GLMversion changes; nointervals/fullstopflags; hypothesizedinterleaving notproved |
| Standalone-versus-agent comparator | Existingagent registrycontrol, no standalone/web-agent comparison |
| Source locators | C01–14; pp.1–7,10–12 |

## Benchmarks and evaluation methods

Security trials and benign evaluator studies are distinguished in each profile. Judge agreement is not acting-agent success or security.

### [AgentDojo](../records/agentdojo_a_dynamic_environment_to_evaluate_prompt_injection_attacks_and_defenses_for_llm_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Stateful tool attack/defense benchmark; Tool-calling LLM agents in four simulated applications. Secondary source tags: defense, prompt-injection |
| Inputs and attacker control | Email, webpages, files and application tool responses. Inject designated output placeholders; knowledge/control fraction varies; no OS/model compromise |
| Trust boundary and mechanism | Third-party text → planning → user-privileged mutable tool state. Important-message, fake-role and other prompts redirect tools toward attacker goals |
| Measured endpoint and conditions | 97 user tasks/27 targets/629 paired cases; GPT-4o Table 3 targeted47.69% +/-3.90 (95% CI); distinct Table 5 baseline57.69% +/-3.9 |
| Defense and utility | Table 5 tool filter6.84% +/-2.0 targeted ASR, utility73.13% benign/56.28% attacked; detector7.95% ASR but41.49% benign utility |
| Major limitations | Synthetic text-only state; simple attack families; filter fails if needed tools also enable goal; counts/rates conflict; no persistent multi-task evaluation |
| Standalone-versus-agent comparator | No matched standalone security comparator |
| Source locators | C01–C16; pp.1–9,20–21,24–26 |

### [AgentRewardBench](../records/agentrewardbench_evaluating_automatic_evaluations_of_web_agent_trajectories_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Evaluation reliability benchmark; BrowserGym/AgentLab agents plus rules and LLM judges. Secondary source tags: benchmark, progress-evaluation, web-agent |
| Inputs and attacker control | Accessibility trees, screenshots, agent reasoning/action histories. No adversarial attacker evaluated |
| Trust boundary and mechanism | Browser execution outcome versus evaluator approval (analyst security relevance). Benign misleading reasoning/incomplete execution; potential side effects separately labeled |
| Measured endpoint and conditions | 1,302 trajectories/351 tasks/4 agents/5 benchmarks; GPT-4o(A) success P69.8/R83.1/F175.9 versus rules83.8/55.9/67.1; false positives30.2% of predicted successes |
| Defense and utility | No evaluated attack defense; expert reference labels and representation comparisons |
| Major limitations | Agreement89.3% only GPT-4o/WebArena success subset; Tables9–12 duplicate all-agent Table8; optimality prompt versus3 reported dimensions; no attack rates inferred |
| Standalone-versus-agent comparator | No matched standalone security comparator |
| Source locators | C01–16; pp.4–9,13,17–23 |

### [An Illusion of Progress](../records/an_illusion_of_progress_assessing_the_current_state_of_web_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Live web-agent capability and evaluator reliability; Six browser agents; WebJudge key points, selected screenshots and action history. Secondary source tags: progress-evaluation, web-agent |
| Inputs and attacker control | Real website observations and agent trajectories. No tested adversary |
| Trust boundary and mechanism | Observation → action; trajectory → evaluator decision. Constraint failures and unsupported final-response assertions; benign errors |
| Measured endpoint and conditions | 300 tasks/136 sites; human Operator61.3%, Claude3.7 56.3%; judge o4 agreement85.7% and average SR gap3.8pp |
| Defense and utility | Evidence-based success judging; strict o4 precision82/recall47.8% on reused AgentRewardBench |
| Major limitations | Search ablation baseline26% vs main30% unresolved; success-only efficiency; dynamic tasks; reused trajectories not independent outcome evidence |
| Standalone-versus-agent comparator | Different agents/benchmarks and judge comparisons; no matched standalone security experiment |
| Source locators | claim_01–16; pp.3–10,19–21,26,30 |

### [Canary Tokens](../records/canary_tokens_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Crawler attribution; Twenty seeded sites,22 chatbots. Secondary source tags: scraping, web-agent |
| Inputs and attacker control | Token-bearing content and answer citations. Detection study; no compromise attacker |
| Trust boundary and mechanism | Observed tokens to crawler attribution. Per-site random token attribution |
| Measured endpoint and conditions | 18/22 attribution;12/18 post-restriction observations |
| Defense and utility | Detection/attribution, not a prevention defense |
| Major limitations | Cache provenance unknown; no proved fresh crawl or training memorization; threshold equation inconsistent; operator intent inferred |
| Standalone-versus-agent comparator | No matched standalone comparator |
| Source locators | canary_claim_01, canary_claim_02, canary_claim_03, canary_claim_04, canary_claim_05, canary_claim_06, canary_claim_07, canary_claim_08, canary_claim_09, canary_claim_10, canary_claim_11, canary_claim_12, canary_claim_13, canary_claim_14, canary_claim_15; physical pp.4,5,6,7,8,9,10,11,12,13,14,15,16 |

### [DoomArena](../records/doomarena_a_framework_for_testing_ai_agents_against_evolving_security_threats_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Benchmarks and evaluation methods; Environment wrappers inject configurable attacks into tau-Bench, WebArena and OSWorld. Secondary source tags: benchmark |
| Inputs and attacker control | Malicious user conversations; queried product catalogs and databases; webpage banners using accessibility attributes; pop-ups with hidden accessibility-tree-like instructions; screenshot overlays in desktop environments. Attacker control and success criteria differ across these surfaces. |
| Trust boundary and mechanism | A modular security-testing layer uses attack configurations, reusable attack implementations, environment-specific gateways, success filters, and optional aborting defenses. Evaluations use 50 airline tasks, 115 retail tasks, 114 Reddit tasks, 192 Shopping tasks, and a stated 39-task OSWorld subset. Metrics are attack success, legitimate task success with and without attacks, and joint-success stealth. |
| Measured endpoint and conditions | Browser judge conditions report0 ASR and0 attacked-task success; combined attacks have narrower triggered cohorts |
| Defense and utility | Aborting judge/restricted LlamaGuard category; clean and attacked task success separate.50 airline/115 retail/114 Reddit/192 Shopping/stated39 OS tasks; combined results condition on both attacks triggered. |
| Major limitations | Different environments/goals/control and model versions are not matched; URL redirect is not proven exfiltration; restricted LlamaGuard category; no own standalone comparison |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | C01 through C14; physical pages in locators |

### [Formalizing Prompt Injection](../records/formalizing_prompt_injection_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Controlled attack/defense benchmark; Instruction/data LLM applications across NLP tasks. Secondary source tags: benchmark, defense, prompt-injection |
| Inputs and attacker control | Attacker-replaced application data. Arbitrary injected instructions/data; no target-instruction or backend modification |
| Trust boundary and mechanism | Legitimate instruction versus untrusted data; backend assumed intact. Naive, escape characters, context ignoring, fake completion and combined attacks |
| Measured endpoint and conditions | GPT-4 combined average ASV 0.75 vs naive 0.62: mixed task scores, not deployed-agent compromise probabilities |
| Defense and utility | Ten candidates tested; low FNR can coexist with high FPR and utility loss |
| Major limitations | 100 sampled pairs per combination; incomplete extended matrices; detection prompts scoped |
| Standalone-versus-agent comparator | Ten LLMs/NLP tasks; no matched web-agent versus standalone security test |
| Source locators | C01–C06/C09–C15; pp.2–6,8–14 |

### [GUIDE](../records/guide_interpretable_gui_agent_evaluation_via_hierarchical_diagnosis_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Benign trajectory evaluation; Segmenter, multimodal diagnosis and aggregation. Secondary source tags: benchmark, progress-evaluation |
| Inputs and attacker control | Recorded GUI trajectories. No attacker tested |
| Trust boundary and mechanism | Evaluation context, not an attack boundary. Hierarchical post-hoc diagnosis |
| Measured endpoint and conditions | 95.80% industrial evaluator accuracy; agent SR is separate |
| Defense and utility | No security defense tested |
| Major limitations | 932 industrial trajectories; 200-subtask human check; long-trajectory improvement not monotonic; missing claimed prompt appendix |
| Standalone-versus-agent comparator | None |
| Source locators | guide_claim_01, guide_claim_02, guide_claim_03, guide_claim_04, guide_claim_05, guide_claim_06, guide_claim_07, guide_claim_08, guide_claim_09, guide_claim_10, guide_claim_11, guide_claim_12, guide_claim_13, guide_claim_14 |

### [InjecAgent](../records/injecagent_benchmarking_indirect_prompt_injections_in_tool_integrated_large_language_model_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Benchmarks and evaluation methods; Forced compromised tool response;1054 base/enhanced cases; simulated intermediate data-stealing output. Secondary source tags: benchmark, prompt-injection, tool-use |
| Inputs and attacker control | Attacker-modifiable fields in retrieved tool responses, including website snippets, emails, reviews, notes, tweets, profiles, calendar events, and product/task descriptions. The attacker attempts to convert external content into instructions for harmful tools. Evaluation conditions on successful retrieval and receipt of the injected response. |
| Trust boundary and mechanism | GPT-4-assisted generation and manual refinement of 17 user cases and 62 attacker cases; full cross-product yields 1,054 cases in each of base and fixed-prefix enhanced settings. Thirty agent configurations are evaluated through parsed tool requests. Direct harm requires a harmful invocation; data stealing requires extraction plus transmission using a GPT-4-simulated extraction response. Results distinguish ASR-valid, ASR-all, and output validity, with additional association, content-freedom, sensitivity, quality, and prompt-length analyses. |
| Measured endpoint and conditions | GPT4 ASR-valid23.6→47 versus ASR-all23.3→46.8; Llama70B ASR-valid86.9/88.2 |
| Defense and utility | Function-calling comparisons change interface/model conditions, not an isolated security intervention.17×62=1054 cases each base/enhanced; forced receipt; simulated extraction; valid-only versus all-case denominators. |
| Major limitations | Parsed harmful calls are not production delivery; validity changes denominator; no full user-task utility; function-calling prose reverses model rates; no matched standalone comparator |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | C01 through C16; physical pages in locators |

### [SafeArena](../records/safearena_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Deliberate web-agent misuse benchmark; Five multimodal backbones in BrowserGym on4simulated sites. Secondary source tags: benchmark, web-agent |
| Inputs and attacker control | Harmful/safe user tasks, screenshots and accessibility trees. Malicious task request; decomposition/priming variants, permissions already supplied |
| Trust boundary and mechanism | Task-granted permissions → browser actions/application state; malicious user rather than external-content attacker. Direct harmful instructions, sequential task decomposition, primed continuation |
| Measured endpoint and conditions | 250harmful/250paired safe; GPT-4o functional harmful/safeTCR22.8/34.4%, ARIA-4judge34.7%; Qwen functional26.0%,judge27.3%;49selected refused Claude tasks jailbroken≤3attempts,mean1.26 |
| Defense and utility | Refusal/NSS quantify behavior; classifier/alignment defenses proposed, not tested intervention; NSS denominator successful paired safe tasks |
| Major limitations | Attempt versus completion distinct; judged versus functional metrics differ; selection-limited jailbreak; NSS aggregation unreconstructible under same-pair binary assumption; explicit harmful intents/fragile checks |
| Standalone-versus-agent comparator | Paired safe/harmful controls isolate task capability partially; no standalone-LLM security control |
| Source locators | SA_C01–15 and narrative section14; pp.3–9,14–15,25,37 |

### [SecureWebArena](../records/securewebarena_a_holistic_security_evaluation_benchmark_for_lvlm_based_web_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Multi-stage security benchmark; Nine screenshot/SoM LVLM agents; six simulated applications. Secondary source tags: benchmark, web-agent |
| Inputs and attacker control | User goals; DOM/CSS, rendered overlays and textual page content. User-level goal control separate from environment DOM/CSS/script control; no chrome/system-prompt access |
| Trust boundary and mechanism | Malicious user goal or attacker-controlled environment → reasoning/actions/final state. Jailbreak, direct injection, pop-ups, distraction, ads and indirect injection |
| Measured endpoint and conditions | 330 cases/agent;2970 trajectories. Pop-up final PDR 76.67–100% across models (30 pop-up cases/agent: five per environment); RVR/BCR/PDR are distinct stage endpoints |
| Defense and utility | No defense intervention; model-category comparisons are observational |
| Major limitations | No uncertainty; incomplete live allocation; live only user-level vectors; prose/Table 2 GUI AdInject mismatch; judge85.5% agreement/200 traces |
| Standalone-versus-agent comparator | No matched standalone comparator |
| Source locators | C01_dual_source_threat_model, C02_benchmark_counts, C03_layered_evaluation, C04_annotation_reliability, C05_popup_success, C06_gui_attack_discrepancy, C08_live_scope, C10_author_limitations; pp.3–9 |

### [ST-WebAgentBench](../records/st_webagentbench_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Policy-aware web-agent evaluation; AWM/WebVoyager/WorkArena sharedGPT4o; BrowserGym. Secondary source tags: benchmark, web-agent |
| Inputs and attacker control | Partially trusted DOM/fields; policies/user/task conflicts. Benign operator; targetedUIinjection plus benignerrors/consent/conflicts |
| Trust boundary and mechanism | Environment observation → browser action under organizational>user>taskrules. Environmental directives, fabricatedinputs, hierarchy errors and unconsentedactions |
| Measured endpoint and conditions | 375tasks/3057policyinstances;pass@3 described; CR/CuP33.8/20AWM,12.8/10.3WebVoyager,26/15WorkArena |
| Defense and utility | Policycontext anddeterministicchecks/simulatedautoapproval; controllerproposednot evaluated |
| Major limitations | Aggregatepolicyviolations notASR; riskdenominator/proseconflicts; pass@3/allpassdefinitions; binnedpolicyloadnotcausal; fuzzyconsentnotrealhumanapproval |
| Standalone-versus-agent comparator | No matched standalone security control |
| Source locators | C01–14; pp.2–10,26–30,36–43 |

### [VPI-Bench](../records/vpi_bench_visual_prompt_injection_attacks_for_computer_use_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Visual injection benchmark; Computer-use and browser-use agents. Secondary source tags: multimodal, prompt-injection |
| Inputs and attacker control | 306 simulated web variants:219CUA/87BUA. Controlled chosen page exposure |
| Trust boundary and mechanism | Pixels/UI cues to tool actions. Visual prompt injection |
| Measured endpoint and conditions | Three-run AR attempts and SR full objectives, both/N; CUA3.7 Booking59.4/36.7% |
| Defense and utility | Four defensive prompt configurations; mixed effects |
| Major limitations | UI-TARS high attempts but zero completion; failed execution is not robust refusal; sandbox consequences and judge sample limited |
| Standalone-versus-agent comparator | CUA/BUA tasks and resources differ; no matched standalone comparator |
| Source locators | vpi_claim_01, vpi_claim_02, vpi_claim_03, vpi_claim_04, vpi_claim_05, vpi_claim_06, vpi_claim_07, vpi_claim_08, vpi_claim_09, vpi_claim_10, vpi_claim_11, vpi_claim_12, vpi_claim_13, vpi_claim_14, vpi_claim_15, vpi_claim_16, vpi_claim_17; physical pp.2,4,5,6,7,8,9,10,11,16,17,18,21 |

### [WASP](../records/wasp_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Restricted-contributor web attacks; VWA, Claude CURI and tool-calling scaffoldings. Secondary source tags: benchmark, prompt-injection, web-agent |
| Inputs and attacker control | GitLab issues/comments; Reddit posts/comments; current URL/history. Add own content only; no layout/pop-ups/others' comments; task-aware default and task-agnostic variants |
| Trust boundary and mechanism | Trusted site's contributor content → agent objective; URL fragment → later context → authenticated action. Dependency pretext; URL-fragment payload persistence; plain-text navigation/action instructions |
| Measured endpoint and conditions | Reported84 attack tasks/37 separate utility tasks. o1 system tool loop 85.7% intermediate/16.7% final, utility 48.6%; judged diversion differs from final-state goal check |
| Defense and utility | GPT-4o axtree+SoM warning: 42.9→22.6% intermediate,3.6→1.2% final,62.2→45.9% utility; hierarchy variants remain attackable |
| Major limitations | Two sites; forced exposure; limited prompts; no uncertainty/judge validation; scenario wording and o1 developer aggregation inconsistency; capability bottleneck hypothesis |
| Standalone-versus-agent comparator | No matched standalone comparator |
| Source locators | wasp_c01–16; pp.3–10,18,21–22 |

## Defenses and containment

Compare enforcement boundaries, assumptions and utility under each protocol; conditional guarantees are not unconditional implementation security.

### [ACE](../records/ace_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | System containment defense; Trusted abstract plan, independent concrete matching, rule-based executor. Secondary source tags: None assigned |
| Inputs and attacker control | Untrusted app metadata/schema/outputs. Strong attacker owns app code, descriptions and schemas |
| Trust boundary and mechanism | App data to control flow and app-to-app information flow. Description manipulation, output disruption and manager hijack |
| Measured endpoint and conditions | INJECAGENT1054 no attacker calls; ASB3/2000 calls authors classify legitimate |
| Defense and utility | Lattice static IFC and isolated restricted workers |
| Major limitations | Benchmark utility often app invocation only; AppendixB denies formal runtime privacy soundness; escaped-worker/message risks; no universal guarantee |
| Standalone-versus-agent comparator | None; architecture/StruQ comparisons change models/protocols |
| Source locators | ace_c01, ace_c02, ace_c03, ace_c04, ace_c05, ace_c06, ace_c07, ace_c08, ace_c09, ace_c10, ace_c11, ace_c12, ace_c13, ace_c14, ace_c15, ace_c16, ace_c17, ace_c18; physical pp.1–18 |

### [BrowseSafe](../records/browsesafe_understanding_and_preventing_prompt_injection_within_ai_browser_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Injection detection; Fine-tuned HTML classifier. Secondary source tags: prompt-injection, web-agent |
| Inputs and attacker control | Constructed benign/malicious HTML. Synthetic page injection |
| Trust boundary and mechanism | Page text to detector label. Binary malicious-content detection |
| Measured endpoint and conditions | Test3680; Qwen30BA3B F1.904/P.978/R.841 |
| Defense and utility | Page classifier |
| Major limitations | No end-to-end acting-agent utility or adaptive security evaluation; filename says preventing, PDF title says detecting |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | bs_claim_01 through bs_claim_16; physical source pages in claim locators |

### [CaMeL](../records/defeating_prompt_injections_by_design_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Control/data separation; Trusted planner; untrusted parser; restricted Python and provenance policies. Secondary source tags: prompt-injection |
| Inputs and attacker control | Typed tool data. Tool-output injection; conditional policy scope |
| Trust boundary and mechanism | Untrusted data cannot freely steer trusted control. Capabilities and data-flow enforcement |
| Measured endpoint and conditions | Main o3 utility77.3 vs native84.5; model/policy attack counts vary |
| Defense and utility | Interpreter and policies |
| Major limitations | Formal property does not establish verified Python implementation;949-attack table has nonzero counts; cohort96/97 and token-stat discrepancies |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | C01 through C12; physical source pages in claim locators |

### [ceLLMate](../records/cellmate_sandboxing_browser_ai_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Browser-side authorization sandbox; Agent-agnostic trusted Chrome extension; HTTP mediation and semantic sitemap. Secondary source tags: defense, web-agent |
| Inputs and attacker control | Untrusted webpage content; HTTP requests/parameters; trusted task/policy input. Fully compromised agent emulated with12 browser scripts; normal hostile-content attacker described |
| Trust boundary and mechanism | Agent UI actions → HTTP semantic action → allow/deny/runtime policy. Attempt disallowed GitLab exfiltration/destruction/access goals |
| Measured endpoint and conditions | All12 scripted forbidden goals blocked under policies for two user tasks; not live injection ASR.219 policy tasks; retail joint argument27/32,26/32,31/32 versus selection144/149,145/149,148/149 |
| Defense and utility | Deterministic HTTP enforcement, trusted sitemaps, selected policies/user consent, runtime constraints/counters |
| Major limitations | Permitted-action misuse excluded; single-turn; trusted browser/agent confinement; maintained complete sitemaps; WebSockets/freshness limits;132vs136 domain count and latency discrepancy |
| Standalone-versus-agent comparator | No matched standalone comparator |
| Source locators | cellmate_c01–15; pp.2–13 |

### [Don’t Click That / DUDE](../records/dont_click_that_teaching_web_agents_to_resist_deceptive_interfaces_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Defenses and containment; Static screenshot grounding plus evaluator/reflection; stage1 training separately ablated. Secondary source tags: web-agent |
| Inputs and attacker control | Visible webpage interfaces: deceptive pop-ups, fake download or continuation buttons, misleading visual hierarchy, preselected subscription controls, overlays, urgency cues, and commercial prompts misaligned with the user's task. Purely backend exploits without visible manifestations are outside the defense's stated scope. |
| Trust boundary and mechanism | DUDE evaluates screenshot, task, and candidate click using a ternary label and confidence; Stage 1 uses asymmetric hybrid-reward learning, Stage 2 summarizes persistent failures with successful anchors into contextual guidance, and inference gates execution with rejection/rethinking. RUC supplies 1,407 annotated examples; general reported evaluation uses 200 tasks across four domains, with Stage-1 training assessed separately through ablation. |
| Measured endpoint and conditions | Qwen SR6.5→33.5/DFR2→0; UI-TARS SR43.5→35.5 with evaluator |
| Defense and utility | Evaluator gating/reflection; stage2 prompt experiments differ from stage1 training ablation. Static trap clicks are not completed harm;1407 examples and200/210 test-size conflict. |
| Major limitations | Trap click is not completed harm;200/210 test sizes and3-step versus larger counts conflict; stage gains not uniform; unexplained53.8% headline; no own matched standalone comparison; no otherwise matched standalone adversarial test |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | claim_01 through claim_14; physical pages in locators |

### [Firewalls All You Need?](../records/indirect_prompt_injections_are_firewalls_all_you_need_or_stronger_benchmarks_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Prompt-injection defenses and benchmark repair; Tool-input Minimizer and tool-output Sanitizer. Secondary source tags: benchmark, prompt-injection |
| Inputs and attacker control | Tool results. Fixed tool-output attacks |
| Trust boundary and mechanism | External tool text to agent instructions/actions. LLM filtering and task-relevance restriction |
| Measured endpoint and conditions | Separate clean BU, attacked UA and ASR; several nonzero residual rates |
| Defense and utility | Sanitizer and combined firewall |
| Major limitations | Utility costs vary; benchmark/scorer fixes confounded; claimed zero ASR not universal; no adaptive guarantee |
| Standalone-versus-agent comparator | None |
| Source locators | C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16 |

### [FocusAgent](../records/focusagent_simple_yet_effective_ways_of_trimming_the_large_context_of_web_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Context pruning and browser injection; Retriever-pruned AXTree plus warning. Secondary source tags: web-agent |
| Inputs and attacker control | Page accessibility trees/pop-ups. Controlled benchmark injection |
| Trust boundary and mechanism | Retrieved text enters acting-model context. Observation selection and safety prompt |
| Measured endpoint and conditions | Popup ASR90.4/81.6 to1/0.9; task success remains2/1.8 |
| Defense and utility | Pruning and warning bundled |
| Major limitations | Low ASR does not restore blocked tasks; warning-only can have better utility; retention/cost subsets differ |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | focusagent_c01 through focusagent_c15; physical source pages in claim locators |

### [IsolateGPT](../records/isolategpt_an_execution_isolation_architecture_for_llm_based_agentic_systems_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Cross-app execution containment; GPT-4 hub/spokes; isolated process/app context and memory. Secondary source tags: defense |
| Inputs and attacker control | App descriptions, emails/websites, app/system data, API outputs. Install malicious apps or expose benign apps to malicious content; host/operator trusted |
| Trust boundary and mechanism | Per-app context/process → deterministic operator → mediated ISC routing/permission → other app or hub. Cross-app manipulation/exfiltration and context propagation; within-app compromise not prevented |
| Measured endpoint and conditions | 1598 scenarios:Vanilla20.2% ASR versus Isolate 7.6% permission appearances/100% warning rate conditional on appearances; these are different metrics |
| Defense and utility | Isolation, mediated messages, validated routing, permissions/user screening; case studies assume warned flows refused |
| Major limitations | User decisions condition protection; no human permission study; tested functionality parity not universal; cold-start/automatic-permission timing |
| Standalone-versus-agent comparator | Paired isolated/nonisolated GPT-4 agents, no tool-free standalone control |
| Source locators | claim_01_shared_execution_risk, claim_02_isolation_method, claim_03_attack_sample, claim_04_security_metrics, claim_05_user_screening, claim_06_permission_condition, claim_07_scope_limit, claim_08_functionality, claim_09_reported_overhead, claim_10_timing_conditions, claim_11_benchmark_limit, claim_14_implementation_controls; pp.2–10,13–14,17,19 |

### [MELON](../records/melon_provable_defense_against_indirect_prompt_injection_attacks_in_ai_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Behavioral pre-action defense; Masked re-execution and tool-call comparison. Secondary source tags: defense, prompt-injection |
| Inputs and attacker control | Retained tool observations with masked task/history. AgentDojo tool-result injections |
| Trust boundary and mechanism | Observation influence on proposed actions. Compare original call with masked proposed calls |
| Measured endpoint and conditions | GPT4o BU68.04/UA58.78/ASR.24; augmented76.29/68.72/.32 |
| Defense and utility | MELON and augmented variant |
| Major limitations | 629 attacks; UA joint success/security; conditional independent ensemble bound differs from deployed single mask;66diagnostic vs22one-pass successes unresolved; masked calls not executed harm |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | C01 through C16; physical source pages in claim locators |

### [PlanGuard](../records/planguard_defending_agents_against_indirect_prompt_injection_via_planning_based_consistency_verification_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Planning consistency defense; Isolated trusted-input planner plus executing agent and semantic verifier. Secondary source tags: defense, prompt-injection |
| Inputs and attacker control | External tool responses; agent reasoning/arguments entering verification. InjecAgent tool-output injection; DeepSeek-V3.2 victim instructed to obey tool commands |
| Trust boundary and mechanism | Trusted user/tool definitions → reference plan versus untrusted agent execution. Unauthorized direct harm / data stealing tool calls |
| Measured endpoint and conditions | 1,054 attack cases; vanilla DH56.90/DS88.67% ASR versus observed0% Stage-I/full; FPR27/38.01% hard matching versus0.97/3.28% full |
| Defense and utility | Exact call pass; absent tool block; semantic checking of allowed-tool argument mismatch |
| Major limitations | Benign denominator/repetitions unclear; FPR not task utility; abstract aggregate1.49% FPR unreconstructed; adaptive attacks theoretical; argument ground truth absent; no quantified latency |
| Standalone-versus-agent comparator | No matched standalone security comparator |
| Source locators | PG_C01–17; pp.1–6 |

### [Prismata](../records/prismata_confining_cross_site_prompt_injection_in_web_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Cross-site prompt-injection confinement; Query-only origin policy; structural-provenance labels; top-down Biba masking and pre-action gate. Secondary source tags: prompt-injection, web-agent |
| Inputs and attacker control | BrowserGym HTML and element paths. Attacker text in user/hosted/external nodes; no DOM scripting/XSS |
| Trust boundary and mechanism | Untrusted page nodes versus trusted policy/labels and authorized actions. Redacted observations and identifier-action mediation |
| Measured endpoint and conditions | Three-template meanASR85.5 to0.7%; attackedTSR4.5 to23%; benign29.9 to26.6 |
| Defense and utility | Prismata policies and gates |
| Major limitations | Informal argument assumes trustworthy structural cues; path counts not risk probabilities; same-origin GET assumption; 21-goal WASP tiny cohorts; async component durations not wall time |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | C1 through C13; physical pp.3–10,15 |

### [RecurGuard](../records/recurguard_runtime_monitoring_for_reasoning_token_consumption_attacks_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Resource exhaustion defense; Reasoning trace monitor and final-output QDM. Secondary source tags: defense, resource-exhaustion |
| Inputs and attacker control | Text-bearing context. Black-box context injection; no detector gradients |
| Trust boundary and mechanism | External decoy to reasoning-token expenditure. Puzzle/encoded-query and adaptive filler |
| Measured endpoint and conditions | OT99/100 and EA46/50 detected; adaptive C1 joint miss~50% at11.9x |
| Defense and utility | Recurrence/volume/task-progress sustained alarm; early stop requires traces+cancellation |
| Major limitations | Clean long-form profiles partly calibration;0/150 held-out QA FPs not zero population FPR; C4evades at2.2x; hidden-trace RG inapplicable |
| Standalone-versus-agent comparator | None; end-to-end RAG future work |
| Source locators | C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14; physical pp.1–14 |

### [ReNNervate](../records/rennervate_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Internal-attention detector; Frozen white-box LLM plus trained attention CNN. Secondary source tags: defense, prompt-injection |
| Inputs and attacker control | Instruction plus injected data. Task data; unseen/adaptive attack variants |
| Trust boundary and mechanism | Internal attention signals to attack classification/optional pruning. Response-to-input attention patterns |
| Measured endpoint and conditions | FIPI accuracy97.88–99.58%; unseen residual ASR up to23.9%; adaptive PAIR19% |
| Defense and utility | Detector and token deletion |
| Major limitations | Generation attention required; no pre-action containment proof; some cross-task utility collapse; Algorithm1 trailing-run handling unclear |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | rennervate_c01 through rennervate_c16; physical source pages in claim locators |

### [SecAlign](../records/secalign_defending_against_prompt_injection_with_preference_optimization_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Model hardening; Structured instruction/data decoder; DPO LoRA. Secondary source tags: defense, prompt-injection |
| Inputs and attacker control | Attacker-controlled data field. White-box optimized data injection |
| Trust boundary and mechanism | Trusted instruction versus data. Preference optimization for ignoring injected data |
| Measured endpoint and conditions | 208 security cases; main Instruct ASR89 to1 /97 to8 |
| Defense and utility | SecAlign training |
| Major limitations | Base Llama residual14%; utility benchmarks include losses; output marker not harmful action; compared models/protocols differ |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | C01 through C13; physical source pages in claim locators |

### [SnapGuard](../records/snapguard_lightweight_prompt_injection_detection_for_screenshot_based_web_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Defenses and containment; Screenshot detector; local variance plus OCR/rules. Secondary source tags: defense, multimodal, prompt-injection, web-agent |
| Inputs and attacker control | Attacker-controlled webpage renderings, third-party or user-generated images, product images, interface layouts, visually concealed instructions, and pixel-level perturbations. The threat model includes malicious content providers and website owners, with iterative refinement using surrogate or publicly available agents. |
| Trust boundary and mechanism | External screenshot-only pre-action detection using variance of grayscale gradient magnitudes, a benign-calibrated VSI threshold, selective inversion of pixels above grayscale intensity 240, OCR candidate union from original and transformed images, and action-oriented pattern categories. Main implementation uses Pytesseract and CPU processing. Exact branch-fusion logic and full pattern rules are unavailable in the supplied pages. |
| Measured endpoint and conditions | 948 benign/2185 malicious images; macro FPR .09, mean TPR .66, F1 .75; CPU1.81s |
| Defense and utility | Pre-action screenshot detector; variance/OCR/rules on CPU. No live-agent utility or completed-action prevention trial. |
| Major limitations | Not a live-agent action/utility test; target .05 FPR differs from observed configuration rates; missing appendices; template venue metadata |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | snapguard_c01–c13; pp.1–10 |

### [Spotlighting](../records/defending_against_indirect_prompt_injection_attacks_with_spotlighting_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Input-provenance defense; Document summarization/Q&A LLM application; Text003 and June2023 GPT-3.5/GPT-4. Secondary source tags: defense, prompt-injection |
| Inputs and attacker control | Untrusted external document text. Synthetic instruction-bearing documents; system-prompt knowledge considered; proposed adaptive variants not quantitatively evaluated |
| Trust boundary and mechanism | External data versus legitimate instructions within shared model channel. Keyword-only task takeover |
| Measured endpoint and conditions | 1000 synthetic documents. Datamarking GPT-3.5 summary3.10%/Q&A8%; GPT-4 Q&A1%; encoding GPT-3.5 summary0%/Q&A1.8% |
| Defense and utility | Delimiters, interleaved markers, encoding plus instructions; encoding harms GPT-3.5 utility; model/task-specific conditions |
| Major limitations | Narrow endpoint; absent exact repeats/splits/uncertainty; delimiter imitation/whitespace-free attacks; below3% prose conflict; proposed dynamic marking lacks adaptive rate |
| Standalone-versus-agent comparator | NLP application evidence, no matched browser-agent/standalone comparison |
| Source locators | spotlighting_c01–15; pp.1–13 |

### [StruQ](../records/struq_defending_against_prompt_injection_with_structured_queries_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Structured-query prompt injection defense; Filter reserved delimiter tokens; distinguish trusted instructions from untrusted data; structured instruction tuning. Secondary source tags: defense, prompt-injection |
| Inputs and attacker control | Arbitrary attacker-controlled data field. Known format and chosen data; trusted prompt immutable; optimized attacks have distinct budgets |
| Trust boundary and mechanism | Data → instruction interpretation. Completion spoofing, manual injection, TAP and white-box GCG |
| Measured endpoint and conditions | 208 AlpacaFarm examples/attack; Llama TAP97→9%, GCG97→58%; Mistral100→36%,99→56%; exact target strings |
| Defense and utility | 805 AlpacaEval comparisons: Llama67.2→67.6%, Mistral80→78.7%; win rate not web-task utility |
| Major limitations | Residual optimized attacks; manual threshold and utility-table discrepancies; BIPIA backbones differ; GPU-limited GCG not a passed test |
| Standalone-versus-agent comparator | Standalone structured-query study; no matched standalone/web-agent control |
| Source locators | struq_c01–16; pp.1–2,8–14 |

### [Task Shield](../records/the_task_shield_enforcing_task_alignment_to_defend_against_indirect_prompt_injection_in_llm_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Task-alignment defense; GPT-family tool-calling assistant plus LLM instruction extractor/checker. Secondary source tags: defense, prompt-injection |
| Inputs and attacker control | External documents, webpages and tool outputs. Inject external-content directives during legitimate tasks; extraction/scoring can be adversarially probed |
| Trust boundary and mechanism | Trusted user goals versus external directives; assistant plans and calls checked before execution. Redirect agent objectives through apparently relevant or high-priority instructions |
| Measured endpoint and conditions | AgentDojo four suites, one trial/task; exact case denominators not supplied. GPT-4o Important Instructions: ASR 47.69→2.07%, attacked utility 50.08→69.79%, clean utility 73.20%; mini ASR 2.23%, attacked utility 54.53% |
| Defense and utility | Extract instructions; sum contribution scores to user-task set; flag zero contribution; original tool output plus feedback; prevent misaligned calls. Slack mini Input Shield/full: utility 63.80/50.48%, ASR 4.76/0.95%, median latency 18.78/62.56 s |
| Major limitations | Semantic checker can fail; synthetic single-benchmark/GPT-family scope; no measured adaptive campaign or security uncertainty; Table 2/4 Slack utility and restatement prose/Table 3 conflicts; significant latency |
| Standalone-versus-agent comparator | No matched standalone-LLM control; defense versus tool-agent baselines only |
| Source locators | claim_01–12; pp.1–9,13–15; Figures 1–7 and Tables 1–7 represented in narrative |

### [Untrusted Content Masking](../records/untrusted_content_masking_for_web_agents_with_security_guarantees_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Defenses and containment; Owner-labeled DOM masking; isolated typed-answer queries. Secondary source tags: defense, web-agent |
| Inputs and attacker control | Attacker-controlled text and images inside untrusted regions of honest websites, including comments, reviews, issue descriptions, names, and externally sourced content. Correct masking removes direct agent exposure, but the remaining Q-Model channel can carry false well-typed data. Mislabeling exposes the original prompt-injection channel. Active-content escape, browser/OS compromise, and malicious site owners are outside the stated protection model. |
| Trust boundary and mechanism | Client-side DOM masking replaces labeled untrusted content with unique placeholders before agent observation. A separate Q-Model answers targeted questions through parser-validated bool, bounded int, bounded float, enum, or date outputs. Human-reviewed strings provide a distinct fallback. Evaluation covers 100 custom tasks, 41 GitLab templates, twelve strengthened WASP goals, data-flow red teaming, and sanitized-DOM selector inference on three sites. |
| Measured endpoint and conditions | 12 strengthened WASP goals: UCM0 ASR versus17±8 baseline; main utility uses three different models/100 tasks |
| Defense and utility | DOM placeholders and isolated typed Q-Model. Guarantee assumes correct labels/trusted browser. Main utility100 tasks/three models differs from12-goal WASP security setup; four hard templates use human-approved free text. |
| Major limitations | Guarantee assumes correct complete labels; four hard templates use human-approved free text; potential query overrides are simulated; no matched standalone comparator |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | C01–C12; pp.1–25 |

### [WARD](../records/ward_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Multimodal guard/defense; Parallel guard for browser/computer-use agents. Secondary source tags: defense, prompt-injection, web-agent |
| Inputs and attacker control | Screenshots/HTML and guard-targeted injected prompts. Environmental and adaptive guard-targeting attacks under listed protocols |
| Trust boundary and mechanism | Observation → guard verdict → agent exposure. Visual/text prompt injection and fake guard-output attacks |
| Measured endpoint and conditions | Adaptive budget ten: sample success 5.62%/3.12%; attempt success 0.62%/0.34%. These are different denominators |
| Defense and utility | Guard SFT, guard-targeted training and adaptive training; OOD and utility tests |
| Major limitations | Dataset-specific recall; pixel attacks and task-aligned fabricated content remain limits; shared generator dependencies |
| Standalone-versus-agent comparator | No matched standalone security comparator |
| Source locators | ward_c02/c04–c09/c11–c15; pp.3,6–9,16–18,20–22 |

### [WebAgentGuard](../records/webagentguard_a_reasoning_driven_guard_model_for_detecting_prompt_injection_attacks_in_web_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Defenses and containment; Parallel reasoning guard on HTML/screenshot/goal. Secondary source tags: defense, prompt-injection, web-agent |
| Inputs and attacker control | Attacker-modified webpage HTML whose instructions are perceivable through processed text, rendered screenshots, or both; recreated pop-ups and supplied VPI-Bench/EIA attacks; one guard-directed instruction inserted at the head or tail of malicious HTML. The formulation includes harmful action examples such as API-key leakage, and qualitative cases include file manipulation and coordinate-click commands. |
| Trust boundary and mechanism | A dedicated multimodal guard runs in parallel with agent action generation, receiving user intent, processed HTML, and screenshot according to the explicit input descriptions. A gateway executes actions when approved by the guard or explicitly authorized by a human. Qwen3-VL 4B/8B backbones are trained on GPT-5-generated synthetic data using explanation-augmented supervised fine-tuning followed by GRPO with a binary format-and-correctness reward. |
| Measured endpoint and conditions | Integrated attack rates fall in reported settings; 8B in-domain recall98.4%; mean guard3.24s |
| Defense and utility | Parallel Qwen3-VL guard/action gateway with distinct human override. Synthetic evaluation1000 balanced examples; external positive-only sets give recall; utility losses remain. |
| Major limitations | Mean latency below agent mean does not prove zero paired wall-time overhead; positive-only benchmarks give recall, not full accuracy; utility losses remain; fixed-suffix test is not adaptive robustness |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | C01–C14; pp.1–18 |

## Surveys and security background

Surveys report secondary evidence. Hybrid original case studies are labeled by their methods; literature counts are not risk estimates.

### [AI Agent Traps](../records/ai_agent_traps_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Conceptual taxonomy; Six overlapping functional targets. Secondary source tags: None assigned |
| Inputs and attacker control | Web/resources/media/memory/collective signals. Environment and architecture-dependent capabilities |
| Trust boundary and mechanism | Perception through action and human approval. Content, semantic, cognitive, behavioral, systemic and human traps |
| Measured endpoint and conditions | No original experiments; cited rates remain secondary |
| Defense and utility | Proposed training/runtime/ecosystem interventions untested |
| Major limitations | Eighteen table subtypes are not eighteen validated attacks; systemic and human mechanisms preliminary |
| Standalone-versus-agent comparator | None |
| Source locators | C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14; physical pp.1–16 |

### [Autonomy-Induced Security Risks](../records/a_survey_on_autonomy_induced_security_risks_in_large_model_based_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Survey / secondary synthesis; Survey; autonomy taxonomy and proposed R2A2 controls. Secondary source tags: survey-taxonomy |
| Inputs and attacker control | User instructions; untrusted web and environmental content; multimodal perception; reasoning and planning; persistent memory and retrieved knowledge; privileged tools and browser APIs; irreversible action interfaces; inter-agent messages and shared stores; live private-data retrieval and transmission. Exposure and impact depend on permissions, persistence, oversight, and validation. |
| Trust boundary and mechanism | Narrative/conceptual security survey using a five-level autonomy taxonomy, qualitative comparisons across three system classes, seven architectural risk loci, eight attack-surface categories, capability-specific CMDP models, a layered defense synthesis, and the proposed R2A2 architecture. No reproducible search protocol or original experimental evaluation is reported. |
| Measured endpoint and conditions | No original attack/utility experiment; expected CMDP constraint is conditional |
| Defense and utility | Proposed R2A2/layered controls not jointly implemented/tested. Expected CMDP cost budget is not zero individual unsafe action. |
| Major limitations | Autonomy levels differ from defense levels; expected cost budget does not guarantee zero unsafe actions; proposed combined stack untested; no matched standalone experiment |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | C01–C15; pp.1–20 |

### [Hidden Dangers of Browsing AI Agents](../records/the_hidden_dangers_of_browsing_ai_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Hybrid threat model and implementation case study; MAESTRO mapping plus BrowserUse authorization and credential-leak cases. Secondary source tags: None assigned |
| Inputs and attacker control | Author-described surfaces include webpage HTML/DOM and screenshots, prompt construction, reasoning/planning loops, tool arguments and registries, sensitive-data replacement, URL allowlists, browser sessions, containers, remote debugging, telemetry, credential stores, shared memory, and multi-agent delegation. Only domain validation and prompt-driven credential exfiltration receive detailed Browser Use case treatment. |
| Trust boundary and mechanism | Mixed security systems analysis: benchmark-informed selection of Browser Use; literature- and demonstration-informed architecture reconstruction; seven-layer MAESTRO mapping; narrative defense synthesis; white-box URL-validation analysis for version 0.1.44; and a GPT-4o-based credential-exfiltration proof-of-concept setup. No systematic review protocol or repeated-trial security benchmark is supplied. |
| Measured endpoint and conditions | Author reports URL-check CVE2025-47241 in.1.44 fixed.1.45; no repeated-trial ASR |
| Defense and utility | Mostly secondary mitigations; URL bug and credential scenario are distinct. Historical0.1.44/0.1.45 claims; no repeated-trial combined-chain ASR or delivery denominator; PoC not executed here. |
| Major limitations | Historical fix status not checked live; URL bypass and prompt injection are distinct components; sample PoC does not measure combined-chain reliability; cited capability/defense rates are secondary; no matched standalone test |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | C01 through C14; physical pages in locators |

### [Layered Attack Surface Model](../records/a_systematic_survey_of_security_threats_and_defenses_in_llm_based_ai_agents_a_layered_attack_surface_framework_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Survey / secondary synthesis; Seven layers by four temporal classes; literature/defense mapping. Secondary source tags: defense, survey-taxonomy |
| Inputs and attacker control | Seven author-defined analytical layers: foundation, cognition, memory, tool execution, coordination, ecosystem, and governance. Web-specific exposure includes page-mediated indirect prompt injection, adversarial pixels, file and API returns, tool permissions, persistent writes, and MCP/tool-description initialization. Temporalities distinguish immediate, within-session, cross-session memory, and drift/dormant-trigger effects. |
| Trust boundary and mechanism | PRISMA-inspired systematic survey of 116 retained papers from 1,634 records across four databases and two search phases, with single-author layer/time coding into 144 reported assignments; conceptual architecture, conditional theorem sketch, defense/benchmark mapping, five-case taxonomy comparison, and four reported robustness protocols. |
| Measured endpoint and conditions | 116 papers/144 reported assignments; selected zone9/144; seven zero-defense cells |
| Defense and utility | Coded literature coverage is not measured protection. The theorem requires unchanged other-layer observation distributions; supplements absent. |
| Major limitations | Assignments not incident risk; multiplicities imply146; table/figure defense counts conflict; theorem assumes unchanged other-layer distributions and gives no incremental discrimination, not zero absolute alerts; supplements absent |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | claim_01_architecture–claim_14_multiplicity; pp.1–58 |

### [SoK Attack and Defense Landscape](../records/sok_attack_and_defense_landscape_of_agentic_ai_systems_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Survey / secondary synthesis; 128-paper review; seven continuous design dimensions; three adversary classes/six vectors. Secondary source tags: defense, survey-taxonomy |
| Inputs and attacker control | AUTHOR-REPORTED: external pages and documents, third-party tool names/descriptions/implementations, direct user inputs, model components, memory and RAG stores, user interfaces, tool credentials, and external resources. Attack vectors V1–V6 are distinct from risks R1–R7. |
| Trust boundary and mechanism | Literature-based cybersecurity systematization of knowledge. The authors report a 2023–October 2025 review, four keyword dimensions, venue/source prioritization, manual exclusion of standalone-model work, and 128 papers including 51 attack methods and 60 defense methods. They synthesize design dimensions, threat models, interacting risks, defense mechanisms, and an Appendix A MITRE ATLAS crosswalk. |
| Measured endpoint and conditions | No new common-protocol attack/defense experiment |
| Defense and utility | Literature synthesis of defenses, not a combined-stack efficacy trial. Design dimensions are not calibrated risk scores. |
| Major limitations | Exposure and consequences are different; nine versus seven risks and three versus four defense categories conflict; cutoff versus late citation unresolved; no own matched standalone comparator |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | C01 through C14; physical source pages in locators |

### [Talk Is (Not) Cheap](../records/talk_is_not_cheap_a_taxonomy_and_benchmark_coverage_audit_for_llm_attacks_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Taxonomy and benchmark audit; LLM-assisted extraction/classification plus manual checks. Secondary source tags: benchmark, survey-taxonomy |
| Inputs and attacker control | 932English papers/benchmark descriptions. Secondary literature, not new victim trials |
| Trust boundary and mechanism | Evidence classification, not acting-agent boundary. Four targets by six technique classes |
| Measured endpoint and conditions | Six audited benchmarks union6/24 cells including partials;507leaves |
| Defense and utility | Proposed benchmark design, not implemented defense |
| Major limitations | 25% cells is not25% risk coverage; InjecAgent/AgentDojo overlap despite prose; multiple novelty denominators and author-added placeholders |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | claim_01 through claim_14; physical source pages in claim locators |

### [Toward Secure LLM Agents](../records/toward_secure_llm_agents_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Lifecycle security survey; Information flow, delegated authority and persistent state across agent classes. Secondary source tags: benchmark, defense, survey-taxonomy |
| Inputs and attacker control | Prompts, web/tool/retrieved content, files, memory, inter-agent channels. Varied prior-study assumptions; no original attack experiment |
| Trust boundary and mechanism | Input/planning/decision/tool/state/coordination transitions. Survey taxonomy: injection, tool hijacking, memory poisoning and propagation |
| Measured endpoint and conditions | 247normalizedpapers;209+42+24retrieval records minus24exclusions/4merges;3annotators/κ0.86; ASR usage129papers vs utility22/latency8/cost7, not outcomes |
| Defense and utility | Qualitative intervention/trust/utility synthesis; suggested stacks expressly unvalidated |
| Major limitations | Multi-label counts not risks/pooled efficacy; search/preprint bias; placeholder ACM DOI/date; Figure6 prose/matrix discrepancy; Figure5 denominator uncertain |
| Standalone-versus-agent comparator | Architectural argument, no matched standalone-agent experiment |
| Source locators | C01–15; pp.1,4–24,36–40 |

### [TrustAgent](../records/a_survey_on_trustworthy_llm_agents_threats_and_countermeasures_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Survey / secondary synthesis; Survey of intrinsic/extrinsic components and five trust dimensions. Secondary source tags: survey-taxonomy |
| Inputs and attacker control | AUTHOR-REPORTED: Brain inputs and reasoning; long-term memory poisoning and leakage; short-term dialogue misuse; tool planning, selection, execution, injection, and forged commands; tool-enabled attacks on external entities; cooperative and infectious inter-agent influence; dynamic physical/digital environments and user interactions. Availability of each surface depends on actual access and capabilities. |
| Trust boundary and mechanism | Qualitative taxonomy-driven survey organized by intrinsic/extrinsic components, attack/defense/evaluation techniques, and five core trustworthiness dimensions. Contains six conceptual figures, one survey-comparison table, and Appendix A definitions. No reported systematic search/screening protocol, original benchmark experiment, or pooled quantitative synthesis. |
| Measured endpoint and conditions | 119 references include duplicate/version entries; no new attack experiment |
| Defense and utility | Taxonomy of existing controls; no implemented guard or original efficacy trial. |
| Major limitations | Citation/benchmark attribution errors flagged; secondary metrics remain separate; architectural hierarchy is not measured security ordering; no own matched comparison |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | C01–C14; pp.1–11 |

## Web application testing and traditional crawling

Scanners attack ordinary applications; traditional crawlers study coverage/resource policy. Neither establishes agent compromise.

### [AWE](../records/awe_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Web application testing and traditional crawling; Context-specialized autonomous web-app pentester; memory reset per target. Secondary source tags: adaptive-attack, web-agent |
| Inputs and attacker control | AUTHOR-REPORTED — The attacked surface is the target web application's HTTP endpoints and attacker-controlled parameters, headers, cookies, request bodies, and dynamic client-side content. Included families are XSS, SQL injection, SSTI, command injection, file inclusion/path traversal, XXE, SSRF, and authenticated unauthorized object access. The security attack surface of AWE itself is not evaluated. |
| Trust boundary and mechanism | AUTHOR-REPORTED — Three-layer memory-augmented architecture with LLM orchestration, eight vulnerability-specific agents, reconnaissance, structured context/filter probing, constrained payload mutation, and browser-backed verification. Model selection uses DVWA; system comparison uses 104 XBOW challenges against published MAPTA results. Correct flag retrieval is required for a counted XBOW success. |
| Measured endpoint and conditions | 54/104 versus published MAPTA80/104; mean solve53.1s versus190.8s; XSS20/23 versus13/23 |
| Defense and utility | No evaluated defense of the agent. Flag retrieval required on104 XBOW tasks/ten-minute cap; memory reset between targets; published baseline differs in backbone. |
| Major limitations | Different backbones and published baseline prevent architecture attribution; $7.73/54≈.143 differs from reported.113; no own test of agents susceptibility to injection |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | AWE-C01 through AWE-C16; physical source pages in locators |

### [Crawl Policy](../records/the_impact_of_crawl_policy_on_web_search_effectiveness_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Traditional crawl policy; Priority/page-selection crawlers. Secondary source tags: information-seeking, web-agent |
| Inputs and attacker control | Web index and click evidence. No attacker tested |
| Trust boundary and mechanism | Inference: acquisition policy to available search evidence. Crawl selection policies |
| Measured endpoint and conditions | NDCG@10 URL-availability ceilings;1.5B vs421M crawl sizes |
| Defense and utility | No measured security defense |
| Major limitations | Historical conditional relevance ceiling, not actual LLM/retriever utility or causal cost ratio |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | crawl_policy_c01 through crawl_policy_c14; physical source pages in claim locators |

### [Crawler-trap detection](../records/detection_of_crawler_traps_formalization_and_implementation_defeating_protection_on_internet_and_on_the_tor_network_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Classical crawler environment deception/resource waste; Word-bigram distributions; entropy distances; proposed dynamic robust clustering. Secondary source tags: crawler-trap, scraping |
| Inputs and attacker control | Site-generated repeated/random pages. Site controls generated content; no LLM attacker tested |
| Trust boundary and mechanism | Page content → family classification → navigation/resource consumption. Infinite paths, changing identifiers, random content |
| Measured endpoint and conditions | 13families×500pages; t=3 Dottyback12.73%family overlap/0.57%merged-cluster overlap; distinct impact7.28% |
| Defense and utility | Proposed on-the-fly distance/clustering; operational tests deferred |
| Major limitations | Interval overlap is not classifier FNR or>99% live accuracy; small diverse families; normality/normalization assumptions unresolved |
| Standalone-versus-agent comparator | No LLM or matched standalone/web-agent comparison |
| Source locators | C01–14; pp.1–3,5–12 |

### [EvoCrawl](../records/evocrawl_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Web application testing and traditional crawling; Classical evolutionary web scanner with server DB feedback, manual users and fitness weights. Secondary source tags: information-seeking, web-agent |
| Inputs and attacker control | Author-studied surfaces are HTML inputs, JavaScript-triggered controls, hidden forms and links, stored/reflected XSS injection points, and directly requested resources with differing user privileges. Some reported findings require trusted administrator/editor privileges, and some are outside developer threat models. |
| Trust boundary and mechanism | A rapid Page Collection Module exchanges URLs with an Evolutionary Search Module. The latter searches element–interaction sequences using crossover, dependency-aware mutation, gene elimination, and weighted browser/database feedback. Modular XSS tracing and sitemap/replay/three-user IDOR analysis evaluate security consequences. Evaluation includes ten applications, 24-hour crawling, baseline comparisons, dependency ablation, selected known XSS, and new-finding reports. |
| Measured endpoint and conditions | Reported59% mean coverage increase; known XSS6/8 versus2/8;8 new reports have differing vendor/privilege status |
| Defense and utility | XSS/replay/IDOR mechanisms test applications, not agent prompt-injection resistance. Ten apps/24-hour runs; server database feedback/manual accounts require privileged setup. |
| Major limitations | Coverage is not application-line fraction; Drupal97151 versus61303 and Dokuwiki ablation−21 conflict with universal prose; privileged feedback; historical version/fix conflicts; no LLM comparator |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | evocrawl_c01 through evocrawl_c14; physical pages in locators |

### [IRLbot](../records/irlbot_scaling_to_6_billion_pagesand_beyond_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Conventional crawler availability/scalability; DRUM disk uniqueness; STAR domain budgets; BEAST deferred frontier. Secondary source tags: None assigned |
| Inputs and attacker control | Dynamic URLs/hostnames, link farms, server HTTP/DNS delays. Site operator can generate branches, hosts or intentional delays; no LLM attacker |
| Trust boundary and mechanism | Web branching/delays → repeated network work and persistent frontier resource load. Queue/DNS expansion, crawl traps and delay attacks described |
| Measured endpoint and conditions | Single server41.27active days in2007;6,380,051,942HTML200responses; average319Mb/s/1789pages/s;41.5billion discovered URL identifiers; extreme-scale rates analytical |
| Defense and utility | Reputation budgets, deferred queues, politeness and disk algorithms; no quantified adversarial ASR reduction |
| Major limitations | URL uniqueness not content deduplication; one integrated run; PLD ranking insufficient for all spam; fixed-memory asymptotic quadratic DRUM; distributed operation projected |
| Standalone-versus-agent comparator | No LLM or matched standalone comparison |
| Source locators | irlbot_c01–14; pp.1–4,10–31 |

### [Measuring What the Crawler Sees](../records/measuring_what_the_crawler_sees_discovery_curves_core_persistence_and_shell_dynamics_in_longitudinal_web_crawls_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Traditional longitudinal crawl model; Dynamic urn plus ideal persistent core and shell. Secondary source tags: scraping, web-agent |
| Inputs and attacker control | Common Crawl domains and academic URL snapshots. No attacker tested |
| Trust boundary and mechanism | Inference: fetch policy to observed population. Fit containment and discovery jointly |
| Measured endpoint and conditions | 51 CC crawls2020–25; approximate core.4; discrepant displayed fit triples |
| Defense and utility | No tested security defense |
| Major limitations | Internal fit consistency not external ground truth; normalization/curvature/inversion concerns; alpha is effective observed persistence, not true web survival |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | C01 through C13; physical source pages in claim locators |

### [Web Crawling](../records/web_crawling_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Traditional crawling survey; Frontier, fetching, deduplication and refresh policies. Secondary source tags: scraping, web-agent |
| Inputs and attacker control | URLs/web content/deep-web forms. Traditional traps/spam discussed |
| Trust boundary and mechanism | Inference: crawler eligibility and execution resources. Coverage/freshness and trap-management concepts |
| Measured endpoint and conditions | Historical secondary crawler throughput, not new controlled measurements |
| Defense and utility | Traditional politeness/budget controls discussed |
| Major limitations | 74physical pages; stationary sampling assumptions; no PI/agent-security evaluation; cited systems not matched experiments |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial security comparison reported. |
| Source locators | C01 through C16; physical source pages in claim locators |

### [YuraScanner](../records/yurascanner_comprehensive_summary.json)

| Comparison field | Source-grounded evidence and qualification |
|---|---|
| Study type and system | Web application testing and traditional crawling; LLM-generated DOM workflows plus conventional XSS detector; authenticated local apps. Secondary source tags: web-agent |
| Inputs and attacker control | AUTHOR-REPORTED: URLs, forms, input fields, JavaScript-driven interactions, authenticated administration interfaces, and workflow-dependent application states. ANALYST INFERENCE: Browser actuation and persistent application changes are relevant to studying agent risk, but hostile webpage control over the agent is not evaluated. |
| Trust boundary and mechanism | Goal-based crawler using semantic DOM abstractions, an LLM bridge with six-action history, concrete browser actuators, depth-one task discovery, CRUD-oriented ordering, separated form-filling prompts, and replay followed by Black Widow XSS testing. Evaluation includes ten-application manual task and coverage analysis and 20-application vulnerability testing, with four-hour tool runs. |
| Measured endpoint and conditions | 2361 generated/1818 valid/667 full/448 partial tasks;13 unique issues across scanners, Yura12/BW3/overlap2 |
| Defense and utility | Conventional Black Widow XSS oracle tests applications, not agent security. Four-hour runs; ten-app task audit/20-app vulnerability study; WordPress excluded from initial21. |
| Major limitations | 55.19% forms is baseline augmentation, not Yura total superiority; partial is not full completion; WordPress excluded; Moodle potential injection and vendor/privilege status qualified; no matched standalone security comparison |
| Standalone-versus-agent comparator | No otherwise matched standalone-LLM/web-agent adversarial comparison supplied. Capability, agent-defender and secondary literature comparisons do not establish one. |
| Source locators | yura_c01 through yura_c15; physical pp.1–16 |

