# YURASCANNER: Leveraging LLMs for Task-driven Web App Scanning

**Authors:** Aleksei Stafeev, Tim Recktenwald, Gianluca De Stefano, Soheil Khodayari, and Giancarlo Pellegrino  
**Affiliation:** CISPA Helmholtz Center for Information Security  
**Published at:** Network and Distributed System Security Symposium (NDSS) 2025

## 1. Background and Context

Web application scanners are automated black-box security-testing tools. Starting from a seed page, they crawl a running application, interact with links, buttons, and forms, and inject test inputs into discovered endpoints. Unlike static analysis, which inspects source code, dynamic scanners test behavior during execution. This can produce concrete proof-of-concept inputs with few or no false positives.

A scanner normally contains:

- A crawler that discovers pages, URLs, forms, request parameters, and other inputs.
- An attack module that tests those inputs with known attack payloads and monitors the application for evidence that a vulnerability was triggered.

The central problem is crawling. Existing scanners generally do not understand an application’s workflows. Breadth-first search (BFS), randomized BFS, and similar navigation methods treat available actions without considering application logic. Consequently, they may visit many shallow pages but rarely perform the precise action sequences needed to reach deeper states.

For example, a scanner cannot test a checkout form unless it first adds a product to a cart. Likewise, Figure 1 shows a real cross-site scripting (XSS) vulnerability in the anonymized application **Redacted** that required six ordered actions:

1. Click **Tools**.
2. Click **Entities**.
3. Click **Entity Management**.
4. Click **Create**.
5. Fill the creation form, including **Parameter B**.
6. Click **Save**.

Parameter B lacked server-side validation and sanitization. Traditional crawlers failed to reach it because they could not reproduce this six-step workflow.

Previous state-aware approaches include learned state machines, reinforcement learning, manually supplied interaction traces, and login scripts. These approaches have limited transferability: models or traces created for one application or workflow generally do not carry over to another, while manually describing tens or hundreds of workflows is expensive. Other LLM browser agents, such as Natbot, use overly fine-grained actions and often reason only from the current page, which can lead to endless navigation loops and failure on multi-step workflows.

The paper’s premise is that large language models may already have broad semantic knowledge of common software functions and workflows from publicly available documentation. If pages, actions, objectives, and history are represented semantically, an LLM may be able to choose actions without application-specific training.

## 2. Research Goal and Objectives

The paper introduces **YURASCANNER**, one of the first fully automated, task-driven web application scanners. It models crawling as the behavior of a rational, goal-based agent: given a task, the current page, and recent history, the agent chooses the action most likely to move toward the goal.

The broader objective is to determine whether task-driven crawling can reach application states missed by conventional crawlers and thereby expose previously unknown vulnerabilities.

The paper asks five research questions:

1. **RQ1—Automated task extraction:** How can a scanner identify a comprehensive catalog of tasks and workflows from a web application?
2. **RQ2—Automated task execution:** Given a task, how can a scanner perform it automatically, including multi-step and state-dependent interactions?
3. **RQ3—Attack-surface coverage:** How does task-driven crawling affect the number of URLs and forms discovered?
4. **RQ4—Attack-surface characterization:** How does the newly discovered surface relate to task depth and workflow complexity?
5. **RQ5—Vulnerability detection:** Does task-driven exploration uncover vulnerabilities missed by traditional scanners?

The intended outcome is not to replace conventional crawling, but to determine whether goal-directed exploration complements its broader, shallower coverage.

## 3. Methods (Approach/Design)

### Overall system

Figure 2 presents a three-stage pipeline:

1. **Task extraction:** Shallowly crawl a web application, extract page elements and semantic cues, and ask an LLM to generate task prompts.
2. **Task execution:** Use an LLM-directed browser agent to carry out those tasks.
3. **Vulnerability scanning:** Record the URLs, forms, and action sequences found during execution, replay the sequences, and dynamically test the forms with XSS payloads.

YURASCANNER was implemented in JavaScript using Node.js. It takes a web application URL and optionally one task or a task list. If no tasks are supplied, it automatically generates a task catalog.

It communicates with models through the OpenAI SDK. Changing the SDK’s `base_url` permits compatible open-source serving systems such as FastChat with a VLLM backend. The authors compared GPT-4, Llama3-8B, Gemma2-9B, and Gemma2-27B on 20 randomly selected tasks in Redacted. GPT-4 had the highest execution success rate and was selected for the main evaluation; the paper does not report the four models’ individual numeric rates.

### Task-execution agent

Figure 3 models the crawler as three cooperating modules:

- **Sensors** turn the current rendered browser page into a concise semantic abstraction.
- **The Bridge** uses an LLM to choose the next high-level action based on the task, current page, and recent history.
- **Actuators** execute that action in the browser.

These modules repeat until the Bridge issues `STOP`.

#### Sensors and page abstraction

After each page load, the sensors snapshot the rendered Document Object Model and identify user-interactable elements:

- Anchor tags
- Buttons
- Button and submit inputs
- Elements with `onclick`
- HTML forms
- Elements with dynamically registered JavaScript handlers

To capture event-driven elements, YURASCANNER reuses and modifies event-registration hooking from jÄk and Black Widow. The modified hooking records the HTML element on which a handler was registered.

The sensor removes:

- Hidden or occluded elements
- Elements with empty labels
- Elements whose textual representation is too large for useful LLM input

Each remaining action receives a unique, incrementing, per-page integer ID. The **Action Mapping** associates that ID with the concrete JavaScript `HTMLElement`, allowing the actuator to find it later.

Semantic labels are selected from the first nonempty source in this order:

1. Accessibility attributes such as `aria-label`
2. Advisory attributes such as `title`
3. Element text such as `innerText`
4. Default displayed values such as `value`

For forms, the abstraction preserves the form name—or its ID if no name exists—plus its `action` and HTTP `method`. Endpoint names can imply purpose, while the method can indicate whether submission is likely to change state. Other attributes are removed to keep prompts concise.

An abstract action retains the tag name, generated ID, and semantic string. An abstract page contains the URL, page title, and list of abstract actions.

#### The Bridge and memory

The Bridge predicts one command:

- `CLICK X`
- `FILL & SUBMIT FORM X`
- `STOP`

Figure 4 shows its three-part prompt:

1. A preamble assigning the persona “Yura, an agent controlling a web browser,” defining the available commands, page representation, task, and expected response format.
2. One worked example containing an abstract page, task, recent steps, and appropriate next command.
3. The actual query containing the current abstract page, task, and recent action history.

The prompt uses one-shot prompting and persona assignment to improve instruction following. The actual query repeats the persona reminder because the model tended to lose focus after several actions. Only one command is allowed per response.

After choosing an action, the Bridge saves the page and selected action in local memory. Empirical tests found that retaining the previous **six actions** balanced accuracy and prompt size.

#### Actuators

For `STOP`, the current task ends and the next task begins.

For `CLICK X`, the actuator resolves the ID through the Action Mapping and triggers the element through Puppeteer’s `click()` function. To avoid managing multiple browser tabs, it replaces anchor targets such as `_blank` or `_top` with `_self`. It then waits **five seconds** for JavaScript execution and navigation; this delay is configurable.

Form filling is handled as a high-level action because preliminary work found that asking the Bridge to issue separate field-filling and submission commands overloaded the prompt and reduced compliance and completion. Instead:

1. The Bridge chooses `FILL & SUBMIT FORM X`.
2. The actuator sends the form to a separate LLM prompt.
3. This “FormGPT” prompt, shown in Figure 5, requests one or more `TYPE X "text"` commands for text fields.
4. The actuator fills and submits the entire form.

Non-text controls are handled algorithmically because the LLM did not reliably operate them:

- All unchecked checkboxes and radio controls are clicked.
- For a drop-down with multiple options, the second option is selected to avoid invalid first entries such as “Please select a country.”

### Automated task generation

YURASCANNER can use manually supplied tasks, but the paper investigates automatic generation.

Starting from the seed URL, it performs a crawl of **depth one**, gathers primary pages, and extracts menu, link, button, and other interactable text. Elements already observed on earlier pages are excluded to reduce duplicate tasks.

An LLM turns these labels into short imperative tasks consisting of a verb and direct object, such as “Create a new user account.” Figure 6 shows that the prompt explicitly asks for tasks involving adding, editing, and deleting items and requests short, direct descriptions.

Tasks are sorted according to basic CRUD dependencies—Create, Read, Update, Delete—because, for example, an object normally must be created before it can be edited or deleted.

### XSS testing

YURASCANNER integrates Black Widow’s XSS engine rather than developing a new vulnerability oracle.

For every form and payload, the engine defines an oracle function `xss(id)`, generates a unique ID, and injects a payload that calls this function.

It operates in two modes:

- **Safe mode:** inject into text, textarea, password, and email fields.
- **Aggressive mode:** if safe injection fails, also test hidden fields, radio buttons, checkboxes, select controls, and file-upload fields.

During task execution, YURASCANNER records:

- URLs containing forms
- Form positions
- Exact concrete action sequences used to reach each form

After execution, it restarts from the seed URL, replays the sequence to each form, and runs Black Widow’s XSS engine there.

### Evaluation applications and baselines

The authors initially selected **21** real-size, modern applications from Black Widow’s test set and the Bitnami, Elestio, and DockerHub catalogs. WordPress was later removed because its theme placed its entire documentation in an input field, making the LLM prompt exceed the maximum size and return HTTP 400 errors. The final evaluation therefore covered **20 applications**.

The ten-app task-execution set consisted of:

- Redacted
- GitLab 16.11.2-ce.0
- OpenCart 4.0.2-3
- Redmine 5.1.2
- Dolibarr 19.0.2
- Moodle 4.4.0
- MediaWiki 1.41.1
- OwnCloud 10.14.0
- LimeSurvey 6.5.3
- phpBB 3.3.11

The vulnerability-detection set added:

- NextCloud 29.0.1
- Joomla 5.1.1
- Leantime 3.1.4
- EspoCRM 8.2.5
- iTop 3.1.1
- MintHCM 4.0.4
- Mautic 5.0.4
- GLPI 10.0.15
- Silverpeas 6.3.5
- Monica 4.1.2

Categories included version control, e-commerce, bug tracking, CRM, learning management, wikis, media sharing, polling, forums, content management, project management, IT, human-capital management, marketing, asset management, and web portals.

Coverage was compared against:

- Black Widow
- Vanilla BFS
- Randomized BFS

Vulnerability detection was compared only against Black Widow. Earlier work had found Black Widow stronger than scanners including Arachni, Enemy of the State, jÄk, Skipfish, w3af, and ZAP.

All applications and scanners ran in Docker containers on the same virtual network. Application state was reset after every tool run. Each scanner received a maximum of **four hours**. Authentication was handled separately and fairly: all tools received credentials or valid session cookies, and authentication steps were manually scripted.

### Manual review and reproducibility

Two authors manually reviewed every generated task using augmented screenshots. Each initially covered five applications, then cross-validated a random sample of the other reviewer’s work. Unclear cases were resolved by discussion, and final sampled cross-validation produced no disagreements.

Reviewers labeled each task as:

- Invalid for the application
- Successful
- Partial: every step except the final one was correct
- Failed

Failures were classified as:

- **Missing state:** a prerequisite state or object was absent.
- **Deviated:** actions went toward the wrong functionality.
- **No action:** the scanner immediately issued `STOP`.

Each review involved between one and fifteen screenshots.

The artifact was tested on Ubuntu 22.04.4 with four CPU cores, 16 GB RAM, 60 GB disk, Docker 24.0.7, docker-compose 1.29.2, and Python 3.10.12. The full experiments required approximately **80–320 compute hours**: 10–20 applications, two to four scanners, and four hours per run. Organization-wide OpenAI rate limits restricted YURASCANNER to one experiment at a time.

## 4. Results and Findings

### RQ2: Task generation and execution

YURASCANNER generated **2,361 tasks** across ten applications.

- **1,818 tasks (77.0%)** described valid application functionality.
- **543 tasks (23.0%)** were invalid.
- Invalid tasks mainly came from ambiguous or context-poor pages. A page containing only a Login button, for example, could lead the model to invent unrelated tasks. A MediaWiki privacy-policy link produced the invalid task “Get detailed information about membership or subscription plans.”

Among the 1,818 valid tasks:

- **667** were completed fully.
- **448** were completed through the penultimate step.
- Thus, **1,115 tasks, or 61.3%,** reached the intended functionality fully or partially.
- **703** failed.

The failure counts in Table II were:

- **287 missing-state failures**
- **172 deviations**
- **244 no-action failures**

Missing-state and no-action failures together accounted for approximately **75%** of failures; deviations accounted for approximately **25%**.

Per-application results were:

| Application | Successful | Partial | Missing state | Deviated | No action | Valid total |
|---|---:|---:|---:|---:|---:|---:|
| Redacted | 76 | 51 | 8 | 27 | 58 | 220 |
| OpenCart | 50 | 45 | 15 | 4 | 2 | 116 |
| GitLab | 73 | 31 | 77 | 0 | 2 | 183 |
| Moodle | 54 | 42 | 38 | 6 | 3 | 143 |
| MediaWiki | 63 | 26 | 18 | 30 | 59 | 196 |
| OwnCloud | 30 | 18 | 31 | 25 | 22 | 126 |
| phpBB | 99 | 79 | 20 | 28 | 20 | 246 |
| LimeSurvey | 30 | 38 | 4 | 9 | 35 | 116 |
| Dolibarr | 75 | 78 | 24 | 21 | 11 | 209 |
| Redmine | 117 | 40 | 52 | 22 | 32 | 263 |
| **Total** | **667** | **448** | **287** | **172** | **244** | **1,818** |

### RQ3: Attack-surface coverage

Coverage was measured using unique URLs and unique forms. Pseudorandom URL parameters, such as session identifiers and security tokens, were manually identified and ignored during URL comparison.

For every baseline comparison, the authors separated:

- Items unique to YURASCANNER
- Items shared by both
- Items unique to the baseline

#### YURASCANNER versus Black Widow

- Forms unique to YURASCANNER: **632 (35.8%)**
- Shared forms: **339 (19.2%)**
- Forms unique to Black Widow: **791 (44.8%)**
- URLs unique to YURASCANNER: **4,476 (31.5%)**
- Shared URLs: **2,699 (19.0%)**
- URLs unique to Black Widow: **7,026 (49.4%)**

Forms-per-URL ratios were 0.14 for YURASCANNER-only coverage, 0.13 for shared coverage, and 0.11 for Black-Widow-only coverage.

#### YURASCANNER versus BFS

- Forms unique to YURASCANNER: **635 (37.1%)**
- Shared forms: **336 (19.6%)**
- Forms unique to BFS: **739 (43.2%)**
- URLs unique to YURASCANNER: **4,301 (23.7%)**
- Shared URLs: **2,874 (15.9%)**
- URLs unique to BFS: **10,902 (60.3%)**

Forms-per-URL ratios were 0.15, 0.12, and 0.07, respectively.

#### YURASCANNER versus randomized BFS

- Forms unique to YURASCANNER: **631 (33.5%)**
- Shared forms: **340 (18.0%)**
- Forms unique to randomized BFS: **908 (48.3%)**
- URLs unique to YURASCANNER: **4,160 (22.0%)**
- Shared URLs: **3,015 (15.9%)**
- URLs unique to randomized BFS: **11,721 (62.0%)**

Forms-per-URL ratios were 0.15, 0.11, and 0.08, respectively.

Across comparisons, the attack surface uniquely added by YURASCANNER represented approximately **35.46% of combined forms** and **25.7% of combined URLs**. Relative to what the comparison tools found, this amounted to an average increase of **55.19% in forms** and **35.16% in URLs**.

Only **18.3% of forms** and **16.9% of URLs**, on average, were shared. This was less than half the size of either method’s unique surface, indicating that task-driven and conventional crawling reach substantially different parts of applications.

Although baselines usually found more total unique URLs and forms, YURASCANNER’s higher forms-to-URLs ratio indicates a denser concentration of forms in its newly reached states.

Table IV provides application-level comparisons and shows substantial variation. Examples include:

- Against Black Widow, YURASCANNER uniquely found 132 Moodle forms versus 101 unique to Black Widow, with 123 shared.
- In Redacted, it uniquely found 117 forms versus 101 unique to Black Widow, with 15 shared.
- In OpenCart, it uniquely found 82 forms versus 184 unique to Black Widow, with only one shared.
- In phpBB, it uniquely found 168 forms versus 114 unique to Black Widow, with 12 shared.
- For URLs, YURASCANNER uniquely found 1,229 in Moodle versus 2,040 unique to Black Widow, with 643 shared.
- In LimeSurvey, it uniquely found 403 URLs versus 374 unique to Black Widow, with 227 shared.
- In Redmine, it uniquely found 286 URLs versus 54 unique to Black Widow, with 189 shared.

These results reinforce that neither approach simply subsumes the other.

### RQ4: Depth and complexity of the new surface

Figure 7 is a stacked logarithmic-scale bar chart of task counts by execution length, from zero to fifteen actions. It separates successful, partial, and failed tasks. Most tasks required only a few actions.

For failures, task length means the number of actions before the error. For successful or partial tasks, it represents the workflow length.

Important observations include:

- Zero-step cases were mainly failures caused by an immediate `STOP`.
- Only **14 zero-step tasks** were partial or successful. These included tasks such as browsing a product catalog already displayed at the seed URL.
- The longest task executions reached **15 steps**.
- At 15 steps, **one task succeeded** and **two were partial**.

Figure 8 plots the cumulative proportion of forms reached as task steps increase:

- **44%** of YURASCANNER’s forms were also found by at least one of Black Widow, BFS, or randomized BFS.
- All shared forms were found within the first **three steps**, indicating that they lay in relatively shallow states.
- By depth three, YURASCANNER had found **85.7%** of all forms it would eventually collect—approximately twice the shared 44% portion.
- The remaining **14.3%** appeared beyond depth three, at depths extending as far as fifteen.
- None of those deeper forms was found by the other tools.

Thus, the distinguishing feature was not simply the number of resources: task-driven crawling exposed forms embedded in longer workflows that traditional strategies could not reach.

### RQ5: Vulnerability detection

YURASCANNER and Black Widow each ran for four hours against the administrative areas of all 20 applications. The intended target included reflected XSS that an unauthenticated attacker might trigger by sending a vulnerable link to an administrator.

Together, the tools produced **15 XSS reports** across three applications:

- **Redacted:** YURASCANNER reported 11; Black Widow reported one.
- **Moodle:** YURASCANNER reported one; Black Widow reported one.
- **Leantime:** Black Widow reported one.

All reports were manually verified and were true positives.

Four reports were duplicates referring to two vulnerabilities, leaving **13 unique zero-day vulnerabilities**:

- **12 unique vulnerabilities** were discovered by YURASCANNER.
- **3 unique vulnerabilities** were discovered by Black Widow.
- The totals overlap because some vulnerabilities were found by both tools.

Table V classifies the findings:

- **Redacted:** 12 reports corresponding to 11 unique vulnerabilities. YURASCANNER found four stored and seven reflected vulnerabilities; Black Widow found one reflected vulnerability.
- **Moodle:** two reports corresponding to one unique finding. YURASCANNER and Black Widow each reported it as a stored issue.
- **Leantime:** one unique stored vulnerability found by Black Widow.
- The other 17 applications produced no reported vulnerabilities.

The Moodle issue was specifically an **HTML meta-tag attribute injection**, not direct XSS, although the paper states that it could escalate to XSS.

For the 11 unique vulnerabilities attributed to YURASCANNER in the depth analysis:

- Three were four clicks from the start.
- Two were three clicks away.
- Six—including the vulnerability also found by Black Widow—were no more than two clicks away.

Exploitability analysis across all 13 unique findings showed:

- Seven reflected XSS vulnerabilities were exploitable by unauthenticated users.
- One stored XSS was exploitable by a low-privileged user.
- The authors could not identify a non-administrator exploit path for the other five stored XSS vulnerabilities.

No statistical hypothesis tests, confidence intervals, or p-values were reported; the evidence consists of manually validated task outcomes, resource counts, workflow depths, and confirmed vulnerabilities.

### Visual and table synthesis

- **Figure 1:** Demonstrates why workflow order matters through a six-step path to an XSS-vulnerable field in Redacted.
- **Figure 2:** Shows the full pipeline from web applications, through LLM-based task extraction and execution, to dynamic vulnerability testing and exploits.
- **Figure 3:** Shows the feedback loop among sensors, the LLM Bridge, actuators, browser state, action mapping, and six-step memory.
- **Figure 4:** Displays the three-part navigation prompt: instructions/persona, a one-shot example, and the current query with recent history.
- **Figure 5:** Shows the separate FormGPT prompt, which turns a form into a list of text-entry commands.
- **Figure 6:** Shows the task-generation prompt built from button labels and requesting simple create/edit/delete-style tasks.
- **Figure 7:** Shows that most workflows are short but some extend to fifteen actions, including successful and partial executions.
- **Figure 8:** Shows that baseline overlap stops by depth three, while YURASCANNER continues finding forms in deeper states.
- **Tables I–V:** Document the application set, task classifications, aggregate and per-application coverage, and vulnerability counts and types.

## 5. Analysis and Interpretation

### Task generation is feasible but context-sensitive

The 77% valid-task rate supports the idea that an LLM can infer application functions from shallowly collected interface text. Invalid tasks mainly arose when the page abstraction lacked sufficient context, causing incoherent or application-irrelevant generations.

The task catalog therefore depends on the quality and completeness of the labels presented to the model. A lone Login button or an ambiguous privacy-policy link provides too little information for reliable workflow inference.

### Task execution works, but dependencies propagate errors

Fully or partially reaching the target functionality in 61.3% of valid tasks demonstrates that an LLM can guide a browser through many multi-step workflows without an application-specific navigation model.

However, tasks are not independent. A direct failure can create later missing-state failures. If “Add an item” fails, subsequent “View item,” “Edit item,” or “Delete item” tasks may become impossible even if their navigation decisions would otherwise be correct.

Task generation can also create destructive dependencies. In Leantime, YURASCANNER successfully executed “Delete a user from the management section,” but that user was the system’s only account. The scanner was then locked out, causing subsequent tasks to fail. Basic CRUD sorting therefore does not fully capture safety constraints or complex dependencies.

### Task-driven and traditional crawling are complementary

Traditional crawlers found more resources overall because they explore broadly and treat clickables as roughly equivalent. That broadness increases coverage of diverse shallow areas.

YURASCANNER stays focused on a goal. This can reduce resource diversity, but it enables ordered action sequences and reaches deeper states. The low overlap—18.3% for forms and 16.9% for URLs on average—shows that the approaches expose different surfaces.

The authors therefore interpret YURASCANNER’s smaller absolute totals not as straightforward underperformance, but as a difference in coverage character:

- Traditional crawling is stronger in shallow, broad exploration.
- Task-driven crawling is stronger in narrow, workflow-dependent exploration.
- Combining them can provide more comprehensive coverage than either alone.

### Deeper access improves vulnerability discovery

The forms unique to YURASCANNER extended to depth fifteen, whereas all forms shared with other tools were within three actions of the seed. Its discovery of 12 of the 13 unique zero-days supports the central hypothesis that reaching workflow-dependent input points can reveal vulnerabilities unavailable to ordinary crawlers.

The paper also notes that the evaluated modern applications were relatively resilient to Black Widow’s payload database. Despite that, YURASCANNER found 11 vulnerabilities in Redacted alone—four stored and seven reflected—because it could reach the relevant forms.

### Relationship to prior work

Unlike learned state machines and reinforcement-learning agents, YURASCANNER does not train an application-specific navigation policy. Unlike trace-replay systems, it does not require users to demonstrate every workflow.

Unlike MindAct, Natbot, and Skyvern, its purpose is automated security coverage rather than assistance with manually supplied tasks. It also generates tasks automatically. Its form handling differs in using a separate form-filling prompt that fills an entire form at once, whereas Natbot and MindAct use the navigation prompt and fill one field per action.

Compared with protected-state scanners based on scripted logins, SSO handling, or regular-expression patterns, YURASCANNER addresses compound client-server workflows after authentication. Authentication itself was not automated in this evaluation.

## 6. Contributions and Novelty

The paper’s main contributions are:

- It introduces one of the first fully automated, LLM-driven, task-oriented web scanning techniques.
- It models web crawling as a rational, goal-based agent that reasons from an objective, the current semantic page abstraction, and recent history.
- It defines sensors and actuators that translate between real browser pages and high-level LLM decisions.
- It separates high-level navigation from whole-form completion, reducing prompt complexity and improving task completion.
- It proposes automatic task-catalog generation from a depth-one crawl and semantically orders tasks using CRUD relationships.
- It integrates task-driven navigation with Black Widow’s dynamic XSS engine by recording and replaying the action sequence needed to reach each form.
- It evaluates task generation and execution through manual review of all **2,361 generated tasks** on ten applications.
- It compares coverage against Black Widow, BFS, and randomized BFS across ten applications.
- It characterizes not just attack-surface size but also workflow depth, showing unique forms as deep as fifteen actions.
- It evaluates vulnerability detection on 20 applications and identifies **13 unique zero-day findings**, **12 of them discovered by YURASCANNER**.
- It provides evidence that goal-directed crawling complements rather than replaces traditional, broad exploration.

## 7. Limitations and Caveats

- Only **20 applications** were retained for the final evaluation; task accuracy and coverage analysis used a randomly selected subset of ten.
- WordPress could not be evaluated because a very large theme-documentation value in an input field exceeded the LLM prompt limit and caused API errors.
- GPT-4 was selected after a small comparison of 20 Redacted tasks. The paper does not provide detailed scores for GPT-4 or the three open-source models.
- LLM behavior is stochastic, so rerunning experiments may produce different results. Black Widow also uses randomized navigation.
- Task generation hallucinated nonexistent functionality when interface text was sparse or ambiguous; 543 of 2,361 tasks were invalid.
- Only 61.3% of valid tasks reached the intended functionality fully or partially.
- Missing prerequisites, premature `STOP`, and wrong action sequences remained common.
- CRUD sorting captured only basic dependencies. It did not reliably ensure prerequisite states or prevent harmful sequences such as deleting the only account.
- The six-action history was chosen empirically from a few examples rather than through a reported systematic ablation.
- The five-second post-click delay assumes relatively local or predictable loading behavior, although it is configurable.
- Checkboxes, radio buttons, and drop-downs are filled with simple rules: all unchecked boxes/radios are selected, and the second drop-down option is chosen. These choices may not reflect the intended semantics of every form.
- Authentication was manually scripted and supplied through credentials or cookies. The evaluation therefore does not show that YURASCANNER can independently register or log in.
- Coverage was measured through unique URLs and forms, not complete semantic state coverage. Pseudorandom URL parameters had to be identified manually.
- Vulnerability evaluation covered XSS using Black Widow’s payload engine; it did not test the system’s effectiveness for the broader range of vulnerability classes mentioned in the background.
- The Moodle finding was an HTML meta-tag attribute injection capable of escalation, rather than direct XSS.
- The authors could not find non-admin exploitation paths for five stored XSS findings.
- Experimental cost was substantial: approximately 80–320 compute hours for the reported scale, with OpenAI organization-wide rate limits preventing parallel YURASCANNER runs.
- All experiments ran on locally hosted containers, so performance against live remote systems and variable network conditions was not evaluated.
- Because of misuse risks—including automated fake-account creation and scraping—the source code is not publicly released without vetting. This restricts unrestricted reproducibility.
- The artifact notes that raw data and figure-generation scripts can reproduce tables and plots, but stochastic reruns may differ from the published results.

## 8. Future Work or Open Questions

The paper does not present a separate future-work section, but it identifies several unresolved directions:

- Improve task generation when a shallow page abstraction contains little or ambiguous semantic context.
- Model task prerequisites and side effects more accurately than basic CRUD ordering.
- Prevent one failed or destructive task from corrupting the state required by subsequent tasks.
- Improve decision-making to reduce premature `STOP` commands and deviations.
- Handle unusually large page or form content without exceeding LLM context limits.
- Evaluate more open-source models and report how model size and choice affect accuracy, cost, and reliability.
- Extend task-driven scanning beyond XSS to other vulnerability classes.
- Explore a combined scanner in which broad traditional crawling and deep task-driven exploration are explicitly coordinated.
- Develop safer controls for potentially destructive tasks and misuse-prone automation.
- Reduce computational and API overhead and improve parallel execution under rate limits.
- Evaluate additional applications and live deployment conditions.
- Improve source-code availability and reproducibility while maintaining the authors’ vetting safeguards.

From an ethical-deployment standpoint, vulnerability coordination remains ongoing. Leantime fixed its issue in version 3.3.0. Moodle judged its finding to have no impact under its threat model. The Redacted developers acknowledged their vulnerabilities and impact but supplied no remediation timeline, so the application remains anonymized.

## 9. High-Level Takeaway (Plain Language)

Most web security scanners wander through websites without understanding what they are trying to accomplish. YURASCANNER instead gives an LLM a concrete task—such as creating or editing an item—and lets it choose the sequence of browser actions needed to complete that task.

This approach was imperfect: about 23% of generated tasks were invalid, and only 61.3% of valid tasks were fully or nearly completed. Nevertheless, it reached forms hidden behind workflows as long as fifteen actions and found parts of applications that ordinary crawlers missed. Across 20 applications, the two tested scanners uncovered 13 unique previously unknown vulnerabilities; YURASCANNER found 12, while Black Widow found three, with some overlap. The main lesson is that goal-directed crawling can complement conventional crawling by reaching deeper, workflow-dependent areas where important security flaws may be hidden.