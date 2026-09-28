#!/usr/bin/env python3
r"""
Organize the Agentic Web Crawlers paper repository.

Design goals
------------
1. Give each PDF ONE primary physical home.
2. Preserve multi-topic relationships as tags in docs/paper_inventory.csv.
3. Detect exact duplicate PDFs by SHA-256.
4. Flag same/near-same titles with different file contents for manual review.
5. Leave docs/, Summaries/, .agents/, and other non-paper assets alone.
6. Update local Markdown PDF links after moves.
7. DRY RUN by default. Nothing is moved unless --apply is supplied.

Typical usage (PowerShell)
--------------------------
python .\organize_agentic_web_crawlers.py --root "G:\My Drive\Papers\Agentic Web Crawlers"
python .\organize_agentic_web_crawlers.py --root "G:\My Drive\Papers\Agentic Web Crawlers" --apply

The first command only previews the plan. Review it before using --apply.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


CATEGORIES = {
    "01": "01_Core_Web_Agent_Architectures",
    "02": "02_Web_Agent_Benchmarks_Environments",
    "03": "03_Agentic_Search_Scraping_Info_Seeking",
    "04": "04_Adversarial_Web_Prompt_Injection_Content_Manipulation",
    "05": "05_Agentic_Traps_Persistence_Adaptive_Attacks",
    "06": "06_Resource_Exhaustion_Availability_Denial_of_Wallet",
    "07": "07_Security_Benchmarks_Evaluation",
    "08": "08_Defenses_Guards_Containment",
    "09": "09_Progress_Long_Horizon_Benign_Controls",
    "10": "10_Traditional_Crawling_Crawler_Traps",
    "11": "11_Surveys_Taxonomies_SoK",
    "12": "12_Contextual_Borderline",
}

# Directories that are not paper-input locations.
PROTECTED_DIR_NAMES = {
    "docs",
    "Summaries",
    ".agents",
    ".git",
    ".github",
    "__pycache__",
    "99_Duplicates",
    "98_Manual_Review",
    *CATEGORIES.values(),
}

# Old organization folders ARE intentionally scanned.
LEGACY_INPUT_DIRS = {"Security", "Borderline", "New"}

# First matching rule wins. These rules are intentionally topic-oriented,
# not simply derived from the current Security/Borderline/root placement.
CATEGORY_RULES = [
    # 08 — defenses first, because many defense titles contain "prompt injection"
    ("08", [
        r"\bward\b",
        r"attention is all you need to defend",
        r"\btask shield\b",
        r"defeating prompt injections by design",
        r"\bmelon\b",
        r"spotlighting",
        r"\bstruq\b",
        r"\bsecalign\b",
        r"\bisolategpt\b",
        r"\bwebagentguard\b",
        r"\bprismata\b",
        r"\bcellmate\b",
        r"\bbrowsesafe\b",
        r"\bsnapguard\b",
        r"untrusted content masking",
        r"\bplanguard\b",
        r"don t click that",
        r"security architecture for llm integrated app systems",
    ]),

    # 06 — availability/resource exhaustion
    ("06", [
        r"autonomy comes with costs",
        r"beyond max tokens",
        r"overthinking loops",
        r"when agents do not stop",
        r"runtime monitoring for reasoning token consumption",
        r"\brecurguard\b",
        r"denial of wallet",
        r"resource amplification",
        r"resource abus",
        r"resource exhaustion",
        r"denial of service vulnerabilities",
    ]),

    # 10 — conventional crawling and crawler-trap foundations
    ("10", [
        r"^web crawling$",
        r"detection of crawler traps",
        r"\birlbot\b",
        r"impact of crawl policy",
        r"measuring what the crawler sees",
        r"crawler trap",
    ]),

    # 11 — surveys / SoKs / taxonomies
    ("11", [
        r"toward secure llm agents",
        r"systematic survey of security threats",
        r"sok attack and defense landscape",
        r"survey on trustworthy llm agents",
        r"survey on autonomy induced security risks",
        r"taxonomy and benchmark coverage audit",
        r"talk is not cheap",
        r"\bsurvey\b",
        r"\bsok\b",
    ]),

    # 05 — closest papers to ACT / persistent/adaptive agent traps
    ("05", [
        r"^ai agent traps$",
        r"how adversarial environments mislead agentic ai",
        r"mind the web",
        r"breaking agents",
        r"\bagentlab\b.*long horizon attacks",
        r"it s a trap",
        r"task redirecting agent persuasion",
        r"context manipulation attacks",
        r"hidden in memory",
        r"sleeper memory poisoning",
        r"\bmaze\b.*agent",
    ]),

    # 07 — security benchmarks/evaluation (not generic capability benchmarks)
    ("07", [
        r"\bwasp\b.*benchmarking web agent security",
        r"\bsafearena\b",
        r"\bst webagentbench\b",
        r"\bsecurewebarena\b",
        r"\bagentdojo\b",
        r"formalizing and benchmarking prompt injection",
        r"indirect prompt injections are firewalls all you need",
        r"benchmark.*prompt injection.*defen",
    ]),

    # 09 — benign long-horizon/progress/trajectory evaluation
    ("09", [
        r"an illusion of progress",
        r"\bodysseys\b",
        r"long horizon task mirage",
        r"\bagentrewardbench\b",
        r"\bwebchorearena\b",
        r"\bguide\b.*hierarchical diagnosis",
        r"\bfocusagent\b",
        r"trajectory.*evaluat",
        r"long horizon.*task",
    ]),

    # 03 — information seeking, search, traversal, scraping
    ("03", [
        r"\bwebscraper\b",
        r"\bautoscraper\b",
        r"\bwebsailor\b",
        r"\bwebdancer\b",
        r"\bwebwalker\b",
        r"evaluating agentic search",
        r"\bwebgpt\b",
        r"autonomous information seeking",
        r"web scraping",
        r"scraper generation",
        r"index content web scraping",
        r"benchmarking llms in web traversal",
    ]),

    # 02 — capability benchmarks/environments/datasets
    ("02", [
        r"\bbrowsecomp\b",
        r"\bbearcubs\b",
        r"\bmmina\b",
        r"\bbrowsergym\b",
        r"\bvisualwebarena\b",
        r"\bwebarena\b",
        r"\bworkarena\b",
        r"\bmind2web\b(?!.*evaluating agentic search)",
        r"\bweblinx\b",
        r"\bwebshop\b",
        r"benchmark for computer using web agents",
        r"benchmarking multihop multimodal internet agents",
        r"realistic web environment for building autonomous agents",
    ]),

    # 01 — core agent architectures/methods
    ("01", [
        r"\bautowebglm\b",
        r"gpt 4v.*generalist web agent",
        r"\bseeact\b",
        r"\blaser\b.*web navigation",
        r"\breact\b.*reasoning and acting",
        r"\bwebvoyager\b",
        r"\bgo browse\b",
        r"training web agents with structured exploration",
        r"large language model based web navigating agent",
        r"end to end web agent",
        r"state space exploration for web navigation",
    ]),

    # 04 — direct attacks/content manipulation/web-connected attack studies
    ("04", [
        r"\bwaaa\b",
        r"web adversaries against agentic browsers",
        r"\beia\b.*environmental injection",
        r"\badvagent\b",
        r"controllable blackbox red teaming",
        r"attacking vision language computer agents",
        r"dissecting adversarial robustness",
        r"\bvpi bench\b",
        r"visual prompt injection",
        r"\bagentfuzzer\b",
        r"\bagentvigil\b",
        r"\bwebinject\b",
        r"commercial llm agents are already vulnerable",
        r"not what you ve signed up for",
        r"overcoming the retrieval barrier",
        r"prompt injection attack to tool selection",
        r"when ai meets the web",
        r"unsafe llm based search",
        r"one polluted page is enough",
        r"how much can we trust llm search agents",
        r"web content pollution",
        r"endorsement vulnerability",
        r"\bwebcloak\b",
        r"identifying ai web scrapers using canary tokens",
    ]),

    # 12 — contextual/adjacent papers
    ("12", [
        r"\btoolformer\b",
        r"\bgorilla\b",
        r"\bandroidworld\b",
        r"\bevocrawl\b",
        r"\bbackdooragent\b",
        r"\bskilltrojan\b",
        r"adaptive agents for dynamic web penetration testing",
        r"\byurascanner\b",
    ]),
]


TAG_RULES = [
    ("web-agent", r"\bweb\b|\bbrowser\b"),
    ("benchmark", r"benchmark|arena|evaluation"),
    ("long-horizon", r"long horizon|multi turn|multihop|trajectory|tedious"),
    ("prompt-injection", r"prompt injection|indirect prompt|environmental injection"),
    ("resource-exhaustion", r"resource|denial of service|denial of wallet|max tokens|consumption|overthinking loop"),
    ("crawler-trap", r"crawler trap|\bmaze\b"),
    ("scraping", r"scrap|crawler|crawling"),
    ("information-seeking", r"search|information seeking|question answering|web traversal"),
    ("multimodal", r"multimodal|vision|visual|screenshot|gpt 4v"),
    ("memory", r"memory|context manipulation"),
    ("adaptive-attack", r"adaptive|fuzzer|red team"),
    ("defense", r"defen|guard|shield|sandbox|masking|isolation|contain"),
    ("progress-evaluation", r"progress|reward|efficiency|diagnos|trajectory"),
    ("tool-use", r"tool|api|mcp"),
    ("survey-taxonomy", r"survey|taxonomy|sok|threat surfaces"),
]


def normalized_title(path_or_name: str | Path) -> str:
    """Normalize filenames so punctuation/underscore differences do not matter."""
    name = Path(path_or_name).stem
    name = name.replace("&", " and ")
    name = re.sub(r"[_\-\u2010-\u2015]+", " ", name)
    name = re.sub(r"[^A-Za-z0-9]+", " ", name)
    name = re.sub(r"\s+", " ", name).strip().lower()

    # Normalize a few common filename/version decorations.
    name = re.sub(r"\bv\d+\b$", "", name).strip()
    name = re.sub(r"\bpdf\b$", "", name).strip()
    return name


def compact_title_key(path_or_name: str | Path) -> str:
    """Stronger normalization for finding title variants."""
    t = normalized_title(path_or_name)
    # Remove punctuation-created stop-like variation, but keep informative words.
    words = [w for w in t.split() if w not in {"a", "an", "the"}]
    return " ".join(words)


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def classify(path: Path) -> tuple[str, list[str], str]:
    title = normalized_title(path.name)
    for category_id, patterns in CATEGORY_RULES:
        for pattern in patterns:
            if re.search(pattern, title, flags=re.I):
                tags = sorted({
                    tag for tag, tag_pattern in TAG_RULES
                    if re.search(tag_pattern, title, flags=re.I)
                })
                return CATEGORIES[category_id], tags, pattern

    tags = sorted({
        tag for tag, tag_pattern in TAG_RULES
        if re.search(tag_pattern, title, flags=re.I)
    })
    return CATEGORIES["12"], tags, "fallback"


def should_scan_pdf(path: Path, root: Path) -> bool:
    if path.suffix.lower() != ".pdf":
        return False

    try:
        rel = path.relative_to(root)
    except ValueError:
        return False

    # Skip protected destinations/metadata/support dirs.
    for part in rel.parts[:-1]:
        if part in PROTECTED_DIR_NAMES:
            return False

    # Scan:
    # - PDFs directly in root
    # - PDFs in the old Security, Borderline, New folders
    if len(rel.parts) == 1:
        return True
    return rel.parts[0] in LEGACY_INPUT_DIRS


def source_priority(path: Path, root: Path) -> tuple[int, int, str]:
    """
    Prefer the already-curated copy over a New/ duplicate.
    Lower tuple wins.
    """
    rel = path.relative_to(root)
    if len(rel.parts) == 1:
        rank = 0
    elif rel.parts[0] == "Security":
        rank = 1
    elif rel.parts[0] == "Borderline":
        rank = 2
    elif rel.parts[0] == "New":
        rank = 3
    else:
        rank = 9
    return (rank, len(str(rel)), str(rel).lower())


def collision_safe_target(target: Path, source_hash: str) -> Path:
    """Avoid overwriting a different file that happens to have the same name."""
    if not target.exists():
        return target
    try:
        if sha256_file(target) == source_hash:
            return target
    except OSError:
        pass

    base = target.with_suffix("")
    suffix = target.suffix
    i = 2
    while True:
        alt = Path(f"{base}__alt{i}{suffix}")
        if not alt.exists():
            return alt
        i += 1


def local_markdown_link_rewrite(md_path: Path, old_to_new: dict[Path, Path]) -> int:
    """
    Rewrite inline local Markdown links such as:
        [PDF](../OldFolder/Paper.pdf)
    after a PDF move.

    Remote URLs and anchors are ignored.
    """
    try:
        text = md_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return 0

    changed = 0

    def repl(match: re.Match) -> str:
        nonlocal changed
        inside = match.group(1)

        # Preserve optional Markdown link title: path "title"
        parts = inside.split(maxsplit=1)
        dest = parts[0]
        tail = (" " + parts[1]) if len(parts) == 2 else ""

        low = dest.lower()
        if (
            low.startswith(("http://", "https://", "mailto:", "data:"))
            or dest.startswith("#")
        ):
            return match.group(0)

        decoded = unquote(dest)
        candidate = (md_path.parent / decoded).resolve(strict=False)

        if candidate not in old_to_new:
            return match.group(0)

        new_abs = old_to_new[candidate]
        new_rel = os.path.relpath(new_abs, md_path.parent).replace(os.sep, "/")
        changed += 1
        return f"]({new_rel}{tail})"

    new_text = re.sub(r"\]\(([^)]+)\)", repl, text)
    if changed:
        md_path.write_text(new_text, encoding="utf-8")
    return changed


def print_tree():
    print("\nRecommended primary-folder taxonomy:\n")
    for key in sorted(CATEGORIES):
        print(f"  {CATEGORIES[key]}/")
    print("  98_Manual_Review/")
    print("  99_Duplicates/Exact/")
    print("  docs/                # existing review docs + generated inventory")
    print("  Summaries/           # existing summaries stay here")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Organize an Agentic Web Crawlers literature repository."
    )
    parser.add_argument(
        "--root",
        required=True,
        type=Path,
        help=r'Repository root, e.g. "G:\My Drive\Papers\Agentic Web Crawlers"',
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually move files and update Markdown links. Default is dry-run.",
    )
    parser.add_argument(
        "--no-link-update",
        action="store_true",
        help="Do not rewrite local Markdown links after moving PDFs.",
    )
    args = parser.parse_args()

    root = args.root.expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: root does not exist or is not a directory: {root}", file=sys.stderr)
        return 2

    print_tree()
    print(f"\nRepository: {root}")
    print("Mode:", "APPLY" if args.apply else "DRY RUN (no changes)")

    pdfs = sorted(
        [p for p in root.rglob("*.pdf") if should_scan_pdf(p, root)],
        key=lambda p: str(p).lower(),
    )

    if not pdfs:
        print("No input PDFs found.")
        return 0

    print(f"Input PDFs discovered: {len(pdfs)}")

    # Hash all discovered PDFs.
    file_hash = {}
    for p in pdfs:
        try:
            file_hash[p] = sha256_file(p)
        except OSError as e:
            print(f"WARNING: cannot hash {p}: {e}", file=sys.stderr)

    pdfs = [p for p in pdfs if p in file_hash]

    # Exact duplicate groups.
    by_hash = defaultdict(list)
    for p in pdfs:
        by_hash[file_hash[p]].append(p)

    canonical_for_hash = {}
    exact_duplicate_of = {}
    for h, group in by_hash.items():
        ordered = sorted(group, key=lambda p: source_priority(p, root))
        canonical = ordered[0]
        canonical_for_hash[h] = canonical
        for duplicate in ordered[1:]:
            exact_duplicate_of[duplicate] = canonical

    # Title groups flag possible different revisions/copies.
    by_title = defaultdict(list)
    for p in pdfs:
        by_title[compact_title_key(p.name)].append(p)

    near_duplicate_groups = {
        title: group
        for title, group in by_title.items()
        if len({file_hash[p] for p in group}) > 1
    }

    # Build move plan only for canonical files.
    plan = []
    old_to_new = {}

    canonical_pdfs = [p for p in pdfs if p not in exact_duplicate_of]
    for p in canonical_pdfs:
        category, tags, rule = classify(p)
        target = root / category / p.name
        target = collision_safe_target(target, file_hash[p])

        plan.append({
            "source": p,
            "target": target,
            "category": category,
            "tags": tags,
            "sha256": file_hash[p],
            "rule": rule,
            "exact_duplicate_of": "",
        })
        old_to_new[p.resolve(strict=False)] = target.resolve(strict=False)

    # Add exact duplicates to duplicate archive plan.
    duplicate_plan = []
    for dup, canonical in exact_duplicate_of.items():
        dup_target = root / "99_Duplicates" / "Exact" / dup.name
        dup_target = collision_safe_target(dup_target, file_hash[dup])
        duplicate_plan.append({
            "source": dup,
            "target": dup_target,
            "category": "99_Duplicates/Exact",
            "tags": ["exact-duplicate"],
            "sha256": file_hash[dup],
            "rule": "sha256-exact-duplicate",
            "exact_duplicate_of": str(canonical.relative_to(root)),
        })
        old_to_new[dup.resolve(strict=False)] = dup_target.resolve(strict=False)

    print("\nPlanned canonical placements:")
    counts = defaultdict(int)
    for item in plan:
        counts[item["category"]] += 1
        print(
            f"  {item['source'].relative_to(root)}\n"
            f"    -> {item['target'].relative_to(root)}"
        )

    print("\nCategory counts:")
    for category in CATEGORIES.values():
        if counts[category]:
            print(f"  {category}: {counts[category]}")

    if duplicate_plan:
        print(f"\nExact duplicate copies detected: {len(duplicate_plan)}")
        for item in duplicate_plan:
            print(
                f"  {item['source'].relative_to(root)}"
                f" -> 99_Duplicates/Exact/"
                f" (same SHA-256 as {item['exact_duplicate_of']})"
            )
    else:
        print("\nExact duplicate copies detected: 0")

    if near_duplicate_groups:
        print("\nPotential revision / near-duplicate title groups (NOT auto-deleted):")
        for title, group in sorted(near_duplicate_groups.items()):
            print(f"  TITLE KEY: {title}")
            for p in group:
                print(
                    f"    - {p.relative_to(root)}"
                    f"  sha256={file_hash[p][:12]}..."
                )
    else:
        print("\nPotential revision / near-duplicate title groups: 0")

    if not args.apply:
        print(
            "\nDRY RUN COMPLETE.\n"
            "No files or Markdown links were changed.\n"
            "If the plan looks correct, rerun with --apply."
        )
        return 0

    # Create destinations.
    for category in CATEGORIES.values():
        (root / category).mkdir(parents=True, exist_ok=True)
    (root / "98_Manual_Review").mkdir(parents=True, exist_ok=True)
    (root / "99_Duplicates" / "Exact").mkdir(parents=True, exist_ok=True)
    (root / "docs").mkdir(parents=True, exist_ok=True)

    # Move canonical files.
    actually_moved = {}
    for item in plan + duplicate_plan:
        source = item["source"]
        target = item["target"]

        if source.resolve(strict=False) == target.resolve(strict=False):
            continue

        target.parent.mkdir(parents=True, exist_ok=True)

        # If identical target already exists, archive the source as duplicate.
        if target.exists():
            try:
                if sha256_file(target) == item["sha256"]:
                    if source.exists():
                        dup_target = collision_safe_target(
                            root / "99_Duplicates" / "Exact" / source.name,
                            item["sha256"],
                        )
                        shutil.move(str(source), str(dup_target))
                        actually_moved[source.resolve(strict=False)] = dup_target.resolve(strict=False)
                    continue
            except OSError:
                pass

        if source.exists():
            shutil.move(str(source), str(target))
            actually_moved[source.resolve(strict=False)] = target.resolve(strict=False)

    # Update Markdown links based on actual move locations.
    if not args.no_link_update and actually_moved:
        updated_links = 0
        updated_files = 0
        for md in root.rglob("*.md"):
            if ".git" in md.parts:
                continue
            n = local_markdown_link_rewrite(md, actually_moved)
            if n:
                updated_files += 1
                updated_links += n
        print(
            f"\nMarkdown link update: {updated_links} links "
            f"across {updated_files} Markdown files."
        )

    # Write canonical inventory after moves.
    manifest_path = root / "docs" / "paper_inventory.csv"
    with manifest_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "filename",
                "primary_category",
                "tags",
                "sha256",
                "classification_rule",
                "original_path",
                "current_path",
                "exact_duplicate_of",
            ],
        )
        writer.writeheader()

        for item in plan + duplicate_plan:
            old = item["source"].resolve(strict=False)
            final = actually_moved.get(old, item["target"].resolve(strict=False))
            try:
                current_rel = final.relative_to(root)
            except ValueError:
                current_rel = final

            writer.writerow({
                "filename": item["source"].name,
                "primary_category": item["category"],
                "tags": ";".join(item["tags"]),
                "sha256": item["sha256"],
                "classification_rule": item["rule"],
                "original_path": str(item["source"].relative_to(root)),
                "current_path": str(current_rel),
                "exact_duplicate_of": item["exact_duplicate_of"],
            })

    # Write near-duplicate/revision report.
    near_path = root / "docs" / "near_duplicate_candidates.csv"
    with near_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["title_key", "filename", "sha256", "original_path"],
        )
        writer.writeheader()
        for title, group in sorted(near_duplicate_groups.items()):
            for p in group:
                writer.writerow({
                    "title_key": title,
                    "filename": p.name,
                    "sha256": file_hash[p],
                    "original_path": str(p.relative_to(root)),
                })

    print("\nORGANIZATION COMPLETE.")
    print(f"Inventory written to: {manifest_path}")
    print(f"Near-duplicate report:  {near_path}")
    print(
        "\nImportant: inspect 12_Contextual_Borderline and the near-duplicate "
        "report manually after the first run. Keyword classification is "
        "deliberately conservative for ambiguous papers."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
