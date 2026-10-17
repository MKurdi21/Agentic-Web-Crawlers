## Stage 0 — Document Accessibility Report

The supplied work is available as page-separated text for physical PDF pages 1–23. Nineteen corresponding page images are supplied: pages 1–4, 6–9, 11, and 14–23. These images were inspected directly alongside the supplied text. Pages 5, 10, 12, and 13 have text-only coverage; no visual inspection of those pages is claimed. The printed page numbers agree with the physical page labels used here. All main sections, the conclusion continuation, references, and Appendix A are represented in the supplied text. No apparently missing numbered page is identified within 1–23, but this does not establish that every separately distributed research artifact is present.

The six numbered figures and twelve numbered tables are visually available. Large labels, table values, and prompt text are generally readable; tiny browser-interface details within Figures 1, 3, and 4 are less dependable than their captions and surrounding descriptions. Mathematical notation in §3.1 is visually available and broadly readable. Extraction artifacts include a stray equals sign after R_j, accent corruption in some names, and awkward mathematical line breaks. These are flagged rather than treated as meaningful notation. OCR was not needed or performed: the supplied native/extracted text served as a reading aid, with images used for visual cross-checks.

Appendix A, including A.1–A.3, is present on pages 14–23 despite the supplied automated accessibility record reporting no detected appendix pages. The visible heading establishes its presence. No standalone supplementary file, benchmark dataset, source repository, executable code, raw trajectory collection, annotation export, or website content is supplied. Appendix A.3 is the supplementary detail explicitly referenced by the main text and is inspected here. The public benchmark address is author-reported but was not visited. The local-image error concerning a path named '-' does not invalidate the nineteen images actually displayed, but no additional image associated with that error was available.

Evidence categories used below are [A] author-reported, [B] directly observable, [C] analyst-derived, and [D] analyst interpretation. No external information [E] is introduced. Confidence is HIGH for clear text and table observations, MEDIUM for interpretations and unresolved methodological implications, LOW where a proposed security connection goes beyond direct measurement, and UNKNOWN for missing implementation details. This analysis addresses the supplied evaluation paper, not a nonexistent security experiment inferred from the user's research question.

## 1. Plain-language orientation

AgentRewardBench asks how reliably a language model can judge whether another language model operating a browser actually completed a user's request. A web agent does more than write an answer: it searches, clicks, enters text, changes pages, and sometimes modifies an online workflow. Its trajectory is the history of those observations and actions. Judging that history requires checking the real task outcome rather than accepting a convincing explanation from the agent. [A: pp. 1–4]

The researchers assembled 1,302 trajectories from four agent backbones across five benchmarks. Six expert annotators assessed success, unintended side effects, and repetitive action cycles. The paper compares twelve LLM judge configurations with official rule-based evaluation, and introduces a simplified judge that consumes action/reasoning history with a final browser-state representation. [A: pp. 1, 4–6]

The central finding is a tradeoff. LLM judges recognize more expert-approved successes than the aggregate rule-based evaluator, but often falsely approve failures. The highest overall LLM success precision in Table 1 is 69.8%, from GPT-4o with the final accessibility tree; the rule-based evaluator has 83.8% precision but only 55.9% recall. Different benchmarks favor different judges. Side-effect detection is particularly weak in the appendix results. [A/B: pp. 6, 17–18]

For the research question 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,' the paper provides indirect evidence about browser-action verification, misleading agent reasoning, and unintended effects. It does not compare attacked web agents with standalone LLMs, define an adversary, or measure security exploit rates. Its contribution is a benchmark of evaluator reliability, not a demonstrated causal explanation of greater security vulnerability. [D: grounded in pp. 1–9]

## 2. Document roadmap and inventory

The title is **AgentRewardBench: Evaluating Automatic Evaluations of Web Agent Trajectories**. The page header identifies it as a conference paper at COLM 2025; the supplied text does not expand that venue acronym. Authors are Xing Han Lù, Amirhossein Kazemnejad, Nicholas Meade, Arkil Patel, Dongchan Shin, Alejandra Zambrano, Karolina Stańczak, Peter Shaw, Christopher J. Pal, and Siva Reddy. Kazemnejad is marked as a core contributor. Affiliations include McGill University, Mila Quebec AI Institute, Google DeepMind, Canada CIFAR AI Chair, Polytechnique Montréal, and ServiceNow Research. [A/B: p. 1]

This is an empirical machine-learning benchmark and dataset paper with a systems implementation component. It is not a theoretical proof paper or a security attack/defense evaluation. Its important inventory is:

| ID | Original component | Location | Role |
|---|---|---|---|
| ABS | Abstract | p. 1 | Problem, dataset, headline findings |
| S1 | §1 Introduction | pp. 1–2 | Evaluation motivation and explicit questions |
| S2 | §2 Related Works | pp. 2–3 | Web agents, judges, trajectory synthesis |
| S3 | §3 AgentRewardBench | pp. 3–6 | Benchmark construction |
| SS31 | §3.1 Assessment Framework | pp. 3–4 | Trajectory notation, labels, annotators, judge |
| SS32 | §3.2 Tasks and Environments | pp. 4–5 | Five benchmarks and task split |
| SS33 | §3.3 Web Agents Design | pp. 5–6 | Models, platform, trajectory split, agreement |
| S4 | §4 LLM judges for web tasks | pp. 6–8 | Implementations and quantitative evaluation |
| SS41 | §4.1 Judge implementations | pp. 6–7 | AER, NNetNav, simplified judge |
| SS42 | §4.2 Evaluation | p. 7 | Precision rationale; recall and F1 |
| SS43 | §4.3 Judge Performance | pp. 7–8 | Aggregate results and ablation |
| S5 | §5 Revisiting how we evaluate task success rate | p. 8 | Expert, LLM, and rule-based rate comparison |
| S6 | §6 Error Analysis | pp. 8–9 | Four qualitative failure categories |
| S7 | §7 Conclusion | pp. 9–10 | Contributions and implications |
| ACK/REF | Acknowledgments and references | pp. 10–13 | Funding and cited sources |
| A1 | Appendix A.1 Environment and Experiments Details | p. 14 | Sampling, platform, limits |
| A2 | Appendix A.2 Annotations | pp. 14–15 | Filtering, interface, consensus |
| A3 | Appendix A.3 LLM Judges | p. 15; objects pp. 17–23 | Prompts and extended results |

Figures F1–F6 are an example trajectory, dataset creation diagram, judge error example, annotation interface, system prompt, and user prompt. Tables T1–T12 cover main judge performance, representation ablation, agent success rates, website visits, hyperparameter flags, expanded success rates, aggregate three-label metrics, benchmark-specific metrics, and four purported agent-specific metric tables. Mathematical objects E1–E7 cover browser transition, trajectory sequence, observation representation, model completion, completion parsing, annotation answers, and judge representation. X1–X6 below identify benchmark construction/agreement, judge comparison, representation ablation, success-rate comparison, qualitative error analysis, and auxiliary-label evaluation. No numbered algorithm, pseudocode procedure, theorem, lemma, keyword list, or formal hypothesis is supplied.

## 3. Background and context

A **large language model (LLM)** receives a representation of the current situation and generates a completion. Here that completion can be parsed into a browser action and an explanation for choosing it. A **multimodal** model can use visual inputs such as screenshots; a text-only model relies on textual representations. A **vision-language model (VLM)** is the paper's notation for the multimodal case. [A: pp. 3–5]

A browser's **Document Object Model (DOM)** represents webpage structure. An **accessibility tree**, abbreviated **A11Y**, is rendered from the DOM and supplies a textual page representation. Screenshots convey visual appearance; the paper notes that they may omit structure or hidden attributes available in accessibility trees. The two input types therefore expose different evidence to an evaluator. [A: pp. 3, 7]

A **trajectory** contains successive browser observations, model reasoning, and executable actions. A **judge** evaluates that trajectory against the user's goal. The official **rule-based evaluator** uses task-specific programs or matching rules. An expert human evaluator can interpret valid alternatives but is expensive to scale. The proposed benchmark treats expert answers as ground truth when comparing automatic judges. This is an operational reference standard, not proof that human labels are infallible. [A: pp. 1–4; D: qualification]

**Reinforcement learning (RL)** uses reward signals to guide learning. **Rejection finetuning (RFT)**, as discussed here, selects trajectories judged successful for further training. False approvals can introduce failed demonstrations into the training collection. **Direct preference optimization** is mentioned in the related-work discussion as one use of synthesized contrasting trajectory pairs; it is not trained or evaluated in this paper. [A: pp. 2–3, 7]

Related work is grouped into web agents/environments, LLM judges, and trajectory synthesis. The authors describe a progression from programmed heuristics to reinforcement-learning, language-model, and multimodal agents. They distinguish prior judge evaluations based on private subsets or rule-based reference labels from their multi-agent, multi-environment, expert-annotated benchmark. The cited 80.6% prior accuracy against WebArena rules is not interchangeable with this paper's precision against expert labels. [A: p. 3]

## 4. Research problem and gap

**Existing problem.** Determining whether a browser agent fulfilled a natural-language goal is difficult because tasks may allow multiple valid action sequences and outcomes. An evaluator must inspect the final result and potentially the actions taken along the way. [A: pp. 1–2]

**Shortcomings attributed to prior approaches.** Task-specific rules are time-consuming to design, difficult to extend, and can reject valid outcomes. Human annotation is slower and more expensive. LLM judges offer flexible evaluation but their agreement with expert judgments is uncertain. Some trajectory-synthesis systems validate judging quality through downstream agent improvements rather than directly measuring the correctness of judgments. [A: pp. 1–3]

**Gap.** The authors seek a shared test of LLM judges across several agents, environments, and outcome dimensions using expert annotations. This avoids assuming the official benchmark reward is itself the correct definition of task success. [A: p. 3]

**Motivation.** Better evaluation could improve benchmark measurement, selection of useful training trajectories, and reward modeling. These downstream uses motivate precision as the primary metric; the paper does not experimentally demonstrate improved finetuning or RL from this benchmark. [A: pp. 2, 7; B: experiment inventory]

**Scope.** The work examines task success, side effects, repetition, representation choices, and evaluation errors on five web-agent benchmarks. It does not assess authentication, authorization, exfiltration, malicious websites, prompt-injection defenses, or comparative standalone-chatbot security. Those topics cannot be silently added to its findings. [D: scope interpretation based on supplied methods]

## 5. Research questions, objectives, and hypotheses

Two explicit questions appear on page 2:

- **RQ1:** Given a web agent trajectory, can an LLM decide if it is successful?
- **RQ2:** If so, how do we determine which LLM is the most capable at evaluating web agents?

The principal objective is to benchmark evaluator predictions against expert annotations. Additional objectives are to cover diverse tasks and agent models, compare prior and simplified judging methods, assess browser-state representations, examine differences in measured agent success rates, and identify judge failure modes. These are objectives inferred from the study organization or directly described as analyses, not newly invented formal research questions. [A/D: pp. 3–9]

No explicit preregistered hypothesis, statistical null hypothesis, or formal security hypothesis is stated. In particular, the user's standalone-LLM comparison is an external research agenda supplied by the user, not a hypothesis tested by the authors. The findings can inform that agenda only through clearly labeled analyst inference.

## 6. Assumptions / Threat Model

There is no adversarial threat model in the supplied paper. No attacker, malicious objective, attacker knowledge, resource budget, payload, attack success criterion, or defended asset is experimentally specified. Calling a judge failure an exploit would therefore overstate the evidence.

The study's operational model has several assumptions. A browser engine can execute the model's actions and return the next observation. The trajectory recording exposes enough relevant state for expert annotation and automatic evaluation. Expert consensus is used as the target label. A judge may operate after execution from saved evidence; continued interactive access to the environment is not assumed. This last point motivates excluding an Agent-as-a-Judge approach when environment state cannot be preserved or shared. [A: pp. 3–6]

The authors use dedicated/resettable environments and real websites, with different task difficulties. They focus on WorkArena++ Level 2 because Level 3 is described as too challenging for current agents. Llama 3.3 is excluded as an agent from VisualWebArena because it is text-only. Its presence as a text-only judge of other agents' trajectories is a different role. [A: p. 5]

**Analyst interpretation for security:** the evaluation boundary connects natural-language goals, webpage observations, model-generated explanations, executable actions, and approval/reward decisions. Misleading reasoning can cross this boundary when accepted as evidence of completion. The paper observes such mistakes without demonstrating deliberate attacker control. Likewise, success and side effects are assessed independently, so task completion is not equivalent to absence of unwanted actions. [D: pp. 4, 8–9]

## 7. Methodology

### Dataset and sampling

The authors curate 351 unique tasks across five benchmarks, eight environments, and 66 websites, separating tasks into 51 development and 300 test tasks. Appendix A.1 additionally identifies 66 unique domains visited in AssistantBench; the relation between the overview's website total and all self-hosted environment sites is not fully clarified. [A: pp. 5, 14]

| Benchmark | Tasks | Supplied description |
|---|---:|---|
| AssistantBench (AB) | 33 | Real-world navigation beginning from a search engine; validation set used because the benchmark test set is private |
| VisualWebArena (VWA) | 100 | Visual reasoning, including image-conditioned or visually distinctive item selection |
| WebArena (WA) | 100 | Six self-hosted website domains spanning shopping, maps, encyclopedia, forum, administration, and collaboration |
| WorkArena (Work) | 18 | Basic professional workflow tasks on ServiceNow |
| WorkArena++ (Wk++) | 100 | More complex professional tasks; Level 2 selected |

WebArena tasks are sampled by domain–evaluation-method subgroup, up to eight per subgroup; VisualWebArena uses up to nine. Original evaluation types include string matching, HTML-based programs, webpage image querying, and final URL matching. The WebArena domain counts are Wikipedia 8, Map 18, Reddit 18, Shopping Admin 18, Shopping 19, and Gitlab 19. VisualWebArena counts are Wikipedia 17, Reddit 27, Classifieds 28, and Shopping 28. [A: p. 14]

Page 14 labels a 100-task category distribution 'WorkArena': sophisticated memory 15; information retrieval 20; contextual understanding infeasible tasks 21; planning/problem solving 22; data-driven decision making/reasoning 22. This conflicts with the same page's 18 WorkArena versus 100 WorkArena++ task totals. The likely destination cannot be silently corrected; the category distribution is preserved with the labeling uncertainty. [B/C: 15+20+21+22+22=100]

### Agents and filtering

Agents use GPT-4o, Claude 3.7 Sonnet, Llama 3.3 70B, and Qwen2.5-VL. The supplied paper does not specify the Qwen parameter size. GPT-4o's agent version is gpt-4o-2024-11-20. Llama uses an instruction-tuned text-only variant and receives no VisualWebArena agent tasks. The other three agents cover all 351 tasks. Llama nominally covers 251, but WebArena tasks 735 and 805 repeatedly time out and are not completed. [A: pp. 5, 14]

The reported total is 1,302 trajectories: 196 development and 1,106 test. **Analyst-derived reconciliation:** 3×351 + 251 − 2 = 1,302; 196 + 1,106 = 1,302. Each receives three binary labels, giving 1,302×3 = 3,906 annotations. The split is tied to task membership, but detailed benchmark-by-split counts and leakage checks are not supplied. [A/C: pp. 5, 14]

### Annotation procedure

Six researchers with deep knowledge of the environments review goals, actions, reasoning, and screenshots. The custom Gradio interface overlays the action element on a screenshot. Annotators can inspect the environment and accessibility tree when screenshots are insufficient. They answer whether the goal was achieved, whether unnecessary actions could cause unintended side effects, and whether action cycles failed to make progress. [A: pp. 4, 14]

Uncertain labels are reviewed by colleagues. Disagreements are discussed to consensus. For ambiguous instructions, annotators are advised to use the most lenient interpretation, exemplified by whether a 'black t-shirt' may contain graphics. The first half of annotation occurs with annotators concurrently present in person, allowing consensus to influence subsequent judgments. A second annotator assesses GPT-4o's WebArena trajectories, yielding 89.3% success agreement; the sample size and agreement statistic beyond percentage agreement are not specified. [A: pp. 6, 15]

### Implementation and hyperparameters

BrowserGym abstracts websites and browser engines as Gym-compatible environments, preprocesses DOM/accessibility information, parses completions, and executes browser actions. AgentLab manages input representations and experiments. Unified settings aim to avoid unintended differences from model-specific prompts and representations. Maximum inputs are 40K tokens; maximum outputs are 8,192 tokens. These are agent settings, not clearly specified judge-generation limits. [A: p. 14]

Table 5 enables use_screenshot, use_som, use_thinking, use_concrete_example, use_abstract_example, use_hints, and be_cautious. It disables use_html, use_past_error_logs, use_think_history, use_diff, filter_visible_elements_only, long_description, individual_examples, use_plan, use_criticise, use_memory, and enable_chat. 'use_som' is not expanded in the supplied work. The global screenshot flag must be understood alongside Llama's explicit text-only capability; model-specific flag handling is not detailed. [A/B: p. 17]

AssistantBench's default search homepage blocks automation, so the researchers substitute DuckDuckGo. Table 4 still records visits to Google and other search services; replacing the initial search engine does not imply all later search-provider visits disappear. Hardware, operating system, library versions, decoding temperatures, random seeds, judging retries, parser failure policies, latency, monetary cost, and repeated-run counts are not reported. [A: p. 14; B: reporting inventory]

### Judges and metrics

Agent Eval Refine (AER) receives reasoning/action history and final state. AER-V uses the screenshot; AER-C uses a generated caption. Both judge and captioner use GPT-4o, replacing the original method's GPT-4. NNetNav summarizes changes between accessibility-tree observations, then rates the trajectory from 1 to 5; a threshold of 4 converts the rating to binary. This implementation uses Llama 3.3 70B rather than the original Llama 3.1 70B. [A: p. 6]

The simplified judge uses history plus a final accessibility tree (A) or final screenshot (S), without a separate captioning/summarization LLM. Five A variants and four S variants appear because Llama is text-only. Together with AER-C, AER-V, and NNetNav these yield twelve LLM configurations. The rule-based evaluator is a separate reference row. Figure 5's actual prompt also requests optimality, creating an unresolved difference from the three-label method description. [A/B: pp. 6, 15, 23]

Precision is primary because false-positive trajectories would contaminate selected training data and rewards. Recall and F1 are auxiliary because discarding genuine successes reduces useful sample availability. No significance testing, confidence intervals, or error bars are supplied. The table values are percentages; the exact micro/macro aggregation procedure is not stated. [A: p. 7]

## 8. Experiments / Analyses

### X1 — Benchmark construction and annotation agreement

Purpose: establish expert-labeled evidence spanning several agent/environment combinations. Data: 351 tasks, 1,302 trajectories, 3,906 binary annotations. Controls are shared platform settings and task-based development/test separation. Agreement is assessed only on the GPT-4o/WebArena subset, with 89.3% agreement on success. This supports a degree of reference-label consistency but does not establish agreement for all models, all benchmarks, or auxiliary labels. [A: pp. 5–6, 14–15]

### X2 — Success-judge comparison

Purpose: answer RQ1/RQ2 by comparing automatic predictions against experts. Conditions: twelve LLM configurations and official rules; aggregate and per-benchmark metrics. Table 1 reports GPT-4o(A) at 69.8/83.1/75.9 precision/recall/F1, versus rules at 83.8/55.9/67.1. AER-C is 67.7/71.9/69.7, AER-V 67.6/71.5/69.5, and NNetNav 52.5/82.4/64.1. These support improved aggregate recall and F1 for several simplified judges, while rules retain higher aggregate precision. [A/B: p. 6]

Benchmark dependence matters: AER-C reaches 100.0% WorkArena precision; Claude(A) leads LLM precision on AssistantBench at 87.5%; Claude(S) leads on VWA at 64.8%; GPT-4o(A) leads on WA at 70.2%; and AER-C plus both Claude variants tie at 66.7% on Wk++. No single LLM configuration wins every benchmark. These are descriptive maxima, not statistically established rankings. [B: pp. 6, 18]

### X3 — Input-representation ablation

Purpose: isolate inclusion of final accessibility-tree and screenshot evidence for GPT-4o Mini. Four conditions are both, A11Y only, screenshot only, and neither. Success P/R/F1 is 62.1/81.7/70.6, 61.5/86.1/71.7, 64.5/78.3/70.8, and 60.7/73.9/66.7 respectively. Screenshot only has highest success precision; A11Y only has highest recall and F1. Both inputs do not dominate either single-input option. [A/B: p. 7]

For repetition, both inputs yield 92.5% precision but 16.8% recall; screenshot only yields 92.3/18.5/30.8; neither yields 78.1/59.1/67.3. For side effects, neither gives the highest F1, 13.2, versus 10.8 with both. Thus 'more information distracts' is the authors' interpretation of this one-model ablation, not a demonstrated universal mechanism. [A/B: pp. 7–8]

### X4 — Evaluator-dependent agent success rates

Purpose: examine how evaluator choice changes measured agent performance. Tables 3 and 6 compare expert labels, GPT-4o(A), and rules. For the GPT-4o agent, WA success is 42.3/50.0/25.6%, VWA is 35.9/47.8/17.4%, and Wk++ is 18.4/11.5/4.6%, in expert/judge/rule order. Rules undercount these successes; the judge overcounts in the first two and undercounts in the third. [A/B: pp. 8, 17]

The ranking of GPT-4o versus Qwen changes: WA rules give 25.6 versus 29.5%, whereas experts give 42.3 versus 33.3%. Wk++ rules give 4.6 versus 11.5%, whereas experts give 18.4 versus 13.8%. VWA rules tie at 17.4%, whereas experts give GPT-4o 35.9% and Qwen 21.7%. [B: p. 8]

### X5 — Qualitative error analysis

Purpose: explain false approval mechanisms using GPT-4o judge cases. Four categories are grounding mismatch, misleading agent reasoning, missed instruction details, and misunderstanding action intents. Examples involve selecting the wrong grid item, falsely claiming a filter was applied, stopping after adding cereal to a cart instead of buying it, and marking a travel-time task infeasible after finding the answer. These cases show mechanisms but supply no category prevalence or randomized error sample. [A: pp. 8–9]

### X6 — Auxiliary side-effect and repetition evaluation

Purpose: test whether judges also detect unwanted actions and unproductive cycles. Table 7 reports extremely low aggregate side-effect precision: 6.6–14.1% among simplified configurations. Repetition is substantially stronger for several models: Claude(A) 82.8/94.9/88.4 and GPT-4o(A) 80.4/96.9/87.9 P/R/F1. GPT-4o Mini(S) trades 92.3% precision for only 18.5% recall. Class counts and uncertainty are absent, so these metrics cannot identify the underlying cause of low side-effect precision. [B: p. 17]

## 9. Results and numerical interpretation

**Aggregate precision is limited.** The best LLM precision is 69.8%. **Analyst-derived:** among predicted successes for that configuration, the false-positive share is 100−69.8 = 30.2%. This is not a claim that 30.2% of all trajectories fail, nor that every benchmark has that false-positive rate. The page-7 prose's statement that no judge exceeds 70% needs the qualifier 'overall LLM precision'; individual benchmark values exceed 70%, and the reference rules reach 83.8% overall. [A/B/C: pp. 6–7]

**Rules sacrifice recall.** Their 55.9% recall means **analyst-derived** 44.1% of expert-positive trajectories are missed under the reported aggregate metric, calculated as 100−55.9. GPT-4o(A)'s recall is higher by 83.1−55.9 = 27.2 percentage points, while its precision is lower by 83.8−69.8 = 14.0 points. Its F1 exceeds the rules by 75.9−67.1 = 8.8 points. These are derived percentage-point differences, not relative percent improvements. [B/C: p. 6]

**Representation choices have mixed effects.** For Mini, screenshot-only versus A11Y-only success precision increases by 64.5−61.5 = 3.0 points, but recall decreases by 86.1−78.3 = 7.8 points. Adding both inputs yields a success F1 of 70.6, below either A-only 71.7 or screenshot-only 70.8, but both-input repetition precision 92.5 narrowly exceeds screenshot-only 92.3. This prevents a blanket claim that every metric worsens with both inputs. [B/C: p. 7]

**Success-rate gaps are absolute points.** Page 8 calls GPT-4o's rule-based shortfalls 16.7% on WA and 18.5% on VWA. Table arithmetic identifies these as 42.3−25.6 = 16.7 percentage points and 35.9−17.4 = 18.5 points. The expert VWA advantage over Qwen is 35.9−21.7 = 14.2 points. No relative percentages are substituted for those differences. [A/B/C: p. 8]

**Auxiliary labels are not equally reliable.** Claude(S) has the highest aggregate side-effect precision, 14.1%, and side-effect F1, 21.4. GPT-4o(A) has much higher side-effect recall, 91.7%, but precision only 7.7%. Repetition is more effective for several configurations, yet Mini(S)'s high precision hides low recall. A safety interpretation cannot rest on one favorable metric. [B/D: p. 17]

**Claims of consistent evaluator bias need qualification.** Table 6 includes rule-based values above expert success for AB Llama, 5.3 versus 3.7%, and AB Qwen, 2.2 versus 0.0%. WorkArena has several ties. The GPT-4o judge also underestimates WorkArena Llama, 50.0 versus 56.2%, beyond the two Wk++ exceptions highlighted in §5. The main trend holds across many entries, but universal wording is stronger than the expanded table supports. [B: p. 17]

## 10. Figure-by-figure interpretation

### Figure 1 — A trajectory and its evaluation

The diagram on page 2 has an orange web-agent box, a natural-language goal, a green sequence of browser screenshots/actions, a yellow human evaluator, green human labels, and a blue LLM judge. Arrows show the goal and agent feeding the action sequence, then the trajectory being assessed by the judge and compared with human annotation. There are no numerical axes, scales, error bars, or statistical markers. The displayed goal requests the latest white Google Pixel listing and a comment offering $10 below the asking price. The pictured sequence searches, selects a listing, fills a comment, and sends it. [B]

The human label says successful, with no side effect and no repetition. The judge text mentions a white Pixel 3XL priced at $260.00. These are illustrative values, not study-wide results. A visible caveat is that the displayed filled comment says only that the buyer is interested in purchasing the phone; no $250 offer is visibly included. The small screenshots do not establish whether omitted details resolve this difference. Accordingly, the visual explains evaluation flow but does not independently certify every criterion of that example's goal. [B/D: p. 2]

### Figure 2 — Benchmark creation process

Page 4 separates an orange web environment from a yellow/green assessment platform. Instructions feed both the web agent and human evaluator. The agent produces trajectories; trajectories and guidelines feed human assessment, which produces annotations. The green lower region identifies trajectories plus annotations as AgentRewardBench. Arrows are workflow/data connections, not measured effects. No axes or quantitative encoding are present. This figure explains why the benchmark is a labeled collection used to evaluate judges rather than a new browser-agent training algorithm. [A/B]

### Figure 3 — False approval of an incomplete purchase

Page 9 combines shopping screenshots with three colored text boxes: orange goal, red agent reply, and blue judge reasoning. Goal #843 asks to buy the cheapest cereal with a graphic character. Claude 3.7 Sonnet says it found Cocoa Puffs and added it to the cart; a red cross marks failure. GPT-4o claims the agent identified and purchased it; a disapproval symbol marks the judge error. Colored connecting arrows associate browser evidence with the statements. There are no axes or plotted numerical results. The caption explicitly establishes the missing purchase step, so this interpretation does not depend on reading tiny shop controls. [A/B]

This supports the missed-instruction-details category and illustrates the distinction between identifying, adding to cart, and completing a purchase. It is not an adversarial attack demonstration, and its single-case nature does not establish prevalence. [D]

### Figure 4 — Annotation interface

Page 16 shows a dark Gradio interface with selectors for annotator, benchmark, model, and task; trajectory step screenshots; reasoning/action text; question controls; and save/navigation buttons. Multiple interface views illustrate reviewing steps and recording judgments. Browser-page controls within the image are small, so exact underlying website values are not relied upon. The visual supports the stated annotation workflow and availability of goal/action/reasoning/screenshot evidence. It does not itself show agreement rates or prove that every annotator used every optional evidence source. [A/B]

### Figure 5 — System prompt template

Page 23 visibly specifies the judge role and four requested answers: success, side effects, optimality, and repetition. Success is binary; side and loop are Yes/No; optimality is a four-level scale from complete failure to completely optimal. Structured tags identify reasoning and each response. It says the judge has first/last screenshots and the final accessibility tree. This is prompt evidence, not an instruction to the analyst. [B]

The four questions and broad input description differ from the main method's three labels and A-versus-S variants. The supplied work does not show exact edited prompts for every ablation condition, nor any optimality result. These discrepancies affect implementation traceability. [B/D]

### Figure 6 — User prompt template

The template lists goal, repeated step number, URL, action, reasoning, final accessibility tree, and final screenshot, and asks for answers to the four system questions. This is a structured record layout with no quantitative visual scale. It makes inclusion of agent-generated reasoning particularly explicit. Placeholders do not contain actual trajectories, and the simultaneous presence of screenshot/tree placeholders cannot prove that both were populated in each A/S experiment. [B: p. 23]

## 11. Table-by-table interpretation

All reported metric values below are on a percentage scale. No table supplies confidence intervals, significance markers, or repeated-run uncertainty. Dashes mark unavailable/not reported auxiliary metrics for evaluators that do not output those labels; they are not zeros. A/S means final accessibility tree/final screenshot, while Claude's 'S.' abbreviates Sonnet and should not be confused with the representation suffix.

### Table 1 — Main success-judge performance, p. 6

Rows compare official rules, existing judge implementations, and nine simplified configurations. Columns give overall precision/recall/F1 and precision on AB, VWA, WA, Work, and Wk++. The rule row is explicitly included for reference. It has the best overall precision, 83.8, but recall 55.9. GPT-4o(A) has the best LLM overall precision and F1, 69.8 and 75.9. Qwen(A) has the highest LLM recall, 89.8. NNetNav has the lowest LLM aggregate precision, 52.5. Existing AER-C reaches 100.0 precision on Work, showing that simplified judges do not dominate every condition. The complete overall success triples are reproduced under Table 7.

### Table 2 — Mini input ablation, p. 7

Rows indicate presence/absence of A11Y and screenshot. The following preserves every experimental result, in P/R/F1 order:

| A11Y | Screen | Success | Side effect | Repetition |
|---|---|---|---|---|
| Yes | Yes | 62.1/81.7/70.6 | 6.5/31.9/10.8 | 92.5/16.8/28.4 |
| Yes | No | 61.5/86.1/71.7 | 7.2/70.8/13.0 | 78.6/46.4/58.3 |
| No | Yes | 64.5/78.3/70.8 | 6.6/31.9/11.0 | 92.3/18.5/30.8 |
| No | No | 60.7/73.9/66.7 | 7.2/76.4/13.2 | 78.1/59.1/67.3 |

Neither-input rows are not evidence-free: action/reasoning history remains part of the judge design. 'Both' is worse than screenshot-only on success precision and F1, but not on every auxiliary metric. This table is a specific ablation, not a universal comparison of text and vision.

### Table 3 — Selected agent success rates, p. 8

Rows are agent models; columns are evaluator-by-benchmark combinations for VWA, WA, Wk++. Every VWA/WA expert-positive agent shown is overestimated by GPT-4o(A), while Wk++ has underestimates for GPT-4o and Llama. The VWA Llama row is 0.0 throughout despite the model being excluded from that benchmark: it should not be interpreted as measured failure on attempted visual tasks. Table 6 omits that nonexistent agent condition, which is preferable evidence for coverage. Evaluator-dependent ranking changes are detailed in X4.

### Table 4 — AssistantBench website visit counts, p. 16

Three repeated Domain/# column pairs list 66 entries. The most frequent are duckduckgo.com 129, google.com 112, wizards.com 24, blackbaudhosting.com 21, and fedex.com and mtggoldfish.com 17 each. Values range from 1 to 129; numerous sites have one visit. These are visits/domain encounters across collected trajectories, not unique tasks, successful tasks, or independent subjects. The website list spans search, shipping, weather, entertainment, shopping, finance, and other domains; all individual low-frequency names are deliberately compressed. The entry 'chromewebdata' is visible and should not automatically be equated with an ordinary public website. The table does not report visit-to-success relationships.

### Table 5 — AgentLab binary settings, p. 17

The two rows group enabled and disabled flags, transcribed in §7. They specify agent input/behavior configuration, not judge quality. No model-specific exceptions or software version appears in the table. Disabled memory, planning, or criticism flags should not be inflated into claims about the intrinsic absence of those capabilities in the underlying models.

### Table 6 — Expanded success-rate comparison, p. 17

The following reproduces all reported expert/judge/rule success-rate triples:

| Benchmark | Claude 3.7 Sonnet | GPT-4o | Llama 3.3 | Qwen2.5-VL |
|---|---|---|---|---|
| AB | 11.1/11.1/0.8 | 14.8/14.8/3.7 | 3.7/7.4/5.3 | 0.0/0.0/2.2 |
| WA | 55.1/64.1/30.8 | 42.3/50.0/25.6 | 22.4/27.6/18.4 | 33.3/52.6/29.5 |
| VWA | 28.3/34.8/23.9 | 35.9/47.8/17.4 | Not listed | 21.7/34.8/17.4 |
| Work | 68.8/68.8/50.0 | 50.0/56.2/50.0 | 56.2/50.0/56.2 | 56.2/56.2/56.2 |
| Wk++ | 18.4/20.7/8.1 | 18.4/11.5/4.6 | 9.2/5.8/3.5 | 13.8/14.9/11.5 |
| Overall | 33.0/38.0/20.4 | 31.3/35.3/16.3 | 17.0/17.5/13.3 | 22.3/31.7/19.5 |

The LLM judge is GPT-4o(A). Overall expert ordering is Claude, GPT-4o, Qwen, Llama; rules put Claude, Qwen, GPT-4o, Llama. Fractional AB rule values such as 0.8 and 2.2 are not explained by binary task-rate counts in the supplied methodology. Without evaluator details, they should not be reverse-engineered into assumed numbers of successful trajectories. The table also contains exceptions to the prose's universal underestimation language.

### Table 7 — Overall three-label metrics, p. 17

This table provides the fullest aggregate comparison. All results are preserved below as P/R/F1:

| Judge | Success | Side effect | Repetition |
|---|---|---|---|
| AER-C | 67.7/71.9/69.7 | — | — |
| AER-V | 67.6/71.5/69.5 | — | — |
| Claude(A) | 68.8/81.6/74.7 | 14.0/34.7/20.0 | 82.8/94.9/88.4 |
| Claude(S) | 69.4/76.3/72.7 | 14.1/44.4/21.4 | 82.0/94.5/87.8 |
| Functional | 83.8/55.9/67.1 | — | — |
| GPT-4o(A) | 69.8/83.1/75.9 | 7.7/91.7/14.2 | 80.4/96.9/87.9 |
| GPT-4o(S) | 68.1/80.3/73.7 | 7.5/90.3/13.8 | 79.2/96.2/86.9 |
| Mini(A) | 61.5/86.1/71.7 | 7.2/70.8/13.0 | 78.6/46.4/58.3 |
| Mini(S) | 64.5/78.3/70.8 | 6.6/31.9/11.0 | 92.3/18.5/30.8 |
| Llama(A) | 67.7/79.0/72.9 | 6.9/79.2/12.7 | 80.1/91.6/85.5 |
| NNetNav | 52.5/82.4/64.1 | — | — |
| Qwen(A) | 64.3/89.8/75.0 | 9.0/55.6/15.4 | 88.1/72.6/79.6 |
| Qwen(S) | 64.5/86.1/73.7 | 8.8/58.3/15.2 | 88.7/64.6/74.7 |

'Functional' matches the rule-based reference metrics and is interpreted as that evaluator, supported by matching values rather than an explicit new definition. Side-effect metrics reveal a weakness largely absent from the main prose. High repetition precision alone can coexist with severe missed-cycle rates.

### Table 8 — Per-benchmark three-label performance, p. 18

This dense table contains thirteen rows per benchmark and nine metric columns. Selected substantive patterns beyond Table 1 are: Mini(A/S) reaches AB success recall 100.0 with F1 88.9; WA GPT-4o(S) has F1 78.7, slightly above GPT-4o(A)'s 78.5; Work functional evaluation has 100.0/91.9/95.8 success P/R/F1; Wk++ Qwen(S) has the highest LLM success F1, 68.5, despite not leading precision.

Side-effect precision remains poor by benchmark: its maximum is 7.7 on AB, 17.2 on VWA, 14.8 on WA, 8.3 on Work, and 17.1 on Wk++. Several Work conditions report 0.0 throughout this label. Such zeros do not distinguish no positive predictions from incorrect predictions without confusion counts and zero-denominator conventions. Repetition has strong Wk++ F1 for Claude(S), 92.8, while Mini(S) is 33.4. On Work, Mini(S) and Qwen(A) both reach 100.0 repetition precision but recalls are 18.2 and 59.1 respectively. These conditions demonstrate why auxiliary-label conclusions cannot be reduced to one overall success score. Remaining per-row values are deliberately compressed, not claimed absent.

### Tables 9–12 — Purported agent-specific results, pp. 19–22

The captions respectively identify Qwen2.5-VL, Llama 3.3, Claude 3.7 Sonnet, and GPT-4o agent trajectories. However, both the supplied text and the rendered tables visibly repeat Table 8's results across all five benchmarks. For example, GPT-4o(A)'s AB success row is 77.8/87.5/82.4 in each, and the repeated Llama-agent table includes VisualWebArena despite the stated collection exclusion. This is a material caption–table/methods inconsistency.

These four objects were inspected individually; their numbers are not treated as valid independent agent-specific measurements. Their repetitive cells are compressed, with the inconsistency preserved. The supplied material cannot determine whether this is an authoring error, artifact construction error, or another provenance problem. No missing correct tables are invented, and no agent-specific claim is inferred from those duplicated contents.

## 12. Diagram / Architecture Interpretation

The agent architecture is a recurring loop: browser observation → representation function → model completion → execution parser → browser action → new observation. The representation can combine page information with prior reasoning/actions. BrowserGym implements page preprocessing and executable browser interaction; AgentLab manages representation and experimental configuration. The terminal observation ends the recorded trajectory. [A: pp. 3–5, 14]

The benchmark architecture is separate: benchmark instruction and environment → agent trajectory → expert interface/guidelines → reference annotations. A judge then receives a goal and trajectory representation and predicts reference answers. Comparing predictions with annotations measures evaluator quality. Figure 2's arrows describe collection and labeling; they do not show an end-to-end training feedback loop. [A/B: pp. 3–4]

Judge implementations differ at the representation stage. AER-C inserts a captioning model; AER-V directly uses the final image; NNetNav inserts a change-summary process; simplified variants directly use history with a final tree or screenshot. This is a comparison of evidence-processing pipelines as well as model backbones. Removing intermediary models is a methodological simplification, but the paper does not measure latency, cost reduction, or which intermediate summaries lost which facts. [A/D: pp. 6–7]

For security research, an analyst can distinguish observation reliability, action correctness, and evaluator approval as separate boundaries. A judge accepting an agent's account can fail even when the browser screenshot contradicts it. That is a conceptual connection supported by error examples, not a tested defense architecture or quantified attack surface. [D: pp. 8–9]

## 13. Equations and mathematical concepts

The paper has definitional equations rather than an optimization theorem or training loss.

**E1 — Browser transition, p. 3:** o_(i+1) = B(o_i, a_i). Here o_i is browser observation at step i, a_i is an executable action, and B is the browser navigation engine. The output is the next observation. This models the changing environment; the work does not explicitly establish deterministic behavior, so deterministic guarantees should not be inferred from the function notation.

**E2 — Trajectory, p. 3:** T = {o_1, (r_1,a_1), o_2, (r_2,a_2), …, o_(n−1), (r_(n−1),a_(n−1)), o_n}. Each r_i is reasoning for an action. There are n observations and n−1 intervening action/reasoning pairs. Although braces are used, the authors call this a sequence; ordering is essential. The final observation o_n is part of the evidence needed to judge completion.

**E3 — Agent representation, p. 3:** p_i = R(o_1,r_1,a_1,…,o_i). R converts observation/history into a model input p_i. An observation may contain screenshot s_i, DOM information, and an accessibility tree. The exact model-specific retained content is not fully specified, and Table 5 disables some history-related flags; the abstract representation is not a guarantee that all history always reaches every model.

**E4 — Model completion, p. 4:** c_i = LM(p_i), or c_i = VLM(p_i,s_i) for the multimodal case. c_i is generated model output. LM and VLM distinguish textual versus visual-input processing, with screenshot s_i supplied in the latter. These formulas do not define the models' architectures or probabilities.

**E5 — Execution parsing, p. 4:** (a_i,r_i) = E(c_i). E parses completion into an action and reasoning. It links language output to operational browser behavior. The order shown here is action then reasoning, whereas trajectory tuples display reasoning then action; the definitions, not tuple order alone, establish meaning. Invalid-output and parser-error handling are not given.

**E6 — Annotation answers, p. 4:** Q = {q_1,…,q_m} and A* = {a*_1,…,a*_m}. Q is the collection of annotation questions; A* is expert ground truth. The answer symbol a*_j must not be confused with browser action a_i. A judge returns predicted answers Â estimating A*. The three reported binary dimensions imply m=3 for the annotation scheme, but Figure 5 requests a fourth optimality answer from the judge.

**E7 — Judge representation, p. 4:** p = R_j(o_1,r_1,a_1,…,o_n). R_j is judge-specific evidence encoding. It can vary from an action list to an observation-history summary. The extracted stray equals sign after R_j in the following sentence has no defined mathematical role and is treated as a typographic/extraction issue.

**Metrics, p. 7:** the authors explicitly define precision as TP/(TP+FP), where TP are correctly predicted positives and FP are incorrectly predicted positives. Plainly, it answers 'Of the trajectories approved as successful, how many actually were successful?' Recall and F1 are named but not explicitly formulated in the supplied text; no missing equations are silently attributed to the authors. Metric interpretation follows their stated concerns about false negatives and sample efficiency. No theorem, proof, formal objective function, or training optimization is supplied.

## 14. Interpretation and Discussion

RQ1 receives a qualified answer: LLM judges can extract useful signals, but the tested overall success precision is insufficient for treating their approval as a dependable certificate. RQ2 receives a benchmark-dependent answer: expert-labeled comparisons reveal tradeoffs across models, representations, and environments. There is no universal winning configuration. These answers are narrower than declaring LLM judging useless or rule-based evaluation inherently inferior. [A/D: pp. 6–9]

The authors argue that rules reject valid alternatives and LLM judges miss nuanced failures. Both can be true simultaneously. A higher F1 or recall is useful for recovering successes, while a higher precision is useful for avoiding contaminated accepted data. The appropriate criterion depends on the downstream purpose; that purpose is discussed but not experimentally tested. [A/D: p. 7]

Cross-reference checks identify the following unresolved points:

- The abstract/methods report 1,302 trajectories; page 2's 1,300 and the conclusion's 'over 1300' are coarser descriptions, not evidence of different dataset versions.
- Twelve LLM configurations are supported by Tables 1/7, while Appendix A.3 says extended results for ten. The discrepancy is not reconciled.
- The three-label method and 3,906 annotations differ from the four-question prompt. Optimality annotations or results are not supplied.
- Figure 5 mentions first/last screenshots, while Figure 6 shows a last-screenshot placeholder; first-screenshot insertion is not documented there.
- Appendix A.1 labels a 100-task category distribution WorkArena despite the 18/100 WorkArena/WorkArena++ totals.
- Tables 9–12 repeat all-agent Table 8 contents despite agent-specific captions, including an impossible Llama-agent VWA condition.
- 'No judge above 70%' is supported for aggregate LLM precision, not every per-benchmark result or official rules.
- Broad claims of consistently underestimated rule rates and only two LLM exceptions are qualified by Table 6.
- Figure 1's visible comment does not display the requested discounted offer, despite a success label.

The page-9/10 conclusion wording also has awkward phrasing about rule-based agreement. The clear quantitative evidence is high relative precision with low recall, not a confidently reconstructed intended sentence. Verification here means rechecking supplied text against supplied visual tables and captions; no raw-data replication or external validation occurred.

## 15. Contributions and novelty

**Benchmark/dataset contribution [A]:** an expert-annotated collection of 1,302 trajectories from multiple agents across five benchmarks, assessed on success, side effects, and repetition. The authors claim this is the first benchmark assessing LLM judges for web agents; that priority claim is recorded but not externally verified. [pp. 1, 3–5]

**Methodological contribution [A]:** evaluate judges against expert reference labels rather than assuming official task rules are the definitive standard, and expose representation/model choices as comparison conditions. [pp. 3–7]

**Implementation contribution [A]:** a simplified judge that avoids separate captioning/change-summary models and supports textual or visual final-state representations, plus an annotation interface and shared agent-platform settings. Full implementation correctness cannot be audited without code. [pp. 6–7, 14–16]

**Empirical contribution [A/B]:** evaluator tradeoffs, benchmark-dependent judge rankings, input-ablation results, changing agent success-rate rankings, weak side-effect prediction, and strong-but-variable repetition prediction. [pp. 6–8, 17–18]

**Analytical contribution [A]:** four qualitative categories explaining judge failure. No new theoretical result, adversarial technique, security mitigation, or demonstrated downstream training improvement is reported. [pp. 8–9]

## 16. Limitations

### Authors' stated limitations and constraints

The authors explicitly report that no tested LLM judge exceeds 70% aggregate precision, limiting use for evaluation and selected training data. They describe failures involving subtle instruction details, action meaning, and incorrect agent reasoning. No single judge excels across all benchmarks. They state that environment-interacting evaluation may be infeasible when state cannot be preserved/shared. [pp. 6–9]

Collection constraints include AssistantBench's private test set, automation blocking on its default search homepage, Llama's lack of visual-input capability, two repeated environment timeouts, and omission of WorkArena++ Level 3 as too challenging. Annotation ambiguity and shared expert knowledge are discussed in Appendix A.2; lenient consensus is the stated response to ambiguous instructions. These are explicit constraints, although the authors do not organize them in a formal limitations section. [pp. 5, 14–15]

### Additional evidence-based analyst observations

Agreement is reported for one model/benchmark subset and one label, not for all annotations. Consensus and leniency can alter the reference definition of success. No class-prevalence counts, confusion matrices, confidence intervals, significance tests, seeds, hardware details, or judge inference settings are supplied. The qualitative error cases do not establish population frequencies. [D]

The prompt/method mismatch and duplicated appendix result tables reduce reproducibility and agent-specific interpretability. The representation ablation uses only GPT-4o Mini, so its explanation cannot be assumed to generalize to larger judges. No actual RFT/RL experiment measures the downstream consequences of false positives. Security relevance is indirect because no adversarial or standalone-model condition is tested. [D]

## 17. Threats to validity

These validity labels are analyst categories, not headings or admissions used by the authors.

**Internal validity [D]:** shared AgentLab settings reduce some implementation differences, but comparisons still mix backbone changes and representation pipelines. AER and NNetNav are modified from their original backbones. Unreported decoding/retry behavior and parser handling prevent isolating all causes of differences.

**Construct validity [D]:** expert task success is a useful operational target, but not the same construct as safe, authorized, or secure behavior. Side effects are separately labeled and poorly predicted. Lenient resolution of ambiguous instructions affects what counts as success. A judge seeing the evaluated agent's reasoning may be influenced by a persuasive but inaccurate account.

**External and ecological validity [D]:** the collection spans self-hosted, real-world, visual, and enterprise tasks, but comprises selected tasks and four custom agents. The results do not establish performance for arbitrary commercial agent products, unseen websites, current model versions, harder enterprise levels, or malicious environments. AssistantBench's altered initial search engine changes the execution setting.

**Statistical conclusion validity [D]:** descriptive percentage differences are clear, but small benchmark subsets and absent uncertainty estimates preclude claims that close rankings are stable or significant. The exact metric aggregation method and handling of undefined auxiliary scores are not explained.

**Reproducibility [D]:** task totals, split sizes, flags, prompts, platform names, and one precise agent version help, but code/data are not supplied here. Duplicate appendix tables and the fourth prompt question prevent complete reconstruction. The author-reported release URL is availability evidence, not verified access.

**Security generalizability [D]:** unintentional judge errors identify possible monitoring weaknesses; they do not quantify exploitation feasibility or establish that web agents are more vulnerable than standalone LLMs.

## 18. Future work and open questions

### A. Author-proposed directions

The authors call for more flexible automatic evaluation that reflects expert judgment, higher-precision judges, better reward models, and work addressing nuanced trajectory mistakes and misplaced agreement with agent reasoning. They position AgentRewardBench as infrastructure for selecting and improving judges and supporting future automatic evaluation/training pipelines. [A: pp. 7–10]

### B. Additional open questions

Analyst questions grounded in the supplied evidence include whether full-state histories or selective evidence improve verification; whether removing agent reasoning reduces false agreement; how to improve side-effect precision without losing recall; how stable per-benchmark rankings are under repeated runs; and how expert disagreement changes measured results. Raw confusion counts and correct agent-specific tables would be needed to answer several of these. [D]

For the user's security question, unresolved issues include whether deliberately manipulated webpage content or agent reasoning can cause judge approval, which observations an attacker could control, whether authorization checks are separate from success checks, and how the same backbone behaves in a standalone-chat condition. These are proposed questions, not observed attacks or paper-established causal explanations. [D: LOW confidence as direct security evidence]

## 19. Terminology and notation glossary

| Term | Meaning in this work |
|---|---|
| AgentRewardBench | Benchmark of expert-labeled web-agent trajectories used to test judges |
| LLM | Large language model; produces language completions used for actions or evaluations |
| VLM | Vision-language model; notation for multimodal completion with screenshot input |
| Web agent | Model-driven system that interacts with a browser to pursue a goal |
| Trajectory T | Ordered history of browser observations, reasoning, and actions |
| DOM | Document Object Model; structured webpage representation |
| A11Y | Accessibility tree representation rendered from the DOM |
| A / S | Final accessibility-tree / screenshot judge variant |
| AER | Agent Eval Refine; prior trajectory-judging framework |
| AER-C / AER-V | Caption-based / visual final-state variants of AER |
| NNetNav | Prior system's judge using observation-change summaries and a 1–5 rating |
| AB / WA / VWA | AssistantBench / WebArena / VisualWebArena |
| Work / Wk++ | WorkArena / WorkArena++ |
| RL | Reinforcement learning; learning guided by reward signals |
| RFT | Rejection finetuning; selecting judged-successful trajectories for training |
| Precision P | Correct positives divided by all predicted positives |
| Recall R | Auxiliary metric concerned with recovering positives; explicit formula not given |
| F1 | Auxiliary combined performance score; explicit formula not given |
| Side effect | Unnecessary action that could lead to unintended effects, independently of success |
| Repetition cycle | Action sequence that does not advance the goal |
| Grounding mismatch | Agent reasoning does not match actual webpage state |
| o_i / s_i | Observation / screenshot at step i |
| a_i / r_i | Executable browser action / reasoning at step i |
| B / E | Browser transition engine / completion execution parser |
| R / R_j | Agent / judge representation function |
| p_i / c_i | Model input representation / generated completion |
| g / Q | User goal / evaluation questions |
| A* / Â | Expert answers / predicted judge answers |
| use_som | AgentLab flag whose expansion is not specified in the supplied work |

## 20. Key numerical results

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| Unique tasks | 351 | tasks | Five benchmarks | Author-reported | p. 5 §3.2; p. 14 A.2 |
| Task split | 51 / 300 | tasks | Development / test | Author-reported | p. 5 §3.2 |
| Trajectories | 1,302 | trajectories | Four agent backbones | Author-reported | p. 5 §3.3 |
| Trajectory split | 196 / 1,106 | trajectories | Development / test | Author-reported | pp. 5, 14 |
| Binary annotations | 3,906 | labels | Three per trajectory | Author-reported | p. 5 |
| Annotators | 6 | experts | Research-experienced annotators | Author-reported | p. 4 |
| Agreement | 89.3 | % | Success; GPT-4o agent on WA | Author-reported | p. 6 |
| LLM judge configurations | 12 | configurations | Main comparison, excluding rules | Author-reported | pp. 1, 6 |
| Best overall LLM success P/R/F1 | 69.8 / 83.1 / 75.9 | % | GPT-4o(A) | Visually readable | T1 p. 6 |
| Official success P/R/F1 | 83.8 / 55.9 / 67.1 | % | Aggregate rule-based reference | Visually readable | T1 p. 6 |
| NNetNav success P/R/F1 | 52.5 / 82.4 / 64.1 | % | Modified Llama 3.3 implementation | Visually readable | T1 p. 6 |
| Highest LLM success recall | 89.8 | % | Qwen(A), aggregate | Visually readable | T1 p. 6 |
| False share among GPT-4o(A) approvals | 30.2 | % | 100−69.8; not all trajectories | Analyst-derived | T1 p. 6 |
| Rule missed share among expert positives | 44.1 | % | 100−55.9 under reported recall | Analyst-derived | T1 p. 6 |
| GPT-4o(A) recall advantage over rules | 27.2 | percentage points | 83.1−55.9 | Analyst-derived | T1 p. 6 |
| GPT-4o agent WA expert/rule success | 42.3 / 25.6 | % | Same agent, different evaluators | Visually readable | T3 p. 8 |
| WA rule shortfall | 16.7 | percentage points | 42.3−25.6 | Analyst-derived | T3 p. 8 |
| GPT-4o agent VWA expert/rule success | 35.9 / 17.4 | % | Same agent, different evaluators | Visually readable | T3 p. 8 |
| VWA rule shortfall | 18.5 | percentage points | 35.9−17.4 | Analyst-derived | T3 p. 8 |
| Best aggregate side-effect precision | 14.1 | % | Claude(S) | Visually readable | T7 p. 17 |
| GPT-4o(A) side-effect P/R/F1 | 7.7 / 91.7 / 14.2 | % | Aggregate side-effect label | Visually readable | T7 p. 17 |
| Claude(A) repetition P/R/F1 | 82.8 / 94.9 / 88.4 | % | Aggregate cycle detection | Visually readable | T7 p. 17 |
| Mini(S) repetition P/R/F1 | 92.3 / 18.5 / 30.8 | % | High precision, low recall | Visually readable | T7 p. 17 |
| Agent token limits | 40K / 8,192 | tokens | Maximum input / output | Author-reported | p. 14 A.1 |
| NNetNav rating threshold | 4 | rating threshold | Rating range 1–5 | Author-reported | p. 6 §4.1 |
| AssistantBench visited domains | 66 | domains | Counts range 1–129 | Author-reported | p. 14; T4 p. 16 |
| Llama timeout exclusions | 2 | tasks | WA task IDs 735 and 805 | Author-reported | p. 14 A.2 |

No approximate visual estimates are used for quantitative results. All numbers are textual labels or table entries; derived results disclose their operands.

## 21. Claim–evidence map

| Claim | Evidence | Figure/table/experiment | Source | Qualification / strength |
|---|---|---|---|---|
| Benchmark spans multiple agents and environments | 1,302 trajectories, four agent backbones, five benchmarks | X1 | pp. 1, 5, 14 | HIGH; sampling is selected, not exhaustive |
| Expert labels include outcome and process problems | Success, side effects, repetition questions | F2/F4, X1 | pp. 4, 14–16 | HIGH; prompt additionally asks unreported optimality |
| Simplified judging can improve aggregate success metrics | GPT-4o(A) 69.8/83.1/75.9 versus AER-C 67.7/71.9/69.7 | T1, X2 | p. 6 | HIGH descriptive; no significance test |
| Rules trade higher precision for lower recall | 83.8 precision, 55.9 recall | T1, X2 | pp. 6–7 | HIGH; benchmark-specific exceptions matter |
| No LLM judge wins every benchmark | Different per-benchmark precision leaders | T1/T8, X2 | pp. 6, 18 | HIGH descriptive; close rankings uncertain |
| Input evidence changes tradeoffs | Four Mini representation conditions | T2, X3 | pp. 7–8 | HIGH for values; MEDIUM for distraction explanation |
| Evaluator choice changes agent rankings | GPT-4o/Qwen ranking reversals on WA/Wk++ | T3/T6, X4 | pp. 8, 17 | HIGH; evaluator rates are not security rates |
| Judges can be misled by incorrect agent reasoning | Filter and wrong-grid-item examples | X5 | pp. 8–9 | HIGH for reported cases; frequency unknown |
| Incomplete operational tasks can be falsely approved | Cart addition judged as purchase | F3, X5 | p. 9 | HIGH; single non-adversarial example |
| Side-effect prediction is weak | Aggregate precision 6.6–14.1 | T7, X6 | p. 17 | HIGH descriptive; prevalence/cause unspecified |
| Agent-specific appendix evidence is unreliable as supplied | T9–T12 repeat T8 despite captions | T8–T12 | pp. 18–22 | HIGH observable inconsistency; origin unknown |
| Security relevance is indirect | Executable actions, independent side effects, false approvals | Framework/X5/X6 | pp. 3–4, 8–9, 17 | MEDIUM inference; no standalone-LLM comparison |

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an AI to shop online. It can search, click a product, add it to a cart, and tell you what it did. Another AI checks whether the job is finished. The important question is whether the checker looks carefully at what happened or simply believes the first AI's explanation.

This paper collects many browser-task histories and has experts mark what really happened. The researchers then test AI checkers and fixed computer rules. The AI checkers find more genuine successes, but they also approve many failures. The fixed rules are more careful about approval overall, but they reject many tasks that experts consider successful. Changing the checker can even change which agent looks best.

One example asks an agent to buy cereal. It adds cereal to the cart and stops. The checker says the purchase succeeded, even though adding something to a cart is not the same as buying it. Other examples show a checker trusting incorrect reasoning or overlooking an important final action. The paper also finds that detecting unwanted side effects is difficult.

For security, this suggests an important question: if an AI can take actions on websites, how do we verify both what it accomplished and whether it caused unwanted changes? This paper helps expose weaknesses in that verification. It does not prove that browser agents are more vulnerable than ordinary chatbots, because it does not attack either group or compare their security under the same conditions.

## Completeness Audit

Coverage is judged against the supplied inventory, not the length of this explanation. 'Represented in compressed form' means the object was inspected and its important role/findings retained, but not every sentence or cell was reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| ABS abstract | Yes, text and image | Yes | Fully represented | Exact dataset total retained |
| S1 introduction | Yes, text and images | Yes | Represented in compressed form | Motivation, example, questions preserved |
| S2 related works | Yes, text and images | Yes | Represented in compressed form | Three categories and attributed contrasts retained |
| S3 benchmark overview | Yes | Yes | Fully represented | Dataset, collection, evaluation role |
| SS31 trajectory definition | Yes, visual notation | Yes | Fully represented | E1–E7 and symbol caveats |
| SS31 annotation design/setup | Yes | Yes | Fully represented | Three labels, six experts, evidence access |
| SS31 judge model | Yes | Yes | Fully represented | Predicted answers and judge representation |
| SS32 tasks/environments | Yes; p. 5 text-only | Yes | Fully represented | Five benchmarks, task counts, scope |
| SS33 agents/platform/splits | Yes; p. 5 text-only | Yes | Fully represented | Model roles, version, exclusions, splits |
| SS33 agreement | Yes | Yes | Fully represented | Subset and unspecified sample size flagged |
| SS41 AER | Yes | Yes | Fully represented | Caption/vision inputs and changed backbone |
| SS41 NNetNav | Yes | Yes | Fully represented | Summaries, rating, threshold, changed backbone |
| SS41 simplified judge | Yes | Yes | Fully represented | A/S conditions and prompt mismatch |
| SS42 metrics | Yes | Yes | Fully represented | Precision definition and rationale; missing formulas noted |
| SS43 overall performance | Yes | Yes | Fully represented | Primary triples and conditional maxima |
| SS43 input ablation | Yes | Yes | Fully represented | Every T2 numerical result retained |
| S5 success-rate analysis | Yes | Yes | Fully represented | Ranking changes, point differences, exceptions |
| S6 grounding mismatch | Yes | Yes | Fully represented | Wrong grid-item case |
| S6 misleading reasoning | Yes | Yes | Fully represented | Unapplied filter case |
| S6 missed instruction details | Yes | Yes | Fully represented | Incomplete purchase case |
| S6 action-intent misunderstanding | Yes | Yes | Fully represented | Travel-time/infeasible-response case |
| S7 conclusion | Yes; p. 10 text-only | Yes | Represented in compressed form | Findings and awkward sentence qualified |
| Acknowledgments | Yes, p. 10 text-only | Yes | Represented in compressed form | Funding acknowledged; detailed thanks secondary |
| References | Yes; pp. 12–13 text-only | Yes | Inspected but deliberately compressed | Bibliographic entries not externally checked |
| RQ1 | Yes | Yes | Fully represented | Success-judging reliability |
| RQ2 | Yes | Yes | Fully represented | Comparative judge capability |
| Formal hypotheses | No supplied object | Yes, absence stated | Not present in supplied material | No hypothesis invented |
| X1 construction/agreement | Yes | Yes | Fully represented | Counts reconciled with derived arithmetic |
| X2 judge comparison | Yes | Yes | Fully represented | Aggregate and benchmark-specific evidence |
| X3 ablation | Yes | Yes | Fully represented | One-model scope preserved |
| X4 success-rate comparison | Yes | Yes | Fully represented | T6 complete rate triples |
| X5 qualitative errors | Yes | Yes | Fully represented | No category prevalence claimed |
| X6 auxiliary-label evaluation | Yes | Yes | Represented in compressed form | T7 complete; T8 selected patterns |
| F1 example trajectory | Yes, visually | Yes | Fully represented with uncertainty | Discounted-offer mismatch flagged |
| F2 creation diagram | Yes, visually | Yes | Fully represented | Inputs, arrows, annotation outputs |
| F3 purchase error | Yes, visually | Yes | Fully represented | Caption corroborates cart/purchase distinction |
| F4 annotation interface | Yes, visually | Yes | Represented in compressed form | Tiny UI details not treated as exact evidence |
| F5 system prompt | Yes, visually | Yes | Fully represented in substance | Four questions; tags and input discrepancy |
| F6 user prompt | Yes, visually | Yes | Fully represented in substance | History fields and final-state placeholders |
| T1 main comparison | Yes, visually | Yes | Fully represented | Overall triples in T7; per-benchmark leaders |
| T2 ablation | Yes, visually | Yes | Fully represented | All cells retained |
| T3 selected success rates | Yes, visually | Yes | Fully represented | Rates retained through T6; Llama placeholder noted |
| T4 website visits | Yes, visually | Yes | Represented in compressed form | Top counts/range; low-frequency names compressed |
| T5 settings | Yes, visually | Yes | Fully represented | All enabled/disabled flags retained |
| T6 expanded success rates | Yes, visually | Yes | Fully represented | All triples retained |
| T7 aggregate auxiliary metrics | Yes, visually | Yes | Fully represented | All triples and missing-value notation retained |
| T8 benchmark metrics | Yes, visually | Yes | Represented in compressed form | Key extremes/tradeoffs; many cells not retranscribed |
| T9 Qwen-captioned table | Yes, visually | Yes | Uncertain; duplicated content compressed | Not accepted as independent agent-specific evidence |
| T10 Llama-captioned table | Yes, visually | Yes | Uncertain; duplicated content compressed | VWA contradiction retained |
| T11 Claude-captioned table | Yes, visually | Yes | Uncertain; duplicated content compressed | Same matrix as T8 |
| T12 GPT-4o-captioned table | Yes, visually | Yes | Uncertain; duplicated content compressed | Same matrix as T8 |
| E1 browser transition | Yes | Yes | Fully represented | Determinism not inferred |
| E2 trajectory sequence | Yes | Yes | Fully represented | Order and final observation explained |
| E3 representation | Yes | Yes | Fully represented | Abstract history versus flag caveat |
| E4 completion | Yes | Yes | Fully represented | LM/VLM and screenshot |
| E5 parser | Yes | Yes | Fully represented | Action/reasoning output and missing error handling |
| E6 annotation answers | Yes | Yes | Fully represented | Browser-action notation distinguished |
| E7 judge representation | Yes | Yes | Fully represented | Extraction artifact flagged |
| Numbered algorithms/theorems | No supplied object | Yes, absence stated | Not present in supplied material | Functional workflow is explained instead |
| Main contributions | Yes | Yes | Fully represented | Benchmark, method, implementation, empirical analysis |
| Author-stated limitations/constraints | Yes | Yes | Fully represented | Separate from analyst validity observations |
| A.1 environment details | Yes | Yes | Fully represented except secondary domain enumeration | Sampling, engine substitution, limits, flags |
| A.2 annotations | Yes | Yes | Fully represented | Filtering, interface, expert knowledge, consensus |
| A.3 judges | Yes | Yes | Fully represented with uncertainty | Ten/twelve and prompt/table discrepancies |
| Standalone supplementary files | Not supplied | No | Missing from supplied material | No files claimed reviewed |
| Dataset/code/raw trajectories | Not supplied | No | Missing from supplied material | Release address not accessed |
| Standalone-LLM security comparison | Not present | Absence and relevance addressed | Not studied by this paper | Security inference explicitly limited |

### Missing or inaccessible material

No numbered text page within 1–23 is missing. Images of pages 5, 10, 12, and 13 were not supplied, so visual layout on those pages cannot be audited. Raw annotations, dataset files, source code, task manifests, full trajectory recordings, exact per-condition prompt variants, correct independent agent-specific result matrices, and any separately distributed supplementary artifact were not available. The release website was not inspected. No actual standalone-model security comparison or adversarial experiment is contained in the supplied study.

### Uncertain interpretations

Unresolved issues are the WorkArena category label, twelve-versus-ten judge count, three-versus-four judgment dimensions, first/last screenshot insertion, duplicated Tables 9–12, the Llama VWA placeholder, Figure 1's absent visible discounted offer, aggregate metric weighting, AB fractional official rates, and behavior when auxiliary precision/recall denominators are zero. Tiny browser details in Figures 1/3/4 are not used as exact evidence. The supplied material cannot establish the provenance of the duplicated tables.

### Deliberately compressed material

Related-work citations, the complete bibliography, acknowledgments, low-frequency website names in Table 4, numerous intermediate per-benchmark auxiliary cells in Table 8, and duplicated Tables 9–12 are compressed. Prompt wording is explained structurally rather than reproduced wholesale. No low-frequency domain is silently used to make a claim about agent success or security. Repeated page headers and decorative symbols are non-substantive apart from identifying publication status or illustrating approval/error.

### Potential omissions

Every identified substantive section, subsection, question, experiment, figure, table, equation family, contribution, and explicit limitation/constraint is represented or marked uncertain/missing. This is not a verbatim replacement for the paper: many Table 8 cells and bibliographic/domain details are intentionally not retranscribed. No additional substantive inventory item is known to be wholly unrepresented. Completeness of unavailable code/data/supplements cannot be assessed, and the supplied inconsistencies prevent a fully verified reconstruction of agent-specific results.
