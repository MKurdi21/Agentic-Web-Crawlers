# SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems

**Authors:** Yunhao Feng*, Yifan Ding*, Yingshui Tan, Boren Zheng, Xiaolong Li, Kun Zhai, Yishan Li, Yanming Guo, and Wenke Huang  
\*Equal contribution.  
**Venue:** Proceedings of the 43rd International Conference on Machine Learning (ICML), PMLR 306, 2026.

## 1. Background and Context

Modern software agents increasingly solve tasks by combining reusable “skills.” A skill is a distributable package containing:

- A natural-language specification \(m\), such as `SKILL.md`, that guides the agent.
- Executable artifacts \(A=\{a_j\}\), such as scripts, tools, API calls, and other resources.

This modular design improves reuse, scalability, planning, and compositional task solving. Skills can execute code, maintain state, access external resources, and persist across tasks, users, and deployments. Public repositories and skill marketplaces make them easy to distribute.

These advantages also create a security problem: installed skills are generally trusted and audited mainly for whether they perform their advertised function. Their internal execution behavior receives less scrutiny than model inputs and outputs.

Earlier backdoor and adversarial research mainly manipulated:

- Model training data or parameters.
- User prompts or planning context.
- Tool descriptions and calls.
- Retrieved memories or knowledge bases.
- Other transient interaction channels.

Such attacks often depend on the model accepting a malicious instruction during one episode. By contrast, executable skills are persistent components that can affect many later runs while leaving the model, prompts, and toolset unchanged. A popular compromised skill could therefore spread malicious behavior across multiple users and deployments.

**Figure 1** depicts this attack surface. An LLM-centered agent composes planning, memory, and tool-execution skills—including planner, search, code, execution, and memory skills. SkillTrojan distributes encrypted payload fragments among several apparently ordinary skills. When a trigger occurs, normal skill composition gathers the fragments, reconstructs the payload, and executes it.

## 2. Research Goal and Objectives

The paper introduces **SkillTrojan**, described as the first systematic backdoor attack aimed at the reusable skill abstraction layer rather than model parameters, training data, prompts, or isolated tool and memory interfaces.

Its objectives are to demonstrate that an attacker can:

1. Embed malicious behavior in skills that retain plausible, useful functionality.
2. Divide an arbitrary encrypted payload among multiple skill invocations.
3. Keep the malicious behavior dormant on ordinary queries.
4. Reconstruct and execute the payload when a predefined trigger appears.
5. Preserve the correct user-visible answer while producing a hidden execution-side effect.
6. Automatically generate many backdoored variants from arbitrary skill templates.
7. Evaluate attack success and benign utility across open- and closed-weight models, multiple tasks, and multiple agent frameworks.
8. Provide a large dataset for research on skill-level attacks and defenses.

The central claim is that a backdoor attached to normal execution semantics can achieve high attack success with little clean-task degradation and evade defenses that inspect only prompts, final answers, or individual skill files.

## 3. Methods (Approach/Design)

### Threat model

A deployed agent installs skills \(S=\{s_1,\ldots,s_K\}\). Given query \(q\), the model uses each skill’s specification to select actions and solve the task.

The attacker replaces selected benign packages \(s=(m,A)\) with backdoored versions \(\tilde{s}=(\tilde m,\tilde A)\). The attacker chooses:

- An executable payload \(P\).
- A trigger predicate \(\mathrm{Trig}_\tau(q)\), defined by a trigger string or pattern \(\tau\).
- A fragment count \(N\).
- An encryption and encoding scheme.

The underlying language model and training data remain trusted and unchanged. After installation, the attacker has no continuing access to the host, operating-system privileges, remote services, or model internals; subsequent interaction occurs only through queries.

The attack must satisfy two goals:

- **Stealth:** If \(\mathrm{Trig}_\tau(q)=0\), the skill should preserve normal behavior.
- **Reliable activation:** If \(\mathrm{Trig}_\tau(q)=1\), normal skill execution should cause \(P\) to run.

Persistence comes only from the installed package. Fragment storage is run-local, temporary, and cleaned after execution. The study excludes attacks requiring long-term or cross-query storage and direct compromise of the model, operating system, or remote services.

### Payload encryption and fragmentation

SkillTrojan encrypts the payload using a symmetric key:

\[
C=\mathrm{Enc}(P;k).
\]

The ciphertext \(C\) is divided into \(N\) indexed fragments:

\[
c_j=\langle j,\mathrm{seg}_j(C)\rangle.
\]

The index allows fragments to be reassembled regardless of the order in which the agent invokes tools. Thus, reconstruction does not depend on a fixed plan, timing, or control-flow sequence.

The fragment count controls a trade-off:

- Larger \(N\) puts less suspicious content in any one output and reduces accidental activation.
- Larger \(N\) also requires the agent to complete more fragment-producing calls, increasing the chance that reconstruction fails.
- Very small \(N\) makes each fragment larger and more conspicuous.

### Specification and executable instrumentation

The benign specification \(m\) is transformed into \(\tilde m\). On clean queries, it remains semantically equivalent to the original and should produce the same distribution of execution traces. On triggered queries, it adds a small planning bias \(\Delta(\pi)\) toward traces that include designated fragment-producing actions and a verifier. It does not explicitly state a malicious instruction or require a fixed action order.

Selected executable actions are modified so that they:

- Preserve their advertised input, output, and functionality.
- Emit nothing extra on clean queries.
- Add one encrypted fragment to a run-local channel on triggered queries.

In the implementation, fragments appear in benign-looking tool-output fields recorded in the agent’s normal trajectory. A verifier retrieves them without cross-run storage.

For an execution trace \(\pi=(a_{i_1},\ldots,a_{i_T})\), the emitted fragments form an unordered set \(F(q)\). The verifier checks whether all required fragments are present:

\[
\{c_1,\ldots,c_N\}\subseteq F(q).
\]

If so, it sorts the pieces by index, reconstructs and decrypts the ciphertext, and executes the recovered payload:

\[
P=\mathrm{Dec}(c_1\Vert\cdots\Vert c_N;k).
\]

It then removes intermediate artifacts. Payload execution is separate from response generation, so the agent can return a correct answer while the payload runs as a hidden side effect.

### Figure 2: layered attack pipeline

Figure 2 follows four layers:

1. **User layer:** A benign query is changed into a subtly marked triggered query.
2. **Agent-reasoning layer:** The LLM, planner, tool selector, and execution controller follow an apparently normal workflow.
3. **Skill-execution layer:** Reusable code, database, network, logging, and utility skills execute; selected calls emit encrypted fragments while retaining normal outputs.
4. **Side-effect layer:** A verifier checks the unordered fragment set, reconstructs and decrypts the payload, executes it, and cleans up.

The visible task result remains benign. The malicious effect occurs only after sufficient ordinary workflow steps have completed.

### SkillTrojanX construction

The researchers crawled the top **1,200** skills by popularity from a public skill marketplace. They retained packages with:

- A parsable natural-language specification.
- Executable artifacts.

Packages were normalized into a common representation. Automated generation then varied:

- Trigger phrase or pattern.
- Payload family.
- Encryption/encoding choice.
- Fragment count \(N\).
- Fragment-emitting and verification entry points.

Each generated package includes structured metadata for these properties.

**Table 4** reports:

| Dataset property | Value |
|---|---:|
| Templates | 1,200 |
| Backdoored skills | 3,000+ |
| Template categories | 6 |
| Payload families | 4 |
| Crypto variants | 3 |
| Fragment-count variants | 3 |
| Unique triggers | 50 |

**Figure 4** distributes the generated packages across Coding, Data/SQL, File/IO, Planning, Utilities, and Web templates. Its four payload families are system profiling, secret harvesting, file drop, and network beacon. Data/SQL has the largest total bar, while the other categories also contain substantial representation from multiple payload families.

### Experimental design

The primary benchmark is an **EHR SQL task**. Given a natural-language clinical question, an agent composes and runs SQL against an electronic-health-record database. SQL correctness is judged by comparing its execution result with the expected result using an LLM judge instructed to return only “yes” or “no.”

Default settings were:

- Poisoning ratio \(\rho=0.2\).
- Fragment count \(N=3\).
- XOR+Base64 encryption/encoding.
- Triggered queries created by inserting a trigger phrase into the original query.

Models served as the agent policy for planning, tool selection, and intermediate reasoning. Skill code and evaluation procedures were otherwise held constant.

**Open-weight models:** GLM-4.7, Qwen3-Coder, GLM-4.6, and Qwen3-VL-235B-A22B-Instruct.

**Closed-weight models:** GPT-4o-mini-0718-Global, Claude-Haiku-4.5, Claude-Sonnet 4.5, Qwen3-Max, and GPT-5.2-1211-Global.

Baselines were GCG, AutoDAN, CPA, BadChain, and AgentPoison. GCG, AutoDAN, and CPA used adversarial suffixes or instruction patterns in the query and/or system prompt. BadChain and AgentPoison placed malicious instructions in agent-readable context, such as tool descriptions or memory, while leaving executable skills unchanged.

All methods were evaluated using an execution-side definition of success. A payload had to produce a deterministic side effect verified outside the model’s text. Baselines were given a benign-looking payload tool, but the model had to choose to invoke it.

Metrics were:

- **ACC:** Percentage of clean queries answered correctly.
- **ASR:** Percentage of triggered queries where the payload was reconstructed and executed, confirmed by a verifier marker and deterministic side effect.

The paper also evaluated SWE-Bench Verified and a separate industry-oriented coding benchmark across four agent frameworks.

## 4. Results and Findings

### EHR SQL: open-weight models

**Table 1** reports ACC/ASR percentages:

| Method | GLM-4.7 | Qwen3-Coder | GLM-4.6 | Qwen3-VL |
|---|---:|---:|---:|---:|
| Non-attack | 84.1 / 0.0 | 71.5 / 0.0 | 76.0 / 0.0 | 53.2 / 0.0 |
| GCG | 83.7 / 35.1 | 70.2 / 41.0 | 75.3 / 38.6 | 51.8 / 24.9 |
| AutoDAN | 82.2 / 46.8 | 68.9 / 51.4 | 73.6 / 55.6 | 49.5 / 19.7 |
| CPA | 81.4 / 44.2 | 67.8 / 57.9 | 72.1 / 52.7 | 48.9 / 31.5 |
| BadChain | 84.0 / 31.8 | 70.7 / 18.4 | 76.6 / 23.7 | 52.6 / 7.9 |
| AgentPoison | 85.0 / 57.2 | 72.4 / 62.5 | 77.1 / 60.8 | 52.0 / 37.6 |
| SkillTrojan | **85.2 / 62.1** | **76.3 / 64.7** | **81.3 / 72.0** | 48.4 / 26.7 |

SkillTrojan had the highest ASR on GLM-4.7, Qwen3-Coder, and GLM-4.6, while maintaining or improving ACC relative to the no-skill Non-attack condition. It was less successful on Qwen3-VL: AgentPoison reached 37.6% ASR versus SkillTrojan’s 26.7%, and SkillTrojan ACC fell from 53.2% to 48.4%.

### EHR SQL: closed-weight models

**Table 2** reports:

| Method | GPT-4o-mini | Claude Haiku 4.5 | Claude Sonnet 4.5 | Qwen3-Max | GPT-5.2 |
|---|---:|---:|---:|---:|---:|
| Non-attack | 71.6 / 0.0 | 73.1 / 0.0 | 86.5 / 0.0 | 82.7 / 0.0 | 73.0 / 0.0 |
| GCG | 70.8 / 30.2 | 70.1 / 32.9 | 69.6 / 37.8 | 69.8 / 42.1 | 70.1 / 45.8 |
| AutoDAN | 67.4 / 42.1 | 68.6 / 39.4 | 69.7 / 34.9 | 67.9 / 30.8 | 68.4 / 27.4 |
| CPA | 66.3 / 38.5 | 66.9 / 41.0 | 67.8 / 44.6 | 67.2 / 48.7 | 67.9 / 51.1 |
| BadChain | 71.9 / 33.7 | 72.6 / 28.9 | 71.5 / 22.7 | 70.9 / 14.2 | 70.8 / 8.3 |
| AgentPoison | 74.8 / 53.7 | 75.5 / 54.8 | 74.1 / 56.2 | 73.4 / 57.6 | 72.9 / 58.3 |
| SkillTrojan | 68.5 / **54.3** | **82.7 / 57.3** | **90.7 / 64.2** | **86.6 / 74.7** | **89.3 / 97.2** |

The strongest result was **97.2% ASR with 89.3% ACC on GPT-5.2-1211-Global**, compared with 73.0% ACC without the skills. The strongest competing ASR was 58.3% from AgentPoison, a 38.9-point gap.

SkillTrojan also achieved 74.7% ASR and 86.6% ACC on Qwen3-Max, and 64.2% ASR with 90.7% ACC on Claude Sonnet 4.5. Its GPT-4o-mini ACC was lower than Non-attack—68.5% versus 71.6%—although its 54.3% ASR narrowly exceeded AgentPoison’s 53.7%.

### Why some SkillTrojan ACC values improve

The installed skills themselves can improve task completion. Table 7 separates this benefit from the backdoor:

| Setting | GLM-4.7 | Qwen3-Coder | GLM-4.6 | Qwen3-VL |
|---|---:|---:|---:|---:|
| Non-attack, no installed stack | 84.1 | 71.5 | 76.0 | 53.2 |
| SkillTrojan | 85.2 | 76.3 | 81.3 | 48.4 |
| Native versions of same skills | **88.7** | **82.3** | **85.5** | **50.3** |

Native skills achieved the best ACC in all four comparisons. SkillTrojan retained much, but not all, of their benign utility. Thus, improvements over Non-attack came from useful installed skills rather than the malicious logic.

### Execution traces

**Figure 3** compares clean and triggered tool-call counts using a violin-style distribution and discrete-frequency plot. Triggered runs use a small but systematic number of additional calls for fragment collection and verification. Nevertheless, their distribution remains close to clean runs and within the ordinary range for complex EHR SQL tasks. Exact pointwise frequencies are not printed clearly enough to report beyond this trend.

### Scanner defense

Approximately 500 skills were classified as safe or unsafe:

| Variant | Qwen3Guard safe (%) | Llama-Guard safe (%) |
|---|---:|---:|
| Full SkillTrojan | 98.2 | 99.4 |
| Native skills | 100.0 | 99.6 |
| SkillTrojan without encryption/segmentation | 3.4 | 2.8 |

The scanners detected the naive unencrypted, unsegmented attack but treated almost all complete SkillTrojan packages as safe. Their outputs on full SkillTrojan were nearly indistinguishable from native skills.

### Fragment-count ablation

**Figure 5** varies \(N\in\{1,2,3,5\}\) on GPT-4o-mini. ASR follows a unimodal pattern:

- Small \(N\) makes each fragment larger and more conspicuous, increasing the chance that the model alters or skips the intended workflow.
- Large \(N\) requires more fragment-bearing calls and raises the probability of incomplete collection.
- **\(N=3\)** produces the highest ASR.
- ACC remains approximately stable across all settings.

The plotted points show the trend, but exact values beyond the identified optimum are not supplied in the caption or text.

### Encryption ablation

Under GPT-4o-mini with \(N=3\) and \(\rho=0.2\):

| Scheme | ACC (%) | ASR (%) | Base64 heuristic flag (%) |
|---|---:|---:|---:|
| XOR+Base64 | 68.5 | 54.3 | 78.0 |
| Hybrid | 68.4 | 54.6 | 21.0 |

Changing encryption altered ACC by only 0.1 point and ASR by 0.3 points, but reduced detection by the simple Base64 heuristic from 78% to 21%.

### Poisoning-ratio ablation

**Figure 6** evaluates \(\rho\in\{0.1,0.2,0.5\}\) on GPT-4o-mini:

- Clean ACC remains near the default **68.5%**, including at \(\rho=0.5\).
- ASR varies by no more than **3 points**.
- The plotted ASR is roughly in the low-to-mid 50% range, while ACC stays around 68–69%.

This supports conditional dormancy: per-trigger success depends on completing the trace within a run rather than on how frequently triggers occur globally.

### SWE-Bench Verified

A software-engineering task counted a patch as correct only if it passed verified unit tests:

| Method | Qwen3-Coder | GPT-5.2 | GLM-4.7 |
|---|---:|---:|---:|
| Non-attack | 64.8 / 0.0 | 70.6 / 0.0 | 67.3 / 0.0 |
| GCG | 62.1 / 10.3 | 68.2 / 12.5 | 55.9 / 26.1 |
| SkillTrojan | **65.7 / 63.9** | 70.4 / **92.8** | **67.6 / 66.4** |

SkillTrojan preserved ACC within 0.2–0.9 points of Non-attack and greatly exceeded GCG’s ASR on all three models.

### Cross-framework results

On a separate industry-oriented coding benchmark, SkillTrojan remained effective across four frameworks. These figures are not directly comparable with EHR SQL:

| Framework | Claude Sonnet 4.5 | GPT-5.1 | Qwen3 Coder Plus | Qwen3.5 Plus | GLM-5 |
|---|---:|---:|---:|---:|---:|
| Claude-Code | 63.53 | 95.59 | 98.53 | 94.12 | 87.65 |
| IFlow | 65.00 | 96.18 | **100.00** | 97.35 | 83.53 |
| OpenHands | 69.12 | 91.18 | 99.12 | 95.88 | 86.18 |
| OpenClaw | 65.88 | 96.76 | 99.71 | 94.71 | 88.53 |

ASR ranged from **63.53% to 100%**, indicating that the mechanism was not tied to a single agent framework.

## 5. Analysis and Interpretation

The authors attribute SkillTrojan’s advantage to its placement in trusted execution rather than conversational persuasion. Prompt-centric attacks require the model to accept a malicious instruction and explicitly call a harmful tool. More capable models may refuse or ignore such instructions. SkillTrojan instead relies on the agent completing an apparently legitimate tool chain; greater tool-use competence can therefore improve activation.

The results support several conclusions:

- A benign final answer does not show that an agent run was safe. The payload can execute independently as a side effect.
- ACC and ASR must be evaluated together. SkillTrojan generally combines competitive ACC with higher ASR than attacks that either harm task accuracy or activate unreliably.
- Backdoor evaluation should inspect tool outputs, call ordering and depth, provenance, and external state changes—not only prompts and final text.
- Fragmentation and indexing make reconstruction robust to planner variability because the verifier needs the complete set, not a prescribed order.
- Encryption and segmentation sharply weaken simple static detection.
- Stable ACC across poisoning ratios means spot checks dominated by clean queries may fail to expose the backdoor.
- The small increase in tool calls is a potential signal, but Figure 3 shows that it remains within the normal regime for complex tasks.
- The SWE-Bench and cross-framework experiments indicate that the vulnerability extends beyond EHR SQL and one implementation stack.

The paper suggests constraining verifier-like tools, auditing unexpected tool-depth increases, checking tool-output provenance, and monitoring side effects. More broadly, defenses need to reason about combinations of individually plausible actions because no single skill must contain the complete plaintext payload or an overtly malicious instruction.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- It introduces the first systematic backdoor paradigm focused on reusable skill implementations.
- It defines an attack that leaves the model, training data, and ordinary prompts unchanged.
- It combines trigger-based activation, encrypted fragmentation, indexed order-independent reconstruction, hidden side-effect execution, and cleanup.
- It provides automated synthesis of backdoored variants from arbitrary templates and payload configurations.
- It evaluates the attack across open- and closed-weight models, EHR SQL, SWE-Bench Verified, a separate coding benchmark, and four agent frameworks.
- It releases **SkillTrojanX**, containing over 3,000 variants from 1,200 real marketplace templates.
- It demonstrates that lightweight LLM scanners and simple encoding signatures are inadequate for the complete attack.
- It identifies skill provenance and execution behavior as security-critical surfaces distinct from model-level behavior.

## 7. Limitations and Caveats

The paper’s scope imposes several qualifications:

- The main detailed benchmark is EHR SQL; SWE-Bench and the cross-framework experiment broaden the evidence but provide less methodological detail in the supplied paper.
- Payloads are constrained by the permissions and capabilities of the skill execution environment.
- The threat model excludes direct model, operating-system, and remote-service compromise.
- It excludes attacks using long-term or cross-query fragment storage.
- The attacker must first distribute a skill and induce developers to install it.
- Successful activation requires the triggered run to execute all fragment-producing actions and reach the verifier.
- Very small and very large fragment counts reduce reliability.
- Triggered traces require somewhat more tool calls, creating a possible detection signal.
- XOR+Base64 is highly visible to the simple Base64 detector, although the hybrid encoding reduces that detector’s hit rate.
- The scanner analysis uses approximately 500 sampled skills and two lightweight guard models; it does not establish the performance of every possible scanner.
- Sandboxing and output validation are outside the attacker’s capabilities unless enabled by the deployment; the experiments therefore do not demonstrate that SkillTrojan bypasses every sandbox or permission policy.
- SQL correctness relies on an LLM-as-a-judge protocol rather than only a deterministic equivalence test.
- The authors disclose that some are Alibaba employees and that the evaluation includes Alibaba-developed Qwen models; they state that protocols, metrics, and comparisons are documented.
- SkillTrojan is dual-use: the framework and dataset can aid defense research but also demonstrate how to conceal malicious executable logic.

No statistical significance tests, confidence intervals, or repeated-run variance estimates are reported in the supplied text.

## 8. Future Work or Open Questions

The paper calls for defenses that jointly analyze:

- Skill composition across multiple tools.
- Tool-call traces and unusual execution depth.
- Output and package provenance.
- Permissions and external side effects.
- Static and dynamic code behavior.
- Runtime state and execution trajectories.

Proposed directions include:

- Targeted defense prompts and guard models.
- Runtime monitors designed for composed skill execution.
- Sandboxing and permissioned resource access.
- Signed package provenance.
- Static and dynamic code inspection.
- Secure skill-marketplace design.
- Red-team evaluation using SkillTrojanX.
- Policies that constrain verifier-like tools or suspicious reconstruction workflows.

The paper leaves open how these mechanisms should be combined under realistic deployment constraints without disrupting useful skill composition. It also motivates broader testing across skill ecosystems because lightweight static scanning cannot reliably separate encrypted SkillTrojan packages from benign ones.

## 9. High-Level Takeaway (Plain Language)

SkillTrojan shows that an AI agent can appear to solve a task correctly while installed skills quietly cooperate to perform something harmful. Each skill carries only a small encrypted piece, so no individual component obviously reveals the attack. A secret trigger causes the ordinary workflow to collect the pieces, rebuild the payload, and execute it behind the scenes.

The attack reached as high as **97.2% success while retaining 89.3% clean accuracy**, generalized to another benchmark and several agent frameworks, and largely escaped two lightweight skill scanners. The main lesson is that securing an agent requires examining the code it installs, how multiple skills interact, what tools do during execution, and what side effects occur—not merely checking the model’s prompt or final answer.