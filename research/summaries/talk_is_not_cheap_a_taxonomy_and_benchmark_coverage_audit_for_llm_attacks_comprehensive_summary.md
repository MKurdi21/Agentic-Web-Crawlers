## Stage 0 — Document Accessibility Report

The supplied material contains extracted text labeled physical PDF pages 1–27 and rendered images for pages 1, 4, 5, 6, 7, 8, 14, 15, 16, 17, 18, 20, 21, and 22. All 27 numbered text pages are available; no gap in that sequence is apparent. This establishes coverage of the supplied 27-page document, not independent verification that no separate supplement exists. The two numbered figures and all seven numbered tables are present in the supplied images and were visually inspected. Additional unnumbered tables on pp. 21 and 23 were inspected visually on p. 21 and through supplied text on p. 23, respectively. Pages 2–3, 9–13, 19, and 23–27 were inspected through supplied extracted text only. Their typography, layout, and any extraction omissions cannot be independently assessed visually.

The main text, references, and Appendices A–K are present. The paper describes released taxonomy JSON, attack records, statistics, code, source manifest, interactive browser, and codebook, but these files were not supplied or inspected. No embedded supplementary files are reported in the supplied accessibility metadata. OCR was unnecessary because native text and readable rendered pages were provided. Figure 1's fine axis labels are small; its exact endpoint percentages come from its caption rather than pixel measurement. There are no numbered mathematical equations, formal algorithms, or theorems in the supplied work. The tuple notation in Appendix A is readable. The supplied source hash is retained as an identifier; it was not independently recomputed.

Evidence labels used below: **[A] Author-reported** means stated in the paper, including its accounts of other studies; **[B] Directly observable** means visible in supplied images; **[C] Analyst-derived** means calculated here with operands shown; **[D] Analyst interpretation** means an inference rather than the paper's finding. No external information is used. Confidence is HIGH for clearly legible source statements, MEDIUM for qualified interpretations or unresolved reporting issues, and UNKNOWN for unavailable artifacts. High confidence that a statement is reported does not certify its underlying scientific correctness.

## 1. Plain-language orientation

This is a security taxonomy, dataset, and benchmark-audit paper. Its original title is **Talk is (Not) Cheap: A Taxonomy and Benchmark Coverage Audit for LLM Attacks**. Karthik Raghu Iyer, Yazdan Jamshidi, Nicholas Bray, and Alexey Shvets, all affiliated with Palo Alto Networks, authored the supplied preprint. Page 1 identifies arXiv:2605.15118v2, dated 3 June 2026; no publication venue for this paper is supplied.

A large language model, or LLM, can be attacked in several ways: persuaded to produce prohibited content, induced to misuse tools, made to reveal information, or forced to consume excessive resources. The paper asks whether existing public evaluations collectively test this range of threats. Its central device is a grid with four attacker objectives and six mechanisms, yielding 24 cells. A benchmark can then be located in the grid according to what its attacks actually test.

[A] The researchers processed 932 arXiv papers, extracted 6,366 attack mentions, normalized them into 2,521 name-based groups, and constructed a 507-leaf taxonomy. They manually mapped six public benchmarks into the grid. Counting partial coverage, the benchmarks collectively reach six cells, or 25%. Entire regions concerning service disruption and model internals receive no coverage under their mapping. These are coverage findings, not measurements showing that 75% of attacks succeed or that deployed systems are 75% insecure.

For the user's question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, the paper supplies a useful mechanism-based explanation but no controlled comparison. [D] An agent that reads web pages or tool responses and can act on them creates opportunities for external content to cross a trust boundary and influence actions. The paper explicitly distinguishes harmful text from unauthorized execution. It does not establish an overall vulnerability multiplier, demonstrate that every agent is less secure than every standalone model, or isolate web access as a causal variable.

## 2. Document roadmap

The main text proceeds from motivation to corpus processing, taxonomy construction, quantitative analyses, and evaluation gaps. Section 1 introduces inadequate taxonomic coverage, fragmented names, and benchmark blind spots. Section 2 describes corpus selection, extraction, normalization, classification, and validation. Section 3 separates the literature-oriented taxonomy from the operational Target × Technique matrix and describes released artifacts. Section 4 examines matrix distribution, naming fragmentation, temporal evolution, and benchmark coverage. Sections 5–6 discuss implications and limitations. Section 7 positions the work against prior surveys; Section 8 concludes. References occupy pp. 10–13, with the conclusion continuing onto p. 10.

The appendices materially qualify the main claims. Appendix A supplies the taxonomy diagram, defense-layer definitions, output-versus-execution rule, and empty-cell analysis. B defines categories. C examines catch-all leaves. D details benchmark mapping and sensitivity. E develops a benchmark specification from one uncovered cell. F supplies temporal counts. G contains validation and sensitivity evidence. H reproduces extraction and classification prompts. I explains dropped entries. J provides the dataset datasheet, including imperfect source attribution. K states ethics and intended defensive use.

The inventory comprises eight main sections, eleven appendices, Figures 1–2, Tables 1–7, unnumbered workflow/metric tables on p. 21, two agreement tables on p. 23, three prompt templates, and the tuple A = (T, M). No explicit numbered research questions or hypotheses appear. This inventory is the denominator for the coverage audit below.

## 3. Background and context

[A] **Jailbreaking** means constructing prompts that bypass safety alignment and produce harmful outputs. **Prompt injection**, as defined here, places adversarial instructions in external data such as web content, files, application programming interface responses, or tool descriptions, rather than directly asking as the user. **Information disclosure** concerns unauthorized access to non-public information, including system prompts, training-data information, or model details. **Service disruption** targets availability, performance, or usefulness. **Decoding manipulation** intervenes in internal generation processes. **Attack generation** describes how an attack is discovered, rather than necessarily describing its final operational mechanism. These definitions are from §§3.1–3.2 and Appendix B, pp. 3–4, 16–17.

The paper separates a taxonomy from a risk matrix. The taxonomy groups work according to its role in the literature; the matrix groups it according to attacker objective and defeated defense layer. Consequently, taxonomy categories and matrix rows cannot be exchanged. A jailbreaking-category leaf can map to the Service Disruption row. A method such as Greedy Coordinate Gradient, or GCG, can belong to Attack Generation while its adversarial suffix maps to Safety Bypass × Obfuscation.

The matrix uses selected STRIDE threat-model categories. The supplied paper names Tampering, Elevation of Privilege, Information Disclosure, and Denial of Service as the grounding for its four rows. It excludes Spoofing and Repudiation as inapplicable to its chosen inference-time scope. This is the authors' modeling decision, not an independently demonstrated universal boundary.

**Benchmark-internal validation** asks whether one evaluation measures what it claims. **Benchmark-external validation** asks whether the collection of evaluations spans the threat surface. **Cell-weighted coverage** gives each target–technique combination equal weight. **Leaf-weighted coverage** weights regions by their number of taxonomy leaves. Neither directly estimates attack likelihood, expected financial loss, or defense effectiveness.

## 4. Research problem and gap

[A] The authors identify three linked problems. First, manual surveys have insufficient scale and granularity for the expanding literature. Second, different names obscure when papers discuss the same attack. Third, evaluations may leave whole threat categories untested. Their proposed response is a normalized attack dataset coupled to a reusable coverage framework, rather than another list of jailbreak examples.

The corpus is attack- and vulnerability-focused. It comes from the Promptfoo LLM Security Database, which does not publish formal paper inclusion criteria. The paper acknowledges this uncertainty while arguing that overrepresentation of familiar attack areas would strengthen the apparent neglect of tail categories. [D] That strengthening argument is conditional: the supplied evidence does not establish the direction of every possible selection bias.

The research gap is collective coverage, not merely benchmark size. A benchmark with hundreds of cases can still occupy one or two cells. Conversely, mapping a benchmark to a cell does not show that it thoroughly covers every attack within that cell. The paper's contribution is to make this distinction inspectable.

For web agents, [D] the relevant gap is that harmful-output evaluations and action-oriented evaluations cover different operational outcomes. Successful refusal of unsafe text does not establish secure tool authorization or correct handling of external instructions. The paper supports separating these assessment questions, but does not measure the relative safety of matched agent and non-agent deployments.

## 5. Research questions / objectives / hypotheses

No formal research questions or statistical hypotheses are explicitly numbered. The following are **author-stated objectives**, not reconstructed hypotheses: build a structured dataset and taxonomy; classify attacks by target and bypassed defense layer; audit public benchmark coverage; characterize naming fragmentation, temporal evolution, and research concentration; and make extensible artifacts available for future benchmark design and tracking (p. 2).

The user's research question is separate from the paper's objectives. [D] This paper can inform why agentic capabilities introduce additional security failure modes: external data can become an instruction channel, tools can turn model decisions into side effects, and resource consumption can be an adversarial objective. It cannot directly answer how much more vulnerable agents are, under which matched defenses, or whether the difference persists after controlling for privileges, task complexity, and exposure. Those comparisons were not performed.

There are no experimental hypotheses about web browsing, no randomized agent-versus-model comparison, and no causal test of whether adding a browser increases attack success. These absences delimit the paper's relevance rather than undermine its actual taxonomy and audit objectives.

## 6. Assumptions / threat model

[A] The nominal scope is inference-time attacks: attacks executed through a deployed model's input interface without training-pipeline or weight access (§3.1, p. 3). Training-phase poisoning, backdoors, and weight manipulation are excluded from the main analysis. The extraction pipeline separately identified 414 training-phase attack types included in released data but excluded from the taxonomy and matrix analysis.

There is an explicit scope exception. Appendix A reports six leaves requiring white-box or hardware access: five require model-weight access and one physical hardware access. Appendix B retains internal-generation attacks because they occur during inference, while acknowledging that an input-interface-only definition would exclude several of them. Therefore, inference-time is partly a timing criterion and partly an access criterion, with a documented tension between them.

The four attacker objectives are Safety & Alignment Bypass, System & Tool Hijacking, Information Exfiltration, and Service Disruption. The key success boundary is operational: harmful text alone counts as Safety Bypass; an executed action or side effect counts as System Hijacking. The authors give calling a tool, writing a file, and running sandboxed code as examples. They associate the former with content filtering and the latter with access control and sandboxing (p. 16).

External data is lower privilege than system or user instructions under the Indirect Injection defense definition. An attack succeeds at that boundary when the model treats external content as authoritative. The paper does not specify a single universal deployment architecture, permission model, attacker query budget, or defender capacity. It argues that new service-disruption benchmarks should explicitly specify these quantities. [D] Thus its threat framework organizes many settings; it is not one fully instantiated attack experiment.

## 7. Methodology

### Corpus and extraction

[A] The corpus comprises 932 English arXiv papers covering H1 2023–H1 2026, where H1 is January–June and H2 July–December. The database indexes vulnerabilities across 803 LLM models; that is a database descriptor, not a claim that this study experimentally evaluated 803 models. Collection ended 10 April 2026 (Appendix J, p. 27), so the H1 2026 bin is not a complete six-month observation window.

Gemini 3.1 Pro, identifier gemini-3.1-pro-preview, performed extraction with temperature 0 and structured JSON output. Records contain attack name, description, example, novelty flag, and original source. The full extraction prompt excludes defenses, metrics, umbrella categories, non-attack components, training-phase attacks, unrelated systems, and non-adversarial failures. A concise retry prompt is used for timeout or truncation. The supplied paper does not report how many papers required retries, hardware, runtime, cost, or repeated-run variability.

### Normalization and matching

The pipeline extracted 6,366 mentions from 863 papers; 69 papers yielded no inference-time attacks. Names underwent case normalization, kebab-case conversion, removal of parenthetical abbreviations, alias merging, and deduplication. Over 50 manually curated variant clusters blocked inappropriate category-to-member merges, resolved ambiguous abbreviations, and preserved distinct techniques with shared names. The result was 2,521 unique attack groups, a reported 60.4% reduction.

Three matching tiers assigned groups: exact leaf lookup, 2.1%; SequenceMatcher fuzzy matching with cutoff 0.75, 2.7%; and semantic classification, 95.2%. The classification prompt asks for mechanism-based matching and permits NOT_AN_ATTACK and NO_LEAF_FITS. It uses the first 800 description characters, a compact leaf catalog, aliases, and optional fuzzy hints. The catalog had 505 leaves during classification; two were added afterward and manually assigned to matrix cells (pp. 25–26).

### Taxonomy and matrix construction

The authors, rather than the extraction model, made structural taxonomy decisions. They iteratively clustered adversarial objectives and defensive requirements. The final taxonomy has 507 leaves: 430 across five attack categories and 77 Attack Generation leaves. Of the 507, 401 contain at least one corpus attack and 106 are author-created placeholders documented elsewhere or derived from threat-model reasoning. These placeholders must not be interpreted as empirically observed corpus attacks.

Each leaf receives a target and technique assignment. The text reports 333 technique assignments inherited from taxonomy structure and 174 individually reviewed. A conflicting subtree breakdown is examined in §14 below. The taxonomy ultimately resolves 2,360 groups: 1,868 in five inference-time categories and 492 in Attack Generation. The remaining 161 are manually reviewed and dropped.

### Benchmark audit

The audit manually identifies each benchmark's evaluated methods, matches names and descriptions to leaves, looks up matrix assignments, and assigns full or partial coverage. Appendix D defines full as at least five methods or a dedicated suite, and partial as one to four methods outside the benchmark's focus. Agent benchmarks are mapped by mechanism and objective when named leaves are unavailable. The main three are HarmBench, InjecAgent, and AgentDojo; AdvBench, JailbreakBench, and StrongREJECT extend sensitivity analysis.

### Validation and statistics

The authors manually review novelty conflicts; evaluate 200 stratified semantic matches; double-code 115 samples; compare the same 200 attacks using Claude Opus 4.6; and inspect extraction in 13 papers. The accuracy interval uses the Wilson method. Cohen's kappa measures classification agreement. No training/test split, learned classifier training procedure, or new attack execution is reported. This is literature extraction and classification validation, not a benchmark leaderboard experiment.

## 8. Experiments / analyses

**X1 — Distribution analysis.** Purpose: identify concentration across the matrix. Data: 507 taxonomy leaves, including 106 unpopulated placeholders. Table 2 and §4.1 report 377 Safety Bypass leaves, 68 System Hijacking, 35 Information Exfiltration, and 27 Service Disruption. Safety Bypass comprises 74.4% of leaves. These are taxonomy counts, not measured deployment incidents.

**X2 — Naming fragmentation.** Purpose: measure instability in identifiers. GCG has 29 surface forms across 376 papers; AutoDAN has 11 across 259. Sixty catch-all leaves each absorb at least ten distinct techniques. The largest listed catch-all has 126 groups. The normalization process addresses aliasing but cannot establish that every distinct name is a distinct mechanism.

**X3 — Temporal analysis.** Purpose: characterize field growth and novelty. Figure 1 uses target-assigned unique groups; Table 7 uses paper counts, attack mentions, and novel mentions. The caption reports Safety Bypass declining from 92% to 74% between H2 2023 and H1 2026, and System Hijacking increasing from 5% to 16%. Table 7's total novelty rate is 18.4%. These denominators differ and must remain distinct. Recall and collection-window biases qualify maturation claims.

**X4 — Coverage audit and sensitivity.** Purpose: locate public evaluation gaps. HarmBench contributes four Safety Bypass cells, including two partial cells. InjecAgent and AgentDojo each cover the same two Indirect Injection cells for hijacking and exfiltration. Their union is six cells. Excluding partial cells leaves four. Adding three benchmarks adds no cells. Approximate leaf-weighted coverage is 80%, illustrating how concentrated research can produce high leaf coverage despite low cell coverage.

**X5 — Proposed benchmark design.** Appendix E applies four steps to Service Disruption × Instructional: choose the cell, enumerate leaves, assemble published evidence, and identify metrics. It reports 13 leaves, 37 groups, 25 papers, and 36.0% novelty. No new attacks are executed. Four source studies supply examples, and the result is a proposed specification rather than a validated new benchmark.

**X6 — Human classification evaluation.** Two experts assess 200 Tier 3 matches, stratified as 100 Jailbreaking, 35 Attack Generation, 25 Prompt Injection, 15 Information Disclosure, 15 Service Disruption, and 10 Decoding Manipulation. Accuracy is 184/200 = 92.0%, Wilson 95% confidence interval [87.4%, 95.0%]; population-reweighted accuracy is 92.3%. Among 16 errors, 12 are within-category, two cross-category, and two forced classifications. Information Disclosure has 73.3% accuracy with n = 15; Service Disruption and Decoding Manipulation reach 100% in their small strata.

**X7 — Annotator agreement.** On 115 independently annotated samples, pre-reconciliation leaf agreement is 70.4%, kappa 0.70; matrix-cell agreement is 86.1%, kappa 0.84. Of 34 leaf disagreements, 18 preserve the same cell and 16 cross cells; nine of those preserve the target row and seven cross rows. Post-reconciliation cell agreement is 103/115 = 89.6%. Reconciled agreement is not independent agreement and should not replace the original figure.

**X8 — Cross-model comparison.** Claude Opus 4.6 reclassifies the same 200 attacks using the same prompt. Agreement with Gemini is 94.5% for target row, 80.5% for matrix cell, and 63.0% for leaf. Of 74 leaf disagreements, 35 preserve the cell. Of 39 cross-cell disagreements, 28 preserve the target and 11 change it. Six attacks lie specifically on the Safety Bypass/System Hijacking boundary. This assesses model sensitivity, not accuracy against an independent truth standard.

**X9 — Extraction recall.** An expert reviews 13 papers: five blind extractions and eight anchored checks; three deliberately low-extraction papers test catastrophic misses. Excluding bare citation-only mentions, precision is 76/76 = 100% and recall 76/85 = 89.4%. Nine missed attacks are described as lesser-known. Five of 76 extracted attacks, 6.6%, are separately misclassified. The small, mixed-protocol sample limits generalization.

**X10 — Novelty and provenance checks.** Seventy-six conflicts or suspicious claims are manually reviewed; 33 false-novel group claims are corrected and 16 cases are confirmed as distinct methods sharing a key. The main text retains 1,133 novel groups as an upper bound. Appendix J separately checks 100 source attributions: 72% correct, 14% ambiguous, and 14% misattributed. Novelty validity and original-source accuracy are different measurements.

**X11 — Corpus representativeness.** An independent survey cites 102 arXiv papers, of which 26 meet the database's stated attack scope; eight are in the corpus, 30.8%. The authors say the techniques in the other 18 appear through citing papers. This supports some technique coverage despite paper omissions, but does not prove exhaustive literature coverage.

## 9. Results

[A] **Coverage is structurally narrow.** The maximum union is 6/24 cells, 25%; full-only coverage is 4/24. [C] The latter is approximately 16.7%, calculated as 4 ÷ 24 × 100. Eighteen cells remain uncovered when partial cells count. These fractions measure the authors' grid, not the fraction of real-world risk.

[A] **Service Disruption and Model Internals are absent from the six-benchmark mapping.** The former is a row with 27 leaves; the latter a column with 33. Published examples include up to 46× token amplification across nine reasoning models with answers correct, 100× latency and throughput falling to 1% at five requests per minute, and 96% attack success through logit suppression on AdvBench behaviors where GCG reaches 69%. These are results reported from other papers, not reproduced here. The 96% and 69% comparison is described as using the same behaviors, but full experimental controls are unavailable in this audit paper.

[A] **Indirect Injection concentrates in agent-action targets.** Table 2 assigns 45 of 49 leaves to System Hijacking and four to Service Disruption. [C] The hijacking proportion is 45 ÷ 49 × 100 ≈ 91.8%. This supports a relationship between external instructions and agentic action, without measuring comparative vulnerability.

[A] **The field emphasizes Safety Bypass.** It accounts for 377/507 leaves, 74.4%, and 83.8% of mapped mentions in §4.3. The discussion rounds mention concentration to 84%. Figure 1's ending 74% refers to a time-specific share of unique groups, a third quantity.

[A] **Classification is more stable at broad levels.** Human matrix-cell agreement exceeds leaf agreement; cross-model agreement drops from 94.5% at target level to 80.5% at cell level and 63.0% at leaf level. Thus confidence in broad concentration patterns is stronger than confidence in every fine-grained leaf label.

[A] **Novelty estimates require qualification.** The paper reports 1,133 retained novel groups, 1,173 novel mentions in Table 7, and an apparent rate near 18%. Group and mention totals are not directly comparable. Limited recall for unfamiliar attacks and uncertain single-paper novelty claims prevent treating the rate as a precise measure of field maturation.

## 10. Figure-by-figure interpretation

### Figure 1 — Target-category growth and changing shares, p. 6

[B] This is a two-panel stacked area chart. Panel (a), Absolute counts, places half-year periods H1 2023 through H1 2026 on the horizontal axis and unique attack groups on the vertical axis. The vertical scale is linear, with labeled increments reaching 1,000. Panel (b), Proportional share, uses the same periods and a linear percentage scale reaching 100. The shared legend uses blue for Safety & Alignment Bypass, salmon/red for System & Tool Hijacking, orange for Information Exfiltration, and green for Service Disruption. No error bars, confidence bands, or significance markers are shown.

The absolute stack rises across time; the blue region remains largest while other regions expand. In the proportional panel, blue narrows and the other colors widen. [A] The caption supplies exact textual endpoints: Safety Bypass falls from 92% to 74% between H2 2023 and H1 2026; System Hijacking rises from 5% to 16%. The graph does not label every period's category count, so exact intermediate values cannot be recovered confidently from the image. No pixel-derived numerical estimates are used here.

The caption qualifies target assignments as pipeline-dependent and cites 94.5% cross-model target-row agreement. Figure 1 supports diversification within the collected literature. It does not establish attack prevalence in deployed agents, and H1 2026 is collection-truncated at 10 April. Its unique-group shares must not be substituted for Table 7's mention-level novelty rates.

### Figure 2 — Hierarchical attack taxonomy, p. 15

[B] This is a left-to-right tree. The root Inference Time branches into Jailbreaking (316), Prompt Injection (47), Information Disclosure (35), Service Disruption (26), and Decoding Manipulation (6). Connecting lines indicate hierarchical membership, not causal influence, execution order, or data flow. The Attack Generation category is absent from this five-category diagram, although present in the complete 507-leaf taxonomy.

Jailbreaking branches into Deceptive & Psychological (79), Obfuscation & Evasion (79), Multi-Modal Jailbreaking (48), and Other (110). Prompt Injection branches into Agentic & Tool-Based (19), Data Source Vectors (15), Multi-Modal Indirect (8), and Other (5). Information Disclosure branches into Data Exfiltration (11), Probing & Reconnaissance (9), System Prompt Extraction (7), and Other (8). Service Disruption branches into Denial of Service (19), Functional Degradation (6), and Watermarking Attacks (1).

The Decoding Manipulation branch lists Refusal Subspace Ablation, Activation Steering (3), Enforced Decoding, Controllable Decoding, MoE Routing Manipulation, and LLM Router Manipulation. The parent count is six, while interpreting all displayed children as independent counted leaves and taking Activation Steering's parenthetical three literally does not yield an obvious reconciliation. Appendix B also describes six manipulation types. The visual is therefore useful for conceptual structure, but its final branch's count semantics remain uncertain.

## 11. Table-by-table interpretation

### Table 1 — Category distribution, p. 4

The columns are Leaves, Mentions, Unique groups, Papers, Novel, and Novelty %. The rows read: Jailbreaking 316 / 2,869 / 1,350 / 712 / 628 / 21.9%; Prompt Injection 47 / 472 / 267 / 192 / 148 / 31.4%; Information Disclosure 35 / 101 / 84 / 55 / 40 / 39.6%; Decoding Manipulation 6 / 82 / 62 / 44 / 34 / 41.5%; Service Disruption 26 / 134 / 103 / 49 / 46 / 34.3%. The five-category subtotal is 430 leaves, 3,658 mentions, 896 novel mentions, and 24.5%; unique and paper subtotals are dashes. Attack Generation has 77 / 2,465 / 492 / 606 / 270 / 11.0%.

The footnote calls Attack Generation orthogonal: it describes discovery methods. Novelty percentages use mention denominators; for example, 46/134 corresponds to 34.3%. Jailbreaking dominates counts, but Decoding Manipulation has the highest listed novelty percentage. The caption's stated comparison range of 11.0–31.4% for other categories conflicts with Information Disclosure's 39.6% and Decoding Manipulation's 41.5%. There are no inferential comparisons, confidence intervals, or significance tests in this table.

### Table 2 — Leaf counts by target and technique, p. 5

Column order is Instructional, Persuasion, Obfuscation, Cross-Modal, Indirect Injection, Model Internals. Safety Bypass has 78, 108, 125, 53, compound-empty, 13; total 377. System Hijacking has 9, 4, 2, 8, 45, corpus-gap; total 68. Information Exfiltration has 10, 8, 4, compound-empty, corpus-gap, 13; total 35. Service Disruption has 13, 2, 1, corpus-gap, 4, 7; total 27. Column totals are 110, 122, 132, 61, 49, 33; grand total 507.

Bullets denote coherent corpus gaps; diamonds denote empty cells requiring compound attacks across two defenses. Empty does not mean impossible or benchmark-covered. The three corpus-gap cells are Exfiltration × Indirect Injection, Service Disruption × Cross-Modal, and Hijacking × Model Internals. The two compound-empty cells are Safety Bypass × Indirect Injection and Exfiltration × Cross-Modal. Table 2's leaves include placeholders and generation-method leaves; it is not a count of empirically confirmed attack incidents.

### Table 3 — Primary benchmark coverage, p. 7

HarmBench occupies Safety Bypass × Instructional and Cross-Modal partially, and Safety Bypass × Persuasion and Obfuscation fully. InjecAgent and AgentDojo both occupy Hijacking × Indirect Injection and Exfiltration × Indirect Injection. Dashes indicate no mapped evaluation. The union is six cells; removing two partial cells leaves four. Importantly, InjecAgent and AgentDojo share cells, contradicting a literal claim that all three benchmarks have zero overlap. HarmBench is disjoint from the two agent benchmarks under this table.

### Table 4 — Largest catch-all leaves by novel groups, p. 18

Novel/total counts are adversarial image perturbations 40/126; iterative LLM refinement 40/57; reinforcement-learning attack generation 35/56; GCG attack 27/67; activation steering 20/30; evolutionary LLM generation 17/25. Image perturbation and iterative refinement tie for the highest listed novel count, while image perturbation has the largest total. Proposed splits distinguish mechanisms such as gradient-based versus diffusion/image patches/typography; feedback-driven versus prompt tuning/genetic refinement; and token-level versus attention-aware GCG variants.

These are granularity proposals, not tested improvements. The prose argues that splits mostly remain within covered cells; a possible steering redistribution would enter an already-uncovered Service Disruption × Model Internals cell. The six-cell coverage union therefore remains unchanged under these particular proposals.

### Table 5 — Extended benchmark mapping, p. 20

This table states the target, technique, coverage level, and grounding methods for all six benchmarks. HarmBench's Obfuscation grounding lists ten gradient/evolutionary methods and its Persuasion grounding five methods. Instructional lists Direct Request, Zero-Shot, and Stochastic Few-Shot, three of 18; Cross-Modal lists two methods and 110 dedicated behaviors but is labeled partial. The mapping's method counts should not be added into a reconciled unique total without overlap rules.

InjecAgent's Direct Harm combines 30 attacker cases with 17 user cases; Data Stealing combines 32 with 17. [C] These yield 510 + 544 = 1,054 cases. AgentDojo lists four environments, five injection phrasings, and 629 cases, with exfiltration tasks in Workspace/Banking. AdvBench maps GCG on 520 harmful behaviors to Obfuscation. JailbreakBench maps GCG on 100 behaviors fully to Obfuscation and PAIR partly to Persuasion. StrongREJECT maps Obfuscation and Persuasion partly among 17 methods. None adds a new cell.

### Table 6 — Evidence for a proposed disruption benchmark, p. 21

Four rows assemble prior results. OverThink uses nine frontier reasoning models and reports 46× token amplification with correct answers. ThinkTrap concerns black-box services, 100× latency, and throughput at 1% at five requests/minute. BenchOverflow reports token overflow via plain-text prompts across multiple LLMs without a single numerical effect in this table. CatAttack concerns DeepSeek R1, o1, and o3-mini: 3× error rate and 42% of queries exceeding 1.5× token budget. Required metrics are token amplification, latency/throughput, token count, and answer correctness/token budget. These studies are evidence assembled for a specification; no common experimental baseline or pooled effect is established.

### Table 7 — Temporal corpus counts, p. 22

Rows list period: papers / mentions / novel mentions / novelty percentage. H1 2023: 3 / 21 / 11 / 52.4%; H2 2023: 42 / 253 / 68 / 26.9%; H1 2024: 74 / 528 / 101 / 19.1%; H2 2024: 120 / 969 / 142 / 14.7%; H1 2025: 183 / 1,397 / 235 / 16.8%; H2 2025: 182 / 1,446 / 259 / 17.9%; H1 2026: 259 / 1,752 / 357 / 20.4%. Totals are 863 / 6,366 / 1,173 / 18.4%.

The 863 papers are attack-bearing papers, whereas the corpus contains 932 overall. H1 2023 has the highest displayed rate, so the prose's description of a 26.9% H2 2023 spike needs qualification. The caption reports 42 false-novel mention corrections, while the text reports 33 corrected group claims; a group-to-mention accounting link is not supplied.

### Unnumbered substantive tables

On p. 21, a leaf list groups 13 Instructional disruption leaves into computational exhaustion, functional degradation, and resource/safeguard exploitation. A metric table proposes token amplification, wall-clock latency, API cost, answer correctness, and throughput under load. On p. 23, agreement tables report human leaf/cell agreement and cross-model row/cell/leaf agreement, detailed in X7–X8. These p. 23 tables were inspected through text only. None reports significance testing.

## 12. Diagram / architecture interpretation

Figure 2 is a hierarchy rather than a software architecture. There is no supplied component-level deployment diagram, control-flow graph, or browser-agent execution trace. Its branches answer which category contains which subcategory.

[A] The methodology nevertheless describes a processing sequence: paper texts → structured attack mentions → normalized name groups → direct/fuzzy/semantic classification → taxonomy leaves → target–technique assignments → distribution statistics. Human review supplies alias rules, taxonomy design, sampled validation, novelty correction, and exclusion review. This sequence is a prose reconstruction of the reported method, not an additional figure.

The benchmark-audit path is distinct: benchmark documentation → evaluated methods → mechanism/leaf match → matrix cell → full/partial coverage. The authors emphasize manual documentation review, making the audit less directly dependent on extraction recall than corpus-frequency analyses. [D] It still depends on the constructed taxonomy, defense-layer definitions, and manual mapping judgments.

The design walkthrough is cell selection → leaf enumeration → published evidence assembly → metric identification. Its output is a specification. There is no feedback-loop experiment demonstrating that this specification improves detection or production security.

## 13. Equations and mathematical concepts

The sole explicit central formalization is **A = (T, M)** in Appendix A, p. 15. A is an attack represented as an ordered pair; T is target objective and M mechanism/technique. This is a categorical representation, not a numerical model, loss function, optimization objective, or success-probability equation. A leaf's pair determines its cell in the 4 × 6 matrix.

[C] The cell denominator is 4 × 6 = 24. The reported maximum coverage is 6/24 × 100 = 25%; full-only coverage is 4/24 × 100 ≈ 16.7%. Uncovered cells are 24 − 6 = 18. Equal weighting is a modeling choice: a cell with few leaves has the same coverage weight as one with many.

[C] The union of the Service Disruption row and Model Internals column contains 6 + 4 − 1 = 9 cells, subtracting their shared intersection once. Selecting Service Disruption × Instructional leaves eight other cells in that union, explaining Appendix E's continuation on p. 22.

Accuracy is correct classifications divided by reviewed classifications: 184/200 = 92.0%. Extraction recall is recovered eligible attacks divided by all eligible attacks found by the reviewer: 76/85 = 89.4%. Extraction precision is correct extractions divided by reviewed extractions: 76/76 = 100%. These evaluate different stages. The paper reports Wilson intervals and Cohen's kappa without giving their equations; no missing mathematical derivation is silently supplied here.

Ratios such as 46× token amplification and 100× latency describe multiplicative increases relative to their source-study conditions. The audit paper does not provide every baseline token count, latency, or budget needed to reconstruct absolute costs.

## 14. Interpretation and discussion

The strongest supported conclusion is that the six audited public benchmarks do not span the authors' operational threat grid. This supports differentiated evaluation infrastructure: harmful-output checks, action authorization checks, resource measurements, and internal-access experiments answer different questions. It does not establish that all uncovered cells have equal severity or prevalence.

For web-agent research, [D] the paper links vulnerability mechanisms to capability. External pages, files, and tool outputs can carry instructions; agent actions can make trust-boundary failures consequential through execution or exfiltration. Yet the paper provides no matched standalone baseline. The justified conclusion is an expanded set of security obligations, not a measured universal ranking of vulnerability.

Several source inconsistencies require explicit preservation:

- **Overlap:** pp. 2 and 7 claim zero overlapping cells among the primary benchmarks, but Table 3 and Table 5 put both InjecAgent and AgentDojo in the same two cells. The narrower statement that HarmBench's region is disjoint from the agent benchmarks is supported. The broader zero-overlap wording is not.
- **Coverage range:** §7, p. 9, says at most 25–30%, whereas the principal tables and sensitivity analysis support at most 25%, falling to 4/24 when partial coverage is excluded. No supplied calculation explains 30%.
- **Highest novelty:** Table 1's caption contrasts Service Disruption's 34.3% with 11.0–31.4% elsewhere, and the conclusion calls it the highest novelty rate. Table 1 instead reports 39.6% for Information Disclosure and 41.5% for Decoding Manipulation.
- **Manual-assignment breakdown:** pp. 15–16 list 38 infrastructure/reasoning, 36 execution/agency, 35 disclosure, 26 disruption, 6 decoding, and 77 generation leaves for the remaining 174 assignments. [C] These sum to 38 + 36 + 35 + 26 + 6 + 77 = 218, not 174. The text does not explain overlap or reconcile this.
- **Category totals:** Table 1 reports 3,658 attack-category mentions plus 2,465 generation mentions. [C] Their sum is 6,123, leaving 6,366 − 6,123 = 243 mentions outside that displayed total. Dropped entries may be relevant, but the paper supplies no explicit mention-level reconciliation, so that explanation remains unconfirmed.
- **Temporal phrasing:** H1 2023 has 52.4% novelty in Table 7, exceeding H2 2023's 26.9% described as a spike. Small initial sample size is visible, but an exclusion rule is not stated.
- **Indirect Injection proportions:** Table 2 gives 45/49, approximately 91.8%, while Appendix G's Gemini robustness comparison gives 96%. The latter occurs in the 200-sample comparison context and may use a different denominator; it should not replace the full-taxonomy fraction.
- **Emerging categories:** §4.3 says no benchmark covers emerging agentic categories, whereas Table 3 covers hijacking and exfiltration through Indirect Injection. A claim of incomplete coverage is supportable; literal absence across these categories is not.
- **Internal-access boundary:** the nominal input-interface-only definition conflicts with retained white-box leaves, a tension explicitly acknowledged by the authors.

These issues affect precision of reporting and some rhetoric. They do not erase the directly visible empty Service Disruption row and Model Internals column in the supplied benchmark tables.

## 15. Contributions and novelty

[A] **Conceptual:** distinguish benchmark-internal adequacy from collective threat-surface coverage; separate a literature-oriented hierarchy from an operational target–mechanism view.

[A] **Methodological:** combine automated extraction with curated alias rules, hierarchical matching, targeted human review, and manual benchmark mapping; define output-versus-execution and bypassed-defense rules.

[A] **Dataset:** supply 6,366 mention records, a 507-leaf taxonomy, 932-paper manifest, novelty and matching metadata, and source links. The contribution includes 106 unpopulated placeholders as prospective coverage categories, rather than pretending all leaves were observed.

[A] **Empirical:** quantify naming fragmentation, research concentration, temporal changes, and classification uncertainty. **Benchmark-design:** provide a reusable grid and a worked disruption-benchmark specification. This is not a newly executed attack benchmark, a new defense, a new exploitation algorithm, or a theorem.

[A] **Implementation and availability:** the authors report six HuggingFace artifacts with Croissant metadata, CC-BY-4.0 licensing for data and taxonomy, and MIT licensing for pipeline code. Availability is author-reported; files, licenses, and executability were not independently checked.

## 16. Limitations

### Authors' stated limitations

The same Gemini model extracts and classifies, permitting correlated blind spots. Recall favors familiar attacks; apparent novelty stabilization may partly reflect extraction bias. Corpus scope is English arXiv work from one database with unpublished formal inclusion criteria. Only eight of 26 in-scope papers in an independent survey are directly present. Recent papers are overrepresented: the full corpus has 305 papers in H1 2026 versus three in H1 2023, while Table 7's attack-bearing H1 2026 subset is 259.

Only six public benchmarks are audited; proprietary/custom suites may cover more. The taxonomy categories and matrix dimensions are design choices rather than natural kinds. Single-cell assignment loses nuance for multi-mechanism attacks. Catch-all leaves combine diverse techniques. The 2,521 groups are a lower bound on produced identifiers, not a reliable count of distinct mechanisms. Novel status is an upper bound because unsupported single-paper novelty assertions can escape contradiction checks. White-box internal attacks stretch the input-interface definition. Source attributions are approximate, with 14% misattribution in the spot-check. The dataset is an early-2026 snapshot.

### Additional evidence-based analyst observations

[D] Agreement deteriorates at finer granularity, limiting exact leaf-level claims. The recall study mixes blind and anchored review and uses only 13 papers. Tail-category accuracy estimates have small denominators. Cross-model agreement does not establish either model's correctness. Equal cell weighting is useful for structural coverage but not calibrated risk. Manual benchmark mapping is independent of extraction operations, but not of taxonomy concepts and judgment. The paper's own overlap and count inconsistencies reduce confidence in unqualified headline wording.

[D] The full/partial rule has an unresolved application issue: Cross-Modal HarmBench coverage is partial despite Table 5 mentioning 110 dedicated behaviors, while the rule allows a dedicated suite to count as full. A dedicated behavior subset may differ from a dedicated suite, but the supplied text does not fully specify this distinction. No independent mapping-agreement study or sensitivity to all plausible column assignments is reported.

## 17. Threats to validity

The following validity labels are analyst organization, not headings the authors systematically apply.

**Construct validity [D]:** coverage is operationalized as occupied target–technique cells. Occupancy does not measure completeness within a cell, attack severity, ecological frequency, or defense quality. The distinction between discovery methods and payload mechanisms requires careful mapping. Placeholder leaves mix observed and prospective coverage.

**Internal validity [D]:** extraction, alias merging, forced matching, and manual assignment can introduce classification error. Shared-model dependence can correlate stages. The audit's manual path reduces direct dependence on missed literature mentions, but cannot make conceptual boundary judgments error-free.

**External validity [D]:** English arXiv coverage from one database, incomplete H1 2026 collection, and six public evaluations restrict generalization to the broader literature and proprietary testing. No direct deployment sample establishes real-world incidence or economic loss.

**Statistical conclusion validity [D]:** the Wilson interval describes the 200-item classification sample under its sampling assumptions. It is not a confidence interval for benchmark coverage or attack prevalence. Small strata, purposeful recall sampling, and uncertain novelty labels limit population-level interpretation. No significance tests establish temporal causal trends.

**Ecological validity [D]:** attack results assembled from other papers use heterogeneous systems and access assumptions. A white-box internal manipulation and an attacker-controlled web page are not interchangeable operational threats. Resource metrics need attacker-budget and defender-capacity conditions.

**Reproducibility [D]:** supplied prompts, model identifier, temperature, matching cutoff, and dataset fields aid reconstruction. Uninspected artifacts, unreported retry counts, model-service dependence, and source-attribution error prevent claiming this review has reproduced the pipeline.

## 18. Future work and open questions

### A. Explicitly proposed by the authors

Develop benchmarks for uncovered cells, beginning with Service Disruption; use standardized attack identifiers; extend collection beyond English and arXiv; refine catch-all leaves; maintain and extend the taxonomy; and map new benchmarks into the same framework over time. The disruption specification calls for token, latency, cost, throughput, and correctness measurements, with explicit attacker budgets and defender capacities. Internal-mechanism evaluation requires infrastructure for the relevant model access.

### B. Additional open questions

[D] For the user's research program, the major unanswered question is comparative: under matched model, task, attacker access, and defenses, what changes when external browsing and tools are enabled? Other unresolved questions are how privileges alter consequences; how compound attacks should occupy multiple cells; whether different evaluators agree on benchmark mapping; whether realistic severity weights change priorities; and whether stronger extraction of unfamiliar attacks changes novelty trends.

[D] A useful future comparison would separate harmful text, unauthorized side effects, data leakage, and resource costs rather than combine them into one vulnerability score. This is an analyst-proposed design implication, not an experiment performed by the paper.

## 19. Terminology and notation glossary

| Term | Meaning in this paper |
|---|---|
| LLM | Large language model. |
| Inference-time attack | Attack during deployment; nominally through inputs, with acknowledged internal-access exceptions. |
| Agentic capability | Ability to use tools or take actions, relevant to external-instruction attacks. |
| Jailbreaking | Inducing harmful output by bypassing safety alignment. |
| Indirect Injection | External-data instructions crossing a privilege/trust boundary. |
| Safety Bypass | Objective satisfied by harmful model output. |
| System Hijacking | Objective requiring action or a side effect. |
| Information Exfiltration | Target objective of unauthorized information release. |
| Service Disruption | Degrading availability, performance, or task usefulness. |
| Denial-of-wallet | Resource/cost abuse against the service or its payer. |
| Model Internals | Mechanisms involving internal representations, architecture, decoding, or related channels. |
| White-box access | Access to model internals beyond ordinary input/output interaction. |
| Taxonomy leaf | Terminal category; not necessarily one unique attack or one observed instance. |
| Attack mention | One extracted paper-level record. |
| Unique attack group | Normalized grouping of names; not guaranteed to equal one distinct mechanism. |
| Catch-all | Leaf absorbing at least ten distinct techniques. |
| GCG | Greedy Coordinate Gradient, an attack-discovery method. |
| RLHF | Reinforcement learning from human feedback; named in the alignment-related technique definition. |
| ASR | Attack success rate. |
| RAG | Retrieval-augmented generation, invoked in the poisoned-document example. |
| API | Application programming interface. |
| MoE | Mixture of experts, used in routing-manipulation descriptions. |
| MCP | Model Context Protocol, named for a tool-related injection category. |
| H1 / H2 | January–June / July–December. |
| A = (T, M) | Attack represented by target T and mechanism M. |
| Kappa, κ | Agreement statistic reported alongside raw agreement. |
| Corpus gap / compound cell | Empty coherent category / category requiring two defense bypasses. |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Corpus | 932 | papers | English arXiv, H1 2023–H1 2026 | Author-reported | pp. 2–3 |
| Attack-bearing subset | 863 | papers | 69 yielded no eligible attacks | Author-reported | p. 3 |
| Raw extraction | 6,366 | mentions | Before group normalization | Author-reported | p. 3 |
| Normalized groups | 2,521 | groups | 60.4% reported reduction | Author-reported | p. 3 |
| Matched / dropped groups | 2,360 / 161 | groups | After manual exclusion review | Author-reported | pp. 15, 26 |
| Taxonomy | 507 | leaves | 430 attack-category + 77 generation leaves | Author-reported | pp. 2–4 |
| Populated / placeholders | 401 / 106 | leaves | Observed versus author-created coverage | Author-reported | p. 3 |
| Matching tiers | 2.1 / 2.7 / 95.2 | percent | Exact / fuzzy / semantic | Author-reported | p. 3 |
| Semantic accuracy | 92.0 | percent | 184/200; CI 87.4–95.0 | Author-reported | pp. 3, 22 |
| Reweighted accuracy | 92.3 | percent | Population proportions | Author-reported | p. 22 |
| Human cell agreement | 86.1 | percent | 115 samples; κ = 0.84 | Author-reported, text-only | p. 23 |
| Cross-model agreement | 94.5 / 80.5 / 63.0 | percent | Target / cell / leaf; n = 200 | Author-reported, text-only | p. 23 |
| Extraction precision / recall | 100 / 89.4 | percent | 76/76 and 76/85; 13 papers | Author-reported, text-only | p. 24 |
| Maximum cell coverage | 6/24 = 25 | percent | Partial cells included | Author-reported | pp. 7, 19 |
| Full-only coverage | 4/24 ≈ 16.7 | percent | Partial cells excluded | Analyst-derived percentage | pp. 7, 19 |
| Leaf-weighted coverage | approximately 80 | percent | Leaves in covered cells | Author-reported | p. 19 |
| Safety Bypass leaves | 377/507 = 74.4 | percent | Taxonomy denominator | Author-reported | p. 5 |
| Indirect Injection hijacking share | 45/49 ≈ 91.8 | percent | Full Table 2 leaf counts | Analyst-derived percentage | p. 5 |
| GCG naming | 29 / 376 | forms / papers | Normalized corpus | Author-reported | p. 6 |
| AutoDAN naming | 11 / 259 | forms / papers | Normalized corpus | Author-reported | p. 6 |
| Retained novel groups | 1,133 | groups | Upper bound | Author-reported | p. 3 |
| Novel mentions | 1,173; 18.4 | mentions; percent | Table 7 total | Visually readable | p. 22 |
| OverThink amplification | up to 46× | token ratio | Nine reasoning models; correctness retained | Author-reported prior result | p. 18 |
| ThinkTrap latency | 100× | latency ratio | Throughput 1% at 5 requests/min | Author-reported prior result | p. 18 |
| CatAttack | 3×; 42% | error ratio; queries | Queries exceeding 1.5× token budget | Author-reported prior result | pp. 18, 21 |
| Logit suppression / GCG | 96 / 69 | percent ASR | Same AdvBench behaviors, as reported | Author-reported prior result | pp. 7, 19 |
| Attribution quality | 72 / 14 / 14 | percent | Correct / ambiguous / wrong; n = 100 | Author-reported, text-only | p. 27 |

Additional supplied prior-study results on pp. 18–19 are: steering reduces Vicuna-7B refusal from 82% to 2% on AdvBench and raises toxic generation from 3% to 83% on ToxiGen, with scaling to Llama2-70B; directional intervention reports 97.88% ASR on AdvBench and 95% on HarmBench across seven models; routing attacks report 88–100% rerouting on open-source routers, 79–91% on Unify, and costs up to 8× on OpenRouter. These heterogeneous results establish examples of consequential mechanisms, not a pooled estimate or experiments reproduced by this paper.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Analysis | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| A reusable framework organizes collective coverage | Four targets, six mechanisms, leaf mapping | Table 2; method | pp. 4–5 | HIGH for definition; framework-dependent |
| Public evaluation covers at most six cells | Explicit benchmark assignments | Tables 3, 5; X4 | pp. 7, 20 | HIGH for supplied mapping; partial coverage included |
| Disruption and internal mechanisms lack mapped evaluation | Empty row and column | Tables 3, 5 | pp. 7, 20 | HIGH within six audited benchmarks |
| All three benchmarks have zero overlap | Prose assertion, contradicted by shared I/A cells | Table 3 | p. 7 | LOW as literal general claim |
| Agentic action changes success criteria | Output-versus-execution rule | Appendix A | p. 16 | HIGH author definition; no comparative effect size |
| External data is an injection channel | Web/files/API/tool descriptions | Appendix B | p. 17 | HIGH author statement |
| Classification uncertainty is granularity-dependent | 94.5/80.5/63.0% cross-model agreement | X8 | p. 23 | HIGH reported; agreement is not accuracy |
| Novelty trend is only apparent | Recall misses unfamiliar attacks | X9; Appendix G | p. 24 | HIGH acknowledged caveat |
| Naming is fragmented | GCG 29 forms; AutoDAN 11 | X2 | p. 6 | HIGH corpus observation |
| Resource attacks need additional metrics | Published amplification/degradation and proposed metrics | Table 6; X5 | pp. 20–21 | MEDIUM specification; not evaluated anew |
| Web agents have additional failure channels | External instructions plus action side effects | Analyst synthesis | pp. 16–17 | MEDIUM interpretation; no direct standalone comparison |

## 22. Very simple explanation — Explain Like I'm 15

Imagine that AI security tests are a school exam. Most questions ask whether an AI can be tricked into saying something dangerous. This paper says an exam should also ask whether the AI can be tricked into using tools improperly, leaking information, or wasting huge amounts of time and money. The researchers make a 24-box checklist and find that six public testing systems together reach only six boxes, counting some partial coverage.

A web agent can read a page written by someone other than its user. If it mistakes instructions on that page for authorized commands, and it also has tools, the mistake can lead to an action. The paper separates saying harmful text from actually calling a tool or writing a file. That distinction helps explain why an agent needs security checks beyond a chatbot's harmful-answer tests.

However, this paper does not run the same AI with and without web access and show which is attacked more successfully. It supports the explanation that agents introduce additional channels and consequences. It does not prove a universal numerical claim that agents are more vulnerable.

The checklist also has limits. The researchers' categories involve judgment, their automatic reader misses some unfamiliar attacks, and a few headline statements conflict with their tables. The useful lesson is to ask exactly what a security evaluation tests, what it leaves out, and which attacker permissions its results assume.

## Completeness Audit

The audit below compares this explanation with the inventory of the supplied 27-page work. Fully represented means the substantive component is explained, not reproduced word for word. Repetitive examples, bibliography details, and complete prompt wording are compressed explicitly.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, abstract, preprint identity | Yes, text and image p. 1 | Yes | Fully represented | §1; headline claims qualified |
| §1 Introduction and contributions | Yes, image p. 1; text p. 2 | Yes | Represented in compressed form | §§1, 4–5, 15 |
| §2.1 Corpus and Extraction | Yes, text pp. 2–3 | Yes | Fully represented | Source, dates, model, settings, exclusions |
| §2.2 Normalization and classification | Yes, text p. 3 | Yes | Fully represented | Tier rates, cutoff, alias rules |
| §2.3 Validation | Yes, text p. 3 | Yes | Fully represented | Cross-linked to Appendix G |
| §3.1 Scope and taxonomy | Yes, text p. 3; image p. 4 | Yes | Fully represented | Placeholders and access tension retained |
| §3.2 Target × Technique | Yes, images pp. 4–5 | Yes | Fully represented | Distinct axes, definitions, worked example |
| §3.3 Released artifacts | Yes, image p. 5 | Yes | Represented in compressed form | Availability author-reported |
| §4.1 Distribution | Yes, images pp. 5–6 | Yes | Fully represented | Counts and denominators retained |
| §4.2 Naming | Yes, image p. 6 | Yes | Fully represented | Alias and catch-all observations |
| §4.3 Temporal evolution | Yes, image p. 6 | Yes | Fully represented | Recall and window caveats |
| §4.4 Benchmark audit | Yes, image p. 7 | Yes | Fully represented | Overlap contradiction disclosed |
| §5 Discussion: concentration, design, naming | Yes, image p. 8 | Yes | Represented in compressed form | §§14–15, 18 |
| §6 Pipeline and Scope limitations | Yes, image p. 8; text p. 9 | Yes | Fully represented | §§16–17 |
| §7 Related Work | Yes, text p. 9 | Yes | Represented in compressed form | Positioning summarized; no external validation |
| §8 Conclusion | Yes, text pp. 9–10 | Yes | Fully represented | Future directions and inconsistent wording noted |
| References | Yes, text pp. 10–13 | Partly | Represented in compressed form | Bibliographic entries not reproduced or verified |
| Appendix overview | Yes, image p. 14 | Yes | Fully represented | Roadmap and audit |
| Appendix A: taxonomy, assignments, definitions, empty cells | Yes, images pp. 15–16 | Yes | Fully represented | Assignment sum discrepancy disclosed |
| Appendix B: six category descriptions | Yes, images pp. 16–17 | Yes | Represented in compressed form | Core meanings and counts retained |
| Appendix C: catch-all analysis | Yes, images pp. 17–18 | Yes | Fully represented | Table 4 and split sensitivity |
| Appendix D: mapping, evidence, sensitivity, weighting | Yes, images pp. 18, 20; text p. 19 | Yes | Fully represented | Prior results distinguished from new experiments |
| Appendix E: four-step design walkthrough | Yes, images pp. 20–22 | Yes | Fully represented | Proposed specification; no new attacks |
| Appendix F: temporal distribution | Yes, image p. 22 | Yes | Fully represented | All Table 7 rows transcribed |
| Appendix G: novelty review | Yes, image p. 22 | Yes | Fully represented | Group/mention distinction preserved |
| Appendix G: human evaluation and agreement | Yes, image p. 22; text p. 23 | Yes | Fully represented | Independent/reconciled agreement separated |
| Appendix G: multi-model and structural robustness | Yes, text p. 23 | Yes | Represented in compressed form | Full agreement results; sample-specific patterns qualified |
| Appendix G: construction, sensitivity, recall, novelty confound | Yes, text pp. 23–24 | Yes | Fully represented | §§7–8, 14, 16 |
| Appendix H: full extraction prompt | Yes, text pp. 24–25 | Yes | Represented in compressed form | Fields, exclusions, novelty instructions; not executed |
| Appendix H: retry prompt | Yes, text p. 25 | Yes | Represented in compressed form | Timeout/truncation role; retry count absent |
| Appendix H: classification prompt | Yes, text pp. 25–26 | Yes | Fully represented | 505-to-507 change, 800-character input, reject options |
| Appendix I: unmatched attacks | Yes, text p. 26 | Yes | Represented in compressed form | 161 drops; borderline exclusions noted |
| Appendix J: datasheet | Yes, text pp. 26–27 | Yes | Fully represented | Provenance quality, uses, licenses, snapshot |
| Appendix K: ethics | Yes, text p. 27 | Yes | Represented in compressed form | Defensive catalog; no new attacks or exploit code |
| Figure 1a and 1b | Yes, visually p. 6 | Yes | Fully represented | Axes, colors, trends, exact caption values |
| Figure 2 | Yes, visually p. 15 | Yes | Fully represented | Hierarchy and decoding-count uncertainty |
| Tables 1–7 | Yes, visually on supplied pages | Yes | Fully represented | All table purposes and substantive values covered |
| Unnumbered leaf and metric tables | Yes, visually p. 21 | Yes | Represented in compressed form | Three subgroups and all metric concepts |
| Unnumbered agreement tables | Yes, text-only p. 23 | Yes | Fully represented | No visual-layout verification |
| Tuple A = (T, M) | Yes, visually p. 15 | Yes | Fully represented | §13 |
| Formal equations, theorems, algorithm blocks | None identified | Accounted for | Not present in supplied material | Prompts are not formal algorithms |
| Explicit research questions and hypotheses | None identified | Accounted for | Not present in supplied material | Objectives separated from user's question |
| X1–X11 analyses and validation checks | Yes | Yes | Fully represented | §8 register |
| Main contributions | Yes | Yes | Fully represented | §15 |
| Author-stated limitations | Yes | Yes | Fully represented | §16; distributed appendix caveats included |
| Released JSON, records, browser, code, statistics, manifest, codebook | No | Availability described | Inaccessible | Files not supplied |
| Referenced underlying attack studies and benchmark documentation | No independent inspection | Paper's accounts represented | Inaccessible as independent sources | No external verification requested |
| Supplied supplementary files | None | Accounted for | Not supplied | No claim of supplement inspection |

### Missing or inaccessible material

No numbered page is missing from the supplied text sequence. The unrendered pages were available only as extracted text. Released artifacts and underlying source studies were not available for independent inspection. This analysis therefore cannot verify code behavior, full leaf mappings, source citations, benchmark implementations, or original attack-study experimental controls. The complete leaf catalog appended at runtime to the classifier is not printed in the paper; only its format and release location are described.

### Uncertain interpretations

Unresolved issues include zero-overlap wording versus shared benchmark cells; the 25–30% phrase; the incorrect highest-novelty characterization; the 174-versus-218 assignment breakdown; the 243-mention gap in Table 1 totals; the group/mention correction accounting; the decoding branch's count semantics; and the exact operational threshold separating partial coverage from a dedicated suite. The paper's claim that source bias necessarily strengthens the gap finding is conditional. Fine plot coordinates are not used as exact data. No direct standalone-versus-web-agent vulnerability estimate is available.

### Deliberately compressed material

The bibliography is not reproduced. Category examples are grouped rather than individually paraphrased. Table 4's suggested sub-splits and Appendix E's 13 leaf identifiers are summarized by mechanism and subgroup. Prompt templates are described rather than quoted at length; their embedded instructions were treated as source evidence only. Appendix I's approximate breakdown of 41 novel-claim drops is compressed: about 15 umbrella terms, eight out-of-scope/training methods, five non-LLM targets, five metrics/frameworks, and eight borderline cases. Appendix K's position is compressed: the authors describe defensive cataloging, public inputs, no personally identifiable information, no new attacks or exploit code, and an acknowledged dual-use concern. Appendix G's structural robustness examples are summarized alongside full agreement statistics rather than all repeated percentages.

### Potential omissions

Every substantive inventory category has been represented or explicitly identified as compressed, text-only, unavailable, or uncertain. This is an inventory-based account of the supplied paper, not a claim that all facts in every underlying cited study or released artifact have been preserved. The primary unresolved research need is a controlled comparison of agents and standalone models; this paper's taxonomy explains relevant mechanisms but does not supply that experiment.
