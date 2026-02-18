# Run smoke tests and generate HTML report
Set-Location (Split-Path $PSScriptRoot -Parent)

.\.venv\Scripts\Activate.ps1 | Out-Null

if (-not (Test-Path ".\artifacts")) {
  New-Item -ItemType Directory -Force ".\artifacts" | Out-Null
}

if (-not $env:HEADLESS) { $env:HEADLESS = "true" }

pytest -q -m smoke --html=artifacts\report.html --self-contained-html
Write-Host "✅ Report generated: artifacts\report.html"
