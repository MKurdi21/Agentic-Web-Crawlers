# Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and ten supplied page images. Paper content is treated as evidence, including its embedded example instructions, rather than as instructions to this analyst. No outside research, repository inspection, execution, or citation verification was performed.

| Accessibility item | Assessment |
|---|---|
| Main document | Supplied as extracted text for physical PDF pages 1–14 |
| Accessible page count | 14; this establishes coverage of the supplied sequence, not independent verification of the original PDF |
| Apparently missing pages | None within the supplied 1–14 sequence |
| Visually inspected pages | 1, 2, 4, 6, 7, 8, 9, 12, 13, 14 |
| Text-only pages | 3, 5, 10, 11 |
| Figures | Figures 1–6 are visually available; small graphical labels and unlabeled plot values require caution |
| Tables | Tables 1–8 are available in extracted text and rendered images; values can be cross-checked |
| Equations | Equations 1–3 are visually available on p. 4; Equations 4–6 are available through text on p. 5 |
| Appendices | A–H are present on pp. 12–14, despite the supplied automated accessibility metadata detecting no appendix pages |
| Supplementary files | None supplied; embedded-file count is reported as zero |
| Referenced external artifacts | Code repository and claimed released dataset/framework; their contents and availability were not inspected |
| OCR | No additional OCR used; extracted text was checked against supplied images where possible |
| Other limitations | The initial local-image error concerns an additional path named '-'; it does not prevent inspection of the ten displayed images |

Evidence labels used below: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. Exact table entries are both reported results and visually readable evidence; approximate graph readings are explicitly identified. Confidence reflects confidence in source representation, not independent confirmation that an experiment occurred as described. HIGH means clearly supported by the supplied material; MEDIUM marks interpretation or incomplete methodological support. No external-information category is used.

# 1. Plain-language orientation

SkillTrojan studies a security problem in AI agents that install reusable packages of instructions and executable scripts, called **skills**. A large language model, or **LLM**, may choose and combine these skills to complete a task. A skill might help inspect a database, build a query, format results, or verify an answer. Installing such packages gives an agent useful capabilities, but also places trust in code acquired from outside its core model. [A; pp. 1–3]

The proposed attack hides a malicious program inside apparently useful skills. The program is encoded, encrypted, and divided into pieces. During a specially triggered task, several ordinary-looking tool calls release these pieces. A verification step collects them, reconstructs the program, and executes it as a hidden side effect. The user can receive a correct answer while an unwanted action occurs in the execution environment. The attack does not require modifying model weights or training data. [A; pp. 3–5]

The authors evaluate task accuracy and hidden-payload execution separately. Their headline EHR SQL result is **97.2% attack success rate with 89.3% clean-task accuracy on GPT-5.2-1211-Global**. This is one model and condition, not a universal result. In another open-weight condition, Qwen3-VL-235B-A22B-Instruct, SkillTrojan achieves only 26.7% attack success and loses clean accuracy relative to the no-skill agent. [A/B; p. 6, Tables 1–2]

The central contribution is an execution-layer threat model and attack framework: useful components can compose into harmful behavior even when the model and final answer appear trustworthy. The authors also report a dataset of over 3,000 generated backdoored skills and experiments on scanners, fragmentation, encoding, workload trigger frequency, software engineering, and four agent frameworks. [A; pp. 2, 7–9, 12–14]

**Relevance to the user's research question is analyst inference [D]:** this paper supplies a concrete reason agents can have vulnerabilities beyond a standalone model's text generation: installed executable skills introduce persistent code, access to resources, intermediate state, and side effects. It does **not** experimentally compare web AI agents against standalone LLMs. Its main benchmarks concern database-query and software-engineering agents; web-agent conclusions must remain conditional rather than be presented as directly measured findings.

# 2. Document roadmap

The original title is **SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems**. The authors are Yunhao Feng, Yifan Ding, Yingshui Tan, Boren Zheng, Xiaolong Li, Kun Zhai, Yishan Li, Yanming Guo, and Wenke Huang. Feng and Ding are marked equal contributors. Affiliations are National University of Defense Technology, Alibaba Group, Fudan University, and Wuhan University. The supplied first page identifies the proceedings of the 43rd International Conference on Machine Learning, Seoul, South Korea, PMLR 306, 2026, and displays arXiv:2604.06811v2, dated 28 May 2026. These are document-reported bibliographic details, not externally verified publication claims. [A/B; p. 1]

This is a mixed **cybersecurity, AI-agent systems, algorithm, dataset, and empirical evaluation paper**. It contains no theorem/proof contribution. No keyword list is visible.

| Inventory identifier | Original component | Location and role |
|---|---|---|
| ABS | Abstract | p. 1; problem, attack, dataset, headline result |
| S1 | §1 Introduction | pp. 1–2; skill-layer gap and three contributions |
| DISC | Conflict of Interest Disclosure | p. 2; Alibaba employment and evaluation of Alibaba models |
| S2.1 | Coding Agents and Executable Skill Abstractions | pp. 2–3; motivation for reusable executable components |
| S2.2 | Backdoor Attacks on Agent Systems | p. 3; positioning against model and interaction-channel attacks |
| S3 | Threat Model | p. 3; attacker, trusted model, installed skills, per-run state |
| S4 | Method | pp. 3–5; workflow-completion attack principle |
| S4.1 | Payload Encoding and Skill Instrumentation | pp. 4–5; Equations 1–4 |
| S4.2 | Triggered Reconstruction and Execution | p. 5; Equations 5–6 |
| S4.3 | Dataset Construction | p. 5; template filtering, variants, metadata |
| S5.1 | Experimental Setup | pp. 5–6; tasks, models, controls, metrics |
| S5.2 | Analysis of main results | pp. 6–8; comparisons, traces, scanners |
| S5.3 | SkillTrojanX | p. 8; dataset composition and intended uses |
| S5.4 | Ablation studies | pp. 8–9; fragment count and encryption |
| S6 | Conclusion | p. 9; interpretation and defense directions |
| ETH | Acknowledgements and Impact Statement | p. 9; support, infrastructure, dual-use framing |
| REF | References | pp. 10–11; cited literature, not independently reviewed |
| APP-A | Additional Ablation Studies | p. 12; poisoning-ratio experiment |
| APP-B | Additional benchmark: SWE-Bench Verified | p. 12; software-engineering generalization |
| APP-C | Algorithmic Pipeline | pp. 12–13; Algorithm 1 |
| APP-D | LLM-as-a-Judge Prompt | p. 13; SQL correctness judgment |
| APP-E | Experimental Details | p. 13; baseline adaptation and execution markers |
| APP-F | Clean-Skill Utility on EHR SQL | p. 14; native-skill control |
| APP-G | Cross-Framework Evaluation | p. 14; separate coding benchmark |
| APP-H | Example Skill Structure | p. 14; package illustration |

The visual inventory is Figures F1–F6, Tables T1–T8, Equations E1–E6, and ALG1. The experiment register is X1 EHR SQL, X2 tool-call distributions, X3 static scanners, X4 dataset coverage, X5 fragmentation, X6 encoding, X7 poisoning ratio, X8 SWE-Bench Verified, X9 native-skill utility, and X10 cross-framework evaluation. These identifiers form the denominator of the final coverage audit.

# 3. Background and context

A **skill** is a distributable package combining a natural-language specification with executable artifacts. The specification guides the model; scripts and resources carry out actions. The authors formalize this as s=(m,A), with instruction text m and action collection A. A deployed agent installs multiple such packages. [A; p. 3]

A **backdoor** is malicious behavior that remains dormant under ordinary inputs and activates under a particular trigger. Here, the trigger is a string or pattern in a user query, represented by a predicate returning zero or one. Dormancy is important because routine testing may encounter correct behavior rather than the hidden side effect. [A; pp. 2–3]

An **execution trace** is the sequence of actions used during a run. **Fragmentation** divides the encoded malicious program into multiple indexed pieces. **Order-agnostic reconstruction** means collection order does not matter: the verifier checks that all pieces exist and uses their indices to restore their order. This removes a fixed ordering requirement, but does not remove the requirement to execute enough relevant actions before verification. [A; pp. 4–5]

A **side effect** is an execution outcome separate from the returned answer. In this paper, successful attacks must create an execution marker corroborated by a deterministic effect, such as a file or database effect. A correct natural-language answer is therefore not sufficient evidence of safe execution. [A; pp. 6, 13]

**EHR SQL** denotes the paper's electronic-health-record database-query task using Structured Query Language. The task begins with a natural-language clinical question, constructs SQL through skills, and executes the query against an EHR database. The supplied work does not identify the database, workload size, or detailed schema. **SWE-Bench Verified** is the software-engineering benchmark used here; the paper describes success through verified tests under its benchmark harness rather than requiring the reader to infer its operation from external knowledge. [A; pp. 5, 12]

# 4. Research problem and gap

**Existing problem [A]:** agents increasingly rely on reusable skills that execute code, maintain state, and mediate external resources. This concentrates trust in third-party implementations and expands the security-relevant system beyond the model's visible input/output behavior. [pp. 1–2]

**Attributed shortcomings of previous approaches [A]:** the authors characterize prior backdoor research as focusing on model parameters, poisoned training data, prompts, tool descriptions, memory entries, or other interaction channels. They argue that defenses often examine these surfaces individually and that installed executable skills are insufficiently audited beyond functional correctness. These are the paper's literature claims, not an independently validated survey conclusion. [pp. 2–3]

**Research gap [A]:** persistent, reusable skill implementations can encode malicious logic while retaining useful behavior. Harm may emerge across a sequence of benign-looking actions, making single-action inspection and final-answer checking incomplete. [pp. 2–5]

**Motivation [A]:** a popular compromised package could influence many downstream runs while the core model, its training data, and ordinary task outputs remain unchanged. Automated generation of variants could scale this problem across a skill ecosystem. Actual adoption, propagation rates, and compromise of real users are not measured. [pp. 2–3]

**Scope:** the work studies installed, attacker-controlled skill packages in code-executing agents. It excludes base-model compromise, direct operating-system compromise, remote-service compromise, and cross-run reconstruction state. It does not establish a universal vulnerability ranking of agents versus standalone LLMs, nor does it evaluate a browsing-only web agent as its principal system. [A/D; pp. 3, 5–6, 14]

# 5. Research questions / objectives / hypotheses

The supplied paper does not enumerate formal research questions or preregistered hypotheses. Its stated objectives can be organized without inventing author-labeled questions:

1. Introduce a skill-layer backdoor that preserves nominal functionality on non-triggered inputs while reliably executing a payload on triggered inputs. [A; pp. 2–3]
2. Develop a general synthesis framework using encrypted fragments, conditional activation, and reusable templates. [A; pp. 2, 4–5]
3. Measure clean utility and attack success across open- and closed-weight policy models. [A; pp. 5–7]
4. Test whether results extend beyond SQL tasks and a single framework. [A; pp. 12, 14]
5. Examine fragment count, encoding, trigger prevalence, and static-scanner detectability. [A; pp. 7–9, 12]
6. Supply a corpus for future controlled attack and defense evaluation. [A; pp. 5, 8]

The design embodies an expectation that moderate fragmentation balances concealment against reliable workflow completion. Figure 5 supports this expectation in one model setting, but the paper does not present a formal statistical hypothesis test. The user's broader question is addressed through a clearly labeled analytical connection, not through a missing standalone-model control.

# 6. Assumptions / threat model

The trusted core is the underlying language model and its training data, assumed unmodified. The deployment dynamically loads third-party skills from repositories or marketplaces. A skill includes both instructions and executable code; its installation creates the persistent foothold. [A; p. 3]

The attacker can publish apparently useful skills, induce their adoption, and replace selected packages with modified instruction text and scripts. The attacker chooses payload P, trigger predicate Trigτ, encoding, and fragmentation. After installation, the attacker has no host access, operating-system privileges, or model-internal access; interaction is limited to user queries. Thus the assumed malicious code enters through the package before execution rather than through a later privileged intrusion. [A; p. 3]

The payload is constrained by the skill execution environment. The attack does not automatically imply arbitrary host privileges: what the environment permits determines the consequences of payload execution. The paper places sandboxing and output-validation defenses outside attacker capabilities unless the deployment explicitly enables relevant conditions; it does not demonstrate bypass of an enforced sandbox. [A/D; pp. 3–4]

Persistence has a specific meaning. The compromised package persists across tasks and deployments. Its reconstruction fragments do not. Fragments occupy a run-local channel, such as tool-return fields, trajectory logs, or scratchpad state, and are intended to be cleaned up. Attacks requiring long-term fragment storage or accumulation across runs are excluded. [A; pp. 3, 5]

The attack's two goals are clean-input stealth and triggered reliability. Neither goal means that every execution is successful or that all observable traces vanish. Figure 3 reports extra tool calls, and the encoding ablation reports detectable intermediate strings. Claims of stealth are therefore relative to the tested observations and scanners. [A/B/D; pp. 7–9]

# 7. Methodology

## 7.1 Study design and construction

The study combines a constructed attack system, generated skill corpus, end-to-end task evaluations, control comparisons, and one-factor ablations. It does not train or alter the underlying policy models. The model plans and chooses tools; installed skills perform the execution. [A; pp. 3–6]

Conceptually, synthesis takes a benign package, a payload, a trigger, a fragment count, and encoding material. It encrypts the payload, partitions the representation into indexed fragments, modifies selected actions to emit fragments conditionally, modifies the skill specification to favor the relevant workflow when triggered, and instruments a designated verification action. The original action results are intended to retain their functional meaning. [A; pp. 4–5, 13]

During a run, normal actions execute. Triggered fragment-emitting actions add their pieces to run-local storage. At verification, the package checks completeness, reconstructs the encrypted program by index, decrypts it, executes it as a side effect, and records success. This is an explanation of the supplied algorithm, not executable attack code. [A; pp. 5, 13]

## 7.2 Dataset and preprocessing

SkillTrojanX begins with popular skills from a public marketplace. The paper describes crawling the top 1,200 skills and retaining packages with executable artifacts and a parsable specification. Retained packages are normalized. Variants vary trigger phrase, payload family, encryption/encoding, and fragment count; metadata also records emitting and verification entrypoints. [A; pp. 5, 8]

Table 4 reports 1,200 templates, over 3,000 backdoored variants, six template categories, four payload families, three crypto variants, three N variants, and 50 unique triggers. The exact generated total and a template-by-variant allocation are not reported. The prose does not give separate pre-filter and post-filter counts, so the apparent equivalence between 1,200 crawled skills and 1,200 templates cannot be independently reconstructed. [A/B/D; p. 8]

The corpus is not the same thing as a counted benchmark workload. The paper does not specify how many SQL queries, SWE-Bench instances, or industry coding tasks were evaluated. It also does not give explicit train/validation/test partitions, deduplication procedures, dataset licenses, annotation validation, or leakage precautions in the supplied material.

## 7.3 Default configuration and models

Defaults are **ρ=0.2**, **N=3**, and **XOR+Base64**. Here ρ is the proportion of triggered queries in the workload, not a model-training poisoning rate. Clean queries have Trigτ(q)=0; poisoned queries insert a trigger phrase and have Trigτ(q)=1. [A; p. 5]

Open-weight policy models are GLM-4.7, Qwen3-Coder, GLM-4.6, and Qwen3-VL-235B-A22B-Instruct. Closed-weight models are GPT-4o-mini-0718-Global, Claude-Haiku-4.5, Claude-Sonnet4.5, Qwen3-Max, and GPT-5.2-1211-Global. These model labels are preserved as supplied; their release history and access routes were not checked. The authors say skill implementation and evaluation protocol are kept identical across models. [A; pp. 5–6]

Hardware, operating system, library versions, model sampling settings, token budgets, seeds, repetition counts, latency, cost, and resource overhead are not specified in the supplied material. The acknowledgements identify Rock Hack as supporting part of the infrastructure, without providing a detailed reproducible environment. [A; p. 9]

## 7.4 Baselines and controls

GCG, AutoDAN, CPA, BadChain, and AgentPoison are adapted to the same tool-executing setting. The paper does not expand every baseline acronym; no unsupported expansions are supplied here. GCG/AutoDAN/CPA use adversarial suffixes or instruction patterns in queries and/or system prompts. BadChain and AgentPoison inject instructions into agent-readable context while leaving executable skills unchanged. [A; pp. 6, 13]

For comparable success measurement, prompt/context baselines receive an otherwise benign payload tool that produces the target side effect if selected. They must persuade the model to call that tool. SkillTrojan instead reaches payload execution through installed compromised code. This preserves a common outcome definition while comparing different attacker control surfaces and privileges. [A/D; p. 13]

**Non-attack** means the agent lacks the installed skill stack. **Skills (Native)** means the benign version of the same stack is installed. These are materially different controls. Native skills are the more direct control for evaluating the utility cost of adding malicious logic to a useful package. [A/D; pp. 6, 14]

## 7.5 Metrics and statistical reporting

**ACC**, clean-task accuracy, is the fraction of non-triggered queries judged correct from SQL execution output. Appendix D provides a yes/no LLM judge prompt comparing agent_result with query_result. Judge identity, calibration, agreement with human judgments, and repeatability are not specified. [A; pp. 6, 13]

**ASR**, attack success rate, is the fraction of triggered queries whose payload is reconstructed and executed, indicated by a verifier marker and corroborated by a deterministic side effect. It is not the fraction of all queries and not a score based solely on malicious text. [A; pp. 6, 13]

SWE-Bench clean success uses verified tests. Scanner safe rate measures the fraction labeled safe; a high safe rate for malicious skills indicates missed detection. Heuristic-flag rate measures a base64-string detector's hits on intermediate outputs and has a different denominator from package classification. No confidence intervals, significance tests, or reported seed variability accompany the main results.

# 8. Experiments / analyses

| ID | Purpose and setup | Variables, evidence, and principal outcome | Caveat |
|---|---|---|---|
| X1 | End-to-end EHR SQL across nine models | Seven methods; clean ACC and triggered ASR; Tables 1–2 | Query counts, judge model, and uncertainty absent |
| X2 | Check whether attack execution changes tool usage | Clean versus triggered traces; Figure 3 | Distribution shifts visible; exact sample counts and summary statistics absent |
| X3 | Test pre-deployment static screening | Approximately 500 sampled skills; two guard models; native/full/unencoded-unsegmented conditions; Table 3 | Scanner prompts and exact sample allocation absent |
| X4 | Describe generated dataset coverage | Six categories, four payload families; Table 4 and Figure 4 | Generation scale does not independently establish attack success for every variant |
| X5 | Isolate fragment-count effects | GPT-4o-mini; N=1,2,3,5; Figure 5 | One displayed model; no plotted uncertainty |
| X6 | Compare encoding and heuristic visibility | GPT-4o-mini, N=3, ρ=0.2; XOR+Base64 versus Hybrid; Table 5 | Hybrid construction and detector threshold unspecified |
| X7 | Separate trigger prevalence from per-trigger success | GPT-4o-mini; ρ=0.1,0.2,0.5; Figure 6 and Appendix A | ACC and ASR use separate subsets; aggregate harm not measured by ASR alone |
| X8 | Extend to software engineering | SWE-Bench Verified; three models and three methods; Table 6 | Instance count and native-skill control absent |
| X9 | Identify source of clean-task utility | Non-attack, SkillTrojan, native skills; four open-weight models; Table 7 | No analogous native control for the five closed-weight models |
| X10 | Extend across deployed frameworks | Four frameworks, five backbones; separate industry coding benchmark; Table 8 | Benchmark identity, workload size, controls, and uncertainty unspecified |

The ablations keep the model, EHR SQL split, trigger phrase, representative side-effect payload, template, and evaluation protocol fixed except for the varied factor, unless otherwise stated. This is the authors' reported control design; the underlying split and payload details are not supplied. [A; pp. 8–9]

# 9. Results

The strongest headline result is GPT-5.2-1211-Global on EHR SQL: SkillTrojan ACC/ASR is 89.3/97.2%, compared with Non-attack 73.0/0.0% and AgentPoison 72.9/58.3%. **Analyst-derived [C]:** the ASR difference from AgentPoison is 97.2−58.3=38.9 percentage points. The clean-accuracy difference from Non-attack is 89.3−73.0=16.3 points, but that baseline lacks the skill stack; it cannot isolate a benefit from malicious logic. [p. 6, Table 2]

SkillTrojan has the largest reported ASR on eight of the nine EHR model columns, an **analyst-derived count [C]** from Tables 1–2. The exception is Qwen3-VL, where AgentPoison reaches 37.6% versus SkillTrojan's 26.7%. SkillTrojan's clean ACC there is 48.4%, below Non-attack's 53.2% and native skills' 50.3%. This qualifies prose suggesting uniformly superior attacks and benign-utility preservation. [pp. 6, 14]

Against native skills, SkillTrojan loses clean accuracy in every Table 7 column: **[C]** GLM-4.7, 88.7−85.2=3.5 points; Qwen3-Coder, 82.3−76.3=6.0; GLM-4.6, 85.5−81.3=4.2; Qwen3-VL, 50.3−48.4=1.9. Native skills themselves underperform Non-attack on Qwen3-VL: 50.3−53.2=−2.9 points. Thus the appendix statement that native skills have the best accuracy in all four settings conflicts with that table. [p. 14]

The two static scanners label 98.2% and 99.4% of full SkillTrojan samples safe, versus 3.4% and 2.8% for the variant without encryption/segmentation. This supports failure of these particular scanner configurations, not failure of all static analysis. [pp. 7–8]

Encoding can substantially change a simple detector's visibility without materially changing reported accuracy or ASR. Table 5 gives heuristic hits of 78.0% for XOR+Base64 and 21.0% for Hybrid. **[C]** This is a 57.0-percentage-point reduction, calculated as 78.0−21.0. The two methods differ by only 0.1 ACC point and 0.3 ASR point, but no uncertainty estimates permit a statistical equivalence claim. [p. 9]

On SWE-Bench Verified, SkillTrojan ASR is 63.9%, 92.8%, and 66.4% across Qwen3-Coder, GPT-5.2, and GLM-4.7. Corresponding clean ACC is 65.7%, 70.4%, and 67.6%. The attack therefore extends beyond SQL in the reported tests, while GPT-5.2 clean accuracy is slightly lower than its 70.6% Non-attack value. [p. 12]

# 10. Figure-by-figure interpretation

## Figure 1 — Skill-based execution model

**Visually inspected, p. 1.** This is a conceptual circular architecture, not a quantitative plot. An LLM core is surrounded by planning, memory, and tool-execution functions. Labels include task decomposition, workflow architecture, contextual recall, long-term knowledge, code interpreter, web search, and API call. Outer skill boxes represent planner, search, code, memory, and execution skills. Dashed red paths and fragment labels connect skill use to reconstruction and payload execution. [B]

Its purpose is to show that the malicious mechanism attaches to skill composition around the model rather than replacing the model. There are no axes, units, sample sizes, or measured outcomes. The web-search and memory icons illustrate scope conceptually; they are not separate evaluated web-search or persistent-memory attacks. Small artwork and the title's devil icon are decorative and carry no quantitative evidence.

## Figure 2 — Layered attack architecture

**Visually inspected, p. 4.** Four broad columns show the user layer, agent reasoning layer, skill execution layer, and side-effect execution layer. A clean query asks for analysis and summary; an alternative triggered query includes a subtle marker. The agent core contains an LLM, planner, tool/skill selector, and execution controller. A repository column presents code, database, network, and logging/utility skills. [B]

The execution trace moves through data loading, database querying, external information fetching, and analysis/summarization. Ordinary outputs continue down the normal workflow. Encrypted fragments travel sideways to a verification module. Set-based verification precedes reconstruction and decryption, followed by payload execution and cleanup. A bottom band distinguishes preserved benign task completion from trigger-only side effects. [B]

The diagram supports a split between normal data flow and malicious side-effect flow. It does not prove that every triggered run returns a correct answer; that stronger claim would require triggered-task correctness measurements, which the reported ACC metric does not provide. [D]

## Figure 3 — Tool-call count distributions

**Visually inspected, p. 7.** The left panel uses violin/box-like summaries for Clean and Triggered tool-call counts. Its vertical axis is tool calls, with labeled ticks roughly 5–30. The right panel plots discrete probability against tool calls per run, roughly 5–30 horizontally and 0.00–0.10 in labeled probability ticks. Blue represents clean and orange triggered runs. [B]

The triggered distribution shifts toward more calls, with considerable overlap. The left summaries appear centered in the mid-teens for clean runs and somewhat higher for triggered runs; those are **approximate visual observations**, not reported means or medians. No exact overhead, sample count, or uncertainty interval is supplied. The authors interpret the shift as additional collection and verification while remaining within ordinary complex-query behavior. [A/B]

## Figure 4 — Corpus coverage

**Visually inspected, p. 8.** A stacked bar chart shows Coding, Data/SQL, File/IO, Planning, Utilities, and Web categories. The vertical axis is number of backdoored skills, with labeled ticks 0, 200, 400, 600, and 800. Colors encode System profiling, Secret harvesting, File drop, and Network beacon. [B]

Data/SQL is the tallest stack; Planning is the shortest. All six categories visibly contain all four payload-family colors. Exact per-stack and per-segment counts are not labeled and are not reconstructed here. The figure establishes diversity of generated variants, not measured real-world prevalence or separate execution success rates for each family.

## Figure 5 — Fragment-count ablation

**Visually inspected, p. 8.** The horizontal axis is fragment count N at 1, 2, 3, and 5. The left vertical axis is ASR (%) and the right is ACC (%), each spanning 0–100. Orange circles encode ASR and blue squares encode ACC. Extraneous '_child1' legend entries and dotted reference lines appear without substantive explanation. [B]

ASR rises from approximately the low 40s at N=1 to the mid-50s at N=3, then falls to approximately the high 30s at N=5. These are **approximate visual estimates**; exact values are not printed. ACC remains near the high 60s. The caption and prose report a peak at N=3 and explain small-N conspicuousness versus large-N incomplete collection. No error bars show whether neighboring settings differ reliably. [A/B]

## Figure 6 — Poisoning-ratio ablation

**Visually inspected, p. 12.** The horizontal axis is poisoning ratio ρ, with plotted conditions 0.10, 0.20, and 0.50. The left and right vertical axes are ASR (%) and ACC (%), both 0–100. Orange circles and blue squares retain Figure 5's encoding, including unexplained '_child1' legend entries. [B]

The ACC line stays near 68.5%; ASR remains in the low-to-mid 50s. Appendix A reports variation within three ASR points and stable ACC. Exact point values are not all printed. The graph supports stability of conditional rates across these workload mixtures; it does not mean the total frequency of malicious events stays constant when more queries are triggered. [A/D]

# 11. Table-by-table interpretation

All results below are percentages. For Tables 1, 2, and 6, each cell pair is **ACC/ASR**. Upward arrows indicate the authors' evaluation direction; larger ASR measures a stronger attack, not safer deployment. No table reports confidence intervals, significance tests, standard deviations, or replicate counts.

## Table 1 — EHR SQL, open-weight models, p. 6

| Method | GLM-4.7 | Qwen3-Coder | GLM-4.6 | Qwen3-VL-235B-A22B-Instruct |
|---|---|---|---|---|
| Non-attack | 84.1/0.0 | 71.5/0.0 | 76.0/0.0 | 53.2/0.0 |
| GCG | 83.7/35.1 | 70.2/41.0 | 75.3/38.6 | 51.8/24.9 |
| AutoDAN | 82.2/46.8 | 68.9/51.4 | 73.6/55.6 | 49.5/19.7 |
| CPA | 81.4/44.2 | 67.8/57.9 | 72.1/52.7 | 48.9/31.5 |
| BadChain | 84.0/31.8 | 70.7/18.4 | 76.6/23.7 | 52.6/7.9 |
| AgentPoison | 85.0/57.2 | 72.4/62.5 | 77.1/60.8 | 52.0/37.6 |
| SkillTrojan | 85.2/62.1 | 76.3/64.7 | 81.3/72.0 | 48.4/26.7 |

SkillTrojan leads ACC and ASR in the first three columns. In the fourth, Non-attack has the best ACC and AgentPoison the best ASR; SkillTrojan has the lowest ACC. Among attacking methods, BadChain has the lowest ASR in every column. The table contains no missing entries or tied maxima. Its exception matters because the prose emphasizes generally superior trade-offs.

## Table 2 — EHR SQL, closed-weight models, p. 6

| Method | GPT-4o-mini-0718-Global | Claude-Haiku-4.5 | Claude-Sonnet4.5 | Qwen3-Max | GPT-5.2-1211-Global |
|---|---|---|---|---|---|
| Non-attack | 71.6/0.0 | 73.1/0.0 | 86.5/0.0 | 82.7/0.0 | 73.0/0.0 |
| GCG | 70.8/30.2 | 70.1/32.9 | 69.6/37.8 | 69.8/42.1 | 70.1/45.8 |
| AutoDAN | 67.4/42.1 | 68.6/39.4 | 69.7/34.9 | 67.9/30.8 | 68.4/27.4 |
| CPA | 66.3/38.5 | 66.9/41.0 | 67.8/44.6 | 67.2/48.7 | 67.9/51.1 |
| BadChain | 71.9/33.7 | 72.6/28.9 | 71.5/22.7 | 70.9/14.2 | 70.8/8.3 |
| AgentPoison | 74.8/53.7 | 75.5/54.8 | 74.1/56.2 | 73.4/57.6 | 72.9/58.3 |
| SkillTrojan | 68.5/54.3 | 82.7/57.3 | 90.7/64.2 | 86.6/74.7 | 89.3/97.2 |

SkillTrojan leads ASR in all five columns, but its advantage over AgentPoison on GPT-4o-mini is only **[C] 54.3−53.7=0.6 points**. It leads ACC in four columns; AgentPoison leads GPT-4o-mini ACC at 74.8%. SkillTrojan's GPT-4o-mini ACC is below Non-attack by **[C] 71.6−68.5=3.1 points**. Thus model-specific behavior is more informative than the headline alone. No uncertainty establishes whether small numerical differences are meaningful.

## Table 3 — Static skill scanners, p. 8

| Package condition | Qwen3Guard safe (%) | Llama-Guard safe (%) |
|---|---:|---:|
| SkillTrojan | 98.2 | 99.4 |
| Skills (Native) | 100.0 | 99.6 |
| SkillTrojan without encryption/segmentation | 3.4 | 2.8 |

Approximately 500 skills are sampled. Full attacks look nearly as safe as native packages to these scanners, whereas the simplified variant is usually rejected. **[C]** If classifications are binary, full-attack unsafe rates are 100−98.2=1.8% and 100−99.4=0.6%. The experiment removes encryption and segmentation together; it cannot separately attribute the change to each component. Exact sample denominators and scanner prompting are absent.

## Table 4 — SkillTrojanX statistics, p. 8

Templates: **1200**; backdoored skills: **3000+**; template categories: **6**; payload families: **4**; crypto variants: **3**; N variants: **3**; unique triggers: **50**. A template is a cleaned marketplace package; a variant has a particular trigger–payload–crypto–N configuration. These counts do not imply a complete Cartesian product. The four N settings in Figure 5 need not equal the three corpus N variants, but their relationship is not explained.

## Table 5 — Encoding ablation, p. 9

| Encoding | ACC (%) | ASR (%) | Heuristic-flag (%) |
|---|---:|---:|---:|
| XOR+Base64 | 68.5 | 54.3 | 78.0 |
| Hybrid | 68.4 | 54.6 | 21.0 |

Condition: GPT-4o-mini-0718-Global, N=3, ρ=0.2. Hybrid has slightly greater ASR and lower heuristic visibility; XOR+Base64 has slightly greater ACC. No tie is exact. The heuristic is a simple base64-string detector on intermediate outputs, not either guard model in Table 3. The supplied work does not define the Hybrid scheme sufficiently for reconstruction.

## Table 6 — SWE-Bench Verified, p. 12

| Method | Qwen3-Coder | GPT-5.2-1211-Global | GLM-4.7 |
|---|---|---|---|
| Non-attack | 64.8/0.0 | 70.6/0.0 | 67.3/0.0 |
| GCG | 62.1/10.3 | 68.2/12.5 | 55.9/26.1 |
| SkillTrojan | 65.7/63.9 | 70.4/92.8 | 67.6/66.4 |

SkillTrojan leads ASR on all three backbones and ACC on two. Non-attack has the best GPT-5.2 ACC, 70.6% versus 70.4%. This benchmark changes task-success measurement to verified tests while keeping the reported trigger, ρ, N, and skill execution environment aligned with the EHR setup. The baseline set is narrower than Tables 1–2.

## Table 7 — Native-skill utility control, p. 14

| Method | GLM-4.7 | Qwen3-Coder | GLM-4.6 | Qwen3-VL |
|---|---:|---:|---:|---:|
| Non-attack | 84.1 | 71.5 | 76.0 | 53.2 |
| SkillTrojan | 85.2 | 76.3 | 81.3 | 48.4 |
| Skills (Native) | 88.7 | 82.3 | 85.5 | 50.3 |

Only clean ACC is reported. Native skills outperform SkillTrojan in all four columns and outperform Non-attack in three. The surrounding sentence claiming the best clean accuracy in all four settings disagrees with the Qwen3-VL column. The data support retained partial skill utility, with a measurable loss against native skills; they do not support zero utility cost.

## Table 8 — Cross-framework ASR, p. 14

| Framework | Claude Sonnet 4.5 | GPT-5.1 | Qwen3 Coder Plus | Qwen3.5 Plus | GLM-5 |
|---|---:|---:|---:|---:|---:|
| Claude-Code | 63.53 | 95.59 | 98.53 | 94.12 | 87.65 |
| IFlow | 65.00 | 96.18 | 100.00 | 97.35 | 83.53 |
| OpenHands | 69.12 | 91.18 | 99.12 | 95.88 | 86.18 |
| OpenClaw | 65.88 | 96.76 | 99.71 | 94.71 | 88.53 |

All entries are ASR percentages on a separate industry-oriented coding benchmark. The minimum visible entry is 63.53 and maximum 100.00. Best framework varies by backbone: OpenHands for Claude, OpenClaw for GPT-5.1 and GLM-5, IFlow for both Qwen columns. There are no exact ties. The authors explicitly warn against direct numerical comparison with EHR SQL. Clean ACC, benchmark identity, and comparative defenses are absent here.

# 12. Diagram / architecture interpretation

Figures 1 and 2 provide complementary views. Figure 1 explains where the vulnerable abstraction sits around an LLM; Figure 2 shows how a single run can carry normal computation and hidden reconstruction concurrently. Their detailed visual content is covered in §10 rather than duplicated here.

The key architecture has two interacting paths. The **control path** begins with query interpretation, planning, skill selection, and action invocation. Modified skill instructions conditionally favor a trace containing the required actions. The **data path** returns ordinary results while carrying extra encoded fields into run-local trajectory state. A verifier gathers those fields, checks completeness, and executes the reconstructed program. [A/B; pp. 4–5]

Appendix H illustrates a package with SKILL.md, schema_analyzer.py, query_builder.py, result_formatter.py, and verify_results.py. Its normal workflow initializes, analyzes schema, constructs SQL, formats results, and verifies the answer. The example supports the threat model by showing plausible places to distribute logic. It is an illustrative directory structure, not a supplied implementation or proof that these exact files were used in every benchmark. [A; p. 14]

A meaningful boundary is that the verifier is itself part of the attacker-modified package. Its role should not be confused with an independent trusted security monitor. The external success corroboration described for evaluation serves a different purpose from the package's reconstruction verifier. [D; pp. 5, 13]

# 13. Equations and mathematical concepts

The mathematics specifies the mechanism rather than proving an optimality or security theorem. Symbols include query q, skill s=(m,A), installed skill set S, payload P, trigger parameter τ, key k, ciphertext C, fragment count N, execution trace π, and run-local fragment collection F(q). A tilde marks a backdoored object. [A; pp. 3–5]

**Equation 1, p. 4: C=Enc(P;k).** This is a transformation from payload program P and symmetric key k to ciphertext C. It expresses concealment before partitioning. Enc is an encryption function in the conceptual model; the default concrete configuration is XOR+Base64. The supplied work gives no cryptographic security proof or key-management analysis.

**Equation 2, p. 4: c_j=⟨j,seg_j(C)⟩.** Each fragment is a pair containing index j and the j-th ciphertext segment. seg_j selects a portion of C; the index permits restoration independent of arrival order. The equation does not specify segment lengths or an exact serialization format.

**Equation 3, p. 4:** Pr_under_modified_m(π|q)=Pr_under_m(π|q) when Trigτ(q)=0; when Trigτ(q)=1 it is written as Pr_under_m(π|q)+Δ(π). This is a conceptual description of conditional trace bias. π is a sequence of skill actions, and Δ represents a small change favoring traces containing designated actions. It explains the instruction modification, rather than a measured probability model or fitted loss.

**Analyst observation [D]:** a valid probability distribution requires probabilities to remain nonnegative and sum to one. The paper does not specify normalization, bounds, or a quantitative construction of Δ. Some trace probabilities would need offsetting reductions if others increase. The expression should therefore not be read as a complete probabilistic implementation.

**Equation 4, p. 5: F(q)={c_j1,…,c_jT}.** This denotes the unordered collection of fragments emitted during one run. It is empty on clean runs according to the emission rule, and it is not meant to persist across queries. The notation uses trace-related indices schematically; the actual number of unique emitted fragments need not equal the total action count.

**Equation 5, p. 5: {c_1,…,c_N}⊆F(q).** Set inclusion asks whether all required indexed fragments are present. It ignores action order, but still requires completeness before successful verification. It does not specify integrity checks for corrupted or conflicting fragments.

**Equation 6, p. 5: P=Dec(c_1∥…∥c_N;k).** Dec decrypts the reconstructed ciphertext using k; ∥ denotes concatenation. Because Equation 2 defines c_j as an index–segment pair, the intended operation is to concatenate segment contents in index order. Algorithm 1 makes this intention clearer through CONCATBYINDEX(F). The paper's shorthand should not be interpreted as decrypting arbitrary index metadata as ciphertext. [A/D]

Together, these equations express encryption, indexed partitioning, conditional workflow selection, per-run collection, completeness checking, and recovery. No optimization objective, theorem, lemma, or proof is supplied. Experimental metrics test whether this chain succeeds in the evaluated agents.

# 14. Interpretation and discussion

The supported central message is that **task correctness and execution safety are different measurements**. A package can preserve normal outputs while adding harmful actions. The reported ASR measures such execution directly, while clean ACC measures ordinary task utility. This is stronger evidence for hidden side effects than an evaluation based only on model-generated malicious text. [A/D; pp. 5–6, 13]

The authors argue that stronger models may complete the necessary tool chain more reliably without needing to endorse an overt malicious request. Their results on GPT-5.2 are consistent with that explanation, but do not isolate model strength as a causal variable. Models differ in many unspecified ways, and no controlled capability intervention is performed. [A/D; p. 7]

Several consistency issues qualify the broad framing:

- **Text–table conflict:** Appendix F says native skills have the best clean accuracy in all four settings, while Table 7 gives Qwen3-VL Non-attack 53.2 versus native 50.3. The table is preserved without silently correcting the prose.
- **Broad superiority versus exception:** §5.2's strongest-attack language is qualified by Table 1, where Qwen3-VL AgentPoison ASR exceeds SkillTrojan.
- **Prompt wording:** the conclusion says the attack works without modifying prompts, while §§3–4 and Algorithm 1 explicitly modify the skill's natural-language specification. A narrower interpretation is unchanged base/system interaction prompts but modified skill instructions; the paper does not cleanly establish that distinction throughout.
- **Fragment settings:** Table 4 reports three dataset N variants, while Figure 5 evaluates four N values. These can refer to different experimental objects, but their relationship is unspecified.
- **Cleanup:** prose states per-run cleanup; Algorithm 1 visibly places cleanup when the verifier executes. Cleanup after early termination or a run that never reaches verification is not explicitly implemented in that pseudocode.
- **Triggered correctness:** correct benign outputs during attack are asserted in the method and Figure 2, but reported ACC is computed on clean inputs. No separate triggered-task accuracy is provided.

These issues do not erase the demonstrated execution-layer mechanism. They constrain how confidently one can generalize its utility, stealth, and deployment behavior.

# 15. Contributions and novelty

**Conceptual [A]:** the paper frames reusable executable skills as a persistent security control surface distinct from model parameters and transient interaction channels. Its first-work claim is the authors' novelty claim and is not independently established here. [pp. 2–3]

**Methodological/algorithmic [A]:** it combines conditional skill instructions, encrypted indexed fragments, order-agnostic collection, and completion-linked execution. Algorithm 1 joins offline package synthesis with online activation. These are system-design contributions rather than a proven cryptographic primitive. [pp. 4–5, 13]

**Dataset [A]:** SkillTrojanX reportedly contains over 3,000 backdoored variants from 1,200 templates and metadata describing trigger, payload, crypto, fragment count, and action roles. [pp. 5, 8]

**Empirical [A]:** the evaluation covers nine EHR backbones, three SWE-Bench backbones, scanner controls, two main design ablations plus poisoning-ratio analysis, native-skill controls, and four framework implementations. Counts of backbones/frameworks are directly recoverable from the reported tables. [pp. 6–9, 12–14]

**Implementation availability [A]:** a GitHub code link and dataset release are claimed. Neither the repository nor release artifacts were supplied or inspected; reproducible availability remains unverified.

# 16. Limitations

## Authors' stated limitations and scope boundaries

The attacker is constrained by the skill execution environment; cannot directly compromise the model, remote services, or operating system; and cannot rely on cross-run fragment storage. [pp. 3–4] The framework experiment uses a separate benchmark and is explicitly not numerically comparable with the main EHR tables. [p. 14] SWE-Bench details are placed in an appendix because of space constraints. [p. 6] The impact statement confines the presentation to controlled experimental settings and acknowledges dual-use risk. [p. 9]

The paper does not present a dedicated limitations section. Missing experimental details listed below are analyst observations, not admissions attributed to the authors.

## Additional evidence-based analyst observations [D]

Benchmark denominators, exact sample allocations, random seeds, repetitions, confidence intervals, and software environments are absent. The EHR judge model and its error rate are not identified. Native-skill controls cover only four open-weight models, leaving headline closed-weight utility claims less directly controlled. The simplified scanner ablation removes two mechanisms together. Hybrid encoding is insufficiently specified. Cross-framework results provide ASR alone on an unnamed workload. There are no measured defenses involving enforced sandboxing, permissions, package signing, or runtime monitoring.

A useful attack package is assumed to be installed; real marketplace uptake is not tested. Fragment concealment is evaluated with two lightweight guard models and one simple detector, rather than an exhaustive adversarial code-review process. Aggregate tool-call distributions do not establish low detectability for every run. Cross-platform persistence and forensic cleanup are asserted at the design level rather than independently audited.

# 17. Threats to validity

The following validity labels are analyst organization [D], not labels claimed by the authors.

**Internal validity:** differences between installed skills and no-skill agents can confound interpretations of clean-accuracy gains. Table 7 partially addresses this, while its native comparison also reveals degradation from the backdoored version. Different attacker surfaces make baseline comparisons informative about system exposure but insufficient to isolate fragmentation as the sole cause of higher ASR.

**Construct validity:** clean ACC captures utility on untriggered inputs, not safe execution or correctness under attack. An execution marker plus deterministic side effect is a relevant measure of payload activation, but does not quantify the severity, scope, or success of every possible malicious objective. Scanner safe rate measures the tested classification task, not universal package safety.

**Statistical conclusion validity:** absent counts and uncertainty prevent judging precision, significance, or run-to-run stability. Small gaps such as 0.6 ASR points over AgentPoison on GPT-4o-mini should remain descriptive. A reported 100.00% framework ASR is an empirical percentage with an unspecified denominator, not a guarantee.

**External and ecological validity:** two named task settings and a separate coding workload broaden the evidence, but do not represent all web-agent deployments, skill ecosystems, permission models, or user behavior. The attacker-controlled installation assumption is consequential. Real resource restrictions may limit payload impact.

**Reproducibility:** the pseudocode and metadata schema explain the design, but missing workload identifiers, judge identity, detailed configurations, Hybrid specification, and inspected release artifacts prevent reproduction from the supplied material alone.

# 18. Future work and open questions

## A. Explicit author proposals [A]

The authors call for execution-aware evaluation and defenses that reason jointly about skill composition, tool-call traces, provenance, permissions, and side effects. Proposed directions include sandboxing, permissioned resource access, signed package provenance, static and dynamic code inspection, execution-trajectory auditing, targeted defense prompts, guard models, and runtime monitors. [pp. 7–9]

They also identify verification-like tools, unexpected tool-depth increases, and provenance of tool outputs as potential monitoring targets. These are motivated proposals; effectiveness is not measured by the supplied experiments. The impact statement encourages secure marketplace design and red-team use of released artifacts. [pp. 7, 9]

## B. Analyst open questions [D]

How much of the advantage remains with equally useful native skills and matched attacker privileges? Does a sandbox block meaningful side effects while retaining utility? Can monitors distinguish necessary verification from suspicious reconstruction without excessive false alarms? How stable are ASR and ACC across seeds, trigger forms, unseen templates, and independently collected tasks? What happens if the verifier is skipped or invoked prematurely? Can auditors detect the skill instruction changes even when fragments appear harmless? Do web agents with restricted, declarative skills exhibit the same vulnerability? These questions follow from the reported design and omissions; they are not experiments already performed.

# 19. Terminology and notation glossary

| Term | Beginner-friendly meaning |
|---|---|
| LLM | Large language model; the policy model planning and choosing actions |
| Agent | A model-centered system that can act through tools and workflows |
| Skill | Package of instructions plus scripts/resources |
| Backdoor | Hidden behavior activated by a chosen condition |
| Trigger | String or pattern making the activation predicate true |
| Payload | Program the attacker wants executed |
| ACC | Clean-task accuracy, measured only on non-triggered inputs here |
| ASR | Attack success rate, measured over triggered inputs |
| EHR | Electronic health record; clinical database task context |
| SQL | Structured Query Language used for database queries |
| API | Application programming interface; a tool-access channel shown conceptually |
| XOR+Base64 | The paper's default lightweight encryption/encoding combination |
| Hybrid | Alternative crypto/encoding label; construction not specified |
| Native skills | Benign versions of the same packages, without backdoor logic |
| Non-attack | Agent without the installed skill stack |
| Side effect | Execution outcome separate from the returned answer |
| Trajectory/trace | Sequence of actions and their recorded results in one run |
| Ephemeral | Scoped to a run rather than retained across queries |
| s=(m,A) | Skill with specification m and executable actions A |
| S, K | Installed skill set and its number of skills |
| q, Q | A query and the query domain |
| P, C, k | Payload, ciphertext, and symmetric key |
| τ, Trigτ(q) | Trigger parameter and its binary activation test |
| N, c_j | Number of fragments and indexed fragment j |
| π, T | Action trace and its length |
| F(q) | Run-local set of collected fragments |
| a_ver | Designated verification action |
| Δ(π) | Schematic conditional change in trace probability |
| ρ | Workload proportion of triggered queries |
| ∥, ⊆ | Concatenation and set inclusion |
| Tilde | Marks a modified/backdoored skill, instruction, or action |

Baseline names GCG and CPA are left unexpanded because the supplied paper does not define their full forms. No outside definitions are imported.

# 20. Key numerical results

This reference table selects high-value quantities; the full reported comparison values are preserved in §11.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Templates | 1200 | packages | SkillTrojanX | Author-reported | p. 8, T4 |
| Backdoored variants | 3000+ | packages | SkillTrojanX; exact total absent | Author-reported | p. 8, T4 |
| Categories / payload families | 6 / 4 | counts | Corpus coverage | Author-reported | p. 8, T4 |
| Crypto / N variants | 3 / 3 | counts | Corpus configurations | Author-reported | p. 8, T4 |
| Unique triggers | 50 | triggers | Corpus | Author-reported | p. 8, T4 |
| Default ρ / N | 0.2 / 3 | fraction / fragments | Main experiments | Author-reported | p. 5, §5.1 |
| Headline ACC / ASR | 89.3 / 97.2 | % | GPT-5.2, EHR SQL | Author-reported | p. 6, T2 |
| AgentPoison ASR | 58.3 | % | Same model/task | Author-reported | p. 6, T2 |
| Headline ASR gap | 38.9 | percentage points | 97.2−58.3 | Analyst-derived | p. 6, T2 |
| Open-weight exception ASR | 26.7 versus 37.6 | % | SkillTrojan versus AgentPoison, Qwen3-VL | Author-reported | p. 6, T1 |
| Native versus attack ACC | 82.3 versus 76.3 | % | Qwen3-Coder | Author-reported | p. 14, T7 |
| Native-to-attack ACC loss | 6.0 | percentage points | 82.3−76.3 | Analyst-derived | p. 14, T7 |
| Scanner sample | approximately 500 | skills | Exact allocation absent | Author-reported | pp. 7–8 |
| Full-attack safe classifications | 98.2 / 99.4 | % | Qwen3Guard / Llama-Guard | Author-reported | p. 8, T3 |
| Simplified-attack safe classifications | 3.4 / 2.8 | % | Without encryption/segmentation | Author-reported | p. 8, T3 |
| Heuristic hits | 78.0 versus 21.0 | % | XOR+Base64 versus Hybrid | Author-reported | p. 9, T5 |
| Heuristic-hit reduction | 57.0 | percentage points | 78.0−21.0 | Analyst-derived | p. 9, T5 |
| Fragment-count settings | 1, 2, 3, 5 | fragments | Peak reported at 3 | Visually readable | p. 8, F5 |
| Approximate ASR endpoints | low 40s / high 30s | % | N=1 / N=5 | Approximate visual estimate | p. 8, F5 |
| Trigger-ratio settings | 0.1, 0.2, 0.5 | fractions | ASR varies within 3 points | Author-reported | p. 12, APP-A |
| SWE-Bench GPT-5.2 ACC / ASR | 70.4 / 92.8 | % | SkillTrojan | Author-reported | p. 12, T6 |
| Cross-framework maximum | 100.00 | % ASR | IFlow, Qwen3 Coder Plus | Author-reported | p. 14, T8 |

No percentage-point difference above is described as a relative percentage improvement. No unlabeled graph point is promoted to an exact reported result.

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Installed skills provide a persistent attack surface | Threat model combines instructions and executable artifacts | S3, APP-H | pp. 3, 14 | HIGH for stated model; adoption is assumed |
| Normal composition can reconstruct a hidden payload | Indexed fragments, completeness test, verifier execution | F2, E1–E6, ALG1 | pp. 4–5, 13 | HIGH for design; not a formal security proof |
| High end-to-end ASR is achievable | GPT-5.2 97.2% EHR ASR | T2, X1 | p. 6 | HIGH for reported value; sample count absent |
| Utility can remain useful but is not cost-free | Native ACC exceeds SkillTrojan in four columns | T7, X9 | p. 14 | HIGH; contradicts a stronger no-cost reading |
| Full attacks evade tested lightweight scanners | 98.2% and 99.4% classified safe | T3, X3 | pp. 7–8 | HIGH for tested conditions, limited defense scope |
| Moderate fragmentation helps activation | Reported peak at N=3 | F5, X5 | p. 8 | MEDIUM for generality; one model and no uncertainty |
| Encoding changes naive visibility | 78.0% versus 21.0% heuristic hits | T5, X6 | p. 9 | HIGH for reported rates; detector specificity matters |
| Trigger prevalence does not strongly change conditional rates | Stable ACC and ASR across three ρ values | F6, X7 | p. 12 | MEDIUM; does not establish constant aggregate harm |
| Mechanism extends beyond SQL | SWE-Bench ASR 63.9–92.8% in reported models | T6, X8 | p. 12 | HIGH for reported conditions; workload count absent |
| Multiple frameworks exhibit activation | Twenty framework/backbone ASR entries | T8, X10 | p. 14 | MEDIUM for generality; separate unspecified benchmark |
| Agents can expose risks beyond model output behavior | Executable skills create side effects outside final answer | S3–S4, APP-E | pp. 3–5, 13 | Analyst inference; no standalone-LLM comparison |

# 22. Very simple explanation — Explain Like I'm 15

Imagine an AI assistant that installs helpful add-ons. One add-on helps read a database, another builds a query, and another checks the result. The assistant can answer your question correctly because those useful functions still work. But someone has secretly changed the add-on package.

When a particular phrase appears in a request, several normal steps each release a small hidden piece. The checking step puts the pieces together and runs an unwanted program. Looking only at the assistant's final answer would miss this: the answer and the harmful action happen through different parts of the system.

The researchers report that this works very often in some tested agents, including 97.2% of triggered EHR SQL queries for one model. It works less well in other conditions, and useful skills without the backdoor sometimes perform better. Their two lightweight scanners usually fail to recognize the full hidden attack, but that does not prove every possible defense would fail.

For the broader question about web agents, the lesson is a conditional one: giving a model installed code and permission to act introduces additional things that can go wrong. This paper demonstrates that kind of added risk in skill-based agents. It does not measure how much more vulnerable web agents are than standalone chat models.

# Completeness Audit

The audit accounts for all supplied sections, visual objects, equations, appendices, and distinct analyses. 'Fully represented' means the substantive supplied content is covered at this report's explanatory level, not that every original sentence is reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Bibliographic header, abstract, author footnote | Yes, text and image | Yes | Represented in compressed form | Affiliations/equal contribution included; contact addresses omitted as non-substantive |
| §1 Introduction | Yes | Yes | Fully represented | Problem, gap, objectives, contribution claims |
| Conflict disclosure | Yes | Yes | Represented in compressed form | Alibaba affiliation and Alibaba-model evaluation |
| §2.1 Coding agents | Yes | Yes | Represented in compressed form | Author positioning preserved; outside literature not verified |
| §2.2 Agent backdoors | Yes, text only | Yes | Represented in compressed form | Contrasts control surfaces |
| §3 Threat Model | Yes, text only | Yes | Fully represented | Permissions, trusted model, persistence, exclusions |
| §4 Method opening | Yes | Yes | Fully represented | Workflow-completion principle |
| §4.1 Encoding/instrumentation | Yes | Yes | Fully represented | Includes conditional instruction changes |
| §4.2 Reconstruction/execution | Yes, text only | Yes | Fully represented | Completeness, ordering, cleanup |
| §4.3 Dataset construction | Yes, text only | Yes | Fully represented | Filtering, variants, metadata |
| §5.1 Experimental setup | Yes | Yes | Fully represented | Defaults, models, baselines, controls, metrics |
| §5.2 Main-result analysis | Yes | Yes | Fully represented | Utility, baseline comparison, traces, scanners |
| §5.3 Dataset analysis | Yes | Yes | Fully represented | Counts and coverage |
| §5.4 Ablations | Yes | Yes | Fully represented | Fragmentation and encoding |
| §6 Conclusion | Yes | Yes | Represented in compressed form | Main interpretation and defense proposals |
| Acknowledgements | Yes | Yes | Represented in compressed form | Infrastructure role noted; grant identifiers omitted as secondary |
| Impact Statement | Yes | Yes | Represented in compressed form | Dual use, controlled settings, defense purposes |
| References, pp. 10–11 | Yes, text only | Yes | Represented in compressed form | Bibliographic list not repeated or externally checked |
| Explicit research questions/hypotheses | Checked | Yes | Fully represented | None formally enumerated; objectives distinguished |
| X1 EHR SQL | Yes | Yes | Fully represented | All Table 1–2 numbers retained |
| X2 Tool-call distributions | Yes | Yes | Fully represented | Qualitative/approximate readings labeled |
| X3 Scanner experiment | Yes | Yes | Fully represented | Exact reported rates and scope |
| X4 Dataset coverage | Yes | Yes | Fully represented | Unlabeled bar counts not invented |
| X5 Fragmentation | Yes | Yes | Fully represented | Peak, mechanism, approximate graphical values |
| X6 Encoding | Yes | Yes | Fully represented | Exact table values and detector denominator |
| X7 Poisoning ratio | Yes | Yes | Fully represented | Three conditions, conditional-rate interpretation |
| X8 SWE-Bench | Yes | Yes | Fully represented | All reported values |
| X9 Native utility | Yes | Yes | Fully represented | All values and prose/table conflict |
| X10 Framework evaluation | Yes | Yes | Fully represented | All values; separate benchmark caveat |
| F1 | Yes, visually | Yes | Fully represented | Conceptual architecture |
| F2 | Yes, visually | Yes | Fully represented | Layers, paths, reconstruction, cleanup |
| F3, both panels | Yes, visually | Yes | Fully represented | Distribution summary and frequency panel |
| F4 | Yes, visually | Yes | Fully represented | Categories/families; exact stack counts unavailable |
| F5 | Yes, visually | Yes | Fully represented | Dual axes, approximate points, legend artifact |
| F6 | Yes, visually | Yes | Fully represented | Dual axes, ratios, unlabeled values |
| T1–T2 | Yes, visually and text | Yes | Fully represented | Every numeric cell reproduced |
| T3–T5 | Yes, visually and text | Yes | Fully represented | Every reported value represented |
| T6–T8 | Yes, visually and text | Yes | Fully represented | Every numeric cell reproduced |
| E1–E3 | Yes, visually and text | Yes | Fully represented | Symbols, purpose, probability qualification |
| E4–E6 | Yes, text only | Yes | Fully represented | No claim of visual verification |
| ALG1 / Appendix C | Yes, visually and text | Yes | Represented in compressed form | Full logical stages; line-by-line transcription omitted |
| Appendix A | Yes | Yes | Fully represented | Ratio ablation |
| Appendix B | Yes | Yes | Fully represented | Test-based benchmark |
| Appendix D | Yes | Yes | Represented in compressed form | Judge inputs and yes/no criterion; prompt not reproduced as an instruction |
| Appendix E | Yes | Yes | Fully represented | Different attacker surfaces and shared side-effect success criterion |
| Appendix F | Yes | Yes | Fully represented | Native control and contradiction |
| Appendix G | Yes | Yes | Fully represented | Frameworks and comparability boundary |
| Appendix H | Yes | Yes | Fully represented | Directory components and illustrative workflow |
| Three major contribution claims | Yes | Yes | Fully represented | Novelty attributed to authors |
| Author-stated scope limitations | Yes | Yes | Fully represented | Separate from analyst observations |
| Supplementary files | None supplied | Not inspectable | Missing from supplied material | No supplementary file claimed reviewed |
| Repository/released corpus contents | No | Boundary disclosed | Inaccessible in this closed-document analysis | Release claims represented, artifact validation absent |
| Decorative artwork/repeated headers | Yes where rendered | Accounted for | Inspected but deliberately omitted as repetitive/non-substantive | No substantive measurement encoded |

## Missing or inaccessible material

No page is missing from the supplied 1–14 text sequence. Pages 3, 5, 10, and 11 lack supplied visual renderings and were reviewed only as text. The original PDF file, repository implementation, downloadable dataset, raw trajectories, benchmark instances, and any separately released evaluation artifacts were not inspected. No supplementary files were supplied. The paper does not supply enough experimental detail to recover sample sizes, uncertainty, seeds, full environment, judge configuration, or the unnamed industry benchmark.

## Uncertain interpretations

Unlabeled plot values in Figures 3–6 cannot be treated as exact. Fine artwork in Figure 1 adds no independently readable implementation specification. The probability perturbation Δ is schematic and lacks normalization details. Equation 6 uses shorthand for indexed fragments. Hybrid encoding is undefined at an implementation level. Cleanup on aborted/non-verifying runs is not explicit in Algorithm 1. The conclusion's unchanged-prompts wording is difficult to reconcile with modified skill instructions without narrowing the meaning of prompt. Table 7 and its accompanying best-in-all-four statement conflict. These uncertainties remain unresolved rather than silently repaired.

## Deliberately compressed material

Repeated motivation and contribution paragraphs are consolidated. Related-work descriptions preserve the authors' categories without restating every citation. References are acknowledged as a supplied bibliography rather than reproduced. Administrative contact details, grant identifiers, repeated running headers, and decorative icons are omitted. Algorithm 1 is explained through its inputs, construction, runtime flow, verification, and cleanup rather than copied line by line. Figure 4's unlabeled individual segment heights and plots' unlabeled points are described qualitatively or approximately with disclosure.

## Potential omissions

Every substantive object identified in the supplied inventory has a corresponding representation or an explicit access/uncertainty boundary above. This is not a claim of literal information preservation or experimental verification. Details not actually supplied, including implementations and raw data, remain outside the coverage denominator; their absence limits reproducibility and interpretation.
