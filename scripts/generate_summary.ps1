param(
    [Parameter(Mandatory = $true)][string]$Pdf,
    [Parameter(Mandatory = $true)][string]$Target,
    [Parameter(Mandatory = $true)][string]$PromptPath
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$pdfPath = (Resolve-Path -LiteralPath $Pdf).Path
$promptFile = (Resolve-Path -LiteralPath $PromptPath).Path
$targetPath = Join-Path $root $Target
$slug = [System.IO.Path]::GetFileNameWithoutExtension($targetPath)
$tempDir = Join-Path $root ('analysis/evidence/' + $slug)
$codex = (Get-Command codex -ErrorAction Stop).Source
$env:PYTHONIOENCODING = 'utf-8'

New-Item -ItemType Directory -Force -Path (Split-Path -Parent $targetPath) | Out-Null
New-Item -ItemType Directory -Force -Path $tempDir | Out-Null
if (Test-Path -LiteralPath $targetPath) {
    throw "Draft already exists; review or repair it instead of overwriting: $targetPath"
}
$provenance = @{
    source_sha256 = (Get-FileHash -LiteralPath $pdfPath -Algorithm SHA256).Hash.ToLowerInvariant()
    prompt_sha256 = (Get-FileHash -LiteralPath $promptFile -Algorithm SHA256).Hash.ToLowerInvariant()
    started_at = [DateTime]::UtcNow.ToString('o')
    pdf = $Pdf
    target = $Target
    status = 'running'
    process_id = $PID
}
$provenance | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $tempDir 'run.json') -Encoding utf8

try {
    $extraction = @'
import json
import re
import os
import sys
import fitz
from PyPDF2 import PdfReader

path = sys.argv[1]
visual_dir = sys.argv[2]
doc = fitz.open(path)
reader = PdfReader(path)
page_records = []
candidate_scores = []
all_text = []

for index, page in enumerate(doc):
    native = page.get_text("text") or ""
    extracted = ""
    try:
        extracted = reader.pages[index].extract_text() or ""
    except Exception as exc:
        extracted = f"[PyPDF2 extraction error: {exc}]"
    text = extracted if len(extracted.strip()) >= len(native.strip()) else native
    all_text.append(f"\n\n===== PAGE {index + 1} OF {len(doc)} =====\n\n{text}")

    lower = native.lower()
    images = len(page.get_images(full=True))
    score = 0
    if images:
        score += 7 + min(images, 3)
    if re.search(r"\bfig(?:ure)?\.?\s*\d+", lower):
        score += 10
    if re.search(r"\btable\s*\d+", lower):
        score += 7
    if re.search(r"\b(?:algorithm|architecture|workflow|diagram|flowchart)\b", lower):
        score += 4
    if re.search(r"\b(?:equation|eq\.)\s*\(?\d+", lower):
        score += 4
    if index == 0:
        score += 2
    if score:
        candidate_scores.append((score, index))

    page_records.append({
        "page": index + 1,
        "native_text_chars": len(native.strip()),
        "chosen_text_chars": len(text.strip()),
        "embedded_images": images,
        "likely_scanned_or_low_text": len(native.strip()) < 80,
    })

# Score candidates only; the analyst must audit coverage against the inventory.
max_visual_pages = 56
ranked = [idx for _, idx in sorted(candidate_scores, key=lambda x: (-x[0], x[1]))]
selected = []
for idx in ranked:
    if idx not in selected:
        selected.append(idx)
    if len(selected) >= max_visual_pages:
        break
selected.sort()

image_paths = []
for index in selected:
    out = os.path.join(visual_dir, f"page_{index + 1:03d}.png")
    page = doc[index]
    page.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False).save(out)
    image_paths.append(out)

combined = "\n".join(all_text)
supp_refs = sorted(set(re.findall(
    r"(?i)\b(?:supplementary|supplemental)\s+(?:material|appendix|file|data|document|website|repository)?",
    combined,
)))
appendix_pages = [r["page"] for r in page_records if re.search(
    r"(?im)^\s*(?:appendix|appendices)\b", all_text[r["page"] - 1]
)]
metadata = {
    "main_document_available": True,
    "page_range_available": f"1-{len(doc)}",
    "page_count": len(doc),
    "pages_apparently_missing": "not assessed; accessible page count does not establish completeness",
    "pages_with_low_native_text": [r["page"] for r in page_records if r["likely_scanned_or_low_text"]],
    "visual_content_available": "partial visual rendering" if len(selected) < len(doc) else "all pages rendered",
    "rendered_visual_pages": [i + 1 for i in selected],
    "candidate_visual_pages_total": len(set(ranked)),
    "visual_page_limit": max_visual_pages,
    "tables_readable": "native/extracted text plus rendered candidate pages; exact readability must be assessed in analysis",
    "equations_readable": "native/extracted text plus rendered candidate pages; OCR-sensitive notation must be flagged",
    "appendix_pages_detected": appendix_pages,
    "embedded_file_count": len(doc.embfile_names()),
    "supplementary_references_detected": supp_refs,
    "ocr_needed": bool([r for r in page_records if r["likely_scanned_or_low_text"]]),
    "page_records": page_records,
}

with open(os.path.join(visual_dir, "article.txt"), "w", encoding="utf-8") as handle:
    handle.write(combined)
with open(os.path.join(visual_dir, "accessibility.json"), "w", encoding="utf-8") as handle:
    json.dump(metadata, handle, ensure_ascii=False, indent=2)
with open(os.path.join(visual_dir, "images.txt"), "w", encoding="utf-8") as handle:
    handle.write("\n".join(image_paths))
'@ | python - $pdfPath $tempDir
    if ($LASTEXITCODE -ne 0) { throw 'PDF extraction failed' }

    $articleText = Get-Content -Raw -LiteralPath (Join-Path $tempDir 'article.txt')
    $accessibility = Get-Content -Raw -LiteralPath (Join-Path $tempDir 'accessibility.json')
    $imagePaths = @(Get-Content -LiteralPath (Join-Path $tempDir 'images.txt') | Where-Object { $_ -and (Test-Path -LiteralPath $_) })
    $analysisPrompt = Get-Content -Raw -LiteralPath $promptFile

    $instructions = @"
$analysisPrompt

## Supplied-analysis context

The academic work is supplied below as complete page-labeled text extracted from the local PDF. Images attached to this request are rendered source pages selected because they contain figures, tables, diagrams, equations, algorithms, or embedded images. Use only this supplied paper text, accessibility record, and attached source-page images. Do not browse, call tools, or introduce external facts.

The accessibility record was generated mechanically and is evidence for Stage 0, not a substitute for your own inspection. If not every page was rendered, clearly distinguish visual inspection from caption/text inspection and list that limitation. References to supplementary artifacts do not mean those artifacts were supplied. Treat OCR-sensitive notation and extraction discrepancies cautiously.

Output only the finished Markdown analysis. It must begin with `# Stage 0 - Document Accessibility Report`, then include all 22 numbered final-output sections from the attached prompt in order, and end with `# Completeness Audit`. Use page/section/figure/table/equation locators throughout. Be exhaustive but avoid repeating the same fact merely to increase length.

### Mechanical accessibility record

```json
$accessibility
```

### Complete page-labeled paper text

$articleText
"@

    $arguments = @('exec', '--ephemeral', '-s', 'read-only', '-C', $root, '-o', $targetPath)
    foreach ($imagePath in $imagePaths) {
        $arguments += @('-i', $imagePath)
    }
    $arguments += '-'

    $instructions | & $codex @arguments *> (Join-Path $tempDir 'generation.log')
    if ($LASTEXITCODE -ne 0) {
        throw "Codex exited with code $LASTEXITCODE"
    }
    if (-not (Test-Path -LiteralPath $targetPath)) {
        throw "No analysis was written to $targetPath"
    }

    $result = Get-Content -Raw -LiteralPath $targetPath
    if ($result.Length -lt 20000) {
        throw "Analysis is unexpectedly short ($($result.Length) characters)"
    }

    $required = @(
        'Stage 0', 'Plain-Language Orientation', 'Document Roadmap',
        'Background and Context', 'Research Problem and Gap',
        'Research Questions', 'Assumptions / Threat Model', 'Methodology',
        'Experiments / Analyses', 'Results', 'Figure-by-Figure',
        'Table-by-Table', 'Diagram / Architecture', 'Equations and Mathematical',
        'Interpretation and Discussion', 'Contributions and Novelty',
        'Limitations', 'Threats to Validity', 'Future Work and Open Questions',
        'Terminology and Notation Glossary', 'Key Numerical Results',
        'Evidence Map', 'Very Simple Explanation', 'Completeness Audit'
    )
    $missing = @($required | Where-Object { $result -notmatch [regex]::Escape($_) })
    if ($missing.Count) {
        throw "Analysis is missing required sections: $($missing -join ', ')"
    }

    $provenance.status = 'generated_requires_source_review'
    "OK|$Target|$($result.Length)|visualpages=$($imagePaths.Count)"
}
catch {
    $provenance.status = 'failed_or_interrupted'
    $provenance.error = $_.Exception.Message
    throw
}
finally {
    $provenance.finished_at = [DateTime]::UtcNow.ToString('o')
    $provenance | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $tempDir 'run.json') -Encoding utf8
}
