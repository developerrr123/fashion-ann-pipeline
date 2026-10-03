$ErrorActionPreference = 'Continue'
$evidence = Join-Path $PSScriptRoot 'evidence'
New-Item -ItemType Directory -Force $evidence | Out-Null

(@{
    'git-log-graph.txt' = { git log --oneline --graph --decorate --all }
    'git-log-stat.txt' = { git log --stat -3 }
    'git-log-patch.txt' = { git log -p -1 }
    'git-main-to-dev.txt' = { git log main..dev }
    'git-diff-main-dev.txt' = { git diff main..dev }
    'git-diff-main-three-dot-dev.txt' = { git diff main...dev }
    'dvc-metrics.txt' = { dvc metrics show }
    'dvc-status.txt' = { dvc status }
}).GetEnumerator() | ForEach-Object {
    & $_.Value 2>&1 | Out-File (Join-Path $evidence $_.Key) -Encoding utf8
}

Write-Host "Evidence written to $evidence"