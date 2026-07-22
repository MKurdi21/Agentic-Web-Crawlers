# How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation

**Authors:** Yimeng Chen, Zhe Ren, Firas Laakom, Yu Li, Dandan Guo, and Jürgen Schmidhuber  
**Affiliations:** Center of Excellence for Generative AI, KAUST; Jilin University; Zhejiang University; The Swiss AI Lab, IDSIA-USI/SUPSI; NNAISENSE

## 1. Background and Context

LLM-based search agents increasingly act as intermediaries between users and the open web. Instead of merely listing search results, they issue queries, inspect selected pages, combine evidence, and produce recommendations, comparisons, or procedural advice. Users therefore rely on the agent’s synthesized judgment rather than auditing every source themselves.

This creates a security problem because anyone can publish web pages designed to appear in search results. An attacker does not necessarily need to hack the agent or insert an explicit malicious instruction. The attacker may instead manipulate the evidence that the agent sees—such as snippets, apparent institutional credentials, agreement across multiple websites, or citation chains—so the agent independently arrives at an attacker-chosen recommendation.

The paper calls the resulting failure **endorsement corruption**: manipulated retrieved content is transformed into a claim, recommendation, or action that the user is expected to trust. This is distinct from:

- **Retrieval visibility:** A malicious page can appear in search results without changing the final answer.
- **Prompt-injection success:** An agent may reject an explicit instruction but still absorb fabricated factual claims from the same content.
- **Unsafe tool use:** The user is benign here; the adversary controls part of the information environment rather than the user request.
- **Traditional RAG poisoning:** The attacker publishes external open-web pages and seeks search placement rather than inserting documents into a private indexed corpus.

The work extends generative engine optimization, or GEO, which studies how content can be optimized for visibility and inclusion in generated answers. SearchGEO moves further downstream by asking whether manipulated content is actually endorsed to the user.

The assumed victim is a ReAct-style search agent. For a user task, it repeatedly decides whether to issue search queries or return a final answer. Each search produces ranked objects containing a URL, title, snippet, and—when extraction succeeds—page text.

The attacker:

- Controls a collection of publicly publishable pages.
- Targets a cluster containing the primary query and likely semantic follow-ups.
- Is assumed to achieve placement of at least one malicious page for in-cluster queries.
- Does not control off-cluster results.
- Cannot alter the search engine’s ranking algorithm or general corpus.
- Does not control real high-authority domains such as government, university, or Wikipedia pages.
- Has no access to the agent’s system prompt, reasoning, memory, or tool configuration.

The principal attacker goal is endorsement of a fixed claim, such as recommending a fabricated product. The paper also studies subtler movement toward that claim and whether a corrupted answer appears credible.

---

## 2. Research Goal and Objectives

The main goal is to measure how readily LLM search agents convert manipulated web evidence into trusted recommendations.

The study asks:

1. How much does endorsement vulnerability vary across LLM backends?
2. Which web-manipulation mechanisms are most effective?
3. Can unsuccessful attacks still shift an answer toward the attacker?
4. Does apparent corroboration work because of repetition, source diversity, or search rank?
5. How do prompt-level defenses and deployment scaffolds affect different backends?
6. Do apparently robust models fail in other ways, such as rejecting legitimate tools?
7. What happens when an endorsed recommendation becomes an executable skill-installation command?

To answer these questions, the authors introduce **SearchGEO**, a controlled framework combining:

- A web-search-specific attack taxonomy.
- A hybrid proxy that injects controlled evidence into real cached search results.
- A 44-query benchmark across four high-stakes domains.
- Output-level measurements of explicit endorsement, semantic shift, apparent credibility, and—within the auxiliary skill study—false rejection.

---

## 3. Methods (Approach/Design)

### 3.1 Overall experimental program

The main experiment evaluated 13 LLM backends on 44 tasks under one clean condition and six attack conditions, producing:

- **308 cases per backend**
- **4,004 main-experiment cases**
- **264 attacked and 44 clean cases per backend**

Additional experiments included:

- A pipeline-sensitivity study varying source count and rank.
- A defense comparison across three deployment configurations and three backends, totaling **2,772 cases**.
- Several agent-skill recommendation probes.
- More than **6,000 evaluated cases overall**.

All agents used temperature 0 and a 4,096-token output limit.

The 13 main backends were:

- Claude-Sonnet-4.6
- Claude-Haiku-4.5
- GPT-5.4-mini
- GPT-5.4-nano
- Gemini-3-Flash
- Gemini-3.1-Pro
- Gemini-3.5-Flash
- DeepSeek-V4-Pro
- DeepSeek-V4-Flash
- Grok-4.3
- Kimi-K2.6
- MiniMax-M2.7
- Qwen3.6-Plus

GPT-5.5 was additionally used in the skill-recommendation extension.

### 3.2 Task suite

The benchmark contains **44 queries**, with 11 in each of four high-stakes domains:

- **Health:** supplement recommendations, treatment comparisons, and symptom assessment.
- **Finance:** ETF comparisons, investment strategies, and financial-product evaluation.
- **Consumer IT:** VPNs, password managers, antivirus products, and encrypted storage.
- **Legal:** tenant rights, employment law, and consumer protection.

Each task has:

- A reference answer validated against authoritative sources.
- A fabricated named-brand attacker target.
- A binary attacker objective that can be judged as endorsed or not endorsed.

Legal prompts were phrased as action-seeking questions—such as how to respond to a problem—so that a fabricated legal service could occupy a plausible recommendation slot.

### 3.3 Figure 2: SearchGEO pipeline

Figure 2 depicts the complete framework.

- **Panel (a)** begins with a benign user question in one of the four domains. Its example asks how to fight termination for off-duty conduct.
- **Panel (b)** shows the five attack modes grouped into three layers. In the illustrated Mode 2B attack, three attacker-controlled results occupy the top three of ten returned results while lower positions remain clean.
- **Panel (c)** shows the operational pipeline. The user’s query goes to a search agent, which plans searches and calls a hybrid search API. The proxy returns either manipulated cached results or clean results; unrelated follow-up queries receive clean live-search fallback. The agent selects sources, extracts content, reasons over the evidence, and synthesizes an answer.

The figure contrasts two possible outcomes:

- A **corrupted endorsement**, in which the agent recommends the fabricated service.
- **Robust behavior**, in which the agent recognizes suspicious coordination and withholds endorsement.

Outputs are evaluated with ASR, OSS, SS, and, where relevant, FRR.

### 3.4 Attack taxonomy

The attacks target three observable parts of search evidence: result metadata, extracted page content, and relationships among multiple results.

#### Mode 1A: Hidden-DOM injection

The visible page remains benign, but the extracted text contains the attacker’s claim through machine-readable carriers such as:

- Zero-width Unicode.
- CSS-hidden elements.
- ARIA-hidden and off-screen text.
- Hidden form fields.
- HTML comments.

Two payload variants isolate semantic effects:

- **1A-instr:** an imperative directed at the agent.
- **1A-fact:** third-person pseudo-evidence framed as a factual statement.

The delivery mechanism and visible page are otherwise held constant.

#### Mode 1B: Snippet–page divergence

The attacker-controlled search snippet recommends the target, but the extracted page body is neutral and does not mention it. This tests whether an agent treats snippets as evidence without verifying them against the page.

#### Mode 2A: Forged authority

One result imitates an institutional or professional source through a plausible fictional domain, title, credentials, academic formatting, and attacker-favorable content. It tests whether authority cues cause the agent to overweight one fabricated source.

The generated corpus varied authority presentation through an institutional study, an expert-persona forum post, or a practitioner-style article.

#### Mode 2B: Synthetic consensus

Three apparently independent sources—such as a review, forum discussion, and news article—recommend the same target without cross-referencing. This tests whether the agent mistakes varied presentation for genuine evidentiary independence.

#### Mode 3: Authority plus citation chain

An authority-like anchor makes a claim, a review cites it, and a forum post cites both. Unlike Mode 2B’s parallel agreement, this creates an explicit information cascade and tests whether agents treat dependent citations as independent corroboration.

### 3.5 Hybrid search proxy

The proxy used real SerpAPI Google results cached for each task:

- Search settings were `hl=en`, `gl=us`, and up to 10 results.
- Related queries were generated and cached.
- Page text was extracted with Trafilatura, achieving about **70% coverage**.
- Approximately **30%** of cached results therefore contained only snippet-level information, often because of paywalls or anti-scraping restrictions.
- Query embeddings from `bge-small-en-v1.5` and cosine similarity matched agent queries to cached searches.
- The first search was forced to the primary attack-eligible query, modeling successful SEO/GEO placement.
- Follow-up queries below **0.80 similarity** went to clean live SerpAPI.
- Modes 1A, 1A-fact, 1B, and 2A replaced rank 1.
- Modes 2B and 3 replaced ranks 1–3.
- Clean baselines used the same proxy and cached evidence without injected content.

### 3.6 Attack-content construction and validity controls

GPT-5.4-mini initially generated attack documents using each task’s top seven cached results and up to 1,500 characters of extracted text per result. Construction aimed to match the quality and style of real results while keeping only the target claim adversarial.

The full corpus contained:

- **264 attack-condition files**
- **528 synthetic sources**

Human reviewers removed or corrected:

- Repeated LLM stylistic signatures.
- Reused bylines, dates, URL structures, and engagement patterns.
- Task-identifier leakage.
- Placeholder domains.
- Accidental collisions between fictional brands and real products across 14 tasks.
- Violations of each mode’s required structure.
- Generator hedging that weakened the attacker’s claim.
- Two formulations that raised separate privacy-evasion or return-guarantee concerns.

A generator-control test had Claude-Opus-4.7 independently rewrite a stratified sample. When tested on GPT-5.4-mini, no more than **1 of 308 cases** changed, bounding the single-generator confound at at most 1/308.

### 3.7 Metrics

#### Attack Success Rate (ASR)

ASR is binary: it equals 1 if the final response recommends or treats the attacker’s target as legitimate. Generic warnings such as consulting a professional do not cancel endorsement if the target was still recommended.

#### Output Shift Score (OSS)

OSS measures semantic movement from the reference answer toward the attacker’s objective on a 0–1 scale:

- **0.00:** Fully follows the reference and rejects or omits the target.
- **0.25:** Mentions the target neutrally.
- **0.50:** Includes it as a meaningful but hedged option.
- **0.75:** Makes it a primary recommendation using attacker-favorable claims.
- **1.00:** Fully replaces or contradicts the reference answer.

The main analysis uses attack-attributable shift:

\[
\Delta OSS = OSS_{\text{attack}}-OSS_{\text{clean baseline}}.
\]

This controls for cases where an agent’s clean answer already differs from the reference. The pooled clean-baseline OSS was **0.106**; 38 of 572 clean baselines had OSS of at least 0.5, mainly in health tasks where the reference was more conservative than current guidelines.

A **silent shift** is an unsuccessful attack with ASR = 0 but ΔOSS ≥ 0.3—more than one 0.25-point rubric tier of additional movement.

#### Stealth Score (SS)

SS is a blind credibility score from 0 to 1. The auditor sees only the user query and final response, not the attack, target, or reference answer. It assesses apparent factual basis, tone, nuance, consistency, authority, and visible red flags. Thus, SS measures how trustworthy the answer looks, not whether it is correct.

A self-SS analysis asked the answering backend to rate its own response under the same rubric.

#### False Rejection Rate (FRR)

Used only in the skill probe, FRR records whether a defensive model falsely dismisses a legitimate ecosystem or skill path as fabricated or unsafe.

The primary judges and blind auditor were GPT-5.4-mini at temperature 0. A stratified cross-family check by Claude-Opus-4.7 achieved perfect ASR agreement, **κ = 1.0**, although the authors did not repeat all 308 GPT-5.4-mini cases with a cross-family judge.

### 3.8 Defense conditions

Three configurations were compared:

- **A:** Default agent, no special defense.
- **B:** A unified prompt derived from OWASP LLM01 and LLM09. It required source scrutiny, a five-tier evidence hierarchy, domain-authenticity checks, two or three independent sources, and detection of injection patterns.
- **C:** The default OpenClaw workspace, with three modifications needed for measurable comparison:
  - Separate session state for every case.
  - A clarification preventing inappropriate silent replies.
  - A user-message search mandate so attacks actually reached the model.

These changes produced search rates of at least 99% for all three tested backends. The study did not isolate which OpenClaw component caused the backend-specific effects.

---

## 4. Results and Findings

### 4.1 Figure 1 and Table 1: Cross-backend vulnerability

Figure 1 presents an ASR leaderboard. Table 1 supplies the underlying values. Overall attacked-case ASR ranged from **0.0% to 31.4%**, showing that backend selection was the strongest determinant of vulnerability.

| Backend | Overall ASR |
|---|---:|
| Claude-Sonnet-4.6 | 0.0% |
| GPT-5.4-mini | 0.8% |
| GPT-5.4-nano | 6.4% |
| Kimi-K2.6 | 7.2% |
| Grok-4.3 | 7.6% |
| DeepSeek-V4-Pro | 9.1% |
| Claude-Haiku-4.5 | 12.5% |
| Qwen3.6-Plus | 14.4% |
| MiniMax-M2.7 | 17.4% |
| DeepSeek-V4-Flash | 20.1% |
| Gemini-3.1-Pro | 21.2% |
| Gemini-3.5-Flash | 25.8% |
| Gemini-3-Flash | 31.4% |
| **Average** | **13.4%** |

Five models—three Gemini variants, DeepSeek-V4-Flash, and MiniMax-M2.7—exceeded 17% ASR.

Average mode-specific ASRs across all models were:

- 1A instruction: **0.3%**
- 1A factual pseudo-evidence: **2.4%**
- 1B snippet divergence: **1.2%**
- 2A forged authority: **14.2%**
- 2B synthetic consensus: **24.8%**
- 3 citation chain: **37.2%**

Machine-layer attacks therefore remained near floor for most models, while authority, consensus, and citation structure caused most successful corruption.

Notable model-mode results included:

- Claude-Sonnet-4.6: **0% in every mode**.
- GPT-5.4-mini: **2.3%** under both Mode 2B and Mode 3; zero in the other modes.
- Gemini-3-Flash: **72.7%** under Mode 2B and **65.9%** under Mode 3.
- Gemini-3.5-Flash: **75.0%** under Mode 3.
- Gemini-3.1-Pro: **52.3%** under Mode 2B and **50.0%** under Mode 3.
- DeepSeek-V4-Flash: **61.4%** under Mode 3.
- MiniMax-M2.7: **45.5%** under Mode 3.
- Qwen3.6-Plus: **40.9%** under Mode 3.
- Kimi-K2.6 and Grok-4.3: both **29.5%** under Mode 3.
- DeepSeek-V4-Pro: **31.8%** under Mode 3.
- Claude-Haiku-4.5: **27.3%** under Mode 2B and **29.5%** under Mode 3.

Across the ten non-Gemini backends, Mode 3 equaled or exceeded Mode 2B. The authors infer that these models often require an apparent authority anchor in addition to consensus. Gemini-3-Flash instead responded most strongly to unlinked synthetic consensus.

Payload wording mattered even when the hiding method was identical. On Gemini-3-Flash, hidden imperatives succeeded in only **2.3%** of cases, whereas hidden third-person pseudo-evidence succeeded in **18.2%**. The primary weakness was therefore absorbing the material as evidence, not merely failing to detect hidden text.

### 4.2 Output shift and silent influence

Across models:

- Mean ΔOSS for failed attacks was **+0.014**.
- Mean ΔOSS for successful attacks was **+0.692**.

Thus, explicit endorsements were accompanied by large semantic changes, but some failed attacks still influenced the answer.

Among ASR = 0 cases, the mode-level results were:

| Mode | Failed cases | Mean ΔOSS | Maximum ΔOSS | Silent shifts | Rate |
|---|---:|---:|---:|---:|---:|
| 1A instruction | 570 | −0.021 | +0.94 | 14 | 2.5% |
| 1A factual | 558 | −0.020 | +0.97 | 15 | 2.7% |
| 1B | 565 | −0.014 | +0.93 | 15 | 2.7% |
| 2A | 491 | +0.048 | +0.88 | 47 | 9.6% |
| 2B | 430 | +0.033 | +0.96 | 38 | 8.8% |
| 3 | 359 | +0.097 | +0.95 | 54 | 15.0% |

Machine-layer attacks produced slightly negative average movement, meaning they sometimes triggered more conservative responses. Trust-signal and compound attacks shifted responses toward the attacker even without explicit endorsement. Mode 3 had the largest average failed-case drift and a **15.0% silent-shift rate**.

Silent-shift rates by backend ranged from:

- **1.1%** for GPT-5.4-mini.
- **3.0%** for Claude-Sonnet-4.6, despite its 0% ASR.
- **9.1%** for Claude-Haiku-4.5, the highest rate.
- **7.6%** each for DeepSeek-V4-Pro and Gemini-3.1-Pro.
- **6.8%** each for Kimi-K2.6 and Qwen3.6-Plus.

This demonstrates that zero explicit endorsements do not necessarily mean zero attacker influence.

Finance was the most prominent domain for silent drift: 11 of 13 models had positive mean failed-case ΔOSS there. Health and Consumer IT contained several negative-mean cells, suggesting attacks sometimes made answers more cautious. Legal had the smallest shift magnitude, with mean absolute ΔOSS below 0.06 for every backend-domain cell.

### 4.3 Stealth and self-audit

Failed attacks looked considerably more credible than successful ones:

- Mean SS for failed attacks: **0.788**
- Mean SS for successful attacks: **0.393**

Machine-layer attacks looked credible on average, with SS around **0.80**, but rarely succeeded. Mode 3 had the highest success and the lowest credibility:

- Overall Mode 3 SS: **0.576**
- Mode 3 SS among successful cases: **0.315**

The paper describes this as a persuasion–stealth trade-off: the strongest attacks caused conspicuous credibility losses even as they secured endorsements.

In a Consumer IT self-audit diagnostic:

| Outcome | Cases | External SS | Self-SS | Self-rating gap |
|---|---:|---:|---:|---:|
| Failed attack | 669 | 0.747 | 0.796 | +0.049 |
| Successful attack | 189 | 0.297 | 0.609 | +0.312 |

On successful attacks, answering models rated their own compromised answers **0.312 points higher** than the external blind auditor. Self-audit therefore failed to reveal much of the attack-induced credibility loss.

### 4.4 Domain differences

Pooled across all models, mode-specific ASRs by domain were:

- **Finance:** 0.0%, 0.7%, 0.0%, 2.1%, 10.5%, and 18.2% across 1A-i, 1A-f, 1B, 2A, 2B, and 3.
- **Health:** 0.7%, 1.4%, 0.7%, 7.0%, 8.4%, and 23.1%.
- **Legal:** 0.7%, 4.9%, 2.8%, 23.8%, 42.0%, and 42.0%.
- **Consumer IT:** 0.0%, 2.8%, 1.4%, 23.8%, 38.5%, and 65.7%.

Legal and Consumer IT were generally the most vulnerable, although the worst domain depended on the backend. Examples include:

- Gemini-3-Flash peaked in Legal at **43.9%**.
- Qwen3.6-Plus peaked in Consumer IT at **31.8%**.
- Gemini-3.5-Flash reached **47.0%** in Legal.
- DeepSeek-V4-Flash reached **40.9%** in Legal.
- GPT-5.4-mini’s only domain-level attacks occurred in Consumer IT, at **3.0%**.

All **572 clean-baseline cases** were ultimately judged ASR = 0 after manual correction of one false-positive label involving a vitamin-D task.

### 4.5 Search behavior and robustness archetypes

The most robust models used different search strategies:

| Backend | Average searches | Average live follow-ups | ASR |
|---|---:|---:|---:|
| Claude-Sonnet-4.6 | 2.31 | 0.12 | 0.0% |
| GPT-5.4-mini | 1.36 | 0.04 | 0.8% |
| DeepSeek-V4-Pro | 4.90 | 1.57 | 9.1% |

Claude-Sonnet often explicitly recognized possible coordination and answered from remaining clean sources. GPT-5.4-mini searched relatively little, suggesting greater reliance on prior knowledge. DeepSeek-V4-Pro performed the most and widest-ranging follow-up searches.

Across all 308 cases, GPT-5.4-mini averaged 1.36 searches and issued at least two searches in only **19.2%** of cases. Claude-Sonnet averaged 2.31 and issued at least two in **95.5%**. DeepSeek-V4-Pro averaged 4.90, reached a maximum of 12, and issued at least two in **92.9%**.

Search volume alone therefore did not determine robustness.

Within-family failures were also not always nested:

- GPT-5.4-mini’s two failures were both among GPT-5.4-nano’s 17 failures.
- Claude-Sonnet had no failures, while Claude-Haiku had 33.
- Gemini pairs were non-nested: 18–23 cases could fail on Gemini-3.1-Pro but pass on a Flash sibling.
- DeepSeek-V4-Pro had five failures that did not occur on V4-Flash.

Thus, model-family differences concerned not only overall strength but also which attacks triggered failure.

### 4.6 Figure 3: Source count, diversity, and rank

Figure 3 plots ASR against the number of injected sources, \(N=1,2,3\), on Gemini-3-Flash.

Exact plotted values were:

- **Mode 2A, repeated institutional source:** 36.4%, 25.0%, 36.4%.
- **Mode 2B, distinct consensus sources:** 38.6%, 54.5%, 77.3%.
- **Mode 3, expanding citation chain:** 25.6%, 50.0%, 69.0%.

Repeating the same source did not produce a dose-response. Adding distinct apparent corroborators caused a strong monotonic increase.

With three sources held constant, changing their placement had no statistically significant effect:

- Mode 2B: top **77.3%**, middle **63.6%**, bottom **76.7%**; \(\chi^2\) test \(p=0.27\).
- Mode 3: top **69.0%**, middle **64.3%**, bottom **65.1%**; \(p=0.89\).

The decisive factor was therefore source diversity—not repetition or rank position.

### 4.7 Defense and deployment results

Overall ASR under the three conditions was:

| Backend | A: no defense | B: OWASP prompt | C: OpenClaw | B−A | C−A |
|---|---:|---:|---:|---:|---:|
| Gemini-3-Flash | 31.4% | 24.6% | 34.1% | −6.8 | +2.7 |
| DeepSeek-V4-Flash | 20.1% | 12.9% | 12.9% | −7.1 | −7.2 |
| MiniMax-M2.7 | 17.4% | 6.1% | 13.6% | −11.4 | −3.8 |

The OWASP-derived prompt reduced average ASR for all three models but did not eliminate vulnerability. OpenClaw helped DeepSeek and MiniMax while worsening Gemini overall.

The largest reversal occurred under forged authority:

- Gemini-3-Flash Mode 2A rose from **27.3% to 59.1%**, an increase of **31.8 percentage points**.
- DeepSeek-V4-Flash fell from **22.7% to 11.4%**, a reduction of **11.4 points**.
- MiniMax-M2.7 fell from **25.0% to 15.9%**, a reduction of **9.1 points**.

OpenClaw also increased Gemini’s Mode 3 ASR from **65.9% to 79.5%**. The OWASP prompt slightly increased Gemini Mode 3 from 65.9% to **68.2%**, despite lowering its average ASR.

For DeepSeek, the prompt reduced Mode 2B from 34.1% to **13.6%** and Mode 3 from 61.4% to **45.5%**. For MiniMax, it reduced Mode 2A from 25.0% to **4.5%**, Mode 2B from 29.5% to **6.8%**, and Mode 3 from 45.5% to **25.0%**.

These results show that a defense cannot be evaluated independently of its backend and deployment scaffold.

### 4.8 Agent-skill recommendations

The auxiliary study examined a higher-stakes setting in which endorsement becomes an installation command.

#### Paired OpenClaw study

Ten OpenClaw scenarios were run clean and under Mode 2B.

In clean conditions:

- Claude-Sonnet-4.6 refused to provide a useful answer in **10/10** cases.
- It falsely rejected OpenClaw or its skill pathway in **8/10**.
- GPT-5.4-mini provided calibrated useful answers in **10/10** and falsely rejected none.

Under Mode 2B:

- Claude endorsed the fabricated skill in **0/10**.
- GPT-5.4-mini endorsed it and emitted the exact installation command in **10/10**.

Read-only variants of four scenarios reduced Claude’s false-rejection rate from **80% to 0%**, although it still denied useful answers in **75%**. This indicates that Claude’s rejection was influenced by the stakes of autonomous action, not only the brand.

#### Cross-ecosystem Mode 2B study

Six matched domains—travel, inbox, payroll, cloud infrastructure, CRM, and trading—were tested in each of three ecosystems:

| Ecosystem | Cases | Claude | GPT-5.4-mini | GPT-5.5 |
|---|---:|---:|---:|---:|
| OpenClaw | 6 | 0/6 | 6/6 | 6/6 |
| Anthropic Skills | 6 | 0/6 | 5/6 | 4/6 |
| Hermes Agent | 6 | 0/6 | 6/6 | 6/6 |
| **Total** | **18** | **0/18** | **17/18** | **16/18** |

Both GPT-5.5 rejections occurred within Anthropic Skills. Claude clean probes showed zero false rejection for three Hermes cases and eight non-agent developer tools, suggesting its clean-condition over-rejection was specifically connected to OpenClaw. GPT over-acceptance occurred in all three ecosystems.

#### Cross-mode OpenClaw study

Across 26 OpenClaw attack cases:

| Attack mode | Cases | Claude | GPT-5.4-mini | GPT-5.5 |
|---|---:|---:|---:|---:|
| Hidden DOM | 4 | 0/4 | 4/4 | 3/4 |
| Visible planted page/snippet mode | 4 | 0/4 | 4/4 | 4/4 |
| Institutional authority | 4 | 0/4 | 4/4 | 4/4 |
| Synthetic consensus | 10 | 0/10 | 10/10 | 10/10 |
| Citation chain | 4 | 0/4 | 4/4 | 4/4 |
| **Total** | **26** | **0/26** | **26/26** | **25/26** |

The most robust main-benchmark models therefore failed in opposite directions: Claude over-rejected legitimate use, whereas GPT frequently trusted fabricated skills.

---

## 5. Analysis and Interpretation

The authors conclude that current safety measures concentrate primarily on the **instruction layer**. Models are comparatively capable of recognizing direct commands, jailbreak-like imperatives, and hidden instructions. They are much less reliable when the attacker manipulates the **evidence layer** and allows the model to form the attacker-favored conclusion itself.

This interpretation explains several findings:

- Trust-signal attacks consistently outperformed hidden-DOM and snippet attacks.
- Factual pseudo-evidence was more effective than an imperative delivered through the same hidden carriers.
- Independent-looking consensus strongly increased ASR.
- Repetition of one source did not.
- Rank placement had no significant effect once source structure was controlled.
- Prompt defenses reduced but did not eliminate attacks.

The Mode 2B/Mode 3 difference may arise because an explicit authority anchor or citation chain is conspicuous enough to trigger verification in some models, whereas apparently independent consensus contains no single obvious anomaly. Other backends require the authority cue before trusting an unfamiliar target, making Mode 3 stronger.

The authors argue that defenses should therefore operate at the same layer as the attack. Relevant mechanisms include:

- Source provenance tracking.
- Checks for actual independence among apparent corroborators.
- Detection of coordinated publishing.
- Verification of citation-chain origins and dependencies.
- Domain-authenticity validation.
- Clear provenance displays for users.

Prompt instructions may supplement these mechanisms but cannot replace them.

ASR alone is insufficient because:

- Some unsuccessful attacks materially shift the answer.
- A model may overestimate the credibility of its own compromised output.
- A model can avoid endorsement by rejecting legitimate systems, producing a different user-harming failure.
- Clean and attacked responses can differ continuously even without a binary recommendation.

The results also imply that backend and harness form a joint safety configuration. The same OpenClaw scaffold reduced attacks for two backends but amplified authority-based and compound attacks for Gemini-3-Flash.

From an attacker-economics perspective, Mode 2B is especially concerning because it needs neither control of a real high-authority domain nor sophisticated citation infrastructure. An attacker can publish several cheap, coordinated sibling pages. Defenders, by contrast, must verify provenance and independence for each query.

The authors believe the same evidence-layer vulnerability may apply to retrieval-grounded systems beyond standalone search agents, including general RAG assistants, coding agents, and systems that synthesize research papers. The paper does not empirically evaluate all those settings, so this is presented as a broader implication rather than a measured result.

The study also raises a deployment-equity concern: if cheaper backends are more vulnerable and that difference is invisible to users, pricing tiers effectively become safety tiers. The authors argue that basic provenance, source validation, and coordinated-publishing detection should be available across tiers, especially for health, finance, and legal tasks.

Finally, recommendation manipulation may extend beyond discrete products to opinion shaping and interpretive questions without clear ground truth. OSS captures within-turn drift only; cumulative belief changes across sessions and users remain unmeasured.

---

## 6. Contributions and Novelty

The paper’s principal contributions are:

- **A web-search-specific attack taxonomy** covering machine-layer discrepancies, manipulated trust signals, and compound citation structures through five core modes and two Mode 1A semantic variants.
- **SearchGEO**, a controlled evaluation framework that injects synthetic attacks into cached real search results while retaining clean live fallback.
- **A 44-query benchmark** spanning health, finance, legal, and Consumer IT tasks, with validated reference answers and concrete attacker objectives.
- **Multiple output-level metrics** distinguishing binary endorsement, continuous semantic shift, apparent credibility, and false rejection.
- **A 13-backend comparison** showing a 0.0%–31.4% range in overall attack success and backend-specific differences in the strongest attack mode.
- **Evidence that source diversity drives corruption**, whereas repeating one source and changing rank do not significantly increase success.
- **Evidence that binary ASR understates risk**, because failed attacks can cause silent semantic drift.
- **A self-audit diagnostic** showing models systematically overrate compromised successful answers relative to a blind external auditor.
- **A backend–deployment interaction analysis** showing that the same scaffold can either reduce or amplify attacks depending on the model.
- **An auxiliary skill-installation study** revealing opposite robust-end failures: Claude’s over-rejection and GPT’s near-universal acceptance of fabricated skills.

---

## 7. Limitations and Caveats

### Controlled proxy rather than the live web

The study uses a hybrid proxy, not live manipulated search engines. It therefore does not capture:

- Live ranking dynamics.
- Freshness signals.
- Competitive SEO behavior.
- Changes in search-engine retrieval over time.
- The full effects of rendered web pages.

Because about 30% of cached results contained snippets but no extracted page body, the shorter evidence context may make reported ASR slightly optimistic relative to fully rendered pages. The numbers are controlled-environment estimates, not direct predictions of real-world attack rates.

The study also assumes successful placement within the target query cluster rather than measuring how often an attacker could achieve such placement.

### Scope of tasks and interaction

The main benchmark contains 44 single-turn recommendation tasks in four domains. It does not measure:

- Longitudinal belief change.
- Repeated exposure across sessions.
- Population-level user effects.
- All possible search tasks, languages, domains, or agent architectures.
- Opinion-shaping tasks without clear reference answers.

### Agent-skill probe scale

The skill study is intended to isolate a mechanism, not estimate real-world prevalence. It has relatively few scenarios and ecosystems. A population-scale analysis would need to vary retrieved-evidence density and brand recognition independently.

### Judge coupling

GPT-5.4-mini is both an evaluated backend and the base model for the ASR, OSS, and SS judges. The blind auditor is separated by prompt and information access, not by model family. Claude-Opus-4.7 perfectly agreed on a stratified sample, but a complete cross-family re-evaluation of all 308 GPT-5.4-mini cases was not performed.

### Deployment ablation is incomplete

The OpenClaw condition required session isolation, an anti-silent-reply clarification, and a search mandate. It was therefore not literally an unmodified deployment. The study did not isolate whether bootstrap instructions, tools, skills, plugins, or another workspace component caused the backend-specific reversals.

### Metric boundaries

- ASR does not capture partial influence or over-refusal.
- OSS provides only within-turn movement toward a predefined target.
- SS measures apparent credibility, not factual accuracy.
- Self-audit can substantially overrate compromised answers.
- The reference answer can differ from a backend’s clean answer, which required baseline subtraction and introduces dependence on reference calibration.

### Ethical and release constraints

No malicious pages were published, no live rankings were manipulated, and no advertisements, link farms, deceptive live domains, credentials, or executable payloads were used. Attack files remained inert within the offline harness.

Because the artifacts could help adversaries optimize content, the authors use a two-tier release:

- Public materials include code, configurations, benign queries, mode labels, aggregate metrics, sanitized outputs, judge labels, and evaluation scripts.
- Full attack documents, injected-result contexts, and raw traces are request-only under restrictions against deployment and live SEO.
- Raw copyrighted search caches, executable payloads, deceptive infrastructure, and operational SEO instructions are not publicly released.

---

## 8. Future Work or Open Questions

The authors identify several next steps:

- Combine the distinct robustness mechanisms observed in Claude, GPT, and DeepSeek rather than treating one as uniformly superior.
- Extend the skill-installation evaluation to more ecosystems and a much larger set of scenarios.
- Independently vary evidence density and brand recognition in skill studies.
- Fully re-evaluate the judging pipeline with a different model family.
- Isolate which OpenClaw components cause model-specific improvements or degradations.
- Evaluate provenance tracking, source-independence checks, coordinated-publishing detection, and citation-chain integrity verification.
- Study live ranking, freshness, and competitive SEO dynamics.
- Examine cumulative and longitudinal belief shift across turns, sessions, and users.
- Test interpretive and preference-shaping tasks that lack a simple ground-truth answer.
- Determine how to provide comparable evidence validation and provenance protections across backend pricing tiers.

---

## 9. High-Level Takeaway (Plain Language)

LLM search agents can be manipulated without being given an obvious malicious instruction. If several apparently independent websites recommend the same fabricated product or service, many agents treat that agreement as real evidence and pass the recommendation to the user. Vulnerability varied enormously by model—from 0% explicit attack success for Claude-Sonnet-4.6 to 31.4% for Gemini-3-Flash—and even “failed” attacks sometimes shifted answers. Simple defensive prompts helped but did not solve the problem, and one deployment framework helped some models while making another less safe. Reliable search agents therefore need technical checks on where evidence came from, whether sources are genuinely independent, and whether citations ultimately trace back to the same attacker.