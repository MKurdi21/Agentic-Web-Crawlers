# *GPT-4V(ision) is a Generalist Web Agent, if Grounded*

**Authors:** Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, and Yu Su — The Ohio State University

## 1. Background and Context

Large multimodal models (LMMs), including GPT-4V and Gemini, combine language and visual understanding. They have performed well on image captioning, visual question answering, and multimodal reasoning, but websites present a harder setting: a rendered page may contain hundreds or thousands of related elements, controls, images, and pieces of text.

A generalist web agent is expected to follow a natural-language instruction and complete it on an arbitrary real-world website. Such tasks can be diverse, span dynamically rendered pages, and require more than ten actions.

Earlier agents generally reason over raw HTML using language models. The authors identify several problems with that approach:

- Raw HTML is noisy and often too large to send directly to a language model.
- HTML has lower information density than a rendered screenshot.
- HTML alone can omit visual meaning, especially meaning conveyed through images or layout.
- In the paper’s truck-rental example, one screenshot corresponds to **423 HTML elements** requiring **186,490 GPT-2 text tokens**, versus only **1,445 GPT-4V visual tokens**.

Rendered pages are therefore both an opportunity and a challenge. Their visual form is compact and meaningful to humans, but much denser and more spatially complicated than ordinary object- or scene-centered benchmark images.

The central distinction in the paper is between:

1. **Action generation:** deciding, in natural language, what should be done next.
2. **Action grounding:** converting that plan into an exact executable browser action—identifying the correct page element, operation, and any input value.

The paper argues that GPT-4V is already strong at the first problem but that fine-grained grounding remains the main obstacle.

---

## 2. Research Goal and Objectives

The paper introduces **SEEACT**, a generalist web agent that uses an LMM—primarily GPT-4V—to visually inspect websites, reason about instructions and action history, and generate browser actions.

Its objectives are to:

- Determine whether GPT-4V can act as a generalist agent across unfamiliar websites and tasks.
- Separate and evaluate action planning from element grounding.
- Compare three practical grounding strategies:
  - element attributes,
  - textual element choices,
  - image annotations.
- Estimate GPT-4V’s upper-bound potential using human-provided oracle grounding.
- Compare GPT-4V with text-only LLMs, smaller multimodal models, supervised models, and coordinate-generating GUI models.
- Compare cached-page offline evaluation with live-website online evaluation.
- Analyze failures, especially hallucinations and spatial errors in image-based grounding.
- Examine broader capabilities such as long-range planning, visual state understanding, world knowledge, path variation, and error correction.

The main research claim is that GPT-4V can be a strong generalist web agent **if its textual plans are grounded correctly**, but currently available automatic grounding methods leave a large performance gap.

---

## 3. Methods (Approach/Design)

### 3.1 Web-agent formulation

For a website \(S\) and task \(T\), the agent generates a sequence of actions:

\[
A=[a_1,a_2,\ldots,a_n].
\]

At step \(t\), the next action depends on the current website observation, the task, and prior actions:

\[
a_t=\pi(s_t,T,\{a_1,\ldots,a_{t-1}\}).
\]

The observation contains:

- an HTML document \(h_t\), and
- a screenshot \(i_t\).

After executing an action, the website moves to a new HTML-and-image state.

An executable action is represented by the triplet:

\[
(e,o,v),
\]

where:

- \(e\) is the target webpage element,
- \(o\) is the operation, such as **Click**, **Type**, or **Select**,
- \(v\) is any required value, such as typed text or a selected date.

Models normally produce a natural-language action description rather than this exact triplet. SEEACT therefore first generates an intended action \((\tilde e,\tilde o,\tilde v)\), then grounds it into an executable action. Parsing the operation and value is relatively manageable; identifying the exact target element is the principal difficulty.

### 3.2 Action generation

GPT-4V receives:

- the user’s task,
- the previous action history,
- the current screenshot.

It does **not** receive HTML during action generation. Its prompt asks it to:

1. Identify the current webpage.
2. interpret previous actions and their intentions;
3. examine the screenshot for the page’s actual current state;
4. choose one valid next action;
5. describe the target element, its location, and the operation.

The prompt permits one operation at a time: click, type, or select.

Figures 4, 6, and 8 show the same Thumbtack example under the three grounding pipelines. After “wedding photographer” and ZIP code “10203” have been entered, GPT-4V correctly recognizes that the next step is to click the adjacent **Search** button.

### 3.3 Grounding strategies

#### Element attributes

GPT-4V describes:

- the target element,
- its element type,
- its exact visible text,
- the operation,
- the operation value.

A heuristic searches the DOM using the predicted type and text. If exactly one match exists, it is selected; with multiple matches, the model is asked to disambiguate.

In Figures 4–5, GPT-4V produces:

- element: the Search button beside the ZIP field,
- type: BUTTON,
- text: Search,
- action: CLICK,
- value: None.

This method can fail because controls may lack text, or the relevant visible text may belong to a nearby DOM element rather than the target itself.

#### Textual choices

A DeBERTa-base cross-encoder ranks webpage elements. The top candidates are represented as HTML-text choices in a multiple-choice question, plus a “none” option. GPT-4V selects the choice matching its planned action.

Figures 6–7 show GPT-4V correctly choosing choice **H**, the `<button ...>Search</button>` element, then returning CLICK with no value.

For SEEACT, the ranker selects the top **50** elements, divided into groups of **17** options for inference.

#### Image annotation

The same ranked candidate elements are marked on the screenshot with red bounding boxes and labels. GPT-4V must return the label attached to its target, or “NA” if the target is unmarked.

Figures 8–9 show a successful case: the Search button is labeled **4**, and GPT-4V outputs element 4 and CLICK.

This resembles set-of-mark prompting, but webpage screenshots are especially dense. The model frequently invents nonexistent labels or confuses a box with an adjacent label.

#### Oracle grounding

Human annotators inspect GPT-4V’s action description and implement its intended action whenever the description contains enough information. This approximates ideal grounding and isolates GPT-4V’s planning ability from automatic element-localization errors.

### 3.4 Dataset

Experiments use **Mind2Web**, which contains more than **2,000** complex tasks with annotated action traces across:

- **137 websites**,
- **31 low-level domains**,
- **12 high-level domains**.

The supported operations are Click, Type, and Select. Hover and Press Enter are incorporated into Click in the offline dataset to avoid ambiguity.

The authors align cached HTML documents with corresponding screenshots and manually verify that elements are visible and correctly rendered. The resulting cleaned resource is called **Multimodal Mind2Web**.

#### Table 1: Dataset statistics

| Split | Tasks | Domains | Websites | Avg. actions | Avg. visual tokens | Avg. elements | Avg. HTML tokens |
|---|---:|---:|---:|---:|---:|---:|---:|
| Train | 1,009 | 17 | 73 | 7.7 | 4,240 | 602 | 128,827 |
| Cross-Domain | 694 | 13 | 53 | 5.9 | 4,314 | 494 | 91,163 |
| Cross-Task | 177 | 17 | 64 | 7.6 | 4,172 | 607 | 123,274 |
| Cross-Website | 142 | 9 | 10 | 7.2 | 4,653 | 612 | 114,358 |

The test settings measure different kinds of generalization:

- **Cross-Task:** new tasks on websites and domains represented in training.
- **Cross-Website:** tasks on ten new websites for each represented top-level domain.
- **Cross-Domain:** tasks from two top-level domains withheld from training.

### 3.5 Comparison models

The study compares:

- **FLAN-T5-XL:** supervised fine-tuning on Mind2Web actions.
- **BLIP-2-T5-XL:** FLAN-T5 plus a frozen CLIP ViT-L/14 image encoder at resolution 2,048; the language model and modality bridge are jointly fine-tuned.
- **GPT-3.5-turbo-0613** and **GPT-4-turbo-1106-preview:** text-only, three-shot in-context learning.
- **GPT-4V:** `GPT-4-vision-preview`.
- **Gemini Pro Vision**.
- **LLaVA-1.5**.
- **CogAgent:** a coordinate-generating GUI model not fine-tuned on Mind2Web.

MindAct-style baselines rank 50 elements, organize them in groups of five, and iteratively refine choices until one is selected or all are rejected.

Gemini supports only single-turn conversations, so the two SEEACT turns are merged.

### 3.6 Evaluation measures

Offline evaluation uses:

- **Element Accuracy:** whether the selected element matches the reference.
- **Operation F1:** token-level F1 for the predicted operation and input value.
- **Step Success Rate:** the percentage of individual steps where both element and operation are correct.
- **Whole-task Success Rate:** all required steps must succeed.

Because exact trace matching gives no credit for alternative valid routes or recovery from errors, the main offline analysis emphasizes the first three measures.

### 3.7 Online evaluation

The authors built a Playwright-based tool that:

- loads live pages,
- sends screenshots and element information to agents,
- turns predicted triplets into browser events,
- executes and monitors those events.

Online testing covers the same **90 tasks**: 30 sampled from each test split. Time-sensitive tasks are updated, and tasks invalidated by website changes are resampled.

A human monitors actions, judges task completion, and blocks potentially harmful state changes. Login, final submissions, purchases, profile changes, and similar operations are prohibited. Pop-up advertisements are manually closed. SEEACT can visually suggest closing ads, whereas the MindAct baselines were not trained to manage them.

---

## 4. Results and Findings

### 4.1 Overall offline performance

#### Table 2: Model performance

All non-oracle SEEACT models use textual-choice grounding. Asterisks indicate evaluation on 30 tasks per test split.

| Model | Cross-Task Ele. Acc | Op. F1 | Step SR | Cross-Website Ele. Acc | Op. F1 | Step SR | Cross-Domain Ele. Acc | Op. F1 | Step SR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| FLAN-T5-XL | 57.1 | 75.7 | 53.5 | 43.8 | 67.7 | 41.1 | 41.4 | 65.9 | 38.9 |
| BLIP-2-T5-XL | 50.1 | 77.0 | 47.0 | 39.4 | 69.3 | 37.0 | 41.2 | 69.3 | 38.9 |
| GPT-3.5* | 19.4 | 59.2 | 16.8 | 14.9 | 56.5 | 14.1 | 25.2 | 57.9 | 24.1 |
| GPT-4* | 40.8 | 63.1 | 32.3 | 30.2 | 61.0 | 27.0 | 35.4 | 61.9 | 29.7 |
| CogAgent | 22.4 | 53.0 | 17.6 | 18.4 | 42.2 | 13.4 | 20.6 | 42.0 | 15.5 |
| SEEACT–LLaVA-1.5 | 9.7 | 65.6 | 8.1 | 9.1 | 60.8 | 7.5 | 10.9 | 63.9 | 8.5 |
| SEEACT–Gemini Pro Vision | 21.5 | 67.7 | 19.6 | 17.1 | 61.3 | 15.4 | 20.7 | 64.3 | 18.0 |
| SEEACT–GPT-4V | 46.4 | 73.4 | 40.2 | 38.0 | 67.8 | 32.4 | 42.4 | 69.3 | 36.8 |
| SEEACT–GPT-4V-Oracle* | 66.4 | 79.2 | 61.9 | 69.5 | 78.9 | 65.0 | 72.8 | 73.6 | 62.1 |

With human grounding, GPT-4V achieves step success rates of:

- **61.9% Cross-Task**,
- **65.0% Cross-Website**,
- **62.1% Cross-Domain**.

Compared with the second-best method, oracle SEEACT leads by:

- **8.4 percentage points** on Cross-Task,
- **23.9 points** on Cross-Website,
- **23.2 points** on Cross-Domain.

The much larger gains on unseen websites and domains indicate that GPT-4V’s visual planning generalizes more broadly than supervised fine-tuning, provided grounding succeeds.

### 4.2 Grounding is the bottleneck

#### Table 3: GPT-4V step success by grounding method

These results use 30 tasks per split.

| Grounding method | Cross-Task | Cross-Website | Cross-Domain |
|---|---:|---:|---:|
| Element attributes | 16.1% | 12.1% | 19.0% |
| Image annotation | 20.3% | 13.9% | 23.7% |
| Textual choices | 39.1% | 32.7% | 42.0% |
| Human/oracle | 61.9% | 65.0% | 62.1% |

Textual choices are clearly the best automatic method, but remain **22.8–32.3 percentage points** below oracle grounding across these splits. The main text characterizes the broader remaining gap as roughly **20–30%**, and the conclusion as approximately **20–25%** for the best explored strategies.

Textual-choice grounding outperforms image annotation by:

- **18.8 points** on Cross-Task,
- **18.8 points** on Cross-Website,
- **18.3 points** on Cross-Domain.

Thus, set-of-mark-style visual annotations do not transfer effectively from ordinary images to dense webpage screenshots.

### 4.3 LMMs versus text-only LLMs

SEEACT with GPT-4V outperforms text-only GPT-4 in step success by:

- **6.8 points** on Cross-Task,
- **5.7 points** on Cross-Website,
- **12.3 points** on Cross-Domain.

This supports the value of rendered visual information, particularly for generalization beyond familiar sites and domains.

However, smaller LMMs do not show the same capability. Gemini Pro Vision, LLaVA-1.5, and CogAgent perform substantially below GPT-4V.

Fine-tuned BLIP-2-T5 also provides no consistent improvement over text-only FLAN-T5. The authors suggest several reasons:

- CLIP may not capture the fine image details required for web navigation.
- Its off-the-shelf image encoder is not optimized for screenshots.
- Some training screenshots may contain rendering or capture errors, even though test screenshots were cleaned.

### 4.4 Supervised fine-tuning versus in-context learning

Supervised models perform especially well on new tasks from websites seen during training. For example, FLAN-T5 achieves **53.5% Cross-Task step success**, compared with **40.2%** for automatically grounded GPT-4V.

In-context-learning models are more consistent across tasks, sites, and domains and are better suited to environments with few annotations. GPT-4V’s oracle results show that its underlying planning ability can exceed supervised models once grounding is improved.

The paper therefore presents a context-dependent conclusion:

- For one known website with available training data, supervised fine-tuning remains competitive.
- For a generalist agent facing billions of websites and expensive annotation requirements, in-context learning is more promising.

### 4.5 Online versus offline whole-task success

#### Table 4: Whole-task success

“Offline 0” allows no wrong steps. “Offline 1” permits one erroneous step.

| Model | Offline 0 | Offline 1 | Online |
|---|---:|---:|---:|
| FLAN-T5-XL | 4.4% | 24.4% | 8.9% |
| GPT-4 | 1.1% | 12.2% | 13.3% |
| SEEACTChoice | 3.3% | 12.2% | 37.8% |
| SEEACTOracle | 13.3% | 27.8% | 51.1% |

The main finding is that strict offline trace matching substantially underestimates actual task completion:

- SEEACTChoice rises from **3.3% Offline 0** to **37.8% online**.
- SEEACTOracle rises from **13.3%** to **51.1%**.
- GPT-4 rises from **1.1%** to **13.3%**.
- FLAN-T5 rises more modestly, from **4.4%** to **8.9%**.

Online SEEACTChoice exceeds both GPT-4 and FLAN-T5 by more than **20 percentage points**. Oracle SEEACT reaches **51.1%**, versus **13.3%** for GPT-4 and **8.9%** for FLAN-T5.

Although offline step metrics make GPT-4 look much worse than FLAN-T5, GPT-4 beats FLAN-T5 online by **4.4 percentage points**. The authors interpret this as evidence that large models can take alternative routes, explore, and recover in ways that reference-trace evaluation does not recognize.

### 4.6 Task difficulty

Figure 3 groups the 90 online tasks by annotated trace length:

- **Easy:** 1–4 actions, 37 tasks.
- **Medium:** 5–9 actions, 35 tasks.
- **Hard:** 10–18 actions, 18 tasks.

All four methods decline as tasks require more actions. SEEACTOracle is best at every difficulty. From the chart, approximate success rates are:

- Easy: oracle about **65%**, choices about **54%**, GPT-4 about **24%**, and FLAN-T5 about **16%**.
- Medium: oracle about **46%**, choices about **35%**, and FLAN-T5 about **6%**; the remaining bar is very small or absent.
- Hard: oracle about **33%**, choices about **11%**, with the other methods near zero.

These values are read approximately from the plotted bars; the paper does not print exact values beside them.

The growing gap between oracle and automatic grounding on longer tasks shows that small grounding errors compound across steps.

### 4.7 Image-annotation ablation

#### Table 5: Annotation label design

| Label | Location | Element accuracy | Operation F1 | Step SR |
|---|---|---:|---:|---:|
| Number | Bottom-left | 27.0 | 73.7 | 24.3 |
| Number | Bottom-center | 23.0 | 76.4 | 21.8 |
| Single letter | Bottom-left | 19.4 | 81.0 | 17.2 |
| Single letter | Bottom-center | 19.7 | 78.8 | 19.7 |
| Double letter | Bottom-left | 19.8 | 68.3 | 18.3 |
| Double letter | Bottom-center | 22.4 | 74.6 | 22.4 |
| Number, annotated image also used in action generation | Bottom-left | 26.6 | 73.9 | 22.3 |

Bottom-left numeric labels provide the highest element accuracy and step success. Giving the annotated image during action generation does not improve the result.

### 4.8 Image-grounding error analysis

The authors sample **100** cases where GPT-4V generated the correct intended action but grounded it incorrectly.

Two error classes account for all sampled cases:

- **54%: invented bounding boxes or labels.** The correct element was absent, so the proper answer was “NA,” but GPT-4V falsely claimed to see a marked target.
- **46%: failure to associate a box with its correct label.** GPT-4V recognized the target element but chose a number attached to a nearby element.

Figures 10–11 illustrate fabrication:

- In the Verizon example, GPT-4V correctly plans to click **Continue**, but that element is not among the marked candidates. It nevertheless invents label **12**.
- In the Dodge Ram search, it correctly identifies the Distance control but chooses nearby label **5**, although the target is unmarked.

Figures 12–13 illustrate label-linking errors:

- For a travel site’s “From” field, it selects label **10** rather than the correct **11**.
- For a “Telehealth” filter, it selects label **7** rather than **6**.

These errors are attributed to visual illusion/hallucination, weak relative-position reasoning, and the dense arrangement of webpage elements.

### 4.9 Qualitative capabilities and failure cases

#### Planning and webpage-state understanding

Figure 14 shows GPT-4V planning a multi-page Best Buy task before the required controls are visible. It proposes navigating to speakers, then applying Bluetooth, wireless, sale, and under-$50 filters.

Figure 15 shows screenshot understanding correcting an incomplete textual history. In a truck-rental form, the history fails to record that:

- the drop-off date was automatically set to the pickup date;
- “No” was selected for returning the truck elsewhere.

GPT-4V reads these states visually and correctly decides to click **Find Your Truck**, anticipating later truck and furniture-pad selection.

#### Identical textual elements

Figure 16 exposes a limitation of textual choices. Three stores each have an HTML-identical **Schedule** button. GPT-4V understands that the Midtown Manhattan button is required, but the textual candidate representation cannot distinguish the buttons. The model empirically tends to choose the first apparently matching option.

#### Knowledge and reasoning

Figure 17 presents a driver-school task in Dublin, Virginia. The page lists districts but does not identify which contains Dublin, so external geographic knowledge is required; GPT-4V states that the screenshot is insufficient to resolve it.

Figure 18 shows a successful knowledge-intensive case. Given origin code **DEL**, GPT-4V correctly supplies **SJD** as the Los Cabos destination code.

#### Alternative valid paths

Figure 19 demonstrates why strict offline evaluation can be misleading. The reference route to a natural-products database is:

1. click “More Resources”;
2. click “Natural products database.”

GPT-4V instead clicks “Natural Product Information” directly from the first page and reaches the same target.

#### Error correction

Figure 20 shows a healthcare signup form where a previously entered mobile number is invalid. GPT-4V notices the highlighted field and error message, abandons the nominal next steps, and prioritizes correcting the number before completing the remaining address fields and continuing.

---

## 5. Analysis and Interpretation

The experiments separate two very different capabilities.

GPT-4V is often able to understand the page, infer the user’s goal, track state, anticipate future page transitions, and describe the correct next action. Its **51.1% live task success with human grounding** demonstrates that this planning competence is practically meaningful.

The much poorer results from automatic grounding show that the bottleneck is not simply high-level reasoning. It is the fine-grained conversion of a sound plan into the exact DOM target.

The three grounding methods fail for different reasons:

- **Element attributes** require accurate visible text and element types, but many controls lack text or separate their text from the actionable node.
- **Image annotation** preserves visual distinctions but triggers label hallucinations and spatial-association errors.
- **Textual choices** combine HTML candidate retrieval with visual reasoning and work best, but collapse distinctions when several elements have identical HTML representations.

The authors consider textual choices the most effective because they exploit a property unique to websites: HTML elements have known relationships to their rendered visual counterparts. Even so, the remaining oracle gap demonstrates that this correspondence is not yet used effectively enough.

Online evaluation produces higher whole-task success because web tasks often have:

- multiple valid action sequences,
- interchangeable action orders,
- shortcuts,
- exploratory actions,
- recoverable errors.

Offline evaluation accepts only the annotated path and usually requires every step to match. It therefore measures conformity to a reference trace more than successful real-world task completion.

The results also distinguish broad generalization from specialization. Supervised models retain an advantage on familiar websites, whereas large in-context models are stronger candidates for generalist use across unfamiliar sites and domains.

---

## 6. Contributions and Novelty

The paper’s principal contributions are:

- It introduces **SEEACT**, an LMM-based generalist web agent that separates screenshot-based action generation from executable action grounding.
- It provides evidence that GPT-4V can complete **51.1% of live tasks with oracle grounding**, substantially surpassing GPT-4 and FLAN-T5.
- It systematically compares element attributes, textual choices, and image annotations for grounding.
- It shows that set-of-mark-style annotation is unreliable on dense webpage screenshots because of hallucinated labels and spatial linking errors.
- It identifies textual-choice grounding, which combines ranked HTML candidates with visual reasoning, as the strongest tested automatic method.
- It constructs **Multimodal Mind2Web**, aligning verified screenshots with Mind2Web HTML and action traces.
- It creates a Playwright-based online evaluation framework for multimodal agents on live websites.
- It quantifies the discrepancy between offline trace matching and live task success.
- It documents higher-level capabilities including speculative planning, state-transition reasoning, world knowledge, alternative-path discovery, and error correction.
- It releases code, data, and evaluation tools for research use under an OPEN-RAIL license.

---

## 7. Limitations and Caveats

- **Grounding remains substantially below oracle performance.** The best automatic method leaves roughly a 20–30-point step-success gap, depending on the split and comparison.
- **Long tasks amplify errors.** A grounding error can corrupt the state and cascade into later steps.
- **Image annotation produces hallucinations.** In the sampled failures, 54% involved invented boxes or labels and 46% involved incorrect box-label associations.
- **Textual choices cannot reliably distinguish identical elements.** Exact or near-identical HTML representations are common.
- **Element-attribute matching is heuristic.** It is unreliable for controls without text or when text belongs to an adjacent node.
- **Smaller visual encoders may miss webpage details.** BLIP-2’s frozen CLIP encoder did not yield a clear advantage over FLAN-T5.
- **Training screenshot quality may be imperfect.** Some training examples could include rendering or capture problems, although test screenshots were verified.
- **Oracle grounding requires humans** and is therefore an upper-bound diagnostic rather than an autonomous solution.
- **Some reported large-model results use subsets.** GPT-3.5, GPT-4, oracle GPT-4V, and Table 3 results are based on 30 tasks per split.
- **Online evaluation covers 90 tasks**, not the entire dataset, and website changes require task resampling.
- **The online experiments exclude login and consequential actions.** Success rates therefore do not establish safe autonomous performance for purchasing, financial operations, form submission, or account changes.
- **Human monitoring is required for safety.** The authors observed that agents could propose potentially harmful actions.
- **World knowledge is uneven.** GPT-4V solves some knowledge-dependent cases, such as the SJD airport code, but cannot resolve others from the screenshot alone, such as locating Dublin within an unspecified district list.
- **Offline metrics are overly strict**, but online metrics also depend on live-site availability and human completion judgments.

The safety caveat is central. Generalist agents may improve accessibility and automate routine tasks, but they may also access personal information or attempt sensitive operations. The authors manually approve every consequential action and oppose harmful use of the technology.

---

## 8. Future Work or Open Questions

The paper identifies several priorities:

- Improve fine-grained grounding by exploiting the known mapping between DOM/HTML elements and their visual renderings.
- Reduce LMM hallucination when visual marks or candidate labels are absent.
- Improve spatial reasoning so models can reliably connect labels to densely packed controls.
- Develop methods that preserve visual distinctions when HTML choices are identical.
- Narrow the large gap between automatic and human grounding, especially on unfamiliar sites and long-horizon tasks.
- Build evaluation methods that recognize alternative valid paths, exploration, and error correction rather than enforcing one reference trace.
- Expand realistic online evaluation while carefully mitigating privacy, financial, submission, and other safety risks.
- Thoroughly assess harmful-action generation before real-world deployment.
- Use GPT-4V’s demonstrated error awareness and website “world model” to support more robust dynamic planning.

---

## 9. High-Level Takeaway (Plain Language)

SEEACT shows that GPT-4V can often look at a webpage, understand what the user wants, and plan the right next step. When humans translate its plans into exact clicks and inputs, it completes **51.1% of live tasks**, far more than the compared text-only and smaller fine-tuned agents. The main unsolved problem is precise grounding: reliably connecting a correct verbal plan to the exact button, field, or menu on a crowded webpage. Solving that problem—and ensuring that live agents cannot perform unsafe actions—is the key step toward dependable general-purpose web agents.