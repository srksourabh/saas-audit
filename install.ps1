[CmdletBinding()]
param(
    [switch]$Project,
    [string]$HermesSkillsDir
)

$ErrorActionPreference = 'Stop'
$SkillName = 'saas-audit'
$SourceDir = Split-Path -Parent $MyInvocation.MyCommand.Path

function Copy-Skill {
    param([Parameter(Mandatory = $true)][string]$Destination)

    $Parent = Split-Path -Parent $Destination
    New-Item -ItemType Directory -Force -Path $Parent | Out-Null
    if (Test-Path $Destination) {
        Remove-Item -Recurse -Force $Destination
    }
    New-Item -ItemType Directory -Force -Path $Destination | Out-Null

    Get-ChildItem -LiteralPath $SourceDir -Force |
        Where-Object { $_.Name -notin @('.git', '.github', 'saas-audit-output') } |
        ForEach-Object {
            Copy-Item -LiteralPath $_.FullName -Destination $Destination -Recurse -Force
        }

    Write-Host "Installed: $Destination"
}

if ($Project) {
    $Root = (Get-Location).Path
    $Destinations = @(
        (Join-Path $Root ".agents\skills\$SkillName"),
        (Join-Path $Root ".claude\skills\$SkillName"),
        (Join-Path $Root ".github\skills\$SkillName")
    )
}
else {
    $Destinations = @(
        (Join-Path $HOME ".agents\skills\$SkillName"),
        (Join-Path $HOME ".claude\skills\$SkillName")
    )
}

if ($HermesSkillsDir) {
    $Destinations += (Join-Path $HermesSkillsDir $SkillName)
}
elseif ($env:HERMES_SKILLS_DIR) {
    $Destinations += (Join-Path $env:HERMES_SKILLS_DIR $SkillName)
}

foreach ($Destination in $Destinations) {
    Copy-Skill -Destination $Destination
}

Write-Host ""
Write-Host "SaaS Audit installed successfully."
Write-Host "Restart or reload your AI coding client, then ask:"
Write-Host "Use the saas-audit skill to audit this repository and issue a release verdict."
