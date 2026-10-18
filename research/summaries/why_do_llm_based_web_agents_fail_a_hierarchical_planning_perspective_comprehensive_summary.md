## Stage 0 — Document Accessibility Report

The supplied work comprises native/extracted text for physical PDF pages 1–24 and rendered images for pages 1–7 and 19–24. All 24 pages have supplied text. Thirteen pages have directly inspectable images; pages 8–18 were assessed through supplied text only. Physical page numbers are used throughout this report; the paper's printed proceedings pagination runs from 32157 to 32180. The title, abstract, main sections, limitations, references, and appendices are present. No obvious gap appears in the supplied page sequence, although page count alone does not prove that every original artifact was included.

| Accessibility item | Assessment |
|---|---|
| Main document | Available as 24 pages of supplied text; partial visual rendering |
| Physical page range | 1–24 |
| Visually inspected pages | 1–7, 19–24 |
| Text-only pages | 8–18 |
| Figures | Figures 1–13 visually available; numbering is not physical placement order |
| Tables | Tables 1–11 visually available and readable |
| Mathematical notation | Main definitions on p. 2 readable; extraction spacing requires care |
| Appendices | Appendix A, §§A.1–A.5, and Appendix B, §§B.1–B.4.2, supplied |
| Supplementary artifacts | No separate files, executable framework, dataset, or repository contents supplied |
| Referenced external artifact | Framework/data repository linked in footnote 1, p. 2; not inspected |
| OCR | Not required; supplied text was cross-checked against available images |
| Visual limitations | Small website screenshots support qualitative inspection, not reliable transcription of every embedded interface detail |

The automated accessibility metadata says no appendix pages were detected, but the supplied text explicitly contains Appendices A and B. The document itself takes precedence over that detection field. No tools, browsing, repository access, code execution, or external factual supplementation were used. The supplied prompts were treated as study evidence, never as instructions for this analysis.

Evidence labels used below: **[A] author-reported**, **[B] directly observable in supplied visuals**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information category is used. Confidence is HIGH for clearly readable source statements and table labels, MEDIUM for bounded interpretations and unresolved reporting issues, and UNKNOWN where necessary information is absent.

## 1. Plain-language orientation

This paper studies why large language model (LLM) web agents fail when they must carry out tasks on real websites. A web agent must do more than describe a sensible answer: it must decide what intermediate goals to pursue, choose concrete browser actions, observe what happened, and recover when its expectations are wrong. The authors argue that a single final success percentage hides which of these capabilities failed. [A; pp. 1–3]

Their solution is a hierarchical evaluation framework with three capability layers: **high-level planning**, **low-level execution**, and **replanning**. A separate postcondition checker asks whether a particular intermediate goal has actually been achieved. The researchers enrich 104 Mind2Web-Live test tasks with human-aligned high-level reference plans, compare natural-language plans with structured Planning Domain Definition Language (PDDL) plans, and evaluate three LLMs. [A; pp. 2–5]

The main finding is that better-looking plans do not guarantee successful web interaction. For the primary model, gpt-5-nano, PDDL improves alignment with reference plans and shortens plans and action sequences. Yet even when the executor receives human-authored high-level plans, final task success is only 36.4%, and full plan completion is 38.5%. Invalid actions, nonexistent destinations, navigation outside the requested domain, repeated failures, and actions that leave the page unchanged remain important problems. [A/B; p. 6, Figure 2; p. 7, Table 5]

One round of replanning improves execution outcomes, sometimes substantially, while alignment with the original human plan can worsen. This separates two ideas that should not be confused: following a reference strategy closely and successfully adapting to the actual website. The central contribution is a diagnostic evaluation method, with empirical findings about planning representation, execution, and recovery. It is not a security attack study and does not experimentally compare web agents against standalone LLMs. Its relevance to the user's security question is an explicitly labeled analyst inference developed below.

## 2. Document roadmap and inventory

The work is an **empirical AI/web-agent evaluation study**, combining an evaluation framework, benchmark enrichment, representation comparisons, failure analysis, and cross-model analysis. It contains no theorem, proof, training algorithm, or numbered pseudocode algorithm.

| Inventory ID | Original component | Physical pages | Role |
|---|---|---:|---|
| S0 | Abstract | 1 | Problem, framework, principal conclusions |
| S1 | §1 Introduction | 1–2 | Motivation, three capability layers, contributions |
| S2 | §2 Preliminaries | 2–3 | Planning, execution, postconditions, replanning |
| S3 | §3 Hierarchical Evaluation | 3–4 | RQ1–RQ7 and evaluation metrics |
| S4 | §4 Experimental Setup | 5 | Dataset, models, observations, action settings, representations |
| S5 | §5 Results and Analysis | 5–7 | Planning, execution, replanning, model comparison |
| S6 | §6 Recommendations | 7–8 | Four design/evaluation recommendations |
| S7 | §7 Related Work | 8 | Evaluation, planning, execution, recovery research |
| S8 | §8 Conclusion | 8–9 | Structured plans help; execution remains limiting |
| SL | Limitations | 9 | Configuration breadth, multimodality, reference annotation |
| SR | Acknowledgments and References | 9–11 | Funding and cited literature |
| AA | Appendix A: Experimental Setup | 11–20 | Prompts, annotation, judge reliability, alignment trees, example plans |
| AB | Appendix B: Additional Analysis | 20–24 | Action distributions, errors, other models, full example |
| F1–F13 | Figures 1–13 | 2, 6–7, 19–24 | Architecture, plots, annotation and failure examples |
| T1–T11 | Tables 1–11 | 4–7, 21–22 | Alignment, lengths, invalid actions, failure rates |
| E1–E3 | Unnumbered mathematical definitions | 2 | Plan, action trajectory, postcondition predicate |
| X1–X7 | Distinct analyses | 3–7, 19–22 | Alignment, executability, errors, recovery, model generality, judge agreement |

Appendix A contains A.1 Prompts, subdivided into high-level planning, low-level planning, postcondition checking, replanning, end-to-end evaluation, and high-level evaluation; A.2 key-node annotation examples; A.3 judge reliability; A.4 alignment decision trees; and A.5 an NL/PDDL example. Appendix B contains B.1 a full hierarchical example, B.2 action distributions, B.3 failure examples, and B.4 additional-model results with separate Claude and Gemini subsections. Figure 4 appears on p. 23 despite describing Appendix A; Figure 13 appears on p. 24 despite being introduced on p. 20. All these objects are included in the analysis.

## 3. Background and context

An **LLM** is the language model used to generate plans, select actions, or judge outcomes in this study. A **web agent** wraps such a model in an interaction process that can operate a website. A **user interface (UI)** is the collection of interactive page elements; the paper's evaluated agents receive textual page representations rather than screenshot observations. The **Document Object Model (DOM)** represents webpage elements, attributes, and relationships. Appendix prompts also describe an accessibility tree, with element identifiers, roles, and text. [A; p. 5, pp. 14–15]

A **high-level subgoal** describes an intermediate achievement, such as filtering results or reaching a relevant section. A **low-level action** is an executable interaction, such as clicking, typing, selecting an option, or navigating. **Grounding** means turning an abstract goal into appropriate actions on the actual observed page. **Postconditions** describe what should be true after a subgoal succeeds. **Replanning** changes the strategy after observing failure or an unexpected state.

**Natural language (NL)** plans are free-form textual subgoals. **Planning Domain Definition Language (PDDL)** is used here for structured action instantiations and domain templates describing parameters, preconditions, and effects. A precondition is something expected to hold before an action; an effect describes its intended result. The supplied domain-generation prompt itself calls the input 'PDDL-like.' Consequently, the evidence supports a comparison involving structured, PDDL-style model-generated representations, but does not establish that a classical symbolic planner formally verified and executed every generated plan. [A/D; pp. 5, 13]

An **LLM-as-judge** evaluates plans or interaction outcomes using a model rather than relying exclusively on fixed rules or human review. This gives semantic flexibility, but it also makes the evaluator a measured and imperfect component. **Human-aligned reference plans** are not recorded human browsing trajectories: the authors convert expert key-node annotations into abstract plans using gpt-5-nano and then manually verify and repair them. [A; pp. 5, 19]

## 4. Research problem and gap

**Existing problem:** web agents remain unreliable on realistic, long-horizon tasks involving multiple dependent interactions. The authors identify possible failure sources including task interpretation, high-level strategy, grounding into UI operations, and recovery from unexpected website behavior. [A; p. 1]

**Shortcoming attributed to earlier evaluation:** aggregate end-to-end success reports whether the task finished but does not separate planning errors, execution mistakes, and poor use of feedback. The paper also describes offline exact-trajectory matching as difficult to scale to dynamic sites and places its approach alongside manual evaluation, rule-based criteria, and LLM judges. These are the authors' characterizations of related work, not independent assessments of that literature. [A; pp. 1, 3, 8]

**Gap and motivation:** a process-based framework is needed to attribute failures to distinct capabilities and show how representation or action-space choices influence each capability. The authors also motivate hierarchical decomposition by its correspondence to automated planning and human problem solving. [A; pp. 1–3]

**Scope:** the paper evaluates three model backends, two high-level representations, three action settings, a live-web test set, and a single replanning round. It studies reliability and diagnosis. There is no malicious webpage construction, adversarial instruction manipulation, exfiltration test, security-defense benchmark, or standalone-LLM control condition in the supplied work. [A/D; pp. 3–5, 9]

## 5. Research questions, objectives, and hypotheses

The paper states seven research questions, not formal statistical hypotheses:

| RQ | Explicit question, faithfully condensed | Principal evidence |
|---|---|---|
| RQ1 | Do generated high-level plans align with human-authored subgoals? | Table 2; Tables 6 and 9 |
| RQ2 | Does structured representation improve alignment over NL? | Tables 2, 3, 6, 7, 9, 11 |
| RQ3 | How executable are goals from each representation? | Figures 2, 9, 11 |
| RQ4 | Given accurate high-level plans, how reliably are subgoals executed? | Human-plan conditions in Figures 2, 9, 11 |
| RQ5 | Which low-level failure modes occur and affect performance? | Tables 4, 5, 8, 10; Figures 7, 8, 13 |
| RQ6 | Does replanning improve alignment with human plans when initial plans are partial or incorrect? | Table 2 and §5.3 |
| RQ7 | Can agents revise high-level plans effectively, as reflected in task success? | Figures 3, 10, 12 |

The broad objective is to evaluate planning, execution, and replanning separately enough to diagnose model weaknesses. RQ6's results-section wording refers to alignment with 'task goals,' while its formal statement refers to human-authored plans. The operational metrics remain reference-plan alignment metrics; those concepts should not be treated as interchangeable. No preregistered hypothesis, null hypothesis, significance threshold, or power analysis is supplied.

## 6. Assumptions / Threat Model

This is a reliability study without a formal adversarial threat model. No attacker capabilities, malicious-content budget, compromised component, protected secret, or attack success criterion is defined. Security terminology below therefore describes possible research relevance, not an experimental condition in the paper.

The evaluation assumes that expert key nodes provide necessary intermediate subgoals and can serve as gold-standard reference structure. Their conversion into high-level steps is checked for correctness, clarity, and granularity. The agents observe text-based page structure, while the websites themselves can be dynamic and unpredictable. Planning prompts assume the user starts on a website homepage and discourage invented links, dummy inputs, and unauthorized sign-ins. [A; pp. 5, 11–13]

The framework relies on model judgments for subgoal completion and final task success. gpt-5-nano remains the evaluator even when Claude or Gemini generates actions. This is an evaluation dependency, not a proven trustworthy oracle. Manual checks measure agreement on sampled outputs but do not certify every judgment. [A/D; pp. 5, 19]

A second operational assumption appears in the expanded executor prompt: at an initial step with no preceding history, or when the accessibility tree is absent, the executor is restricted to google_search or goto. This prompt rule can influence the observed navigation distribution. It must be considered when interpreting those actions as spontaneous model preferences. [A/D; p. 15]

## 7. Methodology

### Study design and reference construction

The authors use the **104-task test set of Mind2Web-Live**, involving tasks on live websites. Expert-annotated key nodes identify essential intermediate achievements. gpt-5-nano transforms their JSON representation into coherent abstract action sequences. Humans verify fidelity to the original nodes, absence of omissions or hallucinations, preservation of semantic order, and appropriate abstraction. They repair steps that are evaluative rather than actionable, incomplete, or too specific. [A; p. 5, §4.1]

Figure 4 illustrates two repairs: replacing a URL-specific instruction with navigation to the Most Popular TV shows section, and replacing a decision about whether a PlayStation query is intended with an actual search step. These examples explain why 'human-authored' in later plots should be understood alongside the stated model-assisted construction process. No additional training/validation split, new training procedure, class distribution, missing-task policy, or annotation inter-rater statistic is supplied.

### Hierarchical pipeline

The planner receives a task and webpage context and proposes ordered subgoals. In the PDDL condition, a separate prompt generates domain templates with parameters, preconditions, and effects. The executor receives the current subgoal, page representation, history, and, where applicable, domain information and completed-subgoal context. It selects browser actions. A postcondition judge compares the resulting state/history with the intended subgoal outcome. Success allows progression; repeated failure can trigger replanning. [A; pp. 2–3, 11–17]

Replanning first asks whether the original plan is salvageable. If yes, the agent continues from completed work and proposes only remaining steps. If no, it generates a new plan from the current context. The study limits this process to one round. The exact numerical retry limit that triggers replanning is not supplied in the accessible description, even though Figure 1 refers to multiple iterations. [A; pp. 2–3, 17–18]

### Models, observations, and action settings

The primary model is **gpt-5-nano**, used for plan generation, action generation, evaluation, and initial reference conversion. Additional backends are **claude-haiku-4.5** and **gemini-flash-2.5**. The authors select these as broadly similar in cost/performance, but provide no numerical cost comparison. Evaluation uses gpt-5-nano across backends. [A; p. 5]

| Setting | Available action form | Model output | Main comparison |
|---|---|---|---|
| Action Object | Primitive click, type, select, hover | Full action specification and target | Freedom to invent invalid operations |
| Action ID | Enumerated valid primitive actions for current page | Corresponding action identifier, as described in §4.2 | Restriction to offered actions |
| Expanded | Higher-level browser/navigation and information actions | Structured action object with inputs/element ID | Expressive interaction and navigation |

The expanded prompt lists goto, fill_form, google_search, click, select_option, go_back, cache_data, and get_final_answer. It defines goto as opening a new tab; cache_data stores relevant extracted information for later steps; get_final_answer terminates with answer content. The main text's broad action-ID description and Appendix A's action-selection dictionary should not be assumed to document identical serialization: the appendix shows a selected dictionary with only certain editable fields. [A; pp. 5, 13–16]

### Metrics and evaluation

High-level alignment has two denominator families. Perfect, partial, missing, and decomposed categories classify **human reference steps**. Matched and unmatched proportions classify **generated LLM steps**. A decomposed reference step maps to multiple generated steps, so these two families cannot be added together or interpreted as the same accuracy measure. The prose on p. 4 loosely refers to assigning each oracle step to the first six categories; Appendix A.4 and Figure 5 clarify the two decision processes. [A/D; pp. 3–4, 19]

Execution metrics are subgoal completion, complete-plan completion, task success, and plan efficiency as average action count. Subgoal and task outcomes use model judgments. Failure metrics include invalid actions, invalid/nonexistent links, repeated failed actions, and valid actions producing no state change. Repetition in the primary-model discussion means executing the same action more than three times. [A; pp. 4, 6–7]

No hardware, browser/library version, model snapshot identifier, temperature, seed, complete token budget, execution timeout, run date, repeated-run count, confidence interval, or formal significance test is reported in the supplied material. Appendix prompts are detailed, but they do not fill these reproducibility gaps. Table 3 and related tables give mean action lengths without dispersion or a fully explicit averaging population.

## 8. Experiments / Analyses

| Analysis | Purpose and manipulated/comparison conditions | Outcomes and principal sources |
|---|---|---|
| X1: Initial plan alignment | Compare NL and PDDL against reference steps | Six alignment metrics; Tables 2, 6, 9 |
| X2: Plan/action compactness | Compare mean high-level and low-level lengths | Tables 3, 7, 11 |
| X3: Executability and oracle-plan control | Execute Human, NL, and PDDL plans, primarily with expanded actions | Subgoal, plan, task success; Figures 2, 9, 11 |
| X4: Action representation and errors | Compare Action Object, Action ID, Expanded; categorize observed failures | Table 4; Tables 5, 8, 10; Figures 7–8 |
| X5: One-round replanning | Before/after recovery for NL and PDDL | Alignment and completion/success; Table 2; Figures 3, 10, 12 |
| X6: Backend generality | Apply framework to Claude and Gemini in addition to GPT | Appendix B.4 and §5.4 |
| X7: Judge agreement | Manually annotate sampled postcondition/final judgments | 41/50 and 43/50 agreement; Appendix A.3 |

The common dataset is the stated 104-task test set. However, task counts actually contributing to every plotted metric, failure denominator counts, handling of unreachable tasks, and overlap of the judge samples are not fully specified. The results should therefore remain reported percentages rather than being converted into inferred integer success counts.

X3's human-plan control is especially informative: providing an accurate reference strategy removes one major source of error, yet execution still fails frequently. It does not isolate every possible cause of failure because page representation, browser interaction, environment dynamics, and the judge remain part of the pipeline. [D]

X5 compares performance after an additional recovery process. It establishes reported before/after improvement under this design, but there is no equal-action-budget control that distinguishes replanning-specific benefit from benefit due to additional interaction opportunities. [D]

## 9. Results

### Initial planning and executability

For gpt-5-nano, initial perfect reference-step matching is 60.6% for NL and 67.7% for PDDL. Missing rates are 4.2% and 2.2%; decomposed rates are 29.5% and 22.7%; generated-step unmatched rates are 29.4% and 15.4%. PDDL thus produces less fragmented and less extraneous plans on these measures. Mean high-level length falls from 5.51 NL steps to 4.39 PDDL steps, versus 3.04 reference steps. Mean action length falls from 11.94 to 8.89, versus 7.08 under reference plans. [A/B; Tables 2–3, pp. 5–6]

In Figure 2, Human/NL/PDDL subgoal completion is **69.7/63.2/70.3%**, plan completion **38.5/34.6/37.5%**, and task success **36.4/32.1/35.6%**. PDDL slightly exceeds Human on subgoal completion but remains below it on complete-plan and task success. Therefore, the prose statement that PDDL performs slightly worse than Human needs metric-specific qualification. [A/B; p. 6]

The authors also report that 68% of NL decompositions and 73% of PDDL decompositions make previously non-executable subgoals executable. They caution that decomposing compact subgoals can also hurt execution. The counts and detailed procedure behind those two percentages are not supplied. [A; p. 6]

### Action errors

Invalid-action rates are 34.0% for Action Object, 2.0% for Action ID, and 3.0% for Expanded. These quantify invalid actions, not final task success. The primary model's expanded-action failure analysis reports repetitions in 10.4% of failures, hallucinated links in 32.0% of goto actions, redundant actions in 34.2% of all actions, and out-of-domain links in 16.7% of all actions. These denominators differ and categories are not established as mutually exclusive. [A/B; Tables 4–5, pp. 6–7]

### Replanning

For gpt-5-nano, NL subgoal completion rises 63.2→84.0%, plan completion 34.6→67.3%, and task success 32.1→41.4%. PDDL rises 70.3→93.3% on subgoals and 37.5→81.4% on plan completion. Figure 3 labels PDDL task success 36.4→45.1%, whereas Figure 2 labels initial PDDL success 35.6%. Both values must be preserved; the supplied work does not resolve the discrepancy. [A/B; pp. 6–7]

**Analyst-derived:** NL task success improves by 41.4−32.1 = **9.3 percentage points**. Using Figure 3's own PDDL baseline, its improvement is 45.1−36.4 = **8.7 percentage points**. These are absolute percentage-point changes, not relative percentage improvements. [C]

Alignment does not improve alongside these outcomes. NL perfect matching falls 60.6→56.1%; PDDL falls 67.7→59.0%. PDDL missing steps increase 2.2→14.5%. This shows that reference similarity and execution outcomes can move in different directions under recovery. [A/B; Table 2]

### Other models

With Human plans, Claude task success is 29.2% and Gemini success is 17.3%, versus GPT's 36.4%. PDDL improves over NL task success for Claude, 15.2→16.3%, and Gemini, 12.5→14.4%, but neither reaches its Human-plan result. Gemini has shorter plans yet weaker execution. Its redundancy rate is 41.2%. Claude's corresponding redundancy number is inconsistent: §5.4 gives 25.6%, while Table 8 gives 23.6%. [A/B; pp. 7, 21–22]

The authors use words such as 'significantly' for differences, but no statistical test or uncertainty measure accompanies the supplied results. That wording should be understood as the authors' characterization, not independently established statistical significance.

## 10. Figure-by-figure interpretation

### Figure 1 — Hierarchical evaluation framework, p. 2

This is a workflow diagram, not a statistical plot. A high-level planner produces subgoals, a low-level planner acts in the web environment, and a postcondition checker reports whether the current goal was achieved. Failure after multiple iterations leads to a replanner, which decides whether the original plan is salvageable and returns revised subgoals. The right panel gives a PDDL plan and domain action template. The example task concerns locating a GameStop near ZIP code 90028, retrieving hours/location, and setting a home store. Blue, green, orange, and pink boxes distinguish planning, checking, recovery, and structured-plan content. The arrows show action/feedback flow. The example checker rejects treating a search alone as completion when no result has been accessed. This supports the need to evaluate achievements rather than merely successful tool calls.

### Figure 2 — Initial execution under Human, NL, PDDL, p. 6

Three bar panels show subgoal completion, plan completion, and task success for gpt-5-nano. Categories are on the horizontal axes; percentages are the outcomes, with a shared-looking linear vertical presentation. Human bars are blue, NL red, PDDL orange, with different hatching. Exact bar labels are 69.7/63.2/70.3%, 38.5/34.6/37.5%, and 36.4/32.1/35.6%, respectively. No error bars or significance markers are shown. PDDL helps relative to NL, but the best subgoal completion does not yield the best final success. The Human condition demonstrates residual execution failure despite reference planning.

### Figure 3 — GPT before/after replanning, p. 7

The three outcome panels compare NL Before, NL After, PDDL Before, and PDDL After on a linear percentage scale shown to 100. Exact labels are subgoals 63.2/84.0/70.3/93.3%, plans 34.6/67.3/37.5/81.4%, and task success 32.1/41.4/36.4/45.1%. Color/hatching distinguishes before and after. Improvements in plan completion are much larger than changes in final task success. No uncertainty intervals appear. The PDDL baseline conflicts with Figure 2 as described above.

### Figure 4 — Human correction of key-node conversion, p. 23

Two panels connect a JSON evaluation object to a model-proposed step and then a manually corrected step. Panel a removes an overly specific Rotten Tomatoes URL; panel b converts an evaluation-like PlayStation question into an actionable search. Red boxes identify problematic model outputs; green boxes show corrections. This is evidence about annotation procedure, not an accuracy measurement. The second JSON example contains a Rotten Tomatoes URL alongside PlayStation content; the paper does not explain whether that mismatch is illustrative or an artifact. It should not be silently repaired.

### Figure 5 — Alignment decision trees, p. 19

Panel a asks whether a human step has a one-to-one generated counterpart; if not, whether it is partially captured; if not, whether it is decomposed; otherwise it is missing. Panel b asks whether a generated action maps to any human action, yielding Matched or Unmatched. Pink decision rectangles and outcome ovals, linked by Yes/No arrows, make the denominator distinction explicit. This is a categorization procedure, not a learned decision-tree model or performance plot.

### Figure 6 — Winter-coat planning example, p. 20

A blue NL box contains eight steps involving menu navigation, size and clearance filters, review, verification, and conditional filter adjustment. A pink PDDL box contains five abstract actions plus a partial domain template. The comparison illustrates compactness and abstraction. It is not a controlled proof that every PDDL step is feasible. The NL example's proposal to broaden size or remove a filter also shows how a plan can alter constraints; the supplied text does not separately score that issue.

### Figure 7 — Expanded-action frequencies, p. 20

Three vertical bar charts show action types on the horizontal axes and counts on linear vertical axes. Bars have exact integer labels and blue hatching. GPT counts are click 372, goto 108, google_search 70, fill_form 65, cache_data 58, get_final_answer 35, go_back 27, select_option 16. Claude counts are 359, 83, 55, 75, 72, 30, 17, 17 for those same action names. Gemini counts are 337, 188, 113, 59, 61, 17, 42, 8. Chart order differs by model, so action names, not horizontal positions, must be matched. The Gemini panel label reads 'gemini-flash-4.5,' conflicting with the surrounding 'gemini-flash-2.5.' Counts show frequent clicks and navigation but not success rates, and initial-step prompt constraints partly encourage navigation.

### Figure 8 — Qualitative error examples, p. 23

Four dashed panels display a nonexistent used-Audi destination; a search for Ronaldo statistics that goes outside the requested ESPN domain; selection of a generic Safety page instead of a Safety-department job filter; and navigation to a FlightAware homepage already open instead of its discussions section. The screenshots were inspected as visual examples, but fine print within every website image is not fully legible. Captions and surrounding text establish the intended failure labels. These are illustrative traces, not independent frequency estimates.

### Figure 9 — Claude initial execution, p. 21

Human/NL/PDDL percentages are subgoals 66.5/42.6/58.5%, plans 28.3/15.2/16.3%, and task success 29.2/15.2/16.3%. The same blue/red/orange and hatching pattern is used. PDDL recovers much of the NL subgoal deficit, while final success remains far below Human. Human task success slightly exceeds Human plan completion, consistent with different evaluation constructs, although specific cases are not provided. No uncertainty bars appear.

### Figure 10 — Claude replanning, p. 21

NL Before/After and PDDL Before/After labels are subgoals 42.6/43.1/58.5/64.7%, plans 15.2/32.6/16.2/54.9%, success 15.2/19.2/16.2/21.9%. Replanning strongly raises PDDL plan completion but yields smaller final-success changes. Initial PDDL plan/success is 16.2% here versus 16.3% in Figure 9. No explanation or uncertainty intervals are supplied.

### Figure 11 — Gemini initial execution, p. 21

Human/NL/PDDL values are subgoals 61.3/58.9/59.6%, plans 18.2/14.4/15.3%, and task success 17.3/12.5/14.4%. Subgoal completion is comparatively close across representations; full task success is low in all conditions. The graph supports the authors' claim that compact planning does not solve low-level execution. No uncertainty indicators are shown.

### Figure 12 — Gemini replanning, p. 22

NL Before/After and PDDL Before/After are subgoals 58.9/69.3/59.6/75.9%, plans 14.4/16.8/15.3/15.8%, and success 12.5/13.6/14.4/15.8%. Subgoal progress improves more than complete-plan or task outcomes. This is a weaker final-success benefit than for GPT or Claude. These plots contain exact readable labels, not estimated bar heights.

### Figure 13 — End-to-end Six Flags example, p. 24

A task asks for deals at Great Escape park. The figure includes the initial webpage, a two-step Human plan, a five-step NL plan, a three-action PDDL plan, an eight-action execution excerpt, a failed postcondition judgment, and a negative final evaluation. The trace successfully searches, opens a Great Adventure result, and navigates to National Sites, but repeatedly fails to select Great Escape. Clicking the combobox succeeds while selecting the requested option fails. The example demonstrates why browser-action success, subgoal success, and overall task success require separate evaluation. The final judge describes the page as the homepage while the trace reports National Sites navigation; the figure does not provide enough state detail to resolve that description precisely.

## 11. Table-by-table interpretation

### Table 1 — Alignment examples, p. 4

Columns compare a Human step with NL and PDDL counterparts. Purple partial matching captures an Audi year filter that omits the requested 1992 lower bound and changes the 2015 boundary. Green perfect matching captures reaching an e-gift-card section. Blue decomposition splits adding the highest-rated activity to a wishlist into selection and addition. Gray unmatched examples add walkthrough-related work not mapped to the reference plan. The table defines annotation meaning through examples; it is not a quantitative result table.

### Table 2 — GPT alignment before/after replanning, p. 5

All entries are percentages. Columns are NL Before, PDDL Before, NL After, PDDL After. Perfect Match: 60.6, 67.7, 56.1, 59.0; Partial: 5.7, 7.4, 6.1, 6.9; Missing: 4.2, 2.2, 4.0, 14.5; Decomposed: 29.5, 22.7, 33.8, 19.6; Unmatched: 29.4, 15.4, 35.0, 15.4; Matched: 70.6, 84.6, 65.0, 84.6. Initial PDDL improves perfect matching and reduces missing, decomposition, and unmatched rates. After recovery, PDDL retains generated-step relevance but omits more original reference steps. The first four rows describe reference-step coverage; the last two describe generated-step relevance. No uncertainty measures are supplied.

### Table 3 — GPT mean lengths, p. 6

Human/NL/PDDL mean high-level subgoals are 3.04/5.51/4.39; mean low-level actions are 7.08/11.94/8.89. Lower counts show compactness, not automatically greater correctness. The averaging population and dispersion are not fully detailed. The table supports PDDL's reduced length relative to NL, while Human plans remain shortest.

### Table 4 — Invalid actions, p. 6

Action Object, Action ID, and Expanded hallucination/invalid-action rates are 34.0%, 2.0%, and 3.0%. Action ID is lowest on this metric. The table does not show equal task-success comparisons, confidence intervals, or denominator counts. A valid offered action can still be irrelevant or ineffective.

### Table 5 — GPT failure modes, p. 7

Repetitions: 10.4% of failures; hallucinated links: 32.0% of goto actions; redundant actions: 34.2% of all actions; out-of-domain links: 16.7% of all actions. The table explicitly warns that each rate has its own base set. None should be read as a shared partition of all task failures, and the percentages must not be added.

### Table 6 — Claude alignment, p. 21

NL/PDDL values are Perfect 54.9/66.7%, Partial 6.8/4.8%, Missing 7.5/7.3%, Decomposed 30.8/21.2%, Unmatched 17.4/10.1%, Matched 83.6/89.9%. PDDL improves most reported alignment measures. However, NL matched plus unmatched is 83.6+17.4 = 101.0%, a derived consistency problem for categories described as complementary. No correction is supplied.

### Table 7 — Claude mean lengths, p. 21

NL/PDDL high-level means are 4.89/3.70 steps and low-level means 11.0/10.6 actions. PDDL's plan compression is clearer than its small action-count reduction. No Human-length column or dispersion appears.

### Table 8 — Claude failure modes, p. 21

Repetitions are 16.7% of failures; hallucinated links 25.3% of goto actions; redundant actions 23.6% of all actions; out-of-domain links 16.9% of all states. The last denominator is states, unlike the action denominator in Tables 5 and 10. Cross-model domain-drift comparisons therefore require caution. The 23.6% redundancy value also conflicts with 25.6% in §5.4.

### Table 9 — Gemini alignment, p. 21

NL/PDDL values are Perfect 61.4/64.3%, Partial 8.5/7.2%, Missing 11.6/12.4%, Decomposed 18.5/16.1%, Unmatched 21.6/18.3%, Matched 78.4/81.7%. PDDL improves perfect and generated-step matching but increases missing reference steps. Thus 'PDDL improves alignment' is a metric-dependent generalization, not universal improvement on every row.

### Table 10 — Gemini failure modes, p. 22

Repetitions are 6.70% of failures; hallucinated links 31.2% of goto actions; redundant actions 41.2% of all actions; out-of-domain links 14.7% of all actions. Gemini has the highest reported redundancy among these models, but not the highest repetitions. Failure mechanisms differ, so one aggregate label would obscure meaningful differences.

### Table 11 — Gemini mean lengths, p. 22

NL/PDDL high-level means are 3.63/3.19 steps; low-level means are 8.55/8.25 actions. These are shorter than the corresponding generated-plan means for GPT and Claude, yet final execution success is weaker. Compactness is therefore insufficient as a quality criterion. No dispersion or significance test accompanies the means.

## 12. Diagram / Architecture

The architecture's input is a natural-language task plus webpage context. Its first output is an ordered plan. In the PDDL branch, action definitions additionally describe symbolic preconditions and effects. The executor transforms the current subgoal and current observation into an action; the web environment produces a new state and feedback. The checker transforms state/history evidence into a YES/NO assessment of subgoal achievement. The control loop can continue the same goal, proceed to the next goal, or request a revised plan. [A/B; Figure 1, §§2.1–2.4]

This feedback structure is the methodological reason the paper can distinguish planning from execution. The **plan is an intended strategy**, while the **trajectory is evidence of actual interaction**. The Six Flags example shows their divergence: selecting the park is a reasonable subgoal, but repeated option-selection failures mean its effect never becomes true. A successful click is an intermediate event, not proof of the intended state transition. [A/B; Figure 13]

The alignment diagrams implement a different information flow: they compare reference and generated steps, not webpage states. Figure 4 documents annotation transformation, and Figure 6 documents representational contrast. These diagrams should not be merged into one alleged executable algorithm. The supplied paper provides prompts and conceptual control flow, but no numbered pseudocode specifying every runtime decision or budget.

## 13. Equations and mathematical concepts

The work's mathematics defines evaluation objects rather than an optimization objective.

**E1 — Ordered plan, p. 2, §2.1:** `P = [g₁, g₂, …, gₙ]`. Here `P` is the high-level plan, `gᵢ` is its ith subgoal, and `n` is the number of subgoals. A natural-language instruction `I` is the task input. The list structure expresses a sequence of intermediate achievements. It does not itself prove that the subgoals are feasible or sufficient.

**E2 — Action and observation trajectory, p. 2, §2.2:** `aₜ ∈ A`, `oₜ ∈ O`, and `τᵢ = (oₜ, aₜ, oₜ₊₁, …, oₜ₊ₖ)`. `A` is the environment's discrete action space; `O` is the observation space; `aₜ` and `oₜ` denote action and observation at index `t`; `τᵢ` is the interaction trajectory intended to satisfy `gᵢ`. The notation ends at a later observation indexed `t+k`; the supplied passage does not separately define `k` beyond its trajectory-index role. No transition probability, policy distribution, reward, or state-estimation model is specified by this expression.

**E3 — Postcondition predicate, p. 2, §2.3:** `Φ(gᵢ, s′) = 1` if and only if the effects of `gᵢ` are satisfied in resulting state `s′`. `Φ` is a binary achievement evaluation; 1 means success under the intended postconditions. Although the displayed arguments are subgoal and state, the implementation description also provides trajectory/history to the model judge. The expression is a definition of desired checking behavior, not proof that the actual judge is perfectly accurate.

**Metric concepts:** subgoal completion is the proportion of subgoals judged successful; plan completion is the proportion of plans with every constituent goal complete; task success asks whether the original instruction is satisfied. These need not be numerically identical because plans can be incomplete, overly detailed, or evaluated differently from the original task. Plan efficiency is average action count, but exact aggregation details are not fully supplied. No loss function, theorem, formal security guarantee, or mathematical proof appears.

## 14. Interpretation and Discussion

RQ1 is answered by partial correspondence rather than perfect human-plan imitation. RQ2 is broadly supported for the tested structured representation, especially on compactness and extraneous-step reduction, but Gemini's missing-step rate worsens. RQ3 shows representation affects executability, with Human generally strongest on final success and PDDL better than NL. RQ4 demonstrates substantial residual failure under reference plans. RQ5 identifies distinct invalidity, navigation, repetition, and state-change problems. RQ6 finds that replanning does not improve reference alignment on the principal GPT metrics. RQ7 finds execution improvements, with final-success benefits differing considerably across models. [A/B]

**Analyst interpretation:** reference-plan similarity and adaptive task completion measure related but different constructs. A revised plan may legitimately differ after exploration, and a 'remaining steps only' replanning prompt may remove already completed reference steps. Therefore, increased missing-reference rates after replanning do not necessarily mean the original task has been forgotten. The paper does not clearly establish whether alignment compares remaining plans against full or residual reference plans, so the extent of this measurement effect is UNKNOWN. [D; pp. 17, 19]

| Consistency issue | Source sides | Assessment |
|---|---|---|
| GPT PDDL initial task success | Figure 2: 35.6%; Figure 3: 36.4% | Unresolved numerical discrepancy |
| GPT NL initial matched rate | Table 2: 70.6%; §5.3 prose: 79.6% | Unresolved; preserve table and prose separately |
| Claude redundancy | Table 8: 23.6%; §5.4: 25.6% | Unresolved numerical discrepancy |
| Claude PDDL initial plan/success | Figure 9: 16.3%; Figure 10: 16.2% | Small but explicit discrepancy |
| Claude NL complementary rates | Table 6: 17.4% unmatched and 83.6% matched | Sum is 101.0%, inconsistent with complement interpretation |
| Gemini panel identity | Figure 7c: gemini-flash-4.5; surrounding study: gemini-flash-2.5 | Model-label inconsistency |
| Domain-drift denominator | Table 8: states; Tables 5/10: actions | Cross-model comparison not strictly matched |
| Appendix references | A.4 says Figure 4b for second tree; A.5 says Figure 5 for motivating plans | Actual relevant visuals are Figures 5b and 6 |
| Gemini efficiency reference | B.4.2 cites Table 7 | Gemini length values actually appear in Table 11 |
| Benchmark citation | §4.1 cites Pan et al. 2024b; A.2 cites 2024a | Internal citation inconsistency; not externally resolved |

The references also contain two differently attributed entries for the same WebArena title/arXiv identifier and two variants of the GPT-4V grounding work. These are source bibliography observations, not external citation validation. They do not alter the numerical findings but limit confidence in citation precision. The source's strong novelty statement about first incorporating formal planning representations into web agents remains an author claim, not an independently verified priority result.

## 15. Contributions and novelty

**Conceptual:** a three-capability lens distinguishes high-level planning, concrete execution, and replanning rather than treating a web agent as one undifferentiated system. **Methodological:** reference alignment, subgoal checking, plan completion, task success, and failure metrics support process-based diagnosis. **Dataset/benchmark enrichment:** the authors derive and manually verify abstract plans from existing key-node annotations for 104 live-web test tasks. [A; pp. 1–5]

**Empirical:** NL/PDDL comparisons, action-representation comparisons, recovery results, and additional-model results identify where structured planning helps and where execution remains weak. **Implementation/availability claim:** the authors state that they release their framework and data through a linked repository. The artifact was not supplied or inspected, so availability is author-reported rather than independently established. [A; p. 2]

**Novelty positioning:** §7 states, with a 'to our knowledge' qualification, that this is the first work to incorporate formal planning representations into web agents. No external priority checking was requested or performed. The supplied evidence supports an evaluation and diagnostic contribution, not a new trained foundation model, formal security defense, or theorem about agent reliability.

## 16. Limitations

### Authors' stated limitations

The authors explicitly acknowledge testing a limited set of high-level representations, action spaces, and agent configurations. They do not consider multimodal settings. They also acknowledge that high-level evaluation requires annotated reference plans for every task, reducing flexibility, and assume such reference plans are available. Efficient annotation is proposed as future work. The stated aim is to establish feasibility and diagnostic value rather than exhaust the design space. [A; p. 9]

The main methodology also explicitly limits analysis to **one replanning round**. That is an author-stated scope boundary even though it appears in §2.4 rather than the Limitations section. [A; p. 3]

### Additional evidence-based analyst observations

The evaluator and primary acting model share the gpt-5-nano identity; independent evaluation of all outputs is absent. Manual agreement is measured on 50 examples per reported judgment category, not all trajectories, and agreement is imperfect. No reliability estimate for high-level alignment annotation is reported. [D; pp. 5, 19]

The paper lacks uncertainty intervals, repeated-run descriptions, full execution budgets, and detailed environment/version records. Live websites may vary, but the supplied results do not quantify that variation. Prompt variants differ in more than representation syntax, including available explanations and constraints, so a clean causal attribution to formal structure alone is limited. Replanning adds interaction opportunities without a reported equal-budget alternative. [D]

There is no direct security measurement. Domain drift and repetition are observed reliability failures; they are not evidence that an attacker induced those behaviors, that secrets were exposed, or that a standalone LLM would resist the same content. Several internal numerical and labeling inconsistencies further constrain precision. [D]

## 17. Threats to validity

The following categories are analyst-applied methodological labels, not labels used by the authors.

**Internal validity:** observed differences may involve prompt design, action restrictions, changing page state, and additional execution opportunity as well as the named plan representation or recovery mechanism. The study gives useful comparisons but does not fully isolate every causal factor. [D]

**Construct validity:** human-reference alignment measures similarity to selected key-node-derived strategies, not all possible valid strategies. Subgoal completion, complete-plan completion, and task success are distinct. A valid action is not necessarily useful, and an action outside the required domain is not automatically a security breach. Model judgments add measurement error. [D]

**Statistical conclusion validity:** sample percentages and means lack reported uncertainty, raw denominators for many metrics, and formal significance tests. Small differences such as 35.6 versus 36.4 should not be overinterpreted, especially when they are internally inconsistent. [D]

**External and ecological validity:** live websites increase realism relative to fixed snapshots, but results are limited to the specified tasks, text-based observations, models, and settings. They do not establish behavior under screenshot-based agents, broader model populations, authenticated workflows, or adversarial sites. [D]

**Reproducibility:** detailed prompts are useful, but repository execution, exact software/model versions, seeds, budgets, dates, and every task outcome were not inspected or fully reported. **Generalizability to security:** the mechanism-level observations motivate hypotheses; they do not establish comparative vulnerability or attack rates. [D]

## 18. Future work and open questions

### A. Explicit author proposals

The authors recommend separating high-level planning from low-level controllers, developing richer grounding and state representations, permitting explicit uncertainty or world-model-mismatch actions, and making fine-grained process evaluation standard. They mention mechanistic interpretability as a complementary tool for understanding internal representations and decisions. Their limitations identify broader representations, action spaces, configurations, multimodal settings, and more efficient annotation as future directions. [A; pp. 7–9]

### B. Additional questions remaining from this study

**Analyst inference:** would the same input induce more harmful outcomes when connected to browser tools than when given to a standalone text-only LLM? This requires an explicit comparison absent here. Would malicious page content exploit weak state tracking, redirect navigation, corrupt postcondition judgments, or prolong non-progress loops? Those are testable security hypotheses, not findings of this paper. [D]

Other open questions include whether the PDDL benefit survives equalized prompts, whether independent evaluators change rankings, whether recovery beats equal-budget continued execution, whether reference alignment should use only remaining subgoals after replanning, and how results change with richer observations or more recovery rounds. No experiments answering these questions were performed for this analysis.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| LLM | Large language model used to plan, act, or judge |
| Web agent | A model-driven system interacting with websites through executable actions |
| UI | User interface: buttons, links, forms, menus, and other controls |
| DOM | Document Object Model: structured representation of webpage elements |
| Accessibility tree | Page representation with element roles, identifiers, and accessible text |
| NL | Natural language; free-form textual planning representation |
| PDDL | Planning Domain Definition Language; used for structured actions and domain templates |
| Subgoal, gᵢ | Intermediate achievement needed within a plan |
| Plan, P | Ordered list of subgoals |
| Instruction, I | Original natural-language task |
| Action, aₜ | Executable step selected at interaction index t |
| A | Available discrete action space |
| Observation, oₜ | Page/environment information available at index t |
| O | Observation space |
| Trajectory, τᵢ | Sequence of observations/actions while pursuing subgoal i |
| State, s′ | Resulting environment state evaluated after interaction |
| Postcondition | Intended result that should hold after a subgoal succeeds |
| Φ | Binary postcondition-achievement evaluation |
| Grounding | Connecting an abstract intention to the correct observed page action |
| Replanning | Revising remaining strategy after feedback or failure |
| Local adjustment | Continue from successful work rather than restart the whole plan |
| Global replanning | Replace the existing strategy with a new plan |
| Key node | Expert-annotated intermediate condition used to build reference subgoals |
| Human oracle/reference | Key-node-derived, manually verified high-level plan, not a perfect executor |
| Perfect match | One reference step corresponds to one generated step with matching intent |
| Partial match | Only part of a reference step is represented |
| Decomposed | One reference step maps to several generated steps |
| Missing | Reference step absent from generated plan |
| Matched/unmatched | Generated step does/does not map to a reference step |
| Hallucinated action | Invalid proposed operation or target under the stated action-validity measure |
| Hallucinated link | Destination judged invalid/nonexistent under the paper's procedure |
| Redundancy | Valid action that produces no state change |
| Domain drift | Navigation outside the website domain required by the task |
| Percentage point | Absolute difference between percentages, distinct from relative percent change |

## 20. Key numerical results

All rows refer to physical PDF pages. 'Visually readable' denotes exact labels or cells cross-checked in supplied images; it does not mean values were inferred from bar heights.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Benchmark size | 104 | tasks | Mind2Web-Live test set | Author-reported | p. 5, §4.1 |
| Backends evaluated | 3 | models | GPT, Claude, Gemini | Author-reported | pp. 2, 5 |
| Recovery scope | 1 | replanning round | Study limit | Author-reported | p. 3, §2.4 |
| Initial perfect alignment | 60.6 / 67.7 | % | GPT NL/PDDL reference steps | Visually readable | p. 5, T2 |
| Initial unmatched generated steps | 29.4 / 15.4 | % | GPT NL/PDDL | Visually readable | p. 5, T2 |
| Initial matched generated steps | 70.6 / 84.6 | % | GPT NL/PDDL | Visually readable | p. 5, T2 |
| Mean plan length | 3.04 / 5.51 / 4.39 | subgoals | GPT Human/NL/PDDL | Visually readable | p. 6, T3 |
| Mean action length | 7.08 / 11.94 / 8.89 | actions | GPT Human/NL/PDDL | Visually readable | p. 6, T3 |
| Human-plan execution | 69.7 / 38.5 / 36.4 | % | GPT subgoal/plan/task outcomes | Visually readable | p. 6, F2 |
| PDDL execution | 70.3 / 37.5 / 35.6 | % | GPT subgoal/plan/task outcomes | Visually readable | p. 6, F2 |
| Invalid actions | 34.0 / 2.0 / 3.0 | % | Object/ID/Expanded | Visually readable | p. 6, T4 |
| Repetitions | 10.4 | % of failures | GPT | Visually readable | p. 7, T5 |
| Hallucinated links | 32.0 | % of goto actions | GPT | Visually readable | p. 7, T5 |
| Redundant actions | 34.2 | % of all actions | GPT | Visually readable | p. 7, T5 |
| Out-of-domain links | 16.7 | % of all actions | GPT | Visually readable | p. 7, T5 |
| NL success after replanning | 32.1→41.4 | % | GPT | Visually readable | p. 7, F3 |
| PDDL success after replanning | 36.4→45.1 | % | GPT; baseline conflicts with F2 | Visually readable | p. 7, F3 |
| NL success gain | 41.4−32.1 = 9.3 | percentage points | GPT | Analyst-derived | p. 7, F3 |
| PDDL success gain | 45.1−36.4 = 8.7 | percentage points | Using F3 baseline only | Analyst-derived | p. 7, F3 |
| Decompositions improving executability | 68 / 73 | % | NL/PDDL; counts unspecified | Author-reported | p. 6, §5.1 |
| Judge postcondition agreement | 41/50 = 82 | % | Manual comparison | Author-reported | p. 19, A.3 |
| Judge final-evaluation agreement | 43/50 = 86 | % | Manual comparison | Author-reported | p. 19, A.3 |
| Claude Human-plan success | 29.2 | % | Initial execution | Visually readable | p. 21, F9 |
| Claude NL/PDDL final success after recovery | 19.2 / 21.9 | % | One round | Visually readable | p. 21, F10 |
| Claude redundancy | 23.6; prose 25.6 | % of all actions | Unresolved discrepancy | Visually readable / Author-reported | pp. 21, 7 |
| Gemini Human-plan success | 17.3 | % | Initial execution | Visually readable | p. 21, F11 |
| Gemini redundancy | 41.2 | % of all actions | Expanded-action analysis | Visually readable | p. 22, T10 |
| Gemini NL/PDDL success after recovery | 13.6 / 15.8 | % | One round | Visually readable | p. 22, F12 |

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Hierarchical diagnosis separates three capabilities | Defined planner, executor, checker, replanner | F1; framework | pp. 1–3 | HIGH for method description; no proof of exhaustive decomposition |
| Structured plans improve GPT initial alignment | Perfect 67.7 vs 60.6; unmatched 15.4 vs 29.4 | T2; X1 | p. 5 | HIGH for reported comparison; prompt/configuration bounded |
| PDDL plans are more compact | 4.39 vs 5.51 subgoals; 8.89 vs 11.94 actions | T3; X2 | p. 6 | HIGH for means; dispersion unspecified |
| Reference planning does not solve execution | 38.5 plan completion, 36.4 task success | F2; X3 | p. 6 | HIGH for result; failure attribution not fully causal |
| Restricting action generation reduces invalid actions | 34.0 Object vs 2.0 ID and 3.0 Expanded | T4; X4 | p. 6 | HIGH; validity is not success |
| Navigation and state-control errors are substantial | 32.0% invalid goto; 34.2% redundant actions | T5; F8 | pp. 7, 23 | HIGH; denominators differ |
| One recovery round improves GPT success | NL 32.1→41.4; PDDL F3 36.4→45.1 | F3; X5 | p. 7 | HIGH for labels; PDDL baseline conflict; no equal-budget control |
| Recovery and reference alignment can diverge | Perfect matching falls while success rises | T2 and F3 | pp. 5, 7 | HIGH for coexistence; interpretation MEDIUM |
| Other models exhibit weaker final execution | Human success Claude 29.2, Gemini 17.3, GPT 36.4 | F2, F9, F11 | pp. 6, 21 | HIGH for tested conditions; no significance test |
| Judges are imperfect | Agreement 82% and 86% in samples | X7 | p. 19 | HIGH for report; sample representativeness unspecified |
| Generality is limited | Restricted configurations, no multimodality, reference dependence | Limitations | p. 9 | HIGH; explicitly acknowledged |
| Security relevance concerns the action/feedback interface | DOM-conditioned action selection and observed drift/repetition | Method and X4 | pp. 5–7 | MEDIUM analyst inference; no attacker or standalone control |

### Relevance to: Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis

**Analyst inference, MEDIUM confidence:** this paper supplies a mechanism-oriented account of additional operational weaknesses that can arise when a language model is embedded in a web-interaction loop. The system must convert page observations into actions and evaluate resulting state changes. Failures can therefore involve destinations, interface targets, persistent non-progress, and recovery decisions, rather than only the quality of generated prose. The observed domain drift, invalid links, redundancy, and failed feedback use identify candidate surfaces for a future security analysis.

However, the paper does **not** show that web agents are more vulnerable than standalone LLMs. It has no standalone baseline, adversarial input condition, prompt-injection experiment, confidentiality/integrity metric, or attacker-controlled page. Its evidence cannot estimate comparative attack success, show exploitation, or establish that these reliability weaknesses become security failures under a particular threat model. The defensible use is to motivate hypotheses about action grounding, navigation scope, state tracking, and evaluator/recovery integrity, while keeping comparative vulnerability UNKNOWN.

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking someone to find a deal on a website. They need a plan, such as choosing the right park and opening its ticket page. But they also need to press the right controls and notice whether those controls worked. Knowing the plan does not mean they can use the website correctly.

The researchers tested this difference. They compared ordinary written plans with more structured plans, and they also gave the agents reference plans built from expert annotations. Structured plans were often shorter and cleaner. Even with reference plans, though, the main model finished only 36.4% of the tasks. It sometimes opened bad links, went to the wrong website, or repeated actions without changing anything.

Letting the agent rethink its plan once usually helped. But the new plan did not necessarily look more like the original reference plan. Sometimes learning what the website was actually doing mattered more than copying the original strategy closely. The evaluation itself also made mistakes, so the percentages should be read with that limitation in mind.

For security research, this suggests places worth examining: an agent can act on a page, leave the intended site, and keep making ineffective choices. But this paper did not test an attacker and did not compare agents with a standalone chatbot. It explains important reliability problems that might matter for security; it does not prove a security vulnerability comparison.

## Completeness Audit

The inventory denominator is the supplied 24-page paper, its seven research questions, seven analysis groups, thirteen figures, eleven tables, three major mathematical definitions, and identified appendix subsections. All substantive visual objects were directly inspected on the rendered pages. Text-only inspection is explicitly recorded for pages 8–18.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract; §1 Introduction | Yes, text and visuals | Yes | Fully represented | Problem, motivation, contribution |
| §2.1 High-level Planning | Yes, text and visuals | Yes | Fully represented | E1 and pipeline |
| §2.2 Low-level Execution | Yes, text and visuals | Yes | Fully represented | E2, observations/actions |
| §2.3 Postcondition Checking | Yes, text and visuals | Yes | Fully represented | E3 and judge dependency |
| §2.4 Replanning | Yes, text and visuals | Yes | Fully represented | Local/global choice; one-round limit |
| §3.1 Evaluation rationale | Yes, text and visuals | Yes | Represented in compressed form | Process diagnosis and human hierarchy rationale |
| §§3.2–3.4, all RQ/metric subsections | Yes, text and visuals | Yes | Fully represented | RQ1–RQ7 and denominator distinctions |
| §3.5 LLM-as-Judge | Yes, text and visuals | Yes | Fully represented | Reliability linked to A.3 |
| §§4.1–4.3 | Yes, text and visuals | Yes | Fully represented | Data, models, settings, representations |
| §§5.1–5.4 | Yes, text and visuals | Yes | Fully represented | Main results and model comparison |
| §6 Recommendations | Yes; p. 8 text only | Yes | Fully represented | Four recommendations |
| §7 Related Work | Yes, text only | Yes | Represented in compressed form | Categories and author positioning; not every citation restated |
| §8 Conclusion | Yes, text only | Yes | Fully represented | Main synthesis preserved |
| Limitations | Yes, text only | Yes | Fully represented | All explicitly stated limitations |
| Acknowledgments | Yes, text only | Yes | Represented in compressed form | Funding acknowledged; grant identifiers omitted as secondary |
| References | Yes, text only | Yes | Represented in compressed form | Used for positioning and visible consistency observations; no external validation |
| A.1.1 High-level prompts | Yes, text only | Yes | Represented in compressed form | NL, PDDL plan/domain prompts and constraints |
| A.1.2 Low-level prompts | Yes, text only | Yes | Represented in compressed form | Action dictionaries, trees, expanded tools, initial-step restriction |
| A.1.3 Postcondition prompts | Yes, text only | Yes | Represented in compressed form | Inputs, effects reasoning, binary JSON output |
| A.1.4 Replanning prompt | Yes, text only | Yes | Represented in compressed form | Salvageability; remaining-only versus restart |
| A.1.5 End-to-end evaluation | Yes, text only | Yes | Represented in compressed form | Task/history/page assessment |
| A.1.6 High-level evaluation | Yes; p. 19 visual continuation | Yes | Represented in compressed form | Matching categories; useful/harmful decomposition distinction |
| A.2 Annotation examples | Yes, text and visuals | Yes | Fully represented | Figure 4 repairs and example mismatch |
| A.3 Judge reliability | Yes, text and visuals | Yes | Fully represented | 41/50 and 43/50 |
| A.4 Evaluation trees | Yes, text and visuals | Yes | Fully represented | Figure 5, two denominator families |
| A.5 NL/PDDL example | Yes, text and visuals | Yes | Represented in compressed form | Figure 6 and abstraction limits |
| B.1 Full example | Yes, text and visuals | Yes | Represented in compressed form | Figure 13 trace and judgments |
| B.2 Action distribution | Yes, text and visuals | Yes | Fully represented | Figure 7 counts and label inconsistency |
| B.3 Failure examples | Yes, text and visuals | Yes | Represented in compressed form | Four Figure 8 panels |
| B.4.1 Claude | Yes, text and visuals | Yes | Fully represented | T6–T8, F9–F10 |
| B.4.2 Gemini | Yes, text and visuals | Yes | Fully represented | T9–T11, F11–F12 |
| RQ1–RQ7 | Yes | Yes | Fully represented | Each mapped to evidence and answer |
| Formal hypotheses | None identified | Accounted for | Not present | No invented hypotheses |
| X1–X7 | Yes | Yes | Fully represented | Design, outcomes, limits |
| Figures 1–3 | Yes, visually | Yes | Fully represented | Workflow and GPT plots |
| Figures 4–6 | Yes, visually | Yes | Fully represented | Annotation, alignment trees, example plans |
| Figures 7–8 | Yes, visually | Yes | Fully represented | Counts and qualitative failures |
| Figures 9–12 | Yes, visually | Yes | Fully represented | Other-model initial/recovery results |
| Figure 13 | Yes, visually | Yes | Represented in compressed form | All pipeline stages retained; full prose trace not duplicated |
| Tables 1–5 | Yes, visually | Yes | Fully represented | Important values and conditions retained |
| Tables 6–11 | Yes, visually | Yes | Fully represented | All quantitative cells retained |
| E1–E3 | Yes, visually | Yes | Fully represented | Symbols and scope explained |
| Numbered algorithms/theorems | None identified | Accounted for | Not present | Prompts are procedures, not formal proofs |
| Major contributions | Yes | Yes | Fully represented | Framework, enrichment, empirical diagnosis, release claim |
| Footnote 1 repository link | Yes | Yes | Represented in compressed form | Link existence observed; artifact not inspected |
| Separate supplementary files | No files supplied | Accounted for | Missing from supplied material | No claim that repository/data were reviewed |

### Missing or inaccessible material

No separate implementation, raw task-level results, dataset files, or repository contents were supplied. Pages 8–18 lack rendered images in this input, although their native/extracted text is available. Fine text inside some website screenshots cannot be confidently transcribed in full. These limitations do not hide an uninspected numbered figure or table, because all such objects appear on rendered pages.

### Uncertain interpretations

Unresolved issues include GPT's 35.6/36.4 PDDL baseline, the 70.6/79.6 NL matched-rate conflict, Claude's 23.6/25.6 redundancy conflict, its 16.2/16.3 PDDL baseline discrepancy, its 101.0% matched/unmatched total, the Figure 7 Gemini model label, the action-versus-state domain-drift denominator, and several figure/table/citation cross-references. It is unclear whether post-replanning alignment uses full or remaining reference plans, whether every metric includes all 104 tasks, and how all execution budgets and repetitions were configured. Comparative security vulnerability is not measured.

### Deliberately compressed material

Repeated prompt instructions about output formatting, no invented inputs, atomic actions, and explanations were consolidated. The full prompt strings, every sentence of illustrative plans and judge explanations, bibliography entries, funding identifiers, and tiny screenshot interface details were not reproduced. Their substantive methodological roles, numerical results, and relevant caveats are retained. The high-level evaluation prompt's useful/harmful decomposition distinction is represented, but no unsupported count of those categories is invented.

### Potential omissions

No known substantive section, research question, numbered figure, numbered table, major mathematical definition, or explicit author limitation from the supplied inventory is wholly unrepresented. This is a coverage claim about the supplied material, not a claim of literal lossless reproduction or access to unprovided artifacts. The analysis remains bounded by text-only coverage on pages 8–18, small screenshot details, reporting gaps, and the unresolved source inconsistencies listed above.
