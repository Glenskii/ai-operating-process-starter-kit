param(
    [Parameter(Mandatory = $true)]
    [string]$Destination,
    [string]$OwnerName = ""
)

$ErrorActionPreference = "Stop"
$source = Split-Path -Parent $PSCommandPath
$resolvedDestination = [System.IO.Path]::GetFullPath($Destination)

if (Test-Path -LiteralPath $resolvedDestination) {
    $existing = Get-ChildItem -LiteralPath $resolvedDestination -Force
    if ($existing.Count -gt 0) {
        throw "Destination must be empty: $resolvedDestination"
    }
} else {
    New-Item -ItemType Directory -Path $resolvedDestination | Out-Null
}

$exclude = @("optional-codex-skill", ".git")
Get-ChildItem -LiteralPath $source -Force | Where-Object { $_.Name -notin $exclude } | ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination $resolvedDestination -Recurse -Force
}

$profileTemplate = Join-Path $resolvedDestination "01-profile\user-profile.template.md"
$profile = Join-Path $resolvedDestination "01-profile\user-profile.md"
Move-Item -LiteralPath $profileTemplate -Destination $profile

if ($OwnerName) {
    $content = Get-Content -LiteralPath $profile -Raw
    $content = $content.Replace("[name]", $OwnerName)
    [System.IO.File]::WriteAllText($profile, $content, [System.Text.UTF8Encoding]::new($false))
}

Write-Host "Created AI Operating Process at: $resolvedDestination"
Write-Host "Next: complete 01-profile\user-profile.md and create a project context from 03-project-context\project.template.md."
