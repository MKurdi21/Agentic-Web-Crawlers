# VisualWebArena: Evaluating Multimodal Agents on Realistic Visually Grounded Web Tasks

**Authors:** Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Chong Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, and Daniel Fried  
**Affiliation:** Carnegie Mellon University  
**Publication:** Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics, 2024, pp. 881–905  
\*Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Chong Lim, and Po-Yu Huang are marked as equal contributors.

## 1. Background and Context

Autonomous web agents aim to complete routine computer tasks by interpreting instructions, planning actions, navigating interfaces, and changing website state. Existing benchmarks, however, largely evaluate agents through text or structured HTML representations. This overlooks an important fact: modern interfaces are designed for human vision, and essential information may appear only through images, colors, icons, spatial layout, or visually referenced objects.

Tasks such as ordering a green shirt, locating a post containing a particular picture, or finding a product that resembles an input image cannot reliably be solved from text alone. This creates both an evaluation gap and a development gap: if benchmarks neglect visual interaction, they give researchers little incentive or evidence for improving multimodal agents.

The paper builds on WebArena, which provides reproducible, self-hosted websites and evaluates agents by checking whether their actions actually produce the requested result. VisualWebArena extends this framework with tasks specifically designed to require visual understanding.

Relevant preceding research includes:

- Reproducible reinforcement-learning and web-interaction environments.
- Web benchmarks based on static pages or simulated interactive sites.
- LLM agents that use prompting, chain-of-thought reasoning, multiple coordinated agents, or trajectory fine-tuning.
- Vision-language models for image captioning, visual question answering, multimodal instruction following, mobile-device navigation, and web interaction.
- Set-of-Marks prompting, which adds numbered visual markers to interface elements so a vision-language model can refer to them directly.

The distinguishing feature of this work is that its Set-of-Marks agent uses JavaScript to label interactable webpage elements and supplies those labels directly as both the visual reference system and action space.

## 2. Research Goal and Objectives

The main goal is to create a realistic, reproducible benchmark for measuring how well autonomous multimodal agents can understand visual and textual information and act on websites.

The paper pursues four connected objectives:

1. Construct a broad collection of visually grounded web tasks requiring image understanding, language interpretation, navigation, and action execution.
2. Develop execution-based evaluation functions that can judge diverse and open-ended visual tasks.
3. compare text-only LLM agents, caption-augmented agents, and fully multimodal vision-language agents.
4. Test whether a Set-of-Marks representation can simplify visual grounding and improve navigation.

The work also analyzes which task properties remain difficult—especially OCR, action and visual complexity, exact image matching, interleaved image-text inputs, and long multi-step execution—and documents common agent failure modes.

## 3. Methods (Approach/Design)

### 3.1 Benchmark environment

VisualWebArena contains **910 tasks** across three principal self-hosted environments:

- **Shopping:** an e-commerce environment inherited from WebArena, with product content originally scraped from Amazon and released through WebShop.
- **Reddit:** a forum environment inherited from WebArena, containing **31,464 posts** with natural images, memes, electronics, charts, and other content.
- **Classifieds:** a newly introduced marketplace based on the open-source OSClass content-management system. It supports searching, posting, commenting, reviews, and ratings.

Some tasks span multiple sites or use a self-hosted Wikipedia installation as a knowledge base. Self-hosting provides reproducibility, realism, and deterministic website behavior.

The Classifieds environment contains **65,955 listings**, each with a title, description, and product image. Its data were scraped over three weeks from Craigslist categories focused on the northeastern United States. Personally identifiable information—including addresses, phone numbers, and email addresses—was redacted using the `scrubadub` package. Names, emails, and phone numbers were replaced with generated placeholders, fictitious email addresses, and fictional 555-prefix numbers.

### 3.2 Formal model

The agent-environment interaction is represented as a partially observable Markov decision process:

\[
\mathcal{E}=(S,A,\Omega,T)
\]

Here:

- \(S\) is the set of website states.
- \(A\) is the set of possible actions.
- \(\Omega\) is the set of partial observations available to the agent.
- \(T:S\times A\rightarrow S\) is a deterministic transition function.

At time \(t\), the environment is in state \(s_t\). The agent receives an observation \(o_t\), selects an action \(a_t\), and moves to \(s_{t+1}\), receiving a new observation \(o_{t+1}\).

The binary reward is:

\[
R:S\times A\rightarrow\{0,1\}
\]

A reward of 1 is assigned at the final step if the execution satisfies the task objective; otherwise the reward is 0.

### 3.3 Observation representations

An observation can contain the current URL, all open browser tabs, the focused webpage, and—when applicable—input images included in the user’s instruction. **25.2% of tasks contain one or more input images.**

The paper considers four webpage representations:

1. **Raw DOM/HTML:** the webpage’s document structure.
2. **Accessibility tree:** a simplified structured representation designed for assistive technology and used by WebArena’s text-agent baselines.
3. **RGB screenshot:** a visual image of the current page.
4. **Set-of-Marks (SoM):** a screenshot in which every interactable element is outlined with a bounding box and assigned a unique numerical ID.

The SoM version is accompanied by a textual listing of the marked elements, their HTML-like element types, and their text or image captions.

**Figure 1** presents the overall benchmark pipeline. An agent receives a webpage and a task specification, possibly containing images, and navigates among Classifieds, Reddit, Shopping, Wikipedia, and related resources by issuing actions such as `click [1602]`. Example tasks include creating a listing for an pictured item, locating an image-based Reddit post, and buying an item to be delivered to a place shown in an image.

**Figure 2** illustrates SoM preprocessing. A Reddit-like page is converted into an annotated screenshot plus a list such as `[7] [A] [Comments]` and `[9] [IMG] [description: picture of a pumpkin]`. The agent can then select an element through a compact action such as `click [31]`.

This ID-based scheme avoids requiring a model to predict exact screen coordinates. It shifts the problem toward higher-level reasoning because the evaluated LLMs and VLMs were not necessarily trained for fine-grained coordinate prediction.

### 3.4 Action space

**Table 1** defines the available actions:

| Action | Meaning |
|---|---|
| `click [elem]` | Click an element |
| `hover [elem]` | Hover over an element |
| `type [elem] [text]` | Type text into an element |
| `press [key_comb]` | Press a keyboard combination |
| `new_tab` | Open a new tab |
| `tab_focus [index]` | Focus the indexed tab |
| `tab_close` | Close the current tab |
| `goto [url]` | Open a URL |
| `go_back` | Use the browser’s back function |
| `go_forward` | Use the forward function |
| `scroll [up\|down]` | Scroll the page |
| `stop [answer]` | End the task and optionally return an answer |

For accessibility-tree agents, action arguments refer to tree element IDs. For SoM agents, they refer to the current page’s marked visual IDs.

### 3.5 Evaluation functions

The benchmark uses manually written binary reward functions. For information-seeking tasks, the agent outputs a string \(\hat{a}\), which is compared with a ground-truth answer \(a^*\):

- **`exact_match`:** succeeds only when \(\hat{a}=a^*\).
- **`must_include`:** succeeds if every required element appears in the answer, allowing unordered lists or answers containing required keywords.
- **`fuzzy_match`:** asks GPT-4 Turbo whether the predicted and ground-truth answers are semantically equivalent. GPT-4 Turbo returns “correct,” “incorrect,” or “partially correct”; only “correct” receives reward 1.
- **`must_exclude`:** succeeds only if none of the prohibited elements appears in the answer.
- **`eval_vqa`:** asks BLIP-2-T5XL a visual question about a selected image. Reward is 1 if its answer contains the ground-truth answer.
- **`eval_fuzzy_image_match`:** compares a candidate image with a ground-truth image using the structural similarity index, or SSIM, and succeeds when similarity exceeds a task-specific threshold.

For navigation and state-changing tasks, evaluators inspect a specified URL or the final page reached. A locator selects relevant text or images—for example, every image with a particular CSS class—and the same matching functions judge whether the page is in the correct state.

The paper uses binary rewards only. It identifies partially graded or continuous performance measures as a possible future extension.

**Table 2** shows how these functions support diverse objectives:

- Buying the least expensive red blanket is evaluated by checking the latest order URL and requiring both a specific product ID and “Red.”
- Adding a green polo shirt like one shown in an input image to a wish list is evaluated by asking whether the resulting product is a polo shirt and whether it is green.
- Creating posts from supplied images is evaluated with fuzzy image matching.
- Changing a white-car listing’s price to \$25,000 requires the new price and prohibits the old \$30,000 price.

### 3.6 Task creation

Six computer-science graduate students, all co-authors, created the tasks. They were familiar with real commercial versions of the three website types and first explored the self-hosted sites.

They wrote **314 unique task templates** and instantiated them with different arguments, producing an average of **2.9 tasks per template**. The authors checked that tasks were not repeated and avoided excessive concentration on a single task type.

Input images came from royalty-free, attribution-free sources and MS-COCO. Annotators also wrote each task’s reward function.

Of the 910 tasks:

- **46 tasks, or 5.1%, are deliberately unachievable.**
- For an unachievable task, the agent must stop and explain why it cannot be completed.
- The explanation is graded with `fuzzy_match`.

### 3.7 Site and difficulty distributions

**Figure 4** reports the task distribution:

- Shopping: **50.9%**
- Classifieds: **25.5%**
- Reddit: **18.7%**
- Multi-site: **4.9%**

**Figure 5** cross-tabulates visual and action difficulty:

| Action difficulty | Easy visual | Medium visual | Hard visual |
|---|---:|---:|---:|
| Easy | 15.7% | 12.9% | 4.2% |
| Medium | 13.7% | 12.6% | 8.5% |
| Hard | 7.0% | 10.5% | 14.8% |

Action difficulty is based on the estimated human action count:

- Easy: at most 3 actions.
- Medium: 4–9 actions.
- Hard: at least 10 actions.

Visual difficulty is defined as:

- Easy: colors, shapes, and high-level object recognition.
- Medium: patterns, semantic interpretation, or OCR of short, large text.
- Hard: multiple images, small or lengthy OCR, or fine visual details.

Overall difficulty averages visual and reasoning/action complexity, with human judgment allowed to adjust cases that disproportionately test one dimension.

### 3.8 Human evaluation

Seven college students completed a representative sample of **230 tasks**, one per selected template. Some had helped create tasks, but no evaluator received a task they had authored.

Humans achieved **88.70% overall success**:

- Classifieds: **91.07%**
- Reddit: **87.10%**
- Shopping: **88.39%**

Human errors were usually minor: misreading part of the instruction, adding an item to the cart instead of the wish list, abandoning an exhaustive image search after 5–10 minutes, or failing to inspect every product page when looking for the cheapest or most highly reviewed item. The authors suggest that sufficiently strong agents could eventually exceed humans on speed and exhaustive search.

### 3.9 Baseline agents

All principal baselines were prompt-based and received **three non-overlapping in-context examples**, one from each main environment.

The evaluated families were:

- **Text-only agents:** LLaMA-2-70B, Mixtral-8x7B, Gemini-Pro, GPT-3.5 Turbo, and GPT-4 Turbo. They used chain-of-thought prompting and accessibility-tree observations.
- **Caption-augmented agents:** image elements and task images were captioned, and captions were inserted as image alt-text in the accessibility tree. GPT-3.5 was tested with LLaVA-v1.5-7B and BLIP-2-T5XL; BLIP-2 was retained thereafter because it was slightly more accurate, smaller, and required less GPU memory.
- **Multimodal agents:** IDEFICS-80B-Instruct, CogVLM, Gemini-Pro, and GPT-4V. They received a page screenshot, BLIP-2 captions, and either the accessibility tree or SoM representation.

### 3.10 Experimental settings

Most baselines used:

- Viewport: **1280 × 2048**
- Text limit: **3,840 tokens**, or **15,360 characters for Gemini**

Models with shorter context windows—LLaMA, IDEFICS, and CogVLM—used:

- Viewport: **1280 × 720**
- Text limit: **640 tokens**

Sampling settings were:

- GPT-3.5 and GPT-4: temperature **1.0**, top-p **0.9**
- Gemini: temperature **0.9**, top-p **1.0**
- Remaining models: temperature **0.6**, top-p **0.95**

All experiments used nucleus sampling.

**Figures 16 and 17** provide the SoM agent’s prompt design. The system message explains the objective, marked screenshot, element list, URL, tabs, preceding action, legal actions, and output format. It tells the model to issue one valid action at a time, reason step by step, and stop when the goal is achieved. The three examples teach it to answer a product-price question, navigate to a Reddit comment section, and search Classifieds for the cheapest dark-colored guitar. Multimodal and SoM examples include screenshots; text-only and caption-based examples contain only text and captions.

## 4. Results and Findings

### 4.1 Main benchmark results

**Table 3** reports the principal success rates:

| Agent | Classifieds | Reddit | Shopping | Overall |
|---|---:|---:|---:|---:|
| **Text-only** |||||
| LLaMA-2-70B | 0.43% | 1.43% | 1.29% | 1.10% |
| Mixtral-8x7B | 1.71% | 2.86% | 1.29% | 1.76% |
| Gemini-Pro | 0.85% | 0.95% | 3.43% | 2.20% |
| GPT-3.5 | 0.43% | 0.95% | 3.65% | 2.20% |
| GPT-4 | 5.56% | 4.76% | 9.23% | 7.25% |
| **Caption-augmented** |||||
| LLaMA-2-70B + BLIP-2 | 0.00% | 0.95% | 0.86% | 0.66% |
| Mixtral-8x7B + BLIP-2 | 1.28% | 0.48% | 2.79% | 1.87% |
| GPT-3.5 + LLaVA | 1.28% | 1.43% | 4.08% | 2.75% |
| GPT-3.5 + BLIP-2 | 0.85% | 1.43% | 4.72% | 2.97% |
| Gemini-Pro + BLIP-2 | 1.71% | 1.43% | 6.01% | 3.85% |
| GPT-4 + BLIP-2 | 8.55% | 8.57% | 16.74% | 12.75% |
| **Multimodal: screenshot + captions + accessibility tree** |||||
| IDEFICS-80B-Instruct | 0.43% | 0.95% | 0.86% | 0.77% |
| CogVLM | 0.00% | 0.48% | 0.43% | 0.33% |
| Gemini-Pro | 3.42% | 4.29% | 8.15% | 6.04% |
| GPT-4V | 8.12% | 12.38% | 19.74% | 15.05% |
| **Multimodal: screenshot + captions + SoM** |||||
| IDEFICS-80B-Instruct | 0.85% | 0.95% | 1.07% | 0.99% |
| CogVLM | 0.00% | 0.48% | 0.43% | 0.33% |
| Gemini-Pro | 3.42% | 3.81% | 7.73% | 5.71% |
| GPT-4V | 9.83% | 17.14% | 19.31% | 16.37% |
| **Humans** | **91.07%** | **87.10%** | **88.39%** | **88.70%** |

The strongest original baseline, GPT-4V + SoM, reached only **16.37%**, leaving a **72.33-percentage-point** gap to humans.

Text-only GPT-4 achieved **7.25%**. Adding BLIP-2 captions raised it to **12.75%**. Giving GPT-4V direct visual input raised performance to **15.05%**, and SoM raised it further to **16.37%**.

Gemini-Pro followed the same broad multimodality pattern:

- Text only: **2.20%**
- Caption augmented: **3.85%**
- Multimodal with accessibility tree: **6.04%**
- Multimodal with SoM: **5.71%**

Thus, multimodality helped Gemini-Pro, but SoM did not improve it.

### 4.2 Effect of Set-of-Marks

For GPT-4V, switching from accessibility-tree grounding to SoM changed success as follows:

- Overall: **15.05% → 16.37%**
- Classifieds: **8.12% → 9.83%**
- Reddit: **12.38% → 17.14%**
- Shopping: **19.74% → 19.31%**

The prose surrounding Table 3 reverses the Classifieds and Reddit site values when describing these changes, stating 12.38%→17.14% for Classifieds and 8.12%→9.83% for Reddit. The table itself associates **8.12%→9.83% with Classifieds** and **12.38%→17.14% with Reddit**.

The authors attribute the benefit to visually dense pages where many small images or controls are spatially close and difficult to distinguish through an accessibility tree. SoM directly links visible elements to action IDs.

IDEFICS improved only from **0.77% to 0.99%**, CogVLM remained at **0.33%**, and Gemini-Pro declined from **6.04% to 5.71%**. The authors conclude that benefiting from SoM requires sufficiently strong visual grounding, which only GPT-4V clearly displayed among these initial models.

**Figure 3** gives a successful GPT-4V + SoM trajectory. The task asks the agent to block the author of a particular image among hot `/f/memes` posts. The agent searches for `/f/memes`, navigates to the forum list when its first attempt fails, enters the correct forum, visually identifies the target image, opens the author’s profile, clicks “block,” and confirms the action. It succeeds without unnecessary actions once it reaches the relevant page.

### 4.3 Performance by task type

**Table 4** analyzes GPT-4V + SoM:

| Task subset | Share | Success rate |
|---|---:|---:|
| OCR required | 17.1% | 13.4% |
| No OCR required | 82.9% | 16.9% |
| Exact image match | 8.7% | 18.9% |
| No exact image match | 91.3% | 16.2% |
| Image input present | 25.2% | 19.0% |
| No image input | 74.8% | 14.9% |

OCR is therefore a bottleneck for GPT-4V + SoM. Exact image matching is not the main bottleneck, and tasks containing input images were actually easier for this agent once visual content was correctly understood.

There are **229 image-input tasks**, corresponding to the reported 25.2%.

### 4.4 Difficulty analysis

**Figure 6a: GPT-4 text-only success**

| Action difficulty | Easy visual | Medium visual | Hard visual | Overall |
|---|---:|---:|---:|---:|
| Easy | 18.9% | 11.1% | 10.5% | 14.8% |
| Medium | 1.6% | 6.1% | 7.8% | 4.7% |
| Hard | 1.6% | 4.2% | 1.5% | 2.4% |
| Overall | 9.0% | 7.3% | 4.8% | 7.3% |

**Figure 6b: GPT-4 + captions**

| Action difficulty | Easy visual | Medium visual | Hard visual | Overall |
|---|---:|---:|---:|---:|
| Easy | 23.1% | 18.8% | 13.2% | 20.1% |
| Medium | 14.4% | 9.6% | 5.2% | 10.4% |
| Hard | 7.8% | 7.3% | 8.1% | 7.8% |
| Overall | 16.9% | 12.2% | 8.0% | 12.7% |

**Figure 6c: GPT-4V + SoM**

| Action difficulty | Easy visual | Medium visual | Hard visual | Overall |
|---|---:|---:|---:|---:|
| Easy | 30.1% | 20.5% | 26.3% | 25.8% |
| Medium | 15.2% | 11.3% | 11.7% | 12.9% |
| Hard | 14.1% | 10.4% | 8.9% | 10.5% |
| Overall | 21.4% | 14.3% | 12.4% | 16.4% |

Success generally declines as either action or visual difficulty increases. On hard visual tasks:

- GPT-4 text only: **4.8%**
- GPT-4 + captions: **8.0%**
- GPT-4V + SoM: **12.4%**

This is the clearest evidence that direct multimodality becomes especially useful when the visual problem is difficult.

**Figure 6d** reports GPT-4V + SoM’s mean trajectory length:

| Action difficulty | Easy visual | Medium visual | Hard visual | Overall |
|---|---:|---:|---:|---:|
| Easy | 6.0 | 7.7 | 6.1 | 6.9 |
| Medium | 10.4 | 10.6 | 7.2 | 10.0 |
| Hard | 14.1 | 9.2 | 12.5 | 12.1 |
| Overall | 9.5 | 9.4 | 10.2 | 9.6 |

Harder action tasks generally require longer trajectories.

### 4.5 OCR, exact matching, and image-input comparisons across agents

**Figure 7** compares OCR and non-OCR success for several Gemini-Pro and GPT-4 configurations. The exact plotted values are small, but the paper explicitly reports the central comparison:

- For GPT-4, moving from caption-based input to multimodality raises OCR-task success from **6.4% to 12.2%**.
- GPT-4-family agents generally perform worse on OCR tasks than on non-OCR tasks.
- Gemini-Pro’s multimodal and SoM variants show a disproportionately large gain on OCR tasks; unlike GPT-4, the multimodal Gemini-Pro agents perform better on OCR tasks than non-OCR tasks.

The authors suggest Gemini-Pro may possess useful inherent OCR capability, though they present this as an interpretation requiring further study.

**Figure 8** compares exact-image-match and non-match tasks:

- GPT-4V + SoM performs better on exact-match tasks than on other tasks.
- Other GPT-4 variants perform relatively worse on exact matches.
- Gemini variants perform substantially worse on exact-match tasks than on non-match tasks.
- For both model families, direct multimodality improves exact matching, and SoM provides an additional gain.

**Figure 9** compares tasks with and without image inputs:

- GPT-4’s captioned, multimodal, and SoM agents perform better when the task includes an input image.
- GPT-4 text-only performs worse on those tasks because it lacks access to the visual information.
- Gemini-Pro generally performs worse on image-input tasks, suggesting difficulty with multiple interleaved image and text inputs.

### 4.6 Trajectory length and success

**Figure 10** groups GPT-4V + SoM trajectories by length. Most runs terminate in fewer than ten actions, indicating that the model often assumes tasks can be completed quickly.

Success rates across trajectory-length bins are approximately:

- 0–5 actions: **22.0% pass**, 78.0% fail
- 5–10: **11.4% pass**, 88.6% fail
- 10–15: **16.0% pass**, 84.0% fail
- 15–20: **14.7% pass**, 85.3% fail
- 20–25: **10.8% pass**, 89.2% fail
- 25–30: **21.1% pass**, 78.9% fail
- 30–35: **9.9% pass**, 90.1% fail

Longer trajectories do not show a consistently higher success rate. Failures remain common at all lengths.

### 4.7 Few-shot prompting

**Table 6** evaluates multimodal Gemini-Pro with screenshot, captions, and accessibility tree:

| In-context examples | Classifieds | Reddit | Shopping | Overall |
|---:|---:|---:|---:|---:|
| 0 | 4.29% | 2.38% | 0.43% | 2.86% |
| 1 | 5.36% | 1.43% | 2.14% | 3.63% |
| 3 | 8.15% | 4.29% | 3.42% | 6.04% |

Overall performance rises with more demonstrations, particularly from one to three examples. The authors infer that training or fine-tuning on web trajectories may produce substantial improvements.

### 4.8 Results from newer models

After the paper’s original submission, the authors tested newer models.

**Table 5** reports:

| Agent | Input type | Classifieds | Reddit | Shopping | Overall |
|---|---|---:|---:|---:|---:|
| Llama-3-70B-Instruct | Caption augmented | 7.69% | 5.24% | 12.88% | 9.78% |
| Gemini-Flash-1.5 | Image + captions + SoM | 3.85% | 4.76% | 8.80% | 6.59% |
| Gemini-Pro-1.5 | Image + captions + SoM | 5.98% | 12.86% | 14.59% | 11.98% |
| GPT-4o | Image + captions + SoM | 20.51% | 16.67% | 20.82% | 19.78% |

GPT-4o becomes the strongest reported model at **19.78%**, compared with GPT-4V + SoM at **16.37%**, but remains far below human performance.

Llama-3-70B-Instruct’s **9.78%** is much higher than caption-augmented LLaMA-2-70B’s **0.66%** and GPT-3.5’s **2.97%**, though still below caption-augmented GPT-4’s **12.75%**.

### 4.9 Qualitative successes and failures

#### Strong visual navigation

**Figure 13** shows GPT-4V + SoM completing a Classifieds task: find the latest white Google Pixel listing and comment with an offer \$10 below its price. The agent searches for “white Google Pixel phone,” filters to cell phones, switches to list view, opens the relevant result, fills the comment title, writes an offer of **\$250**, and posts it. The trace includes a redundant repetition of the comment title but still succeeds.

The authors contrast this with the non-SoM multimodal agent, which could not search effectively. SoM reduced the need to co-reference an accessibility-tree element with its visual location.

#### Fine-grained recognition versus captions

On a Reddit task involving a Pittsburgh skyline, GPT-4V + SoM recognizes UPMC and PNC logos and navigates to `/f/pittsburgh`. BLIP-2 merely captions the image as a city skyline with tall buildings, losing the information needed to identify Pittsburgh.

This illustrates a central limitation of caption pipelines: captions tend to preserve salient global content while omitting fine details required by the task.

#### Failure over long horizons

Agents sometimes complete the correct action and then undo it:

- A caption-augmented GPT-4 agent correctly adds a waves-themed poster to a wish list, then removes it because the wish-list text does not explicitly mention waves.
- GPT-4V + SoM adds the correct banana-themed product to the cart, begins checkout, then stops because it doubts its earlier selection.

These failures indicate weak state tracking and inconsistent commitment to earlier visual judgments.

#### Failures on nominally easy tasks

**Figure 11** shows the starting page for an instruction to add the red product in the second row to the cart. GPT-4V variants click a blue tablecloth in the first row and give up when no red option is available. None of the evaluated agents completes the task, despite its easy action and visual labels.

#### Giving up too early

On a task involving green chocolate bars, GPT-4V + SoM correctly identifies the product but stops because the “add to cart” control is initially below the viewport; it does not try scrolling. Other agents similarly stop after one unsuccessful search instead of reformulating the query or trying a new navigation route.

#### Loops and repeated actions

Agents sometimes oscillate between pages or tabs. In one Classifieds comparison task, GPT-4V spends most of its allowed trajectory switching between two tabs rather than completing the comparison.

**Figure 12** traces an unsuccessful multi-site task asking the agent to prepend South Korea’s country code to a profile phone number. It illustrates three recurring problems:

- The agent opens a blank tab that it never uses.
- It appends the corrected number instead of replacing the old value.
- It repeats the correction and submission actions until reaching the trajectory limit.

The authors propose stronger tracking of past states and action history as a likely remedy.

#### Text-only versus caption-augmented agents

On a Reddit task requiring navigation to a post containing a keyboard picture, text-only GPT-4 is the only GPT-4 baseline to fail. It guesses the hottest `/f/MechanicalKeyboards` post from the title, but that post’s image does not contain a keyboard. Caption or direct-image access provides the needed grounding.

### 4.10 Classifieds interface visuals

**Figure 14** shows the Classifieds homepage, which contains keyword search, category selection, location filters, latest listings with images and prices, category links, and a “Publish Ad” function.

**Figure 15** shows an individual Nintendo Switch listing priced at **\$270.00**, with publication and location information, a large product image, seller details, related listings, and controls for contacting the seller, sharing, rating, and posting comments. These visuals demonstrate why the environment requires both spatial navigation and image understanding.

## 5. Analysis and Interpretation

The results support the paper’s central claim that direct visual access matters for realistic web agents. Text-only systems perform poorly because accessibility trees and page text omit colors, object identity, spatial grouping, small printed text, and image correspondence.

Caption augmentation helps substantially—most clearly for GPT-4, which improves from 7.25% to 12.75%—but remains an incomplete substitute for direct visual reasoning. Captions compress images into generic descriptions and often omit non-salient details, precise text, logos, colors, or relationships that determine the correct action.

Strong multimodal models perform better, especially on hard visual tasks. GPT-4V + SoM reaches 12.4% on hard-visual tasks compared with 8.0% for captioned GPT-4 and 4.8% for text-only GPT-4. The result indicates that difficult web tasks need both language reasoning and detailed visual perception.

SoM is valuable primarily when the underlying VLM can ground numbered marks accurately. It gives GPT-4V a clearer connection between visible controls and executable actions, especially on dense sites, but weaker VLMs gain little or nothing.

The best original system’s 16.37% success and later GPT-4o result of 19.78% remain drastically below humans’ 88.70%. The authors therefore characterize contemporary systems as research prototypes that are insufficient even for many simple tasks.

Several findings are counterintuitive:

- Exact image matching is not the main bottleneck for GPT-4V + SoM; its success is higher on exact-match tasks than elsewhere.
- GPT-4V + SoM performs better on tasks containing input images, presumably because these tasks become relatively tractable once the visual reference is understood.
- Agents can fail tasks labeled visually and action-wise easy.
- Longer action sequences do not consistently correspond to better success.
- Gemini-Pro appears comparatively capable on OCR but comparatively weak at handling interleaved image-text inputs.

The execution traces show that perception is only one part of the problem. Failures also arise from poor planning, insufficient exploration, inability to preserve earlier decisions, incorrect text-field manipulation, loops, redundant actions, and premature termination.

## 6. Contributions and Novelty

The paper makes the following principal contributions:

- It introduces **VisualWebArena**, a benchmark of **910 realistic, visually grounded web tasks**.
- It adds a new Classifieds environment with **65,955 real-world-derived, privacy-redacted listings**.
- It spans Shopping, Reddit, Classifieds, multi-site interactions, and occasional Wikipedia use.
- It requires visual grounding in every task, with **25.2%** also containing image inputs.
- It contributes execution-based visual reward functions for semantic text matching, exclusion constraints, visual question answering, and structural image matching.
- It introduces a systematic SoM-based web agent that labels interactable elements with bounding boxes and IDs.
- It benchmarks a broad range of text-only, caption-augmented, and multimodal agents under common conditions.
- It provides human performance, task-difficulty annotations, subset analyses, trajectory analyses, and qualitative failure studies.
- It shows quantitatively that direct multimodality and, for a sufficiently capable model, SoM grounding improve performance.
- It supplies a self-contained, deterministic sandbox intended for safely developing multimodal web agents.

## 7. Limitations and Caveats

- Even the strongest reported model achieves only **19.78%**, so the tested agents are far from reliable.
- The environments are self-hosted simulations based on real sites and content, not deployment on live commercial services.
- Human performance was measured on **230 of 910 tasks**, not the full benchmark.
- Some human evaluators helped create tasks, although the authors prevented them from evaluating their own tasks.
- Difficulty labels depend partly on estimated human action counts and subjective visual judgments.
- The baseline prompting is relatively simple; the study leaves more advanced prompting strategies unexplored.
- Main results use only three demonstrations, although the few-shot analysis shows sensitivity to the number of examples.
- GPT-4V was not used for the few-shot ablation because of cost.
- Binary rewards do not distinguish partially correct from completely wrong behavior. Even when the fuzzy evaluator can label an answer partially correct, it receives a reward of 0.
- Some evaluation relies on other learned models—GPT-4 Turbo for semantic text equivalence and BLIP-2-T5XL for VQA—so grading depends on their judgments.
- Caption-based agents inherit the lossiness of image-captioning models.
- SoM helps only models with sufficiently strong mark-grounding ability.
- Context and viewport truncation may omit relevant page content, especially for shorter-context models restricted to 640 tokens and a smaller viewport.
- Several open-source models are nearly at zero on medium or hard tasks, limiting the informativeness of the full benchmark for those systems.
- The benchmark contains **46 intentionally impossible tasks**, meaning an agent must distinguish impossibility from situations where more exploration is needed—a distinction current models often mishandle.
- The models are research prototypes and are explicitly not intended for real-world deployment, particularly in high-risk settings.

The paper also raises broader concerns:

- Autonomous agents may improve computer accessibility for people with disabilities or limited technical expertise.
- They could automate large amounts of routine computer work, creating economic and employment implications.
- Deployed agents could unintentionally disadvantage particular groups.
- Because agents can directly alter systems, they may cause greater harm than non-agentic language models if safeguards are inadequate.

## 8. Future Work or Open Questions

The authors identify several promising directions:

- Improve visual perception, OCR, reasoning, planning, and navigation.
- Develop better handling of multiple interleaved images and text.
- Fine-tune VLMs on web-interaction trajectories; the few-shot results suggest that additional examples can materially improve performance.
- Use more advanced prompting approaches than the chain-of-thought baselines studied here.
- Improve memory and tracking of prior states, decisions, and execution history to prevent loops, reversals, and repeated actions.
- Build agents that explore alternatives instead of giving up when an expected control or product is not immediately visible.
- Investigate continuous or partially graded reward scales rather than strictly binary evaluation.
- Study the apparent OCR strengths of Gemini-family models with stronger variants.
- Revisit image-input performance with stronger models and open-source VLMs.
- Determine why only strong models reliably benefit from SoM and how to improve visual mark grounding in other VLMs.
- Analyze and mitigate bias, unsafe behavior, and harmful real-world actions before deployment.
- Consider the social and employment consequences of large-scale task automation.
- Explore whether agents can eventually exceed humans on exhaustive searches and speed while retaining correctness.

## 9. High-Level Takeaway (Plain Language)

VisualWebArena tests whether AI agents can use websites the way people do: by looking at images and layouts, understanding instructions, clicking the right controls, and keeping track of a multi-step goal. Giving agents direct visual access—and labeling clickable objects with numbered marks—helps, but current systems remain highly unreliable. The strongest reported AI completed about one-fifth of the tasks, while people completed nearly nine-tenths. The work therefore provides both a demanding benchmark and clear evidence that better vision, reasoning, planning, persistence, and memory are all needed before autonomous web agents are ready for practical use.