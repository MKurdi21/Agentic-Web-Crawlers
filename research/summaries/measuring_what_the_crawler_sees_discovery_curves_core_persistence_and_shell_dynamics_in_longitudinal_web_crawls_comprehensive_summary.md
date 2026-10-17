## Stage 0 — Document Accessibility Report

The supplied work is accessible as extracted text for physical PDF pages 1–16 and as rendered page images for pages 1, 4, 9, 10, 11, 12, and 13. Those seven images were directly inspected; the other nine pages were reviewed through their supplied text only. No tools, browsing, additional files, or outside sources were used. The supplied contents were treated as evidence, not instructions.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: a 16-page supplied sequence containing the title, main text, conclusion, and references. |
| Page range | Physical PDF pages 1–16; printed numbering agrees on the supplied numbered pages. |
| Apparently missing pages | None within the supplied 1–16 sequence. This does not independently establish whether another version has additional material. |
| Visual coverage | Direct visual inspection of pages 1, 4, 9–13; text-only inspection of pages 2, 3, 5–8, 14–16. |
| Figures | All five numbered figures are visually available: Fig. 1 on p. 4 and Figs. 2–5 on pp. 9–12. Small legends and some tick labels are difficult to read confidently. |
| Tables | No substantive numbered tables appear in the supplied paper. |
| Equations | Equations (1)–(18) are available in extracted text. Several extraction artifacts affect grouping, superscripts, and symbols; mathematical reconstructions below are identified and checked against surrounding definitions. Pages containing the numbered equations were not supplied as rendered images. |
| Appendices | None appears in the supplied sequence. |
| Supplementary material | None supplied; no explicit supplementary-material reference is identifiable in the supplied text. |
| Other artifacts | Public statistics URLs and bibliography entries are present, but their linked contents were not inspected. |
| OCR | No separate OCR was performed. Native/extracted text was sufficient for prose, with equation-specific caveats. |
| Other limitations | Plot legends do not support confident transcription of every fitted parameter. Exact statistical uncertainty and implementation details are largely unreported in the supplied work. |

Evidence labels used throughout: [A] AUTHOR-REPORTED; [B] DIRECTLY OBSERVABLE in a supplied image; [C] ANALYST-DERIVED from stated operands; [D] ANALYST INTERPRETATION. No [E] external information is introduced. HIGH means clear supporting evidence for the stated, bounded claim; MEDIUM indicates interpretation or a material qualification; LOW indicates weak or incomplete evidence; UNKNOWN indicates that the supplied material cannot resolve the point. Confidence in accurately reporting an author's statement is distinct from confidence that the underlying scientific claim has been established.

Pre-narrative inventory and extraction record

The document is a mixed mathematical-method and observational web-measurement paper. Its inventory contains six main sections, twelve substantive numbered subsections, five figures with nine distinct visual panels/objects, eighteen numbered equations, four main empirical analyses, an additional asymptotic consistency diagnostic, an unnumbered interests disclosure, two substantive statistics footnotes, and 36 bibliography entries. No numbered theorem, lemma, algorithm, table, appendix, or supplement is present.

| Inventory ID | Original object and location | Principal extracted content |
|---|---|---|
| META | Title/authors, p. 1 | Measuring What the Crawler Sees: Discovery Curves, Core Persistence, and Shell Dynamics in Longitudinal Web Crawls; Michael Paris, Hande Çelikkanat, Luca Foppiano. |
| ABSTRACT | Abstract/keywords, p. 1 | Two observables of one sampling process; homogeneous-model disagreement; core/shell extension; residual shell heterogeneity. |
| S1 | §1 Introduction, pp. 1–2 | Operator-side measurement problem and contribution. |
| S2 | §2 Related Work, pp. 2–4 | Three strands: urn models, Common Crawl measurement, language-model training substrate. |
| SS2.1–SS2.3 | §§2.1–2.3, pp. 3–4 | Statistical precedents, published crawl metrics, downstream corpus context. |
| S3 | §3 Method, pp. 4–8 | Dynamic urn, containment, discovery formula, asymptotics, operator quantities, two components. |
| SS3.1–SS3.6 | §§3.1–3.6, pp. 4–8 | All six substantive methodological subsections. |
| E1–E18 | Equations (1)–(18), pp. 5–8 | Complete mathematical sequence represented in §13 below. |
| S4 | §4 Results, pp. 8–12 | Common Crawl discovery object, domain fits, German Academic Web check. |
| X1 / SS4.1 | §4.1, pp. 8–9; Fig. 2 | Rolling unique-count discovery trajectories and normalization. |
| X2 / SS4.2 | §4.2, pp. 9–10; Fig. 3 | Homogeneous fits disagree across containment and discovery. |
| X3 / SS4.2 | §4.2, pp. 10–11; Fig. 4 | Core/shell fits recover approximately common core share with residual shell-coverage disagreement. |
| X4 / SS4.3 | §4.3, pp. 10–12; Fig. 5 | German Academic Web single-trajectory cross-source check. |
| X5 | §3.4, p. 6 | Full-curve versus asymptotic homogeneous fit proposed as a consistency check; no separately quantified empirical result. |
| S5 | §5 Discussion, pp. 12–13 | Meaning of parameters, policy conjecture, dormancy ambiguity, rank-resolved future work. |
| S6 | §6 Conclusion, p. 13 | Operator-facing dictionary of coverage, churn, discovery, lifetime, sampled time, hidden time, core share. |
| F1–F5 | Figs. 1–5, pp. 4, 9–12 | Urn diagram and four two-panel empirical figures. |
| NOTES | Footnotes, pp. 3 and 8 | Statistics landing page and crawl-size plotting page; addresses only inspected. |
| DISCLOSURE | p. 13 | Authors report no competing interests. |
| REFERENCES | pp. 14–16 | 36 entries; inspected as supplied bibliography, not independently verified. |

The extraction ledger separates explicit aims from analyst-formulated questions, mathematical assumptions from empirical conclusions, and author limitations from additional observations. Its numerical and claim records are consolidated in §§20–21 and the structured claims accompanying this narrative. Source verification consisted of revisiting the supplied page text and available figure images while checking each major statement; it was not independent reproduction or source validation.

## 1. Plain-Language Orientation

[A; HIGH] This paper asks how much can be learned about a web crawler's behavior from the sequence of pages, hosts, or domains that it captures. A crawler sees only part of an evolving population. Some items reappear frequently; others are newly discovered, temporarily missed, or no longer observed. A large crawl count alone does not explain these differences. The paper turns repeated crawl observations into a small set of interpretable sampling parameters. Sources: pp. 1–2, 12–13.

The researchers use two complementary summaries. Pairwise containment measures the fraction of one crawl that reappears in another. A discovery curve measures how the cumulative number of distinct observed items grows across several crawls. Under their simplest model, both summaries should imply the same survival probability α and sampling coverage c. The empirical test is therefore not simply whether a curve fits one graph: parameters estimated from either observable are drawn on both graphs, exposing disagreement. Sources: pp. 2, 5, 9–10.

[A; HIGH] On Common Crawl domains from 2020–2025, the homogeneous model gives conflicting readings. A model with a persistent, always-observed core and a changing shell brings the inferred core share to approximately κ = 0.4 from both observables, while a shell-coverage disagreement remains. A second archive, the German Academic Web, provides a differently constructed, URL-level check over 2013–2019. The discussion reports approximately (κ, α, c) = (0.06, 0.62, 0.51) there. These are model-dependent effective parameters, not direct census measurements of the entire web. Sources: pp. 10–13.

The central contribution is the discovery-curve formula, its use alongside containment as a model diagnostic, and an operator vocabulary connecting fitted parameters to discovery, persistence, and hidden time. The paper is not a security study of web AI agents. Its relevance to the requested security question is indirect and explicitly treated as analyst inference below.

## 2. Document Roadmap

[A] Section 1 explains why fetch policy matters and introduces the two-observable diagnostic. Section 2 positions the work among population-estimation methods, Common Crawl measurement, and language-model corpus construction. Section 3 builds the mathematical machinery: §3.1 defines the dynamic urn; §3.2 recalls containment; §3.3 derives cumulative discovery; §3.4 examines the long-run regime; §3.5 translates parameters into crawler-facing times; §3.6 introduces the core/shell extension. Sources: pp. 1–8.

Section 4 moves from observing normalized discovery trajectories to testing model agreement. Section 4.1 constructs Common Crawl discovery curves; §4.2 compares homogeneous and two-component domain-level fits; §4.3 checks the procedure on the German Academic Web. Section 5 qualifies the interpretation of the parameters and sketches rank-dependent extensions. Section 6 summarizes the contribution. References occupy pp. 14–16. No appendix supplies additional derivations or experimental detail in this version.

## 3. Background and Context

A Uniform Resource Locator, or URL, is the identifier used for individual web resources in the paper. A crawl is one collection round. Longitudinal means that repeated collections are analyzed through time. The paper changes observational units between URL-level and domain-level analysis; those units must remain explicit because an observed domain can contain many URLs. Sources: pp. 1–2, 9–12.

An urn is a mathematical stand-in for a finite eligible population. Sampling selects some elements; churning replaces some elements. In the homogeneous model every element is assigned the same coverage and survival probabilities. A heterogeneous population contains groups with different behavior. The core/shell model uses two such groups: a perfectly persistent, fully sampled core and a changing, imperfectly sampled shell. Sources: pp. 4, 7–8.

Containment is directional: |u_i ∩ u_j|/|u_i| divides the intersection by the first crawl's size. The discovery curve counts distinct identifiers across a window, so repeatedly observing one identifier does not repeatedly increase its total. Recurrence-weighted means that persistent repeat appearances strongly influence containment; fresh-discovery-weighted means that newly encountered items strongly influence cumulative growth. The authors use this contrast to explain why the observables emphasize different population components. Sources: pp. 2, 5, 11, 13.

Common Crawl, abbreviated CC, is described as a large open-web archive. The German Academic Web, abbreviated GAW, is a focused archive seeded from German academic homepages. Breadth-first search, abbreviated BFS, is the traversal strategy attributed to GAW. Harmonic-centrality rank, abbreviated hc-rank, is the ranking axis associated with CC's prioritization. The supplied work does not define a formula for harmonic centrality; none is imported here. Sources: pp. 1–3, 10–11.

Large language models, or LLMs, enter the motivation through training corpora. The authors argue that downstream filtering cannot recover a resource that upstream fetching never captured. This is an argument about coverage of corpus inputs, not an experiment measuring language-model performance or agent vulnerability. Sources: pp. 3–4.

## 4. Research Problem and Gap

[A] Existing problem: crawler operators publish counts, but counts alone do not directly reveal effective sampling coverage, persistence, or the split between stable and ephemeral material. Policy choices such as host budgets, ranking thresholds, and deletion cutoffs shape the observed population. Sources: pp. 1–2.

[A] Shortcoming attributed to the previous approach: prior pairwise containment modeling recovers α and c under a homogeneous urn but consumes crawl pairs and lacks the proposed cross-observable failure diagnostic. A plausible fit to containment alone need not reveal that uniform sampling behavior is inadequate. Sources: pp. 2–3, 5.

[A] Research gap: a closed-form connection between sequence-level distinct-item accumulation and the same parameters used for pairwise overlap, followed by a diagnostic for heterogeneous populations. The discovery curve supplies that second projection. A two-component extension is proposed when independent fits disagree. Sources: pp. 2, 5, 7–8.

[A] Motivation and scope: infer effective crawler behavior from existing outputs without instrumenting the crawler or requiring an external population census, with empirical emphasis on policy-relevant domain aggregation for CC. The comparison archive is URL-level GAW. The paper does not study malicious content, agent actions, user permissions, model instruction following, or security failures. Sources: pp. 2–4, 9–12.

## 5. Research Questions

The paper supplies objectives and diagnostic predictions rather than a formally numbered hypothesis list. The identifiers below organize those statements and do not imply that the authors used these labels.

| ID | Status | Objective or prediction | Source |
|---|---|---|---|
| O1 | Explicit objective | Infer effective coverage c, persistence α, and core/shell decomposition κ from crawler output without external ground truth. | p. 12, §5 |
| O2 | Explicit methodological objective | Derive cumulative discovery under the same urn process as containment. | pp. 2, 5 |
| P1 | Model prediction | Independent homogeneous fits should agree on α and c if one homogeneous process describes both observables. | pp. 2, 9–10 |
| P2 | Diagnostic proposal | Cross-source disagreement identifies failure of the homogeneous description and motivates a core/shell model. | pp. 7–11 |
| P3 | Transfer prediction | The same structural diagnostic should operate in differently constructed archives, even when fitted values differ. | pp. 10–12 |
| O3 | Explicit translation objective | Express fitted parameters as quantities useful for planning and describing crawls. | pp. 6–7, 13 |
| Q1 | Author-stated unresolved question | Is the persistent core internally structured, and how should the remaining shell disagreement be resolved? | pp. 11–13 |

[D; MEDIUM] For the requested research question, an appropriate secondary objective is to assess whether crawler-observation bias could matter when interpreting an agent's web environment. That is an analyst framing. No author hypothesis compares web AI agents with standalone LLMs, and no attack-related hypothesis is tested.

## 6. Assumptions / Threat Model

[A] The homogeneous system has a constant-size urn containing N unique elements. Each discrete round samples a uniform fraction c and retains a fraction α, replacing the remaining 1−α with brand-new, never-before-seen elements. The model's formulas use fixed probabilities over the interval being fitted. Survival across multiple rounds enters as α raised to elapsed lag. Sources: pp. 4–5.

[A] The two-component extension assumes a core of size κN with α_K = 1 and c_K = 1, and a shell of size (1−κ)N with its own survival and coverage parameters. Thus the core is immortal and fully observed within the model. It is an idealization, not a demonstrated statement that particular domains are literally immortal. Sources: pp. 7–8.

[A] The urn has no explicit rebirth mechanism. A disappearing and returning identifier may be represented either as survival while missed or as fresh mass sharing an identifier. The authors say these alternatives are observationally indistinguishable through the kernel used here. This limits the interpretation of α as physical web survival. Source: p. 13.

[D; MEDIUM] Important model-use qualifications are the fit interval, granularity, and time unit. Results at domain granularity cannot be read as URL-level measurements. Plots use elapsed years despite definitions beginning in rounds; the exact implementation of the discrete model under irregular timing is not supplied. Sources: pp. 4–9, 11–12.

No security threat model is specified. There are no defined adversary capabilities, protected assets, trust boundaries, attack surfaces, or security controls. These concepts cannot be reconstructed from a crawler-sampling model without introducing material outside this paper.

## 7. Methodology

[A] Study design: derive a generative sampling model and its observable functions, then compare independently fitted parameterizations against longitudinal archive observations. The simplest model has two parameters, α and c. The extension adds core fraction κ and gives the shell its own α_∂ and c_∂. Sources: pp. 4–8.

The model first connects pairwise containment to g(Δt) = cα^Δt. It then tracks the proportion of the current urn that has already been seen and sums new discoveries to obtain the cumulative curve. The same parameters should explain both. Log-linear regression is named for the homogeneous containment fit. Analytic regression of the full discovery formula and asymptotic inversion are described for discovery. Joint three-parameter regression is described for the two-component model. The supplied text does not specify an optimizer, weighting scheme, loss function, parameter bounds in code, convergence criterion, or uncertainty-estimation procedure. Sources: pp. 5–8.

[A] CC discovery data come from per-crawl counts and rolling unique-URL statistics named url_last_N, with N in {1, 2, 3, 4, 6, 9, 12}. These are pivoted across valid starts and windows in the 2020–2025 archive. Curves are normalized by single-crawl cardinality. The later cross-source fits use domain aggregation over the same stated period; §5 reports 51 crawls. Sources: pp. 8–10, 12.

The exact transformation from publicly described URL statistics to domain-level observations, including domain parsing conventions and construction of the pairwise domain intersections, is not fully specified in the supplied method. The text asserts domain aggregation but does not provide a reproducible processing recipe or intermediate data. This is an analyst observation about reporting detail, not a claim that the transformation was invalid.

[A] GAW comprises URL-level snapshots over 2013–2019, described as biannual, Heritrix-based, seeded from approximately 150 German academic homepages, using a fixed seed hopper and breadth-first traversal without harmonic-centrality reranking. CC is described as Nutch-based and recursive, deriving fetch lists from a preceding CrawlDB and ranking by harmonic centrality. Sources: pp. 2, 10–11.

The key comparison is cross-source in the sense of two observables, not two external truth datasets. Parameters fit to containment are overlaid on both containment and discovery; parameters fit to discovery are likewise overlaid on both. Burgundy/red and navy/blue distinguish the fitting sources. Agreement tests compatibility of the model across summaries. Source: pp. 9–11.

No train/validation/test partition, learning architecture, hyperparameters for an LLM, participant recruitment, annotation protocol, hardware configuration, runtime benchmark, random seeds, repetition count, confidence interval, or significance test is reported. These absences should not be filled using conventional machine-learning assumptions: this is principally a mathematical and observational study.

## 8. Experiments / Analyses

X1 — Constructing the CC discovery object. Purpose: determine how distinct observations accumulate across windows and whether normalization exposes a common shape. Data: CC 2020–2025, rolling windows from the stated seven crawl-count settings. Variables: starting/ending crawl, elapsed duration, window length, and cumulative unique count. Observable result: cumulative counts rise with diminishing slope; normalized trajectories cluster more closely. The authors treat the common normalized shape as a regression target. Figure: 2, p. 9. Caveat: collapse is described qualitatively; no goodness-of-collapse statistic or uncertainty band is provided.

X2 — Homogeneous cross-source diagnostic. Purpose: test P1 on CC domains. Setup: independently fit containment and discovery with one homogeneous α,c pair each, then display each fit on both observables. Result: clear disagreement in Fig. 3; the containment fit emphasizes persistent recurring mass and the discovery fit emphasizes fresh discoveries. The authors conclude no single homogeneous pair explains both. Sources: pp. 9–10. Caveat: exact parameter values in the small legend are not confidently transcribed here; no quantitative model-comparison score is reported in the prose.

X3 — CC core/shell diagnostic. Purpose: test whether adding a persistent core improves compatibility. Setup: same domain observables and 2020–2025 interval, replacing homogeneous formulas with the two-component ones. Result: both fits imply approximately κ^(d) = 0.4; the shell parameters move closer but c_∂ retains disagreement. Figure: 4, p. 11; discussion pp. 10–13. Caveat: this is partial reconciliation, not exact convergence of every fitted parameter. The discovery-derived κ is acknowledged to be weakly anchored by a shallow parameter ridge.

X4 — GAW cross-architecture check. Purpose: test the structural diagnostic in an archive with contrasting collection design. Data: GAW URL snapshots, 2013–2019, one fixed-start longitudinal trajectory. Setup: two-component independent fitting and overlay as in X3. Result: authors report cross-source convergence and summarize approximately (κ,α,c) = (0.06,0.62,0.51). Figure: 5, p. 12. Caveat: one trajectory cannot provide the same assessment of across-start variation as CC. Different granularity, population, and cadence prevent interpreting numeric differences as isolated architecture effects.

X5 — Full-curve versus tail consistency diagnostic. Purpose: compare two ways of obtaining homogeneous parameters from discovery alone: fitting Eq. (5) and using the asymptotic tail. The authors propose divergence as evidence of different effective subpopulations in transient and long-run behavior. Source: p. 6, §3.4. This is a methodological diagnostic described in the text; no separately tabulated or plotted empirical outcome establishes its performance here.

The per-round increment is explicitly not an additional independent experiment. It is the discrete derivative of the discovery curve and is used as a consistency check because it carries no independent information and loses the core's initial contribution. Source: p. 6.

## 9. Results

[A; HIGH] The most secure result at the reporting level is that the homogeneous fits disagree visibly on both CC domain observables. The plots and prose agree on this qualitative result. It supports rejection of that particular homogeneous description for the displayed data; it does not identify every possible source of heterogeneity. Sources: pp. 9–10, Fig. 3.

[A; HIGH] The two-component model recovers approximately common core mass κ^(d) ≈ 0.4 over the 51-crawl CC domain window. The unit is a dimensionless modeled population fraction, not a fraction of all global URLs or a measured percentage of agent encounters. The shell coverage residual persists. Sources: pp. 10–12, Fig. 4.

[A; HIGH] The GAW summary is approximately (κ,α,c) ≈ (0.06,0.62,0.51) at URL level. These are reported approximate model parameters for that archive, not universal constants. The text attributes numerical differences partly to different populations and cadences. Sources: pp. 11–12, Fig. 5.

[A] Irregular CC timing matters: a nominal 12-crawl window can span 0.9–2.1 years, with cadence ranging from biweekly to occasional 1–2 month gaps in 2021–2022. Thus actual elapsed time is plotted rather than assuming that every window of the same crawl count has the same duration. Source: p. 9, Fig. 2 caption.

No reported p-value, error interval, likelihood-ratio comparison, held-out predictive score, or quantified improvement supports a numerical effect-size claim. No relative percentage improvement is calculated here. Approximate core fractions should not be converted into exact percentages or treated as comparable security-risk estimates.

## 10. Figure-by-Figure

Figure 1 — Partitioning one urn round, p. 4.

[B] The left object is an urn containing N elements. Arrows lead to three right-hand bands: sampled αcN, missed α(1−c)N, and replaced (1−α)N. The two upper bands share survival α and split according to c versus 1−c. The bottom branch represents churn. Heights encode the component masses; there are no numerical axes, error bars, or statistical markers. The diagram supports the memory term α(1−c), the chance of remaining alive but unseen.

[A/B] A convention issue is visible: the numbered procedure says sampling then churning, while the diagram/caption partitions elements by survival followed by sampled-versus-missed status and says αcN appear in the round-t crawl. Equation (1) separately defines full sample size M = Nc. The source does not fully clarify the round-index alignment between these descriptions. The diagram is represented faithfully without silently fixing that convention.

Figure 2 — The CC discovery-curve object, p. 9.

Panel 2a is a heatmap. Its vertical axis lists crawl-window lengths 1, 2, 3, 4, 6, 9, and 12; horizontal ticks show calendar years including 2022, 2024, and 2026. A blue intensity scale encodes cumulative unique URLs, with labels including 3 B, 10 B, and 20 B, where the caption's context makes B billions of URLs. Longer windows are darker, indicating more unique observations. Exact individual cell values are not labeled.

Panel 2b shows normalized cumulative count U(Δt)/U(0) against actual elapsed years. Gray-to-black lines indicate older-to-newer ending crawls. Visible trajectories rise and flatten; normalization makes their shapes more comparable but does not remove all spread. No confidence intervals are identified. Exact endpoints are not treated as numerical results.

[A/B] There is a location-label inconsistency: the horizontal axis label in panel 2a says end of window, and the panel subtitle refers generally to crawl date; the caption describes starting crawl date s on that axis. The discussion also describes pivoting by starts, whereas panel 2b uses one line per ending crawl. Both descriptions are reported; the supplied material does not resolve the precise indexing implementation.

Figure 3 — Homogeneous CC cross-source fits, p. 10.

Panel 3a plots domain-level normalized discovery U^(d)(T)/U^(d)(0) against T in years. The displayed discovery trajectories grow across a horizontal span of roughly 0–3 years. Burgundy/red is the containment-fitted model; navy/blue is the discovery-fitted model. The blue curve follows much of the upward discovery pattern while the burgundy curve remains lower. Panel 3b plots domain-level containment g^(d)(Δt) against elapsed years, with displayed lags extending to about six years. Its vertical axis appears logarithmic from the spacing and labeling, but small tick labels are not all confidently legible. The discovery-fitted prediction falls much more sharply than the containment-fitted prediction.

The point is cross-prediction failure in both directions. The models should coincide under one homogeneous process; they do not. Exact small legend parameter strings are uncertain and omitted rather than guessed. Thin gray trajectories and dark observations are visible; their detailed statistical meaning is not fully defined. No labeled confidence band establishes precision.

Figure 4 — Two-component CC fits, p. 11.

Panel 4a uses the same normalized domain discovery observable and elapsed-year horizontal axis as Fig. 3a. Panel 4b uses the same domain containment observable and lag axis as Fig. 3b. Red/burgundy and blue/navy again identify fitting sources. A dashed horizontal line marks the core-related floor. The two containment curves are closer at long lags, while the discovery-side and short-lag differences remain visible. The caption and prose report κ^(d) ≈ 0.4, not exact equality of all shell parameters.

The visual supports partial reconciliation and persistent short-timescale mismatch. The paper interprets the c_∂ disagreement as nonuniformity within the shell. That is a model-based author interpretation; the plot alone does not isolate causal mechanism. Small legend values are not copied as exact measurements. Sources: pp. 10–11, 13.

Figure 5 — GAW two-component check, p. 12.

Panel 5a plots normalized URL-level discovery U(T)/U(0) against elapsed years, with visible ticks at 0, 2, 4, and 6. Dark observations rise approximately along an increasing curve; red and blue model curves are close but visibly distinct. Panel 5b plots containment g(Δt) against lag, with an apparently logarithmic vertical axis and a dashed core-floor reference. The authors describe this as cross-source agreement on the same triple and report approximate values in §5. Exact legend transcription is not reliable at the supplied resolution.

The caption calls this a ground-truth check. The available evidence is agreement between fitted summaries within one archive; an independent census or externally measured true parameter triple is not shown. Accordingly, the phrase is preserved as the authors' characterization and is not upgraded into independently verified ground truth. The single-trajectory limitation is explicit in the caption.

### Supplemental analyst check of figure legends
A subsequent analyst inspection of higher-resolution renders of physical pp.11–12 resolves important legend values that were not confidently readable in the smaller generation images. Figure4 reports containment (κ,α,c)=(0.42,0.68,0.70), discovery (0.46,0.64,0.20), and dotted core floor0.46. The shared κ≈0.4 is an approximate author characterization, not identical fitted triples or demonstrated confidence-interval overlap. Figure5 reports containment (0.050,0.62,0.51), discovery (0.077,0.76,0.14), and floor0.08. These differ appreciably in shell parameters and do not numerically establish the caption's single-triple convergence; the discussion's (0.06,0.62,0.51) is a further summary rather than either exact displayed triple. Preserve this source inconsistency instead of choosing one fit as ground truth. The 'ground-truth check' is an internal comparison of projections, not validation against an external population census. These are directly observed legend transcriptions and analyst qualifications, not additional author experiments.

## 11. Table-by-Table

No substantive numbered table is present in the supplied work. Therefore there are no author table rows, best-performing entries, missing-value codes, table-specific statistical notes, or table footnotes to transcribe. The tables in this report organize extracted evidence and are analyst-created aids, not reconstructed author tables.

Numerical parameters appear in prose and plot legends rather than a dedicated results table. The prose supports the approximate CC core share and GAW triple; the figure legends are too small to justify exact extraction of every displayed fit. This distinction prevents an analyst-created table from giving unreadable plot values an appearance of precision.

## 12. Diagram / Architecture

Figure 1 is the only explicit process diagram. Its input is the current eligible population N. Its outputs are survived-and-observed mass, survived-and-hidden mass, and replaced mass. The survival branch α precedes a conceptual split by coverage c. The missed branch is the mechanism carrying memory: items may remain eligible while absent from an observed crawl. The replacement branch removes identities and inserts never-before-seen ones. Repetition across rounds generates the containment and discovery equations. Source: p. 4.

The crawler-architecture comparison is textual rather than a drawn system architecture. CC uses a recursive Nutch-based process with a preceding CrawlDB and harmonic-centrality ranking; GAW uses a Heritrix-based, fixed-seed, breadth-first process. The supplied text gives no component interface diagram, data schema, scheduler pseudocode, or implementation trace. Those should not be invented. Sources: pp. 2, 10–11.

[D; MEDIUM] The analytic workflow can be described as observations → two fitted projections → cross-prediction comparison → richer model if needed → operator quantities. This sequence is a synthesis of the method, not an additional diagram supplied by the authors. It contains no agent action loop, attacker feedback loop, or security boundary.

## 13. Equations and Mathematical

Notation is normalized below to remove obvious extraction artifacts such as summation markers and encoded parentheses. This is a mathematical transcription based on surrounding definitions, not a claim that rendered equation pages were visually inspected. All quantities are dimensionless probabilities or normalized counts unless a duration is explicitly attached.

Basic definitions, pp. 4–5: ᾱ = 1−α is churn; c̄ = 1−c is miss probability; q = αc̄ is analyst shorthand for the author's persists-unseen rate; r = 1−q = ᾱ+αc is the resolved probability. Probability constraints are 0 ≤ α,c ≤ 1; formulas with vanishing denominators require limiting treatment, which the supplied work does not develop explicitly.

Equation (1), p. 5: g(Δt) = |u_i ∩ u_j|/|u_i| = cα^Δt, with M = |u_i| = Nc. Inputs are a lag and two model parameters; output is expected containment. Survival over the gap and sampling at the later occasion determine reappearance. Log-linear fitting estimates c from the intercept and α from decay under the stated model. This formula is the pairwise baseline.

Equation (2), p. 5: ρ(t) = α[ρ(t−1)+cν(t−1)] = αc+αc̄ρ(t−1), with ρ(0)=0. Here ρ(t) is the fraction of the current urn already seen before round t; ν(t) is the new fraction in that round. The recurrence retains previously marked elements and adds newly marked ones before survival. The factor αc̄ controls persistence of the transient. The verbal definition and recurrence matter because ρ concerns the current urn, not the cumulative number ever seen.

Equation (3), p. 5: ρ(t) = αc[1−(αc̄)^t]/[1−αc̄]. This solves Eq. (2). As time grows, the geometric term shrinks if αc̄<1, leaving the long-run seen fraction ρ∞ = αc/(1−αc̄). This limiting expression follows directly from the supplied formula and is [C] when stated in that explicit form.

Equation (4), p. 5: U_hat(t) = Σ from τ=0 to t of ΔU_hat(τ), with ν(t) = ΔU_hat(t)/M = 1−ρ(t). It defines cumulative distinct discoveries by adding only new mass at each round. The initial index t=0 includes the first all-new crawl, so t counts one less than the number of included rounds. This indexing differs from prose descriptions using a window of T crawls and must be handled carefully in implementation.

Equation (5), p. 5: U_hat(t)/M = (t+1)ᾱ/(ᾱ+αc) + αc[1−(αc̄)^(t+1)]/(ᾱ+αc)^2. Inputs are t, α, and c; output is cumulative distinct count relative to one crawl. The first term grows linearly because churn keeps introducing identities; the second captures diminishing initial discovery. It connects the same homogeneous parameters to the whole accumulation curve. At t=0 it equals one for nondegenerate denominators, consistent with the first crawl being all new.

Equations (6)–(7), p. 6: U_hat(t)/M ≈ ν∞t + I for large t; ν∞ = ᾱ/(1−αc̄); I = 1+ρ∞τ_h; τ_h = αc̄/(1−αc̄). The approximation discards a decaying geometric term. ν∞ is the long-run fraction of each crawl that is new. I is the intercept of the extrapolated asymptotic line, not the actual first-crawl normalized count. τ_h measures hiding time per resolution, not total hidden time over an item's life.

Equations (8)–(9), p. 6: α = (ρ∞+τ_h)/(1+τ_h), and c = ρ∞/(ρ∞+τ_h), where ρ∞ = 1−ν∞. These invert two independent observable features when the homogeneous assumptions hold: the long-run rate and a transient/intercept-related timescale. A later discussion sentence instead says inversion sends (ν∞,ρ∞) to (α,c). Because those two rates sum to one, they are not independent. This text–equation inconsistency is substantive and remains unresolved in the supplied text.

Equations (10)–(12), pp. 6–7: ℓ = α/ᾱ; η = cℓ = αc/ᾱ; η̄ = c̄ℓ = αc̄/ᾱ. Respectively these are expected lifetime, sampled time, and hidden time in model rounds/crawls. They are mathematical translations of fitted probabilities, not direct measurements of URL age. When α approaches one, finite-lifetime formulas diverge; the idealized core is treated separately.

Equations (13)–(14), p. 7: ℓ = η+η̄, and η/η̄ = c/c̄. The first partitions expected life into sampled and hidden portions. The second expresses coverage odds when the ratio is defined; boundary cases such as c=1 have zero hidden time and require the corresponding limiting interpretation.

Equation (15), p. 7: η̄ = (1+η)τ_h. This connects lifetime-total hiding to the mean hidden-epoch scale and the expected number of such epochs. The authors explain one hidden epoch before each sample and a final one ending in churn. It distinguishes cumulative hidden cost from one episode of invisibility.

Equation (16), p. 7: g(Δt) = κ+(1−κ)c_∂α_∂^Δt. The authors use κ as the persistent containment floor and propose fitting κ, α_∂, and c_∂ jointly. They also call the log-scale curve concave. For ordinary log g against a linear lag, that curvature description conflicts with direct differentiation: for positive floor and exponential component, the second derivative of log g is positive. This is [C] analyst mathematical checking, not a replacement author result. The diagnostic point that a positive-floor mixture is not a single exponential still holds.

Equation (17), p. 8: M = Nκ+N(1−κ)c_∂ and μ = Nκ/M = κ/[κ+(1−κ)c_∂]. μ is the share of a sampled crawl belonging to the core; κ is defined as the core share of the urn. With a nontrivial core and c_∂<1, μ>κ. Thus core representation differs between the eligible population and an observed sample.

Equation (18), p. 8: U_hat_2c(t)/M = μ+(1−μ)B(t;α_∂,c_∂), where B is the right-hand side of Eq. (5). The core appears once and saturates at the first observation; the shell contributes subsequent new identities. For t>0 the new fraction is (1−μ)ΔB. This is why the increment alone has poor core identifiability and why the containment floor is emphasized.

[C; MEDIUM] A normalization inconsistency links Eqs. (1), (16), and (17). Under the paper's stated population partition and directional sample containment, expected persistent-core contribution is Nκ/M = μ. Expected shell overlap is N(1−κ)c_∂²α_∂^Δt. Dividing their sum by M gives g(Δt) = μ+(1−μ)c_∂α_∂^Δt, whose floor is μ, whereas Eq. (16) uses κ. This derivation assumes the same homogeneous shell sampling independence underlying the containment formula. The supplied paper does not explain whether Eq. (16) uses a different normalization or repurposes κ. Consequently the numerical κ values are reported as the authors' model estimates, with uncertainty about their exact population-share interpretation.

No formal theorem or proof chain accompanies these equations. The progression is definitions → recurrence → geometric-series solution → asymptotic approximation/inversion → operator translations → mixture extension. Missing derivation details are not filled with claims of formal proof.

## 14. Interpretation and Discussion

[A] The authors interpret disagreement between recurrence-sensitive and new-discovery-sensitive summaries as useful measurement rather than merely fit failure. A single uniform population hides structure; introducing a stable component reveals a mass split. The remaining shell mismatch says that even this two-part picture is not the end of the story. Sources: pp. 2, 10–13.

[A] The policy interpretation is explicitly conjectural. Coverage c is described as more directly tunable through budgets, rank thresholds, and revisit cadence; survival α is described as supplied by the eligible population's persistence; κ reflects both eligibility policy and population stability. Page 13 says establishing this separation would require holding one side fixed while varying the other. Therefore the cross-archive comparison is not evidence of isolated causal effects from particular policy knobs.

[A] α is ultimately a crawl-side survival reading. Temporary absence, missed sampling, and identifier reuse cannot be fully separated by the observables. The result is useful as an effective description of the urn the crawler sees, but should not be read as a direct estimate of physical deletion from the web. Source: p. 13.

[D; MEDIUM] The empirical evidence answers O1 conditionally: the proposed model produces interpretable estimates and a visible diagnostic on the two archives. It does not establish unique identification of all underlying web dynamics. Parameter ridges, the population-versus-crawl core-share inconsistency, and the missing independent uncertainty analysis narrow the strength of that conclusion.

[D; MEDIUM] For the requested security question, the paper offers a measurement caution: observed web material is selected and temporally incomplete. That could matter when interpreting what information a web-connected system has encountered. The paper provides no evidence that such incompleteness causes exploitable instruction following, that an attacker can manipulate the measured core, or that an agent is more vulnerable than a standalone model. A direct security answer remains unsupported by this source.

## 15. Contributions and Novelty

[A] Conceptual contribution: treat containment and discovery as projections of one sampling process and make their disagreement a diagnostic. Source: pp. 1–2, 9.

[A] Mathematical contribution: give a closed-form cumulative-discovery function for the dynamic homogeneous urn and connect its transient and asymptotic terms to existing survival/coverage parameters. Sources: pp. 5–6.

[A] Methodological contribution: independently fit the observables and overlay both inferred parameterizations on both outputs; extend to a persistent-core/changing-shell model when the homogeneous description fails. Sources: pp. 7–11.

[A] Interpretive contribution: translate probabilities into expected lifetime, sampled time, hidden time, and a per-resolution hiding scale. Sources: pp. 6–7, 13.

[A] Empirical contribution: demonstrate the diagnostic on CC domains and GAW URLs, with approximate core-share convergence and an explicitly acknowledged CC shell residual. Sources: pp. 9–12.

No new language model, security defense, attack benchmark, released dataset, crawler implementation, or measured computational speedup is established as a contribution. Existing statistical and crawler-measurement foundations are acknowledged in §2; their bibliography entries do not independently verify the present work's novelty.

## 16. Limitations

Authors' stated limitations:

• The CC shell retains disagreement on c_∂, indicating that a homogeneous shell is insufficient. Sources: pp. 10–13.
• Discovery-derived κ is less firmly anchored because core plateau and shell parameters trade off along a shallow ridge. Source: p. 8.
• The per-round increment adds no independent discovery information and cannot robustly anchor the core by itself. Source: p. 6.
• GAW supplies one fixed-start trajectory; its test does not assess per-trajectory variance across starts. Sources: pp. 11–12.
• The urn has no rebirth mechanism; temporary dormancy and return cannot be uniquely separated from identifier-reusing fresh mass. Source: p. 13.
• Operator-versus-web attribution of c and α is a conjecture requiring controlled variation. Source: p. 13.
• Internal core structure and a full rank-resolved theory remain undeveloped. Sources: pp. 11, 13.

Additional evidence-based analyst observations:

[D] Exact fitting procedures, uncertainty estimates, processing details, and held-out evaluation are not reported at the level needed for independent reproduction. No code artifact was supplied or inspected.
[D/C] Eqs. (16)–(17) appear inconsistent about core-share normalization; §5's inversion statement conflicts with the independent quantities used in Eqs. (8)–(9); the claimed log-scale concavity is mathematically questionable under the stated function.
[D] Irregular elapsed-time modeling is insufficiently documented for translating fitted α into per-crawl lifetime values. Distinct granularity and populations confound architecture-only interpretations.
[D] Some exact legend values cannot be confidently read from the provided image resolution. This limits transcription, not necessarily the underlying paper's original-resolution readability.
[D] No security outcomes or agent-versus-model comparison are present, sharply limiting relevance to the requested research question.

## 17. Threats to Validity

The following validity labels are analyst organization, not headings or admissions attributed to the authors.

Internal validity: [D; MEDIUM] observed fit disagreement may reflect population heterogeneity, but the supplied evidence does not isolate it from changing parameters, aggregation choices, timing conventions, or imperfect alignment between the two observation sources. The authors' heterogeneity explanation is plausible within their model but not a controlled causal identification.

Construct validity: [A/D; HIGH] α measures persistence as seen by the crawler, not unambiguous real-world existence. κ has an idealized-core meaning whose normalization requires clarification. Domain-level quantities and URL-level quantities measure different constructs. Sources: pp. 7–8, 11–13.

External validity: [D; MEDIUM] two differently constructed archives support a limited transfer demonstration. They do not establish generality to every crawl policy, live browsing session, agent deployment, or adversarial environment. GAW is focused; CC is broad but filtered by its collection process.

Statistical conclusion validity: [D; MEDIUM] the argument relies mainly on visible curve disagreement and approximate parameter agreement. Without reported uncertainty, residual statistics, fitting weights, or sensitivity analyses, the precision and stability of conclusions cannot be fully assessed. Correlated windows may also limit the amount of independent evidence; the supplied work does not quantify that dependence.

Reproducibility: [D; MEDIUM] public data addresses and equations help, but domain parsing, intersection construction, fitting code, exact time treatment, and uncertainty estimation remain underspecified. Linked resources were not fetched, so their contents cannot resolve these gaps in this closed-document analysis.

Ecological validity for security: [D; HIGH] archive-level sampling is not a measured online agent interaction. Using these results to explain comparative exploitation rates would cross beyond the study's observed setting.

## 18. Future Work and Open Questions

A. Author-proposed future work: develop a rank-resolved description of core and shell structure; use per-domain rank changes on the hc-rank axis; move from scalar κ toward a rigidity profile involving μ(r) and D(r); connect drift, diffusion, and survivor flux in a fuller framework. The four referenced rank-resolved profiles are not fully defined in the supplied text, so no equations or fitted values are supplied for them here. Source: p. 13.

The authors also identify the need to determine whether the persistent core is one rigid block and to resolve residual shell-coverage disagreement. Testing the proposed division between operator-controlled and web-controlled quantities requires holding one side fixed while varying the other. Sources: pp. 11–13.

B. Analyst open questions: clarify whether containment-floor κ denotes urn share or crawl share; document the exact independent tail observables used for inversion; state the time-unit convention for fitted survival; report uncertainty and sensitivity to windows and aggregation; explain starting-versus-ending window indexing in Fig. 2; quantify whether a richer model improves held-out predictions. These follow from observed reporting or consistency issues, not from outside literature.

For the user's security research, an additional unresolved question is whether any of these measurement quantities predicts security-relevant outcomes in agent browsing. No such outcome is supplied here, so neither direction nor magnitude can be inferred.

## 19. Terminology and Notation Glossary

| Term/symbol | Meaning in this paper | Qualification/source |
|---|---|---|
| URL | Uniform Resource Locator; identifier for a web resource. | Unit of some analyses, pp. 1–2. |
| CC | Common Crawl. | Domain-level model tests, pp. 9–11. |
| GAW | German Academic Web. | URL-level comparison archive, pp. 10–12. |
| LLM | Large language model. | Motivation through training corpora, pp. 3–4. |
| BFS | Breadth-first search traversal. | GAW design description, p. 2. |
| hc-rank | Harmonic-centrality ranking axis. | Formula not defined here, pp. 1–2, 13. |
| N | Number of unique elements in the urn. | Also used for a public rolling-window crawl count; meanings must be distinguished. |
| M | Per-crawl sample size. | Nc in homogeneous case; mixture expression in Eq. (17). |
| u_i | Observed set in crawl i. | Eq. (1). |
| α | Per-step survival parameter. | Effective crawl-side persistence, pp. 4, 13. |
| ᾱ | 1−α, churn fraction. | p. 4. |
| c | Coverage/sampling fraction. | p. 4; time/unit conditions matter. |
| c̄ | 1−c, miss fraction. | p. 4. |
| g(Δt) | Directional pairwise containment at lag Δt. | Eq. (1). |
| U(s,T) | Cumulative distinct observations across a window starting at s. | Window/index conventions need care. |
| U_hat(t) | Modeled cumulative discovery through round t. | Eqs. (4)–(5). |
| ρ(t) | Fraction of current urn already seen before round t. | Eq. (2). |
| ν(t) | New fraction of a round's sample. | 1−ρ(t), p. 5. |
| ν∞ | Long-run new-discovery fraction. | Eqs. (5)–(6). |
| ρ∞ | Long-run seen fraction, 1−ν∞. | p. 6. |
| I | Extrapolated asymptotic intercept. | Not actual initial count, p. 6. |
| τ_h | Mean hiding time per resolution/hidden epoch. | Eq. (7). |
| ℓ | Expected lifetime in model crawls. | Eq. (10). |
| η | Expected sampled rounds over a life. | Eq. (11); called resolve time in conclusion. |
| η̄ | Expected hidden rounds over a life. | Eq. (12). |
| K, ∂K | Persistent core and changing shell. | §3.6. |
| κ | Defined core share of urn; also used as containment floor. | Potential normalization inconsistency. |
| μ | Core share of an observed crawl. | Eq. (17), distinct from κ. |
| α_∂, c_∂ | Shell survival and sampling parameters. | §§3.6, 4.2. |
| Superscript d | Domain-level quantity. | Figs. 3–4. |
| Subscripts g, U | Fit based on containment or discovery. | Figs. 3–4. |
| B(t;α,c) | Normalized homogeneous discovery expression. | Eq. (18) definition. |
| μ(r), D(r) | Proposed rank-resolved rigidity-related profiles. | Full definitions/development absent, p. 13. |

## 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| CC scale described in introduction | 2–3 billion | URLs/crawl | Broad archive description, not the domain sample size | Author-reported | p. 1 |
| CC archive history described | Over 90 since 2013 | Archives | Background at time of paper | Author-reported | p. 1 |
| Webgraph scale described | 200 billion | Edges | Background for operator knobs | Author-reported | p. 1 |
| GAW starting seed scale | Approximately 150 | Academic homepages | Focused crawl | Author-reported | p. 2 |
| Public window settings | {1,2,3,4,6,9,12} | Crawls/window | url_last_N | Author-reported | p. 8 |
| CC analysis interval | 2020–2025 | Calendar years | Discovery and domain cross-source tests | Author-reported | pp. 8–12 |
| CC window size | 51 | Crawls | Domain analysis summarized in discussion | Author-reported | p. 12 |
| CC cadence variation | Biweekly to occasional 1–2 month gaps | Time | Gaps noted for 2021–2022 | Author-reported | p. 9 |
| Duration of a 12-crawl window | 0.9–2.1 | Years | Irregular CC cadence | Author-reported | p. 9 |
| CC modeled persistent core | κ^(d) ≈ 0.4 | Fraction | Domain-level, both fitting projections | Author-reported | pp. 10–12 |
| CC coverage in policy discussion | ≈0.78 | Fraction | CC-domain operating-point comparison; mapping to each plotted fit is not fully specified | Author-reported | p. 12 |
| GAW interval | 2013–2019 | Calendar years | URL snapshots, described as biannual | Author-reported | pp. 10–11 |
| GAW summary triple | (κ,α,c) ≈ (0.06,0.62,0.51) | Dimensionless parameters | URL-level two-component discussion summary | Author-reported | p. 12 |
| Ideal core parameters | (α_K,c_K)=(1,1) | Probabilities | Model assumption, not measured immortality | Author-reported | p. 7 |
| Core observations after first round | No additional new core mass | Model count behavior | Idealized fully sampled persistent core | Author-reported | pp. 6, 8 |
| Heatmap legend labels | 3 B, 10 B, 20 B | Unique URLs | Fig. 2a color encoding, not exact cell results | Visually readable | p. 9 |

The table deliberately excludes uncertain small legend strings, derived security percentages, and lifetime computations from year-scaled fit parameters. No analyst-derived empirical effect size is asserted. Mathematical derivations are instead shown with operands in §13.

## 21. Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Discovery adds a sequence-level observable governed by homogeneous α,c. | Recurrence and closed-form cumulative formula. | Eqs. (2)–(5) | p. 5 | Strong support for what is derived under the stated assumptions; not assumption-free identification. |
| Independent fits create a compatibility diagnostic. | Each fitted model overlaid on both observables. | X2, Fig. 3 | pp. 9–10 | Clear methodological description and visible mismatch. |
| One homogeneous pair fails on the displayed CC domains. | Red/blue predictions diverge on both panels. | X2, Fig. 3 | p. 10 | HIGH for qualitative displayed disagreement; no uncertainty-based rejection statistic. |
| Core/shell fitting recovers approximate common CC core share. | Caption and discussion report κ^(d)≈0.4. | X3, Fig. 4 | pp. 10–12 | Approximate and model-dependent; normalization concern remains. |
| The shell is still not adequately homogeneous. | Residual c_∂ disagreement. | X3, Fig. 4 | pp. 11, 13 | Author interpretation supported by mismatch, not unique causal diagnosis. |
| GAW provides a different-architecture check. | Fixed-seed BFS archive; reported common approximate triple. | X4, Fig. 5 | pp. 11–12 | One trajectory; URL/domain and cadence differences limit causal comparison. |
| Core identification is weaker from discovery alone. | Shallow ridge and derivative discussion. | Eqs. (16)–(18) | pp. 6, 8 | Explicit author caveat; no uncertainty contour supplied. |
| Survival is crawler-visible, not strict physical survival. | Explicit no-rebirth/dormancy qualification. | Discussion | p. 13 | Strong source support; central construct limitation. |
| Policy attribution is conjectural. | Authors require holding one side fixed while varying the other. | Discussion | pp. 12–13 | Explicitly not a theorem or controlled causal result. |
| Core-floor normalization requires clarification. | Eq. (1) denominator plus Eq. (17) gives floor μ rather than κ. | Analyst derivation | pp. 5, 7–8 | MEDIUM; conditional on common containment definition and shell independence. |
| Security relevance is indirect. | Study measures crawl sampling and corpus coverage, not agent attacks. | Scope and conclusion | pp. 4, 12–13 | Analyst inference; no comparative vulnerability finding. |

## 22. Very Simple Explanation

Imagine taking repeated photographs of a busy public square. Each photograph shows only some people, and people enter or leave between photographs. One question is how many people in one photo appear again later. Another is how many different people you have photographed after taking several photos. The paper uses the same two ideas for repeated web crawls: repeated appearances and cumulative new discoveries.

If everything in the square had the same chance of staying and being photographed, both measurements should tell a compatible story. In the studied web archives, the simple model does not. The authors therefore divide the population into an always-visible stable group and a changing group. This makes the two measurements agree more closely, although the changing group still seems more complicated than one uniform category.

The useful outcome is a way to describe what a crawler sees: how much it samples, how quickly observed identities change, how much is newly discovered, and how long items remain unseen. But being absent from a photograph does not prove a person left the square. Similarly, a missing URL does not prove the web page stopped existing. The authors explicitly warn about that distinction.

This does not show why a web AI agent would be easier to attack than a standalone language model. It shows that web observations are selective and incomplete. Connecting those observations to attacks would require security evidence that this paper does not provide.

## Completeness Audit

Coverage is measured against the supplied inventory, not the length of this report. All supplied pages were reviewed, but only the seven supplied rendered pages received direct visual inspection. All five figures received visual inspection. The mathematical content was reviewed through extracted text, with explicit transcription and consistency caveats.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/version, p. 1 | Yes, text and image | Yes | Fully represented | arXiv:2607.13636v1, 15 July 2026; no supplied conference/journal venue. |
| Abstract/keywords | Yes | Yes | Represented in compressed form | Keywords: web archive, crawl coverage, discovery curve, urn model, two-component model, URL lifetime. |
| §1 Introduction | Yes | Yes | Represented in compressed form | Framing and archive/architecture context preserved. |
| §2 Related Work | Yes | Yes | Represented in compressed form | Three strands retained. |
| §2.1 Urn modeling | Yes, text only | Yes | Represented in compressed form | Capture–recapture, occupancy, cumulative coverage, prior containment positioned as author background. |
| §2.2 CC metrics | Yes, text only | Yes | Represented in compressed form | Published metrics and prior auditing categories covered; citations not externally checked. |
| §2.3 LLM substrate | Yes | Yes | Represented in compressed form | Upstream-fetch limitation preserved; corpus enumeration compressed. |
| §3.1 Urn model | Yes | Yes | Fully represented | Sampling/churn assumptions and round-convention issue included. |
| §3.2 Containment | Yes, text only | Yes | Fully represented | Definition, regression, normalization. |
| §3.3 Discovery | Yes, text only | Yes | Fully represented | Recurrence, sum, closed form, derivative caveat. |
| §3.4 Asymptotic regime | Yes, text only | Yes | Fully represented | Tail, intercept, inversion, consistency issue. |
| §3.5 Operator language | Yes, text only | Yes | Fully represented | Lifetime and both hidden-time concepts. |
| §3.6 Core/shell | Yes, text only | Yes | Fully represented | Equations, sample share, identifiability, normalization concern. |
| §4.1 CC discovery | Yes | Yes | Fully represented | X1/Fig. 2. |
| §4.2 CC cross-source fits | Yes | Yes | Fully represented | X2/X3 and residual preserved. |
| §4.3 GAW validation | Yes | Yes | Fully represented | X4 and single-trajectory qualification. |
| §5 Discussion | Yes, text and images | Yes | Fully represented | Parameter conjecture, dormancy, rank outlook. |
| §6 Conclusion | Yes, text and image | Yes | Represented in compressed form | Operator dictionary retained without duplicating formulas. |
| Objectives O1–O3 | Yes | Yes | Fully represented | Analyst identifiers for author objectives. |
| Diagnostic predictions P1–P3 | Yes | Yes | Fully represented | Not relabeled as formal numbered hypotheses. |
| Formal hypotheses | Not present | Accounted for | No such supplied object | No security hypothesis manufactured. |
| X1 | Yes | Yes | Fully represented | Common normalized discovery shape. |
| X2 | Yes | Yes | Fully represented | Homogeneous mismatch. |
| X3 | Yes | Yes | Fully represented | Approximate core agreement and residual. |
| X4 | Yes | Yes | Fully represented | GAW check. |
| X5 | Yes | Yes | Represented in compressed form | Proposed diagnostic, no separate empirical outcome. |
| Fig. 1 | Yes, visually | Yes | Fully represented | Process diagram and convention issue. |
| Fig. 2a | Yes, visually | Yes | Fully represented | Heatmap; start/end axis inconsistency. |
| Fig. 2b | Yes, visually | Yes | Fully represented | Normalization, timing, gray/black encoding. |
| Fig. 3a–b | Yes, visually | Yes | Represented in compressed form | Exact small legend strings uncertain. |
| Fig. 4a–b | Yes, visually | Yes | Represented in compressed form | Approximate prose-supported κ retained; exact legends uncertain. |
| Fig. 5a–b | Yes, visually | Yes | Represented in compressed form | Prose triple retained; exact legends uncertain. |
| Substantive tables | None present | Accounted for | No such supplied object | Report tables are analyst-created. |
| Eq. (1) | Yes, extracted text | Yes | Fully represented | Directional containment. |
| Eqs. (2)–(5) | Yes, extracted text | Yes | Fully represented | Recurrence and discovery solution. |
| Eqs. (6)–(9) | Yes, extracted text | Yes | Fully represented | Tail and inversion. |
| Eqs. (10)–(15) | Yes, extracted text | Yes | Fully represented | Operator times and identities. |
| Eqs. (16)–(18) | Yes, extracted text | Yes | Fully represented | Mixture, share distinction, identifiability. |
| Numbered algorithms/pseudocode | None present | Accounted for | No such supplied object | Two-step procedure covered. |
| Theorems/lemmas/propositions | None present | Accounted for | No such supplied object | No formal proof claims invented. |
| Major contributions | Yes | Yes | Fully represented | Conceptual, mathematical, methodological, interpretive, empirical. |
| Author limitations | Yes | Yes | Fully represented | All inventory limitations grouped in §16. |
| Statistics footnotes | Yes, text | Yes | Represented in compressed form | Addresses identified as unvisited external artifacts. |
| Interests disclosure | Yes | Yes | Represented in compressed form | No competing interests declared. |
| References 1–36 | Yes, text only | Yes | Represented in compressed form | Categories and role covered; full bibliography not repeated. |
| Appendices | None supplied | Accounted for | No such supplied object | No appendix review claimed. |
| Supplementary material | None supplied | Accounted for | No such supplied object | No supplementary review claimed. |
| External linked statistics/source papers | No | No | Inaccessible within closed-document scope | Links and citations alone are not inspected source contents. |

Missing or inaccessible material

No page is missing from the supplied 1–16 sequence. Rendered images are unavailable for pp. 2, 3, 5–8, and 14–16; those pages have text-only coverage. Exact small-legend fit values are not all confidently readable. No supplementary file, fitting code, processed observations, or linked statistics content was supplied. The report does not assert that such artifacts do not exist elsewhere.

Uncertain interpretations

The main unresolved points are κ versus μ in the containment normalization; the discussion's dependent-rate inversion statement versus Eqs. (8)–(9); the log-curvature description in §3.6; sampling/churn round alignment in Fig. 1 versus M=Nc; Fig. 2's start-versus-end window axis; and the precise implementation of elapsed-time fitting. The original equation-page layouts could not be visually checked. The paper's approximate GAW triple is secure as a prose report, but exact equality of the two underlying fitted triples cannot be reconstructed from the small legends.

Deliberately compressed material

Repeated explanations of the same two-observable principle, duplicated conclusion formulas, the long list of downstream corpora, individual bibliography entries, author ORCID identifiers, and contact details are compressed. Page headers, decorative whitespace, and recurring author/title running heads are non-substantive. No empirical result is deliberately omitted because it is inconvenient to the main interpretation.

Potential omissions

Every substantive object identified in the supplied inventory is represented or explicitly accounted for. This is not a claim to preserve every word or every unreadable legend value. The inaccessible precision and unresolved mathematical/reporting issues above remain potential sources of missing detail. The requested comparative security question cannot be answered directly from this paper; the report preserves that evidence boundary rather than substituting an unsupported security explanation.
