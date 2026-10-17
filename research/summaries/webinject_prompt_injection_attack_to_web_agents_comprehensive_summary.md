# Stage 0 — Document Accessibility Report

The supplied work is **WebInject: Prompt Injection Attack to Web Agents**, by Xilong Wang, John Bloch, Zedian Shao, Yuepeng Hu, Shuyan Zhou, and Neil Zhenqiang Gong, Duke University. The supplied publication line identifies the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, November 4–9, 2025, printed pages 2010–2030. Source locators below use **physical PDF pages 1–21**, not the printed proceedings page numbers.

All 21 physical pages have supplied extracted text. Nineteen pages also have supplied images: pp. 1–9 and 12–21. Pages 10–11, containing references, were inspected as text only. Thus the main document is available across the stated page range, but visual coverage is partial. All supplied substantive figures, tables, and Algorithm 1 fall on visually supplied pages. The images support direct inspection of layouts, tables, equations, diagrams, and code illustrations. Small plotted lines and miniature webpage text are less readable than ordinary body text. Exact unlabeled plot coordinates cannot be reliably recovered.

The supplied extraction is sufficient without additional OCR. Equations were checked against their supplied renderings, with special attention to subscripts, sums, probability conditioning, and the perturbation constraints. No tools, browsing, execution, or outside sources were used. The supplied checksum is retained as identifying metadata; it was not independently recomputed. The failure message concerning an image at `-` does not remove the 19 images visibly supplied in the prompt.

Appendix content is present on pp. 12–21, although no separately lettered appendix heading is visible in the supplied material. References occupy pp. 10–11. No supplementary files, executable repository, model checkpoints, underlying numerical plot data, or dataset files were supplied. The accessibility metadata's detected appendix pages [6, 9] appear to identify mentions of the appendix; they do not establish that the appendix itself begins on either page. No apparently missing numbered page is identified within 1–21. This does not establish the availability of any separate artifacts.

Evidence labels used throughout are **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No [E] external information is introduced. HIGH confidence means the supplied source supports a clear transcription or narrowly stated conclusion; it does not independently validate the authors' experiment. MEDIUM confidence applies to interpretations or unresolved implementation details. UNKNOWN applies to information the supplied work does not specify.

# 1. Plain-language orientation

[A] A web agent uses a multimodal large language model, or **MLLM**, to look at a webpage screenshot and decide what action to take. The action might be a click, typing text, scrolling, or ending the session. The user's instruction is only one input: the model also receives the screenshot and a history of earlier actions. WebInject attacks the webpage that supplies this visual observation, rather than directly changing the user's instruction.

[A] The researchers assume an attacker can change a target webpage's source code and access the parameters of the model used by the agent. They optimize small changes to the webpage's rendered pixel values so that, after the paper's monitor-specific screenshot transformation, the model emits a chosen action. They implement those pixel changes through injected webpage code. The method aims to retain the page's normal appearance and interaction behavior while influencing the agent.

[A] The central technical problem is that the attack cannot simply optimize a screenshot and assume the same perturbation will survive implementation in a webpage. In the authors' system model, raw rendered pixels undergo an International Color Consortium, or **ICC**, profile transformation before becoming the screenshot supplied to the model. The authors train a neural network to approximate this transformation and replace screenshot resizing with a differentiable approximation during optimization.

[A] Table 1 reports WebInject attack success rates, or **ASRs**, between 0.963 and 0.975 across five evaluated model backbones, averaged across ten webpage datasets. The strongest listed textual webpage baseline varies by model; the screenshot-based baseline adapted to the authors' webpage-control threat model has ASR 0.000. These results concern generation of the exact target action under the reported conditions. They are not measurements of completed malware installation, successful theft, or every downstream consequence suggested in the introduction.

[D] For the user's research question—why web AI agents might be more vulnerable than standalone language models—the paper supplies evidence of an additional environmental attack route and of action-level consequences. **It does not conduct a controlled comparison against standalone LLMs, so it does not establish a quantitative vulnerability ranking between those system classes.** Its strongest contribution to that question is explaining how attacker-controlled web content can influence a model's operational decisions through a visual channel.

# 2. Document roadmap

The document is a mixed cybersecurity, machine-learning, and algorithm paper with an empirical evaluation. Its substantive inventory is:

| Inventory ID | Original item | Physical pages | Role |
|---|---|---:|---|
| ABSTRACT | Abstract | 1 | Problem, method, and headline result |
| S1 | §1 Introduction | 1–2 | Motivation, prior attack categories, claimed gap |
| S2 | §2 Background | 2–3 | Screenshot model, agent inputs, action probability |
| S3 | §3 Threat Model | 3–4 | Goals, capabilities, background knowledge |
| S4 | §4 WebInject | 4–6 | Overall attack construction |
| SS4.1 | §4.1 Formulating an Optimization Problem | 4–5 | Loss and perturbation constraints |
| SS4.2 | §4.2 Solving the Optimization Problem | 5–6 | Mapping network, resizing surrogate, projected gradient descent |
| SS4.3 | §4.3 Implementing the Perturbation | 6 | Webpage code and transparent original elements |
| S5 | §5 Experiments | 6–9 | Setup and results |
| SS5.1 | §5.1 Experimental Setup | 6–8 | Datasets, models, prompts, histories, metric, monitors, baselines, parameters |
| SS5.2 | §5.2 Experimental Results | 8–9 | Main results and three variation studies |
| S6 | §6 Related Work | 9 | Prompt injection and web-agent attacks |
| S7 | §7 Conclusion | 9 | Authors' novelty and effectiveness claims |
| S8 | §8 Limitations | 9 | Source-control assumption, untested transfer, proposed defenses |
| S9 | §9 Acknowledgments | 9 | Funding and reviewer acknowledgment |
| REFERENCES | References | 10–11 | Bibliographic entries, inspected as text |
| APPENDIX | Unlettered appendix material | 12–21 | Algorithm, implementation examples, prompts, detailed results |

There are 14 numbered figures, including distinct panels in Figures 2, 4–6, and 11–14; 12 numbered tables; one algorithm; five numbered equations; and several important unnumbered definitions and update rules. There are no visible theorems, lemmas, formal hypotheses, or explicitly numbered research questions. The experiment register used here is X1 main attack comparison, X2 monitor-count variation, X3 perturbation-bound variation, X4 semantic prompt variants, X5 alternative actions, and X6 computational overhead. The inventory, not response length, defines the coverage denominator.

# 3. Background and context

[A] A **webpage** is represented by HTML source code ω. A browser renders it into raw pixel values I(ω,d), where d identifies the monitor or viewing configuration. The paper assumes fullscreen browser operation and defines the visible region using width w_d and height h_d, with the upper-left corner as the coordinate origin. The pixels have three red, green, and blue channels, abbreviated RGB.

[A] The paper distinguishes raw pixels from screenshot pixels. It writes I_s(ω,d) = M(I(ω,d),ICC_d), where M is a mapping determined by the monitor's ICC profile. An ICC profile describes how colors should appear on that monitor. The authors state that different monitor sizes and profiles can produce different screenshots from the same webpage. This is the authors' screenshot model, supported by their examples and simulation procedure; this analysis does not externally validate its applicability to every browser or agent deployment.

[A] The agent's model f receives a user prompt p, a resized screenshot r(I_s(ω,d)), and previous-action history H. It generates a textual action a. An action combines a function name with arguments: a coordinate for a click, content for typing, or a direction for scrolling. Because the action is text, its likelihood can be represented by a product of token probabilities.

[A] A **prompt injection attack**, in the paper's usage, redirects model behavior through untrusted input toward an attacker-selected task. WebInject is unusual within that description because it does not inject an explicit textual instruction into the page. It instead optimizes a visual perturbation that changes the likelihood of an action string. The authors retain the prompt-injection terminology while connecting this mechanism to adversarial visual examples.

[A] **Differentiable** means the optimization can propagate gradients through an operation to determine how changing the perturbation changes the loss. The authors identify both their screenshot mapping and ordinary resizing implementations as obstacles to this propagation. A **surrogate** is an approximation used in their place during optimization. **Projected gradient descent**, abbreviated PGD, repeatedly adjusts the perturbation to reduce loss and then forces it back inside the allowed constraints.

# 4. Research problem and gap

[A] The existing problem is that MLLM-based web agents may act on attacker-manipulated webpages. The authors identify possible consequences including click fraud, redirection to malicious pages, malware downloads, and sensitive-information disclosure. These motivate the work; the experiments primarily measure exact action output rather than those complete harmful workflows.

[A] The authors separate prior attacks into two categories. Webpage-based attacks alter HTML, often with deceptive pop-ups or elements. They describe these approaches as largely heuristic, sometimes ineffective, and often visible. Screenshot-based attacks optimize image perturbations but assume access to screenshots captured on the user's device. In the authors' threat model, the attacker cannot directly change those screenshots.

[A] The claimed gap is therefore a page-implementable attack that is simultaneously effective, visually unobtrusive, and robust to the transformation between rendered webpage pixels and model input. A second concern is variation across monitor dimensions and profiles. A perturbation built for a large viewing area may partly lie outside a smaller one.

[A] WebInject addresses this gap by optimizing in raw webpage-pixel space, accounting for screenshot conversion through learned mapping networks, constraining the perturbation to a shared visible region, and then realizing it through source-code modification. [D] The scope is narrower than arbitrary attacks on all web agents: it concerns screenshot-driven agents, accessible model parameters, controlled target pages, selected target prompts and monitors, and the reported action interface.

# 5. Research questions, objectives, and hypotheses

The paper does not state formal numbered research questions or statistical hypotheses. Its explicit and clearly described objectives are:

1. [A] Induce an attacker-specified action by modifying the target webpage.
2. [A] Keep the webpage modifications visually imperceptible through a small perturbation bound.
3. [A] Implement the perturbation without direct screenshot access.
4. [A] Optimize across target prompts, shadow histories, and potentially multiple monitors.
5. [A] Compare effectiveness against adapted webpage and screenshot attack baselines.
6. [A] Examine monitor count, perturbation magnitude, semantic prompt variation, and other action types.

[D] These objectives can organize research questions for this analysis, but they should not be mistaken for questions explicitly numbered by the authors. X1 tests comparative ASR; X2 tests selected-monitor breadth; X3 tests the magnitude–effectiveness relationship; X4 tests limited semantic prompt variation; X5 tests action-type breadth. X6 reports incremental computational cost.

[D] The user's broader question adds a separate interpretive objective: identify what about web-agent operation introduces attack exposure beyond a model responding to a direct prompt. The supplied study illuminates environmental observation and action generation, but contains no standalone-LLM control group and no hypothesis test of which system class is more vulnerable.

# 6. Assumptions / Threat Model

[A] The attacker controls a target webpage as its malicious administrator or through compromise. They can modify source code ω. The attacker chooses a target action a*, constructs target prompts P intended to resemble user requests, and gathers monitor information D such as sizes and ICC profiles. They have access to the parameters of the victim MLLM f. This is a white-box model-access assumption, even though the attacker lacks local access to the user's screenshot and history.

[A] The attacker cannot directly modify screenshots and does not obtain real agent interaction histories. Instead, they construct a set of **shadow histories** for optimization. Real-user behavior is approximated in evaluation by a separately sampled set of histories. The history representation includes prior actions only; the paper does not include full prior screenshots or conversational observations in H.

[A] The target is a selected action, usually a click at a randomly chosen coordinate within the region shared by selected monitors. The objective is high likelihood of that action when a target or semantically similar prompt is used. Stealthiness concerns the appearance of the modified webpage to ordinary users. The paper implements this with an ℓ∞ bound and shows example images; it does not report a user detection study.

[D] The operational boundary is between untrusted page content and the agent's trusted decision process. The user instruction remains an input, but the attacker changes the environmental input on which the decision depends. The browser, local screenshot machinery, and model execution are outside the attacker's stated direct control. This is an interpretation of the source's capabilities, not a separate formal trust diagram supplied by the authors.

[A] Multiple-monitor optimization limits the perturbation to the top-left rectangle common to all selected displays. It does not establish robustness to every unseen monitor, browser configuration, viewport, dynamic page state, or model. 'Universal' means shared for the target webpage across the selected configurations, not one perturbation demonstrated to attack every webpage or every MLLM.

# 7. Methodology

## Study design and attack construction

[A] For a target webpage, model, action, prompt set, monitor set, and shadow-history set, the method minimizes the summed negative log probability of the target action. Its perturbation δ is added to raw rendered pixels before screenshot conversion. Two constraints restrict δ: each element's absolute magnitude is at most ε, and all elements outside the common visible rectangle are zero.

[A] For each monitor d, a U-Net mapping neural network N_d approximates the transformation M(·,ICC_d). Training pairs consist of randomly perturbed raw pixel inputs and their ICC-transformed outputs. This network is used to supply gradients through an otherwise non-differentiable mapping. A differentiable resizing operation r′ replaces r during optimization. The source mentions PyTorch and TensorFlow resizing functions as examples, without clearly identifying a single fully specified implementation and interpolation configuration for all experiments.

[A] Algorithm 1 initializes δ to zero, randomly samples prompt and shadow-history minibatches, computes the loss gradient g, updates δ ← δ − αg, clamps elements to [−ε,ε], and applies a spatial mask. This runs for T iterations. The resulting perturbation is implemented by extracting canvas pixels from the page, adding perturbation values, and writing pixels back. Original HTML elements are placed above the rendered perturbation layer with opacity zero so that interactions continue to reach those elements.

## Data and sample sizes

[A] Ten datasets cover blog, commerce, education, healthcare, and portfolio pages, with a real and synthetic dataset for each category. Real pages are downloaded with the SingleFile extension, which snapshots a webpage into one file. Synthetic pages are generated using GPT-4-Turbo from the Figure 9 instruction. That instruction asks for category-specific HTML and CSS, responsive design, realistic content, and placeholder images.

| Category | Real pages [A] | Synthetic pages [A] | Source |
|---|---:|---:|---|
| Blog | 50 | 100 | p. 12, Table 3 |
| Commerce | 26 | 100 | p. 12, Table 3 |
| Education | 42 | 100 | p. 12, Table 3 |
| Healthcare | 51 | 100 | p. 12, Table 3 |
| Portfolio | 43 | 100 | p. 12, Table 3 |

[C] The real-page total is 50+26+42+51+43 = 212. The synthetic total is 5×100 = 500. Combined, the table supplies 712 pages. No webpage inclusion/exclusion protocol, URL list, geographic distribution, annotation validation, licenses, or downstream dataset availability is specified in the supplied work. No explicit training/validation/test split is given for mapping-network data.

[A] Each webpage receives ten target prompts generated from its source code. Figure 10 requests realistic action-oriented user intents rather than simple questions about displayed information. There is an unresolved generator-model inconsistency: p. 6 names GPT-4-Turbo and then says the instruction guides GPT-4o. The exact generator cannot be confidently resolved from the supplied material.

[A] Each page has ten randomly sampled shadow histories and ten randomly sampled evaluation histories, each with 3–5 actions. Evaluation histories are not used to optimize the perturbation. No validation that these random histories correspond to coherent actual user trajectories is reported. [C] If every listed page receives ten prompts as stated, there are 712×10 = 7,120 generated target prompts; this is a derived count, not an independently reported evaluation-run total.

## Models, monitors, baselines, and parameters

[A] The backbones are UI-TARS-7B-SFT, Phi-4-multimodal-instruct, Llama-3.2-11B-Vision-Instruct, Qwen2.5-VL-7B-Instruct, and Gemma-3-4b-it. The paper shortens these to UI-TARS, Phi-4, Llama-3.2, Qwen-2.5, and Gemma-3. No additional model sizes should be inferred where the name does not provide them.

[A] The authors report three physical monitors: 24-inch iMac M1, 15-inch MacBook Air M3, and 27-inch 4K UHD LG 27UL500-W. They simulate Dell S2722QC and ASUS XG27UCG 27-inch 4K UHD monitors. The default is a single LG 27UL500-W target monitor. Simulation uses Python, Selenium browser-window sizing, canvas extraction, and PIL ImageCms conversion from sRGB to the target profile.

[A] Baselines combine a common pop-up structure with Naive, Context Ignoring, Fake Completion, or Combined textual instructions. Their three elements are an attention hook, instruction, and information banner positioned at the target coordinate. Screenshot-based attacks are adapted by optimizing screenshot perturbations and then adding them directly to raw webpage pixels. This adaptation is central to interpreting their zero ASR: the result is not a test of unrestricted screenshot editing.

[A] Default perturbation parameters are ε = 16/255, α = 0.3, and T = 2,500. Mapping-network training uses 16,240 input-output pairs across target webpages, 200 epochs, learning rate 0.005, and batch size 16. The mapping-training random perturbation distribution, optimizer, network-detail configuration, data split, seeds, and prompt/history minibatch sizes are not specified here.

[A] ASR is exact target-action equality, averaged over target monitors and then over webpages, target prompts, and user histories for a dataset. Table 1 reports averaging across the ten datasets. No confidence intervals, standard deviations, repeated-seed estimates, p-values, or statistical tests are supplied. The paper uses 'significantly' in its prose; the supplied evidence supports large observed differences, not a documented inferential significance test.

# 8. Experiments / Analyses

| ID | Purpose and manipulated condition | Setup and evidence | Main result | Qualification |
|---|---|---|---|---|
| X1 | Compare attack methods | Five MLLMs, ten datasets, default single monitor and click target; Tables 1, 4–9 | Table 1 WebInject 0.963–0.975; adapted screenshot baseline 0.000 | White-box models; exact action output; Phi-4 aggregate inconsistency |
| X2 | Vary number of selected monitors | Figures 2a, 11, 12; displayed conditions 1, 3, 5 monitors | ASR decreases as monitor count grows | Exact curve values are not tabulated; selected subsets not fully detailed |
| X3 | Vary perturbation bound | Figures 2b, 5, 13, 14; ε = 4/255, 8/255, 16/255, 32/255 | Larger bound increases ASR toward 1 | Visual examples are not perceptual detection measurements |
| X4 | Replace target prompts with semantic variants | Figure 8 and Table 11; five models and ten datasets | Values 0.871–0.959; Gemma synthetic blog 0.957 | One generated semantic-variation procedure, not arbitrary prompt distribution |
| X5 | Change action type | Table 10, Phi-4, synthetic blog dataset | Nine alternative actions have ASR 0.976–0.993 | Narrower model/dataset scope than X1 |
| X6 | Compare computational overhead | Table 12, single NVIDIA RTX A6000 GPU, per page per monitor | +1.70–2.57 minutes and +1.93–2.61 GB | Baseline absolute time and memory unspecified |

[A] X1 supports the comparative-effectiveness claim in the authors' implementation. WebInject's source-space perturbation explicitly accounts for the mapping that the adapted screenshot attacks ignore. However, there is no separate reported ablation removing only N_d, only r′, or only a constraint from WebInject while keeping all other conditions fixed. [D] The baseline comparison is suggestive of the importance of mapping awareness, but does not isolate every causal contribution of the complete method.

[A] X2 studies optimization across more selected displays. The authors attribute declining ASR to a smaller overlapping perturbation region. [D] More monitors also add transformation conditions to the summed objective; the supplied experiment does not isolate spatial-overlap effects from the other changes. It demonstrates a selected-configuration trade-off rather than unrestricted monitor generalization.

[A] X3 explores the perturbation budget. The authors state ASR rises nearly to 1 as ε increases from 4/255 to 32/255. They invoke cited prior work for considering ε ≤ 16/255 stealthy. That is an author-reported contextual justification within the paper, not an independently checked perceptual threshold.

[A] X4 uses generated semantically equivalent user prompts without directly optimizing on those replacements. On Gemma-3 synthetic blog pages, ASR changes from 0.988 with target prompts to 0.957 with variants. [C] The difference is 0.988−0.957 = 0.031, or 3.1 percentage points. Generalization here remains conditional on semantic similarity to the optimized prompts.

[A] X5 extends action generation beyond clicks. The test includes coordinate actions, a randomly chosen keyboard combination, one of four scrolling directions, typing selected harmful-query content, waiting, ending, and requesting user help. Generating those action strings is the measured event; the paper does not show every resulting operation being completed successfully in a realistic multi-step workflow.

[A] X6 appears in the appendix without extensive main-text discussion. It provides incremental rather than total resource consumption. The supplied caption does not fully explain allocation of shared mapping-network training cost across target pages. This prevents a reliable total attack-cost estimate.

# 9. Results

## Main attack comparison

[A/B] Table 1 is the principal aggregate comparison. Values are proportions, so 0.975 corresponds to 97.5% ASR; converting to percentages does not change the reported metric.

| Model | Naive | Context Ignoring | Fake Completion | Combined | Adapted screenshot | WebInject |
|---|---:|---:|---:|---:|---:|---:|
| UI-TARS | 0.085 | 0.147 | 0.054 | 0.050 | 0.000 | 0.975 |
| Phi-4 | 0.095 | 0.050 | 0.047 | 0.025 | 0.000 | 0.963 |
| Llama-3.2 | 0.270 | 0.212 | 0.345 | 0.248 | 0.000 | 0.972 |
| Qwen-2.5 | 0.100 | 0.095 | 0.067 | 0.063 | 0.000 | 0.970 |
| Gemma-3 | 0.062 | 0.054 | 0.037 | 0.062 | 0.000 | 0.972 |

[C] Subtracting each model's strongest displayed baseline gives absolute ASR gains of 0.828 for UI-TARS (0.975−0.147), 0.868 for Phi-4 (0.963−0.095), 0.627 for Llama-3.2 (0.972−0.345), 0.870 for Qwen-2.5 (0.970−0.100), and 0.910 for Gemma-3 (0.972−0.062). These are 82.8, 86.8, 62.7, 87.0, and 91.0 percentage points. The Gemma gain is also explicitly reported by the authors. It must not be called a 91% relative improvement.

[A/B] Table 4 gives detailed WebInject ASR. Its lowest displayed value is 0.929 for Gemma-3 on real education pages. Its highest is 0.999, appearing for Qwen-2.5 synthetic commerce and Gemma-3 synthetic commerce and education. Synthetic conditions generally have higher displayed ASR than real conditions. [D] This does not establish the cause of the difference; page generation, content, layout, and sampling may differ.

## Consistency findings

[C] There is a material Phi-4 discrepancy. Table 4's synthetic values sum to 0.997+0.991+0.991+0.985+0.983 = 4.947. Its real values sum to 0.973+0.966+0.936+0.955+0.948 = 4.778. The equal-weight mean across ten datasets is (4.947+4.778)/10 = **0.9725**, whereas Table 1 reports **0.963**. The paper describes Table 1 as averaged across ten datasets. Ordinary rounding of the displayed cells cannot account for this difference. The supplied material does not resolve whether different conditions, a transcription error, or another aggregation were used.

[A/B] A separate dimensions issue occurs between p. 4, which gives an iMac M1 resolution of 4480×2520 as an example, and Figure 6 on p. 15, which labels its raw-pixel example 3200×1556. The LG example is labeled 3840×1916. [D] Physical resolution and captured viewport dimensions could differ, but that explanation is not established in the source. The values should remain separately attributed rather than reconciled silently.

[A] The p. 6 target-prompt generator alternates between GPT-4-Turbo and GPT-4o. Also, §4 optimizes over a prompt set P, while §5.1 describes a perturbation specific to a webpage–prompt–action tuple. [D] The relation between shared-set optimization and per-tuple evaluation is not fully explained. Neither issue removes the reported results, but both limit exact reconstruction of experimental conditions.

# 10. Figure-by-figure interpretation

## Figure 1 — Attack and normal-agent pipelines, p. 2

[B] Two horizontal pipelines contrast a normal page with a perturbed page. Each contains webpage source, browser, raw pixels, monitor, screenshot, and MLLM. Black arrows and a green region mark the normal path; red arrows and a red region mark the attack path. The user requests today's weather. The normal output is click((257,104)); the perturbed path outputs click((869,533)). These are illustration coordinates, not experimental summary values. The attacker is linked to the webpage stage, showing indirect influence on a screenshot rather than local screenshot access. The check and cross communicate intended versus diverted action. This schematic supports the method's attack-surface explanation, not a quantified causal experiment.

## Figure 2 — Aggregate monitor and perturbation studies, p. 8

[B] Panel a is a line plot with number of target monitors on the horizontal axis, labeled 1, 3, and 5, and ASR on a linear vertical axis from 0 to 1. Panel b uses ε labels 4/255, 8/255, 16/255, and 32/255 with the same ASR scale. The legend identifies UI-TARS in red, Phi-4 in blue dashed lines, Llama-3.2 in black dotted lines, Qwen-2.5 in orange patterned lines, and Gemma-3 in green. There are no visible error bars, uncertainty bands, or statistical annotations.

[B] Monitor-count curves decline moderately from near the top of the plot; ε curves rise and converge near 1. [A] Nearby prose interprets those directions as reduced overlap capacity and increased optimization freedom. Exact interior point values are not labeled. Approximate graphical readings are deliberately avoided where the text and tables already convey the substantive result.

## Figure 3 — Monitor-simulation code, p. 13

[B] This is a code illustration, not a plot. It configures headless Chrome with GPU disabled, loads page source, sets a browser window size, uses html2canvas to obtain an encoded image, decodes it, builds an sRGB-to-target-ICC transform with ImageCms, and applies that transform. Width, height, source-code path, and profile path are placeholders. [D] The displayed code refers to `io.BytesIO` without displaying an `io` import and assumes html2canvas is available. These are visible excerpt omissions, not proof that the authors' full implementation failed. Software versions and execution environment details remain absent.

## Figure 4 — Four textual pop-up baselines, p. 14

[B] Four panels share a CONTACT US attention hook, target-coordinate request, and OK banner. The Naive panel directly asks for a click. Context Ignoring adds a request to ignore previous instructions. Fake Completion announces task completion. Combined joins the latter two cues. Colored dashed boxes identify hook, instruction, and banner. The caption locates the banner at the selected target coordinate, illustrated by (525,196). This explains baseline construction. The displayed attack text is evidence to analyze, not an instruction to follow.

## Figure 5 — Perturbed-page appearance, p. 14

[B] Four miniature blog-page screenshots correspond to ε = 4/255, 8/255, 16/255, and 32/255. They retain a broadly similar pink layout with side navigation and central content. Small textual details and pixel-level differences cannot be confidently inspected at this image scale. There are no detection rates, observer counts, or perceptual scores. [D] Similar thumbnail appearance provides a qualitative example; it cannot establish imperceptibility for all pages or viewing conditions.

## Figure 6 — Raw pixels, screenshots, and differences, p. 15

[B] Panels a–c show iMac raw pixels, screenshot, and pixelwise difference; panels d–f show the LG equivalents. The raw-image labels give 3200×1556 and 3840×1916, respectively. The difference images have visibly altered dark color fields. The caption explicitly says differences are color-enhanced for clarity. There is no difference magnitude scale or numerical error metric. This figure supports the existence of differences in the authors' examples; enhanced colors should not be read as actual human-visible distortion magnitude. The dimensions discrepancy with §4.1 remains unresolved.

## Figure 7 — Webpage perturbation implementation, p. 16

[B] The snippet gets canvas image data inside a selected rectangle, iterates through pixel entries, modifies RGB channels, and writes the image data back. It leaves the original-element layering step as an ellipsis and comment. The code advances by four entries per pixel while modifying three channels. [D] The complete perturbation array layout, scaling between normalized optimization values and canvas channel values, and full layering implementation are not established by this excerpt. It explains the implementation concept rather than serving as a complete reproduction artifact.

## Figure 8 — Semantic prompt-generation instruction, p. 16

[B] A boxed instruction requests rephrasing of a target query into a semantically equivalent version. The displayed spelling error does not change its intended role. This is the generation procedure used in X4. It does not supply independent human verification of equivalence or multiple classes of paraphrase difficulty.

## Figure 9 — Synthetic-page generation instruction, p. 18

[B] The boxed instruction asks for realistic category-specific HTML and CSS, grid or flexbox layout, responsive styling, placeholder images, and output containing only page source. This documents what synthetic generation was prompted to produce. It does not measure whether generated pages actually match live-site functionality, diversity, or accessibility.

## Figure 10 — Target-prompt generation instruction, p. 18

[B] The instruction embeds webpage source and requests ten realistic action-oriented questions, avoiding ordinary content question answering and overly direct click or scroll wording. It mentions navigation, tabs, URL visits, shortcuts, and typing. [D] Its example actions are broader than Table 2's listed interface, which does not explicitly list all navigation and tab operations. The paper does not explain how every generated request was reconciled with the evaluated action vocabulary.

## Figure 11 — Monitor-count curves for synthetic data, p. 19

[B] Five panels correspond to blog, commerce, education, healthcare, and portfolio. Each has a linear ASR axis 0–1 and horizontal monitor labels 1, 3, 5, with the five-model legend used in Figure 2. Curves decrease across panels, remaining substantially above the principal textual baselines. No exact point labels or error bars are present. These panels expose category variation that is compressed by the aggregate plot; individual values are not recoverable exactly from the image.

## Figure 12 — Monitor-count curves for real data, p. 19

[B] The same five categories and model encodings appear for real pages. Curves decline with more monitors and show more spread in some panels than the synthetic curves. The plots support the direction described in the text, but exact inter-model differences cannot be confidently transcribed at this scale. These are selected real-page snapshots, not demonstrated live browsing trajectories.

## Figure 13 — Perturbation-bound curves for synthetic data, p. 20

[B] Five category panels plot ε = 4/255, 8/255, 16/255, and 32/255 against ASR on a linear 0–1 scale. All model curves increase toward near-ceiling performance. Model separation is most visible at smaller budgets. No intervals or significance markers appear. The figure supports sensitivity to optimization freedom without providing a perceptual assessment.

## Figure 14 — Perturbation-bound curves for real data, p. 20

[B] The corresponding real-page panels also increase with ε. Lower-budget curves display greater separation and lower starting success in several categories than the synthetic panels. This is a qualitative visual comparison, not an exact numerical extraction. At high budgets the curves approach the plot ceiling. Similar high-budget ASR does not demonstrate equal stealthiness across real and synthetic pages.

# 11. Table-by-table interpretation

All numerical result tables use ASR proportions unless Table 12 explicitly gives minutes and gigabytes. None supplies confidence intervals, standard errors, statistical-test markers, or missing-value notation. Zeros in Table 9 are reported results, not missing values. Dataset columns in Tables 4–9 and 11 are ordered blog, commerce, education, healthcare, portfolio; each model has synthetic and real rows.

## Table 1 — Aggregate attacks, p. 7

[A/B] This table compares four textual page baselines, the adapted screenshot baseline, and WebInject across five models. The full values are reproduced in §9. WebInject is highest for every model. Llama-3.2's strongest textual baseline is Fake Completion at 0.345; UI-TARS's is Context Ignoring at 0.147; Phi-4 and Qwen use Naive at 0.095 and 0.100; Gemma has a Naive/Combined tie at 0.062. The Phi-4 WebInject value conflicts with the equal-weight Table 4 mean.

## Table 2 — Action space, p. 12

[A/B] Ten action forms are listed: click, left_double, right_single, drag, hotkey, type, scroll, wait, finished, and call_user. Rows define coordinate, key-combination, content, or direction arguments. `wait()` sleeps for 5 seconds and takes a screenshot; `finished()` ends the task; `call_user()` requests user help. These functions show that the target space includes task-control outputs as well as webpage manipulation. They should not all be interpreted as equivalent kinds of harm.

## Table 3 — Dataset counts, p. 12

[A/B] Real-page counts vary from 26 commerce pages to 51 healthcare pages; every synthetic category has 100. Counts and derived totals appear in §7. The imbalance means averaging five real datasets equally differs from pooling all real pages equally. The paper describes aggregate averaging across datasets; it does not supply every pooling intermediate.

## Table 4 — Detailed WebInject results, p. 14

[A/B] The complete displayed rows, in category order, are:

- UI-TARS synthetic: 0.992, 0.997, 0.989, 0.986, 0.986; real: 0.962, 0.967, 0.975, 0.954, 0.944.
- Phi-4 synthetic: 0.997, 0.991, 0.991, 0.985, 0.983; real: 0.973, 0.966, 0.936, 0.955, 0.948.
- Llama-3.2 synthetic: 0.993, 0.998, 0.998, 0.984, 0.986; real: 0.961, 0.943, 0.965, 0.941, 0.954.
- Qwen-2.5 synthetic: 0.991, 0.999, 0.988, 0.996, 0.991; real: 0.946, 0.953, 0.940, 0.958, 0.937.
- Gemma-3 synthetic: 0.988, 0.999, 0.999, 0.997, 0.982; real: 0.974, 0.956, 0.929, 0.939, 0.952.

The detailed table reveals both near-ceiling synthetic success and lower real-page cells. It also supplies the reproducible operands for the Phi-4 discrepancy. No individual page distribution is given.

## Table 5 — Naive baseline, p. 15

[A/B] The table's overall minimum is Gemma synthetic blog, 0.011; its maximum is Llama real portfolio, 0.369, narrowly above Llama real blog at 0.368. Per-model displayed ranges are UI-TARS 0.012–0.171, Phi-4 0.054–0.149, Llama 0.142–0.369, Qwen 0.051–0.139, and Gemma 0.011–0.097. These ranges are analyst-selected summaries of exact table cells, not confidence intervals. The baseline's sensitivity differs across backbones and page categories.

## Table 6 — Fake Completion baseline, p. 16

[A/B] The minimum is Phi-4 synthetic blog, 0.012; the maximum is Llama synthetic education, 0.459. Llama's ten displayed values are consistently larger than those of the other models. Per-model ranges are UI-TARS 0.023–0.101, Phi-4 0.012–0.068, Llama 0.163–0.459, Qwen 0.016–0.108, and Gemma 0.013–0.059. This shows that the aggregate Llama vulnerability to this baseline is not limited to one displayed cell.

## Table 7 — Context Ignoring baseline, p. 17

[A/B] The minimum is Phi-4 synthetic healthcare, 0.020; the maximum is Llama synthetic portfolio, 0.383. Per-model ranges are UI-TARS 0.090–0.198, Phi-4 0.020–0.084, Llama 0.133–0.383, Qwen 0.026–0.196, and Gemma 0.029–0.099. The detailed table prevents treating the single aggregate ASR as a uniform response across categories.

## Table 8 — Combined baseline, p. 17

[A/B] The minimum is Phi-4 synthetic blog, 0.001; the maximum is Llama real healthcare, 0.440. Per-model ranges are UI-TARS 0.018–0.095, Phi-4 0.001–0.047, Llama 0.138–0.440, Qwen 0.015–0.108, and Gemma 0.004–0.101. Combining textual cues does not consistently yield the strongest aggregate baseline: Table 1 shows lower Combined than Naive for several models. There is no factorial analysis isolating cue interactions.

## Table 9 — Adapted screenshot baseline, p. 17

[A/B] All 50 model-by-dataset cells are 0.000: five models, two page types, and five categories. This is deliberately compressed rather than reproducing identical cells. The result applies to screenshot-space perturbations directly transferred into raw webpage pixels under §5.1. It does not establish that screenshot perturbations fail when an attacker actually has direct screenshot control.

## Table 10 — Alternative target actions, p. 18

[A/B] Under Phi-4 on synthetic blog pages, left_double is 0.993; right_single 0.980; drag 0.988; hotkey 0.979; type 0.976; scroll 0.982; wait 0.992; finished 0.987; call_user 0.990. Left_double is highest and type lowest among these rows. Coordinate arguments and keyboard combinations are randomly chosen; scrolling chooses among up, down, left, and right. Typing uses selected harmful-query content to represent malicious requests. These results concern action output, not a measured harmful-answer generation rate.

## Table 11 — Semantic prompt variants, p. 21

[A/B] The complete values, in category order, are:

- UI-TARS synthetic: 0.959, 0.932, 0.953, 0.916, 0.949; real: 0.923, 0.906, 0.911, 0.893, 0.902.
- Phi-4 synthetic: 0.947, 0.907, 0.928, 0.952, 0.953; real: 0.936, 0.933, 0.902, 0.889, 0.899.
- Llama-3.2 synthetic: 0.942, 0.929, 0.959, 0.931, 0.947; real: 0.920, 0.903, 0.928, 0.896, 0.897.
- Qwen-2.5 synthetic: 0.910, 0.940, 0.929, 0.955, 0.928; real: 0.890, 0.883, 0.884, 0.921, 0.871.
- Gemma-3 synthetic: 0.957, 0.943, 0.959, 0.918, 0.945; real: 0.917, 0.906, 0.883, 0.903, 0.892.

The minimum is Qwen real portfolio, 0.871. The maximum 0.959 is shared by UI-TARS synthetic blog, Llama synthetic education, and Gemma synthetic education. Every displayed value is below its corresponding Table 4 value. [D] The variant test therefore shows retained but reduced success, rather than equality of performance or unrestricted prompt independence.

## Table 12 — Computational overhead, p. 21

[A/B] For UI-TARS, Phi-4, Llama, Qwen, and Gemma respectively, extra time is 1.92, 2.18, 2.57, 2.07, and 1.70 minutes; extra GPU memory is 1.93, 1.99, 2.61, 2.10, and 2.18 GB. The table writes total values as Δ plus the time increment and Ω plus the memory increment, where Δ and Ω belong to the adapted screenshot baseline. Llama has the largest increments on both measures; Gemma has the smallest time increment; UI-TARS the smallest memory increment. Absolute baseline values and cost variability are absent.

# 12. Diagram / Architecture Interpretation

[B] Figure 1 supplies the only explicit pipeline diagram. Its data path is source code → browser rendering → raw pixels → monitor transformation → screenshot → MLLM → action. The attack's entry point is the source-code stage. The attack path continues through the same downstream components, explaining why screenshot access is unnecessary under the authors' construction.

[A] Combining §§4.1–4.3 with Algorithm 1 yields two phases. During preparation, target-page raw pixels and ICC-converted samples train monitor mapping networks. During attack optimization, a candidate perturbation passes through those networks and differentiable resizing into the victim model's action loss. The gradient returns to δ, which is updated, clamped, and masked. During deployment, webpage code applies the optimized δ to the rendered page, while original interactive elements remain on a transparent upper layer.

[D] This synthesis is an analyst reconstruction from separately supplied components, not a second architecture figure in the paper. There is no visible architecture diagram specifying model-serving interfaces, browser permissions, deployment packaging, synchronization with dynamic content, or error recovery. The iterative feedback loop is the optimization loop; the experiments do not provide a separate demonstrated live attack feedback loop following each executed user action.

# 13. Equations and mathematical concepts

## Notation and system identities

[A] ω is source code; ω′ is the modified source; d is a monitor; I(ω,d) is raw rendered RGB pixels; I_s(ω,d) is screenshot pixels; ICC_d is the monitor profile; M is the screenshot mapping; r is ordinary resizing; r′ is its differentiable substitute; f is the MLLM; p is a user prompt; a is an action string; a* is the attack target; H is one history; P, D, and ℋ are prompt, monitor, and shadow-history sets; δ is the perturbation; ε bounds its magnitude; α is the attack learning rate; T is iteration count; N_d is a learned monitor mapping; S is a binary spatial mask.

[A] The system identities are I_s(ω,d) = M(I(ω,d),ICC_d) and a_t = f(p,r(I_s(ω,d)),H_t). They connect environmental rendering to model decisions. History H_t = [a_1,…,a_(t−1)] contains previous actions, not previous full observations. The implementation target is I(ω′,d) = I(ω,d)+δ. That equality describes the desired rendering effect, not a separately reported numerical fidelity measurement.

## Equation (1), p. 3 — Probability of an action string

[A] For a tokenized action a = [e_1,…,e_n], the probability is:

`Pr(a | [p,r(I_s(ω,d)),H]) = product over q=1…n of Pr(e_q | [p,r(I_s(ω,d)),H,[e_1,…,e_(q−1)]])`.

Each token's probability is conditioned on the prompt, screenshot, history, and preceding action tokens. The product gives the likelihood of the complete requested action, including its function name and arguments. This connects a textual model output to a targeted optimization objective. It does not itself measure whether the browser executes that action or its ultimate effect.

## Equation (2), p. 4 — Target-action loss

[A] The loss sums `−log Pr(a* | [p,r(M(I(ω,d)+δ,ICC_d)),H])` over p∈P, d∈D, and H∈ℋ. A high target-action probability produces a smaller negative logarithm, so minimizing the sum promotes the requested action across the selected conditions. Inputs are the fixed page/configurations and changing δ; output is a scalar loss. Summing conditions encourages shared effectiveness but provides no proof that every condition individually achieves a minimum success rate.

## Equation (3), p. 5 — Constrained source-pixel optimization

[A] The optimization minimizes Equation (2) over δ subject to `||δ||∞ ≤ ε` and `δ_xy = 0` outside `[0,w_δ]×[0,h_δ]`. The infinity norm is the maximum absolute perturbation element. The common-region dimensions are `w_δ = min over d∈D of w_d` and `h_δ = min over d∈D of h_d`. The magnitude constraint represents the paper's stealthiness proxy; the support constraint keeps perturbation entries inside all selected viewing areas. Neither is a theorem proving imperceptibility or universal success.

## Equation (4), p. 5 — Differentiable surrogate optimization

[A] The objective replaces `r(M(I+δ,ICC_d))` with `r′(N_d(I+δ))`, retaining both constraints. This lets gradients flow from the model's action likelihood back through resizing and a learned mapping to δ. The method's success depends in part on how well these surrogates approximate the transformations used at evaluation. The supplied work does not report mapping-network approximation errors or interpolation-fidelity measurements.

## Unnumbered update rules, pp. 5–6

[A] Initialize δ=0. At each iteration obtain g, the gradient of the minibatch loss, and update `δ ← δ−αg`. Clamp with `Clamp(δ,ε)=min(max(δ,−ε),ε)`, applied elementwise. Apply `δ ← S⊙δ`, where ⊙ denotes elementwise multiplication and S is one inside the common rectangle and zero outside. Together, clamp and mask project the candidate back into the allowed set. Algorithm 1 shows ordinary gradient subtraction; it does not show a sign-gradient update, so a sign operation should not be silently inserted.

## Equation (5), p. 7 — Attack success rate

[A] For a page–prompt–target-action triple, `ASR = (1/|D|) sum over d∈D of 1{f(p_ω,r(M(I(ω,d)+δ,ICC_d)),H_ω)=a*_ω}`. The indicator is one for exact action equality and zero otherwise. This yields the fraction of selected monitors that produce the chosen action for the specified prompt and history. Dataset ASR averages across pages, prompts, and evaluation histories. Equality is stricter than merely producing a vaguely related action, but narrower than verifying downstream harmful execution.

[A] There are no mathematical proofs of optimality, convergence rate, perturbation imperceptibility, or monitor-generalization guarantees. The equations formalize the attack and metric; evidence of effectiveness is empirical.

# 14. Interpretation and discussion

[A] The results support the authors' central claim that their implemented attack can strongly bias exact action output under selected white-box conditions. They also show that the proposed page-space approach substantially exceeds the adapted baselines in those conditions. [D] A useful mechanism-level interpretation is that the model's visual observation is an adversarial input channel whose content can affect operational decisions even without a readable malicious instruction.

[D] For the broader research question, the work identifies three relevant features of web-agent operation. First, the agent repeatedly observes an environment controlled partly by other parties. Second, observation contains rendered visual material, creating an attack route beyond explicit instruction text. Third, the model emits operational actions, so misdirection can target clicking, typing, or task termination. The paper's experiment demonstrates this route; it does not measure how frequently a standalone LLM fails under a matched attack, nor whether each feature independently causes a higher vulnerability rate.

[A] The authors attribute superiority to optimization rather than heuristic prompts and to accounting for webpage-to-screenshot mapping. [D] That explanation is plausible within their study, but the evaluation does not isolate all method components. The zero screenshot-baseline results are conditional on transferring screenshot perturbations into raw page pixels, which intentionally differs from the threat model of an attacker who could directly alter screenshots.

The source-grounded consistency check found clear strengths and unresolved points. Dataset counts are internally usable and all numbered visual objects are supplied. Table 1's Gemma example matches the text. Table 11's Gemma synthetic-blog 0.957 matches the discussion. Table 10's narrower Phi-4/synthetic-blog scope is stated in the text. However, Phi-4 aggregate ASR, prompt-generator identity, iMac dimensions, and prompt-set versus per-tuple optimization remain unresolved. The prose's statistical significance language has no accompanying tests. These qualifications prevent strengthening reported success into a general security guarantee or general ranking of model classes.

# 15. Contributions and novelty

- **Conceptual [A]:** A webpage-based attack that manipulates visual observations without explicit textual prompt injection. The authors call it the first effective, stealthy, and practical such attack; this priority claim is not externally verified here.
- **Methodological [A]:** Optimize perturbations in raw webpage-pixel space while incorporating the paper's monitor-specific screenshot mapping.
- **Algorithmic [A]:** Use learned U-Net mapping networks, differentiable resizing, and constrained PGD to obtain the perturbation.
- **Implementation [A]:** Inject page code that modifies pixels while retaining original interactive elements as a transparent top layer.
- **Cross-configuration [A]:** Constrain a shared target-page perturbation to selected monitors' common visible rectangle.
- **Dataset/evaluation [A]:** Construct ten real/synthetic category datasets and compare five model backbones, four textual page baselines, and an adapted screenshot baseline.
- **Empirical [A]:** Report high ASR, semantic-variant retention, alternative-action success, monitor/budget trends, and incremental resource costs.

[D] This is not a theoretical guarantee, a standalone-LLM benchmark, or a validated defense contribution. Dataset construction is part of the study, but no public dataset release or benchmark adoption is established by the supplied pages.

# 16. Limitations

## Authors' stated limitations

[A] The attacker must be able to modify target-page source code. The authors say this assumption may not apply to highly trustworthy sites and give Amazon as an example. That is their limitation statement, not an assurance that any particular site cannot be compromised.

[A] Transferability to closed-source MLLMs was not evaluated. The authors state that obtaining high transferability typically requires multiple surrogate models and that their computational resources were insufficient. Thus the five tested backbones do not establish attack effectiveness against inaccessible proprietary models.

## Additional evidence-based analyst observations

[D] Stealthiness is operationalized mainly through a perturbation norm and a few displayed page examples, without a supplied human observer study. The real-page sample consists of stored snapshots across five categories, with no documented sampling framework. Histories are random simulated action sequences rather than collected user sessions. The main endpoint is action-string output, not full task compromise. These narrow the meaning of effectiveness and realism.

[D] Important reproduction details are absent: seeds, mapping-data splits, exact resizing settings, mapping error, complete injected-page code, generation-model resolution, and shared-cost allocation. No live dynamic-content stress test, unmatched prompt distribution, unseen-monitor test, or defense experiment is reported. The Phi-4 table disagreement specifically limits confidence in that aggregate number, while the other table results can still be described as reported.

# 17. Threats to validity

The following validity categories are analyst interpretations, not labels used by the authors.

- **Internal validity [D]:** Full-method comparisons do not separately isolate the mapping network, resizing surrogate, mask, and optimization. Baseline adaptations and unresolved Phi-4 aggregation affect attribution and exact comparison.
- **External validity [D]:** Findings apply to the listed open models, selected pages, monitors, prompts, and action interface. Closed-source transfer and arbitrary unseen configurations remain untested.
- **Construct validity [D]:** Exact-action ASR is a clear measure of induced output, but differs from harmful task completion. A bounded pixel perturbation differs from measured human imperceptibility.
- **Statistical conclusion validity [D]:** Large observed differences are visible, but variance, repeated runs, and significance testing are absent. The supplied work cannot support an independently assessed confidence interval around the reported averages.
- **Ecological validity [D]:** Generated prompts, synthetic pages, snapshots, and random histories may differ from naturally evolving browsing sessions. The study does not quantify that mismatch.
- **Reproducibility [D]:** Several equations and hyperparameters are explicit, but code excerpts and missing configuration details prevent exact reproduction from the paper alone.
- **Generalizability [D]:** Semantic variants retain high success, but the evidence concerns similarity to optimized requests. It does not show unconstrained task independence or a perturbation shared across all models and sites.

# 18. Future work and open questions

## A. Explicitly proposed by the authors

[A] The limitations section identifies broader attacker applicability and transferability to closed-source models as future directions. It suggests detecting injected or abnormal source code, detecting adversarial perturbations in screenshots, and adversarially fine-tuning MLLMs. These are proposals, not tested defenses. The authors also argue that a textual prompt-injection detector such as DataSentinel is inapplicable to their setting because the attack lacks explicit textual prompts. This is their stated assessment; no supplied comparative detector experiment verifies it.

## B. Additional open questions from this analysis

[D] How much of the gain comes specifically from mapping approximation versus other design choices? How accurately does N_d approximate actual evaluation transformations? Does success survive realistic multi-step histories, scrolling, dynamic layout changes, and unseen viewport configurations? Can small perturbations evade human scrutiny under controlled testing? How often does exact action output become a consequential completed operation? What are the total and amortized costs of preparing attacks across pages?

[D] For the user's research question, a matched experiment would be needed to compare standalone and web-agent deployments using comparable models, adversary access, tasks, and outcome definitions. The supplied paper motivates that question but cannot answer the comparative part on its own. Resolution of the Phi-4 discrepancy and generation/configuration ambiguities is also needed before using the study as a precise reproduction target.

# 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| LLM | Large language model; generates language or textual outputs |
| MLLM | Multimodal large language model; here receives text and screenshot information |
| Web agent | Model-backed system that chooses actions while interacting with a webpage |
| Prompt injection | Attacker-origin input redirects behavior away from the intended task |
| Target webpage, ω | Page whose source code the attacker controls |
| Modified webpage, ω′ | Source code after implementation of the attack |
| Target action, a* | Exact action string the attacker wants the model to produce |
| Target prompt set, P | Requests selected to resemble user tasks on the page |
| Monitor set, D | Selected display configurations used in optimization/evaluation |
| Shadow histories, ℋ | Simulated previous-action sequences used during optimization |
| User history, H_ω | Separately sampled evaluation sequence of previous actions |
| I(ω,d) | Raw RGB pixel tensor rendered for page and display |
| I_s(ω,d) | Screenshot pixel tensor in the authors' system model |
| ICC profile | Monitor-associated color transformation information |
| M | Mapping from raw pixels to screenshot pixels |
| N_d | Learned approximation to M for monitor d |
| r, r′ | Ordinary resizing and differentiable resizing substitute |
| δ | Small pixel change optimized by the attacker |
| ε | Maximum allowed absolute elementwise perturbation |
| ℓ∞ norm | Largest absolute entry in the perturbation |
| w_δ, h_δ | Minimum widths/heights across target monitors |
| S | Binary mask keeping changes inside the common region |
| PGD | Projected gradient descent: update, then enforce constraints |
| α, g, T | Attack learning rate, loss gradient, and iteration count |
| U-Net | Neural-network architecture selected for mapping equal-size image tensors |
| ASR | Attack success rate; fraction of evaluated cases producing the exact target action |
| Indicator, 1{…} | Value one if the enclosed condition is true, zero otherwise |
| ⊙ | Elementwise multiplication, used for spatial masking |
| Δ, Ω | Screenshot-baseline time and GPU memory in Table 12 |
| Universal perturbation | Shared target-page perturbation across selected conditions; not demonstrated universal across all pages/models |

# 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Real page counts | 50, 26, 42, 51, 43 | pages | Blog through portfolio | Author-reported | p. 12, T3 |
| Synthetic pages/category | 100 | pages | Five categories | Author-reported | p. 12, T3 |
| Total real pages | 212 | pages | Sum of five real counts | Analyst-derived | p. 12, T3 |
| Total supplied dataset pages | 712 | pages | 212+5×100 | Analyst-derived | p. 12, T3 |
| Target prompts/page | 10 | prompts | Source-conditioned generation | Author-reported | p. 6, §5.1 |
| Histories per set/page | 10 | histories | Shadow and evaluation sets | Author-reported | p. 6, §5.1 |
| Actions/history | 3–5 | actions | Randomly sampled histories | Author-reported | p. 6, §5.1 |
| Default ε | 16/255 | pixel perturbation scale | ℓ∞ constraint | Author-reported | p. 7, §5.1 |
| Attack α and T | 0.3; 2,500 | learning rate; iterations | PGD | Author-reported | p. 7, §5.1 |
| Mapping training pairs | 16,240 | pairs | Per target-monitor mapping training | Author-reported | p. 8, §5.1 |
| Mapping epochs/rate/batch | 200; 0.005; 16 | epochs; rate; samples | Mapping network | Author-reported | p. 8, §5.1 |
| UI-TARS WebInject | 0.975 | ASR proportion | Ten-dataset Table 1 aggregate | Visually readable | p. 7, T1 |
| Phi-4 WebInject | 0.963 | ASR proportion | Table 1, unresolved inconsistency | Visually readable | p. 7, T1 |
| Phi-4 Table 4 mean | 0.9725 | ASR proportion | Equal-weight displayed cells | Analyst-derived | p. 14, T4 |
| Llama/Qwen/Gemma | 0.972; 0.970; 0.972 | ASR proportion | Table 1 WebInject | Visually readable | p. 7, T1 |
| Gemma strongest baseline | 0.062 | ASR proportion | Naive/Combined tie | Visually readable | p. 7, T1 |
| Gemma gain | 0.910 | absolute ASR difference | 0.972−0.062; 91.0 percentage points | Author-reported | pp. 2, 7–8 |
| Adapted screenshot cells | 0.000 | ASR proportion | All 50 detailed cells | Visually readable | p. 17, T9 |
| WebInject detailed extrema | 0.929–0.999 | ASR proportion | Across Table 4 cells | Visually readable | p. 14, T4 |
| Semantic-variant extrema | 0.871–0.959 | ASR proportion | Across Table 11 cells | Visually readable | p. 21, T11 |
| Gemma synthetic-blog variant | 0.957 | ASR proportion | Compared with target-prompt 0.988 | Author-reported | p. 9; p. 21, T11 |
| Gemma prompt-variant drop | 0.031 | absolute ASR difference | 0.988−0.957 | Analyst-derived | pp. 14, 21 |
| Alternative-action extrema | 0.976–0.993 | ASR proportion | Phi-4, synthetic blog | Visually readable | p. 18, T10 |
| Extra time | 1.70–2.57 | minutes | Per page/monitor on RTX A6000 | Visually readable | p. 21, T12 |
| Extra GPU memory | 1.93–2.61 | GB | Relative to screenshot baseline | Visually readable | p. 21, T12 |
| Monitor-count conditions | 1, 3, 5 | monitors | Plotted ablation | Visually readable | pp. 8, 19 |
| ε conditions | 4/255, 8/255, 16/255, 32/255 | perturbation scale | Plotted ablation | Visually readable | pp. 8, 20 |

Extrema summarize displayed cells, not uncertainty intervals. No exact unlabeled plot values are inserted into this ledger.

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Webpage modification can induce selected actions | Formal construction and high reported exact-action ASR | ALG1, X1, T1/T4 | pp. 4–8, 12, 14 | HIGH for reported selected conditions; no external replication |
| Mapping awareness is central to the design | Learned N_d and surrogate loss | E4, F3, X1 | pp. 5, 13 | HIGH for method; component-specific causal gain not isolated |
| WebInject exceeds listed baselines | Aggregate ASR gap for every model | T1, X1 | p. 7 | HIGH for displayed comparison; Phi aggregate unresolved |
| Screenshot-to-page transfer baseline fails here | Every detailed ASR cell is zero | T9, X1 | p. 17 | HIGH, conditional on §5.1 adaptation |
| Selected multi-monitor optimization retains high success | Declining but high curves | F2a, F11/F12, X2 | pp. 8, 19 | MEDIUM for exact graphical magnitudes; no unseen-display guarantee |
| Larger budgets increase success | Monotonic upward plotted trends and prose | F2b, F13/F14, X3 | pp. 8, 20 | HIGH for direction; not a perceptual study |
| Semantic variants retain substantial success | T11 0.871–0.959; Gemma example 0.957 | T11, X4 | pp. 9, 21 | HIGH for generated variants; lower than corresponding T4 cells |
| Other actions can be targeted | Nine ASRs 0.976–0.993 | T10, X5 | pp. 9, 18 | HIGH for Phi-4/synthetic blog only |
| Added computation is reported | Incremental minutes and GB | T12, X6 | p. 21 | HIGH for increments; absolute and amortized costs absent |
| Closed-source transfer remains unknown | Explicit limitation | S8 | p. 9 | HIGH as a negative finding |
| Web agents expose an environmental action pathway | Screenshot-conditioned action definition and page-control threat model | S2/S3, F1 | pp. 1–4 | MEDIUM analyst relevance inference; no standalone comparison |
| Stealth is claimed rather than fully perceptually validated | ℓ∞ constraint and example thumbnails | E3, F5 | pp. 4–5, 14 | HIGH for operationalization; no human-detection estimate |

# 22. Very simple explanation — Explain Like I'm 15

Imagine asking an assistant to use a website for you. It looks at a picture of the page and decides where to click or what to type. In this paper, an attacker changes the website so its picture contains tiny, carefully chosen changes. The page can still look broadly normal to a person, but the model becomes much more likely to choose the attacker's action.

The tricky part is that changing a website's pixels is not necessarily the same as changing the final picture the model sees. The researchers account for a color transformation associated with the display and for image resizing. They train a network to imitate part of that process, then repeatedly adjust the tiny changes until the chosen action becomes likely. Finally, they put code into the webpage to display those changes.

Their tests report very high success on five model backbones under the conditions they selected. But the attacker needs control of the page and access to the model parameters. The tests mainly ask whether the model outputs the exact chosen action; they do not prove that every suggested harmful outcome happens. The study also does not compare these agents with ordinary standalone language models. It shows an extra route into an agent's decisions: the website the agent observes can become the attack input.

# Completeness Audit

The audit compares this explanation with the supplied inventory. 'Fully represented' means its substantive role, conditions, and evidence are explained, not that every source word is reproduced. Repetitive cells and bibliography details are compressed explicitly.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes, text and image | Yes | Fully represented | Mechanism, challenge, headline findings |
| §1 Introduction | Yes, text and images | Yes | Fully represented | Motivation and attack taxonomy |
| §2 Background | Yes, text and images | Yes | Fully represented | Rendering, ICC model, agent inputs, token likelihood |
| §3 goals | Yes | Yes | Fully represented | Effectiveness, stealth, prompts, monitors |
| §3 capability | Yes | Yes | Fully represented | Page control, shadow histories |
| §3 background knowledge | Yes | Yes | Fully represented | Model parameters; excluded screenshot/history access |
| §4 overview | Yes | Yes | Fully represented | Pixel-space construction and source implementation |
| §4.1 goals and constraints | Yes | Yes | Fully represented | Loss, magnitude, common rectangle |
| §4.2 challenges and surrogates | Yes | Yes | Fully represented | Mapping network and differentiable resizing |
| §4.2 update/projection | Yes | Yes | Fully represented | Gradient, clamp, mask |
| §4.3 implementation | Yes | Yes | Fully represented | Canvas and transparent original elements; excerpt limits |
| §5.1 dataset collection | Yes | Yes | Fully represented | Sources, categories, counts |
| §5.1 models | Yes | Yes | Fully represented | Full listed model names |
| §5.1 prompts and histories | Yes | Yes | Fully represented | Generation inconsistency, simulation conditions |
| §5.1 metric | Yes | Yes | Fully represented | Exact output equality and averaging |
| §5.1 monitor simulation | Yes | Yes | Fully represented | Physical/simulated displays, default |
| §5.1 baselines | Yes | Yes | Fully represented | Pop-up structure and screenshot adaptation |
| §5.1 parameters | Yes | Yes | Fully represented | Attack and mapping training settings |
| §5.2 main results | Yes | Yes | Fully represented | Aggregate and detailed results; inconsistency |
| §5.2 monitor variation | Yes | Yes | Represented in compressed form | All panels inspected; exact unlabeled values unavailable |
| §5.2 ε variation | Yes | Yes | Represented in compressed form | All panels inspected; exact unlabeled values unavailable |
| §5.2 semantic prompts | Yes | Yes | Fully represented | Conditions, detailed table, drop |
| §5.2 other actions | Yes | Yes | Fully represented | Narrow test scope and every ASR |
| §6 Related Work | Yes | Yes | Represented in compressed form | Categories and attributed shortcomings; citations not validated |
| §7 Conclusion | Yes | Yes | Fully represented | Author novelty claim kept attributed |
| §8 source-control limitation | Yes | Yes | Fully represented | Explicit assumption boundary |
| §8 closed-source transfer limitation | Yes | Yes | Fully represented | Not evaluated |
| §8 proposed defenses | Yes | Yes | Fully represented | Proposals distinguished from experiments |
| §9 Acknowledgments | Yes | Yes | Represented in compressed form | Reviewer thanks and NSF funding noted; grant IDs omitted |
| References, pp. 10–11 | Yes, text only | Partly | Represented in compressed form | Bibliographic function and relevant categories; no citation verification |
| Formal research questions | Not present | Absence represented | Fully represented | Objectives not relabeled as author-numbered questions |
| Formal hypotheses | Not present | Absence represented | Fully represented | No hypothesis tests invented |
| X1 main comparison | Yes | Yes | Fully represented | T1 and detailed tables |
| X2 monitor count | Yes | Yes | Represented in compressed form | Trend and conditions, no fabricated coordinates |
| X3 perturbation bound | Yes | Yes | Represented in compressed form | Trend, budgets, stealth caveat |
| X4 semantic variants | Yes | Yes | Fully represented | T11 values |
| X5 action types | Yes | Yes | Fully represented | T10 values |
| X6 overhead | Yes | Yes | Fully represented | Relative costs and missing absolutes |
| F1 | Yes, visually | Yes | Fully represented | Both pipelines and illustration outputs |
| F2a–b | Yes, visually | Yes | Represented in compressed form | Axes, encodings, trends, no uncertainty bands |
| F3 | Yes, visually | Yes | Fully represented | Code flow and excerpt omissions |
| F4a–d | Yes, visually | Yes | Fully represented | Four textual constructions |
| F5a–d | Yes, visually | Yes | Represented in compressed form | Budget examples; miniature text not transcribed |
| F6a–f | Yes, visually | Yes | Fully represented | Raw/screenshot/difference pairs and dimensions |
| F7 | Yes, visually | Yes | Fully represented | Pixel code and layering omission |
| F8 | Yes, visually | Yes | Fully represented | Semantic-generation role |
| F9 | Yes, visually | Yes | Fully represented | Synthetic-page generation role |
| F10 | Yes, visually | Yes | Fully represented | Target-task generation role |
| F11a–e | Yes, visually | Yes | Represented in compressed form | Synthetic category monitor curves |
| F12a–e | Yes, visually | Yes | Represented in compressed form | Real category monitor curves |
| F13a–e | Yes, visually | Yes | Represented in compressed form | Synthetic category budget curves |
| F14a–e | Yes, visually | Yes | Represented in compressed form | Real category budget curves |
| T1 | Yes, visually and text | Yes | Fully represented | All displayed values |
| T2 | Yes, visually and text | Yes | Fully represented | All action forms and meanings |
| T3 | Yes, visually and text | Yes | Fully represented | All counts |
| T4 | Yes, visually and text | Yes | Fully represented | All values and Phi discrepancy |
| T5 | Yes, visually and text | Yes | Represented in compressed form | Per-model ranges and extrema |
| T6 | Yes, visually and text | Yes | Represented in compressed form | Per-model ranges and extrema |
| T7 | Yes, visually and text | Yes | Represented in compressed form | Per-model ranges and extrema |
| T8 | Yes, visually and text | Yes | Represented in compressed form | Per-model ranges and extrema |
| T9 | Yes, visually and text | Yes | Represented in compressed form | All 50 identical zeros accounted for |
| T10 | Yes, visually and text | Yes | Fully represented | Every action ASR |
| T11 | Yes, visually and text | Yes | Fully represented | All values |
| T12 | Yes, visually and text | Yes | Fully represented | Every time/memory increment |
| E1 | Yes, visually and text | Yes | Fully represented | Token probability product |
| E2 | Yes, visually and text | Yes | Fully represented | Summed target-action loss |
| E3 | Yes, visually and text | Yes | Fully represented | Constraints and common-region definitions |
| E4 | Yes, visually and text | Yes | Fully represented | Surrogate objective |
| E5 | Yes, visually and text | Yes | Fully represented | Exact action ASR |
| Unnumbered system/update equations | Yes | Yes | Fully represented | Screenshot identity, action/history, clamp, mask |
| ALG1 | Yes, visually and text | Yes | Fully represented | Inputs, loop, output, implementation phase |
| Major contributions | Yes | Yes | Fully represented | Claims distinguished from external novelty validation |
| Appendix pp. 12–21 | Yes, text and images | Yes | Represented in compressed form | Every numbered object accounted for |
| Supplementary files/repository | No, not supplied | Absence represented | Missing from supplied material | No inspection or execution claimed |
| Substantive footnotes/theorems | None identified | Absence represented | Fully represented | No unseen content inferred |

## Missing or inaccessible material

No numbered physical page is missing from the supplied text range. Reference pages 10–11 have no supplied visual rendering, so their typography and any rendering-specific details were not visually inspected. No separate dataset, full executable implementation, checkpoint, supplement, underlying plot coordinates, or experimental logs were provided. Absolute screenshot-baseline time/memory, seeds, statistical uncertainty, mapping accuracy, and several reproduction settings are not specified in the supplied document.

## Uncertain interpretations

The Phi-4 Table 1/Table 4 aggregate discrepancy is unresolved. GPT-4-Turbo versus GPT-4o target-prompt generation is unresolved. The iMac resolution versus Figure 6 image-dimension difference is unresolved. Shared prompt-set optimization versus tuple-specific perturbation wording is incompletely explained. Exact plot coordinates, some miniature screenshot text, full source-injection code, perturbation array scaling/layout, and the allocation of mapping-training costs cannot be confidently established. The authors' general screenshot model is reported without outside validation.

## Deliberately compressed material

References are compressed to their role in the authors' positioning. Acknowledgment grant identifiers are omitted as non-substantive to the security analysis. Tables 5–8 are compressed to per-model ranges, extrema, aggregate context, and interpretation rather than repeating all 200 detailed baseline cells. Table 9's 50 zeros are grouped. Figures 11–14 retain every category/panel family and experimental condition, but repetitive curve descriptions and unlabeled coordinates are not transcribed. Miniature webpage body text in Figures 5–6 is secondary to their visual-comparison purpose and is not reconstructed.

## Potential omissions

Every identified substantive numbered figure, table, equation, algorithm, major section, reported experiment, contribution category, and author-stated limitation is represented either directly or with disclosed compression. This does not imply lossless reproduction: individual baseline-table cells, bibliography entries, small webpage content, and exact unprovided plot coordinates are not exhaustively reproduced. No known substantive inventory object is silently omitted, and no absent supplement or standalone-LLM comparison is treated as reviewed evidence.
