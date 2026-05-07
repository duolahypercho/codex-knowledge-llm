param(
    [Parameter(Mandatory = $true)]
    [string]$TargetPath,

    [string]$Owner = "ziwenxu",

    [switch]$Force
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir
$TemplateDir = Join-Path $RepoRoot "templates\vault-kit"
$ResolvedTarget = Resolve-Path -LiteralPath $TargetPath

if (-not (Test-Path -LiteralPath $ResolvedTarget -PathType Container)) {
    throw "Target must be an existing directory: $TargetPath"
}

$copied = 0
$skipped = 0

Get-ChildItem -LiteralPath $TemplateDir -Recurse -Force | ForEach-Object {
    $relative = $_.FullName.Substring($TemplateDir.Length).TrimStart("\", "/")
    $destination = Join-Path $ResolvedTarget $relative

    if ($_.PSIsContainer) {
        New-Item -ItemType Directory -Force -Path $destination | Out-Null
        return
    }

    if ((Test-Path -LiteralPath $destination) -and -not $Force) {
        $script:skipped += 1
        return
    }

    $parent = Split-Path -Parent $destination
    New-Item -ItemType Directory -Force -Path $parent | Out-Null
    $content = Get-Content -LiteralPath $_.FullName -Raw
    $content = $content.Replace("{{OWNER}}", $Owner)
    Set-Content -LiteralPath $destination -Value $content -Encoding UTF8
    $script:copied += 1
}

Write-Output "Vault kit embedded in $ResolvedTarget"
Write-Output "Copied: $copied"
Write-Output "Skipped existing files: $skipped"
