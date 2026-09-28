param(
    [Parameter(Mandatory = $true)][string]$SummaryName,
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$rows = @(Import-Csv -LiteralPath (Join-Path $root 'analysis/manifest.csv') |
    Where-Object { $_.SummaryName -eq $SummaryName })
if ($rows.Count -ne 1) { throw 'SummaryName must identify exactly one manifest entry' }
$row = $rows[0]
if (Test-Path -LiteralPath (Join-Path $root $row.StageTarget)) {
    throw 'A staged draft exists. Review it before considering regeneration.'
}
if ($DryRun) {
    $row | Format-List
    return
}

$lockPath = Join-Path $root 'analysis/generation.lock'
$lock = $null
try {
    # The file can survive a crash; the exclusive handle cannot.
    $lock = [System.IO.File]::Open($lockPath, 'OpenOrCreate', 'ReadWrite', 'None')
    Push-Location $root
    try {
        & (Join-Path $PSScriptRoot 'generate_summary.ps1') -Pdf $row.Pdf `
            -Target $row.StageTarget -PromptPath (Join-Path $root 'analysis/PROMPT.md')
    }
    finally {
        & python (Join-Path $PSScriptRoot 'summary_state.py')
        Pop-Location
    }
}
finally {
    if ($null -ne $lock) { $lock.Dispose() }
}
