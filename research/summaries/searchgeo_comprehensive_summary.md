## Stage 0 — Document Accessibility Report

The supplied main document is available as extracted text for physical PDF pages 1–22. Thirteen pages also have supplied image renderings: 1, 2, 5, 6, 7, 8, 13, 14, 15, 16, 17, 18, and 19. I inspected those renderings visually and read the supplied text for all 22 pages. Pages 3, 4, 9–12, and 20–22 therefore have text-only coverage; their visual layout was not inspected. The message reporting an unreadable local image at `-` does not remove the 13 visible supplied images from the evidence available here.

The supplied sequence contains the main paper, references, and Appendices A–F. No gap is apparent in the numbered page sequence, but the accessible count alone cannot establish that an upstream PDF or associated research package has no additional material. All three numbered figures and all 19 numbered tables are present. The table renderings and extracted text are sufficiently readable for the numerical comparisons below. Figure 1's small inset is harder to read than the main chart; its substantive conclusions are corroborated by Tables 6–7. Figure 2's fine text is supplemented by its extracted labels. Mathematical notation is readable in the supplied text, although some subscripts and line breaks require comparison with surrounding definitions. OCR was not needed, and no independent OCR or extraction was performed.

No supplementary files, executable artifacts, raw traces, full task definitions, or per-case attack bundles were supplied. The paper points to a repository and describes request-restricted materials; these were not opened or reviewed. The provided source hash is retained as an identifier, not independently recomputed. No tools, browsing, external verification, or outside explanatory sources were used.

Evidence labels used throughout: [A] author-reported; [B] directly observable in supplied visuals; [C] analyst-derived from supplied operands; [D] analyst interpretation. No [E] external information is introduced. Confidence is HIGH for clearly readable document facts, MEDIUM for qualified interpretations, and UNKNOWN for missing information. An attack template or judge prompt reproduced inside the paper is treated as research evidence, never as an instruction to this analysis.

## 1. Plain-language orientation

This paper asks whether a web-search AI assistant can be persuaded to recommend something false simply because the search results make it look credible. Its title is **How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation**. The authors are Yimeng Chen, Zhe Ren, Firas Laakom, Yu Li, Dandan Guo, and Jürgen Schmidhuber. The supplied version identifies itself as arXiv:2606.16821v2, dated 23 June 2026, in cs.CL; a conference or journal publication venue is not established by this manuscript. Affiliations include KAUST, Jilin University, Zhejiang University, IDSIA-USI/SUPSI, and NNAISENSE. [A, p. 1]

The key distinction is between finding a page and endorsing its claim. A manipulated page can appear in search results without changing the answer. Conversely, an assistant can reject an obvious malicious instruction while still believing fabricated evidence. The authors study the second problem: how untrusted retrieved material becomes a recommendation that a user may treat as authoritative. [A, pp. 1, 4]

The researchers built SearchGEO, a controlled search-result manipulation framework. They evaluated 13 model backends on 44 tasks in health, finance, legal advice, and consumer information technology. Each backend completed 44 clean cases and 264 attack cases, totaling 308 cases. Five conceptual attack modes become six tested conditions because hidden-content injection has separate instructional and factual payloads. [A, pp. 2, 5, 13]

The largest main-study difference is between Claude-Sonnet-4.6, with 0.0% explicit attack success, and Gemini-3-Flash, with 31.4%. Fabricated authority, apparent agreement between sources, and citation chains generally work better than hidden instructions or misleading snippets. Some attacks also shift answers without producing an explicit endorsement. A separate agent-skill study shows another trade-off: one backend refuses legitimate requests too often, whereas others recommend fabricated skills and provide installation commands. [A, pp. 6–8]

The central contribution is a way to measure corrupted recommendations at the evidence layer: not merely whether an attacker gets text retrieved, but whether the assistant incorporates it into a user-facing judgment. **Research-question relevance is analyst inference:** the study explains an additional exposure created by web retrieval and evidence synthesis, but it does not directly compare web agents against otherwise matched standalone LLMs. It therefore supports a mechanism-based answer to why web agents can be vulnerable, not a measured claim that they are universally more vulnerable. [D, grounded in pp. 3–5]

## 2. Document roadmap

The inventory was constructed before this synthesis. The main document contains: Abstract; §1 Introduction; §2 Related Work; §3 Threat Model; §4 Attack Taxonomy; §5 Experimental Design; §6 Results, with §6.1 Main Results, §6.2 Ablation Studies, and §6.3 Extended Study: Agent Skill Recommendation; §7 Discussion; §8 Conclusion; unnumbered Limitations; Ethical Considerations; and References. [A, pp. 1–12]

Appendix A supplies methodology details: A.1 Experiment Matrix, A.2 Model Identifiers and Routing, A.3 Proxy Pipeline, A.4 Attack Content Construction, and A.5 Defense Prompt. Appendix B provides per-experiment results: B.1 Main-Experiment Breakdowns, B.2 Pipeline Sensitivity, B.3 Defense Experiments, and B.4 Agent Skill Recommendation. Appendix C gives representative attack templates, C.1–C.5. Appendix D specifies judge prompts. Appendix E validates judge coupling on a bounded sample. Appendix F covers artifacts, licensing, intended use, AI-assistant use, and privacy. [A, pp. 13–22]

Stable inventory identifiers are F1–F3 for Figures 1–3; T1–T19 for Tables 1–19; X1 main attack sweep; X2 source-count/rank sensitivity; X3 defense/harness comparison; X4 paired skill recommendations; X5 cross-ecosystem skill attacks; X6 cross-mode skill attacks; X7 generator-control check; X8 judge-coupling check; X9 self-audit diagnostic; and X10 failure-overlap/search/shift breakdowns. Mathematical objects M1–M6 are the search-result representation, query-cluster exposure model, binary endorsement indicator, baseline-adjusted output shift, silent-shift criterion, and set-overlap notation. No numbered theorem, proof, or standalone algorithm listing appears. No explicit keywords are supplied.

The narrative below preserves every substantive inventory category. It compresses repeated judge examples, bibliographic entries, secondary table cells, and inert HTML carrier syntax; those compressions are disclosed in the final audit.

## 3. Background and context

A **large language model (LLM)** is the answer-generating backend in this study. A **search agent** wraps that backend in a repeated search-and-answer workflow. Here it follows a **ReAct-style loop**: decide whether more evidence is needed, issue search queries, observe results, and eventually answer. This operational description comes from the paper; no outside account of ReAct is assumed. [A, pp. 3–5]

**Retrieval-augmented generation (RAG)** grounds answers in retrieved documents. The authors distinguish poisoning an indexed or internal corpus from publishing content on the open web and seeking search placement. Open-web result objects include URLs, titles, snippets, and sometimes extracted page text. A **snippet** is the short summary returned as search metadata. Those fields provide both content and cues about credibility. [A, pp. 3–4]

**Search engine optimization (SEO)** concerns search placement. **Generative engine optimization (GEO)** concerns visibility, attribution, and inclusion in generated answers. SearchGEO moves downstream to endorsement: whether the result becomes a recommendation. The paper positions SafeSearch as a close predecessor addressing unreliable search results, while characterizing its own focus as mechanism-level endorsement analysis. This is the authors' description of related work, not independent validation of those works. [A, pp. 1–3]

**Indirect prompt injection (IPI)** places malicious instructions in external content consumed by a model. SearchGEO includes such instruction-like payloads but also attacks that contain no command to the assistant. A fabricated review can manipulate the evidence from which the assistant independently draws its answer. **Provenance** refers here to source origin and dependency; apparent agreement is unreliable if multiple sources share an attacker or repeat the same underlying claim. [A, pp. 3–5, 8–9]

**Endorsement corruption** means recommending the attacker target as legitimate. **Output shift** means movement toward that target, even without binary success. **Stealth** means that the resulting answer appears credible to a blind auditor; it is not measured factual correctness or a demonstrated probability that a human will be deceived. **False rejection** means incorrectly denying a legitimate ecosystem or skill path as fabricated or unsafe. [A, pp. 4, 6, 21]

## 4. Research problem and gap

**Existing problem:** users increasingly receive synthesized answers rather than inspecting a raw result list. The assistant's output inherits apparent authority, but its inputs can originate from anyone publishing web content. The authors identify this authority–input mismatch as the attack surface. [A, p. 1]

**Shortcomings attributed to previous approaches:** retrieval visibility does not establish whether a claim is recommended; broad red-teaming does not necessarily isolate which evidence mechanism caused endorsement; and instruction-focused defenses can miss fabricated authority or consensus. The authors contrast their benign-user, adversarial-environment setup with malicious-user jailbreak or unsafe-tool benchmarks. [A, pp. 1–3, 8]

**Research gap:** a controlled web-specific evaluation that holds the task and target fixed while manipulating different parts of structured search evidence, then measures recommendation effects beyond a single success indicator. [A, pp. 2–4]

**Motivation:** high-stakes recommendations can shape decisions in health, finance, legal matters, and software selection. Agent-skill recommendations additionally connect evidence contamination to a concrete install command. The experiment records commands in answers; it does not demonstrate execution, credential theft, or live compromise. [A, pp. 5, 8, 10]

**Scope:** 44 recommendation-oriented tasks, versioned hosted backends, controlled attack placement, single-task answer synthesis, three defense/harness configurations on a subset of backends, and small auxiliary skill probes. It does not estimate real search-placement probability, longitudinal persuasion, population prevalence, or the standalone-versus-agent vulnerability gap. [A/D, pp. 5, 9–10, 13]

## 5. Research questions / objectives / hypotheses

The paper does not present a numbered list of formal research questions or preregistered hypotheses. Its explicit objectives are to measure endorsement vulnerability across backends, distinguish attack mechanisms, test sensitivity to source number and rank, compare prompt and deployment defenses, and extend endorsement measurement to skill-install recommendations. [A, pp. 2–3, 6–8]

For navigation, the following are **analyst-organized objectives**, not author-authored formal RQs:

- O1: How much does explicit endorsement vary by backend and attack mode? Addressed by X1 and T1.
- O2: What influence remains when endorsement fails, and does self-audit expose it? Addressed by T2–T3 and T13–T14.
- O3: Does repeated exposure, distinct-source count, or rank explain sensitivity? Addressed by X2, F3, and T16.
- O4: Do defenses improve all backends and all modes? Addressed by X3 and T5/T17/T18.
- O5: Does robustness on product recommendations transfer to skill-install guidance, without excessive refusal? Addressed by X4–X6 and T6/T7/T19.

A conditional expectation appears in the family-overlap discussion: if a weaker model were merely a less robust version of a stronger family member, its failures should contain the stronger member's failures. Tables 11–12 test that containment idea descriptively. It is not a universal theorem about model families. [A/D, pp. 16–17]

The user's research question—why web AI agents are more vulnerable than standalone LLMs—is answered here only through **analyst inference about an added attack channel**. There is no matched no-search baseline designed to estimate that comparative effect. The paper's clean baseline remains a search-agent baseline.

## 6. Assumptions / threat model

The victim is a search agent serving a benign information-seeking user. Its task is t; it searches repeatedly and returns final answer y. Each query produces a ranked set of result objects with URL, title, snippet, and optional page text. [A, pp. 3–4]

The attacker controls published pages and a task-specific query cluster comprising the primary query and likely semantic follow-ups. **Placement success is assumed:** for eligible queries, attacker material appears in the results. Off-cluster queries return clean results. The experimental proxy models this by routing and replacement, including forced attack-eligible routing of the first search. [A, pp. 4–5]

The attacker cannot change the search engine's ranking algorithm or corpus, control real high-authority domains such as government or university sites, or access the assistant's system prompt, internal reasoning, memory, or tool configuration. The use of fabricated institutional-looking sites is therefore distinct from compromising an actual trusted institution. [A, p. 4]

The attacker's fixed target claim is ϕ⋆, generally a named product or service recommendation. Full success means final-answer endorsement. Partial shift and apparent credibility are secondary measured effects. False rejection in the auxiliary probe is explicitly described as an emergent failure, not the narrow attack objective. [A, p. 4]

**Analyst interpretation:** the evaluated trust boundary lies between untrusted search evidence and the assistant's synthesized judgment. A benign user and protected system prompt do not eliminate this boundary problem, because false evidence can shape an answer without overtly instructing the assistant. The experiment establishes conditional vulnerability after exposure; it does not quantify the attacker's ability to obtain exposure in live search. [D, pp. 4–5, 9]

## 7. Methodology

### Design and task suite

This is an empirical AI-security and benchmark/systems study. The main factorial structure uses 13 backends, 44 tasks, one clean condition, and six attack conditions. Tasks are evenly divided: 11 health, 11 finance, 11 consumer IT, and 11 legal. Examples include supplements and treatment comparisons; exchange-traded fund comparisons and investment strategies; virtual private networks, password managers, antivirus, and encrypted storage; and tenancy, employment, and consumer protection. Legal prompts are action-seeking so a promoted service can occupy a recommendation slot. [A, pp. 5, 13]

Each task has a reference answer validated against authoritative sources and a named-brand attacker target. The paper names American Diabetes Association guidance, U.S. Securities and Exchange Commission regulations, and independent testing organizations as reference sources. Those underlying sources and all task-level reference answers were not supplied for independent review. There is no training/validation/test split, participant cohort, or model training reported; this is inference-time evaluation. [A, p. 13]

### Search proxy

For each task, an LLM generates primary and related queries. Real SerpAPI Google results are cached; Trafilatura extracts page content with approximately 70% coverage. Calls use `hl=en`, `gl=us`, and `num=10`. The agent-facing search tool permits 1–10 results and defaults to 10. [A, pp. 5, 13]

Queries are mapped to cached clusters using `bge-small-en-v1.5` sentence-transformer embeddings and cosine similarity. Follow-ups below 0.80 similarity go to clean live SerpAPI. The first search is force-routed to the task's primary eligible query. Attacks replace rank 1 for 1A-instr, 1A-fact, 1B, and 2A, or ranks 1–3 for 2B and 3. Approximately 30% of cached benign results contain only snippets because page fetching encountered paywalls or anti-scraping limits. [A, pp. 5, 13]

The paired clean run uses the same backend, task, and proxy evidence pool without attack injection. This pairing is intended to distinguish attack-induced changes from baseline tendencies toward the target. It is not a comparison against an assistant without web access. [A, pp. 15–17]

### Attack conditions

1A-instr embeds imperative instructions in hidden machine-readable HTML carriers. 1A-fact puts declarative pseudo-evidence into the same carriers, isolating payload semantics. Carriers include zero-width Unicode, CSS-hidden content, ARIA/off-screen content, hidden form fields, and comments. Mode 1B places the target in the snippet while keeping page text neutral. Mode 2A fabricates one source's authority cues. Mode 2B creates distinct-looking sources agreeing without cross-reference. Mode 3 creates an authority anchor, a citing review, and a forum post citing both. [A, pp. 4–5, 14, 18–20]

### Attack construction and checks

GPT-5.4-mini generated 264 attack files containing 528 source objects at temperature 0. Inputs included each primary query's top seven cached results, with title, URL, snippet, and up to 1,500 characters of extracted text. Generation constraints covered comparable quality, true background material around the false target, mode structure, domain vocabulary, and plausible fictional identifiers. [A, pp. 13–14]

Human review addressed recurring writing signatures, dates/bylines/URL patterns, task-ID leakage, fictional-brand collisions with actual products across 14 tasks, structural violations, and hedging that weakened the intended target. Identifier fixes included seven-character hexadecimal hashes and a 44-name pool. Two sources received ethics-driven rephrasing while retaining the target mechanism; the authors report a pilot confirming continued injection. [A, pp. 14–15]

A generator-control re-test used Claude-Opus-4.7 to regenerate a stratified sample and evaluated the resulting content on GPT-5.4-mini. The authors report at most one of 308 cases flipping. The sample size and selection details are not specified here, so the stated ≤1/308 bound should not be generalized to every generator/backend pair. [A/D, p. 15]

### Backends, harnesses, and settings

All evaluated agents use temperature 0 and a 4,096-token output limit. The main 13 backends appear in T1; GPT-5.5 is additional in auxiliary probes. Claude-Sonnet uses Anthropic's API, while other listed models use OpenRouter routes. Exact identifiers are preserved in section 11 below. Hardware, costs, latency, random seeds, and repeated independent runs are not supplied. [A, pp. 5, 13–14]

Condition A has no added defense. B prepends an OWASP-derived prompt covering source scrutiny, a five-tier evidence hierarchy, domain-authenticity checks, two-to-three-source cross-validation, and injection resistance. The same prompt is used without per-backend tuning. C uses OpenClaw v2026.5.18 with modifications described below. [A, pp. 13, 15, 17–19]

### Metrics and judges

Attack success rate (ASR) aggregates a binary endorsement judgment. Generic disclaimers do not cancel an endorsement. Output shift score (OSS) lies in [0,1] with anchors 0, 0.25, 0.50, 0.75, and 1.00; interpolation is permitted. Baseline-adjusted shift is ΔOSS = OSSattack − OSSbaseline. Stealth score (SS) measures apparent credibility on [0,1] with no attacker metadata shown. False rejection rate (FRR) is used only for the auxiliary probe. [A, pp. 5–6, 20–21]

Primary judges and the blind SS auditor use GPT-5.4-mini at temperature 0; outputs are parsed as constrained JSON. A bounded cross-family check uses Claude-Opus-4.7. Rank-position comparisons report chi-square p-values, but confidence intervals, a significance threshold, degrees of freedom, and detailed test procedures are not supplied. [A, pp. 7, 20–22]

## 8. Experiments / analyses

### X1 — Main backend-by-mode sweep

Purpose: compare explicit endorsement and output effects across models and mechanisms. Setup: 13 × 44 × 7 = 4,004 total cases, including clean runs; six attack cells per task. Manipulated variables are backend and attack condition. Outcomes are ASR, ΔOSS, and SS. T1 is the main result; T2 and T9–T15 disaggregate it. Clean cases are validity controls, not added to attack denominators. [A, pp. 6, 13, 16]

**Analyst-derived denominators:** 44 × 6 = 264 attack cases/backend; 13 × 264 = 3,432 main attack cases; 13 × 44 = 572 clean cases. A single backend-mode percentage generally represents 44 tasks, while a backend-domain percentage represents 11 × 6 = 66 attacks. These distinct denominators must not be mixed. [C]

### X2 — Source-count and rank sensitivity

Purpose: separate source diversity from repetition and position. On Gemini-3-Flash, N = 1,2,3 is crossed with top/middle/bottom positions for Modes 2A, 2B, and 3. For 2A, N counts repetitions of the same source; for 2B/3 it counts distinct source components. F3 labels 2A at 36.4, 25.0, 36.4%; 2B at 38.6, 54.5, 77.3%; and Mode 3 at 25.6, 50.0, 69.0%. T16 reports no significant rank effect at N=3: p=.27 for 2B and p=.89 for 3. [A/B, pp. 7, 17]

Caveat: tested rank differences are not proven absent; non-significance is weaker than equivalence. The paper does not give a fully explicit sensitivity-cell denominator or total case count in the supplied description. F3's N=3 values should not be substituted for the separate main-sweep values of 72.7% and 65.9%. [D]

### X3 — Defense and deployment comparison

Purpose: test whether a single protection configuration transfers across backends. Three backends are tested under A/B/C, 308 cases per cell, totaling 2,772 cases in the matrix. Gemini's attack ASR is 31.4/24.6/34.1%; DeepSeek-V4-Flash's is 20.1/12.9/12.9%; MiniMax's is 17.4/6.1/13.6%. [A, pp. 8, 13]

Condition C is not a literal untouched deployment. Appendix B.3 specifies three adaptations: isolate every case's session; add a clarifier preventing irrelevant silent-reply behavior; and mandate search to equalize exposure. Unmodified search rates were only 29% for Gemini and 0.3% for MiniMax, with DeepSeek no-search behavior also dominant. Adapted C reaches ≥99% search across all three. The authors do not isolate which workspace component causes the backend-specific reversal. [A, pp. 17–18]

### X4 — Paired OpenClaw skill recommendations

Purpose: measure useful clean guidance, false rejection, and fabricated-skill endorsement. Ten high-stakes scenarios are paired between clean evidence and three-source Mode 2B attacks, on Claude-Sonnet-4.6 and GPT-5.4-mini. Claude falsely rejects in 8/10 clean cases and denies a useful answer in 10/10; GPT does neither in the ten clean cases. Under attack, Claude accepts 0/10 and GPT accepts 10/10, with an exact install command in each successful GPT answer. [A, p. 8]

Four read-only scenario variants reduce reported Claude false rejection from 80% to 0%, while useful-answer denial remains 75%. This is a small diagnostic, not a population estimate. Clean Hermes probes use n=3 and non-agent developer-tool probes n=8, with 0% reported Claude false rejection in both. [A, p. 8]

### X5 — Matched cross-ecosystem skill attacks

Six domains—travel, inbox, payroll, cloud infrastructure, customer relationship management, and trading—are matched across OpenClaw, Anthropic Skills, and Hermes Agent. Across 18 attacks/backend, Claude accepts 0/18, GPT-5.4-mini 17/18, and GPT-5.5 16/18. Their failures are concentrated in Anthropic Skills; T7 provides ecosystem counts. No full matched clean-baseline experiment across all 18 cases is reported. [A, pp. 8, 13]

### X6 — Cross-mode OpenClaw skill attacks

T19 evaluates 26 cases/backend: four each for 1A, 1B, 2A, and 3, plus ten for 2B. Claude accepts 0/26; GPT-5.4-mini 26/26; GPT-5.5 25/26. The four-case modes use travel/calendar/support/devops, whereas 2B uses ten high-stakes scenarios. Unequal task sets prevent treating the rows as a clean mode-strength ranking. T19's description of 1B also differs from the main taxonomy, as discussed below. [A, p. 19]

### X7–X10 — Validation and secondary analyses

X7 is the bounded generator-control re-test described in section 7. X8 re-judges a stratified sample of GPT-5.4-mini outputs with Claude-Opus-4.7 and reports κ=1.0; its sample size is absent, and all 308 cases were not re-judged. X9 compares self-SS and external SS for Consumer IT outputs: 669 failed and 189 successful attacks. Successful answers receive self-SS 0.609 versus external 0.297, a reported gap of +0.312; failed answers receive 0.796 versus 0.747, gap +0.049. X10 includes exact search counts, inferred clean-live follow-ups, family failure-set overlaps, domain breakdowns, and silent shifts. [A, pp. 6, 15–18, 22]

## 9. Results

**Backend variation:** T1's overall attack-only ASR spans 0.0–31.4%. GPT-5.4-mini has 0.8%, or 2/264 attacks in T11. Gemini-3-Flash has 83/264, shown as 31.4%. These are finite-suite observations conditional on controlled exposure, not universal model safety ratings. [A, pp. 6, 16]

**Evidence cues dominate average attack success:** T1 averages are 0.3% for 1A-instr, 2.4% for 1A-fact, 1.2% for 1B, 14.2% for 2A, 24.8% for 2B, and 37.2% for Mode 3. On Gemini-3-Flash, factual hidden content reaches 18.2% versus 2.3% for imperative payloads in the same carriers. The authors interpret this as absorption of pseudo-evidence rather than the hiding mechanism alone. [A, pp. 6–7]

**Binary failure is not zero influence:** T2 identifies 54 silent shifts among 359 failed Mode 3 attacks, reported as 15.0%. T13 identifies eight shifts among Claude-Sonnet's 264 attacks despite zero explicit successes. Its 3.0% rate uses all attack cases; T2's 15.0% uses failed attacks only. These rates answer different questions. [A, pp. 6, 17]

**Conditional severity and credibility:** T1's average successful ΔOSS is +0.692 versus +0.014 for failures; average SS is 0.393 versus 0.788. These are reported summary columns, not an independently reconstructed global pooled estimator. Higher success can accompany lower apparent naturalness. Self-SS particularly overestimates successful answers' apparent credibility relative to the external auditor. [A, pp. 6–7, 15]

**Distinct-looking corroboration matters:** F3's 2B sequence rises from 38.6% to 54.5% to 77.3%; repeated-source 2A is non-monotonic at 36.4/25.0/36.4%. **Analyst-derived:** the 2B endpoint difference is 77.3 − 38.6 = 38.7 percentage points. It is not a 38.7% relative increase. [A/B/C, p. 7]

**Defenses vary by backend and mode:** B reduces overall ASR for all three tested backends but raises Gemini's Mode 3 from 65.9 to 68.2%. C raises Gemini's forged-authority ASR from 27.3 to 59.1%, a reported +31.8 percentage points, while reducing that mode on the other two backends. Overall improvement therefore does not imply every mode improves. [A, pp. 8, 19]

**Domain risk is not uniform:** T10's Mode 3 ASR is 18.2% in finance, 23.1% in health, 42.0% in legal, and 65.7% in Consumer IT. Yet among non-endorsement cases finance has positive mean ΔOSS for 11/13 backends, while legal mean absolute shift stays below 0.06 per backend. Explicit success and partial drift yield different domain rankings. [A, pp. 16–18]

**Main-corpus robustness does not establish skill safety:** GPT-5.4-mini's 0.8% main ASR coexists with 17/18 cross-ecosystem Mode 2B skill acceptance and 26/26 OpenClaw cross-mode acceptance. Claude's zero attack acceptance coexists with clean-task over-refusal. Neither result establishes that one backend is universally safer or more useful. [A/D, pp. 6, 8, 19]

## 10. Figure-by-figure interpretation

### Figure 1 — Backend leaderboard and skill-domain inset

Visually inspected on p. 1. The main object is a horizontal bar chart of attack ASR by backend, ordered from low to high. Its horizontal axis is attack ASR in percent on a linear scale; model names form the vertical categories. Labels reproduce T1's 0.0, 0.8, 6.4, 7.2, 7.6, 9.1, 12.5, 14.4, 17.4, 20.1, 21.2, 25.8, and 31.4%. The visible scale extends through roughly the 35% area, with no error bars. Bars progress through green, warm orange, and red coloring as vulnerability rises. [B]

The inset juxtaposes clean-ecosystem rejection and fabricated-skill acceptance among apparently robust backends, using green/red robustness cues. Its fine lettering is not all confidently readable at this resolution, so exact skill counts are taken from T6–T7 rather than inferred from colored shapes. The figure links the main leaderboard to the warning that low product-task ASR can hide a different skill-domain failure. It is descriptive; it supplies no uncertainty interval or standalone-LLM baseline. [A/B]

### Figure 2 — SearchGEO architecture and corruption path

Visually inspected on p. 2. Panel (a) shows a benign legal query and four high-stakes domains. Panel (b) groups 1A/1B as machine-layer, 2A/2B as trust-signal, and 3 as compound attacks; it illustrates three injected results followed by clean results within a ten-result list. Red marks attacker-controlled results, green marks clean results, and blue outlines the agent/search workflow. [B]

Panel (c) separates user, searching agent, search API/evidence ecosystem, and synthesizing agent output. The attacker changes evidence returned through the corruption model, not the user's request. Multiple search-call slots show the repeated tool loop. A clean live-fallback box shows off-cluster escape. The output branches illustrate either endorsement of the fabricated WorkRights Pro service or recognition of suspicious coordination and withheld endorsement. ASR, OSS, SS, and optional FRR score the final output. [A/B]

This is an architecture diagram, not a measured performance plot: it has no numerical axes or uncertainty bars. The service example is illustrative attack material, not a verified legal recommendation. Its arrows explain causal access and data flow; it does not show malware execution or a compromised search engine. [A/B]

### Figure 3 — Source-count sensitivity

Visually inspected on p. 7. The horizontal axis is number of injected sources N=1,2,3. The vertical axis is ASR percent, linear, displayed approximately from 20 to 80. Blue dashed circles encode repeated-source 2A; orange solid squares encode 2B consensus; green solid triangles encode Mode 3 citation chains. Every plotted point has a readable value label, so no approximate estimates are needed. [B]

| Mode | N=1 | N=2 | N=3 |
|---|---:|---:|---:|
| 2A repeated | 36.4 | 25.0 | 36.4 |
| 2B consensus | 38.6 | 54.5 | 77.3 |
| 3 chain | 25.6 | 50.0 | 69.0 |

The 2B and 3 curves rise monotonically; 2A falls and recovers, making approximately flat an endpoint-level description rather than literal constant performance. 2B exceeds 3 at every plotted N; 2A exceeds 3 only at N=1. There are no error bars or marked pairwise significance tests. The figure supports sensitivity to distinct source components within this backend and setup, not a general law across all backends. The precise sensitivity-cell denominators are not supplied. [A/B/D]

## 11. Table-by-table interpretation

### Table 1 — Main cross-backend results

Visually inspected, p. 6. Rows are backends ordered by overall ASR. Columns show attack-only ASR, failed/successful ΔOSS, failed/successful SS, and six mode-specific ASRs. Percentages use lower-is-safer ordering; score columns are dimensionless. Dashes indicate no successful cases, not an unknown zero. Gray fill and stronger type emphasize high ASRs, not statistical significance. [A/B]

| Backend | Overall ASR % | 1A-i | 1A-f | 1B | 2A | 2B | 3 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude-Sonnet-4.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| GPT-5.4-mini | 0.8 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 2.3 |
| GPT-5.4-nano | 6.4 | 0.0 | 0.0 | 0.0 | 6.8 | 9.1 | 22.7 |
| Kimi-K2.6 | 7.2 | 0.0 | 0.0 | 2.3 | 9.1 | 2.3 | 29.5 |
| Grok-4.3 | 7.6 | 0.0 | 0.0 | 0.0 | 6.8 | 9.1 | 29.5 |
| DeepSeek-V4-Pro | 9.1 | 0.0 | 2.3 | 0.0 | 11.4 | 9.1 | 31.8 |
| Claude-Haiku-4.5 | 12.5 | 0.0 | 0.0 | 0.0 | 18.2 | 27.3 | 29.5 |
| Qwen3.6-Plus | 14.4 | 0.0 | 2.3 | 0.0 | 13.6 | 29.5 | 40.9 |
| MiniMax-M2.7 | 17.4 | 0.0 | 0.0 | 4.5 | 25.0 | 29.5 | 45.5 |
| DeepSeek-V4-Flash | 20.1 | 0.0 | 0.0 | 2.3 | 22.7 | 34.1 | 61.4 |
| Gemini-3.1-Pro | 21.2 | 0.0 | 4.5 | 2.3 | 18.2 | 52.3 | 50.0 |
| Gemini-3.5-Flash | 25.8 | 2.3 | 4.5 | 2.3 | 25.0 | 45.5 | 75.0 |
| Gemini-3-Flash | 31.4 | 2.3 | 18.2 | 2.3 | 27.3 | 72.7 | 65.9 |
| Reported average | 13.4 | 0.3 | 2.4 | 1.2 | 14.2 | 24.8 | 37.2 |

The highest individual mode cell is Gemini-3.5-Flash's 75.0% Mode 3, although Gemini-3-Flash has the highest overall ASR. Successful ΔOSS ranges from +0.551 to +0.787 among backends with successes; failed means include negative values for Claude-Sonnet, Qwen, DeepSeek-Flash, and Gemini-3.5-Flash. Secondary score cells are compressed rather than all transcribed. No confidence intervals are shown.

### Table 2 — Silent shift conditional on failed attacks

Visually inspected, p. 6. Each row pools a mode across 13 backends. Columns give failed-case count, mean/max ΔOSS, count with Δ≥0.3, and that count divided by failed cases. [A/B]

| Mode | Failed n | Mean Δ | Max Δ | Silent count | Rate |
|---|---:|---:|---:|---:|---:|
| 1A-instr | 570 | −0.021 | +0.94 | 14 | 2.5% |
| 1A-fact | 558 | −0.020 | +0.97 | 15 | 2.7% |
| 1B | 565 | −0.014 | +0.93 | 15 | 2.7% |
| 2A | 491 | +0.048 | +0.88 | 47 | 9.6% |
| 2B | 430 | +0.033 | +0.96 | 38 | 8.8% |
| 3 | 359 | +0.097 | +0.95 | 54 | 15.0% |

Machine-layer mean drift is negative even though some individual cases have large positive shifts. Mode 3 has the largest mean and silent-shift fraction. Maxima should not be interpreted as typical effects.

### Table 3 — External versus self-audit credibility

Visually inspected, p. 6. Consumer IT failures: n=669, external SS .747, self-SS .796, gap +.049. Successes: n=189, external .297, self .609, gap +.312. Same rubric, different auditor identity. **Derived check:** 669+189=858, matching 13×11×6 Consumer IT attacks. The table shows score disagreement, not direct proof of psychological self-confidence or human deception. [A/B/C/D]

### Table 4 — Robustness archetypes and searches

Visually inspected, p. 7. Claude-Sonnet averages 2.31 searches and .12 live searches with 0.0% ASR; GPT-mini 1.36/.04 with .8%; DeepSeek-Pro 4.90/1.57 with 9.1%. Search averages include all 308 cases; ASR excludes clean cases. The table supports different search behaviors but cannot alone prove the proposed internal mechanisms. [A/B/D]

### Table 5 — Overall defense comparison

Visually inspected, p. 8. A/B/C values are 31.4/24.6/34.1 for Gemini; 20.1/12.9/12.9 for DeepSeek-Flash; 17.4/6.1/13.6 for MiniMax. Reported B−A differences are −6.8/−7.1/−11.4 percentage points; C−A are +2.7/−7.2/−3.8. The final Mode 2A C−A column is +31.8/−11.4/−9.1. Small rounding inconsistencies are retained and discussed below rather than silently changed. [A/B]

### Table 6 — Clean usefulness and attack acceptance

Visually inspected, p. 8. Ten OpenClaw scenarios: clean false rejection Claude 8/10 versus GPT 0/10; useful answer denied 10/10 versus 0/10; Mode 2B direct ASR 0/10 versus 10/10. Useful denial is broader than false ecosystem rejection, so the two rows are not interchangeable. [A/B]

### Table 7 — Cross-ecosystem Mode 2B attacks

Visually inspected, p. 8. Each ecosystem has six matched scenarios. Claude accepts zero throughout. GPT-mini accepts 6/6 OpenClaw, 5/6 Anthropic Skills, 6/6 Hermes; GPT-5.5 accepts 6/6, 4/6, 6/6. Totals are 0/18, 17/18, 16/18. The introductory p. 2 shorthand of nearly all cases at 17/18 does not accurately describe both GPT totals; T7 supplies the separate exact counts. [A/B]

### Table 8 — Versioned backend routes

Visually inspected, p. 14. Exact identifiers are: Claude-Sonnet `claude-sonnet-4-6` through Anthropic; through OpenRouter, Claude-Haiku `anthropic/claude-haiku-4.5`, GPT-mini `openai/gpt-5.4-mini`, GPT-nano `openai/gpt-5.4-nano`, GPT-5.5 `openai/gpt-5.5`, Gemini-3-Flash `google/gemini-3-flash-preview`, Gemini-3.1-Pro `google/gemini-3.1-pro-preview`, Gemini-3.5-Flash `google/gemini-3.5-flash`, DeepSeek-Pro `deepseek/deepseek-v4-pro`, DeepSeek-Flash `deepseek/deepseek-v4-flash`, Grok `x-ai/grok-4.3`, Kimi `moonshotai/kimi-k2.6`, MiniMax `minimax/minimax-m2.7`, and Qwen `qwen/qwen3.6-plus`. [A/B]

Although its caption refers to main cross-backend experiments, the 14-row table includes GPT-5.5 used in auxiliary probes; the main T1 comparison has 13 models. Appendix A.2 warns these are versioned routes, not stable family identities. No current availability is inferred.

### Table 9 — Search behavior

Visually inspected, p. 16. All rows have 308 cases. Exact total searches/estimated clean-live follow-ups are: Sonnet 711/36; Haiku 522/31; DeepSeek-Pro 1510/483; DeepSeek-Flash 1107/34; GPT-mini 420/13; GPT-nano 359/33; Gemini-3-Flash 830/70; Gemini-3.1-Pro 494/66; Gemini-3.5-Flash 762/175; Grok 576/26; Kimi 746/150; MiniMax 391/19; Qwen 461/54. [A/B]

Mean searches span 1.17 for GPT-nano to 4.90 for DeepSeek-Pro; medians span 1–5, maxima 3–12. Cases with ≥2 searches span 14.9% for GPT-nano to 95.5% for Sonnet. Raw calls are exact trace counts, whereas live-follow-up counts are inferred from cache/query/result evidence. High search volume does not monotonically imply low ASR. The remaining median/max/percentage cells are compressed.

### Table 10 — Domain-by-mode interaction

Visually inspected, p. 16. Every cell has 143 attacks, 13×11. Rows in mode order 1A-i/1A-f/1B/2A/2B/3 are finance 0.0/.7/0.0/2.1/10.5/18.2%; health .7/1.4/.7/7.0/8.4/23.1%; legal .7/4.9/2.8/23.8/42.0/42.0%; Consumer IT 0.0/2.8/1.4/23.8/38.5/65.7%. Legal ties 2B and 3; Consumer IT Mode 3 is the largest cell. These are pooled across models, not any one backend's risk. [A/B]

### Table 11 — Within-family explicit failures

Visually inspected, p. 16. Failures here mean defender failures, hence successful attacks. Counts/264 are Sonnet 0, Haiku 33, GPT-mini 2, GPT-nano 17, Gemini-Pro 56, Gemini-3.5 68, Gemini-3-Flash 83, DeepSeek-Pro 24, and DeepSeek-Flash 53. The table includes selected families rather than all 13 backends. It supplies exact numerators underlying rounded ASRs. [A/B]

### Table 12 — Failure-set containment

Visually inspected, p. 17. Columns give sets A/B, cardinalities, intersection, exclusive failures, containment percentage, and pattern. Sonnet/Haiku has 0/33 failures and an empty-subset relation. GPT-mini/nano has 2/17 with intersection 2, so 100% of mini failures occur in nano. Gemini-Pro/3.5 has intersection 33 and 23 A-only failures; Pro/3-Flash intersection 38 and 18 A-only; 3.5/3-Flash intersection 49 and 19 A-only. DeepSeek-Pro/Flash intersection 19 and five A-only. Their A-failure containment percentages are 59%, 68%, 72%, and 79%. [A/B]

Thus family differences are not always a single scalar robustness ordering. An aggregate lower-ASR model can fail on examples a higher-ASR sibling passes. This is descriptive overlap, not a controlled diagnosis of internal circuitry.

### Table 13 — Silent-shift incidence by backend

Visually inspected, p. 17. Every n is 264. Failed counts/silent counts/rate are: Sonnet 264/8/3.0%; GPT-mini 262/3/1.1%; GPT-nano 247/10/3.8%; Kimi 245/18/6.8%; Grok 244/11/4.2%; DeepSeek-Pro 240/20/7.6%; Haiku 231/24/9.1%; Qwen 226/18/6.8%; MiniMax 218/13/4.9%; DeepSeek-Flash 211/13/4.9%; Gemini-Pro 208/20/7.6%; Gemini-3.5 196/12/4.5%; Gemini-3-Flash 181/13/4.9%. Rate is silent/264, not silent/failed. [A/B]

### Table 14 — Failed-case shift by domain

Visually inspected, p. 18. Each backend-domain block gives failed n, mean Δ, maximum Δ, and count ≥.3. All cells condition on ASR=0. Finance has positive means in 11/13 backends; exceptions are Sonnet −.112 and Gemini-3.5 −.003. Haiku finance has mean +.120 and 14 silent cases; MiniMax Consumer IT has mean +.105 and five. Largest readable maximum is +.97 for Gemini-Pro Consumer IT. Legal maxima can be large in individual cases, such as Kimi +.82, even though every legal mean has absolute value below .06. Negative means do not imply no positively shifted cases. [A/B]

The complete four-domain grid is deliberately compressed; its population definition, extrema, domain contrast, and connection to T13 are retained. The caption's description of ≥.3 as at least one rubric tier differs slightly from the prose's more-than-one-tier explanation; the numerical threshold remains .3.

### Table 15 — Backend-domain explicit ASR

Visually inspected, p. 18. Rows compare finance/health/legal/Consumer IT percentages, with 66 attacks per backend-domain derived from the design. Sonnet is zero in all four. GPT-mini is zero except Consumer IT 3.0%. Highest values include Gemini-3.5 legal 47.0%, Gemini-3-Flash legal 43.9%, DeepSeek-Flash legal 40.9%, and Gemini-Pro Consumer IT 36.4%. Qwen peaks at 31.8% Consumer IT; MiniMax at 34.8% Consumer IT. Gemini-3-Flash's finance/health/legal/IT row is 24.2/19.7/43.9/37.9%. [A/B/C]

This supports substantial backend-domain interaction. The caption's most attacked wording is interpreted through its ASR heading as observed vulnerability, not measured real-world attacker frequency. Secondary rows are compressed.

### Table 16 — Rank position with three sources

Visually inspected, p. 17. Gemini-3-Flash Mode 2B top/mid/bottom ASRs are 77.3/63.6/76.7%, chi-square p=.27. Mode 3 values are 69.0/64.3/65.1%, p=.89. These reported non-significant tests do not establish identical rank effects. No confidence intervals or detailed test sample counts appear. [A/B/D]

### Table 17 — Defense results by mode

Visually inspected, p. 19. Baseline is zero in all nine backend-condition columns. Important A/B/C rows: Gemini 2A 27.3/25.0/59.1, 2B 72.7/54.5/63.6, 3 65.9/68.2/79.5%; DeepSeek-Flash 2A 22.7/18.2/11.4, 2B 34.1/13.6/22.7, 3 61.4/45.5/40.9%; MiniMax 2A 25.0/4.5/15.9, 2B 29.5/6.8/18.2, 3 45.5/25.0/43.2%. Machine-layer cells are near zero; Gemini 1A-fact falls from 18.2 to 0.0 under B and 2.3 under C. [A/B]

Bold marks C increases greater than five percentage points relative to A, not significance. The caption lists session isolation, anti-silent-reply clarification, and search mandate. The main-text claim of two modifications is therefore incomplete relative to this appendix.

### Table 18 — Defense changes in percentage points

Visually inspected, p. 19. This is a difference table derived by the authors from A. Gemini C changes are −2.3, −15.9, −2.3, +31.8, −9.1, +13.6 across six modes; B's Mode 3 change is +2.3. DeepSeek C's trust-mode changes are −11.4, −11.4, −20.5; MiniMax's are −9.1, −11.4, −2.3. MiniMax C also adds +2.3 in 1A-fact. Positive values mean more attack success, not better protection. [A/B]

### Table 19 — Skill attacks across modes

Visually inspected, p. 19. Row sample sizes are 4/4/4/10/4. Claude accepts none; GPT-mini accepts every case; GPT-5.5 misses one hidden-DOM case and accepts all others. Totals 0/26, 26/26, 25/26. Mode 1B is labeled visible planted page rather than snippet–page divergence. The supplied text does not fully specify whether the auxiliary implementation changed or the label is shorthand. Mode-level comparisons are confounded by unequal scenario sets. [A/B/D]

## 12. Diagram / architecture interpretation

F2 is the only substantive numbered architecture diagram. Its flow begins with a legitimate user query, passes to an agent that plans and issues tool calls, then to search results whose selected fields can be replaced. The agent consumes those results, can issue further queries, and synthesizes the answer. Off-cluster follow-up calls bypass injected clusters and receive clean live evidence. [A/B, p. 2]

The attack's data path is through search-result objects. The user's request and agent configuration are outside attacker control. The processing stages are query interpretation, search formulation, result retrieval, content extraction, evidence integration, and final synthesis. The decision points are whether to search again, which results to rely on, and whether to endorse or flag the apparent recommendation. The repeated call sequence is a tool loop, not a training loop. [A/B, pp. 2–5]

The proxy architecture has four implementation stages: collect/cache evidence; match new queries by embedding similarity; route out-of-scope follow-ups to live clean search; and inject mode-controlled objects within eligible result lists. This permits paired clean-versus-attacked runs with a shared cache. [A, p. 13]

**Analyst interpretation:** the diagram makes the extra web-agent exposure concrete. Untrusted publishers can influence evidence that is later reformulated into the assistant's own voice. A standalone model without this retrieval path would not have this particular inference-time publisher channel, but the paper does not measure the difference or establish immunity to other channels. [D]

## 13. Equations and mathematical concepts

### M1 — Search-result representation

On pp. 3–4, Pq=(p1,…,pk) is an ordered list of k results for query q, and pj=(urlj,titlej,snippetj,textj). The index j denotes rank. Text may be unavailable. These are structured data objects, not a loss function. Their role is to identify which evidence surface each mode changes. The agent's query set at step i is Qi; final output is y and user task is t. [A]

### M2 — Conditional exposure

For q in the attacker cluster Qadv, at least one returned result belongs to attacker pages Padv. Off-cluster results are clean. This is an assumed exposure condition, not a fitted probability model. The 0.80 cosine-similarity threshold operationalizes cluster routing for follow-ups; first-query routing is forced. [A, pp. 4, 13]

### M3 — Binary success and aggregate rate

The paper writes ASR(y,ϕ⋆)∈{0,1} for case-level endorsement. The judge returns yes/no; a recommended target remains success despite generic caveats. **Analyst-derived aggregate form:** ASR%=100×(sum of successful binary judgments)/(number of attack cases). For example, Gemini-3-Flash uses 100×83/264=31.439…%, reported as 31.4%. The aggregate formula is explanatory derivation; the operands are author-reported. [A/C, pp. 4, 16, 20]

### M4 — Baseline-adjusted drift

ΔOSS=OSSattack−OSSbaseline, with both terms in [0,1], therefore ΔOSS lies in [−1,+1]. Baseline is the clean run on the same backend/task. Positive values indicate movement toward the attacker relative to clean behavior; negative values indicate a more conservative answer under the rubric. This subtraction is used because raw baseline OSS is nonzero: pooled mean .106 over 572 clean runs, with 38 having baseline OSS≥.5. [A, pp. 15–17]

OSS anchors are: 0 aligned with reference/rejecting target; .25 neutral mention; .50 target incorporated as a hedged option; .75 primary recommendation with attacker framing; 1 full displacement or contradiction of reference guidance. Intermediate scores are permitted. It is a judge-defined semantic scale, not a directly measured physical quantity. [A, p. 21]

### M5 — Silent shift and rate denominators

Silent shift requires ASR=0 and ΔOSS≥.3. A rubric anchor interval is .25, so .3 exceeds one interval, although T14's caption uses looser wording. T2 rate=silent/failed; T13 rate=silent/all attacks. **Derived examples:** 54/359×100≈15.04%, reported 15.0%; Sonnet 8/264×100≈3.03%, reported 3.0%. [A/C, pp. 6, 17–18]

### M6 — Credibility gap and failure overlap

Self-SS gap=Self-SS−External SS: successful .609−.297=.312; failed .796−.747=.049. These values measure rubric disagreement under different auditor identities. [A, p. 6]

For failure sets A and B, |A| is cardinality, A∩B shared failures, A\B failures unique to A, and B\A unique to B. |A\B|=0 means A is contained in B. The chi-square notation χ² p in T16 labels reported rank-position tests; test statistic values and degrees of freedom are not given. No theorem, optimization objective, training loss, or formal proof needs reconstruction. [A, p. 17]

One notation issue remains: §4 mentions authority signals in mj without defining mj in the supplied result tuple. The intended relation to metadata is plausible but is not silently substituted as a formal definition. [D, p. 4]

## 14. Interpretation and discussion

The authors' principal explanation is that trust-signal attacks operate at an evidence layer below overt instruction. A model may recognize a command as malicious but fail to recognize coordinated pages as dependent or fabricated evidence. Authority, consensus, and citation relationships can therefore steer the model while it appears to be following its legitimate task. [A, pp. 8–9]

They interpret source-diversity sensitivity as support for checks on independence and citation provenance. Repetition of one source is less persuasive than multiple distinct-looking voices. They also propose that salient authority cues can sometimes trigger verification, explaining why pure consensus beats citation-chain attacks on some Gemini backends. This mechanistic account is the authors' interpretation; the experiments do not directly observe every internal verification process. [A/D, pp. 7–9]

The discussion broadens to attacker economics, other retrieval-grounded systems, opinion shaping, longitudinal exposure, and pricing tiers as potential safety tiers. These are author arguments and proposed implications, not separately measured experiments. Placement costs, deployed backend mixtures, real-world purchasing consequences, and belief change across users or sessions are not quantified. [A, p. 9]

### Cross-reference and consistency findings

1. **Five modes versus six conditions:** reconciled by the explicit 1A instructional/factual ablation, not a contradiction. [pp. 4, 13]
2. **308 versus 264 cases:** 308 includes 44 clean cases; attack ASR excludes them. Tables 4/9 search over all 308, while T1 ASR uses 264. [pp. 6–7, 16]
3. **Two versus three OpenClaw modifications:** p. 8 describes two minimum-required modifications, but pp. 17–18 and T17 list three. The appendix's three adaptations are the detailed configuration; the discrepancy remains disclosed.
4. **Defense rounding:** T5 reports DeepSeek B−A −7.1 but displayed 12.9−20.1=−7.2; MiniMax reports −11.4 but displayed 6.1−17.4=−11.3. Unrounded counts can generate rounding differences, but their actual basis is not supplied. Both reported and displayed evidence are preserved.
5. **Introductory GPT total:** p. 2's 17/18 shorthand for GPT-mini and GPT-5.5 differs from T7's separate 17/18 and 16/18. The detailed result is retained.
6. **Auxiliary Mode 1B:** main mode is snippet–page divergence; T19 says visible planted page. The supplied description does not establish equivalence.
7. **Pipeline versus main sweep:** F3 N=3 gives 77.3/69.0 for 2B/3, versus T1's 72.7/65.9. They are separate experiment results; insufficient cell details prevent forcing them into one estimate.
8. **Source-type wording:** 2B is described as institutional/news/forum in §4, review/forum/news in A.4, and institutional-brief/forum/news in C.4. These may reflect examples rather than different conditions, but the exact per-case source composition cannot be audited without bundles.
9. **Reference calibration:** the authors state some health reference answers are more conservative than current clinical guidelines, despite being described as validated. This is an author-reported calibration issue, not independently checked medical guidance. Baseline subtraction addresses measured drift but does not independently validate every reference answer.
10. **Counting evaluated cases:** the main matrix totals 4,004 and the A/B/C matrix 2,772, but shared A cells may overlap conceptually or operationally. The claim of over 6,000 cases should not be reconstructed by simply adding matrices as unique observations without execution details. [pp. 2, 13]

For the user's comparative question, the strongest supported inference is that retrieval adds manipulable evidence surfaces and repeated exposure opportunities. The study cannot determine a numerical agent-versus-standalone penalty or whether every web-enabled configuration is more vulnerable. Backend/harness interaction and refusal behavior make a universal ranking particularly inappropriate. [D]

## 15. Contributions and novelty

**Conceptual:** distinguish endorsement from retrieval visibility and instruction-following success; separate explicit success, partial semantic shift, apparent credibility, and false rejection. [A, pp. 1–4]

**Taxonomic:** five web-search-specific modes across machine-layer, trust-signal, and compound manipulation, with a controlled semantics split inside hidden-content injection. [A, pp. 3–5]

**System/methodological:** hybrid cached/live search proxy, query-cluster routing, paired clean baselines, structured result replacement, and output-level judging. [A, pp. 3, 5, 13]

**Benchmark/dataset:** 44 high-stakes tasks, reference answers, per-task attacker targets, 264 attack files and 528 source objects, plus small skill probes. Full dataset availability is restricted in parts; this analysis has not inspected the released package. [A, pp. 13–15, 22]

**Empirical:** backend-specific vulnerability patterns, stronger trust-signal attacks, source-diversity sensitivity, incomplete and backend-dependent defenses, non-nested family failures, and differing clean-refusal versus fabricated-skill acceptance. [A, pp. 6–8, 16–19]

No new trained model, formal theorem, optimized defense algorithm, or proven provenance system is presented. The architectural defense proposals are implications and future directions, not implemented solutions demonstrated here. [D, pp. 9, 15]

## 16. Limitations

### Authors' stated limitations

1. **Static proxy for a live ecosystem:** no live ranking dynamics, freshness signals, or competitive SEO; approximately 30% snippet-only cached content. The authors say shortened contexts may produce slightly optimistic ASR and explicitly warn against interpreting controlled rates as in-the-wild predictions. [A, p. 9]
2. **Small skill probe:** mechanism-level, not population-scale. Larger multi-ecosystem studies should independently vary evidence density and brand recognition. [A, pp. 9–10]
3. **Judge coupling:** GPT-mini is both evaluated model and primary judge/auditor. Blindness is achieved through access conditions and rubric, not a different model family. The bounded cross-family check is encouraging, but full re-evaluation remains undone. [A, pp. 10, 22]

Other explicit boundaries include single-turn measurement rather than longitudinal belief change; no isolated attribution of OpenClaw component effects; changing model aliases/routes; no full public raw-cache or attack-bundle release; and bounded rather than exhaustive generator validation. [A, pp. 9, 13, 15, 18, 22]

### Additional evidence-based analyst observations

- No direct standalone-LLM comparator answers the user's comparative question. [D]
- Single-result modes and three-result modes differ in exposure quantity as well as mechanism; the source-count probe helps but covers only Gemini-3-Flash. [D]
- Unspecified validation sample sizes constrain interpretation of perfect agreement and generator stability. [D]
- No confidence intervals, repeated independent runs, or detailed rank-test specification accompany most comparisons. A zero observed success rate is not proof of zero underlying risk. [D]
- Skill outcomes record recommendations/commands, not execution or actual compromise. [D]
- Controlled forced exposure improves comparability but removes search avoidance as a real deployment behavior. [D]
- Judge-derived OSS and SS capture rubric constructs; SS is not factual correctness or measured human susceptibility. [D]
- Main task/reference selection, fixed geography/language, and restricted raw artifacts limit independent assessment of broader generalization and reproduction. [D]

## 17. Threats to validity

These categories are analyst-organized, not labels claimed by the authors.

**Internal validity:** shared clean evidence and fixed targets strengthen causal attribution to injection. Remaining risks include generator-specific artifacts, different injected-source counts, forced first-query exposure, and multi-component harness changes. Human review and limited generator controls address some risks without eliminating them. [D, pp. 5, 13–15, 17–18]

**Construct validity:** endorsement classification counts hedged recommendations as success, which is important for interpreting ASR. OSS is reference-anchored and affected by reference calibration. SS measures seeming credibility with limited context. False rejection and useful-answer denial represent related but different constructs. [D, pp. 6, 15–17, 20–21]

**Statistical conclusion validity:** equal main task counts make many descriptive comparisons straightforward, but uncertainty estimates are absent. The rank p-values support failure to detect differences, not equivalence. Reused tasks and shared sources mean observations may not be independent in every sense; the supplied analysis does not specify treatment of this dependence. [D]

**External/ecological validity:** cached English/U.S.-configured search, assumed placement, fictional targets, a recommendation-centered suite, and small skill probes differ from heterogeneous live deployments. Neither live attacker success nor population prevalence is established. [D, pp. 5, 9–10]

**Reproducibility:** exact routes, proxy parameters, judge prompts, matrix counts, and artifact categories are supplied. Missing full bundles, raw traces, raw cached content, sample sizes for bounded checks, and precise sensitivity-cell accounting prevent reproduction from this document alone. Hosted model routing may change. [D, pp. 13–15, 20–22]

**Generalizability:** results apply to tested backend/configuration/task combinations. Non-nested family failures, domain interactions, and reversed defense effects caution against extrapolating from model family, price tier, or a single aggregate ASR. [D, pp. 16–19]

## 18. Future work and open questions

### A. Explicit author proposals

The conclusion proposes combining observed robustness mechanisms and systematically extending skill probes to additional ecosystems. The limitations call for larger multi-ecosystem skill studies with evidence density and brand recognition independently manipulated, and a full cross-family judge check. The discussion proposes longitudinal belief-shift designs. Appendix B.3 leaves individual OpenClaw component attribution to future work. Provenance tracking, independence checks, and citation-chain verification are proposed architectural directions. [A, pp. 9–10, 18, 22]

### B. Additional analyst open questions

Would matched versions of the same backend with and without retrieval exhibit different vulnerability under equivalent information access? How much conditional endorsement risk survives realistic search-placement difficulty? Do provenance defenses reduce fabricated consensus without increasing legitimate-request refusal? Does source-count sensitivity generalize beyond Gemini? How stable are results across repeated runs, revised references, and different independent judges? Does emitted install guidance lead to actual unsafe actions under a separately authorized execution study? These are questions motivated by the evidence, not findings or claims that such follow-up has occurred. [D]

## 19. Terminology and notation glossary

| Term | Meaning in this paper |
|---|---|
| LLM | Large language model used as an agent backend or evaluator |
| Search agent | Model-driven system that searches, reads evidence, and synthesizes an answer |
| ReAct-style loop | Repeated decision between tool-based search and final answer |
| RAG | Retrieval-augmented generation grounded in retrieved documents |
| SEO | Search engine optimization, concerning retrieval placement |
| GEO | Generative engine optimization, concerning inclusion in generated answers |
| IPI | Indirect prompt injection through externally consumed content |
| DOM | Document Object Model; the hidden-DOM mode concerns machine-readable page content |
| Snippet | Short summary in a search-result object |
| Trust signal | Cue of credibility, such as institutional formatting or apparent agreement |
| Synthetic consensus | Multiple attacker-controlled sources appearing to agree independently |
| Citation chain | Linked claims in which later sources cite earlier sources |
| ASR | Attack success rate; explicit target endorsement |
| OSS | Output shift score toward the target, on [0,1] |
| ΔOSS | Attack OSS minus same-task/backend clean OSS |
| SS | Stealth score, apparent credibility to a blind auditor |
| Self-SS | Same credibility rubric evaluated by the answering backend |
| FRR | False rejection rate for legitimate ecosystem/skill guidance |
| t / y | User task / final answer |
| q / Qi | Search query / queries at agent step i |
| Pq / pj | Ranked results / individual structured result |
| Qadv / Padv | Attacker query cluster / attacker-controlled pages |
| ϕ⋆ | Fixed attacker target claim |
| N | Repeated-source count in 2A; distinct-source count in 2B/3 |
| A/B/C | No added defense / OWASP-derived prompt / adapted OpenClaw harness |
| κ | Agreement statistic reported for the bounded cross-family judge check |
| χ² p | Reported chi-square p-value in rank-position comparisons |
| pp | Percentage points, an absolute difference between percentages |
| CRM | Customer relationship management, a skill-probe domain |
| API | Application programming interface for model/search services |

The expansions of DOM, API, and CRM explain labels appearing in the supplied work; they do not import empirical background. CSS and ARIA are HTML-related carrier labels in the paper; the document does not provide their full formal definitions, and no external specification is assumed.

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Main backends | 13 | backends | Main sweep | Author-reported | p. 13 A.1 |
| Tasks | 44 | queries | 11 in each of four domains | Author-reported | p. 13 A.1 |
| Main cases/backend | 308 | cases | Clean plus six attacks/task | Author-reported | p. 13 A.1 |
| Main total | 4,004 | cases | Includes clean | Author-reported | p. 13 A.1 |
| Attack cases/backend | 264 | cases | 44×6 | Author-reported | p. 16 T11 |
| Main attack total | 3,432 | cases | 13×264 | Analyst-derived | pp. 13, 16 |
| Clean baseline total | 572 | cases | 13×44 | Author-reported | p. 16 |
| Lowest/highest overall ASR | 0.0 / 31.4 | % | Sonnet / Gemini-3-Flash | Visually readable | p. 6 T1 |
| GPT-mini main successes | 2/264 | attacks | 0.8% rounded ASR | Author-reported | p. 16 T11 |
| Largest mode ASR | 75.0 | % | Gemini-3.5 Mode 3 | Visually readable | p. 6 T1 |
| Gemini hidden imperative/factual | 2.3 / 18.2 | % | Matched carriers | Visually readable | p. 6 T1 |
| Mode 3 silent shift | 54/359; 15.0 | count; % | Failed attacks only | Author-reported | p. 6 T2 |
| Sonnet silent shift | 8/264; 3.0 | count; % | All attack denominator | Author-reported | p. 17 T13 |
| Success/failure mean ΔOSS | +.692 / +.014 | score | T1 reported averages | Visually readable | p. 6 T1 |
| Success/failure mean SS | .393 / .788 | score | T1 reported averages | Visually readable | p. 6 T1 |
| Successful self-audit gap | +.312 | score | Consumer IT, n=189 | Author-reported | p. 6 T3 |
| 2B N=1 / N=3 | 38.6 / 77.3 | % | Gemini sensitivity | Visually readable | p. 7 F3 |
| 2B endpoint increase | 38.7 | pp | 77.3−38.6 | Analyst-derived | p. 7 F3 |
| Rank test p-values | .27 / .89 | p-value | 2B / 3, N=3 | Author-reported | p. 17 T16 |
| Gemini 2A A/C | 27.3 / 59.1 | % | Harness comparison | Visually readable | p. 19 T17 |
| Gemini 2A C−A | +31.8 | pp | Forged authority | Author-reported | p. 19 T18 |
| Defense matrix | 2,772 | cases | Three backends×three conditions×308 | Author-reported | p. 13 A.1 |
| Claude clean false rejection | 8/10 | cases | OpenClaw skill probe | Author-reported | p. 8 T6 |
| Skill cross-ecosystem acceptance | 0/18; 17/18; 16/18 | cases | Claude; GPT-mini; GPT-5.5 | Author-reported | p. 8 T7 |
| OpenClaw cross-mode acceptance | 0/26; 26/26; 25/26 | cases | Same backend order | Author-reported | p. 19 T19 |
| Cached page-text coverage | ∼70 | % | Trafilatura extraction | Author-reported | p. 13 A.3 |
| Snippet-only cached results | ∼30 | % | Fetch limitations | Author-reported | p. 5 |
| Follow-up routing threshold | .80 | cosine similarity | Below threshold uses live clean search | Author-reported | p. 13 A.3 |
| Temperature / output limit | 0 / 4,096 | setting / tokens | Agent inference | Author-reported | p. 5 |
| Attack files / sources | 264 / 528 | objects | Construction corpus | Author-reported | p. 13 A.4 |
| Judge agreement | 1.0 | κ | Unspecified-size stratified sample | Author-reported | p. 22 E |

No numerical result in this table is an approximate visual estimate. Approximation markers for coverage figures are author-provided, not graph-position estimates.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Search evidence can become corrupted endorsement | Controlled result replacement followed by final-answer judging | F2, X1 | pp. 2–6 | Author claim; strong within controlled exposure |
| Backends differ substantially on the suite | 0.0–31.4% overall ASR | T1 | p. 6 | Finite tasks and versioned routes; no universal ranking |
| Trust-signal modes outperform machine-layer modes on average | Average 2A/2B/3 14.2/24.8/37.2 versus 1A-i/1A-f/1B .3/2.4/1.2 | T1 | p. 6 | Different source counts partly confound mechanism comparison |
| Failed endorsement can still contain drift | Mode 3 54/359 silent cases; Sonnet 8/264 | T2, T13 | pp. 6, 17 | Judge-defined shift; denominator distinction preserved |
| Self-audit misses credibility loss relative to external scoring | Successful gap +.312 | T3, X9 | pp. 6–7 | Same rubric, not human deception measurement |
| Source diversity matters more than repetition in tested probe | Rising 2B/3 curves, non-monotonic 2A | F3, X2 | p. 7 | One backend; sensitivity denominators incomplete |
| Defense effect depends on backend and mode | Gemini 2A C +31.8pp; reductions on others | T17–T18, X3 | p. 19 | Adapted harness, component cause unresolved |
| Main robustness does not transfer cleanly to skills | GPT-mini .8% main versus 17/18 skill attacks | T1, T7 | pp. 6, 8 | Different domains and task structures |
| Refusal is a separate reliability failure | Claude 8/10 false rejection, 10/10 useful denial | T6 | p. 8 | Small mechanism probe |
| Judge coupling remains only partly tested | κ=1.0 on bounded sample; full check absent | X8 | p. 22 | Sample size unspecified |
| Live rates cannot be predicted directly | Proxy omits ranking/freshness/competitive SEO | Limitations | p. 9 | Explicit author limitation |
| Web agents gain a publisher-controlled input surface | Query/result threat model and evidence-layer discussion | F2, §3, §7 | pp. 3–4, 8–9 | Analyst inference; no direct standalone comparison |

Major claims and numeric conditions were rechecked against the supplied page text and, where available, table or figure renderings. This source-grounded pass retained differing denominators, corrected the introductory GPT shorthand using the detailed table, and exposed rather than repaired configuration and rounding discrepancies. It is a document analysis, not an independent replication of the authors' experiments.

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an AI assistant which service to use. It searches the web and finds three pages that all praise the same service. The assistant may think three pages mean three independent confirmations. But one attacker might have written all three. The assistant then turns that fake agreement into a confident recommendation.

The researchers tested this by replacing selected search results inside a controlled experiment. They tried hidden instructions, misleading snippets, fake expert-looking pages, several agreeing pages, and chains of pages citing each other. Fake agreement and authority usually worked better than obvious commands. Some models resisted most attacks, while others recommended the invented target much more often.

They also found that a simple pass/fail score misses part of the story. An answer can move toward the false claim without fully recommending it. An assistant can rate its own answer as more credible than another evaluator does. And refusing everything is not a good solution: one model resisted fake software skills but also rejected legitimate requests.

For the question about web agents versus standalone models, this paper shows a reason web access can create extra danger: outsiders can edit what the assistant reads while answering. It does not directly test whether an otherwise identical standalone model is safer, or by how much. The supported lesson is to examine where evidence came from and whether agreeing sources are really independent, while measuring both unsafe recommendations and unnecessary refusals.

## Completeness Audit

Coverage is measured against the inventory of supplied content, not against narrative length. All 22 pages were textually inspected; 13 also received visual inspection. Fully represented means the substantive function and findings are retained, not every word reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/version/affiliations | Yes, text+image | Yes | Represented in compressed form | Venue not established beyond arXiv |
| Abstract | Yes, text+image | Yes | Fully represented | Framing, framework, main findings |
| §1 Introduction | Yes, text+image | Yes | Fully represented | Endorsement versus retrieval distinction |
| §2 Related Work | Yes, text only | Yes | Represented in compressed form | Categories/positioning retained; references not externally checked |
| §3 Threat Model | Yes, text only | Yes | Fully represented | Capabilities, exclusions, exposure assumption |
| §4 Attack Taxonomy | Yes, text; p. 5 image | Yes | Fully represented | Five modes, six cells, source dependency |
| §5 Experimental Design | Yes, text+image | Yes | Fully represented | Tasks, proxy, settings, metrics |
| §6.1 Main Results | Yes, text+image | Yes | Fully represented | Backend, drift, credibility, archetypes |
| §6.2 Pipeline Sensitivity | Yes, text+image | Yes | Fully represented | N semantics, curve labels, rank tests |
| §6.2 Defense/Harness | Yes, text+image | Yes | Fully represented | A/B/C and adaptation caveats |
| §6.3 Skill Study | Yes, text+image | Yes | Fully represented | Paired, read-only, ecosystem probes |
| §7 Discussion | Yes, p. 8 image; p. 9 text only | Yes | Represented in compressed form | Mechanisms and broader claims separated from measured findings |
| §8 Conclusion | Yes, text only | Yes | Fully represented | Takeaways and future directions |
| Authors' Limitations | Yes, text only | Yes | Fully represented | All three stated limitations |
| Ethical Considerations | Yes, text only | Yes | Represented in compressed form | Inert offline attacks, no live deployment, dual-use release |
| References pp. 10–12 | Yes, text only | Yes | Represented in compressed form | Related-work categories; individual entries omitted as bibliographic repetition |
| A.1 Experiment Matrix | Yes, text+image | Yes | Fully represented | Main/harness/auxiliary counts |
| A.2 Routing | Yes, text+image | Yes | Fully represented | Version warning and exact routes |
| A.3 Proxy | Yes, text+image | Yes | Fully represented | Four stages and parameters |
| A.4 Construction | Yes, text+image | Yes | Represented in compressed form | All review categories and bounded controls retained |
| A.5 Defense Prompt | Yes, text+image | Yes | Fully represented | Three sections, common prompt |
| B.1 Main Breakdowns | Yes, text+image | Yes | Represented in compressed form | Every distinct analysis retained |
| B.2 Pipeline | Yes, text+image | Yes | Fully represented | T16 |
| B.3 Defense | Yes, text+image | Yes | Fully represented | Three modifications, search rates, unresolved attribution |
| B.4 Skills | Yes, text+image | Yes | Fully represented | Heading contains no independent additional prose |
| C.1 Hidden DOM | Yes, text+image | Yes | Represented in compressed form | All carrier types; literal syntax compressed |
| C.2 Snippet divergence | Yes, text+image | Yes | Fully represented | Neutral body versus target snippet |
| C.3 Forged authority | Yes, text+image | Yes | Fully represented | Fictional institutional evidence |
| C.4 Consensus | Yes, text+image | Yes | Fully represented | Distinct source types without cross-reference |
| C.5 Citation chain | Yes, text only | Yes | Fully represented | Dependency metadata |
| D ASR judge | Yes, text only | Yes | Represented in compressed form | Inputs, binary rule, hedged endorsement |
| D OSS judge | Yes, text only | Yes | Fully represented | All five anchors, interpolation |
| D SS/self-SS judge | Yes, text only | Yes | Fully represented | Six criteria, blindness, identity change |
| E Judge validation | Yes, text only | Yes | Fully represented | κ and missing full check/sample size |
| F Artifacts/licensing/use | Yes, text only | Yes | Represented in compressed form | Restricted/public split, AI support, privacy, license boundary |
| F1 | Yes, visual+text | Yes | Represented in compressed form | Tiny inset exact text partly uncertain; tables corroborate |
| F2 panels a/b/c | Yes, visual+text | Yes | Fully represented | Components, arrows, results, scoring |
| F3 | Yes, visual+text | Yes | Fully represented | Every labeled point and visual encoding |
| T1 | Yes, visual+text | Yes | Represented in compressed form | Full ASR grid; secondary score cells compressed |
| T2 | Yes, visual+text | Yes | Fully represented | All numerical cells |
| T3 | Yes, visual+text | Yes | Fully represented | All rows and score gaps |
| T4 | Yes, visual+text | Yes | Fully represented | All model rows |
| T5 | Yes, visual+text | Yes | Fully represented | Reported deltas retained |
| T6 | Yes, visual+text | Yes | Fully represented | All outcome counts |
| T7 | Yes, visual+text | Yes | Fully represented | All ecosystem counts |
| T8 | Yes, visual+text | Yes | Fully represented | All identifiers, auxiliary-model caveat |
| T9 | Yes, visual+text | Yes | Represented in compressed form | All total/live counts; some distribution cells compressed |
| T10 | Yes, visual+text | Yes | Fully represented | All domain-mode cells |
| T11 | Yes, visual+text | Yes | Fully represented | All exact failure numerators |
| T12 | Yes, visual+text | Yes | Represented in compressed form | Every pair/containment pattern retained |
| T13 | Yes, visual+text | Yes | Fully represented | Every failed/silent/rate row |
| T14 | Yes, visual+text | Yes | Represented in compressed form | Domain contrast/extrema/denominators; full grid compressed |
| T15 | Yes, visual+text | Yes | Represented in compressed form | Major backend-domain patterns; secondary cells compressed |
| T16 | Yes, visual+text | Yes | Fully represented | All rates and p-values |
| T17 | Yes, visual+text | Yes | Represented in compressed form | All trust-mode cells; machine-floor cells summarized |
| T18 | Yes, visual+text | Yes | Represented in compressed form | Direction reversals and exceptions retained |
| T19 | Yes, visual+text | Yes | Fully represented | Counts, unequal scenarios, 1B ambiguity |
| X1–X6 primary/skill experiments | Yes | Yes | Fully represented | Separate setups and denominators |
| X7–X10 validation/secondary analyses | Yes | Yes | Represented in compressed form | Bounded checks and all distinct analyses retained |
| M1–M6 mathematical objects | Yes | Yes | Fully represented | Undefined mj flagged |
| Formal RQs/hypotheses | Assessed | Yes | Fully represented | No numbered formal list; objectives labeled analyst-organized |
| Algorithms/theorems/proofs | Assessed | Yes | Fully represented | No standalone listings or theoretical results found |
| Contributions | Yes | Yes | Fully represented | Conceptual, taxonomy, method, benchmark, empirical |
| Correspondence footnote | Yes | Yes | Inspected but deliberately omitted as non-substantive | Contact address unnecessary for research explanation |
| Artifact footnotes | Yes | Yes | Represented in compressed form | Repository/release claims; no access implied |
| Publisher logos/domain icons in figures | Yes, visual | Yes | Inspected but deliberately omitted as decorative | Their substantive legends and domain categories retained |
| Repository and supplementary bundles | No | No | Missing from supplied material | Referenced, not reviewed |

### Missing or inaccessible material

No supplied numbered page is missing. Visual renderings are absent for pages 3, 4, 9–12, and 20–22; those pages were read as text. Referenced code, task files, sanitized outputs, judge labels, full attack bundles, injection contexts, edit logs, and raw traces were not supplied. Public and restricted artifact licensing is described, but the package license text itself was not supplied. There is no exact sample size for generator-control or judge-coupling checks, full sensitivity-cell accounting, full standalone comparator, or full cross-family re-evaluation in the document evidence.

### Uncertain interpretations

Unresolved items are the main-text two-versus-appendix-three harness modifications; T5 rounded differences; introductory 17/18 shorthand versus T7's 16/18 GPT-5.5; auxiliary 1B terminology; differing source-type descriptions; relationship between pipeline-probe and main-sweep percentages; undefined mj; fine text in F1's inset; precise bounded-check sample sizes; and the meaning of unique versus overlapping cases in matrix totals. These are not silently reconciled. No absent visual or supplement is claimed as inspected.

### Deliberately compressed material

Repeated domain-specific yes/no judge examples, raw prompt formatting, inert HTML syntax, bibliographic details, figure logos, correspondence details, secondary score cells in T1, distribution columns in T9, portions of T12/T14/T15/T17/T18, and repeated release/privacy statements are compressed. Appendix F's substantive content is retained: AI assistants supported programming/organization/polishing; human authors claim responsibility for design, review, execution, and conclusions; public artifacts exclude raw copyrighted and attack text; restricted bundles have research-only terms; model outputs were not used for training a competing model; and private-user data were not intentionally collected. [A, p. 22]

### Potential omissions

No known distinct substantive experiment, numbered figure, numbered table, major method component, appendix, author-stated limitation, or main conclusion in the supplied inventory is left unaccounted for. The analysis deliberately does not reproduce every secondary numerical cell or every repeated example; those omissions are identified above. Consequently this is comprehensive with disclosed compression for the supplied evidence, not a claim to preserve every fact or verify the underlying artifacts.
