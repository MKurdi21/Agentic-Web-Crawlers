# ACE: A Security Architecture for LLM-Integrated App Systems

**Authors:** Evan Li, Tushin Mallick, Evan Rose, William Robertson, Alina Oprea, and Cristina Nita-Rotaru  
**Affiliation:** Northeastern University  
**Venue:** Network and Distributed System Security (NDSS) Symposium 2026

## 1. Background and Context

Large language models are increasingly connected to third-party applications that let them perform real-world tasks such as reading files, managing email, booking flights, or reserving restaurants. In these “LLM-integrated app systems,” a central system LLM usually alternates between two activities:

1. **Planning:** deciding what app to call next and with what inputs.
2. **Execution:** calling that app, examining its output, and then planning the next step.

Frameworks such as LangChain, Semantic Kernel, and AutoGen support this dynamic, iterative model. Apps are represented by:

- A natural-language **description** explaining their purpose.
- A **schema** defining inputs and outputs.
- A **function or service** implementing their behavior.

The system LLM reasons over the user query, prior conversation, app descriptions, and intermediate app outputs. This makes control flow flexible, but it also means untrusted app metadata or outputs can influence subsequent planning.

### Security problem

Malicious apps installed on a user’s device can attack both planning and execution. The paper groups the most relevant objectives into four classes:

1. **Planning integrity violation:** manipulating which apps are selected, such as promoting a malicious app or suppressing a benign competitor.
2. **Execution integrity violation:** changing execution flow or causing benign apps or users to receive manipulated information.
3. **Execution availability breakdown:** interrupting a task even though suitable resources remain available.
4. **Execution privacy compromise:** leaking sensitive information from the execution environment.

Planning-time availability attacks are possible but considered easy to detect. Privacy is principally an execution concern because that is when sensitive user data becomes available.

The paper distinguishes two attacker models:

- **Weak attacker:** app descriptions and schemas are trusted, although app behavior or output may be malicious.
- **Strong attacker:** the attacker controls an app’s implementation, outputs, schema, name, description, and other metadata.

The authors argue that existing defenses do not adequately address the strong model.

### Existing defenses

**f-Secure** separates an LLM planner operating on trusted input from a rule-based executor processing untrusted data. A security monitor applies information-flow-control rules so untrusted execution data cannot affect planning. However, f-Secure trusts app descriptions and schemas, leaving it vulnerable if those representations are malicious.

**IsolateGPT** uses a Hub-and-Spoke architecture. Its hub contains:

- A planner LLM that identifies potentially useful apps.
- An execution-manager LLM that repeatedly chooses which isolated app “spoke” to run next.

Apps execute in isolated environments, and the hub mediates communication between them. Nevertheless, IsolateGPT trusts descriptions during planning and inserts raw app output into the execution-manager LLM’s context. Thus, isolation does not prevent malicious descriptions or outputs from altering system-level control flow. Its reliance on user interaction for app control may also produce user fatigue.

### Table I: coverage of existing defenses

Table I compares protection under weak and strong threat models:

| Phase and objective | IsolateGPT weak | IsolateGPT strong | f-Secure weak | f-Secure strong | ACE weak | ACE strong |
|---|---:|---:|---:|---:|---:|---:|
| Planning integrity | Protected | Not protected | Protected | Not protected | Protected | Protected |
| Execution integrity | Not protected | Not protected | Protected | Not protected | Protected | Protected |
| Execution availability | Not protected | Not protected | Protected | Not protected | Protected | Protected |
| Execution privacy | User-guided | User-guided | Not protected | Not protected | Protected | Protected |

ACE is therefore the only architecture in the comparison designed to protect all four relevant objectives under both threat models.

### Figure 1: architectural contrast

Figure 1a shows a conventional architecture in which a system LLM alternates between planning and execution—for example, deciding to read `file.txt`, receiving its contents, and then deciding to email those contents. The resulting control flow can depend on the user query, app descriptions, and intermediate app responses.

Figure 1b shows ACE. It first creates a complete abstract plan from the trusted query, such as calling an abstract `FileReader` followed by an abstract `EmailSender`. A separate concrete planner maps these independently to installed apps, such as a disk app and email app. A rule-based executor then runs the fixed plan. Untrusted app data is introduced only after the overarching control flow has been established.

---

## 2. Research Goal and Objectives

The paper’s main goal is to design an LLM-app security architecture that prevents malicious installed apps from influencing either the system’s high-level plan or its execution flow, while retaining useful task performance.

The specific objectives are to:

- Protect planning integrity even when app descriptions and schemas are malicious.
- Prevent malicious app outputs from changing execution control flow through indirect prompt injection.
- Prevent execution-integrity and availability failures.
- Enforce privacy policies so sensitive data cannot reach apps or destinations lacking appropriate clearance.
- Eliminate unintended cross-app effects, such as one app manipulating the selection of another.
- Give each plan and app only the minimum capabilities required for its work.
- Maintain high task utility across different LLM configurations.
- Support static reasoning about control and information flow before execution.
- Demonstrate weaknesses in IsolateGPT through concrete attacks and show that ACE blocks those attacks.
- Evaluate ACE against standard prompt-injection and realistic tool-use benchmarks.

---

## 3. Methods (Approach/Design)

### 3.1 New attacks against IsolateGPT

The authors implemented three attacks against the public IsolateGPT system. All use a fare-comparison scenario involving:

- **MetroHail:** treated as the benign fare-calculation app.
- **QuickRide:** treated as malicious.
- A user asking for fares from “Main Street” to “Elms Avenue.”

#### Execution Flow Disruption

A malicious app returns a prompt-like message claiming that all fare-calculation tools are being used for illegal activity. Because IsolateGPT places raw output into the execution-manager LLM’s context, the manager prematurely stops the workflow.

Figure 2 illustrates the result: the plan contains QuickRide and MetroHail, but after QuickRide returns the malicious warning, the manager responds that there is a technical problem and never invokes MetroHail. The attack therefore causes an availability failure and obscures the actual source of the problem.

#### Execution Manager Hijack

A malicious app returns instructions telling the execution manager to report a normal fare for the malicious app and an artificially inflated fare for MetroHail. The app’s spoke repeats the injected instructions, and the execution-manager LLM follows them. This permits one app to corrupt information attributed to another app, causing cross-app interference and an execution-integrity violation.

#### Planner Manipulation

QuickRide inserts a malicious instruction into its app description telling the planner to select QuickRide instead of MetroHail. Because IsolateGPT trusts descriptions during planning, it excludes MetroHail and returns only QuickRide’s result. This allows a malicious developer to promote its own app and demote a competitor without the user’s knowledge.

### 3.2 ACE design principles

ACE follows four principles:

1. **Separate planning from execution.** The core workflow is fixed using trusted information before untrusted descriptions or outputs enter the system.
2. **Remove unintended cross-app interactions.** Whether one app can implement a required function is evaluated independently of unrelated apps.
3. **Enforce data controls within execution paths.** Static, rule-based policies track direct and long-range dependencies so sensitive data cannot reach an unauthorized destination.
4. **Enforce least privilege.** Each component receives only the capabilities it needs.

### 3.3 Three-phase architecture

Figure 3 presents ACE as three successively less privileged phases.

#### Phase 1: Abstract planning

The abstract planner is the most trusted and privileged component. It sees:

- The trusted user query.
- Optionally, a trusted high-level description of the operational environment.

It does **not** see installed app names, descriptions, schemas, or outputs. Consequently, installing a malicious app cannot influence the abstract plan.

The planner generates two artifacts:

- **Abstract apps:** typed interfaces describing required capabilities without implementing them.
- **An abstract plan:** a structured program expressing how those abstract capabilities should be composed.

An abstract app has a name, natural-language description, and input/output type signature. For example, “summarize `file.txt`” may lead to abstract capabilities for loading a document and summarizing text.

The optional operational context must come from a fully trusted source. It can broadly describe available capabilities or the environment, but may not include explicit app metadata or app outputs.

#### Figure 4: abstract-plan example

For a request to load and summarize `file.txt`, the abstract plan:

1. Calls an abstract `DocumentLoader`.
2. Passes the returned string to an abstract `TextSummarizer`.
3. Displays and returns the summary.

Because these abstract apps are generated from the trusted request rather than installed-app metadata, their creation cannot be manipulated by installed apps.

#### Restricted planning language

Plans use a modified subset of Python with a single `main()` entry point. The language supports:

- Basic statements.
- Typed function calls.
- `if` statements.
- Integer-range `for` loops.
- `while` loops whose condition is a single variable.

`break` is forbidden in loops. Programs must define one argument-free `main` function returning a single string. Variables and functions have strict types, enforced both statically and at runtime.

Mutable variables and hidden state are minimized to support referential transparency. Functions must be pure, and mutable collections such as lists, dictionaries, and sets are forbidden.

Table V lists disallowed facilities:

- Built-ins including `open`, `exec`, `eval`, `compile`, `__import__`, `input`, `globals`, `locals`, `vars`, `dir`, `help`, `exit`, `quit`, `getattr`, `setattr`, `delattr`, `super`, and `memoryview`.
- Mutable types: `list`, `dict`, and `set`.
- Dynamic features: lambdas, nested functions, nested classes, and `exec`.
- All imports except `math`.

Abstract-app calls are replaced during compilation with a protected runtime `invoke` operation that communicates with the orchestrator. Plans cannot directly call `invoke`; doing so causes syntax validation to fail.

#### Phase 2: Concrete planning

The concrete planner maps every abstract app to exactly one installed concrete app. The abstract plan plus this mapping forms the executable concrete plan.

Matching has two steps:

1. **Embedding filter:** compare abstract and concrete app descriptions using `text-embedding-ada-002` and Euclidean-distance similarity, then discard irrelevant candidates.
2. **LLM compatibility assessment:** a specialized LLM evaluates whether each remaining app can implement the abstract function, resolving fine-grained semantic and type differences.

A compatibility layer can reconcile differences such as:

- Different argument orders.
- A concrete app returning more outputs than the abstract app needs.
- Other compatible but nonidentical input/output signatures.

Matching decisions are binary and pairwise: each abstract–concrete pair is assessed independently. This prevents one malicious app description from causing another candidate to be excluded.

Different LLMs can be used for abstract planning and concrete matching, allowing cost/performance trade-offs. If several concrete plans are possible, ACE can prioritize those satisfying least-privilege and information-flow requirements.

#### Phase 3: Isolated execution

The executor uses an orchestrator-worker design:

- **Orchestrator:** trusted, privileged process that holds the concrete plan, creates execution environments, assigns permissions, validates schemas and types, routes messages, monitors resources, and terminates workers that exceed limits.
- **Plan worker:** executes the fixed plan in a restricted container. It has no unnecessary file or system-app access and communicates only with the orchestrator through defined socket interfaces. To invoke an app, it makes a blocking request and waits for the orchestrator’s response.
- **App workers:** Dockerized, isolated environments, each containing one app and only the permissions that app needs. They exchange data solely with the orchestrator over defined network sockets.

App outputs are handled as typed data inside the pre-existing program. They are never fed to an LLM that can modify control flow. Apps cannot directly communicate with one another or access arbitrary host resources.

ACE supports standalone applications and single queries. Application suites and multi-query interactions are left for future work.

### 3.4 Static information-flow verification

ACE models privacy and integrity policies as a universally bounded lattice \((C,\sqsubseteq)\), where \(x\sqsubseteq y\) means information labeled \(x\) is allowed to flow into a destination labeled \(y\).

- The **join** \(x\sqcup y\) combines security labels. Data derived from multiple sources becomes at least as restricted as all of them.
- The **meet** \(x\sqcap y\) identifies the highest class that can safely flow to multiple differently cleared destinations.

Figure 7 gives a subset lattice over `{M, F, P}`, representing categories such as medical, financial, and personal. Information can flow upward to equal or more inclusive label sets, but not downward without authorization.

ACE labels:

- The user query, according to user-specified sensitivity.
- Program variables, which are dynamically relabeled as they become “contaminated” by sensitive inputs.
- App memory and resources, which have static security clearances.

All flows are implicitly contaminated by the query label because the plan itself was generated from that query.

The information-flow grammar has three forms:

1. An atomic internal or external information flow.
2. Sequential composition \(S_1;S_2\).
3. A statement \([S]\) executed an arbitrary but finite number of times.

For internal computations, destination variables receive the join of their current labels and all source labels. For external app calls, input data must be permitted to flow into the app’s clearance, and the app’s output is conservatively assigned the app’s clearance. This accounts for apps that may return sensitive information even without explicit sensitive inputs, such as an app retrieving API keys.

For loops, ACE repeatedly propagates labels to a fixed point, capturing leakage that appears only after multiple iterations. The paper relates this to finding transitive closure in an information-flow graph, similar to Warshall’s algorithm. Loop-condition dependencies are injected into all flows in the body. Branch-condition dependencies are similarly inserted into both branches, capturing implicit leakage through control decisions.

#### Figures 5, 8, and 9: detected leaks

- **Figure 5:** financial data loaded by `load_bank_details()` is sent to an email app cleared only for personal data. Static analysis rejects the plan.
- **Figure 8:** a loop first sends a harmless value, then loads bank details. On a later iteration, the bank information reaches `network_send`. Fixed-point loop analysis detects the delayed leak.
- **Figure 9:** secret information controls whether a public variable receives `"0"` or `"1"`. Although the secret is not directly assigned to the output, the output reveals it through the branch decision. ACE detects this implicit dependency.

If no mapping from abstract to concrete apps satisfies the lattice policy, ACE stops with an error instead of running an insecure plan.

### 3.5 Evaluation design

ACE was evaluated along three dimensions:

1. Resistance to the three newly introduced attacks.
2. Security and utility on indirect-prompt-injection benchmarks.
3. Utility, cost, and runtime on a realistic tool-use benchmark.

Models included GPT-4o, o3-mini, GPT-4.1, Claude 3.7 Sonnet, and Qwen-2.5-72B.

#### Prompt-injection datasets

**INJECAGENT** contains 1,054 cases involving:

- 17 user apps.
- 52 attacker apps.
- 544 data-exfiltration cases.
- 510 direct-user-harm cases.

The original benchmark assumes a ReAct agent has already invoked a user tool and tests whether injected output induces another tool call. The authors adapted it so ACE must generate and execute a complete plan for the original query, testing both tool generation and control-flow integrity.

**Agent Security Bench (ASB)** spans:

- 10 agents.
- 10 application scenarios.
- 50 user queries, each requiring one or more tools.

The original agent prompts were used to derive trusted operational context for ACE.

Security was defined as **not invoking designated attacker apps**. Utility was defined as using expected apps:

- INJECAGENT has one expected app per case.
- ASB has two plausible user apps per agent; invoking at least one counts as success.

Utility was decomposed into:

- **Matching success:** an expected concrete app is matched to an abstract app.
- **Execution success:** execution completes without error, conditioned on matching.
- **Overall success:** end-to-end expected-app invocation.

These datasets use trivially simulated apps and do not check output correctness, so their utility measure is limited.

#### Tool Usage benchmark

The LangChain Tool Usage benchmark evaluates complete tool trajectories and final states in three environments:

- **Single Tool:** repeatedly invoke one tool to type a requested word, passing the correct character each time.
- **Multiple Tool:** perform the same typing task using 26 separate argument-free tools.
- **Relational Data:** answer questions over three database tables using 17 tools.

Utility metrics were:

- **Step accuracy:** whether calls occurred in the correct sequence.
- **Overall accuracy:** whether the final output and simulated final environment state were correct.

Cost metrics were:

- Average API price per query.
- Wall-clock runtime.

---

## 4. Results and Findings

### 4.1 The three IsolateGPT attacks succeed

The attacks demonstrate that process isolation alone does not preserve system-level behavior when raw app descriptions and outputs remain part of LLM reasoning.

- **Execution Flow Disruption:** the malicious output causes execution to stop before a benign app runs. The user receives a vague technical-error message rather than the valid benign result or an identification of the malicious app.
- **Execution Manager Hijack:** malicious output changes another app’s reported result, allowing cross-app misinformation.
- **Planner Manipulation:** a malicious description causes the planner to omit a benign alternative without telling the user.

### 4.2 ACE blocks all three new attacks

The case studies report that ACE prevents all three attacks and still produces useful output, regardless of which evaluated LLM is used for abstract and concrete planning.

#### Planner Manipulation

The attack fails because:

- The abstract plan depends only on the trusted query.
- Pairwise matching prevents QuickRide from influencing MetroHail’s eligibility.
- The fixed abstract plan requires both operations, so later malicious output cannot suppress one of them.

Figure 11 contrasts the systems. IsolateGPT selects only QuickRide and reports `$54`. ACE independently maps `MetroHailFareCalculator` to MetroHail and `QuickRideFareCalculator` to QuickRide, then returns both results: MetroHail `51.4` and QuickRide `54.0`.

#### Execution Flow Disruption and Execution Manager Hijack

Both fail because app outputs remain typed values and are never interpreted as new control instructions.

The supplied visual labels appear transposed relative to the attack definitions in the prose:

- **Figure 6**, captioned as a failed “Execution Flow disruption” attack, visually shows the malicious instruction to report QuickRide as `$54` and MetroHail as `$85`, which corresponds to the paper’s Execution Manager Hijack description. IsolateGPT reports the injected values. ACE preserves MetroHail’s output (`51.4`); QuickRide’s incompatible malicious string results in a `TypeError` instead of controlling the system.
- **Figure 10**, captioned as a failed “Execution Manager Hijack” attack, visually shows the warning that fare tools distribute drugs, which corresponds to the prose definition of Execution Flow Disruption. IsolateGPT stops with a technical-error message. ACE continues to invoke MetroHail, reports its fare as `51.4`, and contains QuickRide’s malformed result as a `TypeError`.

Despite this apparent caption/name mismatch, both diagrams support the same central result: malicious natural-language output becomes inert or type-invalid data rather than an instruction that can redirect ACE.

### 4.3 INJECAGENT security

ACE achieved **100% security across all 1,054 INJECAGENT cases**, irrespective of the LLM chosen for abstract and concrete planning. No attacker app named by an injected user-app output was executed.

#### Table II: INJECAGENT utility

| Planner configuration | Category | Matching (%) | Execution (%) | Overall (%) |
|---|---|---:|---:|---:|
| Qwen-2.5-72B | Direct harm | 88.8 | 71.1 | 63.1 |
|  | Data stealing | 86.9 | 66.0 | 57.4 |
|  | Average | 87.9 | 68.5 | 60.2 |
| GPT-4o | Direct harm | 83.3 | 99.3 | 82.7 |
|  | Data stealing | 85.3 | 98.9 | 84.4 |
|  | Average | 84.3 | 99.1 | 83.6 |
| Claude 3.7 Sonnet | Direct harm | 64.6 | 91.2 | 58.8 |
|  | Data stealing | 68.6 | 91.2 | 62.5 |
|  | Average | 66.6 | 91.2 | 60.7 |
| GPT-4o + o3-mini | Direct harm | 84.3 | 99.1 | 83.5 |
|  | Data stealing | 87.7 | 99.4 | 86.9 |
|  | Average | 86.1 | 99.2 | 85.3 |

The strongest average result was **85.3% overall utility** with GPT-4o and o3-mini. GPT-4o alone achieved **83.6%**. Claude 3.7 Sonnet and Qwen-2.5-72B retained approximately **60%** overall utility, with their losses arising from different stages: Claude had lower matching success, while Qwen had substantially lower execution success.

### 4.4 Comparison with StruQ

StruQ is a model-level defense that marks input segments as instructions or data and fine-tunes the LLM to distinguish them. The authors adapted INJECAGENT inputs to include the required delimiters.

- The Mistral-7B StruQ model had a **7% attack success rate**, meaning some security violations remained.
- The Llama-7B StruQ model could not be evaluated because its context window was too small for the test cases.
- ACE instead achieved 100% benchmark security because its plans are structurally restricted to trusted input rather than relying on the model to recognize malicious instructions.

### 4.5 ASB results

ACE achieved at least **86% utility** with GPT-4.1 and GPT-4o.

Across **2,000 trials**, attacker apps were invoked only **three times**. The authors do not classify these as security violations because the selections were unrelated to the injected instructions and the apps genuinely matched the task.

One example asked the system to evaluate risks and returns from investing in a new sector. ACE generated an abstract `MarketDataAnalysis` capability and matched it to an app named `MarketAnalysisTool`, whose stated function was analyzing trading data and supporting investment decisions. The match was semantically appropriate even though the benchmark designated that app as an attacker.

Detailed ASB results were placed in the paper’s extended version and are not included in the supplied text.

### 4.6 Tool Usage utility

#### Table III

| Model configuration | Suite | Step accuracy (%) | Overall accuracy (%) |
|---|---|---:|---:|
| GPT-4o | Single Tool | 100 | 100 |
|  | Multiple Tool | 80.0 | 80.0 |
|  | Relational Data | 66.7 | 81.0 |
| GPT-4.1 | Single Tool | 95.0 | 95.0 |
|  | Multiple Tool | 80.0 | 80.0 |
|  | Relational Data | 76.2 | 85.7 |
| GPT-4o + o3-mini | Single Tool | 100 | 100 |
|  | Multiple Tool | 80.0 | 80.0 |
|  | Relational Data | 47.6 | 66.7 |

ACE achieved at least **80% overall accuracy across all suites** when using GPT-4o or GPT-4.1. GPT-4.1 performed best on relational data, with **76.2% step accuracy** and **85.7% overall accuracy**.

GPT-4o plus o3-mini remained strong on the single- and multiple-tool suites but achieved only **47.6% step accuracy** and **66.7% overall accuracy** on relational data, the most difficult task.

Manual inspection found that ACE generated structured programs with nontrivial control flow. Appendix C gives a GPT-4.1 trace answering whether Bob and Alice live in the same city. ACE generated three abstract capabilities:

1. Find users by name.
2. Retrieve each user’s location ID.
3. Retrieve each city from its location ID.

It called these in the required order, passed identifiers between stages, compared the final city strings with a rule-based conditional, and correctly returned that Bob and Alice did not live in the same city. No LLM decision was needed after the relevant data had been gathered.

### 4.7 Cost and runtime

#### Table IV

| Model | Suite | Cost (USD) | Abstract (s) | Concrete (s) | Execute (s) | Total (s) |
|---|---|---:|---:|---:|---:|---:|
| GPT-4o | Single Tool | 0.01 | 3.02 | 2.15 | 5.65 | 10.84 |
| GPT-4o | Multiple Tool | 0.55 | 6.44 | 8.87 | 5.41 | 19.96 |
| GPT-4o | Relational Data | 0.19 | 8.21 | 4.31 | 3.16 | 15.65 |
| GPT-4.1 | Single Tool | 0.01 | 4.32 | 1.79 | 5.61 | 11.73 |
| GPT-4.1 | Multiple Tool | 0.27 | 4.96 | 10.83 | 5.43 | 20.95 |
| GPT-4.1 | Relational Data | 0.10 | 6.46 | 5.13 | 3.17 | 14.74 |
| GPT-4o + o3-mini | Single Tool | 0.01 | 3.45 | 11.09 | 5.58 | 20.14 |
| GPT-4o + o3-mini | Multiple Tool | 0.49 | 5.14 | 38.78 | 5.04 | 48.00 |
| GPT-4o + o3-mini | Relational Data | 0.11 | 6.29 | 19.30 | 2.80 | 28.24 |

The phases have different overhead sources:

- **Abstract planning** requires two LLM calls: one to generate abstract apps and one to generate the plan. Its monetary cost is relatively insensitive to system configuration, although runtime rises with output length.
- **Concrete planning** may require one comparison for every abstract–concrete app pair. These can be batched to control runtime, but many comparisons increase API cost.
- **Execution** is dominated by creating/configuring Docker containers and orchestrator-worker communication.

The 26-tool Multiple Tool suite intentionally stresses matching and is more demanding than the authors expect typical tasks to be.

For GPT-4.1:

- Single Tool cost only **$0.01** and took **11.73 seconds**.
- Multiple Tool cost **$0.27** and took **20.95 seconds**, despite using all 26 tools.

The paper compares these values with reported IsolateGPT results:

- IsolateGPT took **39.21 seconds** on Single Tool, versus ACE’s **11.73 seconds** with GPT-4.1.
- IsolateGPT reached **126.65 seconds** with 13 tools in Multiple Tool.
- ACE took **20.95 seconds** with all 26 tools.

GPT-4o and GPT-4.1 generally offered better utility and overhead than the GPT-4o/o3-mini combination. The reasoning model o3-mini required more cost and computation without consistently providing better utility.

No statistical significance tests, confidence intervals, or variance estimates are reported in the supplied paper.

---

## 5. Analysis and Interpretation

The results support the authors’ central argument that security must come from system architecture rather than relying on an LLM to recognize which natural-language content is data and which is an instruction.

ACE’s protection derives from three boundaries:

- **Before planning:** the trusted planner cannot observe malicious installed-app metadata.
- **Before execution:** the generated program is statically checked against type, control-flow, and information-flow constraints.
- **During execution:** isolated workers and a privileged orchestrator enforce the plan and least-privilege permissions.

This makes the abstract plan a hard constraint on possible execution traces. Selecting a different implementation for an abstract app may change which concrete utility runs, but it cannot freely replace the program’s overarching logic. App output cannot create new steps or cancel required steps because it is not returned to a planning LLM.

Pairwise independent app matching addresses a different problem: cross-app manipulation. An app can describe itself, but it cannot directly alter whether another app is judged suitable for a required abstract role.

The lattice system extends protection from control flow to privacy. It tracks not only direct assignments but also:

- Data accumulated across long sequences.
- Delayed leakage through loops.
- Information revealed indirectly through branch outcomes.
- Sensitive information that an app might generate from its own internal resources.

The benchmark results show a security–utility distinction. ACE maintained perfect INJECAGENT security across model choices, while utility varied substantially by model. This suggests that plan isolation provides security independently of model capability, whereas correctly generating, matching, and executing useful tools still depends on the underlying model.

The StruQ comparison further illustrates the distinction. StruQ reduces attacks by teaching a model to recognize data boundaries, but still recorded a 7% attack success rate. ACE makes malicious output structurally unable to become a planning instruction.

The Tool Usage results indicate that fixed ahead-of-time plans are not limited to trivial sequences. ACE can generate loops, branches, multi-stage database workflows, and dependencies between tool calls. GPT-4.1’s **85.7% overall relational-data accuracy**, despite lower **76.2% step accuracy**, also shows that some trajectory differences can still lead to a correct final result and system state.

Finally, the overhead results show that concrete matching becomes the dominant cost when many tools or a more computationally intensive matching model are used. Nevertheless, ACE was substantially faster than the IsolateGPT figures quoted for the same benchmark, including when ACE handled twice as many Multiple Tool utilities.

---

## 6. Contributions and Novelty

The paper makes four principal contributions:

- It introduces and demonstrates three attacks against IsolateGPT: Execution Flow Disruption, Execution Manager Hijack, and Planner Manipulation.
- It proposes **Abstract-Concrete-Execute (ACE)**, a three-phase security architecture that fixes control flow using trusted information before interacting with untrusted apps.
- It introduces independent abstract-to-concrete app matching, preventing malicious app descriptions from suppressing unrelated apps.
- It combines a restricted, typed planning language with lattice-based static information-flow analysis, including support for direct flows, branches, loops, and long-range dependencies.
- It provides an isolated orchestrator-worker execution environment with app-specific permissions and typed data interfaces.
- It demonstrates 100% security on all 1,054 INJECAGENT cases and prevention of the paper’s three new attacks.
- It reports high utility on ASB and the LangChain Tool Usage benchmark, including at least 80% overall Tool Usage accuracy with GPT-4o or GPT-4.1.
- It shows that the architectural guarantees are largely LLM-agnostic: model selection changes utility and overhead, but malicious app output remains unable to determine control flow.
- It supplies a public implementation and describes an extended version containing additional results.

---

## 7. Limitations and Caveats

The authors identify several limitations:

- **No full formal soundness guarantee.** ACE uses restricted Python because current LLMs write it well and Python’s AST tools simplify implementation. Python nevertheless has complex runtime semantics, so the authors cannot formally guarantee that the implemented privacy analysis is sound.
- **Restricted scope.** The current system supports standalone apps and single queries. Application suites and multi-query interactions are not supported.
- **Potential plan-worker escape risk.** Sandboxing limits filesystem and network access, but external damage might remain possible through a container escape or carefully constructed messages sent to the orchestrator.
- **Orchestrator visibility.** The orchestrator does not have an explicit view of all plan-worker program state, limiting its ability to verify that every runtime invocation precisely matches a valid trace.
- **Benchmark utility is incomplete.** INJECAGENT and ASB use trivially simulated apps and do not assess correctness of app outputs. Their “utility” metric mainly measures expected-app selection and successful execution.
- **Model-dependent task utility.** Security remained strong across models, but overall INJECAGENT utility ranged from approximately 60% to 85.3%, and relational-data overall accuracy fell to 66.7% with GPT-4o/o3-mini.
- **Matching can be expensive.** Comparing every abstract app with many installed apps can create a multiplicatively large number of LLM queries.
- **Container overhead remains.** Execution time includes Docker setup and cross-container communication.
- **Trusted inputs remain necessary.** The user query and optional operational context must be trusted. The context cannot safely include explicit app metadata or app outputs.
- **Coarse app labels.** App-memory security labels only coarsely represent what data an app may observe.
- **No detailed ASB table in the supplied paper.** The main text gives aggregate utility and the three appropriate attacker-app invocations, but sends full ASB results to the extended version.
- **No reported inferential statistics.** Results are expressed as rates, costs, and runtimes without confidence intervals, variance, or significance tests.
- **Figure-caption inconsistency.** Figures 6 and 10 appear to swap the names of Execution Flow Disruption and Execution Manager Hijack relative to the attack behavior defined in the prose. Their substantive traces still demonstrate containment of both malicious-output patterns.

---

## 8. Future Work or Open Questions

The paper identifies the following next steps:

- Replace restricted Python with a purpose-built domain-specific language having a formal grammar and operational semantics.
- Prove a formal noninterference property connecting the planning language to the information-flow model.
- Extend ACE from standalone, single-query apps to application suites and multi-query interactions.
- Strengthen runtime verification so the orchestrator can better validate plan-worker state, execution traces, and tool invocations.
- Reduce matching cost and runtime as the number of installed apps grows.
- Benefit from future LLM improvements: because ACE is model-agnostic, more capable and efficient models should improve complex-task utility while lowering cost.
- Further develop the general architecture toward provable security for autonomous agents.

---

## 9. High-Level Takeaway (Plain Language)

LLM agents are vulnerable when they repeatedly read an app’s text output and let that text decide what to do next. A malicious app can then act as if it were giving the agent new instructions. ACE avoids this by making a complete, typed plan from the trusted user request first, safely choosing apps to fill the plan, checking where sensitive data may flow, and then executing the fixed plan in isolated containers. In the reported experiments, this design blocked every INJECAGENT attack and all three newly demonstrated attacks while still completing most realistic tool-use tasks successfully.