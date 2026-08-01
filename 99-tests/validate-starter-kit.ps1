param(
    [string]$Root = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = "Stop"

$required = @(
    "README.md",
    ".gitignore",
    ".gitattributes",
    "Initialize-AIOperatingProcess.ps1",
    "00-START-HERE.md",
    "00-CORE-INDEX.md",
    "LICENSE",
    "SECURITY.md",
    "RELEASE-NOTES.md",
    "01-profile\voice-and-delivery.template.md",
    "02-operating-rules\execution-standard.md",
    "02-operating-rules\work-modes.md",
    "02-operating-rules\runtime-guardrails.md",
    "03-project-context\project.template.md",
    "04-routines\ROUTINE-INDEX.md",
    "04-routines\bug-fix.md",
    "04-routines\writing-system.md",
    "04-routines\live-delivery-preflight.md",
    "04-routines\save-context.md",
    "04-routines\public-claim-readiness.md",
    "05-task-briefs\task.template.md",
    "06-approval-gates\approval-gates.md",
    "07-output-templates\completed-work.md",
    "07-output-templates\blocker.md",
    "07-output-templates\handoff.md",
    "08-memory-updates\README.md",
    "09-system-adapters\README.md",
    "09-system-adapters\codex\AGENTS.md.template",
    "09-system-adapters\claude\CLAUDE.md.template",
    "09-system-adapters\chatgpt\PROJECT-INSTRUCTIONS.template.md",
    "99-tests\release-checklist.md"
    ,"scripts\initialize-process.sh"
    ,"scripts\validate-process.sh"
    ,"scripts\initialize_process.py"
    ,"scripts\validate_process.py"
)

$missing = foreach ($relative in $required) {
    if (-not (Test-Path -LiteralPath (Join-Path $Root $relative) -PathType Leaf)) {
        $relative
    }
}

$profileTemplate = Join-Path $Root "01-profile\user-profile.template.md"
$profileConfigured = Join-Path $Root "01-profile\user-profile.md"
if (-not (Test-Path -LiteralPath $profileTemplate -PathType Leaf) -and -not (Test-Path -LiteralPath $profileConfigured -PathType Leaf)) {
    $missing += "01-profile\user-profile.template.md or 01-profile\user-profile.md"
}

$markdown = Get-ChildItem -LiteralPath $Root -Recurse -File -Filter "*.md"
$empty = $markdown | Where-Object { $_.Length -eq 0 }
$emDash = foreach ($file in $markdown) {
    if ((Get-Content -LiteralPath $file.FullName -Raw).Contains([char]0x2014)) {
        $file.FullName
    }
}

if ($missing) {
    Write-Host "FAIL: Missing required files"
    $missing | ForEach-Object { Write-Host " - $_" }
    exit 1
}

if ($empty) {
    Write-Host "FAIL: Empty Markdown files"
    $empty | ForEach-Object { Write-Host " - $($_.FullName)" }
    exit 1
}

if ($emDash) {
    Write-Host "FAIL: Em dash found"
    $emDash | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host "PASS: AI Operating Process Starter Kit validation passed."
Write-Host "Markdown files: $($markdown.Count)"
