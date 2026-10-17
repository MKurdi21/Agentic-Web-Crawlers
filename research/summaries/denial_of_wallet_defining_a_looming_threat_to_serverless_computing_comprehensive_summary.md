## Stage 0 — Document Accessibility Report

The supplied work is **Denial of wallet—Defining a looming threat to serverless computing**, by Daniel Kelly, Frank G. Glavin, and Enda Barrett. The main document is available as supplied extracted text for physical PDF pages 1–10. Images of pages 1, 4, 5, 6, 7, 8, and 9 are also supplied and were visually inspected. Pages 2, 3, and 10 were inspected through text only. These distinctions matter: the six numbered figures and Table 1 are on visually supplied pages, whereas the attack taxonomy on pages 2–3 is available through extracted text rather than page rendering.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied text for pages 1–10 |
| Page range and count | Physical PDF pages 1–10; ten accessible text pages |
| Apparent missing main pages | None within the supplied numbered sequence; this does not independently establish whether another version contains additional material |
| Visual coverage | Pages 1, 4–9 visually inspected; pages 2, 3, and 10 text-only |
| Figures | Figures 1–6 supplied visually and inspected |
| Tables | Table 1 supplied in text and a readable page image |
| Equations | No numbered substantive equations found; Table 1 contains dimension notation |
| Appendices | None identified in supplied content |
| Supplementary material | None supplied or explicitly identified as a supplement |
| Referenced external artifacts | Pricing guides, implementation repository, software websites, and cited publications are referenced but not inspected |
| OCR | Not used; supplied extracted text and direct visual inspection were sufficient |
| Limitations | Plot positions support approximate estimates, not exact underlying data; some axis and image-dimension meanings remain ambiguous |

The accessibility metadata is treated as a supplied description, not proof of independent file inspection. The source hash is carried forward exactly as provided and was not independently recomputed. The reported error concerning a local image named '-' does not prevent reading the seven images actually displayed in the prompt. No tools, browsing, repository inspection, external verification, or supplement retrieval were performed.

Evidence labels used throughout are **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information [E] is introduced. Confidence describes fidelity to the supplied evidence, not the probability that a hypothesized attack will succeed in the real world. HIGH means clearly stated or readable; MEDIUM indicates interpretive or approximate support; LOW indicates weak support; UNKNOWN indicates unavailable evidence.

## 1. Plain-language orientation

[A] The paper examines a security problem created by combining automatic expansion of computing capacity with payment based on use. A serverless application runs functions when events occur—for example, when a request arrives or a user uploads an image. Its owner pays for function executions and their resource consumption. An attacker can therefore harm the owner financially by causing repeated, unnecessary executions, even when the application remains available. The authors call this **Denial of Wallet (DoW)**, or forced financial exhaustion. [p. 1, Abstract and §1; p. 2, §3]

The central distinction is between exhausting a service's resources and exhausting its owner's budget. In **Denial of Service (DoS)**, the intended damage is service disruption. In DoW, automatic scaling can keep handling requests while generating an increasingly large bill. The authors describe request volume, execution duration, and additional resource consumption as routes to increasing charges. [p. 2, §3]

[A] The researchers combine a conceptual attack analysis with preliminary demonstrations. They build an isolated OpenFaaS environment, record an unprotected one-hour request flood, test how larger uploaded images increase thumbnail-processing time, and project charges for four commercial serverless platforms. The cost projections are theoretical; the paper does not report an actual victim losing those amounts. [pp. 4–9, §§6–10]

The main quantitative observations are over 130,000 invocations during the unprotected flood, an increase in reported mean image-processing time from 241.818 ms to 9885.918 ms across Table 1's smallest and largest input-size rows, and projected costs of roughly $40,000 after one month for 1000 modeled attack nodes sending 2000 requests per node per hour. [p. 6, §§7–8.1; p. 8, §8.2]

[D] For the user's question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, this paper supplies a relevant infrastructure mechanism: automated web interactions can repeatedly trigger paid computation. It does not study artificial intelligence agents, large language models, prompt injection, or a comparison between agents and standalone models. Its relevance is an analyst inference about possible financial attack surfaces, not direct evidence of comparative LLM vulnerability.

## 2. Document roadmap

The article appears in *Journal of Information Security and Applications*, volume 60, article 102843, with an online availability date of 1 June 2021. The authors are affiliated with the School of Computer Science, National University of Ireland, Galway. The supplied DOI is 10.1016/j.jisa.2021.102843. Keywords are serverless computing, cloud computing, cloud security, denial-of-wallet, and function-as-a-service. [p. 1]

The following inventory is the denominator for the coverage audit:

| ID | Original section or object | Physical pages | Function in the argument |
|---|---|---:|---|
| ABS | Abstract | 1 | Problem, two objectives, simulations, isolated test bed |
| S1 | 1. Introduction | 1 | Serverless execution and financial exposure |
| S2 | 2. Related work | 1–2 | Existing advice and adjacent security research |
| S3 | 3. Defining denial of wallet attacks | 2 | Definition and distinction from DoS |
| SS3.1 | 3.1. Preemptive examination of a threat | 2 | Motivation for investigating a largely unobserved threat |
| S4 | 4. Mechanisms of a potential attack and mitigation strategies | 2–4 | Attack taxonomy and possible defenses |
| SS4.1 | Traditional attack methods | 2–3 | HTTP floods, ReDoS, XML expansion |
| SS4.2 | Short time span attack | 3 | Flooding and rate limiting |
| SS4.3 | Long time span attack | 3 | Persistent low-rate leeches |
| SS4.4 | Distributed denial of wallet | 3 | Multiple attack sources |
| SS4.5 | Adaptive mitigation deception | 3 | Manipulating adaptive traffic baselines |
| SS4.6 | Serverless exploitation | 3 | Storage triggers, input size, memory consumption |
| SS4.7 | Fake users | 3–4 | Automated users and related bot-detection work |
| S5 | 5. Denial of wallet scenarios | 4 | Motivation and execution scenarios |
| SS5.1 | Attack motivation | 4 | Startup sabotage and political scenarios |
| SS5.2 | Attack execution | 4 | Direct endpoints versus application-mediated triggers |
| S6 | 6. Isolation zone for denial of wallet attack testing | 4–6 | Safe experimental infrastructure |
| SS6.1–6.6 | Configuration; serverless deployment; web server; security; pricing emulator; attacking nodes | 5–6 | Implementation details |
| S7 | 7. Demonstrating denial of wallet | 6–7 | One-hour flood and qualitative protection comparison |
| S8 | 8. Theoretical damage analysis | 6–8 | Input-size measurements and billing projections |
| SS8.1 | Serverless function input parameter exploitation | 6 | Thumbnail experiment |
| SS8.2 | Cost analysis of excessive function invocation | 6–8 | Four-provider theoretical cost model |
| S9 | 9. Discussion | 8 | Attack characteristics and proposed defenses |
| S10 | 10. Conclusions and future work | 8–9 | Research agenda and distributed-attack conclusion |
| F1 | Figure 1 | 5 | Experimental architecture |
| F2–F4 | Figures 2–4 | 7 | Invocation totals, invocation rate, runtime |
| F5 | Figure 5 | 8 | Function-container replication |
| F6 | Figure 6, three panels | 9 | Costs for 10, 1000, and 10,000 nodes |
| T1 | Table 1 | 6 | Five image-size conditions, five timings each, reported averages |
| DECL | Competing-interest declaration | 9 | Authors' disclosure |
| REF | References 1–26 | 9–10 | Sources cited by the article |

There are no explicitly numbered research questions, hypotheses, algorithms, theorems, or equations. Four analytical activities deserve separate treatment: X1, unprotected flooding; X2, a qualitative protected-flood comparison; X3, image-size runtime measurements; and X4, modeled long-term financial damage. The related bot-detection studies are background, not additional experiments by these authors.

## 3. Background and context

[A] **Serverless computing** is presented as an event-driven deployment model in which the provider manages the execution infrastructure. The developer supplies functions and identifies events that trigger them. The paper uses the event–trigger–action model: an event occurs, a trigger connects it to code, and the function executes the action. Developers retain access to selected settings, including memory allocation and execution timeout. [p. 1, §1]

**Function-as-a-Service (FaaS)** refers to executing these functions with charges tied to execution rather than directly renting the uptime of their underlying machines. The paper explains that functions still run on virtual-machine infrastructure. **Infrastructure-as-a-Service (IaaS)** is the underlying virtual-machine offering; a **virtual machine (VM)** provides an execution environment, while a function container packages the function's execution. The provider manages provisioning and may reuse containers. [p. 1, §1]

**Scaling** means adding execution capacity to accommodate demand. This helps availability but exposes a financial trade-off: handling more requests can mean paying for more work. A **function invocation** is one execution triggered by an event. **Runtime** is the duration of that execution. The authors' cost analysis considers invocation count, runtime, memory allocation, platform allowances, and additional charges such as API calls. [pp. 1–2; p. 8, §8.2]

An **Application Programming Interface (API)** provides a way to invoke functionality. An exposed function endpoint can permit direct requests; alternatively, a web application or storage event can trigger the same paid work. A **Web Application Firewall (WAF)** filters application requests. **Rate limiting** restricts requests, for example by source Internet Protocol (IP) address. A **Sybil** is a fake user identity; the paper connects fake identities to automated application interactions. [pp. 2–4, §§2, 4–5]

The authors distinguish their proposed low-rate **leech** from slow DoS techniques such as Slowloris and R-U-Dead-Yet (RUDY). Existing slow DoS examples aim to occupy connection resources. A DoW leech instead keeps causing billable executions over a long period while trying to resemble normal traffic. [p. 3, §4.3]

## 4. Research problem and gap

[A] The existing problem is that useful serverless features—automatic scaling, event-triggered execution, and usage-based payment—can also support intentional financial exhaustion. The authors define DoW as intentional mass and continual invocation of functions resulting in inflated bills and financial exhaustion. Their framing makes the application owner's finances the protected asset. [p. 2, §3]

According to the authors, prior blogs and security-risk lists described the danger but did not provide an academic analysis of DoW. This is their literature-positioning claim at the time of writing, not an independently verified statement about all research before or after 2021. They also report an absence of publicly known major attacks and frame their work as preemptive investigation. [pp. 1–2, §§2–3.1]

The paper reviews advice including efficient functions, timeout limits, disk limits, API throttling, access controls, and avoiding application-layer DoS weaknesses. It argues that these are starting points rather than complete solutions. Efficiency does not eliminate accumulated long-term consumption; restrictive resource limits may replace financial exhaustion with service disruption; and access control can fail when attackers obtain ordinary user accounts. [p. 2, §2]

The methodological gap is also practical. Real attacks on commercial platforms could create actual charges, while historical attack traces are unavailable according to the paper. An isolated execution environment with a pricing emulator provides a way to generate attack-related observations without paying the projected commercial attack bill. [p. 4, §6; p. 8, §10]

The scope is serverless financial abuse and possible mitigation. It is not a validated universal detection system, an incident investigation, a systematic literature review, or an AI-agent security benchmark. [D] Its combination of threat definition, architecture, and preliminary experiments makes it a cybersecurity and computer-systems paper with exploratory empirical components.

## 5. Research questions / objectives / hypotheses

The abstract states two explicit objectives: first, provide a concise, informative overview of the emerging attack paradigm; second, establish a starting point for researchers and service providers to create mitigation strategies. It also identifies simulated damage experiments and an isolated test bed as supporting activities. [p. 1, Abstract]

The introduction adds two practical aims: evaluate potential financial damage across AWS Lambda, Google Cloud Functions, Microsoft Azure Functions, and IBM Cloud Functions; and devise a safe means of testing DoW through serverless-platform emulation. [p. 1, §1]

| Inventory ID | Objective | Evidence supplied |
|---|---|---|
| O1 | Define and explain DoW and its potential attack patterns | Definition and taxonomy, §§3–5 |
| O2 | Provide a foundation for mitigation research | Test-bed architecture and proposed defense directions, §§6, 9–10 |
| O3 | Illustrate financial damage across four platforms | Pricing emulator and Figure 6, §§6.5, 8.2 |
| O4 | Support safe experimentation | Four-desktop isolated environment, §6 and Figure 1 |

No formal research questions or statistically framed hypotheses are stated. The following are organizing questions introduced by the analyst, not questions quoted from the article: can requests produce many executions; can input properties increase execution cost; can persistent distributed requests accumulate large modeled charges; and why might short-term rate limits leave this mechanism insufficiently addressed?

The supplied paper does not pose the user's LLM-comparison question. [D] It can help identify an operational-cost mechanism to examine when web agents invoke paid services, but cannot answer how often agents experience it or whether standalone LLMs are less susceptible under comparable configurations.

## 6. Assumptions / threat model

[A] The victim operates an application whose events trigger serverless functions and whose owner bears usage charges. The adversary's intended harm is inflated spending, potentially accompanied by misleading usage analytics. The paper proposes sabotage of smaller organizations and competitors as motivations; these are hypothetical scenarios rather than documented incidents. [p. 4, §5.1]

The attacker must obtain a way to trigger functions. Scenario 1 assumes scraped or leaked API endpoint URLs and direct HTTP requests. Scenario 2 assumes interaction through the application's normal interface, including fake accounts or uploads, when direct endpoints are obscured or a different event triggers the function. The second route is described as requiring more computing resources and application knowledge. [p. 4, §5.2]

Capabilities considered include repeated requests, persistent low-rate requests, multiple attack sources, automated browser interactions, fake identities, large input files, and inputs that cause expensive computation. The paper also hypothesizes gradual manipulation of adaptive defenses by increasing traffic slowly enough to establish false normal baselines. [pp. 2–4, §4]

The model does not require stealing administrative credentials or compromising the cloud provider. [D] Its main mechanism can use reachable function triggers while the provider faithfully executes and bills work. This is an interpretation of the described scenarios, not a formal trust specification supplied by the authors.

For the flood demonstration, the evaluated condition is explicitly unprotected: one source continuously invokes one function for one hour. For the protected comparison, per-source rate limiting is enabled, but thresholds and detailed outcomes are not reported. For the long-term projections, attack-node counts, requests per node, benchmark runtime, and memory are model inputs; continued successful execution over months is assumed by the scenario. [pp. 6–9]

The supplied work does not define a formal list of excluded capabilities, economic attacker costs, credential-acquisition probabilities, or detection probabilities. It also does not quantify the probability that an owner will mistake attack traffic for business growth. Such omissions limit how far its hypothetical sabotage narrative can be treated as measured evidence.

## 7. Methodology

### Study design and architecture

[A] Four desktop PCs share a network. One is the victim, hosting the serverless platform and pricing emulator; three are attacker machines. The victim runs Ubuntu 18.04 and OpenFaaS. A mock web front end runs on Apache Server 2. ModSecurity v2 protects the application server, while Snort v2 supplies intrusion-prevention filtering for the serverless deployment. [pp. 4–5, §§6–6.4]

OpenFaaS supplies function execution and automatic scaling. The paper describes its PLONK stack: Prometheus for metrics/time series; Linux for the operating-system or service-mesh layer; OpenFaaS for compute management and scaling; NATS for asynchronous messaging; and Kubernetes for clustering. Functions are packaged as Docker containers or Open Container Initiative (OCI)-format images. The gateway is accessible through a representational state transfer (REST) API, command-line interface (CLI), or user interface (UI). [p. 5, §6.2]

The front end invokes functions through an API gateway, using HTTP requests and JavaScript Object Notation (JSON). Prometheus collects metrics used by the gateway and autoscaling. Grafana is named alongside Prometheus in the flood demonstration's monitoring description. [p. 5, §6.2; p. 6, §7]

### Security configuration

ModSecurity provides application monitoring, access control, HTTP logging, passive assessment, and hardening. The authors use it primarily against attacks such as XML and shell injection. Snort examines traffic and, in inline mode between bridged interfaces, can drop packets matching rules while forwarding others to Apache or OpenFaaS. Per-IP rate limiting is the defense used in the flood comparison. Exact rules, thresholds, and false-positive measurements are not supplied. [pp. 5–6, §6.4]

### Pricing emulator

The Python emulator converts OpenFaaS usage metrics into hypothetical charges for the four named providers. It queries Prometheus for successful invocations and cumulative execution time. Section 6.5 says all functions are configured to 128 MB, allowing aggregated costs without distinguishing individual function executions. A GitHub implementation URL appears in footnote 16, but its code was not supplied or inspected. [p. 6, §6.5]

Section 8.2 separately describes a calculator accepting request count, per-function runtime, and memory allocation, including free allowances and API charges. Its damage benchmark uses 512 MB, based on the image experiment. The paper does not explicitly explain how the 128 MB aggregate-emulator configuration was changed or related to this 512 MB scenario. This is an unresolved methods-description boundary, not proof that the calculations are wrong. [pp. 6–8, §§6.5, 8.2]

### Workloads and data

Attacking machines can run a Python script sending multiple GET requests and changing the machine's IP address to simulate attack nodes. Kali Linux and Low Orbit Ion Cannon (LOIC) are used for the flood demonstration. The image experiment runs an AWS Lambda function resizing uploaded images to 128 × 128 pixels and storing thumbnails in a separate S3 bucket. [p. 6, §§6.6–8.1]

There is no training dataset, train/validation/test split, participant sample, learned model, or classifier evaluation in the authors' experiments. The experimental data are usage time series and five timing measurements at each of five image-size conditions. Hardware CPU, physical RAM, network bandwidth, function source details, image encoding, random seeds, and confidence intervals are not specified in the supplied text.

## 8. Experiments / analyses

### X1 — Unprotected one-hour HTTP flood

Purpose: demonstrate that an available function can be repeatedly invoked and that the serverless platform scales in response. One Kali Linux node runs LOIC against one OpenFaaS function for one hour. Metrics include total invocations, invocation rate, average runtime, and container replicas. Figures 2–5 all describe the no-protection condition. [pp. 6–8, §7]

[A] The authors report over 130,000 invocations. [B] Figure 2 rises to approximately 132,000, and Figure 5 reaches 20 replicas with a brief interruption. Runtime is generally about 0.24 seconds in Figure 4. These are graphical observations; exact samples are unavailable. The experiment establishes local execution activity under an intentionally permissive condition, not an actual commercial-provider loss.

### X2 — Protected flooding comparison

The authors say they ran LOIC again with the intrusion-prevention system activated and limited damage from one source through rate limiting. They conclude that short-span, single-node flooding is not a suitable effective DoW strategy when such protection operates. [p. 6, §7]

No separate protected-run graph, invocation total, cost total, rate threshold, duration, or statistical comparison is supplied. Thus the protected comparison is author-reported qualitative evidence. It should not be converted into a measured percentage reduction or a guarantee of complete protection.

### X3 — Increasing image-size runtime

An AWS Lambda function resizes S3-uploaded images to 128 × 128-pixel thumbnails. Memory is held at 512 MB because the authors found lower allocations could not handle the largest images. Five source-size conditions have five test runtimes each. Mean runtime increases monotonically across the conditions. [p. 6, §8.1 and Table 1]

The manipulated variable is image size as listed by the table; the outcome is runtime in milliseconds. Target thumbnail dimensions and memory are controlled. Source-size notation is ambiguous: the column is headed l × w (px), but rows contain single numbers rather than explicit dimension pairs. Therefore this report preserves row labels 540, 1080, 2160, 4320, and 8640 without silently asserting their precise geometry.

### X4 — Long-term theoretical cost analysis

The authors use 2950 ms at 512 MB as a benchmark for a plausible image-processing function, then model repeated invocation across AWS, Google, Azure, and IBM. Figure 6 has separate panels for 10, 1000, and 10,000 attack nodes sending 2000 requests every hour. Its caption and node-based interpretation support reading this rate as per node. [pp. 6–9, §8.2 and Figure 6]

The prose reports roughly $40,000 for 1000 nodes after one month and $400,000–$500,000 after a year. The discussion describes up to $50,000 in one month. These are theoretical scenario outputs, not measurements from deploying a real 1000-node botnet. The paper supplies no uncertainty interval or provider-by-provider numeric table for the projection.

## 9. Results

The strongest direct experimental result is the unprotected workload demonstration: one source generated over 130,000 executions in one hour while OpenFaaS increased replica count. This supports the mechanism that repeated reachable triggers can generate extensive computation. Its condition is crucial: no protection was active in the published plots. [p. 6, §7; pp. 7–8, Figures 2–5]

The image experiment demonstrates another cost lever. Reported mean times are 241.818, 379.044, 1057.188, 2950.868, and 9885.918 ms for the five increasing row labels. [C] Comparing endpoints gives 9885.918 / 241.818 ≈ 40.882 times the runtime, with an absolute difference of 9644.100 ms. This is an analyst-derived ratio and difference, not an author-reported improvement, and it applies only to the measured input conditions at 512 MB. [p. 6, Table 1]

The theoretical projections rank Google Cloud Functions highest in charges, followed by AWS Lambda, IBM Cloud Functions, and Microsoft Azure Functions. Figure 6 is visually consistent with this ordering. The result belongs to the paper's historical pricing model and workload; it is not a current pricing comparison or an intrinsic ranking of platform security. [p. 8, §8.2; p. 9, Figure 6]

[C] At the stated rate, one modeled node sends 2000 / 3600 ≈ 0.556 requests per second on average. A 1000-node scenario therefore aggregates to approximately 555.556 requests per second, or 2,000,000 per hour. Low rate per source does not mean low aggregate load. These calculations use only the paper's operands and do not establish whether any particular defense would detect the traffic.

The paper's conclusion that effective attacks will certainly be distributed is stronger than its direct experiments alone establish. [D] The evidence supports distributed persistence as a plausible scenario and one-source flooding as rate-limitable in their setup. It does not establish that every financially serious attack against every realistic application must be distributed. [p. 9, §10]

## 10. Figure-by-figure interpretation

### Figure 1 — Isolated test-bed architecture

[B] The diagram shows three attacker boxes outside a victim-host boundary. GET requests enter Snort. Filtered traffic can proceed to the OpenFaaS platform or to Apache's HTML application page. Apache invokes two depicted Python functions. ModSecurity connects to Apache through security-check arrows. OpenFaaS connects downward to a cost simulator through an arrow labeled Calculate Cost. [p. 5]

There are no numeric axes, error bars, or measured performance values. Red/pink attacker blocks, a purple Apache block, and a blue OpenFaaS block visually separate roles. The two function boxes illustrate deployed functions; the flood text says one function was targeted. This supports architecture understanding rather than proving two-function evaluation.

### Figure 2 — Total function invocations

This purple-line time-series plot has time of function call on the horizontal axis, approximately 13:15–14:15, and number of total function invocations on a linear vertical axis from 0 to 140,000. The cumulative curve increases almost linearly to roughly 132,000. The caption identifies an HTTP flood with no protection. [p. 7]

The endpoint supports the author-reported over-130,000 result. An exact final count is not printed and should not be replaced by a visually guessed integer. No comparison condition or error interval appears.

### Figure 3 — Function invocation rate

The horizontal axis again spans approximately 13:15–14:15. The vertical axis runs from 0 to 40 and is labeled Function Invocation Rate (over 20 second period). The purple line usually lies near 37–38, with a sharp dip to approximately 14 near 13:25 and smaller later dips. [p. 7]

There is a reporting ambiguity. The caption describes rate per 20-second interval, but does not clearly specify whether plotted values are requests per second averaged over that interval or counts within the interval. [C] A total exceeding 130,000 over 3600 seconds implies an average exceeding 36.111 requests per second. This is consistent with the plotted level if it is a per-second rate, but not with approximately 37 raw invocations per 20 seconds. The supplied evidence does not resolve the axis definition; this report retains the uncertainty rather than silently relabeling it.

### Figure 4 — Average function runtime

The same hour is shown horizontally. The vertical axis spans approximately 0.16–0.26 and is labeled Function Average Runtime (over 20 second period). Values usually fluctuate near 0.24, with a conspicuous dip near 13:25 to about 0.166. [p. 7]

[D] Seconds are the plausible intended duration unit, but the axis does not clearly print a standalone unit. Consequently, approximately 0.24 seconds is an interpretation of the runtime graph, not an exact table value. The caption says averages per 20-second interval. There are no error bars, sample counts per point, or explanations for the dips.

### Figure 5 — Function-container scaling

The plot uses time from approximately 13:15–14:15 and a linear vertical axis labeled Num Function Replicas from 0 to 25. The purple trace begins near one, climbs stepwise to 20, drops briefly near 13:25 to roughly one, then recovers to 20 and remains there. The caption identifies no-protection HTTP-flood metrics. [p. 8]

This directly illustrates replica generation under load. The ceiling of 20 is observable, but the paper does not specify whether it reflects a configured cap, resource limit, or another mechanism. The synchronized dips in Figures 3–5 are visible; their cause is not established.

### Figure 6 — Long-term leech-attack costs

Three vertically arranged panels represent 10, 1000, and 10,000 nodes. Each horizontal axis spans attack months 1–12. The shared quantity is total cost incurred in USD. Approximate vertical ranges are 0–5000, 0–500,000, and 0–5,000,000, respectively. All axes are linear. [p. 9]

The legend identifies AWS Lambda with purple, Google Cloud Functions with green, Azure Functions with cyan/light blue, and IBM Cloud Functions with orange. Provider identities should be read through the legend because the thin lines are closely spaced. There are no points denoting measured observations, statistical markers, or confidence bands.

[B] Lines rise approximately linearly, with Google highest, AWS next, IBM next, and Azure lowest. Twelve-month endpoints are approximately $4000–$5000 for 10 nodes, $400,000–$500,000 for 1000, and $4–$5 million for 10,000. These are approximate visual estimates; the middle range is also stated in prose. The caption specifies 2000 requests every hour, and the text associates the scenario with the 2950-ms, 512-MB benchmark.

This figure supports modeled accumulation and scaling with node count. It does not show that attacks evade detection for twelve months, that every request succeeds, or that victims actually pay the projected total.

## 11. Table-by-table interpretation

### Table 1 — Image size and thumbnail-processing runtime

The table compares increasing source-image-size row labels under a fixed 512-MB Lambda allocation and a 128 × 128-pixel thumbnail target. It supplies five individual timings and one average per row. All timing columns use milliseconds. [p. 6, §8.1]

| Image-size row, as printed | Test 1 | Test 2 | Test 3 | Test 4 | Test 5 | Reported average |
|---:|---:|---:|---:|---:|---:|---:|
| 540 | 248.27 | 230.51 | 254.77 | 239.32 | 236.22 | 241.818 |
| 1080 | 371.18 | 368.43 | 361.15 | 385.22 | 409.24 | 379.044 |
| 2160 | 1045.59 | 1051.62 | 1083.57 | 1046.05 | 1059.11 | 1057.188 |
| 4320 | 2945.17 | 2958.46 | 2954.22 | 2963.07 | 2933.42 | 2950.868 |
| 8640 | 9901.85 | 9843.55 | 9924.92 | 9877.68 | 9881.59 | 9885.918 |

The column heading is image size l × w (px), yet each row contains a single size label. Neither supplied prose nor the rendering explicitly expands these labels into length–width pairs. They should not be treated as an unambiguous pixel-area count or as confidently established square dimensions.

The lowest mean runtime occurs at 540 and the highest at 8640. There are no ties, missing values, significance markers, confidence intervals, or standard deviations. These conditions are workload comparisons rather than competing algorithms. For example, [C] the 4320 row's arithmetic mean is (2945.17 + 2958.46 + 2954.22 + 2963.07 + 2933.42) / 5 = 2950.868 ms, matching the printed average. The same direct arithmetic check is consistent with the other displayed means.

The monotonic pattern supports the authors' interpretation that larger inputs can increase execution duration. It does not quantify all determinants of image-processing cost because image format, contents, compression, library implementation, and execution-state effects are not specified.

## 12. Diagram / architecture interpretation

Figure 1 contains two invocation paths. In the direct path, an attacker sends a GET request through Snort to a function exposed by OpenFaaS. In the application-mediated path, filtered traffic reaches Apache, and application activity invokes functions. ModSecurity checks the Apache application path; Snort provides the upstream filtering described in the implementation. [p. 5, Figure 1 and §§6.1–6.4]

The cost simulator is downstream of execution accounting. The diagram labels its connection Calculate Cost, while §6.5 explains that the actual accounting uses Prometheus metrics. [D] It is therefore reasonable to read this as a measurement/accounting relationship rather than a simulator that authorizes every incoming invocation.

The diagram's important security lesson is that protecting the front end and protecting directly reachable function endpoints are separate implementation concerns in this test bed. The authors explicitly split the security system because a single catch-all solution was difficult to deploy locally. [p. 5, §§6.1, 6.4]

No algorithmic decision tree, retry loop, user-authentication sequence, or learned detection feedback loop is depicted. Proposed adaptive-rule deception and reinforcement-learning defenses belong to the conceptual discussion, not to implemented Figure 1 components.

## 13. Equations and mathematical concepts

No numbered equations, optimization objectives, proofs, or mathematical algorithms are present in the supplied paper. The key quantities are invocation count, execution duration, allocated memory, request rate, attack duration, number of sources, and monetary cost.

The l × w notation in Table 1 is intended to describe image dimensions; l and w are not separately defined in the supplied prose. The 128 × 128 notation explicitly specifies thumbnail dimensions in pixels. Memory is reported in MB, runtime in ms, and Figure 6 costs in USD.

[C] A reproducible counting identity useful for interpreting the modeled workload is N = b × r × h, where N is requests, b is modeled nodes, r is requests per node per hour, and h is hours. This identity is an analyst calculation, not a published equation. For b = 1000, r = 2000, and h = 1, N = 2,000,000 requests. It counts attempted workload under the scenario; it does not prove successful execution or billability.

[C] The measured-runtime ratio is R = 9885.918 / 241.818 ≈ 40.882. The absolute change is Δt = 9885.918 − 241.818 = 9644.100 ms. Neither quantity is a percentage-point change. Both compare the largest and smallest Table 1 labels at the reported fixed memory setting.

A provider-specific cost equation cannot be reconstructed faithfully from the article alone. The text identifies relevant inputs and inclusion of allowances and API costs but does not print complete tariffs, billing-rounding rules, regional assumptions, or implemented formulas. External pricing references and code were not inspected.

## 14. Interpretation and discussion

[A] The authors interpret serverless scalability as a potential economic vulnerability: a system may keep serving requests while the owner pays for fictitious demand. They favor persistent, distributed requests and fake-user behavior over conspicuous flooding. They also hypothesize indirect harm when inflated usage persuades an owner to spend more on business expansion. [pp. 4, 8, §§5.1, 9]

Their preemptive objectives are partly addressed. The taxonomy explains candidate mechanisms; the test bed supplies a concrete experimental starting point; the image experiment demonstrates one runtime lever; and the emulator illustrates potential accumulated costs. However, no effective low-rate detector is evaluated, no long-term botnet evasion experiment is reported, and no real financial-exhaustion incident is established.

Several cross-reference issues require explicit preservation:

| Issue | Sources | Assessment |
|---|---|---|
| 128 MB versus 512 MB | §6.5 versus §§8.1–8.2, p. 6 | Local aggregate-emulator configuration and theoretical benchmark differ; transition is not fully explained |
| Invocation-rate unit | Figure 3, p. 7; total in §7, p. 6 | Plot near 37–38 fits per-second rate, not raw count per 20 seconds; exact definition unresolved |
| Source-image dimensions | Table 1, p. 6 | Single labels under l × w heading do not fully specify image geometry |
| Smartphone benchmark | §8.2, p. 6 | 4032 × 3024 photo reference is linked to approximately 2950 ms from another size condition; mapping is not measured explicitly |
| One-month cost | §8.2 and §9, p. 8 | Roughly $40,000 versus up to $50,000; different approximation language, not necessarily a contradiction |
| Tenfold nodes versus twelvefold duration | §8.2, p. 8; Figure 6, p. 9 | Statement that 10,000 nodes match a 1000-node year in one month is approximate; linear scaling alone gives ten rather than twelve times monthly workload |

[C] Ignoring nonlinear allowances, twelve months at 1000 nodes corresponds to 12,000 node-months, while one month at 10,000 corresponds to 10,000 node-months: 10,000 / 12,000 ≈ 0.833. This exposes the approximation rather than supplying a corrected dollar bill.

[D] For agent-security research, the distinction between harmful computation and harmful output is useful. A system that performs paid web actions can create a financial exposure even when no sensitive answer is leaked. But the paper contains no model of autonomous decision-making, tool permissions, or language-model behavior. Those questions remain outside its evidence.

## 15. Contributions and novelty

**Conceptual contribution [A]:** a definition of DoW focused on financial exhaustion and a distinction from serverless resource-exhaustion DoS. The authors frame this as an emerging, underexamined threat. [p. 2, §3]

**Threat-analysis contribution [A]:** a taxonomy covering short-span flooding, long-span leeches, distributed sources, adaptive-defense deception, large-input exploitation, and fake users. Several are proposed attack patterns rather than empirically demonstrated mechanisms. [pp. 2–4, §4]

**Systems contribution [A]:** an isolated OpenFaaS/Apache test bed with separate security components and a pricing emulator for four providers. The design is intended to enable future data generation without the projected commercial attack charges. [pp. 4–6, §6]

**Empirical contribution [A/B]:** a local flood trace and five-condition image-runtime measurements. These provide concrete observations, although neither constitutes a broad security benchmark. [pp. 6–8, §7, §8.1, Figures 2–5, Table 1]

**Analytical contribution [A]:** historical theoretical cost projections under specified invocation, duration, memory, and node-count assumptions. The conclusion describes modeled damage exceeding one million dollars, consistent with the largest Figure 6 scenarios. [pp. 8–9]

No new learned detector, theorem, dataset release with documented schema, evaluated reinforcement-learning algorithm, or comparative AI-agent benchmark is established in the supplied paper. Novelty claims remain the authors' positioning and were not externally validated.

## 16. Limitations

### Authors' stated limitations

[A] The work is preliminary and preemptive, with no known historical DoW examples available according to the authors. This limits access to realistic attack data. [p. 4, §6; p. 8, §§9–10]

They explain that testing financial attacks on real commercial platforms is impractical and that realistic safe test rigs are a barrier. Their isolated environment is presented as progress toward that need. [p. 4, §6; p. 8, §10]

They label the published flood a worst-case condition in which one attacker continuously sends requests without protection. They acknowledge that a WAF can mitigate simple flooding through rate limiting. [p. 6, §7]

They note that very long attacks become more susceptible to discovery, especially during financial analysis, and that application-mediated attacks require more resources and knowledge. These are attack-scenario caveats rather than measured detection probabilities. [p. 8, §9; p. 4, §5.2]

They also report that lower Lambda memory allocations could not process the largest test images, leading to the fixed 512-MB choice. [p. 6, §8.1]

### Additional evidence-based analyst observations

[D] Local OpenFaaS behavior is not automatically equivalent to commercial-provider scaling, scheduling, or runtime. Pricing conversion does not validate behavioral equivalence.

[D] The protected comparison lacks quantitative reporting, so effectiveness cannot be expressed as an exact reduction. Persistent leech attacks, fake-account generation, adaptive-rule deception, and bot-detection defenses are not evaluated in the reported experiments.

[D] Five timings per image-size row establish a small repeated measurement set, but there are no confidence intervals or execution-state controls. The input geometry and smartphone-to-benchmark mapping are incompletely specified.

[D] The cost model omits sufficient printed detail for independent reconstruction without external artifacts. It does not evaluate attacker expenditure, intervention, changing traffic conditions, or twelve-month operational realism.

[D] Direct relevance to web AI agents is limited to an inferred financial mechanism; comparative vulnerability against standalone LLMs is untested.

## 17. Threats to validity

The following validity categories are analyst assessments, not terminology the authors explicitly use.

**Internal validity [D]:** unexplained simultaneous dips in rate, runtime, and replicas complicate causal interpretation of individual time-series features. Missing function implementation and hardware specifications restrict isolation of workload effects. The input experiment controls reported memory and target dimensions, but does not report other execution conditions.

**Construct validity [D]:** invocation count and modeled charges measure pathways to financial harm, not demonstrated financial exhaustion. Misleading business analytics, stealth, and successful long-term evasion are discussed but not operationally measured.

**External validity [D]:** a small local test bed and one thumbnail workload provide limited evidence about the diversity of production functions, provider behavior, and real application defenses. Figure 6 varies scale in a model rather than deploying the corresponding physical botnets.

**Statistical conclusion validity [D]:** no inferential tests, uncertainty intervals, or repeated flood experiments are reported. Table 1 supports a clear descriptive monotonic pattern, but should not be generalized into an estimated population effect with an invented confidence level.

**Ecological validity [D]:** uninterrupted modeled requests across months do not reproduce owner intervention, user activity variation, billing review, or changing defenses. The paper acknowledges possible discovery but does not model its timing.

**Reproducibility [D]:** named versions and a code URL help, but code, exact rules, prices, images, raw traces, and hardware parameters are absent from the supplied evidence. Availability of a cited repository is different from verifying its contents.

**Research-question transfer [D]:** importing these results into an AI-agent-versus-LLM comparison risks confusing an infrastructure property with a demonstrated model property. A controlled comparison would need matched deployment and action capabilities; no such comparison is present here.

## 18. Future work and open questions

### A. Future work explicitly proposed by the authors

The conclusion lists four priorities: classification of fictitious requests; protection against proposed leeches; investigation of serverless-specific weaknesses; and detection and mitigation of fake users. It calls for meaningful data generation before large-scale incidents occur and continued development of realistic isolated simulations. [p. 8, §10]

The discussion proposes common usage graphs for suspicious-user analysis, honeypots discoverable by malicious web scrapers, and reinforcement learning applied to user-interaction graphs. These are possible avenues, not evaluated systems. [p. 8, §9]

The final page proposes investigating Distributed Denial of Wallet alongside existing and future Distributed Denial of Service research. [p. 9, §10]

### B. Additional open questions logically remaining

[D] What false-positive and false-negative rates would a detector achieve against realistic legitimate and fictitious users? What fraction of modeled requests would complete successfully over long periods? How faithfully do local metrics predict commercial executions? How much does input geometry, image encoding, or execution state affect runtime? How do cost controls trade availability against spending limits?

[D] For the user's research question, the remaining question is whether a web AI agent's actual permissions and deployment connect untrusted interactions to paid executions in ways absent from a particular standalone-LLM baseline. This paper suggests examining that boundary, but supplies no answer about relative frequency, exploitability, or effect size.

## 19. Terminology and notation glossary

| Term | Meaning in this analysis |
|---|---|
| DoW | Denial of Wallet: intentional function invocation causing inflated usage bills and financial exhaustion |
| DoS | Denial of Service: disruption through exhausted service resources |
| DDoS | Distributed Denial of Service: DoS involving multiple sources |
| FaaS | Function-as-a-Service: event-triggered function execution with usage-based charging |
| IaaS | Infrastructure-as-a-Service: underlying virtual-machine infrastructure described by the paper |
| Invocation | A triggered function execution |
| Runtime | Time consumed by an execution |
| Autoscaling | Automatically increasing or decreasing execution capacity |
| Container / replica | Packaged execution instance; a replica is an additional instance shown in Figure 5 |
| API / endpoint | Application Programming Interface and its addressable entry point |
| HTTP / GET | Hypertext Transfer Protocol and the request method used in the described scripts/flood |
| WAF | Web Application Firewall: request-filtering protection |
| IP | Internet Protocol; source addresses are used by described rate limits |
| NIDS / IPS | Network Intrusion Detection System / Intrusion Prevention System |
| Snort | Traffic inspection tool used inline for prevention in the test bed |
| ModSecurity | Application-security toolkit protecting Apache |
| OpenFaaS | Framework providing the local serverless platform |
| Prometheus / Grafana | Tools named for collection and presentation of experiment metrics |
| PLONK | Prometheus, Linux, OpenFaaS, NATS, Kubernetes |
| NATS | Asynchronous message bus/queue in the stated stack |
| REST / CLI / UI | Representational state transfer / command-line interface / user interface |
| JSON / YAML | Formats named for communication and function configuration |
| LOIC | Low Orbit Ion Cannon: tool used for the one-hour HTTP flood |
| Sybil | Fake user identity that may interact through normal application features |
| Leech | Proposed persistent, low-rate program triggering billable functions |
| Botnet | Multiple automated attack sources in the proposed scenarios |
| ReDoS | Regular expression Denial of Service: expensive regex evaluation proposed as a runtime lever |
| XML bomb / XEE | Extensible Markup Language entity-expansion attack proposed as another runtime lever |
| CAPTCHA | Challenge named in the related adaptive-defense discussion |
| S3 | AWS storage service named as the upload trigger in the image experiment |
| l × w | Table 1 dimension notation; row geometry remains uncertain |
| px / ms / MB / USD | Pixels / milliseconds / megabytes / United States dollars |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Isolated test-bed machines | 4 | desktop PCs | One victim, three attackers | Author-reported | p. 4, §6 |
| Victim operating system | 18.04 | Ubuntu version | Local environment | Author-reported | p. 5, §6.1 |
| Security versions | 2 | major version | ModSecurity and Snort | Author-reported | p. 5, §6.1 |
| Local aggregate-emulator memory | 128 | MB | §6.5 configuration | Author-reported | p. 6, §6.5 |
| Flood duration | 1 | hour | One node, one target function, no protection | Author-reported | p. 6, §7 |
| Flood invocations | >130,000 | invocations | Same unprotected run | Author-reported | p. 6, §7 |
| Cumulative graph endpoint | ≈132,000 | invocations | Figure 2 end of run | Approximate visual estimate | p. 7, F2 |
| Replicas at plateau | 20 | replicas | Unprotected run | Visually readable | p. 8, F5 |
| Thumbnail target | 128 × 128 | px | AWS Lambda resizing | Author-reported | p. 6, §8.1 |
| Image-experiment memory | 512 | MB | Fixed across Table 1 | Author-reported | p. 6, §8.1 |
| Timing tests | 5 per condition | tests | Five image-size rows | Visually readable | p. 6, T1 |
| Mean runtime, label 540 | 241.818 | ms | Fixed 512 MB | Author-reported | p. 6, T1 |
| Mean runtime, label 1080 | 379.044 | ms | Fixed 512 MB | Author-reported | p. 6, T1 |
| Mean runtime, label 2160 | 1057.188 | ms | Fixed 512 MB | Author-reported | p. 6, T1 |
| Mean runtime, label 4320 | 2950.868 | ms | Fixed 512 MB | Author-reported | p. 6, T1 |
| Mean runtime, label 8640 | 9885.918 | ms | Fixed 512 MB | Author-reported | p. 6, T1 |
| Largest/smallest runtime ratio | ≈40.882 | ratio | 9885.918 / 241.818 | Analyst-derived | p. 6, T1 |
| Runtime absolute increase | 9644.100 | ms | 9885.918 − 241.818 | Analyst-derived | p. 6, T1 |
| Smartphone photo reference | 4032 × 3024 | px | Author-cited iPhone X example | Author-reported | p. 6, §8.2 |
| Cost benchmark runtime | 2950 | ms | At 512 MB; theoretical scenario | Author-reported | p. 6, §8.2 |
| Modeled per-node requests | 2000 | requests/hour | Figure 6 scenarios | Author-reported | pp. 8–9, §8.2/F6 |
| Per-node average rate | ≈0.556 | requests/second | 2000 / 3600 | Analyst-derived | p. 9, F6 condition |
| Aggregate for 1000 nodes | 2,000,000 | requests/hour | 1000 × 2000 | Analyst-derived | pp. 8–9 |
| Cost after one month | roughly 40,000 | USD | 1000 nodes; benchmark workload | Author-reported | p. 8, §8.2 |
| Discussion monthly upper wording | up to 50,000 | USD | 1000 nodes | Author-reported | p. 8, §9 |
| Cost after one year | 400,000–500,000 | USD | 1000 nodes | Author-reported | p. 8, §8.2 |
| Largest-panel annual endpoint | ≈4–5 million | USD | 10,000 modeled nodes | Approximate visual estimate | p. 9, F6 |
| Suggested attack span | 1–6 | months | Authors' conceptual discussion | Author-reported | p. 8, §9 |

Secondary numbers are background, not results of this study. These include the cited five-minute timeout and 100-ms billing granularity, 10,000-request/s API example, estimated Twitter bot prevalence of 9%–15% and approximately 49.5 million accounts, and the cited fake-user studies summarized below. Their historical accuracy was not externally checked. [p. 3, §§4.1–4.7]

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| DoW targets finances through continual invocation | Explicit definition | Conceptual framing | p. 2, §3 | HIGH source fidelity; definition, not prevalence evidence |
| A reachable unprotected function can receive extensive execution load | >130,000 invocations in one hour | X1, F2 | p. 6, §7; p. 7 | HIGH for reported local condition |
| Platform capacity grows during the flood | Replica trace reaches 20 | X1, F5 | p. 8 | HIGH for visible plateau; cause of cap unknown |
| Single-source rate limiting reduces flood damage | Protected rerun described | X2 | p. 6, §7 | MEDIUM empirical detail; no quantitative protected trace |
| Larger inputs increase measured processing time | Five increasing mean runtimes | X3, T1 | p. 6, §8.1 | HIGH descriptive support; geometry ambiguous |
| Persistent distributed requests can produce large modeled costs | Four-provider projections | X4, F6 | pp. 8–9 | HIGH as scenario output; unvalidated real-world persistence |
| Fake-user and adaptive-baseline routes may aid attacks | Threat scenarios | §§4.5, 4.7, 5.2 | pp. 3–4 | Hypotheses, not evaluated bypasses |
| Effective attacks must be distributed | Authors' conclusion | Discussion/conclusion | p. 9, §10 | Author claim stronger than direct comparative evidence |
| Financial exhaustion may be relevant to paid web-agent actions | Inferred trigger-to-cost connection | Analyst transfer | pp. 2–4, 8 | MEDIUM conceptual relevance; no AI-agent experiment |
| Standalone LLMs are comparatively safer | No direct comparison supplied | None | Whole document | UNKNOWN; not established by this paper |

## 22. Very simple explanation

Imagine an application that pays a small amount whenever it performs a task. Its cloud service can automatically add more workers when many tasks arrive. That keeps the application useful during busy periods, but it also means someone can deliberately create work that the owner must pay for. This paper calls that Denial of Wallet.

The researchers showed that an unprotected function could be triggered more than 130,000 times in an hour. They also measured a thumbnail-making function and found that larger input images took longer to process. More executions and longer executions are two ways the bill can grow.

Their largest dollar figures come from a calculator using assumed attack rates and function settings. They did not observe a business actually lose millions of dollars. The paper argues that many sources sending requests slowly could be harder to recognize than one obvious flood, but it does not test a finished detector against such a long-term attack.

For web AI agents, the possible connection is that web actions can cause paid work. If an agent's deployment lets interactions repeatedly trigger that work, spending becomes something security analysis should examine. This paper does not test agents or standalone language models, so it cannot establish that one is generally more vulnerable than the other.

## Completeness Audit

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract and metadata | Yes, text and visual | Yes | Fully represented | Two objectives, authors, venue, keywords, date |
| §1 Introduction | Yes, text and visual | Yes | Fully represented | Execution, charging, scale, four platforms |
| §2 Related work | Yes; p. 2 text-only | Yes | Represented in compressed form | Prior advice, workflow monitoring, adaptive defenses |
| §3 Definition | Yes, text-only | Yes | Fully represented | Financial target and resource-cost mechanisms |
| §3.1 Preemptive examination | Yes, text-only | Yes | Fully represented | Historical absence is author-reported |
| §4 overview | Yes, text-only | Yes | Fully represented | Proposed taxonomy versus demonstrated attacks |
| §4.1 Traditional methods | Yes, text-only | Yes | Represented in compressed form | HTTP flooding, regex complexity, XML expansion |
| §4.2 Short-span attacks | Yes, text-only | Yes | Represented in compressed form | WAF rules, false positives, DoS trade-off |
| §4.3 Long-span attacks | Yes, text-only | Yes | Fully represented | Leeches differ from connection-locking slow DoS |
| §4.4 Distributed attacks | Yes, text-only | Yes | Fully represented | Multiple sources and botnets |
| §4.5 Adaptive deception | Yes, text-only | Yes | Fully represented | False normative baselines; not evaluated |
| §4.6 Serverless exploitation | Yes, text-only | Yes | Represented in compressed form | Storage uploads and input size; authors also propose Azure memory exploitation |
| §4.7 Fake users | Yes; p. 3 text-only, p. 4 visual | Yes | Represented in compressed form | Automation plus three detection categories |
| §5.1 Motivation | Yes, text and visual | Yes | Represented in compressed form | Startup and political sabotage are hypothetical |
| §5.2 Execution | Yes, text and visual | Yes | Fully represented | Scraped endpoints and application-mediated triggers |
| §6 overview | Yes, text and visual | Yes | Fully represented | Four-machine safe environment |
| §6.1 Configuration | Yes, text and visual | Yes | Fully represented | Ubuntu, OpenFaaS, Apache, security versions |
| §6.2 Serverless deployment | Yes, text and visual | Yes | Represented in compressed form | PLONK, packaging, gateway, HTTP/JSON |
| §6.3 Web server | Yes, text and visual | Yes | Represented in compressed form | Compatibility catalogue compressed |
| §6.4 Security | Yes, text and visual | Yes | Fully represented | ModSecurity roles and inline Snort |
| §6.5 Pricing emulator | Yes, text and visual | Yes | Fully represented | Python, metrics, 128 MB, uninspected code URL |
| §6.6 Attacking nodes | Yes, text and visual | Yes | Fully represented | GET script, changed IP, Kali/LOIC |
| §7 Demonstration / X1 | Yes, text and visual | Yes | Fully represented | One-hour no-protection condition |
| Protected comparison / X2 | Yes, text | Yes | Fully represented | Quantitative outcomes unavailable |
| §8.1 / X3 | Yes, text and visual | Yes | Fully represented | All 25 timings and five averages preserved |
| §8.2 / X4 | Yes, text and visual | Yes | Fully represented | Benchmark, providers, node rates, charges |
| §9 Discussion | Yes, text and visual | Yes | Fully represented | Proposed attack traits and defenses |
| §10 Conclusion/future work | Yes, text and visual | Yes | Fully represented | Four priorities and distributed conclusion |
| O1–O4 objectives | Yes | Yes | Fully represented | No formal RQ numbering in original |
| Formal hypotheses | Not present | Absence stated | Missing from supplied material | No statistical hypotheses invented |
| F1 architecture | Yes, visual | Yes | Fully represented | Components and both invocation paths |
| F2 cumulative invocations | Yes, visual | Yes | Fully represented | Exact count unavailable |
| F3 invocation rate | Yes, visual | Yes | Uncertain | Rate normalization unresolved |
| F4 runtime | Yes, visual | Yes | Uncertain | Duration unit not clearly printed |
| F5 replicas | Yes, visual | Yes | Fully represented | Plateau visible; cap mechanism unknown |
| F6, all three panels | Yes, visual | Yes | Fully represented | Approximate endpoints identified |
| T1 | Yes, visual and text | Yes | Fully represented | Dimension-row interpretation uncertain |
| Equations/theorems | None identified | Absence stated | Missing from supplied material | Analyst identities labeled separately |
| Algorithms/pseudocode | None identified | Absence stated | Missing from supplied material | Scripts described, code not supplied |
| Major contributions | Yes | Yes | Fully represented | Conceptual, systems, empirical, analytical |
| Authors' caveats | Yes | Yes | Fully represented | Preliminary evidence, safe testing, discovery, worst case |
| Appendices | None identified | Absence stated | Missing from supplied material | No appendix review claimed |
| Supplements | None supplied | Absence stated | Missing from supplied material | No supplement review claimed |
| References 1–26 | Yes, text | Yes | Represented in compressed form | Citation roles retained; external works not reviewed |
| Footnotes 1–21 | Yes, text | Yes | Represented in compressed form | Mostly service, software, code, pricing URLs |
| Competing-interest declaration | Yes | Yes | Represented in compressed form | Authors report no known competing interests |
| Publisher logos, journal cover, page furniture | Yes where rendered | Accounted for | Inspected but deliberately omitted as non-substantive | No analytical content attributed to decoration |

### Missing or inaccessible material

No main page within the supplied 1–10 sequence is missing as text. Visual renderings for pages 2, 3, and 10 were not supplied. External cited publications, software documentation, current or historical pricing pages, and the pricing-emulator repository were not inspected. Raw experiment traces, exact protected-run results, detailed hardware configuration, function implementations, full pricing formulas, and source-image files are not supplied. No appendix or supplement was identified; their absence must not be described as a successful review.

### Uncertain interpretations

The main unresolved readings are Figure 3's rate normalization, Figure 4's explicit duration unit, Table 1's single-number dimension labels, the 128-MB-to-512-MB modeling transition, and the mapping from a 4032 × 3024 reference photograph to the approximately 2950-ms benchmark. Causes of the synchronized plot dips and the 20-replica plateau are unspecified. Dollar endpoints read from Figure 6 are approximate. The tenfold-node/one-month versus twelve-month comparison is an approximation rather than an exact workload equality.

### Deliberately compressed material

Related-work numerical examples are secondary evidence attributed by this paper to other studies. The supplied §4.7 reports SybilWalk's 99% among the top 80,000 ranked nodes, compared with 0.3% for SybilRank and 30% for CIA; a crowd-labeling study with 10 volunteers and 2000 accounts; and a Naïve Bayes study with 86.1% classification before Entropy Minimisation Discretisation and 90.9% afterward. These are not reproduced as comparable benchmarks or results of Kelly and colleagues. [p. 4]

The six recommendations from related work are grouped rather than repeatedly quoted. ReDoS and XML expansion are explained as runtime-increasing candidates; the XML example's ten levels of tenfold entities leading to one billion copies and the paper's historical timeout/billing examples are secondary illustrations. Network-level flood names—ICMP, SYN, and UDP—are grouped as attacks the authors consider less directly applicable to function triggers. The Apache operating-system compatibility catalogue, individual service URL patterns, bibliography formatting, contact details, and license metadata are compressed because they do not change the experiment interpretation.

The startup and political scenarios are condensed while preserving their hypothetical status, inflated bills, false analytics, and possible secondary spending. OpenFaaS's ease-of-use, portability, language support, CLI templating, and autoscaling features are represented through the implementation explanation rather than copied as promotional lists. The competing-interest statement reports no known competing financial interests or personal relationships influencing the work. Decorative publisher material is accounted for but excluded from scientific interpretation.

### Potential omissions

Every substantive numbered section, subsection, experiment/analysis, figure, table, objective, major contribution, and author caveat identified in the supplied inventory is represented, with secondary material explicitly compressed. Remaining gaps concern unavailable artifacts, ambiguous reporting, and the absence of a direct AI-agent-versus-standalone-LLM comparison. The analysis is comprehensive with respect to the supplied inventory; it does not claim access to every referenced artifact or preservation of every sentence.
