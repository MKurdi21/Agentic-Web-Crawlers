# Metadata verification ledger (closed local corpus)

**Audit date:** July 22, 2026
**Scope:** exactly the 48 PDFs represented by the 48 files in `Summaries/` (24 repository-root PDFs, 17 `Security/` PDFs, and 7 `Borderline/` PDFs).
**Network use:** none. This audit did not browse or renew any external verification.

This is a citation-safety ledger, not a finished bibliography. It distinguishes what is visible in the supplied PDF/summary evidence from what the existing local search report says was once checked externally. A URL, venue, or statement in that report is **historical documentation**, not a current web verification and not independent corroboration merely because it is repeated in another local document.

## Evidence hierarchy and status definitions

Evidence is ranked as follows:

1. **L — local paper evidence:** title-page, header, footer, proceedings statement, arXiv/version line, DOI, or other bibliographic text observed in a supplied PDF and recorded in its corresponding summary. The summaries are the audit index; the PDF is the controlling local artifact when the summary records a conflict or omits a consequential detail.
2. **S — local summary evidence:** explicit metadata in the corresponding file in `Summaries/`. This is locally observed metadata, but it is not a second independent source and should not be described as web-verified.
3. **H — historical external-verification record:** a claim or URL preserved in `agentic_ai_web_agents_literature_search_report.md`. It may document a prior official-source check, but it was not rerun here and can be stale.
4. **U — unresolved/current verification need:** a missing field, disagreement, placeholder, preprint-to-proceedings transition, or recent/future publication claim that the closed corpus cannot settle.

Row statuses:

- **LC (local-complete):** the corresponding summary explicitly gives title, authors, year, and venue/source/version. This verifies what the supplied artifact says, not that an external record is current.
- **LH (local + historical supplement):** local inclusion/title/authorship are clear, but at least one citation field (usually year, venue, source, or exact author expansion) comes only from the historical report. Use the noted conservative citation form or recheck externally.
- **CU (conflict/unresolved):** local documents conflict or contain publication placeholders; do not promote the disputed claim without a current authoritative check.

“Title match” below means the summary title and local PDF filename identify the same work; capitalization, punctuation, acronym prefixes, and filename-safe character substitutions are not treated as mismatches. “Included” means both a local PDF and one corresponding summary are present. No row is labeled “web-verified.”

## Exact corpus accounting

| Location | PDFs | Summaries mapped | Ledger rows | Result |
|---|---:|---:|---:|---|
| Repository root (core) | 24 | 24 | 24 (C1–C24) | Complete |
| `Security/` | 17 | 17 | 17 (S1–S17) | Complete |
| `Borderline/` | 7 | 7 | 7 (B1–B7) | Complete |
| **Total** | **48** | **48** | **48** | **48/48 accounted for** |

## Core/root papers (24/24)

| ID | Paper (title match; included) | Year | Venue/source safe to state from this corpus | Author/version ambiguity and citation note | Evidence | Status |
|---|---|---:|---|---|---|---|
| C1 | *Webscraper: Leverage Multimodal Large Language Models for Index-Content Web Scraping* (Yes; Yes) | 2026 | arXiv-era preprint; no peer-reviewed venue locally established | Huang and Joung are explicit locally. Year and arXiv:2603.29161 are supplied only by H; cite as a preprint pending record/version check. | S+H | LH |
| C2 | *WebSailor: Navigating Super-human Reasoning for Web Agent* (Yes; Yes) | 2025 | arXiv preprint (H: 2507.02592) | Nineteen authors are explicit in S. S omits year/source; do not infer a conference venue. | S+H | LH |
| C3 | *WebDancer: Towards Autonomous Information Seeking Agency* (Yes; Yes) | 2025 | arXiv:2505.22648v3, dated Aug. 10, 2025 | Thirteen authors and the exact supplied version are explicit. Cite the version/date if reproducibility matters. | S/L | LC |
| C4 | *WebWalker: Benchmarking LLMs in Web Traversal* (Yes; Yes) | 2025 | ACL 2025, long papers, pp. 10290–10305 | Eleven authors are explicit. Proceedings volume/pages are locally stated. | S/L | LC |
| C5 | *Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge* (Yes; Yes) | 2025 | arXiv preprint (H: 2506.21506) | Twenty-six authors and three equal contributors are explicit in S; S has no publication line. Do not assign a conference. | S+H | LH |
| C6 | *GO-BROWSE: Training Web Agents with Structured Exploration* (Yes; Yes) | 2026 | ICLR 2026 conference paper | Gandhi and Neubig are explicit. Earlier metadata reportedly described a 2025 preprint; cite the supplied ICLR 2026 form but recheck final proceedings details. | S/L; H conflict history | LC |
| C7 | *AutoScraper: A Progressive Understanding Web Agent for Web Scraper Generation* (Yes; Yes) | 2024 | EMNLP 2024, pp. 2371–2389 | Eight authors are explicit. H records ACL Anthology/arXiv URLs but is not needed for the local venue claim. | S/L | LC |
| C8 | *AutoWebGLM: A Large Language Model-based Web Navigating Agent* (Yes; Yes) | 2024 | KDD 2024, Barcelona | Eleven authors are explicit. The local source supports KDD; arXiv:2404.03648 is only historically recorded. | S/L | LC |
| C9 | *GPT-4V(ision) is a Generalist Web Agent, if Grounded* (SeeAct) (Yes; Yes) | 2024 | ICML 2024 only as historically documented | Five authors are explicit; “SeeAct” is the system/project alias, not the paper title. S omits year and venue. | S+H | LH |
| C10 | *WEBLINX: Real-World Website Navigation with Multi-Turn Dialogue* (Yes; Yes) | 2024 | ICML 2024 only as historically documented | Lù, Kasner, and Reddy are explicit. S omits year/venue; retain diacritics. | S+H | LH |
| C11 | *WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models* (Yes; Yes) | 2024 | ACL 2024, pp. 6864–6890 | Eight authors are explicit. Proceedings metadata is locally stated. | S/L | LC |
| C12 | *LASER: LLM Agent with State-Space Exploration for Web Navigation* (Yes; Yes) | 2023 | Preprint/OpenReview-style source only as historically documented | Six authors are explicit. S has no year/venue; H records arXiv:2309.08172 and OpenReview, but no archival venue. | S+H | LH |
| C13 | *ReAct: Synergizing Reasoning and Acting in Language Models* (Yes; Yes) | 2023 | ICLR 2023 conference paper | Seven authors are explicit. The 2022 arXiv posting and 2023 conference year are distinct citation dates; use 2023 for proceedings. | S/L | LC |
| C14 | *WebGPT: Browser-assisted question-answering with human feedback* (Yes; Yes) | 2021 | OpenAI technical report / arXiv preprint | S abbreviates authorship as “Nakano et al.”; H expands the first author to Reiichiro Nakano and records arXiv:2112.09332. Recover the full author list from the PDF before bibliography export. | S+H | LH |
| C15 | *BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents* (Yes; Yes) | 2025 | OpenAI benchmark report; no conference locally established | Ten authors and equal contribution for Wei/Sun are explicit. Year/source are H-only. | S+H | LH |
| C16 | *BEARCUBS: A Benchmark for Computer-Using Web Agents* (Yes; Yes) | 2025 | COLM 2025 | Six authors are explicit. The local summary states COLM; H’s prior OpenReview claim is historical only. | S/L | LC |
| C17 | *MMInA: Benchmarking Multihop Multimodal Internet Agents* (Yes; Yes) | 2025 | Findings of ACL 2025, pp. 13682–13697 | Four authors are explicit. The arXiv posting may be 2024, but the locally stated proceedings year is 2025. | S/L | LC |
| C18 | *The BrowserGym Ecosystem for Web Agent Research* (Yes; Yes) | 2025 | Transactions on Machine Learning Research, Feb. 2025 | S distinguishes three lead authors, core contributors, benchmark contributors, and advisors; do not collapse this contributor structure without checking the paper’s preferred citation. | S/L | LC |
| C19 | *WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks* (local filename omits “++”; Yes) | 2024 | NeurIPS 2024, Datasets and Benchmarks Track | Nine authors are explicit. Treat the root filename as WorkArena++ despite its filename-safe title. | S/L | LC |
| C20 | *WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?* (filename says “WebAgents”; Yes) | 2024 | ICML 2024 | Twelve authors are explicit. Minor filename spacing is not a title conflict. | S/L | LC |
| C21 | *VisualWebArena: Evaluating Multimodal Agents on Realistic Visually Grounded Web Tasks* (Yes; Yes) | 2024 | ACL 2024, pp. 881–905 | Ten authors are explicit; S also records five equal contributors. Preserve that note if required by citation style. | S/L | LC |
| C22 | *WebArena: A Realistic Web Environment for Building Autonomous Agents* (Yes; Yes) | 2024 | ICLR 2024 conference paper | Twelve authors are explicit. | S/L | LC |
| C23 | *Mind2Web: Towards a Generalist Agent for the Web* (Yes; Yes) | 2023 | NeurIPS 2023, Datasets and Benchmarks Track | Eight authors are explicit. | S/L | LC |
| C24 | *WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents* (Yes; Yes) | 2022 | NeurIPS 2022 | Four authors are explicit. | S/L | LC |

## Security papers (17/17)

| ID | Paper (title match; included) | Year | Venue/source safe to state from this corpus | Author/version ambiguity and citation note | Evidence | Status |
|---|---|---:|---|---|---|---|
| S1 | *WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections* (Yes; Yes) | 2026 | arXiv preprint (H: 2605.15030); no archival venue locally established | Eleven authors are explicit. S omits year/source, so both are historical supplements. | S+H | LH |
| S2 | *Identifying AI Web Scrapers Using Canary Tokens* (Yes; Yes) | 2026 | arXiv preprint (H: 2605.13706); no archival venue locally established | Six authors are explicit. S omits year/source. | S+H | LH |
| S3 | *When AI Meets the Web: Prompt Injection Risks in Third-Party AI Chatbot Plugins* (Yes; Yes) | 2026 | Accepted to IEEE Symposium on Security and Privacy 2026 | Six authors are explicit. Local wording is “accepted,” not necessarily final proceedings publication; check pagination/DOI before final citation. | S/L | LC |
| S4 | *Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems* (Yes; Yes) | 2026 | USENIX Security 2026 only as historically documented | Four authors are explicit. S omits year/venue; H supplies the venue claim. Use “preprint/manuscript” if an external recheck is impossible. | S+H | LH |
| S5 | *Prompt Injection Attack to Tool Selection in LLM Agents* (ToolHijacker) (Yes; Yes) | 2026 | NDSS 2026 | Six authors are explicit. “ToolHijacker” is an attack/framework alias used in local documents, not part of the title. | S/L | LC |
| S6 | *Attention Is All You Need to Defend Against Indirect Prompt Injection Attacks in LLMs* (RENNERVATE) (Yes; Yes) | 2026 | NDSS 2026 | Six authors are explicit. RENNERVATE is the method alias; cite the full paper title. | S/L | LC |
| S7 | *AWE: Adaptive Agents for Dynamic Web Penetration Testing* (Yes; Yes) | 2026 | LAST-X workshop, Feb. 27, 2026 | Jaswal and Baghel are explicit. This is the Workshop on LLM Assisted Security and Trust Exploration, not an NDSS main-conference paper. | S/L | LC |
| S8 | *ACE: A Security Architecture for LLM-Integrated App Systems* (Yes; Yes) | 2026 | NDSS 2026 | Six authors are explicit. | S/L | LC |
| S9 | *Unsafe LLM-Based Search: Quantitative Analysis and Mitigation of Safety Risks in AI Web Search* (Yes; Yes) | 2025 | 34th USENIX Security Symposium | Seven authors are explicit. | S/L | LC |
| S10 | *WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks* (Yes; Yes) | 2025 | NeurIPS 2025, Datasets and Benchmarks Track | Five authors are explicit; S notes Grattafiori’s independent-researcher/current-versus-work-done-at-Meta distinction. | S/L | LC |
| S11 | *SAFEARENA: Evaluating the Safety of Autonomous Web Agents* (Yes; Yes) | 2025 | ICML 2025, PMLR 267 | Nine authors are explicit. Preserve capitalization only stylistically; “SafeArena” and “SAFEARENA” identify the same work. | S/L | LC |
| S12 | *YURASCANNER: Leveraging LLMs for Task-driven Web App Scanning* (Yes; Yes) | 2025 | NDSS 2025 | Five authors are explicit. | S/L | LC |
| S13 | *ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents* (Yes; Yes) | 2026 | ICLR 2026 conference paper | Seven authors are explicit. H records an earlier 2024 arXiv identity; cite the supplied 2026 conference version and recheck final version/task counts if quoting them. | S/L; H version history | LC |
| S14 | *Formalizing and Benchmarking Prompt Injection Attacks and Defenses* (Yes; Yes) | 2024 | 33rd USENIX Security Symposium | Five authors are explicit. | S/L | LC |
| S15 | *Not What You’ve Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection* (Yes; Yes) | 2023 | 16th ACM AISec workshop, Nov. 30, 2023 | Six authors are explicit. AISec is a workshop, not ACM CCS main conference. | S/L | LC |
| S16 | *How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation* (SearchGEO) (Yes; Yes) | 2026 | arXiv preprint (H: 2606.16821); no archival venue locally established | Six authors are explicit. “SearchGEO” is a benchmark/system alias. S omits year/source; H previously recorded v2 dated June 23, 2026, but that version was not rechecked here. | S+H | LH |
| S17 | *One Polluted Page Is Enough: Evaluating Web Content Pollution in Generative Recommenders* (FORGE) (Yes; Yes) | 2026 | arXiv preprint (H: 2606.13610); no archival venue locally established | Luo and Chen are explicit. “FORGE” is the benchmark alias. S omits year/source; H previously recorded submission June 11, 2026. | S+H | LH |

## Borderline papers (7/7)

| ID | Paper (title match; included) | Year | Venue/source safe to state from this corpus | Author/version ambiguity and citation note | Evidence | Status |
|---|---|---:|---|---|---|---|
| B1 | *Toolformer: Language Models Can Teach Themselves to Use Tools* (Yes; Yes) | 2023 | NeurIPS 2023 only as historically documented | Eight authors are explicit. S omits year/venue; distinguish any 2022 preprint date from the reported 2023 proceedings year. | S+H | LH |
| B2 | *Gorilla: Large Language Model Connected with Massive APIs* (Yes; Yes) | 2024 | NeurIPS 2024 | Four authors are explicit. | S/L | LC |
| B3 | *AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents* (Yes; Yes) | 2025 | ICLR 2025 conference paper | Fifteen authors are explicit. A 2024 preprint may coexist with the 2025 conference version; use 2025 for proceedings. | S/L | LC |
| B4 | *EvoCrawl: Exploring Web Application Code and State using Evolutionary Search* (Yes; Yes) | 2025 | NDSS 2025 | Four authors are explicit. This is locally clear despite an older ledger’s stale “unclear” label. | S/L | LC |
| B5 | *BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents* (Yes; Yes) | 2026 | Findings of ACL 2026, pp. 16115–16127 | Nine authors are explicit. H records DOI 10.18653/v1/2026.findings-acl.791, but it was not renewed here. | S/L | LC |
| B6 | *SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems* (Yes; Yes) | 2026 | ICML 2026, PMLR 306 | Nine authors and equal contribution for Feng/Ding are explicit. The final PMLR landing record/pagination remains worth checking. | S/L | LC |
| B7 | *Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation* (Yes; Yes) | 2026 | **Unresolved:** S labels it ACM TOSEM, Jan. 2026; earlier ledger notes describe arXiv:2606.10749 and placeholder TOSEM metadata | Ling, Yu, Chen, and Fang are explicit. Do not cite as an accepted/published TOSEM article until an authoritative record resolves the placeholder-versus-publication conflict; safest current local form is manuscript/preprint. | S+H conflict | CU |

## Status totals and consistency checks

| Status | Core | Security | Borderline | Total |
|---|---:|---:|---:|---:|
| LC — local-complete | 15 | 13 | 5 | **33** |
| LH — local + historical supplement | 9 | 4 | 1 | **14** |
| CU — conflict/unresolved | 0 | 0 | 1 | **1** |
| **All rows** | **24** | **17** | **7** | **48** |

Additional checks:

- All 48 rows have a same-work title match and both a local PDF and summary; there are no search-only items in this ledger.
- All 48 rows state a year, but 14 rows obtain at least one essential citation field from H and therefore still need authoritative rechecking before high-stakes citation.
- Exactly one row (B7) contains a material local publication-status conflict.
- Alias handling is explicit for SeeAct, ToolHijacker, RENNERVATE, SearchGEO, FORGE, and WorkArena++.
- Workshop/main-conference distinctions are explicit for AWE and the AISec paper.

## Prioritized rechecks

### Priority 1 — citation-blocking

1. **B7 Toward Secure LLM Agents:** resolve arXiv/manuscript versus accepted/published ACM TOSEM status; obtain a non-placeholder DOI, volume, issue, pages/article number, and authoritative publication date before citing it as TOSEM.
2. **C14 WebGPT:** recover the full author list and preferred technical-report/arXiv citation from the supplied PDF or an authoritative record; the summary only says “Nakano et al.”
3. **All LH rows:** renew the H-only year/source or venue claim before describing it as externally verified: C1, C2, C5, C9, C10, C12, C14, C15, S1, S2, S4, S16, S17, and B1.

### Priority 2 — recent version/proceedings transitions

1. **GO-BROWSE and ST-WebAgentBench:** reconcile earlier preprint years with the supplied ICLR 2026 versions and capture final proceedings metadata.
2. **When AI Meets the Web:** convert “accepted to IEEE S&P 2026” to a proceedings citation only after pages/DOI are available.
3. **SkillTrojan and BackdoorAgent:** confirm final PMLR/ACL landing metadata and pagination/DOI; locally stated venues remain usable as supplied-paper metadata.
4. **SearchGEO, FORGE, WARD, Canary Tokens, WebSailor, Webscraper, Mind2Web 2, and LASER:** check for later versions or archival publication; until then cite conservatively as preprints where the source is known.

### Priority 3 — attribution and formatting

1. **BrowserGym:** use the paper’s preferred citation author list rather than treating all locally described contributor groups as equivalent authors.
2. Preserve diacritics (`Lù`, `Zdeněk`, `Dessì`, `Jürgen`) and recorded equal-contribution notes where the chosen citation style supports them.
3. Use full titles in citations; treat SeeAct, RENNERVATE, ToolHijacker, SearchGEO, and FORGE as aliases unless an authoritative citation record incorporates them.

## Safe-use rule

For a bibliography built without further browsing, cite LC rows exactly as metadata observed in the supplied artifact, while making clear that this is local-paper evidence. For LH rows, cite only the conservative source type stated above and do not call the venue/year externally verified. For CU, do not use the disputed venue claim. Any later external check should record the authoritative URL, access date, version identity, and the exact field it resolves rather than replacing uncertainty with an unqualified “verified” label.
