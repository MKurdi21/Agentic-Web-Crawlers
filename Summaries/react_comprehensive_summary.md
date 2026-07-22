# ReAct: Synergizing Reasoning and Acting in Language Models

**Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao  
**Affiliations:** Princeton University and Google Research, Brain Team  
**Publication:** ICLR 2023 conference paper

## 1. Background and Context

Large language models had shown two important capabilities that were mostly studied separately:

- **Reasoning:** Producing intermediate verbal steps, especially through chain-of-thought prompting.
- **Acting:** Producing plans or commands that interact with an external system, such as a website, knowledge base, or simulated environment.

The paper argues that human intelligence combines these capabilities continuously. While carrying out a task, people reason to track progress, plan the next step, handle exceptions, and recognize when more information is needed. They also act—such as checking a source or inspecting an object—to obtain information that improves subsequent reasoning.

Existing chain-of-thought methods are comparatively static and rely on the model’s internal representations. They cannot directly verify facts or update their knowledge from the outside world. Consequently, an early hallucination can propagate through the rest of a reasoning chain.

Conversely, existing language-model agents typically predict domain-specific actions without explicitly maintaining high-level plans or verbal working memory. They may act without understanding what has already happened, what remains to be done, or why an action failed.

The paper addresses the missing connection between these two areas: whether a language model can reason and act in an interleaved, mutually supporting way and whether doing so systematically improves both knowledge reasoning and interactive decision-making.

## 2. Research Goal and Objectives

The main goal is to introduce and evaluate **ReAct**, a prompting paradigm in which a language model alternates between:

- **Thoughts:** Free-form verbal reasoning that does not alter the environment.
- **Actions:** Task-specific commands that interact with the environment.
- **Observations:** Feedback returned by the environment after an action.

The authors seek to demonstrate that:

1. Reasoning can guide more purposeful and successful actions.
2. External actions can ground reasoning in retrieved or observed facts.
3. Combining the two can outperform reasoning-only and acting-only approaches.
4. Explicit reasoning traces can make agents more interpretable, diagnosable, trustworthy, and controllable.
5. ReAct can generalize across knowledge reasoning, fact verification, household simulation, and web navigation using only a few in-context examples.
6. ReAct can benefit from fine-tuning when small models have difficulty learning the combined behavior from prompts alone.

## 3. Methods (Approach/Design)

### 3.1 ReAct formulation

At each time step, an agent receives an environmental observation and chooses an action based on its accumulated context. ReAct expands the ordinary action space by adding the space of natural-language thoughts.

A thought changes the agent’s context but does not affect the external environment and therefore produces no environmental observation. It can nevertheless support later reasoning or action by:

- Decomposing a goal into subgoals.
- Creating or revising an action plan.
- Extracting important facts from an observation.
- Applying commonsense or arithmetic reasoning.
- Tracking completed and pending subgoals.
- Reformulating a failed search.
- Handling exceptions.
- Synthesizing the final answer.

For knowledge-intensive tasks, thoughts and actions are generated densely in alternating **thought–action–observation** steps. For long-horizon decision tasks, thoughts appear only at strategically useful points, and the model decides when to think.

Most experiments use a frozen **PaLM-540B** model with few-shot prompting. Additional experiments use GPT-3 `text-davinci-002`. Smaller PaLM-8B and PaLM-62B models are tested in prompting and fine-tuning settings.

### 3.2 Benchmarks

The method is evaluated on four domains:

1. **HotpotQA:** Multi-hop question answering requiring reasoning across two or more Wikipedia passages.
2. **FEVER:** Fact verification, with labels SUPPORTS, REFUTES, or NOT ENOUGH INFO.
3. **ALFWorld:** A synthetic text-based household environment with six task types and potentially more than 50 locations and 50 expert actions per instance.
4. **WebShop:** A simulated online store containing 1.18 million real products and 12,000 human-written shopping instructions.

HotpotQA and FEVER use a question-only setting: models receive no supporting passages and must rely on internal knowledge or retrieve evidence.

### 3.3 Wikipedia action environment

The knowledge tasks use a deliberately simple Wikipedia interface with three actions:

- `search[entity]`: Returns the first five sentences of the entity’s page, or five similar entity suggestions if the exact page is unavailable.
- `lookup[string]`: Returns the next sentence on the current page containing the specified string, resembling browser “find.”
- `finish[answer]`: Ends the episode and submits an answer.

This interface is weaker than state-of-the-art lexical or neural retrieval systems. It is intended to simulate explicit human-like information seeking and make successful retrieval depend on reasoning.

### 3.4 Knowledge-task prompts and baselines

For HotpotQA and FEVER, the authors randomly selected respectively **six and three training examples** and manually wrote complete ReAct trajectories. More examples did not improve performance.

The comparison methods were derived by ablating the same demonstrations:

- **Standard:** Direct answer prompting, with thoughts, actions, and observations removed.
- **CoT:** Reasoning-only chain-of-thought prompting.
- **CoT-SC:** Self-consistent chain of thought, sampling 21 trajectories at temperature 0.7 and selecting the majority answer.
- **Act:** Acting only, with thoughts removed.
- **ReAct:** Interleaved thoughts, actions, and observations.

Two hybrid methods combine internal model knowledge with external retrieval:

- **ReAct → CoT-SC:** If ReAct fails to answer within seven HotpotQA steps or five FEVER steps, use CoT-SC.
- **CoT-SC → ReAct:** If the majority answer among \(n\) CoT samples occurs fewer than \(n/2\) times, treat internal knowledge as insufficiently confident and switch to ReAct.

Longer ReAct limits were not useful: among correct trajectories, only **0.84%** of HotpotQA examples used seven steps and **1.33%** of FEVER examples used five.

### 3.5 Fine-tuning

The authors bootstrapped **3,000 correctly answered generated trajectories** for each method and fine-tuned PaLM-8B and PaLM-62B to generate complete trajectories conditioned on questions or claims.

All fine-tuning used a batch size of 64:

- PaLM-8B: ReAct and Act for 4,000 steps; Standard and CoT for 2,000.
- PaLM-62B: ReAct and Act for 4,000 steps; Standard and CoT for 1,000.

ReAct and Act generally benefited from additional training, whereas Standard and CoT began degrading relatively early.

### 3.6 ALFWorld design

ALFWorld contains six task categories: **Pick, Clean, Heat, Cool, Look, and Pick Two**. The agent navigates a simulated household and manipulates objects using text commands.

For each task type, the authors manually annotated three training trajectories with sparse thoughts that:

- Decompose the overall goal.
- Track subgoal completion.
- Select the next subgoal.
- Use commonsense to identify likely object locations and appropriate actions.

Evaluation used **134 unseen games** in a task-specific setting. Six prompts per task type were created from every ordered selection of two trajectories from the three annotations. Act used the same demonstrations with thoughts removed, providing a controlled comparison.

The main prior baseline was **BUTLER**, an imitation-learning agent trained on \(10^5\) expert trajectories per task type. A GPT-2 method trained on 3,553 instances across all task types was excluded because it did not match the task-specific comparison.

The authors also constructed **ReAct-IM**, an Inner-Monologue-style ablation containing dense external-state feedback but lacking several forms of internal reasoning: recognizing completed subgoals, selecting the next subgoal, and using pretrained commonsense to locate objects.

### 3.7 WebShop design

WebShop asks agents to purchase products satisfying natural-language constraints. It contains noisy structured and unstructured text, including titles, descriptions, product options, and prices.

Evaluation used **500 test instructions** and two measures:

- **Score:** Average percentage of desired attributes satisfied.
- **Success rate:** Percentage of episodes satisfying every requirement.

Act prompts supplied search, product-selection, option-selection, and purchase actions. One-shot ReAct added thoughts about what to explore, which product attributes matter, and when an item is suitable to buy.

Baselines included:

- Imitation learning trained on **1,012 human trajectories**.
- Imitation plus reinforcement learning using an additional **10,587 training instructions**.

## 4. Results and Findings

### 4.1 Figure 1: Why reasoning and acting need each other

Figure 1 contrasts the approaches on HotpotQA and ALFWorld.

In the HotpotQA example, the question asks what device besides the Apple Remote can control the software the remote was originally designed for:

- Standard answers “iPod,” incorrectly.
- CoT hallucinates that the relevant program was Apple TV and answers with iPhone, iPad, and iPod Touch.
- Act retrieves information about Apple Remote and Front Row but cannot reason from it to the answer, eventually submitting “yes.”
- ReAct discovers that Apple Remote was designed for Front Row, reformulates a failed search as “Front Row (software),” retrieves the relevant description, and answers **keyboard function keys**.

In ALFWorld, the task is to put a pepper shaker on a drawer:

- Act opens the drawer, searches an unrelated sink basin, and repeatedly tries to take an object that is not there.
- ReAct first reasons about likely pepper-shaker locations, searches systematically, finds it on countertop 3, picks it up, recognizes that the destination drawer is closed, opens it, and completes the placement.

The examples illustrate “reason to act” and “act to reason”: thought supports planning and recovery, while action supplies facts and feedback.

### 4.2 Table 1: HotpotQA and FEVER prompting

PaLM-540B results were:

| Method | HotpotQA exact match | FEVER accuracy |
|---|---:|---:|
| Standard | 28.7 | 57.1 |
| CoT | 29.4 | 56.3 |
| CoT-SC | 33.4 | 60.4 |
| Act | 25.7 | 58.9 |
| ReAct | 27.4 | 60.9 |
| CoT-SC → ReAct | 34.2 | **64.6** |
| ReAct → CoT-SC | **35.1** | 62.0 |
| Supervised state of the art | 67.5 | 89.5 |

ReAct consistently outperformed Act, showing that reasoning improves action selection and final-answer synthesis.

Relative to ordinary CoT:

- ReAct was better on FEVER: **60.9 versus 56.3**.
- ReAct was slightly worse on HotpotQA: **27.4 versus 29.4**.

The best prompting result was the hybrid ReAct → CoT-SC on HotpotQA and CoT-SC → ReAct on FEVER. Nevertheless, every prompting method remained far below the supervised state of the art.

### 4.3 Figure 2: Number of CoT self-consistency samples

Figure 2 plots HotpotQA exact match and FEVER accuracy against the number of CoT-SC samples.

Both ReAct/CoT hybrid methods consistently surpassed plain CoT-SC across sample counts. They reached approximately the performance of a **21-sample CoT-SC ensemble using only about three to five CoT samples**.

The advantage was task-dependent:

- ReAct → CoT-SC was strongest on HotpotQA.
- CoT-SC → ReAct was strongest on FEVER.

This supports using internal knowledge when it is effective and external retrieval when the model is uncertain or its initial procedure fails.

### 4.4 Table 2: Human analysis of success and failure modes

The authors manually studied 50 correct and 50 incorrect trajectories from each of ReAct and CoT on HotpotQA—**200 trajectories total**.

Among successful trajectories:

| Success type | ReAct | CoT |
|---|---:|---:|
| True positive: correct reasoning and facts | 94% | 86% |
| False positive: hallucinated reasoning or facts | 6% | 14% |

Among failures:

| Failure type | ReAct | CoT |
|---|---:|---:|
| Reasoning error | 47% | 16% |
| Unhelpful or empty search result | 23% | Not applicable |
| Hallucination | 0% | 56% |
| Label ambiguity | 29% | 28% |

Thus, CoT’s main weakness was hallucination. ReAct was more fact-grounded and trustworthy, but its imposed thought–action–observation structure made reasoning less flexible. ReAct sometimes repeated earlier thoughts and actions and failed to escape a loop. Uninformative search results also caused 23% of its failures and were difficult to recover from.

Appendix examples illustrate these categories. ReAct correctly grounds answers such as identifying Bill Clinton through retrieved information. Its false positives can still arise when it searches the wrong entity. Reasoning errors include following a long, inefficient list of entities rather than locating the required relationship. CoT examples include incorrect age comparisons and unsupported dates. Some apparent failures came from labels that differed in specificity from otherwise reasonable answers.

### 4.5 Figure 3: Prompting versus fine-tuning at different scales

Figure 3 compares Standard, CoT, Act, and ReAct on HotpotQA for PaLM-8B, PaLM-62B, and PaLM-540B prompting, and for PaLM-8B and PaLM-62B fine-tuning.

The plotted prompting values for PaLM-540B correspond to Table 1: Standard 28.7, CoT 29.4, Act 25.7, and ReAct 27.4. For smaller prompted models, ReAct is visibly the weakest or among the weakest; the plotted bars are approximately:

- PaLM-8B: Standard about 16, CoT about 13, Act about 6, ReAct about 5.
- PaLM-62B: Standard about 21, CoT and Act about 23, ReAct about 17.

Exact smaller-model bar values are not printed in the supplied text, so these are visual approximations.

After fine-tuning on 3,000 trajectories, the ordering reverses. ReAct becomes best:

- Fine-tuned PaLM-8B ReAct is approximately 25 exact match and outperforms all PaLM-62B prompting methods.
- Fine-tuned PaLM-62B ReAct is approximately 33 and outperforms all PaLM-540B prompting methods.
- Act is also substantially improved by fine-tuning, while Standard and CoT remain weaker.

The authors interpret this as evidence that prompting small models to learn both thought and action from a few examples is difficult, but training on trajectories teaches a reusable skill: how to reason and retrieve information rather than merely memorize potentially hallucinated facts.

### 4.6 Table 3: ALFWorld success rates

Task-specific success rates were:

| Method | Pick | Clean | Heat | Cool | Look | Pick Two | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| Act, best of 6 | 88 | 42 | 74 | 67 | 72 | 41 | 45 |
| ReAct, average | 65 | 39 | 83 | 76 | 55 | 24 | 57 |
| ReAct, best of 6 | **92** | 58 | **96** | 86 | **78** | 41 | **71** |
| ReAct-IM, average | 55 | 59 | 60 | 55 | 23 | 24 | 48 |
| ReAct-IM, best of 6 | 62 | **68** | 87 | 57 | 39 | 33 | 53 |
| BUTLER-g, best of 8 | 33 | 26 | 70 | 76 | 17 | 12 | 22 |
| BUTLER, best of 8 | 46 | 39 | 74 | **100** | 22 | 24 | 37 |

The best ReAct prompt achieved **71% overall success**, compared with **45%** for the best Act prompt and **37%** for BUTLER. The abstract describes this as a 34-point absolute advantage over the prior learning baseline.

Even the worst ReAct trial, at **48%**, exceeded the best Act and BUTLER trials. Across the six controlled prompt trials, ReAct’s relative gain over Act ranged from **33% to 90%**, averaging **62%**.

ReAct outperformed ReAct-IM overall, **71% versus 53%**, and on five of six task types. ReAct-IM’s dense external feedback did not adequately support high-level goal decomposition, deciding when a subgoal had finished, choosing the next subgoal, or using commonsense to locate objects.

### 4.7 ALFWorld trajectory evidence

The appendices compare three agents on cleaning a knife and placing it on a countertop:

- ReAct explicitly decomposes the task into finding, taking, cleaning, and placing. It searches likely locations, finds the knife on countertop 2, travels to the sink, cleans it, and places it on countertop 1.
- Act finds and takes the knife but attempts to clean it without first going to the sink. It then repeatedly revisits countertops and retries invalid actions.
- ReAct-IM incorrectly frames the task as finding an already clean knife. It picks up an uncleaned knife, places it on a countertop, and repeatedly attempts the same placement instead of repairing the missing cleaning step.

These trajectories show that useful reasoning must represent task state and subgoal transitions, not merely repeat the current objective.

### 4.8 Table 4: WebShop results

| Method | Average score | Success rate |
|---|---:|---:|
| Act | 62.3 | 30.1% |
| ReAct | **66.6** | **40.0%** |
| Imitation learning | 59.9 | 29.1% |
| Imitation + reinforcement learning | 62.4 | 28.7% |
| Human expert | 82.1 | 59.6% |

One-shot Act was already comparable to the trained IL and IL+RL systems. ReAct’s sparse reasoning increased success to **40.0%**, an absolute improvement of about **10 percentage points** over the previous best success rate.

ReAct more effectively connected noisy product text to user constraints. In the Appendix Table 10 example, Act selects an $85 strawberry-banana product for a request requiring an apple-cinnamon 16-pack under $50 and scores **0.125**. ReAct rejects mismatched results, opens a $12.99 product with configurable flavor and pack size, selects “apple cinnamon” and “pack of 16,” and scores **1.0**.

ReAct remained well below expert humans. Humans searched more products and reformulated queries more often, behaviors that prompting-based agents still found difficult.

### 4.9 Figure 4: Current information versus outdated labels

Figure 4 presents a HotpotQA question about the number of rooms in the hotel hosting the Cirque du Soleil show *Mystère*.

- The dataset label is **2,664**.
- Standard answers **3,000**.
- CoT hallucinates or recalls **2,885**.
- Act searches but fails to complete the chain and returns no answer.
- ReAct identifies Treasure Island Hotel and Casino, retrieves **2,884 rooms and 220 suites**, adds them, and answers **3,104**.

The authors classify the ReAct answer as reasonable and up to date, even though it does not match the old dataset label. The example demonstrates that exact-match evaluation can count current, evidence-based answers as wrong when benchmark labels have become outdated.

### 4.10 Table 5: GPT-3 generalization

ReAct prompting was also tested with GPT-3 `text-davinci-002` using greedy decoding:

| Task | PaLM-540B | GPT-3 |
|---|---:|---:|
| HotpotQA exact match | 29.4 | **30.8** |
| ALFWorld success rate | 70.9% | **78.4%** |

HotpotQA used a random subset of 500 validation questions. ALFWorld used all 134 unseen tasks and the prompt set selected as best under PaLM-540B.

GPT-3 consistently outperformed PaLM-540B, possibly because it was fine-tuned for following human instructions. The experiment indicates that ReAct is not specific to a single language model.

### 4.11 Figure 5: Human correction by editing thoughts

Figure 5 shows an ALFWorld task requiring two keychains to be placed in a safe.

In the original trajectory, ReAct finds keychain 3 in drawer 4 but hallucinates that keychain 2 is also there. It later returns and repeatedly tries to take a nonexistent keychain.

A human removes the hallucinated belief in the thought at Act 17 and edits the later thought at Act 23 to suggest likely locations such as a dresser, garbage can, safe, side table, sofa, or shelves. The agent then searches dresser 1, finds keychain 2, takes it, and places it in the safe successfully.

Only two thought edits replace what would otherwise require manually specifying many actions. The authors argue that thought editing can modify beliefs, plans, or reasoning style during execution, whereas editing isolated actions may not change the agent’s later behavior.

### 4.12 Prompt examples in the appendices

The full prompts demonstrate how ReAct behavior is taught without a specialized formal reasoning language:

- HotpotQA examples teach question decomposition, entity search, lookup, search reformulation, comparison, and final answer synthesis.
- FEVER examples teach the model to retrieve evidence and distinguish contradiction from insufficient information.
- The WebShop prompt adds short evaluations of which product and options satisfy the instruction.
- The ALFWorld ReAct prompt explicitly predicts likely object locations and marks transitions between finding, taking, cleaning, and placing.
- The ReAct-IM prompt repeatedly restates the current subgoal but lacks the richer commonsense and progress-tracking thoughts used by ReAct.

## 5. Analysis and Interpretation

The experiments support a complementary relationship between reasoning and acting.

### Acting improves reasoning

External retrieval reduces dependence on unsupported internal memories. This was particularly helpful on FEVER, where very small factual differences can determine whether a claim is supported or refuted. CoT’s hallucinations accounted for 56% of its analyzed failures, whereas no ReAct failure in the sampled analysis was categorized as hallucination.

External evidence also improves transparency: a reader can distinguish facts retrieved from Wikipedia from conclusions produced by the model.

### Reasoning improves acting

Act-only agents often retrieve the wrong entity, fail to synthesize observations, lose track of task state, or repeat impossible commands. ReAct thoughts help specify:

- Why an action is needed.
- What information is missing.
- How a failed search should be reformulated.
- Which subgoal has been completed.
- What should happen next.

This advantage appears consistently in knowledge retrieval, household interaction, and product navigation.

### Neither reasoning source is sufficient alone

ReAct’s grounding can reduce flexibility. It may become trapped by an unhelpful search or rigid trajectory format. CoT can formulate effective reasoning structures but invent facts. The hybrid results show that the best system can use both:

- Internal knowledge and flexible reasoning when confidence is high.
- External retrieval when confidence is low or an initial procedure fails.

### Sparse, flexible thought is more useful than constant feedback

ALFWorld’s ReAct-IM ablation shows that merely inserting frequent statements about external state is not equivalent to reasoning. High-level decomposition, commonsense knowledge, progress tracking, and flexible subgoal selection are central to ReAct’s improvement.

### Fine-tuning changes the scaling picture

Few-shot ReAct prompting is demanding for small models because they must learn two forms of behavior at once. However, when trained on correct trajectories, smaller models can learn the combined skill effectively. Fine-tuned PaLM-62B ReAct surpassing all PaLM-540B prompt methods suggests that trajectory training can be more valuable than relying only on greater model scale.

### Interpretability and control

The verbal traces allow people to inspect why an agent selected an action and identify hallucinated beliefs, loops, or failed subgoal transitions. Figure 5 further shows that these traces can serve as an interface for real-time correction.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- It introduces **ReAct**, a general prompting paradigm that interleaves natural-language reasoning with environment-specific actions.
- It formalizes verbal thoughts as additions to an agent’s action space that modify context without directly changing the environment.
- It demonstrates the approach across four substantially different tasks: question answering, fact verification, household simulation, and online shopping.
- It shows consistent advantages over acting-only models and competitive or superior performance relative to reasoning-only prompting.
- It introduces hybrid ReAct/CoT-SC procedures that combine internal and externally retrieved knowledge.
- It provides systematic behavioral analysis showing that ReAct reduces hallucination but can introduce search dependence and reasoning rigidity.
- It demonstrates that sparse internal reasoning is more effective than dense external-feedback-style monologue for long-horizon action.
- It reports initial fine-tuning evidence that ReAct can become especially effective when learned from generated trajectories.
- It shows cross-model applicability using both PaLM-540B and GPT-3.
- It presents thought editing as a potential mechanism for human inspection, correction, and collaboration during execution.

## 7. Limitations and Caveats

- **Prompt length:** Complex tasks with large action spaces may require many demonstrations, but these can exceed the context limits of in-context learning.
- **Small-model prompting difficulty:** PaLM-8B and PaLM-62B struggle to infer combined reasoning and acting from a few examples.
- **Annotation cost:** ReAct demonstrations require human-written thoughts and actions. The fine-tuning experiments partly address this through bootstrapping, but the authors still identify high-quality human data as desirable.
- **Restricted retrieval:** The Wikipedia interface retrieves only short snippets through exact entity searches and string lookup. Uninformative results caused 23% of analyzed ReAct failures.
- **Reasoning rigidity:** The structured interleaving can make ReAct less flexible than CoT and produces more reasoning errors in the HotpotQA analysis: 47% versus 16%.
- **Loops:** ReAct sometimes repeats previous thoughts and actions instead of selecting a new step. The authors suspect greedy decoding may contribute and suggest that methods such as beam search might help.
- **Benchmark-label problems:** Some HotpotQA labels are ambiguous or outdated. Exact match may therefore penalize reasonable current answers.
- **Performance remains below specialized systems and humans:** Prompting results are far below supervised state-of-the-art knowledge systems, and WebShop ReAct remains far below expert human performance.
- **Limited exploration and query reformulation:** Prompted WebShop agents do less product exploration and search reformulation than humans.
- **Prompt sensitivity:** ALFWorld performance varies across prompt selections, although ReAct beats controlled Act prompts in all six trials.
- **Model accessibility and reproducibility:** The main experiments use PaLM, which was not openly accessible. The paper supplies prompts, GPT-3 experiments, and GPT-3 code to mitigate this.
- **No real purchases or unrestricted web actions:** WebShop is a benchmark environment rather than a live purchasing system.
- **Safety concerns:** Giving a language model external actions can create risks such as accessing inappropriate or private information or taking harmful actions. These experiments restrict agents to Wikipedia, WebShop, and safe predefined action spaces; the agents cannot edit Wikipedia or actually buy products.
- **Limited human-editing evidence:** Human-in-the-loop correction is demonstrated through an example rather than a systematic evaluation.
- **No statistical significance tests are reported:** Performance differences are reported as scores, success rates, or controlled trial comparisons rather than p-values or confidence intervals.

## 8. Future Work or Open Questions

The authors identify several directions:

- Fine-tune ReAct on more high-quality human-written reasoning-and-action trajectories.
- Scale ReAct through multi-task training so that a single agent can operate across more domains.
- Combine ReAct with reinforcement learning and human feedback.
- Develop better decoding procedures, potentially including beam search, to reduce repetitive loops.
- Improve the agent’s ability to explore products and reformulate web queries.
- Study human thought editing more systematically as a mechanism for alignment, correction, and human–machine collaboration.
- Investigate how to scale demonstrations for complex action spaces without exceeding context limits.
- Design broader interactive systems while explicitly managing privacy, inappropriate-information access, and harmful-action risks.
- Improve the combination of internal reasoning and external evidence so the system can switch between them more reliably.

## 9. High-Level Takeaway (Plain Language)

ReAct teaches a language model to alternate between thinking and doing. Instead of answering entirely from memory or blindly issuing commands, the model writes down what it needs to accomplish, takes an action such as searching Wikipedia or examining a virtual room, reads the result, and updates its plan.

Across question answering, fact checking, household tasks, and online shopping, this combination generally made actions more purposeful and reasoning more grounded. It reduced hallucination, produced understandable decision traces, and allowed people to correct behavior by editing thoughts. The method is not yet as strong as specialized supervised systems or expert humans, and it can still fail because of poor searches, rigid reasoning, or loops, but the experiments show that reasoning and interaction work better together than either capability does alone.