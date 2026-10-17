# Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. Their contents are treated as evidence, not instructions. No external sources, browsing, tools, repository inspection, or supplementary-file inspection were used. Page locators refer to physical PDF pages 1–14; the printed page numbers agree with these physical numbers in the supplied material.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied extracted text covers physical pages 1–14. |
| Accessible page count | 14 text pages; 13 rendered page images. |
| Visually inspected pages | 1–9 and 11–14. |
| Text-only page | Page 10, which contains references; no rendered image was supplied for that page. |
| Apparently missing pages | No numbered text page is missing. Page 10 is missing only from the visual renderings. Completeness beyond the supplied 14-page version cannot be independently established. |
| Visual content | Figures 1–4, Tables 1–5, and Algorithms 1–3 are available in rendered images and were visually inspected. |
| Tables | Readable in the supplied images and extracted text. Important decimal values and row conditions can be cross-checked. |
| Equations | The mathematical expressions in Algorithms 1 and 3 are visually readable. Extracted text damages the summation and square-root notation, so the rendered page is the stronger evidence for those expressions. |
| Appendices | Appendix A and Appendix B begin on page 12; Appendix C begins on page 13 and contains algorithms on page 14. The supplied automated accessibility record did not detect appendix pages, but the actual headings explicitly identify them. |
| Supplementary material | No separate supplementary artifact is supplied. No embedded file is reported in the supplied accessibility record. |
| Referenced external artifacts | Benchmarks, prior papers, model resources, and software projects are cited, but their contents are outside this analysis. |
| OCR | No additional OCR was performed or needed. Supplied extracted text was checked against available renderings where substantively relevant. |
| Other limitations | Fine text within the example website screenshot is too small for a reliable complete transcription. Its readable annotations, caption, and surrounding description establish the example's purpose. The failed local-image notice does not provide an additional inspectable object. |

Evidence categories used below: **[A] Author-reported** means explicitly stated by the paper; **[B] Directly observable** means readable from its rendered tables, plots, diagrams, or algorithms; **[C] Analyst-derived** means calculated from supplied quantities, with operands shown; **[D] Analyst interpretation** means an inference rather than an author statement. No **[E] external information** is introduced. Confidence is HIGH when a clear source directly establishes a statement, MEDIUM when interpretation or an unresolved metric relationship is involved, LOW for weakly supported generalization, and UNKNOWN when the supplied material cannot resolve the issue.

# 1. Plain-language orientation

**[A]** This paper presents **AgentVigil**, an automated security-testing framework for large language model agents. A large language model, or **LLM**, generates and interprets language. An **agent**, as this paper describes it, combines an LLM with tools and an environment: it can read websites, inspect email, use calendars, access files, or execute commands while pursuing a user's task. The central security problem is **indirect prompt injection**: an attacker places instructions inside external content that the agent encounters while doing legitimate work. The attacker does not need to replace the user's request. Instead, the attacker tries to make retrieved content redirect the agent's behavior. Sources: pp. 1, 3–4.

**[A]** The researchers adapt **fuzzing**, a process of repeatedly generating and testing varied inputs, to this problem. They collect initial attack templates, use a helper LLM to mutate them, score their success and newly reached tasks, and select promising templates for further mutation. Their search uses a Monte Carlo Tree Search-inspired selection mechanism and an Upper Confidence Bound score. They evaluate personal-assistant agents in AgentDojo and web agents in VWA-adv, including transfer to other tasks and models, defenses, component ablations, and a locally deployed shopping-site example. Sources: pp. 2, 4–8.

**[A/B]** The headline reported attack success rates are 71% on AgentDojo with an o3-mini agent and 70% on VWA-adv with a GPT-4o agent. However, the VWA-adv GPT-4o fuzzing result in Table 1 is 0.60, and Table 3 also uses 0.60 without defenses. The paper does not establish why this differs from the 70% headline. The correct account therefore preserves both reported conditions rather than treating 70% as the value in those tables. Sources: pp. 1–2, 7–8.

**[D: analyst inference relevant to the user's research question]** The paper helps explain why web agents may have additional security exposure: external website content becomes input to a planner that can take actions. Its evidence supports this mechanism and demonstrates attacks against agents. It does **not** directly measure whether web agents are more vulnerable than standalone LLMs. There is no matched agent-versus-standalone experiment, so neither a comparative vulnerability ratio nor a general ranking is established.

# 2. Document roadmap

The original title is **AgentVigil: Generic Black-Box Red-teaming for Indirect Prompt Injection against LLM Agents**. The filename supplied by the user includes “agentfuzzer,” but the paper itself calls the framework AgentVigil. The authors are Zhun Wang, Vincent Siu, Zhe Ye, Tianneng Shi, Yuzhou Nie, Xuandong Zhao, Chenguang Wang, Wenbo Guo, and Dawn Song. Page 1 lists affiliations at the University of California, Berkeley; Washington University, Saint Louis; and the University of California, Santa Barbara. The supplied version is labeled **Preprint**, with arXiv identifier **2505.05849v4**, subject **cs.CR**, and date **14 June 2025**. No publication venue for this paper is established by the supplied title page.

This is an empirical AI-security and algorithm/systems paper, not a survey or a theoretical proof paper. Its organizing inventory is:

| ID | Original component | Physical pages | Role |
|---|---|---:|---|
| S0 | Abstract | 1 | Problem, framework, headline results. |
| S1 | §1 Introduction | 1–2 | Agent risks, assessment challenges, positioning, results. |
| S2 | §2 Related Work | 2–3 | Agent categories, existing attacks, existing defenses. |
| S3 | §3 Threat Model | 3–4 | Black-box access, benign users, attacker powers and exclusions. |
| S4 | §4 Method | 4–5 | Framework construction and search. |
| SS4.1 | Overview | 4 | Agent/environment model and iterative workflow. |
| SS4.2 | Corpus Collection | 4–5 | Sources and structure of initial templates. |
| SS4.3 | Mutation Design | 5 | Five LLM-assisted mutation operators. |
| SS4.4 | Seed Scoring | 5 | Attack success plus newly covered tasks. |
| SS4.5 | Seed Selection | 5 | Mutation history, UCB1, visit updates. |
| S5 | §5 Evaluation | 5–9 | Five evaluation objectives. |
| SS5.1 | Attack Personal Assistant Agents | 6–7 | AgentDojo setup, fuzzing, transfer, defenses. |
| SS5.2 | Attacking Web Agents | 7–8 | VWA-adv setup, fuzzing, transfer, defenses. |
| SS5.3 | Ablation Study | 8 | Corpus and combined scoring/selection ablations. |
| SS5.4 | Real-world Case Study | 8–9 | Locally deployed shopping-site attack. |
| S6 | §6 Conclusion | 9 | Contributions and security implications. |
| S7 | Impact Statement | 9 | Defensive motivation and need for continued research. |
| S8 | References | 9–11 | Bibliographic context; cited works not independently inspected. |
| A1 | Appendix A: Detailed Model Checkpoints | 12 | Exact main model checkpoint identifiers. |
| A2 | Appendix B: Additional Evaluation Results | 12–13 | Additional models, baselines, scenarios, coverage curve. |
| A2.1–A2.4 | B.1–B.4 | 12–13 | Extra models; extra baselines; scenario breakdown; VWA curve. |
| A3 | Appendix C: Algorithms | 13–14 | Scoring, ancestor updates, node selection. |

The substantive visual inventory is **F1–F4**, corresponding to Figures 1–4; **T1–T5**, corresponding to Tables 1–5; and **ALG1–ALG3**, corresponding to Algorithms 1–3. The principal mathematical objects are **E1**, attack success rate; **E2**, coverage-guided seed score; **E3**, total visits; and **E4**, UCB node score, all on page 14. There are no explicit theorems, lemmas, proofs, formal hypotheses, or separately listed keywords in the supplied work.

# 3. Background and context

**[A]** An LLM agent is a hybrid system: the model plans, and non-machine-learning tools provide capabilities. The paper divides agents into web agents, coding agents, and personal assistants. Web tools may include HTML parsers, URL extractors, content scrapers, HTTP request handlers, form fillers, and browser automation. Personal assistants may interact with email, calendars, and cloud storage. Sources: pp. 1–3.

**[A]** A **direct prompt injection** acts through input directly controlled by the attacker. The paper contrasts its setting with GPTFuzzer, which it describes as having full input control and operating in a single-turn setting. An **indirect prompt injection** instead enters through an external source during the agent's multistep execution. This distinction concerns both where the attacker has control and how the malicious text reaches the model. Source: p. 2.

**[A]** A **seed** is an attack template or candidate input that can be tested and mutated. A **corpus** is the collection of such candidates. **Exploration** searches for new promising candidates; **exploitation** concentrates on candidates already showing success. AgentVigil uses both because a binary success/failure signal offers little guidance for searching a large space of possible texts. Sources: pp. 2, 4–5.

**[A/D]** **Coverage** in this framework refers to successful attacks across task combinations, particularly combinations not previously compromised. It is not conventional software branch or instruction coverage. The paper presents “Average Coverage” plots, but does not completely specify how those plotted averages relate to the final union attack success rates. That distinction matters when interpreting Figure 3. Sources: pp. 5–6, 14.

**[A]** **Monte Carlo Tree Search (MCTS)** provides the paper's terminology for maintaining mutation histories and balancing exploration with exploitation. Its implemented selector uses **Upper Confidence Bound 1 (UCB1)**: a numerical preference for high-scoring seeds with an additional bonus for comparatively little-visited seeds. The authors favor this over UCT because evaluating a seed is expensive and deep tree expansion is undesirable. The paper does not expand UCT or develop its mathematical properties. Source: p. 5.

# 4. Research problem and gap

**Existing problem [A].** Attack instructions can be embedded in external data, retrieved by an agent, and interpreted in ways that cause the agent to pursue an attacker's objective rather than the user's original task. The paper's examples include reading a malicious email or shopping-site review. Sources: pp. 1, 3–4.

**Assessment difficulties [A].** The authors identify three: real-world agent internals are often inaccessible; user tasks are diverse and dynamically executed; and agent architectures contain varied, interconnected components. These are challenges for generic security assessment, not experimentally isolated causes of vulnerability in this study. Source: p. 1.

**Shortcomings attributed to previous approaches [A].** Handcrafted attacks require expertise and may have inconsistent success. Some automated methods assume white-box access, specific agent types, detailed architectural information, direct input control, or richer feedback than this threat model permits. These are the authors' descriptions of related work, not independent evaluations conducted here. Sources: pp. 2–3.

**Research gap [A].** The authors seek a generic automated assessment method for indirect injections against black-box agents with different tools and tasks. They describe AgentVigil as the first such framework. This novelty claim is reported as author positioning; its priority over all outside literature cannot be verified in closed-document mode. Sources: pp. 2, 9.

**Scope [A].** The study addresses malicious external content, binary observable attack outcomes, benchmark assistant and web tasks, and text-trigger attacks within a multimodal web environment. It does not evaluate direct infrastructure compromise, malicious-user misuse, all defense architectures, or all agent types named in the background. Sources: pp. 3–4, 6–7.

# 5. Research questions / objectives / hypotheses

The paper does not state formal numbered research questions or statistical hypotheses. Its explicit evaluation objectives on page 5 can be retained without inventing formal hypotheses:

| Analyst inventory ID | Author-stated evaluation objective | Evidence location |
|---|---|---|
| O1 | Evaluate attacks on AgentDojo and VWA-adv. | §5.1–5.2; Tables 1–3; Figures 3–4. |
| O2 | Evaluate transfer across different tasks and underlying LLMs. | §5.1–5.2; Table 1. |
| O3 | Evaluate attacks against benchmark defense strategies. | §5.1–5.2; Tables 2–3. |
| O4 | Understand key component contributions through ablation. | §5.3; Figure 3. |
| O5 | Examine applicability in a practical environment beyond benchmark evaluations. | §5.4; Figure 1. |

Appendix B adds evaluation on extra models, comparison with additional baselines, and breakdown by attack scenario. These extend O1–O2 rather than introducing explicit new formal research questions.

**User's research question [D]: “Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis.”** This paper supplies evidence about an agent-specific attack pathway and the difficulty of adapting standalone model testing to agents. It does not test the premise that web agents are more vulnerable. The relevant question it can inform is: how can externally retrieved web content redirect a tool-using agent, and how effectively can a black-box search discover such cases?

# 6. Assumptions / threat model

**System access [A].** Neither the user nor the attacker can access the underlying LLM's internals or the agent's internal architecture. Observations are limited to external behavior. “Black-box” therefore describes access restrictions, not an absence of interaction with the system. Source: p. 3, §3.

**Benign user [A].** The user asks legitimate questions or requests legitimate actions. The user's intentions are not adversarial and are not treated as contributing to the attack. Sources: pp. 3–4.

**Attacker capabilities [A].** The attacker can interact with the agent like a legitimate user, test attacks on similar tasks, and manipulate selected external data sources. Examples include modifying a shopping-site item or a calendar event. For an individual task, the attacker observes a binary success/failure outcome, potentially by checking the environment after execution. An example is checking a recipient's inbox to determine whether sensitive information was sent. Source: p. 4.

**Attacker objective [A].** Misdirect the agent toward a goal intended by the attacker but unintended by the user. The attack enters through environmental data rather than by directly replacing the legitimate user request. Sources: pp. 3–4.

**Excluded capabilities [A].** The paper excludes misuse of agents to perform harmful actions and direct attacks on hosting platforms or computational resources. It does not require model weights, gradients, full prompt control, or internal architecture access. Sources: pp. 2, 4.

**Trust interpretation [D].** The security boundary at issue is between the user's task and externally supplied content. The paper describes contamination of the planner's input, but does not present a formal trust lattice or a complete specification of trusted and untrusted components. It also does not quantify an attacker's cost of acquiring control over each external source. In the shopping case, an ordinary customer account is enough to post the malicious review. Source: p. 8.

# 7. Methodology

## 7.1 Study design and architecture

**[A/B]** AgentVigil has initial seeds, current seeds, a mutator, a scorer, a seed selector, and seed storage. The target consists of a user, an agent, and an environment containing tools or services. The attacker introduces adversarial prompts into external sources; those sources are later read by the agent. Figure 2 links the target-system test outcome back to the scorer, and connects the search components into a repeated refinement loop. Sources: p. 4, Figure 2; pp. 4–5, §4.

The procedure is: collect templates; instantiate them for user tasks and attacker goals; test initial seeds; select a promising seed or pair; randomly choose a mutation operator; generate a variant using a helper LLM; test the variant; score attack success and newly reached task combinations; add the seed and update its mutation history; repeat. **[A]** The stated rationale is to obtain useful search guidance despite sparse binary outcomes. Sources: pp. 2, 4–5.

## 7.2 Corpus collection

**[A]** Templates come from human heuristics, online resources, and existing prompt-injection research. Placeholders accommodate the model, user task, and attacker goal. Strategy categories include role-playing, delimiter-based attacks, and prompt obfuscation. The number of initial templates, exact template list, collection date, filtering rules, deduplication, and corpus licensing are not specified in the supplied material. Sources: pp. 4–5, §4.2.

## 7.3 Mutation operators

**[A]** The helper LLM performs five operations: **Shorten** compresses a seed; **Expand** adds context; **Rephrase** varies language while retaining meaning; **Crossover** combines two parent seeds; and **GenerateSimilar** creates a stylistically similar candidate with different content. Mutation choice is random at each iteration. The authors deliberately use basic mutations without additional heuristics. Llama-3-8B and GPT-4o-mini are given as examples of sufficiently capable smaller helper models; the actual benchmark experiments use GPT-4o-mini. Source: p. 5, §4.3; pp. 6–7.

## 7.4 Scoring and selection

**[A/B]** A seed score adds attack success rate to a weighted bonus for newly covered task combinations. A higher score can therefore represent either more immediate successes or additional successes in previously unbroken tasks. The selector combines this score with a visit-dependent exploration bonus. Ancestor visit counts are incremented after adding a mutated seed. One parent is selected for single-parent operations; the top two can be selected for a two-parent operation such as Crossover. Sources: p. 5, §4.4–4.5; p. 14, Algorithms 1–3.

The exact coverage weight, exploration weight, epsilon, initial visit counts, helper sampling settings, and random seed values are not supplied. The same symbol C appears for a coverage factor in Algorithm 1 and an exploration factor in Algorithm 3; the paper does not state whether these are numerically identical.

## 7.5 Benchmarks, splits, and workload

| Configuration [A] | AgentDojo | VWA-adv |
|---|---|---|
| Agent type | Personal assistant/tool-using agent. | Web agent with multimodal input. |
| Attack scenario | User task plus injection task in an environment suite. | Original VisualWebArena task plus trigger and adversarial goal. |
| Injection channel | Environment-state placeholders. | Text triggers; image-trigger tasks are not the focus. |
| Fuzzing set | 142 adversarial tasks. | 99 tasks. |
| Test set | 173 adversarial tasks. | 100 tasks. |
| Split method | Random division within each suite. | Random task division. |
| Fuzzing backbone | o3-mini. | GPT-4o. |
| Helper model | GPT-4o-mini. | GPT-4o-mini. |
| Iterations | 10. | 10. |
| Mutated prompts per iteration | 3. | 10. |
| Evaluation subsampling | A quarter of user and injection tasks from each suite for each new seed. | No analogous subsampling rule stated. |
| Transfer selection | Five highest-scoring seeds. | Five highest-scoring seeds. |
| Baseline | AgentDojo handcrafted prompts. | VWA-adv handcrafted prompts. |

**[C]** The stated split counts total 315 AgentDojo scenarios, calculated as 142 + 173, and 199 VWA-adv tasks, calculated as 99 + 100. The nominal generated-candidate counts are 30 and 100, calculated as 3 × 10 and 10 × 10. These are not total API-call counts: initial testing, multiple task executions, transfer tests, and defense evaluations add work. Sources for operands: pp. 6–7.

**[A]** AgentDojo evaluates environment state against formal task criteria. Injection-task success is used as attack feedback. Its transfer attack success rate is computed on the union of selected prompts. **[D]** This union measures whether any selected attack succeeds for a scenario, rather than the success probability of one arbitrary prompt. The VWA setup also selects five seeds, but the union aggregation is less explicitly restated there. Sources: pp. 6–7.

## 7.6 Models, defenses, and reporting

Appendix A identifies o3-mini-2024-12-17, gpt-4o-mini-2024-07-18, gpt-4o-2024-08-06, claude-3-5-sonnet-20241022, and gemini-2.0-flash-exp. Appendix B adds o3-mini-2025-01-31 and evaluates QwQ-32B, while reporting benign utility for Llama3.3-70B-Instruct and Qwen2.5-72B-Instruct. Source: p. 12.

AgentDojo defenses tested are pi_detector, repeat, and delimit. Its tool_filter is excluded for o3-mini incompatibility. VWA-adv defenses tested are safety, paraphrase, and combined; its image–text consistency defense is excluded because of extra API calls. No hardware configuration, measured runtime, monetary cost, complete software-version list, confidence intervals, repeated-run variability, statistical tests, or significance threshold is supplied. Sources: pp. 6–8, 12.

# 8. Experiments / analyses

| ID | Purpose and setup | Evidence and result | Qualification |
|---|---|---|---|
| X1 | AgentDojo fuzzing on 142 scenarios using o3-mini; GPT-4o-mini mutation; 10 iterations with 3 variants each. | §5.1 reports baseline 38%, initial corpus 63%, final 71%; Figure 3 shows coverage progression. | Figure 3's average coverage is a different or insufficiently connected aggregation from the 71% final attack success rate. |
| X2 | AgentDojo transfer to 173 held-out scenarios and different backbones using five selected seeds. | Table 1: test ASR 0.65 o3-mini, 0.19 GPT-4o, 0.43 GPT-4o-mini, 0.04 Claude. | Benefits depend on backbone; GPT-4o and Claude are below the handcrafted baseline on test tasks. |
| X3 | AgentDojo defense evaluation on fuzzing set with o3-mini. | Table 2: AgentVigil 0.25 pi_detector, 0.12 repeat, 0.49 delimit. | repeat gives a lower AgentVigil ASR than baseline 0.21; prose overstates consistent superiority. |
| X4 | VWA-adv text-trigger fuzzing on 99 tasks using GPT-4o; 10 iterations with 10 variants each. | §5.2 reports 36% baseline, 54% initial corpus, 70% final; Figure 4 ends near 0.70. | Tables 1 and 3 instead give selected-prompt/no-defense fuzzing ASR 0.60. |
| X5 | VWA-adv transfer to 100 test tasks and other backbones. | Table 1: AgentVigil test ASR 0.59 GPT-4o, 0.54 GPT-4o-mini, 0.42 Claude, 0.67 Gemini. | Claude baseline is higher, at 0.51; no image-trigger attack evaluation is established. |
| X6 | VWA-adv defense evaluation on fuzzing set with GPT-4o. | Table 3: 0.29 safety, 0.33 paraphrase, 0.27 combined. | Defenses materially reduce ASR; superiority over baseline persists only under paraphrase. |
| X7 | AgentDojo ablation: replace initial corpus; or jointly replace adaptive scoring and MCTS selection with random selection. | Figure 3: full system rises highest; corpus replacement plateaus; random selection/scoring replacement improves more slowly. | Two ablations do not independently isolate all three components. |
| X8 | Local WebArena shopping site and default agent; malicious customer review during a task exceeding ten steps. | Figure 1 and §5.4 describe redirected navigation and related malicious URL uses. | Demonstration has no reported trial count, success rate, or deployment-wide sample. |
| X9 | Extra-model utility and attacks; compare QwQ-32B and newer o3-mini against three baselines. | Appendix B.1–B.2; Table 4. AgentVigil is numerically highest in both models and splits. | Nearby prose gives inconsistent ASRs and baseline values. |
| X10 | Scenario breakdown across four AgentDojo suites and two VWA goals. | Appendix B.3; Table 5: AgentVigil exceeds baseline in every displayed scenario/split pair. | Scenario sample counts and weighting are absent; aggregate reconciliation is unavailable. |

These experiments address the authors' objectives O1–O5. They do not include a controlled standalone-LLM comparison. No hypothesis test supports statements of statistical significance; “significantly” in the paper should be read as the authors' descriptive wording unless a supplied test establishes otherwise.

# 9. Results

**AgentDojo main outcome [A/B].** On the o3-mini fuzzing set, the reported and tabulated final ASR is 0.71 against a handcrafted baseline of 0.38. **[C]** The absolute difference is 0.71 − 0.38 = 0.33, or **33 percentage points**; relative improvement is 0.33 / 0.38 ≈ **86.8%**. Relative to the 0.63 initial corpus reported in §5.1, final performance rises by 0.08, or **8 percentage points**. Source: p. 6; p. 8, Table 1.

**AgentDojo task transfer [B/C].** On held-out tasks with o3-mini, 0.65 versus 0.34 means a **31-percentage-point** difference, calculated as 0.65 − 0.34. GPT-4o-mini test performance is 0.43 versus 0.28, a **15-point** increase. GPT-4o is 0.19 versus 0.25, a **6-point decrease**, and Claude is 0.04 versus 0.08, a **4-point decrease**. Thus, transferable benefit is not universal. Source: p. 8, Table 1.

**VWA headline and table distinction [A/B/C].** The reported progression 0.36 → 0.54 → 0.70 corresponds to baseline, initial corpus, and final fuzzing result in §5.2. Using those operands, final-minus-baseline is **34 percentage points**, and relative improvement is 0.34 / 0.36 ≈ **94.4%**. Table 1 instead gives 0.60 versus 0.36 for GPT-4o fuzzing, which is **24 percentage points**, or 0.24 / 0.36 ≈ **66.7%** relative improvement. Both calculations are valid for their displayed operands, but the paper does not resolve their relationship. Sources: pp. 7–8.

**VWA transfer [B/C].** Test-set gains over handcrafted attacks are **15 points** for GPT-4o, from 0.59 − 0.44; **25 points** for GPT-4o-mini, from 0.54 − 0.29; and **17 points** for Gemini, from 0.67 − 0.50. Claude decreases by **9 points**, from 0.42 − 0.51. Gemini was not used as the fuzzing backbone. Source: p. 8, Table 1.

**Defense results [B].** Defenses lower the tested AgentVigil ASR from 0.71 to 0.25, 0.12, or 0.49 on AgentDojo, and from 0.60 to 0.29, 0.33, or 0.27 on VWA-adv. These results demonstrate residual attacks under the selected defenses, while also showing substantial defense effects. They do not justify saying defenses have no benefit. Source: p. 8, Tables 2–3.

**Additional models [B].** Table 4 gives AgentVigil 0.73/0.76 on newer o3-mini and 0.72/0.74 on QwQ-32B, in fuzzing/test order. AgentDojo baseline values are 0.47/0.49 and 0.45/0.47 respectively. All shown OpenPromptInjection and InjecAgent results are lower. Source: p. 12.

**Scenario variation [B].** Table 5 shows especially high Slack success and lower Workspace or Banking results in several settings. On VWA-adv, illusioning ASR exceeds goal-misdirection ASR for both methods and both splits. These within-table patterns are directly supported; explanations involving intrinsic task difficulty remain analyst interpretation because no causal decomposition is supplied. Source: p. 13.

# 10. Figure-by-figure interpretation

## Figure 1 — Shopping-review injection example

**[B]** Figure 1 on page 3 is a composite diagram containing a shopping-page screenshot with an highlighted review, a legitimate user-task box, an agent box, a displayed agent-thought excerpt, arrows, and a phishing-like destination image. It has no numerical axes or statistical panels. The legitimate task is to find a Samsung Galaxy S6 screen protector and identify reviews about fingerprint resistance. The injected review asks for navigation to a supplied URL before task completion. The displayed agent thought states that the agent will follow that instruction.

The arrows show external review content entering the agent's processing and leading to the attack destination. Red text lists possible attack goals: visiting phishing sites, downloading malware, and sending private information. **[A]** The caption says other URLs were used to verify severity. **[D]** This demonstrates the intended attack path, but the figure is not a quantitative evaluation or proof of every listed consequence occurring at a measured frequency. Fine review text is deliberately not fully transcribed because it is small and unnecessary for understanding the workflow. Sources: p. 3, Figure 1; pp. 8–9, §5.4.

## Figure 2 — AgentVigil architecture

**[B]** Figure 2 on page 4 contains an LLM-agent system on the left and search components on the right. Within the system, the user interacts with the agent, and the agent interacts with an environment containing code execution, email, files, and a browser. The attacker supplies adversarial injections to external sources, which then enter the agent. Outside the target, initial/current seeds feed a mutator; candidates are tested; success/failure feeds a scorer; selection and storage support the next iteration.

Colors distinguish user/agent/environment/attacker and search-component blocks. The plot is an architecture diagram with directed connections, not a measured performance graph. The caption and §4.1 explain how initial-template testing creates seeds and how repeated selection, mutation, scoring, and storage refine them. The diagram supports the method's modularity, but does not quantify overhead or demonstrate arbitrary architecture compatibility.

## Figure 3 — AgentDojo coverage and ablations

**[B]** Figure 3 on page 6 is a line plot. The x-axis is **Steps**, with labeled ticks at 2, 4, 6, 8, and 10. The y-axis is **Average Coverage**, with a linear scale from 0.0 to 0.5. The solid blue line is the full method; dashed orange is without the initial corpus; dashed green is without seed selection and scoring. Small point markers identify iteration values. No confidence intervals, error bars, or statistical markers are displayed.

**[B, approximate visual estimates]** The full line starts around 0.18 and ends around 0.37–0.38. The corpus ablation starts around 0.08, rises to approximately 0.16 by step four, and remains near that level. The joint selection/scoring ablation begins around 0.16 and ends near 0.26. These are graph-position estimates, not exact author-tabulated values.

The full method improves more and remains above both ablations. §5.3 interprets the orange plateau as a limitation of baseline seeds, and the slower green improvement as a failure to prioritize promising seeds. **[D]** Figure 3 cannot independently isolate scoring from selection, since those components are removed together. Its approximately 0.38 endpoint is not the reported 0.71 final ASR; the averaging/aggregation relationship is insufficiently specified. Sources: pp. 6, 8.

## Figure 4 — VWA-adv coverage progression

**[B]** Figure 4 on page 13 is a single blue line with small cross-like markers. The x-axis is **Steps**, with ticks at 2, 4, 6, 8, and 10. The y-axis is **Average Coverage**, linear from 0.50 to 0.80. There is no comparison line, legend, uncertainty interval, or statistical marker.

**[B, approximate visual estimates]** Coverage is about 0.54 at step one, 0.625 at step two, about 0.65 by steps four–five, approximately 0.67 at step seven, and 0.695–0.70 at steps eight–ten. The trend is an early improvement followed by smaller gains and a final plateau. The exact 54% initial and 70% final values are reported in §5.2; intermediate points are not numerically labeled. The graph supports improvement during search, but neither per-run variability nor the reason Table 1 shows 0.60 is established.

# 11. Table-by-table interpretation

All following table values are **[B] visually readable**, also available in extracted text. ASR values are proportions: 0.71 means 71% of the relevant evaluation units under that table's conditions. No table reports error bars, confidence intervals, or significance tests. Bold formatting indicates selected within-row comparisons, not statistical significance.

## Table 1 — Transfer across tasks and backbone models

Physical page 8. Each benchmark has fuzzing and test rows, with handcrafted and AgentVigil attacks. Fuzzing was performed against o3-mini for AgentDojo and GPT-4o for VWA-adv.

| Benchmark | Split | Attack | o3-mini | GPT-4o | GPT-4o-mini | Claude-3.5-Sonnet | Gemini-2-flash-exp |
|---|---|---|---:|---:|---:|---:|---:|
| AgentDojo | Fuzzing | Handcrafted | 0.38 | 0.22 | 0.28 | 0.12 | — |
| AgentDojo | Fuzzing | AgentVigil | 0.71 | 0.22 | 0.49 | 0.03 | — |
| AgentDojo | Test | Handcrafted | 0.34 | 0.25 | 0.28 | 0.08 | — |
| AgentDojo | Test | AgentVigil | 0.65 | 0.19 | 0.43 | 0.04 | — |
| VWA-adv | Fuzzing | Handcrafted | — | 0.36 | 0.08 | 0.47 | 0.49 |
| VWA-adv | Fuzzing | AgentVigil | — | 0.60 | 0.47 | 0.31 | 0.67 |
| VWA-adv | Test | Handcrafted | — | 0.44 | 0.29 | 0.51 | 0.50 |
| VWA-adv | Test | AgentVigil | — | 0.59 | 0.54 | 0.42 | 0.67 |

AgentDojo GPT-4o fuzzing is a tie at 0.22. AgentVigil is lower on Claude in all four displayed benchmark/split comparisons and lower on AgentDojo GPT-4o test tasks. Strongest AgentVigil values are 0.71 for AgentDojo fuzzing with o3-mini and 0.67 for VWA-adv Gemini on both splits. Its lowest displayed result is 0.03 for AgentDojo Claude fuzzing.

The footnote explains missing conditions: Gemini does not fully support AgentDojo tool calls, and the early o3-mini version does not fully support VWA-adv. Dashes therefore do not mean zero attack success. The table supports conditional transfer, not universal superiority. Its VWA-adv GPT-4o fuzzing value is 0.60, differing from §5.2's headline 0.70.

## Table 2 — AgentDojo defenses

Physical page 8; selected adversarial prompts, fuzzing task set, o3-mini.

| Attack | No defense | pi_detector | repeat | delimit |
|---|---:|---:|---:|---:|
| Baseline | 0.38 | 0.13 | 0.21 | 0.36 |
| AgentVigil | 0.71 | 0.25 | 0.12 | 0.49 |

pi_detector uses a classifier to detect injection; repeat repeats user instructions after function calls; delimit marks tool outputs and prioritizes user instructions. Among AgentVigil defenses, repeat has the lowest attack success, 0.12, and delimit the highest, 0.49. For the baseline, pi_detector is lowest at 0.13. There are no ties. The caption says “four defenses,” while the columns show three named defenses plus no defense. The prose assertion that AgentVigil consistently outperforms the baseline is contradicted by repeat: 0.12 is below 0.21. Sources: pp. 6–8.

## Table 3 — VWA-adv defenses

Physical page 8; selected adversarial prompts, fuzzing task set, GPT-4o.

| Attack | No defense | safety | paraphrase | combined |
|---|---:|---:|---:|---:|
| Baseline | 0.36 | 0.34 | 0.27 | 0.30 |
| AgentVigil | 0.60 | 0.29 | 0.33 | 0.27 |

safety uses delimiters and system prompts; paraphrase transforms untrusted text; combined integrates both. AgentVigil exceeds the baseline without defense and under paraphrase, but is lower under safety and combined. Its combined-defense ASR of 0.27 is below both individual-defense values, 0.29 and 0.33. This directly conflicts with the nearby statement that combined does not further reduce success compared with individual defenses. For the baseline, combined lies between safety and paraphrase. These conditions should not be merged into a blanket claim that combination never helps.

## Table 4 — Extra models and extra baselines

Physical page 12; AgentDojo. Each cell is **fuzzing / test**.

| Attack | o3-mini-2025-01-31 | QwQ-32B |
|---|---:|---:|
| AgentVigil | 0.73 / 0.76 | 0.72 / 0.74 |
| AgentDojo baseline | 0.47 / 0.49 | 0.45 / 0.47 |
| OpenPromptInjection | 0.38 / 0.39 | 0.20 / 0.20 |
| InjecAgent | 0.15 / 0.11 | 0.14 / 0.12 |

AgentVigil is numerically highest in every displayed model/split condition. InjecAgent is lowest in each. QwQ OpenPromptInjection has a fuzzing/test tie at 0.20. **[C]** AgentVigil's gains over the AgentDojo baseline are 26 and 27 percentage points on newer o3-mini, calculated as 0.73 − 0.47 and 0.76 − 0.49; and 27 points on both QwQ splits, calculated as 0.72 − 0.45 and 0.74 − 0.47.

Appendix B.1 prose reports 72%/74% and baseline 50%/53% in a passage following discussion of the newer o3-mini checkpoint. The 72%/74% pair appears in Table 4's QwQ column, while 50%/53% does not appear in either baseline column. The prose's model attribution is ambiguous and its baseline numbers do not match the table. No reconciliation is supplied.

## Table 5 — Scenario breakdown

Physical page 13. Each cell is **fuzzing / test**; scenario counts are not supplied.

| Benchmark | Model | Scenario | AgentVigil | Benchmark baseline |
|---|---|---|---:|---:|
| AgentDojo | o3-mini | Slack | 0.81 / 0.97 | 0.64 / 0.70 |
| AgentDojo | o3-mini | Workspace | 0.63 / 0.60 | 0.20 / 0.22 |
| AgentDojo | o3-mini | Travel | 0.71 / 0.83 | 0.55 / 0.50 |
| AgentDojo | o3-mini | Banking | 0.49 / 0.38 | 0.25 / 0.23 |
| AgentDojo | QwQ-32B | Slack | 1.00 / 0.97 | 0.85 / 0.88 |
| AgentDojo | QwQ-32B | Workspace | 0.33 / 0.42 | 0.05 / 0.10 |
| AgentDojo | QwQ-32B | Travel | 0.80 / 0.80 | 0.60 / 0.65 |
| AgentDojo | QwQ-32B | Banking | 0.60 / 0.65 | 0.23 / 0.23 |
| VWA-adv | GPT-4o | Illusioning | 0.82 / 0.76 | 0.51 / 0.62 |
| VWA-adv | GPT-4o | Goal misdirection | 0.58 / 0.42 | 0.00 / 0.20 |

AgentVigil exceeds the corresponding baseline in all 20 scenario/split comparisons. The largest AgentVigil value is 1.00 for QwQ Slack fuzzing; its smallest is 0.33 for QwQ Workspace fuzzing. The zero baseline for VWA goal-misdirection fuzzing is an actual reported zero, unlike the dashes in Table 1. Fuzzing/test ties occur within QwQ Travel for AgentVigil and QwQ Banking for the baseline. The table does not identify which o3-mini checkpoint underlies its scenario rows, so that attribution remains uncertain.

# 12. Diagram / architecture interpretation

The two substantive diagrams are Figures 1 and 2. Their functions differ: Figure 1 explains an attack path; Figure 2 explains the testing system that searches for attack inputs.

**Figure 1 flow [A/B].** The user's legitimate request leads the agent to search a shopping site and read reviews. A malicious customer review is an input from the environment. The displayed agent reasoning promotes that review's instruction into a step of its task plan. The output is navigation toward an attacker-specified destination. **[D]** The important boundary crossing is therefore from third-party descriptive content into action guidance. The figure does not show a change to the original user request or a compromise of model weights.

**Figure 2 flow [A/B].** The target system consumes external sources through its environment. Separately, the test framework maintains attack candidates. The selector controls which candidate or candidates become mutation inputs; the helper-generated variant becomes a test input; the target's outcome becomes scorer input; the score and stored mutation history affect subsequent selection. This is a feedback loop rather than a one-time prompt generation process.

The environment box names code execution, email, file systems, and web browsing as possible components. **[D]** Their presence in the architecture is not evidence that every named component received a separate quantitative evaluation. The actual reported benchmark coverage centers on assistant suites and text-trigger web tasks. Tool-specific permissions, interface contracts, deployment security controls, and execution-isolation mechanisms are not fully specified.

# 13. Equations and mathematical concepts

No numbered mathematical equation or formal theorem is presented. The essential equations are embedded in page 14's pseudocode.

## E1 — Attack success rate, Algorithm 1 line 19

**[B]** `ASR = total_success / num_questions`.

`total_success` counts successful injection evaluations; `num_questions` counts evaluated units. ASR is a dimensionless proportion. It summarizes how often a seed achieves the attack objective on the evaluated sample. The extracted text misspells the numerator as `total_succcess`; the intended variable is clear from initialization and increment lines. No behavior for a zero denominator is specified.

**[D]** The pseudocode loops over `task_suite`, while comments describe evaluating user/injection task combinations. The exact nesting and counting of multiple combinations within a suite is abbreviated. Therefore the mathematical denominator's operational construction is not fully determined by the pseudocode alone.

## E2 — Coverage-guided score, Algorithm 1 line 20

**[B]** `seed_score = ASR + C × coverage_bonus / num_questions`.

C is identified as the coverage factor. `coverage_bonus` is intended to count newly successful combinations not covered before. The score is a dimensionless ranking quantity, not necessarily a probability, because it adds a weighted bonus to ASR. The value of C is not reported. The accompanying §4.4 explanation establishes the intended novelty reward.

**Pseudocode caveat [B/D].** Lines 12–15 contain a comment about newly successful combinations, but the visible condition is only “if injection successful then.” An explicit “not already covered” predicate is absent. If literally implemented with the same counting units and no additional novelty check, the two success counters would increment together, yielding `seed_score = (1 + C) × ASR`. This is an **analyst-derived conditional observation**, not a claim about the authors' actual implementation. The supplied material does not allow deciding whether the comment abbreviates a real omitted check.

## E3 — Total node visits, Algorithm 3 line 1

**[B]** `total_visits = Σ(node ∈ N) node.visits`.

N is the stored set of seed nodes. Each node has a visit count. The summation adds these counts to form an exploration-scale input. The paper does not fully specify initial visit counts or whether the sum should be interpreted as independent evaluations, because ancestor counts are also incremented.

## E4 — UCB selector, Algorithm 3 line 2

**[B]** `UCB(node) = node.score + C × sqrt(log(total_visits + 1) / (node.visits + ε))`.

`node.score` is empirical seed performance. C is an exploration factor in this algorithm. `node.visits` is the node's visit count. The added one occurs inside the logarithm. ε is visibly present in the denominator, but its numerical value and explicit definition are not supplied. **[D]** Its placement suggests a denominator stabilizer; that is interpretation, not an author-provided definition. The logarithm's base is not specified.

The square-root term gives a larger preference to less-visited nodes for a fixed global visit total. The score term favors effective candidates. Algorithm 3 takes the highest UCB node when n = 1, or sorts and takes the top two when n = 2. No selection branch for other n values is shown.

## Algorithms 1–3 as a whole

**ALG1 [A/B]** initializes counters, evaluates sampled tasks, counts success and intended new coverage, and returns a score. Its “Ensure” line promises a final score and suite results, but the visible return statement returns only `seed_score`.

**ALG2 [A/B]** receives a new node and parent information, increments visits along ancestors, and adds the node to N. It does not show backpropagation of reward values; visit updates are the explicitly displayed operation. Multiple parents are possible, consistent with Crossover, so the history is not necessarily a simple single-parent tree. Duplicate-ancestor handling and initialization are not detailed.

**ALG3 [A/B]** ranks stored nodes by UCB and chooses one or two. These algorithms supply a compact mechanism, but do not constitute a complete reproducible implementation or a proof of optimality.

# 14. Interpretation and discussion

**What the results establish [A/B].** Automated mutation and search can discover successful indirect injections against the evaluated black-box agent settings. The AgentDojo ablations support a contribution from the initial corpus and from the combined scoring/selection mechanism. Transfer results show that some attacks remain effective on held-out task combinations and different backbones. Defense results show both meaningful reductions and residual vulnerabilities.

**What they do not establish [D].** They do not establish universal transfer, universal defense failure, quantified scalability, or a general superiority over every baseline or every agent type. Claude is a clear counterexample to broad transfer superiority in Table 1. The paper's claim of robustness against complex prompts on AgentDojo must be kept separate from Claude's much higher VWA-adv success rates: the same model family can behave differently in different evaluated environments.

**Consistency check [A/B].** Four material discrepancies remain unresolved:

1. **VWA headline versus tables:** §5.2 and Figure 4 report or suggest about 0.70 final coverage, while Tables 1 and 3 give 0.60 for selected-prompt GPT-4o fuzzing/no-defense ASR. A possible aggregation difference is not a documented reconciliation.
2. **AgentDojo defense prose versus Table 2:** §5.1 says AgentVigil consistently outperforms baseline, but repeat gives 0.12 versus baseline 0.21.
3. **Combined-defense prose versus Table 3:** §5.2 says combined does not further reduce attack success, but AgentVigil combined is 0.27, below safety 0.29 and paraphrase 0.33.
4. **Appendix B.1 prose versus Table 4:** prose gives AgentVigil 72%/74% and baseline 50%/53% after discussing newer o3-mini; Table 4 gives newer o3-mini 73%/76% and 47%/49%, and QwQ 72%/74% and 45%/47%.

Further reporting ambiguities include Figure 3's average-coverage aggregation, the precise novelty check in Algorithm 1, Table 2's caption counting, and the checkpoint used in Table 5. These do not erase the numerical table evidence, but they limit confident synthesis across different summaries.

**Research relevance [D: analyst inference, MEDIUM confidence].** Web agents combine an additional input channel—third-party web content—with action-capable planning. A malicious review can therefore affect subsequent navigation during an otherwise legitimate task. The paper's contrast with direct single-turn fuzzing supports a difference in attack setting, not a measured difference in vulnerability rate. Its relevance to “more vulnerable than standalone LLMs” is mechanistic and contextual; the comparative premise remains untested.

# 15. Contributions and novelty

| Contribution category | What the paper supplies | Qualification |
|---|---|---|
| Conceptual [A] | Frames generic black-box indirect-injection testing as an agent fuzzing problem. | Novelty priority is an author claim, not externally verified. |
| Methodological [A] | Combines curated initial seeds, LLM mutations, coverage-guided scoring, and history-aware selection. | Exact corpus and several settings are absent. |
| Algorithmic [A/B] | Scoring, ancestor-visit update, and UCB selection pseudocode. | No theoretical guarantee or complete implementation is given. |
| System [A/B] | Modular target/testing feedback architecture. | “Scalable” is asserted without measured time, cost, or scaling curves. |
| Empirical [A/B] | Two benchmark evaluations, transfer, defenses, ablations, and local shopping demonstration. | Benefits are condition-dependent; some prose and tables disagree. |
| Additional evaluation [A/B] | Open-source-model experiment, newer checkpoint, additional baselines, scenario results. | Appendix prose has unresolved numerical discrepancies. |

No new dataset, independent benchmark, formal theorem, defense architecture, or reported training procedure is established as a contribution in the supplied paper. The evaluated benchmarks and underlying models are existing resources according to the paper.

# 16. Limitations

## Authors' stated limitations and scope restrictions

**[A]** Attackers can influence external content rather than directly control all inputs, and receive only binary attack feedback. The work excludes malicious-user misuse and attacks on hosting infrastructure. The web evaluation focuses on text triggers. Several model/benchmark combinations are unsupported, as Table 1's footnote explains. Sources: pp. 2–4, 7–8.

**[A]** Transfer is weaker to GPT-4o and Claude in some settings. The authors explicitly acknowledge that GPT-optimized attacks do not transfer well to Claude and suggest, after manual inspection, that simpler prompts may affect it more. This explanation is an author interpretation, not a separately controlled experiment. Source: p. 7.

**[A]** AgentVigil's VWA defense performance declines and approaches baseline levels. The authors suggest attack complexity and limited context as possible reasons. Some defenses are omitted for incompatibility, utility, computational cost, or adaptation difficulties. The shopping-site case uses a local copy for ethical reasons. Sources: pp. 6–8.

**[A]** The impact statement says no single testing or defense approach is infallible and continued research and updates are needed. The paper has no dedicated limitations section. Source: p. 9.

## Additional evidence-based analyst observations

**[D]** Important limitations include missing random seeds, repeated-run statistics, confidence intervals, query budgets, measured costs, initial-template inventory, helper generation settings, and exact scoring weights. Separate test scenarios do not necessarily imply fully independent user tasks or attack goals, because the scenario is a combination and the exact split membership is not supplied.

**[D]** The ablation removes scoring and selection together; their separate effects cannot be estimated. Selected-prompt union success should not be treated as single-prompt success. A local shopping-site demonstration cannot establish prevalence across live deployments. Text-trigger success in a multimodal environment is not evidence that visual attacks were optimized or evaluated.

**[D]** The reported inconsistencies reduce confidence in cross-section aggregate numbers, especially the VWA final rate and Appendix B.1 prose. They do not justify silently correcting the paper. The lack of a standalone-LLM control is decisive for the user's comparative research question.

# 17. Threats to validity

The following validity labels are **analyst observations [D]**, not labels explicitly used by the authors.

**Internal validity.** The full method and ablations differ in multiple linked choices. The joint scoring/selection ablation cannot attribute gains to one of those components alone. Random sampling and helper generation introduce variability, but repeated runs are not reported. Whether baseline attack budgets match the selected-prompt search budget is not fully documented.

**Construct validity.** ASR measures achievement of benchmark-defined attacker objectives. It is not automatically equivalent to real financial loss, successful malware execution, or actual compromise of sensitive data in deployed systems. “Average Coverage” and union ASR require clearer aggregation definitions. Benign utility is reported for extra-model selection, but corresponding utility under attacks and defenses is not comprehensively tabulated.

**External validity and generalizability.** Two benchmarks, selected backbones, and one local web case support those settings. They do not cover all coding agents, memory systems, browser permission models, or organizational deployments. Claude's condition-dependent results illustrate limits on generalization across models and environments.

**Statistical conclusion validity.** No uncertainty intervals, statistical tests, run counts, or variance estimates accompany the ASRs. Exact underlying success counts cannot reliably be recovered by multiplying rounded proportions by the reported split sizes. Numerical differences are descriptive evidence, not demonstrated statistical significance.

**Ecological validity.** The shopping site resembles an existing e-commerce platform and involves a multistep task, but the experiment remains a local deployment. Benchmark-controlled injection placeholders may differ from an attacker's real ability to edit live sources.

**Reproducibility.** Checkpoint identifiers, split sizes, iterations, and pseudocode provide useful detail. Missing corpus contents, parameters, complete implementation, split memberships, cost information, and the unresolved pseudocode novelty test prevent a full reconstruction from the supplied document alone.

# 18. Future work and open questions

## A. Explicit author directions

**[A]** The conclusion advocates more robust security measures and development of next-generation security solutions. The impact statement calls for ongoing research and proactive updates as threats evolve. These are broad directions; the paper does not give a detailed future-work schedule or a specific new defense algorithm. Source: p. 9.

## B. Open questions remaining from the evidence

**[D]** A direct answer to the user's comparison would require matched evaluations of a standalone model and an agent using the same backbone, with explicitly controlled input access, goals, and attack budget. That experiment is absent here.

Other unresolved questions are: how much separate benefit comes from scoring versus selection; how robust results are across independent splits and repeated runs; how outcomes change with one seed versus a union of five; how task coverage is averaged; why VWA rates differ between prose and tables; what exact parameters and corpus were used; whether stronger permission boundaries change the consequences of injection; and how attack resistance trades off against benign-task completion under defenses. These are analyst-proposed questions, not experiments already performed.

# 19. Terminology and notation glossary

| Term | Beginner-friendly meaning grounded in this paper |
|---|---|
| LLM | Large language model; the language-processing and planning component. |
| LLM agent | An LLM combined with tools and an environment to complete tasks. |
| Black-box | Internal model and agent design are unavailable; only external behavior is accessible. |
| Red-teaming | Adversarial testing intended to uncover security weaknesses. |
| Indirect prompt injection | Malicious instructions enter through external content encountered during a task. |
| Direct prompt injection | Injection through directly controlled model input; contrasted with the paper's external-content setting. |
| Fuzzing | Repeatedly generating, varying, and testing candidate inputs. |
| Seed | Candidate attack prompt/template used as a starting point for mutation. |
| Corpus | Collection of attack templates or seeds. |
| Mutator | Component generating a changed seed with a helper LLM. |
| Crossover | Mutation combining elements of two parent seeds. |
| Exploration | Searching less-tested candidates or trajectories. |
| Exploitation | Favoring candidates already showing good attack performance. |
| ASR | Attack success rate; successful evaluated attacks divided by evaluated units. |
| Coverage bonus | Reward intended for newly successful task combinations. |
| MCTS | Monte Carlo Tree Search; the paper's history-aware search framework terminology. |
| UCB1 | Upper Confidence Bound 1; the selector's balance of empirical score and exploration bonus. |
| UCT | Alternative named in §4.5; not expanded or formally defined in the supplied paper. |
| AgentDojo | Benchmark/environment framework for assistant-agent injection attacks and defenses. |
| VWA-adv | Adversarial task benchmark based on VisualWebArena; expansion of the abbreviation is not explicitly given. |
| Multimodal | Uses more than one input modality; the web environment includes visual and textual input. |
| Illusioning | Attacker goal that misleads the agent about object attributes or perceived state. |
| Goal misdirection | Attacker goal that changes the action the agent pursues. |
| Task suite | Related user and injection tasks within an AgentDojo environment. |
| Union success | Success if a task is compromised by any selected attack prompt. |
| Utility | In Appendix B.1, success rate on benign tasks. |
| N | Set of stored seed nodes in Algorithms 2–3. |
| n | Number of nodes selected; displayed cases are one or two. |
| C | Coverage factor in Algorithm 1; exploration factor in Algorithm 3; values and equality are unspecified. |
| ε | Denominator symbol in UCB; numerical value and explicit definition are unspecified. |
| node.parents | Parent seed node or nodes recording mutation ancestry. |
| node.visits | Visit count used for exploration preference and ancestor updates. |

# 20. Key numerical results

This compact register supplements the full table transcriptions above. Source text values are **Author-reported**; values explicitly checked in rendered tables are **Visually readable**; calculations are **Analyst-derived**; plot-position readings are **Approximate visual estimate**.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| AgentDojo fuzzing/test split | 142 / 173 | Scenarios | Random division within suites. | Author-reported | p. 6, §5.1 |
| VWA-adv fuzzing/test split | 99 / 100 | Tasks | Text-trigger evaluation. | Author-reported | p. 7, §5.2 |
| AgentDojo iterations / mutations per iteration | 10 / 3 | Iterations / prompts | o3-mini target. | Author-reported | p. 6 |
| VWA iterations / mutations per iteration | 10 / 10 | Iterations / prompts | GPT-4o target. | Author-reported | p. 7 |
| Selected transfer seeds | 5 | Seeds | Highest-scoring candidates, both benchmarks. | Author-reported | pp. 6–7 |
| AgentDojo baseline / initial / final | 38 / 63 / 71 | % ASR | o3-mini fuzzing. | Author-reported | p. 6 |
| AgentDojo final-minus-baseline | 33 | Percentage points | 71 − 38. | Analyst-derived | pp. 6, 8 |
| AgentDojo relative improvement | Approximately 86.8 | % | (71 − 38) / 38 × 100. | Analyst-derived | pp. 6, 8 |
| AgentDojo o3-mini held-out ASR | 0.65 vs 0.34 | Proportion | AgentVigil versus handcrafted. | Visually readable | p. 8, T1 |
| VWA baseline / initial / final headline | 36 / 54 / 70 | % ASR | GPT-4o fuzzing progression. | Author-reported | p. 7 |
| VWA selected-prompt GPT-4o fuzzing | 0.60 vs 0.36 | Proportion | AgentVigil versus baseline; conflicts with headline aggregation. | Visually readable | p. 8, T1–T3 |
| VWA headline relative improvement | Approximately 94.4 | % | (70 − 36) / 36 × 100. | Analyst-derived | p. 7 |
| VWA table relative improvement | Approximately 66.7 | % | (60 − 36) / 36 × 100. | Analyst-derived | p. 8, T1 |
| VWA GPT-4o held-out ASR | 0.59 vs 0.44 | Proportion | Selected prompts, test set. | Visually readable | p. 8, T1 |
| VWA Gemini ASR | 0.67 / 0.67 | Proportion | Fuzzing/test; backbone not used for fuzzing. | Visually readable | p. 8, T1 |
| AgentDojo AgentVigil with defenses | 0.25 / 0.12 / 0.49 | Proportion | pi_detector / repeat / delimit. | Visually readable | p. 8, T2 |
| VWA AgentVigil with defenses | 0.29 / 0.33 / 0.27 | Proportion | safety / paraphrase / combined. | Visually readable | p. 8, T3 |
| Benign utility | 42 / 54 / 74 / 79 | % | Llama3.3-70B / Qwen2.5-72B / QwQ-32B / o3-mini. | Author-reported | p. 12, B.1 |
| Newer o3-mini AgentVigil ASR | 0.73 / 0.76 | Proportion | Fuzzing/test; use table condition. | Visually readable | p. 12, T4 |
| QwQ AgentVigil ASR | 0.72 / 0.74 | Proportion | Fuzzing/test. | Visually readable | p. 12, T4 |
| QwQ Slack maximum | 1.00 | Proportion | Fuzzing scenario. | Visually readable | p. 13, T5 |
| VWA illusioning ASR | 0.82 / 0.76 | Proportion | AgentVigil fuzzing/test. | Visually readable | p. 13, T5 |
| VWA goal-misdirection ASR | 0.58 / 0.42 | Proportion | AgentVigil fuzzing/test. | Visually readable | p. 13, T5 |
| Figure 3 full-method endpoint | About 0.37–0.38 | Average coverage | Step 10; not final union ASR. | Approximate visual estimate | p. 6, F3 |
| Figure 4 endpoint | About 0.695–0.70 | Average coverage | Steps 8–10. | Approximate visual estimate | p. 13, F4 |
| Shopping task length | More than 10 | Operations | Local WebArena shopping example. | Author-reported | p. 8, §5.4 |

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| External content can redirect an agent's task. [A] | Threat description and malicious-review example. | F1, X8 | pp. 1, 3–4, 8–9 | HIGH for stated mechanism; demonstration lacks frequency estimate. |
| AgentVigil implements black-box adaptive prompt fuzzing. [A/B] | Corpus, five mutations, scoring, UCB selection. | F2, ALG1–3 | pp. 4–5, 14 | HIGH for documented design; some parameters absent. |
| AgentDojo o3-mini attacks improve over handcrafted prompts. [A/B] | 0.71 versus 0.38 fuzzing; 0.65 versus 0.34 test. | T1, X1–X2 | pp. 6–8 | HIGH for displayed comparisons; no uncertainty statistics. |
| VWA fuzzing improves during search. [A/B] | Reported 54% initial and 70% final; rising F4. | F4, X4 | pp. 7, 13 | MEDIUM for synthesis because tables show 0.60. |
| Transfer benefits depend on backbone. [B] | GPT/Gemini gains coexist with Claude and some GPT-4o losses. | T1, X2/X5 | p. 8 | HIGH for observed table pattern. |
| Tested defenses leave residual attacks. [B] | Nonzero ASR under all displayed defenses. | T2–T3, X3/X6 | p. 8 | HIGH for these settings; does not cover omitted defenses. |
| Initial corpus and combined search components contribute. [A/B] | Full line exceeds both ablations. | F3, X7 | pp. 6, 8 | MEDIUM for separate component attribution; scoring/selection jointly removed. |
| Additional-model table favors AgentVigil. [B] | Highest ASR across both models and splits. | T4, X9 | p. 12 | HIGH for table; nearby prose inconsistent. |
| Success varies by operational scenario. [B] | Slack, Workspace, Travel, Banking and two web goals differ. | T5, X10 | pp. 12–13 | HIGH for displayed values; scenario counts absent. |
| Web-agent action capabilities increase the consequences available through external-content manipulation. [D] | Review-to-navigation path and tool-using planner description. | F1–F2, X8 | pp. 3–4, 8 | MEDIUM analyst inference; no standalone comparison. |
| The study does not quantify greater vulnerability than standalone LLMs. [D] | Evaluation compares attacks, models, tasks, and defenses within agents. | X1–X10 | pp. 5–8, 12–13 | HIGH for the bounded absence in supplied evaluation inventory. |

# 22. Very simple explanation — Explain Like I'm 15

Imagine asking an assistant to shop for a screen protector and summarize customer reviews. The assistant reads a review that includes an instruction to visit another website first. The review is supposed to be information about the product. The attacker wants the assistant to treat it as an instruction for what to do next. That is the indirect prompt-injection problem studied here.

The researchers built a system that keeps trying different versions of those malicious instructions. It starts with existing templates, asks another language model to shorten, expand, reword, or combine them, and tests the results. It gives extra attention to versions that work well or succeed on tasks that previous versions could not affect.

The attacks succeeded frequently in the tested agent environments, but their effectiveness depended on the model, task, and defense. Some defenses reduced success substantially. Some attacks transferred to new models and tasks; others did worse than simpler baseline attacks. A few reported numbers also disagree between the paper's prose and tables, so they cannot all be treated as one consistent result.

For the question about web agents versus standalone language models, the useful lesson is that an agent can read third-party content and then act on it. That creates an important attack pathway. This paper demonstrates that pathway, but it does not run the comparison needed to prove that web agents are generally more vulnerable than standalone models.

# Completeness Audit

The audit denominator is the inventory of supplied sections, subsections, objectives, experiments, figures, tables, mathematical objects, algorithms, contributions, limitations, and appendices. “Represented” does not mean every sentence was reproduced. The analysis preserves substantive methods and all five result tables while compressing repeated background and conclusions.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, version, affiliations | Yes, text and image | Yes | Fully represented | Section 2; filename/title discrepancy noted. |
| Abstract | Yes, text and image | Yes | Represented in compressed form | Orientation and numerical qualifications. |
| §1 Introduction | Yes, text and images | Yes | Represented in compressed form | Problem, three assessment challenges, positioning. |
| §2 Related Work: agents | Yes | Yes | Represented in compressed form | Agent categories and tool examples. |
| §2 Related Work: attacks | Yes | Yes | Represented in compressed form | Handcrafted/automated distinctions and claimed limitations. |
| §2 Related Work: defenses | Yes | Yes | Represented in compressed form | Categories and evaluation exclusions; literature not externally assessed. |
| §3 black-box setting | Yes | Yes | Fully represented | Section 6. |
| §3 benign-user assumption | Yes | Yes | Fully represented | Section 6. |
| §3 attacker capabilities/goals | Yes | Yes | Fully represented | Binary feedback, external-source control, exclusions. |
| §4.1 Overview | Yes | Yes | Fully represented | Sections 7 and 12. |
| §4.2 Corpus Collection | Yes | Yes | Fully represented | Sources, placeholders, strategy categories, missing details. |
| §4.3 Mutation Design | Yes | Yes | Fully represented | All five operators and random selection. |
| §4.4 Seed Scoring | Yes | Yes | Fully represented | Formula and novelty-check uncertainty. |
| §4.5 Seed Selection | Yes | Yes | Fully represented | UCB, visits, one/two parents, unspecified parameters. |
| §5 evaluation objectives O1–O5 | Yes | Yes | Fully represented | Section 5 and experiment register. |
| Formal research questions/hypotheses | Checked | Yes, absence stated | Fully represented | None explicitly formulated in supplied work. |
| §5.1 setup/fuzzing | Yes | Yes | Fully represented | X1 and configuration table. |
| §5.1 transfer | Yes | Yes | Fully represented | X2, Table 1, conditional benefits. |
| §5.1 defenses | Yes | Yes | Fully represented | X3, Table 2, prose/table conflict. |
| §5.2 setup/fuzzing | Yes | Yes | Fully represented | X4; text triggers; 70%/60% discrepancy. |
| §5.2 transfer | Yes | Yes | Fully represented | X5 and full Table 1. |
| §5.2 defenses | Yes | Yes | Fully represented | X6 and combined-defense discrepancy. |
| §5.3 ablation | Yes | Yes | Fully represented | X7; joint removal limits attribution. |
| §5.4 local case | Yes | Yes | Fully represented | X8; local deployment and no quantified trial frequency. |
| §6 Conclusion | Yes | Yes | Represented in compressed form | Contributions and caveats. |
| Impact Statement | Yes | Yes | Represented in compressed form | Defensive purpose, infallibility caveat, continued research. |
| References pp. 9 and 11 | Yes, text and images | Yes | Inspected but deliberately compressed as secondary | Bibliographic context; no external citation validation. |
| References p. 10 | Yes, text only | Yes | Represented in compressed form | Missing rendering disclosed; no substantive experiment located there. |
| Figure 1 | Yes, visually | Yes | Fully represented with a readability limitation | Fine website-review text not fully transcribed. |
| Figure 2 | Yes, visually | Yes | Fully represented | Architecture and feedback flow. |
| Figure 3 | Yes, visually | Yes | Fully represented | Axes, legend, trends, approximate values, metric ambiguity. |
| Figure 4 | Yes, visually | Yes | Fully represented | Axes, trend, approximate values, plateau. |
| Table 1 | Yes, visually and text | Yes | Fully represented | All numeric cells, dashes, footnote and exceptions. |
| Table 2 | Yes, visually and text | Yes | Fully represented | All cells and caption/prose discrepancies. |
| Table 3 | Yes, visually and text | Yes | Fully represented | All cells and combined-defense discrepancy. |
| Table 4 | Yes, visually and text | Yes | Fully represented | All cells and Appendix B.1 conflict. |
| Table 5 | Yes, visually and text | Yes | Fully represented | All scenario pairs; missing counts/checkpoint noted. |
| E1 ASR | Yes, visually | Yes | Fully represented | Variables and denominator ambiguity. |
| E2 seed score | Yes, visually | Yes | Fully represented | Coverage factor and conditional derivation. |
| E3 total visits | Yes, visually | Yes | Fully represented | Summation and counting uncertainty. |
| E4 UCB | Yes, visually | Yes | Fully represented | Square root, logarithm, undefined epsilon/value settings. |
| Algorithm 1 | Yes, visually and text | Yes | Fully represented | Novelty predicate and return mismatch flagged. |
| Algorithm 2 | Yes, visually and text | Yes | Fully represented | Ancestor visits, node insertion, multiple-parent caveat. |
| Algorithm 3 | Yes, visually and text | Yes | Fully represented | One/two-node selection; unspecified other cases. |
| Appendix A | Yes | Yes | Fully represented | All main checkpoint identifiers. |
| Appendix B.1 | Yes | Yes | Fully represented | Utility numbers, extra models, prose ambiguity. |
| Appendix B.2 | Yes | Yes | Fully represented | Additional baselines and Table 4. |
| Appendix B.3 | Yes | Yes | Fully represented | Scenario descriptions and Table 5. |
| Appendix B.4 | Yes | Yes | Fully represented | Figure 4. |
| Appendix C | Yes | Yes | Fully represented | All three algorithms and essential mathematics. |
| Major contributions | Yes | Yes | Fully represented | Section 15; author novelty distinguished from verification. |
| Author-stated limitations/scope restrictions | Yes | Yes | Fully represented | Section 16, without inventing a dedicated limitations section. |
| Supplied supplementary material | None supplied | Absence represented | Missing from supplied material | No separate supplement was reviewed. |
| Standalone-LLM comparative experiment | Not present | Absence represented | Missing from supplied material | No direct support for comparative vulnerability magnitude. |

## Missing or inaccessible material

The only numbered page lacking a visual rendering is page 10; its extracted reference text is available. No separate supplement, executable implementation, full seed corpus, exact split membership, or benchmark resource contents are supplied. These artifacts were not inspected. The fine text inside Figure 1's website screenshot is not fully readable, although the attack annotations and caption are readable. No numbered main-text section, figure, table, or algorithm is known to be missing from the supplied 14-page paper.

## Uncertain interpretations

Unresolved points are the VWA 70% versus 60% relationship; Figure 3 average coverage versus final ASR; Appendix B.1 prose versus Table 4; the novelty predicate and evaluation counting in Algorithm 1; epsilon, C values, and initial visit settings; exact union aggregation for VWA transfer; and the o3-mini checkpoint in Table 5. The paper's categorical defense prose is contradicted by specific table entries. The proposed explanation of Claude's behavior is not a controlled finding. The broader comparative vulnerability of web agents and standalone LLMs remains unmeasured.

## Deliberately compressed material

Repeated introductory statements, repeated conclusion claims, bibliographic entries, decorative page rules and headers, and the small website-review body text are compressed. Related-work examples are grouped by their role rather than individually reviewed as outside literature. Intermediate plot coordinates are described approximately rather than fabricated as exact numerical data. All substantive table values are retained.

## Potential omissions

No substantive item identified in the supplied section/visual/algorithm inventory is knowingly left unrepresented. This is an inventory-based coverage statement about the supplied material, not a claim to have preserved every word or to have verified absent artifacts. The explicit accessibility and reporting limitations remain part of the analysis.
