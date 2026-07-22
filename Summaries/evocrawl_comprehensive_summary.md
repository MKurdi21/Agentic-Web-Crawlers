# EvoCrawl: Exploring Web Application Code and State using Evolutionary Search

**Authors:** Xiangyu Guo, Akshay Kawlay, Eric Liu, and David Lie — University of Toronto  
**Venue:** Network and Distributed System Security (NDSS) Symposium 2025

## 1. Background and Context

Web vulnerabilities often appear only when two conditions coincide: vulnerable code must execute, and the application must be in the server-side state required to trigger the defect. A scanner may therefore miss a vulnerability even after reaching the relevant code if it has not first created the required objects or completed prerequisite actions. For example, GitLab’s repository-management code cannot be exercised until a repository has been created.

Dynamic scanners do not require source code and can be independent of implementation language, but they can detect only vulnerabilities reached during exploration. They are consequently paired with crawlers intended to maximize code coverage. Merely following links is insufficient: crawlers must also submit forms, trigger JavaScript events, and create different application states.

This is difficult for two reasons:

- **Ordering constraints:** Interactions must occur in the right order. A field may appear only after another control is activated, or a form may require fields to be completed before submission.
- **Formatting constraints:** Inputs such as dates, email addresses, or URLs must have acceptable formats. Optional fields may be better left blank when their constraints cannot be inferred.

Earlier systems such as BlackWidow and Enemy of the State include forms in their navigation graphs, while BlackWidow also includes JavaScript events. However, they simplify the search by filling every form field and enumerating combinations of events and forms. Filling every field can violate constraints on optional inputs, while event enumeration grows exponentially.

The paper illustrates this problem with a page containing 10 JavaScript events and one form: sequences of \(n\) interactions yield a search space expressed in the paper as \(n^{11}\). The target is not merely any sequence, but one that reveals links, exposes new elements, submits data, or reaches a new server-side state.

**Figure 1** shows a WordPress “Quick Draft” component. The title and content form fields become available only after clicking an arrow control highlighted in red. It demonstrates a concrete dependency: interacting with the arrow must precede interacting with the newly revealed form.

The security motivation is substantial. The paper reports that broken access control and XSS injection have remained among the OWASP Top 10 since 2017 and that OWASP’s 2021 report found some form of broken access control or injection vulnerability in 94% of tested applications.

## 2. Research Goal and Objectives

The paper introduces **EvoCrawl**, a black-box web crawler designed to explore more application code and server-side states by searching for effective sequences of fine-grained browser interactions.

Its principal objectives are to:

1. Find interaction sequences that satisfy ordering dependencies among web elements.
2. Submit forms despite difficult or optional fields by considering subsets of fields rather than always filling everything.
3. search the resulting large sequence space efficiently through an evolutionary algorithm and a feedback-based fitness function.
4. Increase code coverage and the number of successfully submitted forms relative to existing crawlers.
5. Integrate modular detectors for:
   - Cross-Site Scripting, or XSS;
   - Insecure Direct Object Reference, or IDOR, a broken-access-control defect where an unauthorized user can directly request another user’s or an administrator’s resource.
6. Determine whether better exploration leads to improved detection of known and previously unknown vulnerabilities.

The central premise is that evolutionary search can preserve and recombine promising interaction sequences, while dependency tracking can eliminate sequences that attempt impossible interaction orders.

## 3. Methods (Approach/Design)

### Overall architecture

EvoCrawl contains two complementary crawling modules and two vulnerability detectors.

**Figure 2** depicts this architecture:

- The **Page Collection Module (PM)** rapidly discovers pages and elements.
- The **Evolutionary Search Module (ESM)** searches interaction sequences on individual pages.
- PM and ESM exchange URLs in both directions.
- Both supply element URLs to the **IDOR Vulnerability Detector**.
- Both act as input sources for the **XSS Vulnerability Detector**, while the detector monitors execution sinks.

The division balances breadth and depth. PM visits many pages quickly, whereas ESM spends more effort discovering useful sequences and server-side states on a page.

### Page Collection Module

A DOM-changing interaction is called an **event**. A page URL and an optional associated event form a seed, represented as \(\langle URL, EVENT\rangle\). Seeds are stored in a queue.

For every seed, PM performs three stages:

1. **Link crawling**
   - Navigate to the URL.
   - Trigger the seed’s event if one is present.
   - Extract all anchor `href` values.
   - Add unvisited URLs as new seeds.

2. **Event crawling**
   - Interact once with each interactable element.
   - If the DOM changes without a refresh or navigation, record the triggering element’s CSS selector as an event.
   - PM does not combine events. Given Event 1 and Event 2, it produces separate seeds rather than a combined sequence; sequence combinations are delegated to ESM.

3. **Form crawling**
   - Locate elements with the HTML `form` tag.
   - Interact sequentially with their fields and try immediate submission.
   - Detect DOM changes during submission and interact with newly appearing controls, such as a confirmation dialog.

### Evolutionary Search Module

ESM treats an interaction as a **gene**, such as `input-click`, `input-typeText`, or `button-click`. An ordered list of genes is a sequence.

For each page, ESM evolves sequences over multiple generations. Each generation has:

1. **Sequence generation**
   - Randomly combine genes to preserve diversity.
   - Use crossover to recombine highly scored earlier sequences—for example, the first half of one sequence with the second half of another.
   - Mutate sequences to enforce newly discovered dependencies.
   - Place submit buttons at the ends of sequences to improve the chance of form submission.

2. **Sequence evaluation**
   - Reload the target URL.
   - Execute each gene through the browser interface.
   - Observe browser and database feedback.
   - Score the sequence using the fitness function.
   - Retain high-scoring sequences to produce the next generation.

Unlike a conventional genetic algorithm seeking one optimum, ESM seeks many useful solutions that either discover links or reach server-side states.

If an interaction navigates away from the page, ESM records the destination, sends it to PM, returns to the original page, and continues the sequence. This confines evolutionary search to the current page. Because navigation may reset earlier JavaScript state, a gene that causes navigation—and all sequences containing it—is subsequently removed from the search space.

### Dependency tracking and enforcement

During evaluation, if one interaction triggers JavaScript and reveals a new element, ESM infers that the element depends on the triggering gene. It records this relationship in a dynamic map.

During mutation, dependent elements are inserted after their prerequisite. If clicking `button1` reveals `a3`, then `a3-click` must follow `button1-click`.

**Figure 3** visualizes this mutation. An initial sequence containing text entry and clicks is expanded by inserting the newly available `a3-click` gene immediately after `button1-click`, its prerequisite. When several elements appear, ESM randomly selects some to insert.

This heuristic may infer false dependencies because web pages can be nondeterministic, but the authors report that false dependencies were very rare in practice.

### Generating field values

For text inputs and text areas, ESM checks:

1. The element’s `value` attribute.
2. Its `placeholder`.
3. Other attributes for keywords such as “URL” or “email.”
4. A user-configured default if no clue is found.

A URL-like field receives a value of the form `www.esm{i}.com`; otherwise, the experimental default is `esm{i}`, where \(i\) uniquely identifies the injected input. The fitness function indirectly determines whether the value satisfies the field’s constraints.

EvoCrawl can try sequences that omit some fields. This makes it possible to bypass optional inputs whose specialized formats cannot be inferred. It still cannot submit a form when an unrecognized, strictly constrained field is mandatory.

### Fitness function

Every sequence begins with a common score that changes during execution. Useful actions are rewarded; attempts to interact with invisible elements are penalized.

The function is:

\[
f=\sum o_iw_i
\]

Here, \(o_i\) is the measured count for an objective and \(w_i\) is its weight.

**Table I — Fitness objectives and weights**

| Objective | Weight |
|---|---:|
| Number of form submissions | 40 |
| Number of filled inputs | 20 |
| Number of uploaded files | 20 |
| Number of triggered JavaScript events | 15 |
| Number of invisible elements | −2 |

A successful form submission is detected by inserting uniquely identifiable text into inputs and checking the server-side database after sequence execution. Finding the tainted value in a database transaction indicates that the form was submitted.

The design strongly rewards successful submissions but also favors descendants that fill additional optional fields. Conversely, if adding a constrained field prevents submission, loss of the 40-point submission reward outweighs the 20-point input reward, steering evolution back toward sequences that omit that field.

The weights were selected empirically and used unchanged across applications. They were not fine-tuned per benchmark, although the authors state that they are tunable.

### XSS Vulnerability Detector

The XSS Vulnerability Detector, or XVD, is integrated into both PM and ESM:

- PM substitutes an XSS payload after each form submission.
- ESM replaces generated text with the payload.

Each payload contains a unique integer generated from a UNIX timestamp. If browser JavaScript executes the payload, that integer is pushed into a global list inserted into the page header. The detector then matches the executed sink to its originating input source.

The detector is designed to find injection points, not to evolve specialized payloads that bypass sanitizers.

### IDOR Vulnerability Detector

The IDOR Vulnerability Detector, or IVD, was designed for this work because the authors could not find a suitable existing detector to integrate.

It first constructs a sitemap from all browser requests observed during PM and ESM crawling. Nodes are URLs, and edges are the HTML elements or interactions producing transitions.

**Figure 4** shows a WordPress sitemap centered on `wp-admin/`. Blank nodes represent ordinary page URLs, the gray node a REST API URL, and the blue node an AJAX URL. Labeled edges such as `a1`, `a2`, and `a3` record which element caused each transition.

IVD classifies resources using users at different privilege levels:

1. An administrator-level crawler discovers resources.
2. A lower-privileged replay user repeats interactions in lockstep on the same application instance.
3. Resources reachable through the lower-privileged UI are public.
4. Resources found only through the administrator UI are provisionally private.
5. IVD sends forged requests for private URLs using lower-privileged credentials.

Lockstep replay is necessary because objects can be created and deleted during crawling. Replaying against a different state could incorrectly label a public resource as private.

If any route to a destination is accessible to the replay user, that destination is considered public. Correctly replaying interactions and mapping the proper edge is important because an error can create both false positives and false negatives.

#### Triad response test

For every private resource, IVD sends requests as three users:

- **userA:** the crawler, with the higher privilege;
- **userB:** the lower-privileged replay user;
- **userC:** another user at the same privilege level as userB.

Responses are analyzed in two stages:

1. Search for manually collected phrases commonly found in access-denied responses. The authors found five phrases sufficient for each tested application, although some applications’ final lists contained fewer.
2. If no denial phrase appears, compare responses. Comparing A and B alone would confuse protected content with ordinary user-specific differences such as names or email addresses. Comparing B and C identifies those user-specific differences, allowing them to be ignored when A and B are compared.

The appendix supplies the application-specific denial phrases used by the detector.

### Implementation

EvoCrawl uses a customized version of TestCafe for browser automation, visibility checks, element interaction, JavaScript execution, and request/response capture.

It injects rrweb’s recording script into page headers. rrweb uses `MutationObserver` to capture DOM changes with low overhead. Because rrweb’s timestamped element IDs can point to the wrong element after dynamic DOM changes, the authors use only its recording component and implement replay themselves.

Kafka provides durable seed storage. PM and ESM run as separate processes with distinct cookie sessions and separate consumer groups.

For applications whose page URLs contain tokens tied to cookies, EvoCrawl compares post-login redirect query strings from PM and ESM to infer token parameter names, then replaces token values when sharing seeds. This works only for persistent tokens appearing in every URL. Intermittent tokens can produce invalid shared seeds, slowing the system without stopping it.

Initial deployment requires a one-time manual setup: enabling automatic login and registering three users.

### Experimental design

The authors evaluated four crawlers:

- EvoCrawl;
- BlackWidow;
- JAK;
- CrawlJAX.

Each ran on a four-CPU virtual machine with 6 GB of memory and an Intel Xeon Gold 6336Y processor. Applications were reset before every run. Because EvoCrawl uses two processes, competing crawlers were also run with two parallel processes for equal CPU allocation.

Every experiment lasted 24 hours. EvoCrawl was run five times because its evolutionary process is randomized. ESM parameters, including sequence length and generation count, were fixed across benchmarks.

Coverage was measured as executed source-code lines:

- Xdebug and php-code-coverage were used for PHP applications.
- Coverband was used for the Rails application.

Vulnerability detectors were disabled during coverage tests. Successful forms were identified by logging database-modifying transactions and checking whether crawler-generated unique text appeared in them.

All crawlers received manually configured login credentials. They were prevented from visiting user-account, core-configuration, extension/plugin-installation, and similar pages that could alter credentials or crash the application. They were also prevented from clicking logout controls.

CrawlJAX used its defaults with unlimited depth and states and was allowed to click event handlers. JAK used the developers’ example configuration. BlackWidow was modified to generate unique values per field only for the form-submission experiment; its unmodified implementation was used for coverage.

### Applications

**Table II** lists the 10 benchmark applications:

| Application | Functionality | Version | GitHub stars reported |
|---|---|---:|---:|
| WordPress | Blog | 6.4.3 | 2.3k |
| HotCRP | Content management system | v3.0b3 | 319 |
| Dokuwiki | Content management system | 2022-07-31 “Igor” | 4k |
| Drupal | Content management system | 9.3.15 | 4k |
| Humhub | Social software platform | 1.12.1 | 6.2k |
| Opencart | eCommerce | 4.0.0 | 7.3k |
| phpBB | Forum | 3.8.8 | 1.8k |
| ImpressCMS | Content management system | 1.4.4 | 27 |
| Kanboard | Project management system | 1.2.22 | 8.2k |
| GitLab | DevSecOps platform | 11.5.1 | 23.6k |

WordPress, HotCRP, Drupal, and phpBB had also been used in cited prior studies. The targets were chosen to cover varied functions, active users, and actively maintained software.

The artifact appendix instead lists WordPress 6.1.1 and phpBB 3.3.8 among its packaged benchmarks, differing from the main evaluation table’s WordPress 6.4.3 and phpBB 3.8.8.

## 4. Results and Findings

### Overall outcomes

The paper’s headline results are:

- An average **59% increase in code coverage**.
- Between **6% and 192% greater coverage** than BlackWidow, depending on the application.
- HTML forms submitted with POST **five times more frequently** than the next-best tool, as reported by the authors.
- Eight zero-day XSS and IDOR vulnerabilities found across WordPress, HotCRP, Kanboard, ImpressCMS, and GitLab.

### Code coverage

**Figure 5** is a set of normalized stacked bars comparing EvoCrawl separately with BlackWidow, JAK, and CrawlJAX. Blue denotes lines unique to EvoCrawl, orange denotes lines common to both tools, and red denotes lines unique to the comparator. Every comparison favors EvoCrawl: blue is consistently larger than red, often by a wide margin. Exact counts are given in Appendix Table VII.

**Table VII — Exact coverage comparisons**

Each cell is shown as: **EvoCrawl-only / common / comparator-only lines**.

| Application | vs. BlackWidow | vs. JAK | vs. CrawlJAX |
|---|---:|---:|---:|
| WordPress | 57,398 / 45,868 / 3,368 | 58,721 / 44,545 / 1,063 | 67,905 / 35,361 / 673 |
| HotCRP | 10,706 / 17,679 / 331 | 14,447 / 13,938 / 131 | 11,412 / 16,973 / 250 |
| Dokuwiki | 4,191 / 12,531 / 284 | 3,099 / 13,623 / 44 | 8,885 / 7,837 / 22 |
| Drupal | 42,460 / 54,691 / 21,437 | 15,843 / 45,460 / 1,195 | 46,545 / 14,758 / 767 |
| Humhub | 10,064 / 21,606 / 1,741 | 16,392 / 15,279 / 398 | 22,463 / 9,207 / 290 |
| ImpressCMS | 6,157 / 16,485 / 622 | 8,418 / 14,224 / 624 | 11,638 / 11,004 / 390 |
| Kanboard | 10,130 / 5,246 / 4 | 9,626 / 5,750 / 1,193 | 10,681 / 4,695 / 488 |
| Opencart | 8,353 / 14,500 / 672 | Not reported | Not reported |
| phpBB | 21,781 / 14,142 / 11,616 | Not reported | Not reported |
| GitLab | 10,775 / 172,367 / 617 | 19,398 / 163,744 / 419 | 14,323 / 168,819 / 2,652 |

JAK and CrawlJAX results are absent for Opencart and phpBB because they could not handle those applications’ token implementations.

Across all 10 applications, the statistical comparisons between EvoCrawl and BlackWidow were significant. **Table III** reports:

| Application | p-value |
|---|---:|
| WordPress | 0.00096 |
| HotCRP | 0.000007 |
| Dokuwiki | 0.00082 |
| Drupal | 0.004448 |
| Humhub | 0.000031 |
| ImpressCMS | 0.000502 |
| Kanboard | 0.000719 |
| Opencart | 0.000009 |
| phpBB | 0.000159 |
| GitLab | 0.000120 |

The paper does not identify the exact statistical test used.

#### Coverage case studies

- **HotCRP:** BlackWidow sometimes clicked “cancel” before “save.” EvoCrawl evolved sequences that omitted cancel and selected save. This mattered because later functionality, such as paper reviews, was available only after submitting a paper. EvoCrawl could also leave difficult optional fields blank.
- **Kanboard:** EvoCrawl was the only scanner to create tasks inside projects. Other scanners entered invalid values into difficult fields; EvoCrawl omitted them, enabling access to task modification and management code.
- **WordPress:** EvoCrawl installed themes and explored their code. It also published posts by finding the required sequence of filling the form and then triggering a JavaScript event. BlackWidow could create drafts but not publish them.
- **Opencart:** Correct submission required a JavaScript event after filling inputs. BlackWidow’s exhaustive event/form enumeration produced too large a search space to find the sequence. It also failed to reveal links hidden behind combinations of JavaScript events.
- **Other applications:** EvoCrawl avoided unrelated event combinations and therefore spent more time visiting pages and forms. It also found submission sequences that competing tools missed.

### Successful form submissions

**Table IV** separates forms into those unique to EvoCrawl, common to both crawlers, and unique to BlackWidow:

| Application | EvoCrawl-only | Common | BlackWidow-only |
|---|---:|---:|---:|
| WordPress | 8 | 7 | 2 |
| HotCRP | 17 | 6 | 3 |
| Humhub | 25 | 3 | 2 |
| Drupal | 70 | 11 | 33 |
| Kanboard | 17 | 5 | 0 |
| phpBB | 15 | 12 | 10 |
| ImpressCMS | 7 | 2 | 3 |
| Opencart | 15 | 0 | 1 |
| Dokuwiki | 6 | 8 | 2 |
| GitLab | 30 | 1 | 1 |

Thus, EvoCrawl submitted more forms on every application. It had 210 unique submissions plus 55 shared forms; BlackWidow had 57 unique plus those 55 shared forms. The paper separately reports the headline result that EvoCrawl submitted POST forms five times more frequently.

The largest EvoCrawl-only counts were Drupal with 70, GitLab with 30, and Humhub with 25. BlackWidow did submit some forms EvoCrawl never analyzed, especially in Drupal and phpBB, because different seed schedules led the crawlers to different parts of those applications.

EvoCrawl’s advantages on HotCRP, Humhub, and Kanboard were specifically tied to bypassing constrained optional fields and respecting interaction order. BlackWidow’s failures also prevented access to downstream forms: paper assignment and review forms in HotCRP, task-related forms in Kanboard, and space-creation-dependent forms in Humhub.

### Dependency-tracking ablation

The authors created **EvoCrawl-nodt**, which disables dependency tracking during sequence generation.

**Figure 6** uses blue for lines unique to full EvoCrawl, orange for common lines, and red for lines unique to EvoCrawl-nodt. Full EvoCrawl generally has substantially more unique coverage, although differences are small in applications that do not rely heavily on JavaScript to expose links or forms.

**Table VIII — Exact ablation results**

| Application | EvoCrawl-only | Common | No-dependency-tracking-only |
|---|---:|---:|---:|
| WordPress | 29,676 | 73,590 | 21,738 |
| HotCRP | 8,578 | 19,807 | 627 |
| Dokuwiki | 91 | 16,631 | 112 |
| Drupal | 2,321 | 58,982 | 1,318 |
| Humhub | 576 | 31,094 | 34 |
| ImpressCMS | 1,039 | 21,603 | 604 |
| Kanboard | 4,484 | 10,892 | 246 |
| Opencart | 1,151 | 21,675 | 59 |
| phpBB | 8,926 | 17,340 | 3,113 |
| GitLab | 3,034 | 180,108 | 2,131 |

Dokuwiki is the only row where the no-dependency version has slightly more unique lines than full EvoCrawl, although total full-EvoCrawl coverage remains larger because of the shared and EvoCrawl-only lines.

WordPress and phpBB show notable unique coverage for both configurations. Dependency tracking reveals additional elements and pages, lengthening EvoCrawl’s queue. Because neither crawl finishes all pages within 24 hours, the two versions reach different page subsets. Nevertheless, total full-EvoCrawl coverage is always higher.

### Known XSS vulnerabilities

The authors ran 24-hour tests using vulnerable versions selected under three conditions:

1. The vulnerable environment and trigger were reproducible.
2. Detection did not require a specialized payload to bypass sanitization.
3. The vulnerability had not previously been found by EvoCrawl or BlackWidow.

The tested versions were WordPress 4.7.2, Kanboard 1.2.8, ImpressCMS 1.4.4, and Humhub 1.11.0.

**Table V** reports detected/known vulnerabilities:

| Application | EvoCrawl | BlackWidow |
|---|---:|---:|
| WordPress | 2/2 | 1/2 |
| Humhub | 0/1 | 0/1 |
| ImpressCMS | 2/2 | 0/2 |
| Kanboard | 2/3 | 1/3 |

Application-specific findings were:

- **Humhub:** Both injected the payload into the Space “name” field but failed because manifestation required logging in again as another user.
- **Kanboard:** Both missed a vulnerability requiring another-user re-login. EvoCrawl alone found a vulnerability requiring creation of a task under a project followed by injection into its “external link” field. BlackWidow could not create the task because it failed to omit constrained fields.
- **ImpressCMS:** EvoCrawl found vulnerabilities on “edit user” and “blocks admin.” BlackWidow failed on one because it could not bypass a field constraint and on the other because the form was hidden behind an interaction sequence.
- **WordPress:** Both found the “taxonomy name” vulnerability. Only EvoCrawl found the “upload filename” vulnerability; BlackWidow was slowed by enumerating JavaScript-event combinations.

### Zero-day XSS findings

Across the latest benchmark versions, EvoCrawl reported five zero-day XSS vulnerabilities:

- **WordPress:** Two stored XSS injection points in the comment field and post-title field. Admin or editor users could inject scripts. WordPress acknowledged them but did not plan fixes because those roles are trusted under its security policy.
- **HotCRP:** One stored XSS on `settings/decisions`, where chair or admin users could inject scripts into the decision-name field. It was acknowledged and fixed.
- **HotCRP:** One reflected XSS on `settings/reviews` in the round-name field. It was reported but not acknowledged as a vulnerability because it was visible only to administrators and protected by a CSRF token.
- **Kanboard:** One stored XSS on `settings/api`, where administrators could inject scripts into the application-URL field. It was acknowledged and fixed.

EvoCrawl also generated one conservatively counted false positive in Humhub: a field intentionally allowed the site owner to enter custom page-statistics scripts.

### IDOR detector results

**Table VI** reports the numbers of discovered, private, and public URLs; false positives; site-configuration exposures (**Type 1**); and implementation flaws (**Type 2**):

| Application | URLs | Private | Public | False positives | Type 1 | Type 2 |
|---|---:|---:|---:|---:|---:|---:|
| WordPress | 1,025 | 379 | 646 | 9 | 106 | 0 |
| HotCRP | 526 | 415 | 111 | 39 | 3 | 0 |
| Humhub | 10,729 | 9,451 | 1,278 | 0 | 5 | 0 |
| Drupal | 1,908 | 1,242 | 666 | 4 | 55 | 0 |
| Kanboard | 7,973 | 4,511 | 3,462 | 17 | 0 | 0 |
| phpBB | 1,684 | 1,527 | 158 | 385 | 0 | 0 |
| Opencart | 1,202 | 870 | 332 | 4 | 60 | 0 |
| Dokuwiki | 3,121 | 864 | 2,257 | 8 | 13 | 0 |
| ImpressCMS | 615 | 593 | 22 | 0 | 111 | 2 |
| GitLab | 1,382 | 640 | 742 | 27 | 63 | 1 |

A numerical inconsistency is visible in the source table for phpBB: 1,527 private plus 158 public URLs equals 1,685, while the listed total is 1,684.

Type 1 findings were endpoints exposing resources such as images or JavaScript files because of site-builder configuration or folder permissions rather than defective application code. The authors still considered these reports useful for checking deployment privileges.

The IVD found three Type 2 implementation vulnerabilities:

- **ImpressCMS:** `userinfo.php?id=1` exposed other users’ information when the `id` parameter was changed. It was acknowledged and a patch was under development.
- **ImpressCMS:** `/libraries/image-editor/image-edit.php?image_id=1&uniq=` allowed forced browsing to private images by changing `image_id`. It remained under inspection.
- **GitLab:** `autocomplete/users.json?search=&active=true&current_user=true` exposed information about all users, including avatar URL, username, and status. The paper’s detailed list calls it acknowledged and fixed, while the preceding IDOR subsection says it would be addressed in a future version.

False positives largely occurred when a genuinely public resource lacked a visible route in the unprivileged UI. phpBB accounted for 374 of 385 false positives according to the text, and HotCRP for 35 of 39. Remaining errors occurred when crawling did not discover every public navigation path within the time limit.

### Total new vulnerabilities

EvoCrawl found eight zero-day vulnerabilities:

- Five XSS vulnerabilities:
  - WordPress: 2;
  - HotCRP: 2;
  - Kanboard: 1.
- Three Type 2 IDOR vulnerabilities:
  - ImpressCMS: 2;
  - GitLab: 1.

Six were acknowledged and confirmed by developers. All were responsibly disclosed. The introduction says all were fixed or acknowledged except two; the detailed results identify the unacknowledged HotCRP reflected XSS and the still-inspected ImpressCMS IDOR as unresolved cases.

## 5. Analysis and Interpretation

The results support the paper’s central argument that exploring web applications requires searching both pages and server-side states.

EvoCrawl improves exploration through two interacting mechanisms:

- **Evolutionary selection** keeps sequences that submit forms, reveal elements, upload files, or trigger useful JavaScript events. Crossover and mutation then build variations from these promising sequences.
- **Dependency tracking** prevents interactions with elements before their prerequisites have made them visible. This reduces wasted trials and helps expose links and forms hidden behind multi-step interactions.

Fine-grained treatment of individual fields is also important. Instead of treating an entire form as an indivisible operation, EvoCrawl can discover that a constrained field should be omitted while required fields are filled. The HotCRP, Kanboard, Humhub, and ImpressCMS results show that this capability creates states and reaches vulnerabilities missed by BlackWidow.

The form-submission results explain much of the coverage improvement. Successfully creating a paper, task, post, space, or similar object exposes downstream functionality. Consequently, a single successful state-changing sequence can unlock multiple additional pages, forms, and code regions.

The ablation confirms that dependency tracking is most useful when JavaScript dynamically exposes links or forms. It has less effect on applications that do not rely heavily on these patterns. Different exploration queues also explain why the ablated system occasionally covers lines absent from the full system under a fixed 24-hour budget.

The vulnerability experiments connect exploration quality to security outcomes. EvoCrawl and BlackWidow use comparable XSS payload concepts, but EvoCrawl finds more known injection points because it reaches the relevant fields and application states. The principal improvement is therefore navigation and state exploration rather than payload sophistication.

Relative to earlier work:

- BlackWidow and JAK enumerate navigation-graph elements, spending time on unrelated events and using event-capture mechanisms the authors consider less robust.
- Enemy of the State omits client-side JavaScript events.
- CrawlJAX represents unique DOM states but does not track dependencies between them.
- Existing evolutionary XSS systems evolve payloads, whereas EvoCrawl evolves interaction sequences.
- Existing machine-learning scanners such as Link adapt XSS payloads rather than maximize application coverage.
- General LLM web agents require task-specific natural-language instructions and are therefore described as unsuitable for fully automatic vulnerability scanning.
- White-box access-control systems depend on source code and language and may miss runtime-generated links.
- REST/API fuzzers require specifications or focus on server errors rather than whether a malicious request improperly succeeds.

## 6. Contributions and Novelty

The paper’s main contributions are:

- It identifies efficient execution of client-side events and satisfaction of element dependencies as major barriers to web-application exploration.
- It introduces EvoCrawl, which combines ordinary crawling with evolutionary search over fine-grained interaction sequences.
- It uses browser and database feedback to reward sequences likely to reveal links or produce new server-side states.
- It dynamically infers dependencies among web elements and enforces them during mutation to reduce the sequence space.
- It searches subsets of form fields, permitting difficult optional inputs to be omitted.
- It separates fast page discovery from deeper page-specific sequence exploration through PM and ESM.
- It provides modular XSS and IDOR detectors.
- It introduces an IDOR detector that constructs and replays a navigation sitemap and uses a three-user response comparison to reduce confusion from user-specific content.
- It evaluates four crawlers over 10 applications, reporting a 59% average coverage increase and substantially more successful form submissions.
- It finds eight previously unknown vulnerabilities across five prominent applications.
- It releases EvoCrawl and an artifact with setup and evaluation instructions.

## 7. Limitations and Caveats

### Explicitly stated limitations

- **Fitness-parameter tuning:** The fixed weights worked empirically, but optimal results may require manual adjustment for particular applications.
- **Redundant seeds:** Different URLs may represent identical or nearly identical pages, such as differently sorted views. Since EvoCrawl identifies seeds by URL, it may repeatedly crawl equivalent content.
- **Mandatory constrained fields:** EvoCrawl can bypass difficult optional inputs, but it still fails when a mandatory field requires a format its heuristics cannot generate.
- **Intermittent URL tokens:** Token discovery works only when token parameters persist across page URLs. Intermittent tokens can produce invalid exchanged seeds and reduce speed.
- **Manual initialization:** Automatic login must be configured, and three users must be registered.
- **Linux-only artifact:** The released implementation supports Linux, preferably Ubuntu, and depends on Node 12.22.12, npm 6.14.16, and additional Node modules.

### Detector limitations

- XVD finds injection points but does not construct specialized payloads to bypass sanitizers.
- Both tested crawlers missed vulnerabilities requiring logout or re-login as another user.
- IVD’s access-denied phrases are manually collected and may be incomplete.
- IVD can misclassify public resources when they have no visible path in the lower-privileged UI.
- Incomplete crawling can prevent IVD from finding a legitimate public route and create false positives.
- Correct IVD classification depends on reliable interaction replay and synchronized application state.
- Some configuration-level exposed resources are reported even though they are not implementation bugs.
- The Humhub intentionally script-enabled field produced an XSS false positive.

### Experimental caveats

- Experiments used 10 applications and a 24-hour limit; WordPress and phpBB were not fully crawled.
- Randomized EvoCrawl runs were repeated five times, but the paper does not specify the statistical test behind the reported p-values.
- JAK and CrawlJAX could not be evaluated on Opencart and phpBB because of token incompatibility.
- Form tracking covered HTML forms identified by their action attributes; non-form state changes were excluded because they were difficult to track.
- BlackWidow and EvoCrawl sometimes explored different forms because of seed scheduling, complicating direct per-form attribution.
- Certain sensitive pages and logout controls were deliberately excluded to preserve application stability and login state.
- The detailed form counts and the separate “five times” POST-submission claim use differently described measures; the source does not fully reconcile them.
- The artifact’s shortened eight-hour reproduction workflow may not reproduce all findings from the original 24-hour experiments.

## 8. Future Work or Open Questions

The authors identify two principal future directions:

1. **Automatic parameter tuning:** Analyze the effect of each fitness weight and build a system that adjusts weights automatically for each application.
2. **Better page equivalence detection:** Compare DOMs or use related techniques instead of relying only on URLs, reducing redundant crawling of similar pages.

Other open issues arising directly from the paper include:

- Supporting mandatory inputs whose formatting constraints cannot be inferred.
- Handling tokens that appear in only some URLs.
- Improving automatic collection of access-denied responses.
- Reducing IDOR false positives when public resources lack visible unprivileged navigation paths.
- Supporting vulnerability workflows requiring account switching or re-login.
- Improving exploration scheduling so long queues can be covered more completely within a fixed time.
- Further studying the currently fixed ESM parameters and fitness weights.
- Extending artifact experiments beyond eight hours when full reproduction of the 24-hour findings is required.

## 9. High-Level Takeaway (Plain Language)

EvoCrawl treats web scanning as a search for the right sequence of actions, not merely a hunt for links. It learns that one button may need to be clicked before another field appears, that some optional fields should be left blank, and that successful actions can unlock entirely new parts of an application. On 10 web applications, this approach covered substantially more code, submitted more forms, and uncovered eight previously unknown XSS and broken-access-control vulnerabilities. The main lesson is that a security scanner must understand and explore changing application states if it is to reach the code where vulnerabilities actually hide.