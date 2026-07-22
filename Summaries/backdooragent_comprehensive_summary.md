# BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents

**Authors:** Yunhao Feng, Yige Li, Yutao Wu, Yingshui Tan, Yanming Guo, Yifan Ding, Kun Zhai, Xingjun Ma, and Yu-Gang Jiang  
**Venue:** Findings of the Association for Computational Linguistics (ACL 2026), pp. 16115–16127

## 1. Background and Context

Large language model agents differ from ordinary, single-turn language models because they repeatedly plan actions, retrieve information from memory, use external tools, observe the results, and update their internal state. This structure supports long-horizon tasks such as question answering, code generation, web navigation, and autonomous driving.

The same structure creates a broader security problem. A malicious trigger need not be placed directly in the underlying language model. It can instead enter through:

- A manipulated plan or reasoning trace.
- Poisoned retrieved memory.
- Altered tool output or an adversarial environmental observation.

These intermediate artifacts are especially dangerous because agents repeatedly write them back into their context or state. A trigger introduced at one step can therefore survive, affect later decisions, and cross from one workflow component into another.

Previous backdoor studies mainly examined standalone LLMs, retrieval-augmented generation systems, or individual agent components under separate assumptions and evaluation protocols. Such isolated tests do not adequately represent modern agents, where planning, memory, tools, and feedback are tightly connected over multiple steps.

### Figure 1: Conceptual propagation of an agent backdoor

Figure 1 depicts a user asking an agent to analyze sales data. The agent cycles among three stages:

1. **Planning**, which creates reasoning or action plans.
2. **Memory**, which supplies long-term knowledge, contextual recall, and session history.
3. **Tool execution**, which includes operations such as code interpretation, web search, and other external interactions.

A trigger introduced into any one stage can travel into the other stages through repeated context and state updates. The central point is that an agent backdoor is a trajectory-level phenomenon, not necessarily an isolated malicious output.

## 2. Research Goal and Objectives

The paper aims to provide a unified way to study where backdoors enter an LLM-agent workflow, when they activate, how long they persist, and how they propagate across planning, memory, and tool-use stages.

Its specific objectives are to:

- Develop a modular, stage-aware framework called **BackdoorAgent**.
- Organize existing agent attacks using a common taxonomy based on their injection stage.
- Record complete execution trajectories so that trigger activation and downstream effects can be examined.
- Build a standardized benchmark covering language-only and multimodal agents.
- Compare seven attacks across multiple closed-source, open-source, and more advanced LLM backbones.
- Determine whether attack vulnerability depends more on the underlying model, the task, or the workflow channel through which the trigger enters.
- Test whether token-probability signals used to detect backdoors in standalone LLMs transfer to multi-step agents.

No formal statistical hypotheses or significance tests are stated.

## 3. Methods (Approach/Design)

### 3.1 Formal model of an agent workflow

At discrete step \(t\), an agent receives a query \(q\) and maintains:

- An **observable context** \(x_t\), including system and user messages, retrieved material, tool feedback, and environmental observations.
- An **internal state** \(s_t\), including structured or non-textual information such as planner metadata, prior interaction records, caches, or memory indices.

The workflow has three functional stages:

- **Planning:** produces a plan or reasoning artifact \(p_t\).
- **Memory:** retrieves content \(m_t\), optionally using the current plan.
- **Tools:** execute an external action and return feedback \(o_t\).

Afterward, the artifacts are added to the next context:

\[
x_{t+1}=x_t\cup\{p_t,m_t,o_t\},
\]

while an agent-specific state-update operation produces \(s_{t+1}\).

In plain language, plans, retrieved passages, and tool results do not disappear after use. They become part of what the agent sees or remembers later, allowing a malicious artifact to influence subsequent planning, retrieval, and actions.

### 3.2 Definition of a successful agent backdoor

A clean execution trajectory \(A(q)\) should produce benign behavior. A triggered trajectory \(A_\tau(q)\), in which trigger \(\tau\) is introduced into a plan, memory item, tool output, or the channel producing it, should produce the attacker’s intended behavior:

\[
A(q)\rightarrow\text{benign behavior},\qquad
A_\tau(q)\rightarrow\text{backdoor behavior}.
\]

Unlike a single-turn model backdoor, an agent backdoor can persist because the altered artifact is carried into later context and internal state. For example, poisoned memory may distort later planning, while deceptive tool feedback may bias subsequent retrieval and decisions.

### 3.3 Attack taxonomy

Table 1 classifies seven representative attacks:

| Attack | Injection stage | Access | Persistence | Stealthiness | Objective |
|---|---|---:|---|---|---|
| BadChain | Planning | Black-box | Short-term | Low | Hijack |
| BadAgent | Planning | White-box | Short-term | Low | Disruption |
| PoisonedRAG | Memory | White-box | Long-term | Medium | Hijack |
| TrojanRAG | Memory | White-box | Long-term | Medium | Control |
| AgentPoison | Memory | White-box | Long-term | High | Control |
| DemonAgent | Tools | White-box | Session-persistent | High | Control |
| AdvAgent | Tools | Black-box | Short-term | High | Disruption |

Thus, planning attacks mainly modify reasoning or plans; memory attacks contaminate persistent retrieval; and tool attacks manipulate actions, returned information, or environmental observations.

### 3.4 BackdoorAgent framework

BackdoorAgent exposes hook points at planning generation, memory retrieval, and tool execution/return interfaces. An attacked agent replaces one clean component with an attacked version:

- \((P_\tau,M,T)\) for a planning attack.
- \((P,M_\tau,T)\) for a memory attack.
- \((P,M,T_\tau)\) for a tool attack.

The framework does not require a rigid planning–memory–tool order. An agent may call memory or tools multiple times per step. Hooks are attached to component interfaces so the framework can support different agent designs.

Each run is defined by one configuration containing the agent template, task instances, and attack variant. Execution proceeds for a fixed step budget or until termination. The system records complete structured trajectories:

\[
\mathcal{T}(q)=\{(x_t,s_t,p_t,m_t,o_t)\}_{t=0}^{T-1}.
\]

This logging reveals where a trigger enters, when it activates, and how it changes later decisions.

BackdoorAgent also standardizes:

- How the query and context are serialized into prompts.
- How tool calls and outputs are extracted and validated.
- Memory indexing, top-\(k\) retrieval, reranking, and reinsertion into context.
- Task loading, agent templates, evaluation, and replay information.

### Figure 2: Framework architecture

Figure 2 shows three layers:

- A **backdoor attack suite**, divided into planning, memory, and tool-use attacks.
- A **unified agent workflow**, where planning, memory, and tools exchange persistent artifacts through repeated updates.
- A **benchmark layer** containing Agent Drive, Agent QA, Agent Code, and Agent Web, with unified attack-success and accuracy evaluation.

The diagram emphasizes stage-aware hooks, instrumented execution, configurable attacks, and trajectory logging.

### 3.5 Representative tasks

The benchmark contains four agent applications:

- **Agent QA:** Retrieval-grounded reasoning with persistent memory. The attacker tries to induce an incorrect but fluent answer.
- **Agent Code:** Iterative program synthesis with execution feedback. Attacks can trigger destructive operations, such as database deletion, while preserving the appearance of correct code generation.
- **Agent Web:** Multimodal web perception and action. Attacks cause interface-level misdirection, such as purchasing an incorrect item while appearing to finish the task.
- **Agent Drive:** Closed-loop sequential control with environmental feedback. Small perturbations can accumulate and produce unsafe behavior such as a sudden stop.

Agent Web is evaluated only on multimodal-capable backbones.

### 3.6 Models and evaluation conditions

The experiments cover closed-source and open-source backbones under identical task instances and step budgets. Reported model families and variants include GPT, Claude, Gemini, Qwen, DeepSeek, and Kimi systems. A separate table evaluates newer or more advanced GPT and Gemini variants.

Three metrics are used:

- **Clean ACC:** Task success without trigger injection, measured using task-specific verification—exact match for QA, unit tests for Code, task completion for Web, and safety constraints for Drive.
- **Attack success rate (ASR):** Percentage of triggered cases in which the attacker-specified behavior occurs.
- **ACC under attack:** Ordinary task success on the same triggered executions.

The paper does not report sample counts, uncertainty intervals, or statistical significance tests.

## 4. Results and Findings

### 4.1 High attack success can coexist with good task accuracy

Across Tables 2–5, many attacks obtain high ASR while causing only limited loss in normal task accuracy. An agent can therefore satisfy an ordinary benchmark verifier while also carrying out the malicious objective.

Examples highlighted by the paper include:

- **Agent Code, qwen2.5-72b, AgentPoison:** clean ACC 78.45, ASR 88.34, and attacked ACC 75.89.
- **Agent QA, Kimi-K2, AgentPoison:** clean ACC 71.25, ASR 79.83, and attacked ACC 73.77. Here attacked accuracy is higher than the clean baseline.
- **Agent Code, GPT-4o-mini, AgentPoison:** ASR 98.01 with attacked ACC 56.74, compared with clean ACC 58.95.
- **Agent QA, qwen2.5-72b, AdvAgent:** ASR 93.89 with attacked ACC 72.13, compared with clean ACC 69.47.

These results show that accuracy alone may not reveal behavioral compromise. In some settings, a backdoored agent appears equally capable or even improves on the task metric while executing an attacker-selected behavior.

### 4.2 Closed-source backbone results

Table 2 evaluates Claude Sonnet 4.5, Gemini 3 Flash, GPT-4o-mini, GPT-5-mini, and Qwen3-Max on Code, QA, and Drive.

Notable results include:

- In **Code**, memory attacks are often extremely effective:
  - GPT-4o-mini reaches ASR 92.30 under PoisonedRAG, 92.86 under TrojanRAG, and 98.01 under AgentPoison.
  - Gemini 3 Flash reaches 92.31, 91.43, and 76.49 on those attacks.
  - Claude Sonnet 4.5 reaches 80.13, 80.05, and 80.31.
- DemonAgent is much less effective in several Code settings, including ASR 3.70 for GPT-4o-mini, 4.29 for GPT-5-mini, and 4.76 for Claude.
- In **QA**, GPT-4o-mini reaches ASR 91.30 under PoisonedRAG and 95.76 under AdvAgent. GPT-5-mini reaches 93.48 under PoisonedRAG and 84.78 under AdvAgent.
- In **Drive**, TrojanRAG and AgentPoison are especially effective:
  - Gemini reaches ASR 95.76 under TrojanRAG and 95.12 under AdvAgent.
  - GPT-4o-mini reaches 95.33 under TrojanRAG and 92.68 under AgentPoison.
  - GPT-5-mini reaches 95.12 under TrojanRAG, 95.24 under AgentPoison, and 92.51 under AdvAgent.
  - Qwen3-Max reaches 92.68 under TrojanRAG and 97.38 under AdvAgent.

Clean accuracy varies substantially by task and model, but high clean performance does not consistently correspond to low ASR.

### 4.3 Agent Web results

Table 3 evaluates multimodal Agent Web using Claude Sonnet 4.5, Gemini 3 Flash, GPT-4o-mini, and Qwen3-VL-235B. Their clean accuracies are high: 98.54, 96.20, 99.16, and 99.25, respectively.

Vulnerability varies sharply by backbone:

- **Claude Sonnet 4.5:** BadChain reaches ASR 97.39 while attacked ACC remains 98.35. The other listed attacks have ASR 0, with attacked ACC between 96.49 and 99.65.
- **Gemini 3 Flash:** BadChain reaches 98.74; PoisonedRAG 95.16; TrojanRAG 97.44; AgentPoison 86.67; AdvAgent 5.32; and DemonAgent 95.40. Attacked ACC remains between 92.41 and 97.47.
- **GPT-4o-mini:** ASRs are comparatively low—0 for BadChain, 4.52 for PoisonedRAG, 3.57 for TrojanRAG, 8.91 for AgentPoison, 2.53 for AdvAgent, and 4.53 for DemonAgent—while attacked ACC remains between 95.37 and 99.66.
- **Qwen3-VL-235B:** ASRs range from 0 for BadChain to 14.35 for DemonAgent; attacked ACC remains between 95.64 and 99.88.

Thus, similarly high-performing web agents can have very different backdoor susceptibility.

### 4.4 Open-source backbone results

Table 4 evaluates DeepSeek-R1-671B, DeepSeek-V3.2-Exp, Kimi-K2, Qwen2.5-72B-Instruct, and Qwen3-235B-A22B.

Important patterns include:

- In **Code**, Qwen2.5 and Qwen3 have the highest clean accuracies, 78.45 and 80.47, but remain vulnerable:
  - Qwen2.5 AgentPoison ASR is 88.34.
  - Qwen3 AgentPoison ASR is 85.64.
  - DeepSeek-V3.2 AdvAgent ASR is 86.48.
  - Kimi-K2 TrojanRAG ASR is 84.29.
- In **QA**, AdvAgent is highly successful on Qwen models:
  - Qwen2.5: ASR 93.89.
  - Qwen3: ASR 91.30.
  - Kimi-K2’s AgentPoison ASR is 79.83.
- **Drive is markedly vulnerable to planning and tool/environment attacks:**
  - BadChain exceeds 90 ASR for every open-source backbone: 92.58 for DeepSeek-R1, 97.85 for DeepSeek-V3.2, 92.15 for Kimi-K2, 97.33 for Qwen2.5, and 96.47 for Qwen3.
  - AdvAgent reaches 80.48 for DeepSeek-R1, 97.56 for DeepSeek-V3.2, 85.71 for Kimi-K2, 87.21 for Qwen2.5, and 75.34 for Qwen3.
  - TrojanRAG reaches 85.37 for DeepSeek-V3.2 and 87.80 for Qwen2.5.
  - DemonAgent reaches 75.37 for Kimi-K2, while results vary more across the other families.

### 4.5 More advanced backbone results

Table 5 evaluates GPT-5.2, GPT-4o-1120, and Gemini 3 Pro.

- In **Code**:
  - GPT-5.2 has clean ACC 84.73 and reaches ASR 85.94 under TrojanRAG.
  - GPT-4o has clean ACC 62.47 and reaches ASR 90.17 under PoisonedRAG, 92.08 under TrojanRAG, and 95.61 under AgentPoison.
  - Gemini 3 Pro has clean ACC 73.06 and reaches ASR 78.12 under TrojanRAG and 77.48 under AdvAgent.
- In **QA**:
  - GPT-5.2 clean ACC is 89.37, but PoisonedRAG reaches ASR 90.78 and AdvAgent 82.43.
  - GPT-4o clean ACC is 74.83, while PoisonedRAG reaches 92.63 and AdvAgent 94.52.
  - Gemini 3 Pro clean ACC is 90.61, while PoisonedRAG reaches 84.19 and AdvAgent 78.76.
- In **Drive**:
  - GPT-5.2 reaches ASR 88.77 under TrojanRAG, 90.43 under AgentPoison, and 88.71 under AdvAgent.
  - GPT-4o reaches 92.54 under TrojanRAG, 91.83 under AgentPoison, and 90.52 under AdvAgent.
  - Gemini 3 Pro reaches 91.57 under TrojanRAG and 88.94 under AdvAgent.

These results reinforce that stronger or newer models are not automatically more resistant.

### 4.6 Vulnerability is organized mainly by injection channel

The paper concludes that the point where a trigger enters the workflow predicts vulnerability better than task category alone.

- **Memory attacks** are consistently effective when retrieved material is repeatedly reintroduced into context. This repeated exposure reinforces misinformation in QA and destructive instructions in Code.
- **Planning attacks** generally have moderate but relatively stable effects in QA and Code.
- **Tool and environmental attacks** become especially dangerous in closed-loop tasks such as driving, where manipulated observations or feedback alter future states.

### Table 6: Model-family vulnerability by module

Average ASR across attacks and tasks is:

| Model family | Planning ASR | Memory ASR | Tools ASR |
|---|---:|---:|---:|
| GPT | 43.58 | 77.97 | 60.28 |
| Claude | 10.43 | 54.82 | 23.07 |
| Gemini | 39.49 | 75.39 | 48.98 |
| Qwen | 35.41 | 55.45 | 54.45 |
| DeepSeek | 27.84 | 38.91 | 42.20 |

Memory is the most vulnerable channel for four of the five families. DeepSeek is the exception, with tool ASR 42.20 slightly exceeding memory ASR 38.91. Planning is generally the least effective channel.

The abstract’s headline persistence figures—43.58% for planning, 77.97% for memory, and 60.28% for tool-stage attacks—correspond to the GPT-family aggregate in this table.

### 4.7 Memory poisoning intensity

Table 7 varies the proportion of the external memory or retrieval corpus that is poisoned:

| Model family | ASR at 0.1 poisoning | ASR at 0.2 | ASR at 0.5 |
|---|---:|---:|---:|
| GPT | 53.06 | 77.97 | 97.72 |
| Gemini | 50.39 | 75.39 | 97.00 |
| Qwen | 33.25 | 55.45 | 86.75 |
| DeepSeek | 21.84 | 38.91 | 70.83 |

Attack success rises monotonically for every family. This shows that memory-channel vulnerability is strongly sensitive to corpus contamination intensity.

### 4.8 Sequential amplification in Agent Drive

Agent Drive differs from QA and Code because each action changes the next state. A small malicious perturbation can therefore compound over time.

In QA and Code, attacks often steer text artifacts, and some effects remain bounded within a step. In Drive, altered plans, tool feedback, or observations affect subsequent decisions, producing cascading failure. BadChain exceeds 90 ASR on all open-source Drive backbones, while AdvAgent frequently exceeds 90 in both closed- and open-source settings.

The authors interpret this as evidence that sequential state transitions can convert small changes into long-horizon behavioral derailment.

### 4.9 Computational overhead

Figure 3 plots relative token overhead against trigger strength from 1 to 4 for GPT-4o:

- All modules begin at approximately 1.0 relative overhead.
- Planning attacks increase only slightly, reaching roughly 1.1–1.15 at strength 4.
- Tool-use attacks rise more strongly, to approximately 1.45–1.5.
- Memory attacks rise most sharply, to approximately 1.9.

The precise intermediate values are not printed in the text, so these readings are approximate from the graph. Memory attacks cost more because retrieved malicious material is repeatedly fetched and reinserted. Planning attacks are most token-efficient because they primarily alter transient reasoning traces. The result suggests a trade-off between attack effectiveness and computational efficiency.

### 4.10 Probability-based defense analysis

The authors test whether token-probability cues used for standalone LLM backdoor detection distinguish clean and triggered agent trajectories.

#### Figure 4: Target versus non-target token probability

Across Agent Drive, Agent QA, and Agent Code, attack-target tokens receive slightly higher average probabilities than non-target tokens. The bars appear to be approximately:

- Target tokens: about 0.94–0.96.
- Non-target tokens: about 0.89–0.91.

These values are approximate because exact labels are not supplied. The important result is that the gap is small and inconsistent despite successful malicious control.

The authors argue that multi-step malicious effects may be delayed and mixed with benign reasoning, retrieval, and tool outputs. This weakens the token-level signals that may be visible in a single model response.

#### Figure 5: ROC curve

The supplementary defense analysis compares output-token probability distributions from a target backbone and a reference model under clean and triggered conditions. Figure 5 aggregates the resulting receiver operating characteristic curve across tasks and attack types.

The displayed AUROC is approximately **0.7681**, above random guessing but with only modest separation. The curve therefore indicates that some backdoor signal exists, but probability-based detection does not separate clean and attacked trajectories reliably enough for high-confidence detection.

## 5. Analysis and Interpretation

The results answer the paper’s main question by showing that agent backdoors are primarily workflow-level vulnerabilities.

Three mechanisms explain the observed behavior:

1. **Persistence of intermediate artifacts:** Plans, retrieved passages, and tool results are repeatedly written into later context or state.
2. **Cross-stage propagation:** A malicious memory item can alter planning, or deceptive tool feedback can influence later memory retrieval and decisions.
3. **Closed-loop amplification:** In sequential environments, one altered action changes the next observation, allowing errors to compound.

The most important interpretive finding is the separation between **task success** and **behavioral integrity**. An agent may pass unit tests, answer the benchmark question correctly, complete a web task, or satisfy another task verifier while also performing a harmful secondary behavior. Therefore, clean accuracy and attacked accuracy cannot by themselves measure whether the agent remains under legitimate control.

Model capability and backdoor robustness also diverge. High-performing backbones remain vulnerable because workflow-level persistence and feedback are not solved merely by improving the language model.

Memory is a systematic attack surface because poisoned information can be retrieved and reinforced multiple times. Tool attacks depend more strongly on task dynamics, but become dominant when tools or environmental feedback directly control a sequential system.

Finally, standalone LLM defenses do not transfer cleanly to agents. Those defenses often assume that malicious behavior appears immediately as a probability or logit anomaly in one response. Agent attacks may instead be delayed, distributed across modules, or entangled with benign content. The authors therefore argue that defenses should examine complete trajectories, state evolution, module interactions, and tool-mediated consequences.

## 6. Contributions and Novelty

The paper’s main contributions are:

- It introduces **BackdoorAgent**, described as the first modular, stage-aware framework to study agent backdoors from a unified agent-centric perspective.
- It decomposes the attack surface into planning, memory, and tool/environment stages.
- It formalizes how triggers persist through recurrent context and state updates.
- It provides component-level hooks that work without imposing one rigid agent control flow.
- It records full trajectories for locating injection, activation, persistence, and cross-stage influence.
- It standardizes prompt construction, tool-call formatting, memory retrieval, execution, logging, replay, and evaluation.
- It organizes seven existing attacks in a common taxonomy covering access requirements, persistence, stealthiness, and attacker objectives.
- It introduces a benchmark spanning four agent applications, including language-only and multimodal workflows.
- It demonstrates empirically that injection channel and workflow structure are more informative about vulnerability than clean model performance alone.
- It provides initial evidence that token-probability defenses designed for standalone LLMs have limited transferability to multi-step agents.
- The authors state that they will release the code and dataset to support reproducibility and defense research.

## 7. Limitations and Caveats

The authors identify several limitations:

- The benchmark includes several tasks, attacks, and model backbones, but does not represent the full diversity of real-world agent architectures, environments, and threat models.
- Experiments are conducted in controlled benchmark settings, so deployment behavior may be richer and less predictable.
- The analysis focuses mainly on trigger persistence and cross-stage propagation.
- Adaptive adversaries are not studied.
- More complex deployment scenarios remain unexplored.
- The work is primarily attack-centric and does not propose a new defense mechanism.
- The probability-based defense study is preliminary and shows only limited separation.
- Agent Web is evaluated only on multimodal-capable models, so it does not have the same backbone coverage as the other tasks.
- The paper does not report sample sizes, confidence intervals, variability across repeated runs, or statistical significance tests.
- Token-overhead and token-probability plots do not provide exact numerical labels for every plotted point, limiting precise extraction from the supplied figures.
- Some attack results vary sharply by model and task, especially in Agent Web and for tool attacks, so no single attack is uniformly effective in every configuration.
- High ASR combined with preserved ACC means ordinary task-level evaluation may substantially underestimate compromise.

## 8. Future Work or Open Questions

The paper identifies the following directions:

- Study adaptive attackers that respond to defenses or changing agent behavior.
- Evaluate more diverse real-world architectures, execution environments, and threat models.
- Examine complex deployments where malicious behavior appears in less predictable forms.
- Develop defenses specifically designed for agents rather than directly transferring single-response LLM defenses.
- Design detectors that analyze complete trajectories, temporal propagation, internal state evolution, cross-module interactions, and tool-mediated effects.
- Determine how to separate delayed malicious influence from benign reasoning, retrieved information, and environmental feedback.
- Continue expanding and updating the benchmark.
- Release and maintain the code and dataset to support reproducibility and further research.

## 9. High-Level Takeaway (Plain Language)

An AI agent does not make just one response—it repeatedly plans, remembers information, uses tools, and reacts to what happens. This paper shows that a hidden malicious trigger inserted into any one of those stages can survive for several steps and spread through the whole workflow. Memory is generally the most vulnerable channel, while manipulated tools or observations are especially dangerous in closed-loop systems such as driving. Even worse, an attacked agent may still score well on ordinary benchmarks, so it can look functional while doing something harmful. BackdoorAgent provides a common framework and benchmark for exposing these trajectory-level failures and shows why agent defenses must monitor the whole workflow rather than only individual model outputs.