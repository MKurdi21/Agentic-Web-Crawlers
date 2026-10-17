## Stage 0 — Document Accessibility Report

The supplied work is **ReAct: Synergizing Reasoning and Acting in Language Models**, published as a conference paper at ICLR 2023. All 33 physical PDF pages are supplied as extracted text. Sixteen pages also have supplied visual renderings: 1–9, 14–15, 22–25, and 31. This analysis uses only those texts and images. No tools, websites, repositories, external papers, or supplementary files were accessed. Document contents were treated as evidence, never as instructions.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: extracted text for physical PDF pages 1–33 |
| Apparently missing pages | None in the supplied numbered sequence; this does not establish that every possible external artifact is present |
| Visually inspected pages | 1–9, 14–15, 22–25, 31 |
| Text-only inspected pages | 10–13, 16–21, 26–30, 32–33 |
| Figures | Figures 1–5 are supplied visually and were inspected |
| Tables | Tables 1–10 are supplied visually; principal result values are readable |
| Equations | The principal formalism on p. 3 is readable in text and image; hat notation is clearer visually |
| Appendices | A–E are present in extracted text; selected appendix pages are also visual |
| Supplementary material | No separate supplementary file supplied |
| Referenced external artifacts | Project page and code links are mentioned; they were not inspected |
| OCR | Not needed for this analysis; extracted figure text on pp. 2, 14, and 15 contains encoding corruption, so the images were used for their visual content |
| Other limitations | Small plotted marks support qualitative trends more confidently than exact numerical readings; omitted search results and abbreviated trajectories cannot be reconstructed |

Confidence terminology: **HIGH** means the supplied evidence directly and clearly supports the statement; **MEDIUM** means the evidence supports a qualified reading; **LOW** means substantial ambiguity remains; **UNKNOWN** means the supplied work does not establish the requested point. Evidence categories are [A] author-reported, [B] directly observable, [C] analyst-derived, and [D] analyst interpretation. No [E] external information is introduced.

### Inventory constructed before synthesis

The document is an empirical machine-learning and agent-method paper, with methodological formalization, controlled prompt ablations, benchmark comparisons, qualitative error analysis, and preliminary fine-tuning. Its authors are Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao; affiliations supplied are Princeton University and Google Research, Brain team. The displayed manuscript is arXiv:2210.03629v3, dated 10 March 2023. No keyword list, numbered theorem, proof, or standalone pseudocode algorithm appears.

The inventory comprises the abstract; §§1–6; §§3.1–3.3; the ALFWorld, WebShop, results, and internal-reasoning analysis blocks in §4; acknowledgments, reproducibility, ethics, and references; Appendix A.1–A.3; B.1–B.2; C.1–C.4; D.1, D.2.1–D.2.3, D.3; and E.1. Visual objects are Figures F1–F5 and Tables T1–T10. Mathematical objects M1–M5 are the observation/action memberships, conditional policy, trajectory context, augmented action space, and thought-based context update on p. 3. Experiments X1–X9 cover knowledge-task prompting, hybrid inference, manual error analysis, model-size/fine-tuning comparisons, ALFWorld prompt robustness, WebShop comparisons, IM-style ablation, GPT-3 comparisons, and human thought editing. The outdated-label case is additional analysis X10. There are four numbered contribution claims on p. 3, but no formally enumerated research questions or hypotheses.

## 1. Plain-Language Orientation

[A, HIGH] This paper asks whether a language model can solve tasks better by **reasoning and acting together**. A language model can write an explanation, but an explanation generated entirely from its existing knowledge may contain invented facts. Conversely, a model that merely selects actions may fail to understand what it has already done, what its observations mean, or what should happen next.

ReAct combines written reasoning with executable task actions. For example, the model can decide what fact it needs, search Wikipedia, read the returned text, revise its plan, and then search again or answer. In a household simulation it can state the subgoal of finding an object, move through locations, recognize that it has found the object, and proceed to cleaning or placement. In WebShop it can inspect product listings and select options matching a shopping instruction.

The researchers chiefly prompt a frozen PaLM-540B model with a few human-written example trajectories. They test four benchmarks: HotpotQA, FEVER, ALFWorld, and WebShop. They also compare smaller fine-tuned models, investigate failure modes, test GPT-3 on two tasks, and illustrate human correction of generated thoughts.

The findings are conditional. ReAct improves over acting alone on both knowledge tasks, but it does not exceed reasoning-only chain-of-thought on every benchmark: it scores 27.4 versus 29.4 exact match on HotpotQA, while scoring 60.9 versus 56.3 accuracy on FEVER. Combining ReAct with self-consistent chain-of-thought produces the strongest prompting results in their main knowledge-task comparison. On ALFWorld the best ReAct prompt trial achieves 71% overall success; on WebShop ReAct achieves 40.0% success.

[D, MEDIUM] For the requested security research question, the central relevance is architectural: an agent reads outside information and uses a language model to choose actions that may affect an environment. This creates possible pathways from environmental text to behavior. **The paper does not establish that web agents are more vulnerable than standalone language models.** Its experiments measure task performance and ordinary errors, not attacks. Its ethics statement explicitly recognizes potential dangers from connecting language models to external action spaces, but its benchmark actions deliberately restrict those dangers.

## 2. Document Roadmap

[A, HIGH] The abstract and §1, pp. 1–3, motivate the union of reasoning and acting and state four contributions. §2, pp. 3–4, defines the agent interaction model and explains dense versus sparse thought generation. §3, pp. 4–6, presents Wikipedia-based knowledge tasks, prompting baselines, hybrid switching, fine-tuning, and error analysis. Figure 3 on p. 7 completes that model-scaling discussion.

§4, pp. 7–8, studies ALFWorld and WebShop, including prompt variability and the Inner Monologue-style ablation. §5, p. 9, positions ReAct against reasoning methods, browser-assisted question answering, dialogue agents, and embodied planning. §6, pp. 9–10, gives conclusions and future directions. Page 10 separately contains reproducibility and ethics statements. References run through p. 13.

Appendix A, pp. 14–15, adds GPT-3 results, an outdated HotpotQA label example, and human thought editing. Appendix B, p. 15, provides fine-tuning and IM-style details. Appendix C, pp. 16–25, supplies prompt examples for all four domains. Appendix D, pp. 25–31, shows generated FEVER, ALFWorld, and WebShop trajectories. Appendix E, pp. 32–33, illustrates the manual success/failure taxonomy. The appendices materially qualify the main claims: they expose residual hallucination, unsuccessful retrieval, repetitive actions, an Act prompt containing a thought, and benchmark restrictions relevant to security interpretation.

## 3. Background and Context

[A, HIGH] A **large language model (LLM)** generates language and, here, textual action commands. **Prompting** supplies examples in the input rather than updating model parameters. **In-context learning** is the use of those examples to guide behavior on a new instance. **Few-shot**, **one-shot**, and **two-shot** describe how many demonstrations are included.

**Chain-of-thought (CoT)** prompting generates intermediate reasoning before an answer. The paper describes its ordinary use as relying on internal model representations, with no external observations to update its knowledge during that reasoning. **Act** is the authors' acting-only baseline: it contains actions and observations but removes thoughts. **ReAct** interleaves reasoning with actions and environment observations. A **trajectory** is the sequence of these steps for one task.

**Self-consistency (SC)** samples multiple CoT trajectories and selects the majority answer. In this paper the main configuration uses 21 samples at decoding temperature 0.7. **Fine-tuning** updates model parameters using training trajectories; it differs from the main frozen-model prompting setup. **Greedy decoding** is the decoding procedure named for most agent comparisons, but the supplied work does not give a general mathematical definition of it.

**Imitation learning (IL)** learns from demonstrated trajectories. **Reinforcement learning (RL)** is named as an additional training paradigm in baselines and future work; no full RL objective is developed here. **Inner Monologue (IM)** is prior work characterized by the authors as using environment-state feedback and remaining subgoals. ReAct-IM is their restricted thought-pattern ablation, not a reproduction of every component of that prior system.

**Multi-hop question answering** requires combining information across two or more passages. **Fact verification** assigns SUPPORTS, REFUTES, or NOT ENOUGH INFO to a claim. **Exact match (EM)** judges an answer against a label; Appendix E shows that this can penalize answers with differing specificity or phrasing. **Success rate (SR)** on WebShop requires all specified requirements to be satisfied, whereas its score measures partial attribute coverage.

[D, HIGH] Task reliability and security are different constructs. Incorrect answers, missed subgoals, and repetitive actions are observed reliability failures. They do not become measured adversarial vulnerabilities merely because the system is an agent.

## 4. Research Problem and Gap

[A, HIGH; pp. 1–3] The existing problem is that reasoning and acting had largely been studied separately. According to the authors, reasoning-only approaches can hallucinate facts, propagate mistakes, and lack the ability to react to newly observed information. Acting-focused approaches can fail to reason about abstract goals, maintain useful working memory, or understand observations sufficiently to choose the next action.

The gap claimed is a lack of systematic study of whether reasoning and acting can be combined for general task solving with benefits over either alone. The motivation is the reciprocal relationship between planning and information gathering: reasoning determines useful actions, and actions obtain evidence that improves reasoning.

The scope is four benchmark environments, mainly using a frozen language model and a small number of demonstrations. This is neither unrestricted web browsing nor a deployed shopping assistant. Wikipedia actions retrieve information and finish tasks; WebShop purchasing is simulated. The authors' comparisons to prior systems describe their positioning, not an independently verified review of all earlier literature.

[D, MEDIUM] For security analysis, the relevant gap remains unfilled by this paper: there is no controlled comparison of agents and standalone LLMs under malicious inputs, matched tasks, matched permissions, or equal adversarial exposure. ReAct can inform a model of the interaction pathways to investigate, but cannot supply a comparative vulnerability estimate.

## 5. Research Questions / Objectives / Hypotheses

[A, HIGH] The paper does not enumerate formal research questions or preregistered hypotheses. Its objectives can be faithfully extracted without inventing such a structure:

1. Introduce a prompt-based method that combines reasoning and actions for general task solving.
2. Evaluate whether it helps across knowledge reasoning and interactive decision-making domains.
3. Use ablations to examine the value of actions in reasoning tasks and thoughts in action tasks.
4. Investigate prompting limitations and preliminary improvements from fine-tuning.
5. Examine whether thought traces assist interpretation, diagnosis, and human correction.

The WebShop subsection asks whether ReAct can interact with noisy real-world language environments for practical applications, p. 7. The authors also test whether benefits extend to another model, Appendix A.1.

[D, MEDIUM] The user's question—why web AI agents might be more vulnerable than standalone LLMs—is an external research objective applied to this paper, not the paper's research question. Relevant analyst questions are where external information enters the agent's context, how that information can influence actions, and what authority those actions possess. These are analytical uses of the reported architecture. Whether a malicious actor can exploit these pathways, and whether agents are comparatively more vulnerable, remain UNKNOWN from this work.

## 6. Assumptions / Threat Model

[A, HIGH; §2, p. 3] The system model assumes an agent receives observations from an environment, retains an interaction context, and chooses actions according to a policy. ReAct adds language thoughts to the action space. A thought changes the context but, in the abstract formulation, does not change the external environment or generate substantive environmental feedback.

The method assumes sufficiently strong language priors to generate useful thoughts and domain-specific actions from demonstrations. It also assumes access to the relevant interfaces: the Wikipedia API, the household text environment, or WebShop. Knowledge tasks provide only the question or claim, without supporting paragraphs. Interactive environments are presented through textual observations and available commands.

There is **no adversarial threat model** specifying an attacker, attacker-controlled pages, capabilities, targets, defense assumptions, attack success, or trust-boundary enforcement. No security experiment assigns malicious control over an observation or tool response.

[A, HIGH; ethics statement, p. 10] The experiments restrict interactions to Wikipedia or WebShop, described as free of private information, and exclude dangerous actions. Models cannot actually purchase products on WebShop or edit Wikipedia. The authors recognize potential risks of retrieving inappropriate/private information or taking harmful actions when action spaces are expanded.

[D, MEDIUM] A security-oriented interpretation can identify user instructions, environmental observations, generated thoughts, and executable actions as distinct functional components. The paper does not show a security mechanism that enforces different trust levels among those components. Absence of a described mechanism is not evidence that an attack was successful or that no implementation safeguard existed outside the supplied account.

## 7. Methodology

### Interaction procedure

[A, HIGH; pp. 3–4] The main procedure uses PaLM-540B without parameter updates. Human demonstrations contain task actions, free-form thoughts, and observations. For knowledge tasks, thoughts and actions alternate densely. For longer decision-making tasks, thoughts appear sparsely at useful points; the model chooses when to generate them.

Thoughts serve several reported functions: decomposing goals, forming plans, using commonsense knowledge, extracting useful observations, recording progress, selecting the next subgoal, handling exceptions, reformulating searches, and synthesizing answers. There is no separate planner whose formal optimality is established and no proof that generated thoughts accurately expose internal computation.

### Knowledge-task data and interface

[A, HIGH; §3.1–3.2, p. 4] HotpotQA requires multi-hop reasoning across Wikipedia passages. FEVER uses three verification labels. Both are evaluated in a question-only or claim-only setup: supporting paragraphs are not initially supplied.

The Wikipedia API has three actions. `search[entity]` returns the first five sentences of an entity page, or top-five similar entities when no matching page is found. `lookup[string]` returns the next sentence in the current page containing that string. `finish[answer]` ends the task. The authors deliberately use a limited interface to simulate human interaction and require explicit reasoning about retrieval. They describe it as weaker than state-of-the-art lexical or neural retrievers.

They randomly select six training cases for HotpotQA and three for FEVER, then manually write ReAct trajectories. Standard, CoT, and Act prompts are derived by removing components. Standard removes thoughts, actions, and observations; CoT removes actions and observations; Act removes thoughts. Appendix C gives the actual exemplars, including search disambiguation, comparisons of dates and professions, and uncertainty about whether a chart position occurred in a particular year.

### Hybrid reasoning and fine-tuning

[A, HIGH; p. 5] CoT-SC samples 21 trajectories at temperature 0.7. ReAct→CoT-SC falls back when ReAct fails to answer within seven steps for HotpotQA or five for FEVER. CoT-SC→ReAct falls back when the most common answer occurs fewer than n/2 times among n samples. These are heuristic switching conditions, not externally calibrated probabilities of correctness.

Fine-tuning uses 3,000 model-generated trajectories with correct final answers for each investigated method to train PaLM-8B and PaLM-62B. The target includes trajectory content conditioned on the input. Appendix B.1 specifies batch size 64. ReAct and Act use 4,000 training steps at both model sizes. Standard and CoT use 2,000 steps at 8B and 1,000 at 62B. The authors report that the latter methods degrade sooner, while action-based methods benefit from more training.

### Interactive-task setup

[A, HIGH; pp. 7–8] ALFWorld contains six task types and can require exploration across more than 50 locations and more than 50 expert steps. Three training trajectories are annotated per task type. Choosing ordered pairs from those three produces six two-example prompts per type. Evaluation uses 134 unseen games in a task-specific setup. Act uses matching trajectories with thoughts removed, according to the methods description. BUTLER baselines are trained on 100,000 expert trajectories per task type. A separate GPT-2 result trained across task types is mentioned but excluded from the comparison because its setup differs.

WebShop contains 1.18 million products and 12,000 human instructions, with structured and unstructured product text. Evaluation uses 500 test instructions. The prompt is one-shot. Actions search, open products, select options, and invoke a simulated buy command. IL is trained on 1,012 human trajectories; IL+RL additionally uses 10,587 training instructions. Score measures average desired-attribute coverage; SR measures full requirement satisfaction.

### Reporting limits

[A/B, HIGH] The supplied paper reports neither hardware nor comprehensive software versions, random seeds, confidence intervals, nor named significance tests for these comparisons. Main knowledge-task evaluation counts are not specified here; Appendix A.1 explicitly specifies a separate 500-question HotpotQA subset. Prompt permutations and sample-based CoT inference are reported, but they should not be treated as a complete statistical uncertainty analysis.

## 8. Experiments / Analyses

| ID | Purpose and setup | Findings and qualifications |
|---|---|---|
| X1: knowledge-task prompting | Compare Standard, CoT, CoT-SC, Act, ReAct with PaLM-540B; HotpotQA EM and FEVER accuracy; T1 | ReAct beats Act on both tasks; CoT exceeds ReAct on HotpotQA. Domain-specific supervised references remain much higher. |
| X2: hybrid inference | Vary CoT-SC sample count and switch using answer frequency or step limits; F2, T1 | Best main HotpotQA result is ReAct→CoT-SC, 35.1; best FEVER result is CoT-SC→ReAct, 64.6. Curves favor hybrids over CoT-SC. No cost-normalized evaluation is reported. |
| X3: manual error analysis | Sample 50 correct and 50 incorrect trajectories from each of ReAct and CoT: 200 total; T2 | ReAct has less labeled hallucination but more reasoning errors. Samples are stratified by final-answer correctness, so percentages are conditional within outcome groups. |
| X4: scaling/fine-tuning | Standard, CoT, Act, ReAct at 8B/62B and prompting at 540B; 3,000 correct trajectories; F3, B.1 | ReAct is weakest in smaller-model prompting but strongest after fine-tuning. Exact bar values are not all labeled. Training steps differ by method. |
| X5: ALFWorld prompt robustness | Six controlled prompt permutations, 134 unseen games, task-specific comparisons; T3 | Best ReAct overall success is 71%, average 57%, reported worst 48%; best Act is 45%. Best-of-prompt figures must be distinguished from averages. |
| X6: WebShop | One-shot prompting; 500 instructions; Act, ReAct, IL, IL+RL, human expert; T4 | ReAct score 66.6 and SR 40.0%; human score 82.1 and SR 59.6%. Benchmark buying is simulated. |
| X7: restricted IM-style thoughts | Same ALFWorld demonstrations, reannotated with dense restricted feedback; T3, B.2, T9 | ReAct best overall 71 versus ReAct-IM 53; ReAct-IM is better on Clean. This ablation changes thought content and density together. |
| X8: model comparison | GPT-3 text-davinci-002 versus PaLM-540B; greedy decoding; 500 HotpotQA validation questions, 134 ALFWorld instances; T5 | GPT-3: 30.8 EM and 78.4% success; PaLM: 29.4 and 70.9%. The HotpotQA subset differs from the main table's condition. |
| X9: human correction | Edit two thoughts in one ALFWorld keychain trajectory; F5 | The edited continuation succeeds. This is a demonstration, not a population-level study of correction success. |
| X10: outdated label | Hotel-room question; F4 | Authors argue retrieved current information conflicts with an outdated label. The illustrated room/suite aggregation remains semantically qualified. |

Appendix D supplements these experiments with individual trajectories rather than independent aggregate trials. FEVER examples include shared success, shared or differing failures, and a case where ReAct correctly rejects the wrong year while Act and CoT support it. The ALFWorld knife example compares success, an invalid cleaning loop, and omission of cleaning. WebShop's example compares scores of 0.125 and 1.0.

## 9. Results

[A/B, HIGH; T1, p. 5] Main PaLM-540B prompting results are:

| Method | HotpotQA EM | FEVER accuracy |
|---|---:|---:|
| Standard | 28.7 | 57.1 |
| CoT | 29.4 | 56.3 |
| CoT-SC | 33.4 | 60.4 |
| Act | 25.7 | 58.9 |
| ReAct | 27.4 | 60.9 |
| CoT-SC→ReAct | 34.2 | 64.6 |
| ReAct→CoT-SC | 35.1 | 62.0 |
| Supervised state of the art | 67.5 | 89.5 |

[C, HIGH] ReAct minus Act is 27.4−25.7 = **1.7 percentage points** on HotpotQA and 60.9−58.9 = **2.0 points** on FEVER. ReAct minus CoT is **−2.0 points** and **+4.6 points**, respectively. The best hybrid exceeds CoT-SC by 35.1−33.4 = **1.7 points** on HotpotQA and 64.6−60.4 = **4.2 points** on FEVER. These are absolute point differences, not relative percentage improvements.

[A/B, HIGH; T2, p. 6] Among manually inspected successful answers, correctly reasoned/factual trajectories are 94% for ReAct and 86% for CoT; false-positive trajectories are 6% and 14%. Among inspected failures, ReAct's categories are 47% reasoning errors, 23% search-result errors, 0% hallucination, and 29% label ambiguity. CoT's are 16%, a dash for search errors, 56%, and 28%. These values describe the labeled samples, not all possible behavior. The ReAct failure percentages sum to 99%; the source gives no explanation, so they are preserved without normalization.

[A/B, HIGH; T3, p. 8] The best ReAct ALFWorld prompt reaches 71% overall success, versus 45% for best Act and 37% for best BUTLER. [C] The latter difference is 71−37 = **34 percentage points**, explaining the headline ALFWorld improvement. ReAct's average across prompt sets is 57%; the authors report the worst trial as 48%. A headline based on the best prompt should not be read as the performance of an arbitrary prompt.

[A/B, HIGH; T4, p. 8] WebShop ReAct has score 66.6 and SR 40.0; Act has 62.3 and 30.1; IL has 59.9 and 29.1; IL+RL has 62.4 and 28.7; humans have 82.1 and 59.6. [C] ReAct−Act is **4.3 score points** and **9.9 SR percentage points**. ReAct−IL is **10.9 SR points**; ReAct−IL+RL is **11.3 SR points**. The paper's approximate headline of 10% absolute improvement is retained as author wording; it is not substituted for these exact differences.

[D, HIGH] No result reports an attack success rate, private-information leakage rate, harmful-action rate, or security comparison with standalone models. The performance gains cannot be translated into vulnerability gains or reductions.

## 10. Figure-by-Figure Interpretation

### Figure 1 — Reasoning, actions, and observations in two domains

[B, HIGH; p. 2] This is a trajectory comparison diagram, not a plot with axes. Its upper part contains four HotpotQA approaches: Standard, CoT, Act-only, and ReAct. Its lower part compares Act-only and ReAct in ALFWorld. Red highlights and crosses indicate problematic steps or failure; green highlights and check marks indicate useful evidence or successful completion; blue highlights mark planning/progress thoughts in the household example.

The question concerns what besides an Apple Remote can control the program for which the remote was originally designed. Standard answers iPod; CoT supplies an incorrect chain; Act retrieves relevant information but finishes with an unsuitable answer. ReAct identifies Front Row, handles an unsuccessful search through disambiguation to Front Row software, extracts the controlling device, and answers keyboard function keys. The evidence supports the role of retrieval-guided reasoning in this example, not a universal success claim.

In ALFWorld, Act repeatedly attempts to take a pepper shaker from a location where observations do not show it. ReAct plans likely locations, searches, recognizes success, and handles a closed drawer before placement. The caption explicitly says in-context examples are omitted from the figure: the visible blocks are generated task trajectories, not the full prompts.

### Figure 2 — Performance versus self-consistency samples

[B, HIGH; p. 5] Two line plots show HotpotQA EM and FEVER accuracy against the number of CoT-SC trials, extending to roughly 21 samples with labeled ticks through 20. Axes are linear. HotpotQA's vertical labels are approximately 26–34; FEVER's are 47.5–65.0. The legend distinguishes blue CoT-SC→ReAct, orange ReAct→CoT-SC, green CoT-SC, red dashed ReAct, and purple dashed CoT. No error bars or confidence bands are shown.

Hybrid curves generally stay above the pure CoT-SC curve. On HotpotQA the orange hybrid has the strongest endpoint; on FEVER the blue hybrid does. CoT-SC improves as sample count increases, whereas ReAct and CoT baselines are horizontal. Exact terminal results are taken from T1 rather than guessed from line positions. [A] The authors state hybrids reach 21-sample CoT-SC performance with only 3–5 samples, p. 6. This concerns CoT sample count, not total tool calls, token cost, or latency.

### Figure 3 — Model size and learning regime

[B, HIGH; p. 7] Grouped bars compare Standard, CoT, Act, and ReAct. Blue, orange, green, and red encode those methods. The left panel is learning by prompt at model sizes 8B, 62B, and 540B; the right is fine-tuning with bars at 8B and 62B. The x-axis is categorical model size; the y-axis is HotpotQA EM, with visible ticks from 0 to 30. There are no error bars and no exact labels on every bar. No 540B fine-tuning result is displayed.

Smaller prompted ReAct models perform poorly relative to other methods, but fine-tuned ReAct is strongest. [A] The prose states fine-tuned 8B ReAct exceeds all 62B prompted methods, and fine-tuned 62B ReAct exceeds all 540B prompting methods in that four-method comparison. The result illustrates a change in ranking with training; it does not show that model scale is irrelevant or that 3,000 examples always suffice.

### Figure 4 — Retrieved knowledge and an outdated benchmark label

[B, HIGH; p. 14] Four trajectory blocks compare the same approaches as F1. The visible HotpotQA label is 2,664. Standard answers 3,000; CoT answers 2,885; Act ends without an answer. ReAct obtains an observation reporting 2,884 rooms and 220 suites and returns 3,104. [C] Its arithmetic is 2,884+220 = 3,104.

[A] The authors call the original label outdated and the ReAct answer up-to-date. [D, MEDIUM] The supplied example cannot independently establish the hotel's historical inventory or whether the question's room count should include suites. The reasoning assumes the two categories should be added. The image supports the authors' demonstration of retrieval and label disagreement, with that semantic qualification.

### Figure 5 — Editing thoughts to alter a continuation

[B, HIGH; p. 15] Two side-by-side ALFWorld trajectories show an original failure and a human-edited success. The task is to place two keychains in a safe. The original thought invents a second keychain in drawer 4, and later actions fail when the drawer contains only a watch. The edited trajectory removes the unsupported sentence at Act 17 and adds likely alternative locations at Act 23. It finds another keychain in a dresser and places it in the safe.

Red highlighting identifies unsupported or failed content; blue marks edits/planning; green marks successful completion. There are no statistical axes. [A] The caption attributes success to two thought edits. [D] This demonstrates sensitivity to authorized context edits. It does not demonstrate unauthorized manipulation, an attack, or the frequency with which editing works.

## 11. Table-by-Table Interpretation

### Table 1 — Main knowledge-task prompting comparison

[A/B, HIGH; p. 5] Rows are prompting methods; columns are HotpotQA EM and FEVER accuracy on percentage scales. Values are reproduced in §9. Best prompting rows differ by task: ReAct→CoT-SC for HotpotQA and CoT-SC→ReAct for FEVER. The supervised reference row is higher than all prompting rows and belongs to different cited approaches, not a matched ReAct training condition.

Footnote a lists previously reported HotpotQA values of 27.1, 28.9, and 33.8 for Standard, CoT, and CoT-SC. These differ from the table's 28.7, 29.4, and 33.4 and are attributed to another paper; the supplied work does not fully explain their evaluation differences. Footnote b identifies supervised references. No uncertainty intervals or significance markers appear.

### Table 2 — Conditional manual trajectory classifications

[A/B, HIGH; p. 6] Success rows distinguish correct reasoning/facts from correct final answers accompanied by hallucinated reasoning/facts. Failure rows distinguish reasoning, retrieval, hallucination, and label ambiguity. The percentages are conditional on success or failure within 50-case strata for each method. A dash for CoT search errors is not an explicitly measured zero. The taxonomy reveals that final-answer correctness and reasoning correctness can diverge. Counts, annotator agreement, and labeling protocol beyond manual classification are not supplied.

### Table 3 — ALFWorld task-specific success

[A/B, HIGH; p. 8] Columns are Pick, Clean, Heat, Cool, Look, Pick 2, and All; units are success percent.

| Method | Pick | Clean | Heat | Cool | Look | Pick 2 | All |
|---|---:|---:|---:|---:|---:|---:|---:|
| Act, best of 6 | 88 | 42 | 74 | 67 | 72 | 41 | 45 |
| ReAct, average | 65 | 39 | 83 | 76 | 55 | 24 | 57 |
| ReAct, best of 6 | 92 | 58 | 96 | 86 | 78 | 41 | 71 |
| ReAct-IM, average | 55 | 59 | 60 | 55 | 23 | 24 | 48 |
| ReAct-IM, best of 6 | 62 | 68 | 87 | 57 | 39 | 33 | 53 |
| BUTLERg, best of 8 | 33 | 26 | 70 | 76 | 17 | 12 | 22 |
| BUTLER, best of 8 | 46 | 39 | 74 | 100 | 22 | 24 | 37 |

ReAct best-of-six wins the overall column and Pick, Heat, and Look. BUTLER's 100 is highest for Cool. ReAct-IM's 68 is highest for Clean. Act and ReAct best-of-six tie at 41 for Pick 2. Thus aggregate superiority does not mean winning every task. The six task columns should not be averaged unweighted to reconstruct All; task counts and exact aggregation are not supplied. BUTLER uses beam search; other rows use greedy decoding. Baseline values come from a prior paper. No intervals are shown.

### Table 4 — WebShop aggregate performance

[A/B, HIGH; p. 8] Rows compare Act, ReAct, IL, IL+RL, and Human Expert; columns are score and SR. Values and derived differences appear in §9. ReAct leads the automated methods on both columns; the human row is higher on both. IL+RL slightly exceeds Act in score, 62.4 versus 62.3, but has lower SR, 28.7 versus 30.1. The metric distinction matters because partial matching and complete requirement satisfaction can rank systems differently. Baseline rows are imported from the cited WebShop paper. No uncertainty or significance test is displayed.

### Table 5 — Cross-model appendix results

[A/B, HIGH; p. 14] ReAct with PaLM-540B and GPT-3 text-davinci-002 is compared under greedy decoding. HotpotQA values are 29.4 and 30.8 EM on 500 randomly sampled validation questions. ALFWorld values are 70.9% and 78.4% on all 134 unseen validation instances, using the prompt set selected as best according to PaLM. [C] Differences are 1.4 EM points and 7.5 success points. The authors' explanation involving instruction following is explicitly a possibility, not a controlled causal finding.

### Table 6 — WebShop demonstration prompt

[B, HIGH; p. 22] Columns show Act and ReAct for a 3-ounce bright citrus deodorant for sensitive skin below $50. Both select a $10.99 product and relevant scent/size options. ReAct adds two thoughts about candidate choice and option matching. There is no aggregate metric. [D, HIGH] One ReAct thought describes both listed Earth Mama candidates as bright citrus even though the second listing says Ginger Fresh. The prompt therefore contains an imprecise intermediate claim; its successful selected product does not make every thought correct.

### Table 7 — Nominal Act household prompt

[B, HIGH; p. 23] The caption says no thoughts are provided, and §4 describes Act prompts as removing thoughts. However, the displayed trajectory includes a `think:` line after cleaning the lettuce. This is a caption–visual and methods–appendix inconsistency. It is visible in the image and extracted text. The supplied paper does not establish whether the table contains a presentation mistake or whether that thought was present in the actual evaluated Act prompt. This prevents an unconditional claim that every displayed Act exemplar is thought-free.

### Table 8 — ReAct household prompt

[B, HIGH; p. 24] The same lettuce task is supplemented with goal decomposition, likely-location reasoning, recognition of finding/taking the lettuce, cleaning, and placement tracking. There is no result statistic. It illustrates how sparse thoughts link actions across subgoals rather than adding a thought after every observation.

### Table 9 — Restricted IM-style prompt

[B, HIGH; p. 25] The same task uses repeated dense reminders of the current subgoal. It contains initial decomposition, but omits detailed likely-location reasoning and explicit progress-transition thoughts present in T8. The example itself completes the lettuce task. Aggregate performance differences come from T3; they cannot be inferred from this successful demonstration alone.

### Table 10 — Generated WebShop trajectories

[B, HIGH; p. 31] Both methods receive a request for a sixteen-pack of apple cinnamon freeze-dried banana chips below $50. Act selects a strawberry-banana 100-pack at $85 and buys without matching required options; its score is 0.125. ReAct inspects a different candidate and selects apple cinnamon and a pack of 16; its score is 1.0. The selected listing displays $12.99 before option selection; the abbreviated sequence does not show a fresh price after changing pack size. The benchmark reports full score, but the visible trace alone does not independently establish every pricing detail or resolve the request's flavor/product wording.

## 12. Diagram / Architecture Interpretation

[A/B, HIGH] F1, F4, and F5 are trajectory diagrams; no separate component architecture schematic is provided. Their functional structure is: task instruction and examples → language-model context → generated thought or action → environment execution for an action → returned observation → updated context → subsequent generation. A finishing action ends a knowledge task; simulated buying ends shopping.

The loop permits information gathering and plan revision. Thoughts summarize evidence and subgoal state. Actions connect generated language to an external interface. Observations include search failures, entity suggestions, object inventories, product titles, prices, and selectable options. F1 shows search failure triggering disambiguation; F5 shows context edits altering future actions.

[D, MEDIUM] The security-relevant pathway is environmental content → context → generated interpretation → action selection. A hypothetical malicious observation could be studied along this pathway, but that hypothesis is not tested here. Authorized human thought editing supplies evidence that changes in context can affect behavior, without establishing that an attacker can access that editing channel. Action consequences depend on interface permissions: this paper's simulated buy and read-only Wikipedia access intentionally limit impact.

## 13. Equations and Mathematical Concepts

[A, HIGH; §2, p. 3] The paper gives an unnumbered interaction formalism rather than a theorem or optimization derivation.

**M1: observation and action membership.** At time t, `o_t ∈ O` and `a_t ∈ A`. Here t indexes interaction time, o_t is an observation, O is the observation space, a_t is an action, and A is the original action space. Membership means each item belongs to the corresponding set. No complete enumeration of O is supplied.

**M2: policy.** `π(a_t | c_t)` represents the policy for selecting an action conditional on context c_t. π is a conditional policy, not a loss function. The input is context; the represented output is action choice or its conditional distribution. The paper does not derive a training objective for this expression.

**M3: context.** `c_t = (o_1, a_1, …, o_(t−1), a_(t−1), o_t)`. The parentheses describe the ordered interaction history through the latest observation. Context supplies information needed to infer the next action. The written pre-ReAct expression does not list thoughts; the augmentation explains how thoughts are subsequently added.

**M4: augmented action space.** `Â = A ∪ L`, where L is the language space. The union operator adds language thoughts to environment actions. A thought `â_t ∈ L` does not alter the outside environment in the abstract description. It is useful because it can compute or organize information from the current context. No formal restriction on possible language strings is supplied; the authors call the language space unlimited.

**M5: context update by a thought.** `c_(t+1) = (c_t, â_t)`. The new context appends the generated thought. This is a sequence update, not an equation guaranteeing the thought's truth. It links planning and memory to future choices.

The authors characterize learning the mapping `c_t → a_t` as difficult when the required reasoning is highly implicit. Strong language priors and demonstrations are used instead of solving a formally specified optimization problem. Example arithmetic such as comparing 1844 with 1989 in Appendix C is task reasoning, not a new mathematical contribution. The hybrid condition of fewer than n/2 matching answers is a decision threshold; equality at n/2 is not included in the stated fallback rule.

[B/D, HIGH] A representational detail requires qualification: §2 says thoughts have no observation feedback, but ALFWorld and WebShop transcripts show `OK.` after `think` actions. These acknowledgments do not demonstrate a substantive environmental state change. The abstract mathematical statement and implementation-style transcript differ in whether an acknowledgment is printed; the supplied work does not formally reconcile their timestep conventions.

## 14. Interpretation and Discussion

[A, HIGH] The authors' central interpretation is reciprocal assistance: reasoning guides actions and actions ground reasoning. Their ablations support this in the tested configurations, particularly when ReAct exceeds Act and restricted feedback thoughts. The results also expose a trade-off. External retrieval improves factual grounding, but the thought–action structure can constrain flexible reasoning and create search-dependent failures.

The error taxonomy supports a narrow claim about selected trajectories: ReAct has fewer hallucination-classified failures in that sample, while reasoning errors and search-result failures remain substantial. Appendix E shows ReAct can still produce a hallucinated rationale accompanying a correct answer. Therefore the reported 0% hallucination among sampled failures cannot be generalized to zero hallucination across ReAct outputs.

The hybrid results suggest that internal model knowledge and retrieved information complement each other. Fine-tuning results suggest smaller models can learn the combined format better than they infer it from a few examples. However, neither result isolates all possible causal variables: switching adds procedures, and fine-tuning schedules differ across methods.

### Cross-reference and consistency findings

1. T7 contains a thought despite its caption and the Act-removal description. This is unresolved.
2. T5's PaLM HotpotQA value is 29.4, while T1's ReAct value is 27.4. T5 explicitly uses a 500-question subset; these conditions must remain separate.
3. T5 gives ALFWorld 70.9, while T3 rounds the headline to 71. The values are compatible with rounding, although raw episode counts are not supplied.
4. The approximately 10% WebShop headline differs from exact table-derived gaps, which depend on the chosen baseline.
5. The p. 4 statement about consistently outperforming reasoning-only or acting-only baselines is broader than T1's HotpotQA comparison to CoT. T1 takes precedence for that specific condition: ReAct is lower there.
6. F5 is in Appendix A.3, although p. 4 points to Figure 5 in Section 4. The figure itself remains accessible.
7. T2's ReAct failure categories total 99%; no correction is invented.
8. Appendix D says search results are omitted, and E says nonrepresentative steps are omitted. Missing intermediate evidence cannot be recreated from resulting thoughts.

[D, MEDIUM] For the requested research, the paper offers both potential risk pathways and mitigating evidence about ordinary reliability. Reading outside text broadens input exposure; selecting actions can broaden consequences; accumulating observations and generated thoughts can preserve errors across a trajectory. Conversely, retrieval reduces some factual errors and thoughts make certain failures visible. The work supports studying these mechanisms, not assigning a net security effect or claiming agents are demonstrably more vulnerable.

## 15. Contributions and Novelty

[A, HIGH; p. 3] **Conceptual/methodological:** a unified prompt format for reasoning and actions, with dense alternation for knowledge tasks and sparse thought insertion for longer interactive tasks.

**Experimental/empirical:** evaluation across four domains, component-removal comparisons, hybrid inference, prompt permutations, model-size comparisons, and additional GPT-3 results.

**Analytical:** a success/failure taxonomy separating final-answer correctness from reasoning/factual correctness, along with illustrative trajectories showing search failures, repetitions, and ambiguous labels.

**Training-related:** preliminary bootstrapped fine-tuning with 3,000 correct-answer trajectories, demonstrating changed rankings at smaller model sizes.

**Human-interaction:** a thought-editing example showing that human correction of a generated context can change subsequent task behavior.

No new dataset or benchmark is introduced, no security defense is evaluated, and no theoretical guarantee is proved. Claims of being first or novel are the authors' positioning within the supplied related-work discussion, not an externally verified priority determination.

## 16. Limitations

### Authors' stated limitations

[A, HIGH; pp. 3, 6, 8–10] Prompting supplies limited reasoning and acting behaviors. Smaller models have difficulty learning both from demonstrations alone. Interleaving can reduce reasoning flexibility; repetitive thought/action loops occur. Noninformative retrieval can derail reasoning. The deliberately weak Wikipedia API retrieves only a small part of a passage and requires exact entity navigation.

All prompting approaches remain far below domain-specific state-of-the-art knowledge-task references. Complex tasks with large action spaces may need more demonstrations than the input length permits. WebShop methods remain below expert humans, with exploration and query reformulation still challenging. Some dataset labels can be outdated. PaLM was not openly accessible according to the reproducibility statement. The authors acknowledge risks of broader action spaces and restrict their experiments accordingly.

### Additional evidence-based analyst observations

[D, HIGH/MEDIUM] No measured adversarial evaluation supports a vulnerability comparison. No confidence intervals or significance tests accompany the result tables. Some best-of-prompt comparisons differ in the number of candidate prompts. Fine-tuning steps differ by method. Manual error analysis has no supplied annotator agreement statistics. Abbreviated observations limit verification of some reasoning examples. T7 complicates the claim of entirely thought-free Act exemplars. Human correction is illustrated on a single trajectory rather than evaluated systematically. Prompt reasoning can itself be imprecise, as T6 demonstrates.

These are analyst observations about what the evidence establishes. They are not additional admissions attributed to the authors, and they do not imply that unreported implementation details necessarily did not exist.

## 17. Threats to Validity

[D, MEDIUM] **Internal validity:** matched trajectories for ReAct/Act are a useful control, but the T7 inconsistency leaves uncertainty about the displayed Act prompt. IM-style ablation changes both thought content and density; attributing the entire difference to one factor would exceed the design. Fine-tuning schedules differ.

**External validity:** four domains provide breadth, but WebShop is a restricted benchmark and ALFWorld a synthetic text game. Results do not establish performance across unrestricted browsers, authentication flows, arbitrary websites, or physical actuators. GPT-3 comparisons cover only two tasks and one specified model variant.

**Construct validity:** EM measures label matching, not fully verified reasoning. The authors' manual taxonomy and outdated-label example expose that limitation. WebShop score and SR measure task compliance, not privacy or resistance to attacks. Human-readable thoughts are an interpretability artifact; the work does not prove they faithfully describe every internal computation.

**Statistical conclusion validity:** uncertainty intervals, significance procedures, and complete random-seed reporting are absent from the supplied account. Terms such as significantly better should therefore be read as author descriptions without a supplied inferential test. Stratified error-analysis samples do not estimate unconditional failure prevalence.

**Ecological validity:** benchmark text contains realistic product language but excludes actual purchasing and private information. This protects the study while limiting inference about consequential deployment.

**Reproducibility:** full prompt examples, training-step details, and code links improve traceability. Restricted PaLM access, missing hardware/version details, and the uninspected external code constrain independent reproduction from this document alone.

**Security generalizability:** no adversary, malicious observation set, or matched standalone comparator is evaluated. Comparative vulnerability, exploitability, and real-world harm remain UNKNOWN.

## 18. Future Work and Open Questions

### A. Authors' proposed directions

[A, HIGH; pp. 3, 6, 9–10, 15] Scale ReAct through more tasks and multi-task training. Use more high-quality human annotations for fine-tuning. Combine it with reinforcement learning and potentially human feedback. Investigate better decoding, such as beam search, for repetitive loops. Study human thought editing more systematically. Broader external-environment experiments should recognize the potential dangers noted in the ethics statement.

### B. Additional open questions from the evidence

[D, MEDIUM] How robust are aggregate gains to random prompt selection rather than best-prompt selection? How does matching tool-call, token, and latency budgets change hybrid comparisons? What fraction of failures can thought editing correct? How often do correct final answers mask incorrect reasoning? What safeguards preserve the usefulness of retrieved information while preventing environmental content from acquiring instruction-like authority?

For the user's security project, a future study would need a defined adversary, controlled observation modifications, explicit action permissions, and a matched comparison with standalone models. That is a proposed research requirement, not a method performed in this paper. The paper leaves open whether agentic feedback amplifies malicious influence, whether thought traces improve detection, and how action restrictions change possible harm.

## 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| LLM | Large language model used to generate reasoning and textual actions |
| ReAct | Method combining reasoning traces with environment actions |
| CoT | Chain-of-thought: intermediate written reasoning before answering |
| CoT-SC | CoT with self-consistency: sample several trajectories and choose the majority answer |
| Act | Acting-only baseline described as omitting thoughts |
| Thought/reasoning trace | Generated language used to organize evidence, plans, and progress |
| Observation | Text returned from an environment or action interface |
| Trajectory | Ordered sequence of thoughts, actions, and observations |
| Frozen model | Model whose parameters are not updated in the prompting experiment |
| Fine-tuning | Updating parameters using example trajectories |
| Few-shot | Prompt containing a small number of demonstrations |
| API | Application programming interface; here, the Wikipedia action interface |
| HotpotQA | Multi-hop question-answering benchmark involving Wikipedia passages |
| FEVER | Fact-verification benchmark with three labels; its full name is not expanded in the supplied prose |
| ALFWorld | Synthetic household text environment; no acronym expansion is supplied |
| ALFRED | Embodied benchmark with which ALFWorld is designed to align; full expansion is not supplied |
| WebShop | Simulated online-shopping environment using real product text |
| EM | Exact match of a predicted answer with a reference label |
| Acc | Accuracy of the fact-verification label |
| SR | Success rate: fraction satisfying all shopping requirements |
| IL | Imitation learning from demonstrated behavior |
| RL | Reinforcement learning, used by comparison systems and proposed future combinations |
| IM | Inner Monologue, prior environment-feedback-based work |
| ReAct-IM | Restricted dense-feedback thought-pattern ablation |
| Hallucination | Reasoning or factual content classified by the authors as invented or unsupported |
| Label ambiguity | A prediction judged right in meaning but failing to match the dataset label precisely |
| O, o_t | Observation space and observation at time t |
| A, a_t | Original action space and action at time t |
| L | Space of language thoughts |
| Â, â_t | Augmented action space and an action in that augmented formulation |
| c_t | Accumulated interaction context |
| π(a_t\|c_t) | Conditional policy for choosing an action from the context |
| ∪ | Set union, combining actions with language thoughts |
| n | Number of sampled CoT trajectories in the hybrid switching rule |
| B in model sizes | Billions of parameters in the named 8B, 62B, and 540B model configurations |

## 20. Key Numerical Results

All source locators below use physical PDF pages. Table values are author-reported and visually readable; derived rows identify their operands explicitly.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Main model | 540B | parameters | Frozen PaLM prompting | Author-reported | p. 3, §2 |
| Demonstrations | 6 / 3 | cases | HotpotQA / FEVER | Author-reported | p. 4, §3.2 |
| Search response | 5 / 5 | sentences / suggestions | Wikipedia entity search | Author-reported | p. 4, §3.1 |
| CoT-SC samples | 21 | trajectories | Main self-consistency configuration | Author-reported | p. 5, §3.2 |
| CoT-SC temperature | 0.7 | decoding parameter | Sampled CoT inference | Author-reported | p. 5 |
| ReAct fallback limits | 7 / 5 | steps | HotpotQA / FEVER | Author-reported | p. 5 |
| Correct trajectories at those limits | 0.84 / 1.33 | percent | Conditional on correct final answers; HotpotQA / FEVER | Author-reported | p. 5, footnote 3 |
| ReAct | 27.4 / 60.9 | EM / accuracy percent | Main HotpotQA / FEVER | Visually readable | p. 5, T1 |
| Act | 25.7 / 58.9 | EM / accuracy percent | Same main comparison | Visually readable | p. 5, T1 |
| CoT | 29.4 / 56.3 | EM / accuracy percent | Same main comparison | Visually readable | p. 5, T1 |
| Best hybrid | 35.1 / 64.6 | EM / accuracy percent | Different hybrid direction for each task | Visually readable | p. 5, T1 |
| ReAct−Act | 1.7 / 2.0 | percentage points | 27.4−25.7 / 60.9−58.9 | Analyst-derived | p. 5, T1 |
| Error-analysis sample | 200 | trajectories | 50 per method per success/failure stratum | Author-reported | p. 6 |
| Successful-answer false positives | 6 / 14 | percent | ReAct / CoT, conditional manual sample | Visually readable | p. 6, T2 |
| Failure hallucinations | 0 / 56 | percent | ReAct / CoT, conditional manual sample | Visually readable | p. 6, T2 |
| Fine-tuning examples | 3,000 | trajectories | Correct final answers; smaller PaLM models | Author-reported | pp. 5–6 |
| Fine-tuning batch size | 64 | examples per batch | All reported fine-tuning | Author-reported | p. 15, B.1 |
| ReAct/Act training | 4,000 | steps | Both 8B and 62B | Author-reported | p. 15, B.1 |
| Standard/CoT training | 2,000 / 1,000 | steps | 8B / 62B | Author-reported | p. 15, B.1 |
| ALFWorld evaluation | 134 | unseen games | Task-specific evaluation | Author-reported | p. 7 |
| ALFWorld prompt sets | 6 | ordered pairs | From 3 annotated trajectories per task type | Author-reported | p. 7 |
| Best ReAct ALFWorld | 71 | success percent | Best of six prompts | Visually readable | p. 8, T3 |
| Average ReAct ALFWorld | 57 | success percent | Average prompt performance | Visually readable | p. 8, T3 |
| Worst ReAct ALFWorld | 48 | success percent | Reported worst trial | Author-reported | p. 8 |
| ReAct−BUTLER | 34 | percentage points | 71−37, best reported overall rows | Analyst-derived | p. 8, T3 |
| WebShop inventory | 1.18M / 12k | products / instructions | Benchmark description | Author-reported | p. 7 |
| WebShop evaluation | 500 | test instructions | Aggregate score and SR | Author-reported | p. 7 |
| IL data | 1,012 | human trajectories | WebShop baseline | Author-reported | p. 8 |
| Additional IL+RL data | 10,587 | instructions | WebShop baseline | Author-reported | p. 8 |
| ReAct WebShop | 66.6 / 40.0 | score / SR percent | One-shot prompting | Visually readable | p. 8, T4 |
| Human WebShop | 82.1 / 59.6 | score / SR percent | Human expert reference | Visually readable | p. 8, T4 |
| ReAct−Act WebShop SR | 9.9 | percentage points | 40.0−30.1 | Analyst-derived | p. 8, T4 |
| GPT-3 / PaLM HotpotQA | 30.8 / 29.4 | EM percent | Separate 500-question subset | Visually readable | p. 14, T5 |
| GPT-3 / PaLM ALFWorld | 78.4 / 70.9 | success percent | 134 cases, PaLM-selected prompt | Visually readable | p. 14, T5 |
| Human thought edits | 2 | edited thoughts | One keychain example | Author-reported | pp. 14–15, F5 |
| WebShop example scores | 0.125 / 1.0 | episode score | Act / ReAct individual trajectory | Visually readable | p. 31, T10 |

## 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| ReAct integrates thoughts and actions | Formal augmented action space and trajectories | M4–M5, F1 | pp. 2–4 | HIGH for reported method; no optimality guarantee |
| Thoughts improve acting in knowledge tasks | ReAct exceeds Act on both metrics | T1, X1 | pp. 5–6 | HIGH for these conditions; modest point differences |
| ReAct does not uniformly beat CoT | HotpotQA 27.4 versus 29.4 | T1 | pp. 5–6 | HIGH; prevents an unqualified superiority claim |
| Retrieval improves sampled factual grounding | Lower false-positive and hallucination classifications | T2, X3 | p. 6 | HIGH for sample; not universal factuality |
| Retrieval creates a failure dependency | 23% of sampled ReAct failures are search-result errors | T2, E.1 | pp. 6, 33 | HIGH conditional finding |
| Hybrid methods perform best in main prompting comparison | 35.1 HotpotQA and 64.6 FEVER | T1, F2, X2 | pp. 5–6 | HIGH; hybrid direction differs by task |
| Fine-tuning helps smaller ReAct models | Rank reversal between prompting and fine-tuning | F3, B.1 | pp. 6–7, 15 | HIGH qualitative ranking; exact bar values not all labeled |
| Sparse reasoning benefits interactive tasks | ALFWorld and WebShop aggregate comparisons | T3–T4, X5–X7 | pp. 7–8 | HIGH for reported setups; not every task column |
| Thoughts can be corrected by humans | Two edits change a failed continuation into success | F5, X9 | pp. 14–15 | HIGH example evidence; no estimated general correction rate |
| Connecting action spaces introduces potential danger | Ethics statement names information and harmful-action risks | Ethics | p. 10 | HIGH author warning; no attack experiment |
| Agent architecture is relevant to external-input influence | Observations enter context used to choose future actions | M2–M5, F1 | pp. 2–3 | MEDIUM analyst inference; exploitability untested |
| Comparative security remains unresolved | Evaluated outcomes concern task accuracy/success and ordinary errors | X1–X10 | pp. 3–10, 14–15 | HIGH scope observation; vulnerability level UNKNOWN |

## 22. Very Simple Explanation

A language model can write an answer from what it already knows. But sometimes it needs to look something up, and sometimes it needs to do several things in the right order. ReAct lets it write a short plan, take an action, read what happened, and decide what to do next. The paper tests this on answering questions, checking claims, moving objects in a simulated house, and selecting products in a simulated shop.

This often helps. The model can notice that a search failed, try a more precise name, or remember that an object has been picked up but still needs cleaning. It still makes mistakes. A good-looking explanation can contain a false claim, searching can return unhelpful information, and an agent can get stuck repeating actions. The paper finds that combining retrieval-based ReAct with reasoning from the model's own knowledge can work better than either by itself.

For security, the useful lesson is about the connection between reading and doing. An agent may read text from an environment and then use that text when choosing actions. If those actions had real permissions, mistakes could have more consequences. That is an analyst interpretation of the architecture, not a measured attack result. This study deliberately prevents real purchases and Wikipedia edits, and it does not test whether malicious web content can control the agent.

So this paper helps explain what an agent's information-and-action loop looks like. It does not prove that web agents are more vulnerable than standalone language models, or measure how much more vulnerable they might be. Answering that security question requires an additional adversarial study.

## Completeness Audit

The audit denominator is the supplied 33-page work, including its appendices, five figures, ten tables, principal formalism, distinct analyses, contributions, and limitations. Visually inspected means an image was supplied and examined; text-only means the extracted text was examined without a page rendering.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, abstract | Yes, visual/text | Yes | Fully represented | Metadata and main framing covered |
| §1 Introduction | Yes, visual/text | Yes | Represented in compressed form | Human inner-speech analogy compressed |
| §2 ReAct formalism/features | Yes, visual/text | Yes | Fully represented | Dense/sparse thoughts and M1–M5 explained |
| §3 Knowledge-intensive tasks | Yes, visual/text | Yes | Fully represented | Domain, interface, and result distinctions preserved |
| §3.1 Setup | Yes, visual/text | Yes | Fully represented | Question-only condition and API limits included |
| §3.2 ReAct prompting | Yes, visual/text | Yes | Fully represented | Demonstration counts and purposes included |
| §3.2 Baselines | Yes, visual/text | Yes | Fully represented | Component removal and SC configuration included |
| §3.2 Hybrid methods | Yes, visual/text | Yes | Fully represented | Both switching rules and step limits included |
| §3.2 Fine-tuning | Yes, visual/text | Yes | Fully represented | Bootstrap data and model sizes included |
| §3.3 Results/error analysis | Yes, visual/text | Yes | Fully represented | Conditional samples and trade-offs included |
| §4 ALFWorld | Yes, visual/text | Yes | Fully represented | Data, prompts, baselines, best/average distinguished |
| §4 WebShop | Yes, visual/text | Yes | Fully represented | Dataset, metrics, simulated actions included |
| §4 Internal reasoning vs feedback | Yes, visual/text | Yes | Fully represented | Restricted ablation and task exception included |
| §5 Related work | Yes, visual/text | Yes | Represented in compressed form | Categories preserved; individual citation detail compressed |
| §6 Conclusion | Yes, visual/text then text-only | Yes | Fully represented | Context-length and training directions preserved |
| Acknowledgments | Yes, text-only | Yes | Inspected but deliberately omitted as non-substantive | Funding/thanks do not establish method or security effects |
| Reproducibility statement | Yes, text-only | Yes | Fully represented | Restricted PaLM access and uninspected links disclosed |
| Ethics statement | Yes, text-only | Yes | Fully represented | Potential dangers and action restrictions preserved |
| References, pp. 10–13 | Yes, text-only | Yes | Represented in compressed form | Used only for author positioning; not externally checked |
| Explicit RQs/hypotheses | Checked | Yes | Fully represented | No formal enumeration; extracted objectives distinguished |
| X1 Knowledge prompting | Yes | Yes | Fully represented | Exact T1 values included |
| X2 Hybrid inference | Yes | Yes | Fully represented | Curve trends and exact endpoint conditions included |
| X3 Manual classification | Yes | Yes | Fully represented | Sample strata and percentages included |
| X4 Scaling/fine-tuning | Yes | Yes | Represented in compressed form | Rankings preserved; unlabeled bars not digitized |
| X5 ALFWorld robustness | Yes | Yes | Fully represented | Six prompt sets, 134 cases, best/mean/worst covered |
| X6 WebShop comparison | Yes | Yes | Fully represented | All aggregate rows included |
| X7 IM-style ablation | Yes | Yes | Fully represented | Restricted thoughts and Clean exception included |
| X8 GPT-3 comparison | Yes | Yes | Fully represented | Separate subset/prompt selection preserved |
| X9 Human correction | Yes | Yes | Fully represented | Single-case scope retained |
| X10 Outdated label | Yes | Yes | Fully represented | Room/suite qualification included |
| F1, both domain panels | Yes, visual | Yes | Fully represented | Four QA and two household conditions explained |
| F2, both plots | Yes, visual | Yes | Fully represented | Axes, legend, trends, lack of uncertainty covered |
| F3, both learning panels | Yes, visual | Yes | Represented in compressed form | Exact unlabeled values uncertain |
| F4, four trajectories | Yes, visual | Yes | Fully represented | Displayed answers, retrieval, arithmetic included |
| F5, two trajectories | Yes, visual | Yes | Fully represented | Edits and continuation explained |
| T1 | Yes, visual/text | Yes | Fully represented | All rows and relevant footnotes represented |
| T2 | Yes, visual/text | Yes | Fully represented | All categories, dash, and sum issue included |
| T3 | Yes, visual/text | Yes | Fully represented | All cells reproduced |
| T4 | Yes, visual/text | Yes | Fully represented | All rows reproduced in results |
| T5 | Yes, visual/text | Yes | Fully represented | All cells and caption conditions included |
| T6 | Yes, visual/text | Yes | Represented in compressed form | Prompt flow and imprecise candidate thought preserved |
| T7 | Yes, visual/text | Yes | Fully represented | Thought/caption inconsistency explicitly preserved |
| T8 | Yes, visual/text | Yes | Represented in compressed form | Thought roles preserved; object lists compressed |
| T9 | Yes, visual/text | Yes | Represented in compressed form | Repeated restricted feedback compressed |
| T10 | Yes, visual/text | Yes | Fully represented | Scores, key options, price visibility caveat included |
| M1–M5 principal mathematical objects | Yes, visual/text | Yes | Fully represented | Notation and lack of optimization proof stated |
| Algorithm/pseudocode | Checked | Yes | Fully represented | No standalone numbered algorithm supplied |
| Four p. 3 contribution claims | Yes, visual/text | Yes | Fully represented | Categories and evidence boundaries covered |
| Author-stated limitations | Yes | Yes | Fully represented | Prompting, retrieval, loops, context, human gap, access, risks |
| Appendix A.1 | Yes, visual/text | Yes | Fully represented | Cross-model results included |
| Appendix A.2 | Yes, visual/text | Yes | Fully represented | Outdated label discussed |
| Appendix A.3 | Yes, visual/text | Yes | Fully represented | Editing example and future-study status included |
| Appendix B.1 | Yes, visual/text | Yes | Fully represented | Batch and method-specific steps included |
| Appendix B.2 | Yes, visual/text | Yes | Fully represented | Restricted thought functions included |
| Appendix C.1, pp. 16–19 | Yes, text-only | Yes | Represented in compressed form | Six cases, formats, disambiguation, comparisons summarized |
| Appendix C.2, pp. 20–21 | Yes, text-only | Yes | Represented in compressed form | Three labels, evidence and missing-year reasoning summarized |
| Appendix C.3 | Yes, visual/text | Yes | Represented in compressed form | T6 examined |
| Appendix C.4 | Yes, visual/text | Yes | Represented in compressed form | T7–T9 compared |
| Appendix D.1, pp. 25–27 | Yes, mixed visual/text-only | Yes | Represented in compressed form | Success and failure examples summarized; omitted retrieval unavailable |
| Appendix D.2.1 | Yes, text-only | Yes | Represented in compressed form | Knife find/clean/place sequence included |
| Appendix D.2.2 | Yes, text-only | Yes | Represented in compressed form | Invalid cleaning and repeating loop included |
| Appendix D.2.3 | Yes, text-only | Yes | Represented in compressed form | Missing cleaning and placement loop included |
| Appendix D.3 | Yes, visual/text | Yes | Fully represented | T10 explained |
| Appendix E.1, pp. 32–33 | Yes, text-only | Yes | Represented in compressed form | All success/failure categories and key caveats included |
| Substantive footnotes | Yes, mixed | Yes | Represented in compressed form | Demonstration saturation, cutoff percentages, decoding speculation, excluded baseline, feedback direction |
| Separate supplementary files | No | Yes, absence disclosed | Missing from supplied material | No supplied file to inspect |
| Linked code/project artifacts | No | Yes, absence disclosed | Inaccessible within closed-document analysis | References do not constitute review |

### Missing or inaccessible material

No numbered page is missing from the supplied text sequence. Visual renderings are absent for pp. 10–13, 16–21, 26–30, and 32–33, so those pages received text-only review. External code and project pages were not inspected. Search results and steps explicitly omitted by the paper remain unavailable. No separate supplementary file was supplied, and no such file is claimed to have been reviewed.

### Uncertain interpretations

The actual cause and evaluation impact of T7's thought in a nominal Act prompt remain UNKNOWN. Exact unlabeled F3 bar heights were not confidently recovered. The precise meaning of room totals in F4 is qualified by its inclusion of suites. T10 does not show an updated option-specific price. Main knowledge-task evaluation counts, annotation agreement, significance procedures, seeds, hardware, and software versions are not supplied here. No explanation is provided for T2's 99% ReAct failure total. The native figure text's encoding corruption was resolved through supplied images where possible, without claiming exact recovery of every tiny character.

### Deliberately compressed material

Full prompt transcripts, household object inventories, repetitive failed commands, bibliographic entries, background human-cognition examples, and individual error-example narratives were compressed. Their substantive roles, failure categories, methodological controls, and relevant discrepancies are represented. Exact numbers for principal results and experimental conditions were retained; incidental biographical dates and product identifiers were not exhaustively reproduced because they are exemplar content rather than aggregate research findings.

### Potential omissions

Every identified substantive section, experiment, figure, table, principal mathematical object, contribution, and author-stated limitation is represented either directly or with disclosed compression. This is an inventory-based account of the supplied work, not a claim of word-for-word preservation or access to unprovided artifacts. Security conclusions beyond architectural relevance and the authors' warning remain unsupported: the work contains no adversarial comparison establishing greater vulnerability of web agents than standalone LLMs.
