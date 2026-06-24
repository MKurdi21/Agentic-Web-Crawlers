# Metadata and Venue Verification Notes

This file tracks venue/source confidence for the 43 local PDFs. It is not a formal bibliography. Use it to decide what needs re-checking before citation.

Verification status values:

- `Verified from local PDF`
- `Verified from existing search report`
- `Needs web verification`
- `Unclear from local PDF`
- `Potential mismatch`

Targeted official-source checks were performed for unstable/recent items including Go-Browse, BEARCUBS, ST-WebAgentBench, AWE, EvoCrawl, AutoWebGLM, SafeArena, and WARD. Where the existing search report and a later official source differ, the table flags that explicitly.

| Paper | Local PDF title match? | Year | Venue/source in README | Verification status | Notes |
|---|---|---:|---|---|---|
| AutoScraper | Yes | 2024 | EMNLP 2024 | Verified from existing search report | Search report points to ACL Anthology/EMNLP. Re-check only for final citation formatting. |
| AutoWebGLM | Yes | 2024 | KDD 2024 / arXiv | Verified from existing search report | Targeted web check found ACM DOI page for KDD metadata and arXiv page. |
| BEARCUBS | Yes | 2025 | COLM 2025 | Verified from existing search report | Targeted OpenReview check confirms COLM 2025; arXiv page remains preprint source. |
| BrowseComp | Yes | 2025 | OpenAI / arXiv-style report | Verified from existing search report | OpenAI technical benchmark/report; no conference venue inferred. |
| Go-Browse | Yes | 2026 | ICLR 2026 | Potential mismatch | Existing search report listed 2025 OpenReview/workshop-style preprint. Targeted OpenReview/arXiv PDF check indicates ICLR 2026 conference paper. Verify before formal citation. |
| SeeAct / GPT-4V(ision) is a Generalist Web Agent, if Grounded | Yes | 2024 | ICML 2024 | Verified from existing search report | Search report lists official project/arXiv and ICML venue. |
| LASER | Yes | 2023 | arXiv / OpenReview | Verified from existing search report | Venue remains preprint/OpenReview-style in current repo metadata. |
| Mind2Web 2 | Yes | 2025 | arXiv | Verified from existing search report | Treat as preprint unless a later venue is verified. |
| Mind2Web | Yes | 2023 | NeurIPS 2023 Datasets and Benchmarks | Verified from existing search report | Search report points to NeurIPS proceedings. |
| MMInA | Yes | 2025 | Findings of ACL 2025 | Verified from existing search report | Search report points to ACL Anthology. |
| ReAct | Yes | 2023 | ICLR 2023 | Verified from existing search report | Well-established venue; search report cites official/publication sources. |
| BrowserGym | Yes | 2025 | TMLR / OpenReview | Verified from existing search report | Search report lists TMLR/OpenReview. |
| VisualWebArena | Yes | 2024 | ACL 2024 | Verified from existing search report | Search report points to ACL Anthology. |
| WebArena | Yes | 2024 | ICLR 2024 | Verified from existing search report | Search report points to OpenReview/ICLR. |
| WebDancer | Yes | 2025 | arXiv / OpenReview | Verified from existing search report | Treat as preprint/OpenReview unless a peer-reviewed venue is later confirmed. |
| WebGPT | Yes | 2021 | OpenAI / arXiv | Verified from existing search report | Technical report/preprint status. |
| WebLINX | Yes | 2024 | ICML 2024 | Verified from existing search report | Search report lists official project/arXiv and ICML. |
| WebSailor | Yes | 2025 | arXiv | Needs web verification | Search report lists arXiv preprint. Year appears future relative to some common citation flows; verify latest version before citing. |
| Webscraper | Yes | 2026 | arXiv | Verified from existing search report | Treat as preprint. |
| WebShop | Yes | 2022 | NeurIPS 2022 | Verified from existing search report | Search report points to NeurIPS proceedings. |
| WebVoyager | Yes | 2024 | ACL 2024 | Verified from existing search report | Search report points to ACL Anthology. |
| WebWalker | Yes | 2025 | ACL 2025 | Verified from existing search report | Search report points to ACL Anthology. |
| WorkArena | Yes | 2024 | ICML 2024 | Verified from existing search report | Search report lists ServiceNow/project and peer-reviewed venue. |
| WorkArena++ | Yes | 2024 | NeurIPS 2024 | Verified from existing search report | Search report points to NeurIPS proceedings. |
| ACE | Yes | 2026 | NDSS 2026 | Verified from existing search report | Search report points to NDSS page. Re-check final proceedings details before camera-ready citation. |
| RENNERVATE / Attention is All You Need to Defend Against Indirect Prompt Injection Attacks in LLMs | Yes | 2026 | NDSS 2026 | Verified from existing search report | Search report points to NDSS page. |
| AWE | Yes | 2026 | NDSS LAST-X 2026 / arXiv | Potential mismatch | Existing README had "Unclear from local PDF"; search report referenced an NDSS page with uncertain status. Targeted official check indicates NDSS LAST-X 2026 accepted/co-located event, not necessarily NDSS main conference. |
| Formalizing and Benchmarking Prompt Injection Attacks and Defenses | Yes | 2024 | USENIX Security 2024 | Verified from existing search report | Search report points to USENIX Security. |
| Identifying AI Web Scrapers Using Canary Tokens | Yes | 2026 | arXiv | Verified from existing search report | Treat as preprint. |
| Not What You've Signed Up For | Yes | 2023 | ACM AISec 2023 | Verified from existing search report | Search report notes AISec, not ACM CCS main conference. |
| Overcoming the Retrieval Barrier | Yes | 2026 | USENIX Security 2026 | Verified from existing search report | Search report points to USENIX Security 2026 page; verify final proceedings metadata before formal citation. |
| ToolHijacker / Prompt Injection Attack to Tool Selection in LLM Agents | Yes | 2026 | NDSS 2026 | Verified from existing search report | Search report points to NDSS PDF/page. |
| SafeArena | Yes | 2025 | ICML 2025 / PMLR | Verified from existing search report | Targeted check found OpenReview and PMLR page. |
| ST-WebAgentBench | Yes | 2026 | ICLR 2026 / OpenReview | Potential mismatch | Existing search report listed 2024 arXiv preprint. Targeted OpenReview check indicates ICLR 2026 page with updated task/policy counts. Verify exact version before citation. |
| Unsafe LLM-Based Search | Yes | 2025 | USENIX Security 2025 | Verified from existing search report | Search report points to USENIX Security. |
| WARD | Yes | 2026 | arXiv | Verified from existing search report | Targeted arXiv check confirms preprint status. |
| WASP | Yes | 2025 | arXiv / OpenReview | Verified from existing search report | Treat as preprint/OpenReview unless a later venue appears. |
| When AI Meets the Web | Yes | 2026 | IEEE S&P 2026 | Verified from existing search report | Search report points to IEEE S&P accepted papers; verify final proceedings entry before formal citation. |
| YuraScanner | Yes | 2025 | NDSS 2025 | Verified from existing search report | Search report points to NDSS PDF. |
| AndroidWorld | Yes | 2025 | ICLR 2025 | Needs web verification | The existing search report listed 2024 benchmark/arXiv as borderline; current README says 2025 ICLR. Re-check official ICLR/OpenReview before citation. |
| EvoCrawl | Yes | 2025 | NDSS 2025 | Potential mismatch | Existing README had "Unclear from local PDF"; targeted official NDSS check confirms NDSS page. Update formal citation from official NDSS proceedings. |
| Gorilla | Yes | 2024 | NeurIPS 2024 | Verified from existing search report | Borderline tool-use paper; verify exact proceedings track if needed. |
| Toolformer | Yes | 2023 | NeurIPS 2023 | Verified from existing search report | Borderline tool-use paper; venue is well established in search report. |

## Verification Summary

- **Total PDFs accounted for:** 43.
- **Verified from existing search report:** 37.
- **Needs web verification:** 2.
- **Potential mismatch:** 4.
- **Unclear from local PDF:** 0 after targeted notes, but several future/recent venues still deserve final citation checks.

## High-Priority Rechecks

- **Go-Browse:** confirm final ICLR 2026 citation details and reconcile with earlier 2025 OpenReview/preprint metadata.
- **ST-WebAgentBench:** confirm final ICLR 2026 version, task count, policy count, and preferred citation.
- **AWE:** cite as NDSS LAST-X 2026 / arXiv unless an official main-conference entry exists.
- **EvoCrawl:** update citation from official NDSS 2025 proceedings.
- **AndroidWorld:** verify ICLR 2025 metadata against official OpenReview/ICLR source.
- **Future/recent security venues:** re-check ACE, RENNERVATE, ToolHijacker, Overcoming the Retrieval Barrier, and When AI Meets the Web before camera-ready bibliography use.
