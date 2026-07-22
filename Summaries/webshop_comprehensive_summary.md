# *WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents*

**Authors:** Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan  
**Affiliation:** Department of Computer Science, Princeton University  
**Published at:** NeurIPS 2022

## 1. Background and Context

Recent work in natural language processing and reinforcement learning has produced agents that can make sequences of decisions using language. Large pretrained models such as BERT and GPT-3 also perform well on static tasks such as classification, information extraction, and question answering. However, these two research directions leave an important gap:

- Existing interactive environments tend to contain limited or artificial language and are difficult to expand because collecting data or feedback requires substantial human effort.
- Conventional NLP benchmarks contain realistic language at scale, but they are usually static and do not require language to be grounded in actions, images, objects, or changing environments.

The authors argue that progress in grounded language understanding requires scalable environments with:

1. Rich language reflecting real-world use and collectable at scale.
2. Well-defined, automatically calculated feedback that supports interactive learning without continual human evaluation.

The World Wide Web is attractive for this purpose because it is large, realistic, semantic, interactive, dynamic, and multimodal. It also provides a natural deployment setting for agents that could reduce human effort in tasks such as purchasing products or booking appointments.

Previous web-agent benchmarks have important restrictions. Some reduce web interaction to one supervised classification decision or a few pages. Others focus only on following hyperlinks or depend on human feedback because they lack an automatic reward. Environments based on low-level mouse clicks and keystrokes are also difficult to scale and transfer.

WebShop addresses these limitations through a simulated e-commerce site built from real products. An agent receives a natural-language request and must search, examine products, select variations such as color or size, and purchase a matching item. Solving a task can require query reformulation, noisy-text interpretation, comparison of several products, backtracking, multiple searches, option selection, and long-term memory.

## 2. Research Goal and Objectives

The paper’s main goal is to create a large-scale, realistic, and automatically scored environment for developing grounded language agents capable of extended web interaction.

Its specific objectives are to:

- Construct a simulated shopping website using over one million real-world products and thousands of human-written instructions.
- Define a high-level, semantically meaningful action space that can transfer more easily to real websites than raw mouse and keyboard actions.
- Provide an automatically computable reward so agents can be trained without continuous human feedback.
- Train and compare rule-based, imitation-learning, reinforcement-learning, language-pretrained, and vision-language agents.
- Analyze why agents remain worse than people, using score breakdowns, trajectories, human demonstrations, model ablations, and an action-choice oracle.
- Test whether agents trained only in WebShop can transfer without fine-tuning to Amazon and eBay.

The central question is whether a simulated but realistic and scalable web environment can support the development of agents that meaningfully transfer to real-world websites.

## 3. Methods (Approach/Design)

### 3.1 WebShop environment

WebShop is a modular, OpenAI Gym-compatible e-commerce environment. Its website transitions are separated from task-specific components such as instructions and rewards, allowing other tasks or domains to be incorporated.

The environment is formulated as a partially observable Markov decision process containing:

- A state space of webpages.
- An action space.
- A deterministic state-transition function.
- A reward between 0 and 1.
- A space of natural-language instructions.
- An observation space.

There are four webpage states:

1. **Search page:** contains a search bar.
2. **Results page:** lists products returned by the search engine.
3. **Item page:** presents a product and its selectable options.
4. **Item-detail page:** provides descriptions or overview information.

Products are represented by:

- Aggregated text from the title, description, and overview.
- Price.
- A set of selectable buying options.
- Product images, potentially corresponding to particular options.
- Hidden attributes extracted from product text. Agents cannot see these annotations directly; they are used to calculate rewards.

### 3.2 Actions and transitions

The environment has two high-level action types:

- `search[query]`
- `choose[button text]`

Search is available only on the search page. All other interaction uses `choose`, which selects a semantic web button rather than a screen coordinate.

**Table 1 identifies the permitted transitions:**

- Search with a query: search page → results page.
- Choose “Back to search”: any applicable page → search page.
- Choose previous or next page: results page → another results page.
- Choose a product title: results page → item page.
- Choose a product option: item page → updated item page.
- Choose Description or Overview: item page → item-detail page.
- Choose Previous: item-detail page → item page.
- Choose Buy: item page → episode termination.

Search transitions use a deterministic search engine, and click-based transitions deterministically lead to the corresponding webpage.

### 3.3 Observation modes

WebShop supports two parallel representations:

- **HTML mode:** provides the webpage’s HTML and permits browser interaction. Human performance was collected in this mode.
- **Simple mode:** removes unnecessary HTML metadata and exposes a cleaner textual representation. All models were trained and evaluated in this mode.

Although agents could theoretically learn from raw webpage pixels, the authors consider the associated low-level interaction space less semantic. A translator can instead convert new HTML pages into the simple format, which supports transfer to real websites.

### 3.4 Instructions and automatic reward

Each instruction specifies:

- At least one desired product attribute.
- A set of requested buying options.
- A maximum permitted price.

Instructions are written from a particular target product. The requested attributes and options are subsets of that product’s annotations and available options, while the stated price limit is higher than the target product’s price.

The final reward combines four factors:

1. **Attribute match:** the fraction of requested attributes possessed by the purchased item.
2. **Option match:** the fraction of requested options correctly selected.
3. **Price match:** whether the product is within the stated budget.
4. **Product-type match:** a text-matching heuristic that penalizes products of an obviously wrong type, even if they share attributes or options.

The attribute, option, and price components are averaged and then multiplied by the type-match reward. The type check prevents misleading matches—for example, butter and plant-based meat could share properties such as “cruelty-free” and “non-GMO” without being the same product type.

The exact text-match formula is placed in the paper’s appendix and is not included in the supplied main text.

Two evaluation measures are used:

- **Task Score:** 100 times the average reward.
- **Success Rate:** percentage of episodes receiving the maximum reward of 1.

A successful purchase need not be the exact source product used to write the instruction. Any item satisfying all requirements can earn full reward.

### 3.5 Figure 1: example interaction and notation

Figure 1 illustrates a complete trajectory:

1. The shopper searches for a “small portable folding desk” that is assembled, has a khaki wood finish, and costs under $140.
2. The results page returns products.
3. The shopper selects a product and chooses the khaki option.
4. The shopper visits Description and Overview detail pages and returns to the item page.
5. The shopper clicks Buy and receives reward 1.0.

The figure contrasts the browser-oriented HTML interface with the stripped-down simple mode. In simple mode, blue text marks clickable actions and bold text marks the selected action. It also shows the formal product representation: instruction, product text, price, options, images, and hidden attributes.

### 3.6 Dataset construction

The authors used ScraperAPI to collect **1,181,436 Amazon products** from five categories:

- Fashion
- Makeup
- Electronics
- Furniture
- Food

The scraping process used **113 subcategory names** as queries. Product title and item-detail text averaged **262.9 words**, and the vocabulary contained **224,041 words occurring more than 10 times**. Products collectively offered **842,849 unique options**.

The deterministic search engine was implemented with Pyserini and BM25. Its index concatenated each product’s title, description, overview, and customization options.

### 3.7 Attribute mining

Hidden product attributes were obtained by:

1. Computing TF-IDF scores for all bigrams in titles and descriptions within each category.
2. Reviewing the 200 highest-ranked bigrams per category.
3. Removing phrases judged noisy or not understandable to people.
4. Assigning the retained phrases to products.

This produced a pool of **670 attributes**.

### 3.8 Human-written instructions and demonstrations

Amazon Mechanical Turk workers saw a sampled product’s title, category, attributes, and buying options. They then wrote a command instructing an automated shopper to find it. Workers were told not to copy an entire title but to describe the product faithfully.

The resulting dataset contains:

- **12,087 instructions**
- A vocabulary of **9,036 words**
- An average instruction length of **15.9 words**

For demonstrations, the authors recruited and trained **13 workers** and designated the top **7** as experts after qualification and performance screening.

The 12,087 instructions were divided into:

- **10,587 training**
- **1,000 development**
- **500 test**

The authors collected:

- **1,012 training demonstrations**
- **54 development demonstrations** for hyperparameter tuning and checkpoint selection
- Human trajectories for all **500 test instructions**

### 3.9 Figure 2: difficulty of direct search

Figure 2 shows where the target product ranks when the complete instruction is used directly as the search query:

- **32.2%** appear on page 1, ranks 1–10.
- **11.7%** appear on pages 2–5, ranks 11–50.
- **56.1%** are not found in the first 50 results.

Thus, simply submitting the original instruction often fails to retrieve the intended product, motivating learned search generation and query reformulation.

### 3.10 Rule baseline

The rule baseline:

1. Searches the exact instruction.
2. Selects the first result.
3. Buys it without choosing any options.

It benefits from the lexical search engine and can earn partial attribute credit, but it cannot reliably interpret option language, reformulate queries, compare products, or explore strategically.

### 3.11 Imitation learning

The imitation-learning system separates search generation from action choice.

#### Search generation

Search is treated as sequence-to-sequence generation from the instruction alone. The model receives no history of previous searches or visited products.

A BART model is fine-tuned using:

- **1,421 instruction–search-query pairs**
- Extracted from the **1,012 training demonstrations**

At runtime, BART generates its five highest-scoring queries by beam search, and the system randomly selects one to encourage diversity.

#### Choice model

The choice model predicts a probability distribution over all currently available click actions and is trained to maximize the probability of the button selected by a human.

Training uses:

- **9,558 observation/action samples**
- A **12-layer pretrained BERT** to encode the observation and each candidate action
- Cross-attention between observation and action representations
- Mean pooling
- A learned projection producing a scalar action score
- A softmax over all available action scores

On non-search pages, the agent samples an action from this distribution. Sampling is used because always taking the highest-probability action can restrict exploration or make an agent repeatedly bounce between pages.

#### Image handling

A pretrained ResNet-50 converts product images into **512-dimensional vectors**. A learned linear layer expands these to **768 dimensions**, after which they are concatenated with BERT’s textual observation representation.

#### Figure 3: multimodal choice architecture

Figure 3 depicts this action-scoring pipeline. The product image passes through ResNet, while the instruction and webpage text pass through a BERT-initialized Transformer. Their representations are concatenated. Candidate action text—such as `choose[khaki]`—is encoded by a weight-sharing Transformer. An attention-fusion layer combines each action with the multimodal observation, and mean pooling plus an MLP produces the logit \(S(o,a)\) used to rank that action.

### 3.12 Reinforcement learning

The IL choice model is further trained through online reinforcement learning, producing the **IL+RL** agent.

BART is frozen because directly optimizing language generation with RL could cause language drift and reduce performance. It generates its ten best search queries, which become a restricted action set from which the choice policy learns.

The RL method uses:

- Policy-gradient optimization with return-to-go.
- A learned value function as a baseline.
- Shared BERT weights between the policy and value estimator.
- Squared-error loss for value prediction.
- Entropy regularization to discourage premature convergence.

The total RL objective combines policy-gradient, value, and entropy terms.

## 4. Results and Findings

### 4.1 Main WebShop performance

Figure 4 reports averages over three trials.

| Model | Task Score | Success Rate |
|---|---:|---:|
| Rule | 45.6 | 9.6% |
| IL without pretrained choice model | 45.8 | 10.6% |
| IL without pretrained search generator | 56.0 | 26.3% |
| IL | 59.9 | 29.1% |
| RL | 52.5 | 11.2% |
| RL with RNN encoders | 55.2 | 17.6% |
| IL+RL | **62.4** | 28.7% |
| Average human | 75.5 | 50.0% |
| Expert human | **82.1** | **59.6%** |

The rule baseline’s **45.6 score and 9.6% success rate** confirm that lexical retrieval alone is insufficient, particularly because it does not select options or inspect alternatives.

IL substantially improves both measures. Adding RL raises score from **59.9 to 62.4**, but slightly lowers success from **29.1% to 28.7%**. Consequently:

- **IL+RL has the highest model score.**
- **Plain IL has the highest model success rate.**

The abstract rounds the best reported task success to **29%** and compares it with **9.6%** for the rule system and **59%** for experts.

Even the best learned results remain far below people. The model success rate of approximately 29% is less than half the expert rate of 59.6% and about 60% of the 50% average-human rate.

### 4.2 IL ablations

Removing language pretraining from the choice model is highly damaging:

- Score falls from **59.9 to 45.8**.
- Success falls from **29.1% to 10.6%**, a reduction of nearly two-thirds.

This demonstrates that pretrained language representations are crucial for interpreting webpage text, instructions, and action labels.

Replacing BART search generation with the rule of searching the full instruction gives:

- Score **56.0**
- Success **26.3%**

Both are about three points below full IL, showing that learned search generation and expanded search exploration help, though pretrained action choice matters more.

Adding one previous observation and the last five actions as history slightly reduces score from **59.9 to 57.3**. Simple history concatenation therefore does not provide effective memory; more advanced memory mechanisms are needed.

### 4.3 RL ablations

Training RL directly from pretrained BERT, without an imitation-learning warm start, performs worse than the rule baseline in success rate:

- RL score: **52.5**
- RL success: **11.2%**

This suggests that demonstrations provide essential task priors, potentially because WebShop differs substantially from conventional language-pretraining tasks.

Replacing Transformer text encoders with RNNs yields:

- Score **55.2**
- Success **17.6%**

Its success rate is more than 10 percentage points below IL+RL and has much higher variance. The authors suggest stronger RL architectures might improve and stabilize training if initialized with better language and task knowledge.

### 4.4 Score-component and trajectory analysis

Table 2 decomposes reward and records navigation behavior.

| Model | Overall | Attributes | Options | Type | Price |
|---|---:|---:|---:|---:|---:|
| Rule | 45.6 | 66.6 | 0.0 | 80.5 | 86.0 |
| IL | 59.9 | 69.3 | 45.2 | 86.4 | 84.0 |
| IL+RL | 62.4 | 74.0 | 38.9 | 89.7 | 88.7 |
| Human expert | 82.1 | 81.8 | 73.9 | 94.4 | 97.7 |

Experts outperform all agents on every subscore. The largest model–expert weakness is option selection: expert option score is **73.9**, compared with **45.2** for IL and **38.9** for IL+RL. The paper describes this as a gap of approximately 28 points relative to IL.

Trajectory statistics are reported as average, with maximum and minimum in parentheses:

| Model | States visited | Items checked | Searches |
|---|---:|---:|---:|
| Rule | 3.0 (3/3) | 1.0 (1/1) | 1.0 (1/1) |
| IL | 9.4 (90/3) | 1.6 (11/1) | 1.3 (17/1) |
| IL+RL | 4.5 (5/1) | 1.0 (1/1) | 1.0 (1/1) |
| Human expert | 11.3 (114/4) | 1.9 (16/1) | 1.4 (16/1) |

The text later describes IL+RL’s trajectory length as dropping to **4.8**, whereas Table 2 gives **4.5**. This is an internal inconsistency in the supplied paper.

Humans follow longer and more variable trajectories, inspect more products, and search more often. Their behavior is more flexible than that of the agents.

### 4.5 Qualitative trajectory examples

**Table 3, instruction 1:** The user requests white, easy-to-install blackout shades measuring 66 by 66 inches.

- The human initially searches with the full dimensional wording, checks a result, returns to search, reformulates the query as “66 x 66 blackout shades,” selects a suitable item, chooses the `66"w x 66"h` and white blackout options, and buys it.
- The human earns **1.0 reward in 8 actions**.
- IL+RL issues a slightly incorrect query containing “65 inches,” selects one item, and immediately buys it.
- IL+RL earns **0.2 reward in 3 actions**.

The human removes words such as “inches,” “width,” “height,” and “white” because product pages often abbreviate them with symbols such as `"`, `w`, and `h`. This illustrates grounded query reformulation.

**Table 3, instruction 2:** The user requests a hand-painted gingko-light pillow cover in size 20 by 20 inches.

- The human searches, examines descriptions and overviews across products, later returns to the initially explored product, selects the correct size and design, and purchases it.
- The trajectory earns **1.0 reward in 17 actions**.
- Some human actions are omitted in the table for space.
- IL+RL searches, chooses a different product, and buys immediately.
- It earns **0.25 reward in 3 actions**.

This example shows the value of exploration and long-term memory. The model also struggles with semantically matching noisy or paraphrased option names to instruction wording.

### 4.6 Effect of RL after IL

RL makes the IL policy greedier and less exploratory. Compared with IL:

- Attributes improve from **69.3 to 74.0**.
- Type improves from **86.4 to 89.7**.
- Price improves from **84.0 to 88.7**.
- Options decline from **45.2 to 38.9**.
- The average trajectory becomes much shorter.
- The agent visits fewer items and conducts fewer searches.

This explains how IL+RL can obtain a higher average score while having a slightly lower exact success rate. The authors conclude that RL needs a better exploration–exploitation balance, potentially through intrinsic exploration bonuses.

### 4.7 Choice-oracle experiment

To separate search quality from action-choice quality, the authors construct a Choice oracle with access to hidden product attributes, options, and the reward function. For a supplied query, it exhaustively checks all returned products and options and purchases the combination with the highest reward.

This oracle requires more than 100 steps per episode, compared with average trajectories of **4.5 states for IL+RL** and **11.3 for experts**.

On 500 test instructions, the authors test four query sources:

| Query source | Score | Success Rate |
|---|---:|---:|
| Full instruction | 79.7 | 52.6% |
| Top IL/BART query | 83.0 | 57.6% |
| Expert’s first query | 82.1 | 57.9% |
| Expert’s last query | 84.4 | 61.0% |

The oracle raises success from:

- **9.6% to 52.6%** when starting from the rule baseline’s full-instruction query.
- **29.1% to 57.6%** when using the learned BART query.

This confirms that choosing products and options is a major agent bottleneck. Oracle choice improves human performance much less because humans already choose effectively. In **74.8%** of human trajectories, the first and last query are identical because only one query is issued.

The paper notes that an analogous search oracle is harder to design because the space of possible text queries is infinite. Searching the hidden target product name would also make the choice task artificially easy because that item would usually rank first.

### 4.8 Zero-shot transfer to Amazon and eBay

The authors sampled **100 test instructions** and deployed the rule, IL, and IL+RL agents on Amazon and eBay with no fine-tuning. Each episode was manually scored using the same reward definition.

#### Amazon

| System | Score / Success | Attributes | Options | Type | Price |
|---|---:|---:|---:|---:|---:|
| Rule | 45.8 / 19% | 45.6 | 38.0 | 66.2 | 90.0 |
| IL | 61.5 / 27% | 60.7 | 53.7 | 85.6 | 96.0 |
| IL+RL | **65.9 / 25%** | 71.6 | 47.0 | 87.8 | 100.0 |
| Human | **88.2 / 65%** | 86.2 | 76.3 | 99.0 | 100.0 |

IL+RL improves substantially over the rule baseline in score, **65.9 versus 45.8**, and in success, **25% versus 19%**. IL has a lower score than IL+RL but a slightly higher success rate, **27%**.

#### eBay

| System | Score / Success | Attributes | Options | Type | Price |
|---|---:|---:|---:|---:|---:|
| Rule | 31.7 / 7% | 62.3 | 25.9 | 49.0 | 67.0 |
| IL | 58.2 / 21% | 60.2 | 52.3 | 85.1 | 96.9 |
| IL+RL | **62.3 / 21%** | 69.1 | 39.5 | 91.7 | 97.0 |
| Human | **79.7 / 40%** | 80.3 | 70.1 | 99.5 | 100.0 |

IL+RL again greatly exceeds the rule system: **62.3 versus 31.7 score** and **21% versus 7% success**.

The prose reports the Amazon human score as **88.0**, while Table 5 gives **88.2**; the eBay score is consistently **79.7**. Human success is **65% on Amazon** and **40% on eBay**.

Humans remain much more accurate but are slower. Their interactions average **815 seconds per episode**, whereas IL and IL+RL take **under 8 seconds per Amazon episode**.

Only two minor coding additions were reportedly needed to transfer WebShop agents to these sites. Performance remains broadly similar to simulated WebShop despite changes in products and search engines. The rule baseline performs unusually well on Amazon relative to WebShop, which the authors attribute to Amazon’s stronger search engine.

## 5. Analysis and Interpretation

The experiments answer the paper’s main question positively but only partially. WebShop supports learning useful policies that transfer to real shopping websites, yet present agents remain far from human-level grounded web interaction.

Several findings explain the gap:

- **Language pretraining is essential.** Training the choice Transformer from scratch reduces success from 29.1% to 10.6%.
- **Action choice is the clearest bottleneck.** Agents particularly struggle with product variations and noisy option phrasing. The Choice oracle more than quintuples the rule baseline’s success and nearly doubles learned-agent success.
- **Search generation still matters.** More than half of targets do not appear in the first 50 results when the full instruction is searched directly. Learned BART queries improve both score and success, and human trajectories show adaptive reformulation using website-specific notation.
- **Humans explore strategically.** They search more, inspect more items, revisit previous products, and use longer and more variable trajectories.
- **Current agents lack effective memory.** They have difficulty returning to a previously seen good product. Naively adding a short observation/action history lowers performance rather than helping.
- **RL can overemphasize exploitation.** RL improves partial reward by quickly choosing products with better attributes, type, and price, but reduces exploration and correct option selection. This raises average score without increasing exact completion.
- **Imitation learning is a necessary foundation for RL.** Direct RL does not reliably acquire the task from pretrained language weights alone.
- **Real-world transfer is feasible.** Models trained in simulation preserve useful behavior on Amazon and eBay without retraining and consistently outperform the simple rule system, despite product and search-engine shifts.

The authors describe WebShop as a joint testbed for problems usually studied separately: query generation, reformulation, robust language understanding, semantic action selection, strategic exploration, and long-term memory.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- **A large-scale interactive benchmark:** WebShop contains 1,181,436 real products and 12,087 human-written shopping instructions.
- **Realistic multimodal grounding:** Agents must connect instructions to webpage text, product images, prices, attributes, and selectable variations.
- **Long-horizon semantic interaction:** Tasks involve search, product comparison, detail inspection, option selection, backtracking, and purchase across multiple webpage types.
- **A scalable high-level action space:** Agents generate text searches and select semantic buttons instead of operating through raw mouse coordinates.
- **Automatic graded evaluation:** A reward function scores product type, attributes, options, and price without requiring a human evaluator for every episode.
- **Two complementary interfaces:** HTML mode supports people and browser interaction, while simple mode supports model training and transfer from new webpages.
- **Human demonstration data:** More than 1,600 demonstrations are used for task verification, training, development, and evaluation.
- **A multimodal learning architecture:** BART generates searches; BERT scores textual actions contextually; ResNet features incorporate product images; IL and RL are combined.
- **Detailed diagnostic analysis:** Ablations, reward decomposition, trajectory comparisons, qualitative examples, and a Choice oracle identify why models fail.
- **Evidence of zero-shot sim-to-real transfer:** WebShop-trained models operate on Amazon and eBay without fine-tuning and outperform direct-search heuristics.

## 7. Limitations and Caveats

- **Large human–agent gap:** The strongest model success is about 29%, compared with 59.6% for experts.
- **Weak option selection:** This is the largest score-component gap and becomes worse after RL fine-tuning.
- **Limited exploration:** IL+RL generally checks one item and performs one search, while humans follow longer, more flexible trajectories.
- **No effective long-term memory:** Agents struggle to revisit promising products, and the tested short-history mechanism lowers performance.
- **Search generation ignores interaction history:** BART generates a query solely from the instruction, without past searches or visited items.
- **Direct RL is ineffective:** RL without imitation-learning initialization performs poorly, indicating difficult exploration and substantial domain shift.
- **RL may become too greedy:** It improves partial reward but shortens trajectories and slightly decreases exact success.
- **IID evaluation:** The main train, development, and test sets are independently and identically distributed. Generalization across product categories or larger distribution shifts was not evaluated in the reported WebShop experiments.
- **Reward relies on mined annotations and heuristics:** Hidden attributes come from TF-IDF-ranked bigrams followed by manual filtering, while product type uses a heuristic text-match function.
- **The Choice oracle is not a practical agent:** It uses hidden information and takes more than 100 steps per episode; it is intended only to diagnose the choice bottleneck.
- **Human data caveat:** Some crowdsourced workers lacked the patience and consistency required for the task. The authors therefore distinguish the top seven experts from average workers, though a large expert–model gap remains.
- **Transfer evaluation is limited in size:** The Amazon and eBay experiment uses 100 instructions and manually scored episodes.
- **Real-site agents remain less capable than humans:** Transfer works, but success reaches only 25–27% on Amazon and 21% on eBay, compared with 65% and 40% for humans.
- **Reported numerical inconsistencies:** Table 2 lists IL+RL’s average states as 4.5, while the prose says 4.8. Table 5 gives Amazon human score as 88.2, while the prose reports 88.0.

No statistical significance tests, confidence intervals, or p-values are provided in the supplied text. Terms such as “significant” therefore describe the authors’ qualitative characterization rather than a reported hypothesis test.

## 8. Future Work or Open Questions

The authors identify several directions:

- Develop more robust search generation and query reformulation that adapt to webpage conventions and prior search results.
- Improve semantic matching between instructions and noisy or paraphrased product-option labels.
- Add explicit working or episodic memory so agents can compare products and return to earlier promising items.
- Improve strategic and action exploration over long horizons and large action spaces.
- Use intrinsic bonuses or related methods to balance exploration and exploitation during RL.
- Develop better techniques for using interaction history, since simple history concatenation was ineffective.
- Explore stronger RL architectures initialized with richer language and task priors.
- Pretrain with multimodal data, web hypertext, or mappings between web instructions and actions.
- Combine capabilities across disciplines—for example, memory with exploration, or exploration with query reformulation.
- Evaluate harder generalization settings, such as train/test splits by product category.
- Extend WebShop’s modular framework to new web tasks and domains.
- Continue improving practical grounded agents that can operate autonomously on real websites while reducing human effort.

## 9. High-Level Takeaway (Plain Language)

WebShop is a simulated online store designed to teach and test AI systems that must understand a person’s request, search for products, compare choices, select details such as size or color, and complete a purchase. Learning from human demonstrations and pretrained language models makes these agents much better than a simple “search and buy the first result” rule, and their skills transfer to Amazon and eBay without retraining. However, they still succeed only about 29% of the time in WebShop, versus roughly 60% for human experts. Their biggest problems are choosing the correct options, reformulating searches, exploring patiently, and remembering products they saw earlier.