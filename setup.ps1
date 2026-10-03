$ErrorActionPreference = 'Stop'

if (-not (Test-Path '.venv')) {
    py -3 -m venv .venv
}

.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Write-Host 'Environment ready. Activate with .\.venv\Scripts\Activate.ps1'
