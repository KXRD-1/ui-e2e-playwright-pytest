# Open the most recent Playwright trace
Set-Location (Split-Path $PSScriptRoot -Parent)

.\.venv\Scripts\Activate.ps1 | Out-Null

$traceDir = "artifacts\trace"
if (-not (Test-Path $traceDir)) {
  Write-Host "❌ Trace folder not found: $traceDir" -ForegroundColor Red
  exit 1
}

$last = Get-ChildItem "$traceDir\*.zip" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if (-not $last) {
  Write-Host "❌ No trace files found in $traceDir" -ForegroundColor Red
  exit 1
}

Write-Host "Opening trace: $($last.FullName)"
python -m playwright show-trace "$($last.FullName)"
