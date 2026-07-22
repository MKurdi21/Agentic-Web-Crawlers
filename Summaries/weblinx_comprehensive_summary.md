# WEBLINX: Real-World Website Navigation with Multi-Turn Dialogue

**Authors:** Xing Han Lù, Zdeněk Kasner, and Siva Reddy

## 1. Background and Context

Most earlier web-navigation agents either operate in simplified simulations, specialize in one application, or autonomously execute a fully specified instruction. They do not adequately represent a more realistic situation in which a user’s objective develops through conversation and the agent must both operate a browser and ask or answer follow-up questions.

Website-specific conversational assistants also commonly depend on plugins. Because every plugin must be separately developed and may expose only part of a site’s functionality, the authors ask whether conversational language models can instead navigate arbitrary websites directly in the user’s browser.

They define **conversational web navigation** as a setting where an agent:

- receives an initial natural-language instruction;
- communicates with the user over multiple dialogue turns;
- observes and controls a real browser;
- asks for missing information or receives revised instructions;
- and completes a real-world task whose details may evolve during the conversation.

Potential applications include assisting visually impaired users, adding voice-controlled browsing to digital assistants, and reducing repetitive work while leaving the human in control. Scientifically, the problem tests instruction following, dialogue, environmental interaction, and transfer to unforeseen situations simultaneously.

Earlier benchmarks capture only portions of this setting. For example, MiniWoB++ is simplified; WebShop covers one e-commerce domain; Mind2Web is real-world and general but lacks dialogue; RUSS has dialogue but only 80 specialized help-center demonstrations; WorkArena has dialogue but one IT-management domain; and META-GUI focuses on mobile applications rather than browsers.

**Table 1** establishes WEBLINX’s distinguishing scale and scope. It is the only listed benchmark that simultaneously has multi-turn dialogue, general tasks, browser use, and real-world websites. It contains:

- 155 domains;
- 2,337 demonstrations;
- an average of 1,775 HTML elements per page;
- an average of 43.0 turns per demonstration.

By comparison, Mind2Web has 137 domains, 2,350 instances, 1,135 elements per page, and 7.3 turns; WebShop has one domain and 11.3 turns; RUSS has 22 domains, 80 instances, and 5.4 turns.

A key technical obstacle is scale: real pages may contain thousands of DOM elements, making the complete HTML representation too long and slow for a language model to process interactively. The paper therefore couples its benchmark with a fast method for retrieving only the most relevant page elements.

## 2. Research Goal and Objectives

The principal goal is to establish and study real-world conversational web navigation.

The paper has four explicit objectives:

1. Introduce the task and build **WEBLINX**, a large expert-annotated benchmark spanning real websites and multi-turn dialogue.
2. Develop action-specific metrics that fairly compare predicted browser and dialogue actions with human reference actions.
3. create an efficient method—**Dense Markup Ranking (DMR)**—for pruning large HTML pages into compact model inputs.
4. Evaluate text-only, image-only, and multimodal models, both zero-shot and finetuned, and measure their ability to generalize beyond familiar websites and scenarios.

The study also asks which inputs and modeling choices matter: specialized prior navigation training versus the new representation, screenshots versus structured text, model size, finetuning, and transfer to unseen websites, subcategories, geographies, and instructors who cannot see the browser.

## 3. Methods (Approach/Design)

### 3.1 The WEBLINX benchmark

WEBLINX stands for **Web Language Interface for Navigation and eXecuting actions**. It contains 2,337 demonstrations, over 100,000 recorded actions and utterances, and an average of 43 turns per demonstration. Tasks span:

- 155 real-world websites;
- 15 geographic areas;
- 8 broad categories;
- 50 subcategories.

The eight category totals shown in **Figure 2** are:

- Booking: 983 demonstrations
- AI Tools: 603
- Information Lookup: 391
- Shopping: 330
- Composing: 295
- Summarizing: 286
- Social Interaction: 276
- Productivity: 218

A demonstration can use more than one website or category, so these category counts are not mutually exclusive.

**Figure 1** illustrates the task with a Google Calendar interaction. The instructor asks the navigator to create a “Career Fair” task. The navigator opens Calendar, begins creating it, asks whether a description is needed, receives “Bring multiple copies of my resume,” enters that note, saves the task, and confirms completion. The example shows that the correct action depends on both the browser state and evolving dialogue.

### 3.2 Human data collection

Eight trained expert annotators from a professional labeling company worked in pairs:

- the **instructor** supplied natural-language instructions and follow-up information;
- the **navigator** communicated through chat and exclusively controlled the browser.

Normally, the instructor could see the navigator’s shared screen; in the `TEST_VIS` condition, the instructor could not. **Figure 3** summarizes this arrangement: instructor and navigator exchange instructions and replies, the navigator controls the browser, and the instructor views it except in the visionless split.

A custom Chrome extension recorded, for each browser action:

- a screenshot;
- the DOM tree;
- bounding boxes for visible elements;
- browser events;
- and the page state.

Zoom supplied screen recording, screen sharing, and chat. Browser states, actions, and chat were aligned in post-processing.

**Figure 6** presents the complete pipeline: the navigator controls the browser and communicates with the instructor; the browser interaction is recorded; data undergo post-processing; and the navigator uploads the results through a web interface to form the dataset.

A different annotator validated each demonstration under the original navigator’s supervision. Reviewers removed unnecessary actions, corrected asynchronously misordered events and typographical errors, and realigned screenshots to video frames. Screenshots with insufficient information for the recorded action were marked invalid. Screenshot realignment was necessary partly because Chrome permitted only one capture per 500 ms.

Annotators could start from recommended safe websites or choose other suitable sites. They were encouraged to record both short single-task demonstrations and complex, multi-subtask sessions. A demonstration ended when the instructor asked to terminate it. They were instructed to stop before consequential real-world actions such as actually buying a ticket or placing an order.

Annotators were paid US$7.50 per hour for recording and US$5 per hour for preparation, upload, and review, averaging US$2.58 per demonstration. Purpose-created accounts were used; identifying information was not retained.

### 3.3 Dataset splits

**Table 2** defines the splits:

- `TRAIN`: model training.
- `VALID`: in-domain hyperparameter selection.
- `TEST_IID`: in-domain evaluation.
- `TEST_WEB`: unseen websites from familiar subcategories.
- `TEST_CAT`: unseen subcategories within familiar broad categories.
- `TEST_GEO`: geographic locations absent from training.
- `TEST_VIS`: the instructor cannot see the browser.
- `TEST_OOD`: the aggregation of the four out-of-domain splits.

The detailed counts in **Table 8** are:

| Split | Demonstrations | Mean turns | SD | Active turns | Total turns |
|---|---:|---:|---:|---:|---:|
| Train | 969 | 44.93 | 17.37 | 24,418 | 43,538 |
| Validation | 100 | 40.76 | 14.51 | 1,717 | 4,076 |
| Test IID | 100 | 43.18 | 16.08 | 1,846 | 4,318 |
| Test CAT | 223 | 45.30 | 25.43 | 4,979 | 10,102 |
| Test WEB | 211 | 40.47 | 18.17 | 4,184 | 8,540 |
| Test VIS | 444 | 36.05 | 20.09 | 7,725 | 16,006 |
| Test GEO | 290 | 48.05 | 18.66 | 6,141 | 13,934 |

The shorter `TEST_VIS` demonstrations are attributed to fewer visually grounded follow-up requests. A sighted instructor can, for example, request a specific visible airline filter, whereas a nonsighted instructor would not ordinarily know it is present.

The flow labels in Figure 2 appear to aggregate split totals differently from Table 8, showing Train 1,404, Valid 140, Test-IID 146, and Test-OOD 1,692. Because the detailed table gives the authoritative demonstration counts above and the supplied text does not explain this discrepancy, it should not be resolved by assumption.

### 3.4 Website and task coverage

The benchmark includes popular and lesser-known sites to promote categorical and geographic diversity. The appendix lists all starting websites, covering applications such as calendars, email, flight and lodging search, restaurants, medical search, shopping, delivery, social media, translation, encyclopedias, news, scientific articles, writing assistants, image generation, and finance.

The 16 deliberately held-out `TEST_CAT` subcategories are spreadsheet, handmade products, reviews, computer vision, chatbot, transport, presentation, furniture, professional networking, books, tasks, automatic translation, question answering, encyclopedia, recipe, and geography. Five—handmade products, reviews, computer vision, professional networking, and geography—appear only in `TEST_CAT` rather than elsewhere.

AI tools were used in 280 demonstrations, with 46.79 mean turns and 13,100 total turns. The other 2,057 demonstrations averaged 42.50 turns and contained 87,414 turns.

### 3.5 States, actions, and history

Each demonstration is a sequence of states and actions. Depending on availability, a state contains:

- candidate target elements;
- the current DOM tree;
- a browser screenshot;
- the instructor’s current utterance;
- viewport height and width;
- interaction history.

Early conversational turns can lack screenshots and DOM data if the participants are still defining the task.

The five core evaluated actions in **Table 3** are:

- `click(element)`
- `load(url)`
- `say(text)`
- `submit(element)`
- `textinput(element, value)`

The complete observed action space in **Table 6 and Figure 5** adds coordinate-based clicks and hovers, `change`, `scroll`, `copy`, `paste`, and tab creation, removal, and switching. Overall, the dataset records 13 intent types. The model may produce navigator speech but not instructor speech.

Only `click`, `load`, `say`, `submit`, and `textinput` are evaluated. `change` and `scroll` are training targets but are excluded from evaluation because `change` does not occur in every split and scrolling cannot be evaluated reliably. Copy, paste, hover, and tab operations remain in the history.

**Table 7** reports action frequencies:

| Intent | Demos containing it | Mean occurrences | SD | Total |
|---|---:|---:|---:|---:|
| say | 2,337 | 16.82 | 5.62 | 39,305 |
| click | 2,333 | 14.52 | 10.16 | 33,865 |
| load | 2,324 | 1.59 | 1.07 | 3,702 |
| copy | 1,587 | 4.08 | 3.05 | 6,477 |
| textinput | 1,465 | 3.28 | 3.06 | 4,799 |
| paste | 1,130 | 1.89 | 1.95 | 2,141 |
| scroll | 1,046 | 3.82 | 3.00 | 3,999 |
| tab switch | 800 | 3.28 | 3.65 | 2,621 |
| tab create | 712 | 1.71 | 1.12 | 1,220 |
| submit | 645 | 1.40 | 1.11 | 904 |
| hover | 361 | 1.55 | 1.11 | 560 |
| tab remove | 309 | 1.94 | 1.17 | 599 |
| change | 165 | 1.95 | 1.34 | 322 |

Loads are less frequent because many tasks remain on one site or page. Unnecessary hover events were removed during curation.

Because models have limited context, the input retains the last five actions and the first plus last four instructor utterances. This preserves the initial objective while emphasizing recent changes. Earlier screenshots and element states are omitted.

Generated action strings are parsed with regular expressions into executable intent/argument structures. For coordinate-only vision models, coordinates are mapped to the smallest overlapping element, using default render order because CSS z-index is unavailable. URLs are normalized by removing a leading `www`, separating the network location, and tokenizing slash-separated path components.

### 3.6 Evaluation framework

A demonstration-level task-success rate is unsuitable because the complete objective may not be known at the first turn and can change through conversation. The authors therefore evaluate each turn.

- **Intent Match (IM):** 1 if predicted and reference intents match, otherwise 0.
- **Element IoU:** for click, submit, and text-input actions, intersection-over-union measures overlap between predicted and reference element bounding boxes, multiplied by IM. It penalizes nonoverlap and overly large or small target boxes.
- **Text F1:** for `say` and `textinput`, character-level chrF with character n-grams up to the default \(n=6\), multiplied by IM.
- **URLF:** for `load`, F1 over normalized URL segments rather than characters.

The **element group** consists of click, submit, and textinput and uses IoU. The **text group** includes load, say, and textinput and uses text or URL F1. A text-input action needs both the right element and the right content, so its turn score is `IoU × F1`. The final overall score is the micro-average across turn scores.

### 3.7 Dense Markup Ranking

The prior Mind2Web cross-encoder paired every candidate element with the entire query and took an average of 916 ms per turn. WEBLINX proposes **Dense Markup Ranking (DMR)**, a dual-encoder retrieval method.

DMR:

1. creates a simplified textual representation of the current state and history;
2. separately encodes that representation and each candidate HTML element;
3. learns cosine similarity scores, with the target element labeled 1 and other elements 0;
4. ranks all elements and passes the top 10 to the action model.

Training minimizes squared error between the binary label and cosine similarity. Because the state and candidate are independently encoded, computation grows with the sum of their separate squared lengths rather than the square of their concatenated length.

The selected DMR backbone is finetuned MiniLM. **Table 13** gives Recall@10:

| Ranker | ID | VIS | GEO | CAT | WEB | OOD |
|---|---:|---:|---:|---:|---:|---:|
| BGE | 74.44 | 60.07 | 48.82 | 43.61 | 47.55 | 50.01 |
| GTE | 73.24 | 56.91 | 44.46 | 42.74 | 48.39 | 48.16 |
| MiniLM | 74.27 | 59.73 | 50.95 | 44.05 | 52.75 | 51.87 |
| DeBERTa cross-encoder | 76.86 | 63.28 | 52.76 | 48.43 | 54.65 | 54.78 |

MiniLM therefore loses 2.91 OOD recall points relative to DeBERTa but is much faster. On 24,418 training turns, it required 4,545 seconds, or 186 ms per turn, versus 22,385 seconds and 916 ms for DeBERTa—approximately a fivefold speedup.

### 3.8 Optimal Text Representation and truncation

The paper’s **Optimal Text Representation (OTR)** retains:

- HTML tags, attributes, values, and children;
- viewport dimensions;
- each candidate’s unique ID, XPath, and bounding box;
- strategically truncated DOM, dialogue, candidates, and action history.

Inputs use the top 10 DMR candidates. Each candidate includes a tag, XPath, bounding box, attributes, and child tags.

Strategic truncation assigns budgets to each input component and shortens long subcomponents above a computed threshold rather than naively deleting everything from one end. It protects essential structures such as tags, bounding boxes, and field keys. The target length is 2,048 tokens: 700 for the DOM, 40 per retained utterance, 50 per action, 65 per candidate, and approximately 248 for the prompt.

**Figures 7 and 8** show the same Encyclopedia.com state in image and multimodal form. Pix2Act receives a screenshot with the viewport, utterances, and prior actions embedded as header text. Structured models receive pruned HTML, dialogue history, viewport dimensions, action history, and ten element candidates. Figure 8 highlights the target search field.

### 3.9 Models and training

The study examines 19 model variants from eight architecture families. Eleven major variants appear in the main aggregate table.

Three modality classes are used:

- **Text-only:** instruction, pruned DOM, candidate descriptions, and history.
- **Image-to-text:** screenshot plus instructions/history rendered into the image.
- **Multimodal:** screenshot plus structured textual inputs.

Models include MindAct/Flan-T5, Flan-T5 with OTR, Sheared-LLaMA, LLaMA-2 chat models, GPT-3.5 Turbo, GPT-4 Turbo, Pix2Act, Fuyu-8B, and GPT-4V. Five models are tested zero-shot; the remaining variants are finetuned.

Finetuning is performed once per hyperparameter setting with a fixed seed. Models generally use AdamW, bfloat16 precision, a linear scheduler, a 256-token output limit, and fully sharded data parallelism for models of at least 7B parameters. Most train for three or five epochs. GPT-3.5 is finetuned for three epochs. LLaMA and Sheared-LLaMA use learning rate \(5\times10^{-5}\); Fuyu uses the same; Pix2Act uses \(2\times10^{-5}\); and Flan-T5/MindAct use \(5\times10^{-5}\).

## 4. Results and Findings

### 4.1 Main out-of-domain and in-domain performance

**Table 4** reports the principal results:

| Model | Setting | Size | IM | IoU | F1 | OOD overall | IID overall |
|---|---|---:|---:|---:|---:|---:|---:|
| LLaMA-2 | Zero-shot | 13B | 43.7 | 4.8 | 1.3 | 5.2 | 5.6 |
| GPT-3.5T | Zero-shot | — | 42.8 | 8.6 | 3.5 | 8.5 | 10.3 |
| GPT-4T | Zero-shot | — | 41.7 | 10.9 | 6.8 | 10.7 | 12.2 |
| GPT-4V | Zero-shot | — | 42.4 | 10.9 | 6.2 | 10.4 | 12.9 |
| Pix2Act | Finetuned | 1.3B | 81.8 | 8.3 | 25.2 | 16.9 | 23.9 |
| Sheared-LLaMA | Finetuned | 2.7B | 84.0 | 22.6 | 27.2 | 25.0 | 37.4 |
| MindAct | Finetuned | 3B | 79.9 | 16.5 | 23.2 | 20.9 | 25.7 |
| Flan-T5 | Finetuned | 3B | 81.1 | 20.3 | 25.8 | 23.8 | 31.1 |
| Fuyu | Finetuned | 8B | 80.1 | 15.7 | 22.3 | 20.0 | 30.9 |
| LLaMA-2 | Finetuned | 13B | 83.0 | 22.8 | 26.6 | 25.2 | 37.0 |
| GPT-3.5F | Finetuned | — | 77.6 | 18.6 | 22.4 | 21.2 | 30.8 |

Key findings are:

- Every leading finetuned model substantially exceeds the best zero-shot models.
- Finetuned LLaMA-2-13B has the highest reported OOD overall score, 25.2, narrowly above 2.7B Sheared-LLaMA at 25.0.
- Sheared-LLaMA slightly exceeds LLaMA-2 on IID overall score, 37.4 versus 37.0.
- The strongest multimodal finetuned model, Fuyu-8B at 20.0 OOD, trails both smaller Sheared-LLaMA and LLaMA-2 text-only models.
- GPT-4V and GPT-4T are nearly tied, suggesting that GPT-4V does not effectively exploit screenshots for this action-prediction setup.
- Finetuned GPT-3.5 reaches 21.2 OOD, below open finetuned Sheared-LLaMA and LLaMA-2.

The supplementary consolidated table gives slightly more precise values: OOD overall is 25.21 for LLaMA-2-13B and 25.02 for Sheared-LLaMA-2.7B; IID overall is 37.09 and 37.43, respectively.

### 4.2 Effect of OTR and DMR-based representation

**Table 16** compares MindAct’s Mind2Web formatting against Flan-T5 with OTR on validation data:

| Model | Overall | IM | IoU | F1 |
|---|---:|---:|---:|---:|
| MindAct 250M | 17.78 | 77.05 | 19.02 | 9.87 |
| Flan-T5 OTR 250M | 21.91 | 79.27 | 24.10 | 11.02 |
| MindAct 780M | 21.39 | 77.58 | 22.46 | 15.32 |
| Flan-T5 OTR 780M | 23.94 | 80.26 | 24.90 | 15.99 |
| MindAct 3B | 27.86 | 79.91 | 24.24 | 24.79 |
| Flan-T5 OTR 3B | 31.97 | 82.00 | 31.18 | 27.81 |

OTR improves every size. At 3B, overall performance rises by 4.11 points, IoU by 6.94, and F1 by 3.02. The gap grows with model size, indicating that careful input construction becomes more important as capacity increases. Flan-T5 had no prior navigation training, whereas MindAct had been trained on Mind2Web, so representation is a substantial contributor.

### 4.3 Image-only versus multimodal models

**Table 17** reports validation results:

| Model | Overall | IM | IoU | F1 |
|---|---:|---:|---:|---:|
| Pix2Act 282M | 14.39 | 79.09 | 6.70 | 18.11 |
| Pix2Act 1.3B | 24.21 | 83.40 | 13.38 | 31.61 |
| Fuyu-8B | 31.60 | 81.36 | 26.34 | 30.99 |
| GPT-4V zero-shot | 14.26 | 41.00 | 14.44 | 6.06 |

Scaling Pix2Act from 282M to 1.3B produces a large improvement. Fuyu achieves the best overall and element scores, likely benefiting from text inputs and greater capacity, but Pix2Act-1.3B is slightly higher in IM and text F1. Zero-shot GPT-4V trails all finetuned models overall and has much lower intent and text scores.

Thus, larger multimodal models can outperform image-only models overall, but finetuned text-only chat decoders remain strongest.

### 4.4 Model size and finetuning

**Table 18** compares decoder-only text models on validation data:

| Model | Setting | Overall | IM | IoU | F1 |
|---|---|---:|---:|---:|---:|
| LLaMA-2-13B | Zero-shot | 6.07 | 39.55 | 5.54 | 1.62 |
| GPT-3.5T | Zero-shot | 11.48 | 41.93 | 11.67 | 3.16 |
| GPT-4T | Zero-shot | 13.75 | 41.64 | 13.83 | 6.58 |
| Sheared-LLaMA-2.7B | Finetuned | 35.47 | 86.14 | 33.80 | 34.20 |
| LLaMA-2-13B | Finetuned | 38.03 | 86.49 | 36.43 | 36.54 |
| GPT-3.5F | Finetuned | 28.98 | 79.03 | 27.42 | 25.99 |

Larger zero-shot models perform better, but scaling gives only a modest advantage after finetuning: 13B LLaMA-2 exceeds 2.7B Sheared-LLaMA by only 2.56 overall points on validation and is virtually tied on OOD data. A 2.7B finetuned model greatly exceeds GPT-4T zero-shot. GPT-3.5 finetuning helps substantially, but its result is below the smaller Sheared-LLaMA. The authors caution that GPT finetuning hyperparameters are mostly inaccessible, so the source of this difference is uncertain.

### 4.5 Generalization

All finetuned models drop sharply between IID and OOD evaluation. Examples include:

- Sheared-LLaMA-2.7B: 37.4 IID to 25.0 OOD.
- LLaMA-2-13B: 37.0 to 25.2.
- Fuyu-8B: 30.9 to 20.0.
- Flan-T5-3B: 31.1 to 23.8.
- Pix2Act-1.3B: 23.9 to 16.9.

For LLaMA-2-13B, **Table 5** breaks down OOD performance:

| Split | IM | IoU | F1 | Overall |
|---|---:|---:|---:|---:|
| TEST_WEB | 82.7 | 24.2 | 28.7 | 27.0 |
| TEST_CAT | 81.0 | 20.7 | 26.1 | 24.3 |
| TEST_GEO | 78.6 | 22.0 | 27.7 | 25.9 |
| TEST_VIS | 85.3 | 26.1 | 23.9 | 25.0 |

Unseen subcategories are hardest overall. A model may transfer from one restaurant-booking site to another, but not from restaurant booking to medical appointments. `TEST_VIS` has the highest IM and IoU but the lowest text F1, reflecting the different dialogue pattern when instructors cannot see the page.

The complete grouped tables show the same pattern. LLaMA-2-13B scores 24.27 on `TEST_CAT`, 25.93 on `TEST_GEO`, 25.00 on `TEST_VIS`, and 27.00 on `TEST_WEB`. Sheared-LLaMA-2.7B scores 25.06, 24.62, 24.12, and 26.82, respectively, demonstrating unusually strong robustness for its smaller size.

### 4.6 Sample action prediction

In the Encyclopedia.com example in **Figures 7–8 and Table 15**, the search field already contains the relevant state and the correct next action is to click the target field, either by element ID or coordinates.

Correct predictions are made by all listed Flan-T5 sizes, Fuyu-8B, both LLaMA-2 sizes, all MindAct sizes, both Sheared-LLaMA sizes, and Pix2Act-1.3B. Pix2Act-282M clicks the wrong coordinates. GPT-3.5T, GPT-4T, and GPT-4V instead predict text input for “biotechnology,” illustrating that an intuitively plausible action can still be inconsistent with the recorded trajectory.

**Figure 9** presents a related failure: a restaurant form’s location text is already filled. The correct action is to submit the form, but GPT-4T tries to type a date and GPT-4V repeats the existing location. LLaMA-2.7B correctly submits.

### 4.7 Qualitative click behavior

**Figures 4 and 10** compare zero-shot GPT-4V with finetuned LLaMA-2-13B:

1. On a news page, the instructor requests the 4:15 AM item. GPT-4V clicks 3:30 AM; LLaMA clicks 4:15 AM.
2. A delivery-location dialog is already open. GPT-4V attempts to close and reopen it, potentially creating a loop; LLaMA clicks “Change.”
3. When using Bard to draft an email, GPT-4V goes directly to a login page, whereas the reference and LLaMA open the homepage, which is more efficient if already authenticated.
4. When asked for the week’s top questions, GPT-4V correctly clicks “Week”; LLaMA clicks the inert heading “Top Questions.”

GPT-4V therefore often lacks awareness of the current task stage or chooses a locally plausible but inefficient action. Finetuned LLaMA usually does better but can still select noninteractive elements.

### 4.8 Qualitative text-input behavior

**Figures 4 and 11** show:

1. For an “Invitation to Collaboration” email, the correct subject is that phrase. GPT-4V enters the recipient name “Leon Tales”; LLaMA enters the correct subject.
2. In a password field, GPT-4V enters the email address; LLaMA enters the password.
3. When a passage has already been entered and the remaining step is choosing French, GPT-4V repeats passage content and LLaMA predicts a click rather than the required language input. Both fail to use the current multi-step context.
4. When a title was supplied earlier and an introduction later, GPT-4V and LLaMA produce only the introduction and omit the title. Long-range information remains difficult even after finetuning.

### 4.9 Dialogue-action behavior

**Table 19** shows that finetuned LLaMA learns the annotators’ short acknowledgment style—“Alright,” “Okay,” or “Sure”—whereas GPT-4V tends to be more elaborate.

More substantive GPT-4V failures include:

- supplying an incorrect discussion link when merely asked to share the link;
- refusing a feasible request;
- producing a different but pragmatically valid follow-up question.

For an email discount offer, the human asks who should receive the email, while GPT-4V asks about terms or an expiration date. Both questions could be useful, exposing a limitation of single-reference automatic evaluation.

Despite visible stylistic examples, the models’ mean reply lengths are close: LLaMA-2-13B averages 58.29 characters across 1,194 `say` predictions, versus GPT-4V’s 60.41 across 220 predictions on validation and IID data.

### 4.10 Human comparison

Three annotators supplied alternative actions for 134 validation turns, producing 402 annotations. Agreement was computed against the closest of the original or alternative plausible actions.

**Table 20** reports:

| Source | IM | Text F1 | Element IoU | Overall | Normalized |
|---|---:|---:|---:|---:|---:|
| Original navigator | 95.52 | 40.19 | 56.20 | 48.07 | 100.00 |
| Alternative annotator mean | 92.79 | 36.20 | 58.40 | 46.62 | 96.97 |
| LLaMA-2-13B | 91.04 | 34.37 | 28.44 | 31.45 | 65.42 |
| Fuyu-8B | 84.33 | 25.07 | 27.44 | 26.24 | 54.58 |
| GPT-4T | 58.21 | 12.47 | 21.46 | 16.90 | 35.15 |
| GPT-4V | 54.48 | 9.57 | 20.49 | 14.95 | 31.09 |

Humans agree strongly with one another, while LLaMA achieves only about 65% of the original human’s normalized overall score and GPT-4V about 31%. LLaMA’s intent score approaches human agreement, but its element grounding remains far behind.

Annotating all test splits was estimated to require roughly ten months for the three annotators, excluding tooling and logistical work.

### 4.11 In-context examples

**Table 21** tests whether adding action descriptions and one example per action improves non-finetuned models on `TEST_IID`.

- GPT-3.5T falls from 10.87 overall zero-shot to 8.50 with descriptions/examples.
- GPT-4V changes from 13.52 to 13.04.
- GPT-4V without screenshots scores 12.33.
- GPT-4T’s zero-shot baseline is 12.87; no description/example result is reported for it.

There is therefore no substantial benefit from these demonstrations. GPT-4V’s small screenshot advantage again suggests limited use of visual information.

## 5. Analysis and Interpretation

The experiments answer the paper’s main questions in several ways.

First, conversational web navigation is measurably difficult even for powerful models. Zero-shot GPT-4-class systems frequently identify the wrong action, ground the right intent to the wrong interface element, repeat completed steps, confuse form fields, or ignore information from earlier turns.

Second, **task-specific finetuning matters more than raw scale** in the tested setting. Finetuned 2.7B Sheared-LLaMA exceeds GPT-4T and GPT-4V zero-shot by a wide margin and performs nearly as well as 13B LLaMA-2. Finetuning appears to teach both browser-action conventions and the human navigators’ dialogue style.

Third, structured textual page representations remain more useful than screenshots for the models evaluated. Fuyu benefits from multimodality and beats image-only Pix2Act overall, but it does not match text-only chat decoders. GPT-4V barely exceeds or sometimes trails GPT-4T, implying that merely providing a screenshot does not guarantee effective visual grounding.

Fourth, representation quality is critical. OTR’s preservation of element attributes, IDs, XPaths, boxes, viewport information, dialogue, and structured truncation consistently improves Flan-T5 over MindAct formatting. DMR makes this richer representation feasible in near-real-time by reducing candidate-selection latency from 916 to 186 ms while sacrificing only a few Recall@10 points.

Fifth, familiar-distribution scores can substantially overstate real-world readiness. All finetuned systems deteriorate on held-out environments. The narrow gap between 2.7B and 13B text decoders outside the training distribution indicates that greater parameter count alone does not solve transfer. Unseen task subcategories are especially difficult.

Finally, exact-reference scoring remains imperfect. Different replies or alternate browser paths may both be reasonable, while visually overlapping elements may be functionally equivalent. The proposed action-specific metrics reduce this problem but do not eliminate it, as demonstrated by GPT-4V’s pragmatically valid alternative follow-up question and the human alternative-trajectory study.

## 6. Contributions and Novelty

The paper contributes:

- The formulation of **real-world conversational web navigation**, combining browser control with evolving multi-turn dialogue.
- **WEBLINX**, the first benchmark in the paper’s comparison to combine dialogue, general tasks, real browser use, and large-scale real-world coverage: 2,337 demonstrations, 155 websites, 15 geographic areas, 8 categories, 50 subcategories, and over 100,000 actions and utterances.
- Rich records connecting each action to DOM trees, screenshots, element boxes, chat, and demonstration video.
- Carefully designed IID and four-way OOD evaluation covering new websites, subcategories, geographies, and visionless instructors.
- An action-specific evaluation framework using intent match, element IoU, text chrF, URL-segment F1, and micro-averaged turn scores.
- **Dense Markup Ranking**, a retrieval-style DOM candidate selector that operates approximately five times faster than the prior cross-encoder.
- **Optimal Text Representation** and strategic component-aware truncation for large HTML pages and long interaction histories.
- A comparison of 19 model variants across eight architectures and three modality classes.
- Empirical evidence that small finetuned text decoders can beat much larger zero-shot and multimodal systems, but still generalize poorly.
- Public research release of the benchmark, code, data, and models.

## 7. Limitations and Caveats

- **Static demonstrations:** The benchmark contains fixed human trajectories. It cannot meaningfully test interactive recovery or alternative action paths in a live environment.
- **Reference ambiguity:** Multiple dialogue replies or browser actions may be valid. Automatic metrics can penalize a reasonable response because it differs lexically or follows another trajectory.
- **Limited history:** Models see only five recent actions and the initial plus four recent utterances. They do not receive previous screenshots or past DOM states, contributing to failures involving information supplied many turns earlier.
- **Candidate-retrieval loss:** MiniLM DMR is faster but has lower Recall@10 than DeBERTa—51.87 versus 54.78 on aggregate OOD data. If the correct element is not retrieved, the downstream text model cannot select it.
- **Generalization failure:** Every finetuned system drops markedly on OOD splits, especially unseen subcategories.
- **Modality limitations:** Text-only models cannot inspect images or draw on canvases. Image-only models struggle with long textual instructions. Existing multimodal models are not jointly optimized to parse full HTML and screenshots.
- **One training run per configuration:** Computational cost permitted only one finetuning run for each hyperparameter setting. The fixed seed improves reproducibility, but variation across runs is not measured.
- **Commercial-model opacity:** GPT-3.5 finetuning exposes few hyperparameters, making its weaker result difficult to diagnose.
- **No significance testing:** The paper reports benchmark metrics but no statistical significance tests or confidence intervals.
- **Human comparison scope:** Human agreement is measured on only 134 validation turns rather than complete test sets.
- **Potential recording lag:** Chrome’s screenshot rate caused delays requiring video-based realignment.
- **Safety and deployment:** Agents may book the wrong flight or take other consequential unintended actions. The authors state that the released models should not be deployed and should remain under human supervision with dialogue enabled.
- **Labor impact:** Powerful agents could automate work performed by knowledge workers. The proposed framework aims instead to keep a human instructor in control and automate repetitive, difficult, or error-prone steps.
- **Malicious use:** The same technology could automate spam, impersonation, or fraud. Open research access may also support defensive work and red teaming.
- **Consequential tasks were intentionally incomplete:** Demonstrations stop before purchases, bookings, or similar real-world changes, so successful execution of those final actions is not evaluated.

## 8. Future Work or Open Questions

The authors propose:

- multimodal architectures that efficiently combine visual inputs with structured HTML information;
- environments spanning more complex websites and advanced browser events;
- extension beyond browsers to operating-system-level interaction;
- reward-based optimization such as reinforcement learning from human feedback and direct preference optimization;
- alternative training methods based on self-experience and grounded synthetic data;
- multimodal-specific capabilities for tasks that text-only systems cannot perform;
- broader human annotation of alternative valid trajectories;
- and models that retain the benefits of finetuning while generalizing to new websites, subcategories, locations, and dialogue conditions.

A central unresolved question is how to evaluate and train agents when more than one action or conversational response is valid. Another is how to supply enough long-term state without making real-time processing prohibitively slow.

## 9. High-Level Takeaway (Plain Language)

WEBLINX studies an assistant that can chat with a person while directly using ordinary websites on their behalf. The authors collected 2,337 detailed human demonstrations across 155 sites and created methods for shrinking huge webpages into manageable inputs and scoring different kinds of actions fairly. Small language models trained on these demonstrations performed better than zero-shot GPT-4V and larger screenshot-based models, showing that focused training and good HTML representation matter greatly. However, even the best system achieved only about 65% of human-level agreement in a sampled comparison and deteriorated substantially on unfamiliar tasks and websites. The benchmark therefore shows both the promise of conversational browser agents and how far they remain from safe, reliable real-world use.