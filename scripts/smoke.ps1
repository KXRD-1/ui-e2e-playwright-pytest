# Run smoke tests (headless by default)
Set-Location (Split-Path $PSScriptRoot -Parent)

if (-not (Test-Path ".\.venv\Scripts\Activate.ps1")) {
  Write-Host "❌ .venv not found. Create it first: python -m venv .venv" -ForegroundColor Red
  exit 1
}

.\.venv\Scripts\Activate.ps1 | Out-Null

# Default HEADLESS=true if not set
if (-not $env:HEADLESS) { $env:HEADLESS = "true" }

pytest -q -m smoke
