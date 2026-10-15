# Not Your Vibe: Windows PowerShell One-Line Installer
# Usage: irm https://raw.githubusercontent.com/apinee/not_ur_vibe/main/scripts/install.ps1 | iex

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "          ✨ Installing Not Your Vibe ✨                 " -ForegroundColor Yellow
Write-Host "  Universal Learning-First AI Pair Programming Framework  " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""

$targetDir = Get-Location
Write-Host "Target project directory: $targetDir" -ForegroundColor White

$dirs = @(
    ".vibewise",
    ".cursor/rules",
    ".agents/skills/learn",
    ".agents/skills/reset",
    ".agents/skills/review"
)

foreach ($d in $dirs) {
    $full = Join-Path $targetDir $d
    if (-not (Test-Path $full)) {
        New-Item -ItemType Directory -Path $full -Force | Out-Null
    }
}

$profilePath = Join-Path $targetDir ".vibewise/profile.md"
if (-not (Test-Path $profilePath)) {
    @"
# Learner Profile

Learning mode: active
Onboarding: incomplete

Remaining onboarding: Project situation, experience, stack familiarity, goals, and preferences.
"@ | Set-Content -Path $profilePath -Encoding UTF8
    Write-Host "✔ Created .vibewise/profile.md" -ForegroundColor Green
}

$progressPath = Join-Path $targetDir ".vibewise/progress.md"
if (-not (Test-Path $progressPath)) {
    @"
# Learning Progress

No learning events recorded yet.
"@ | Set-Content -Path $progressPath -Encoding UTF8
    Write-Host "✔ Created .vibewise/progress.md" -ForegroundColor Green
}

$gitIgnore = Join-Path $targetDir ".gitignore"
if (Test-Path $gitIgnore) {
    $content = Get-Content -Path $gitIgnore -Raw
    if ($content -notmatch "\.vibewise/") {
        Add-Content -Path $gitIgnore -Value "`n# Not Your Vibe learning state`n.vibewise/"
        Write-Host "✔ Added .vibewise/ to .gitignore" -ForegroundColor Green
    }
} else {
    Set-Content -Path $gitIgnore -Value "# Not Your Vibe learning state`n.vibewise/" -Encoding UTF8
    Write-Host "✔ Created .gitignore with .vibewise/" -ForegroundColor Green
}

Write-Host ""
Write-Host "✅ Not Your Vibe installed successfully in $targetDir!" -ForegroundColor Green
Write-Host "Open your project in Antigravity, Claude Code, Codex, or Cursor and start learning!" -ForegroundColor White
Write-Host ""
