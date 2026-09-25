$ErrorActionPreference = 'Stop'
$port = 7985
$healthUrl = "http://127.0.0.1:$port/health"

try {
    $health = Invoke-RestMethod $healthUrl -TimeoutSec 2
    if ($health.status -eq 'ok') {
        Write-Host "Synora AI backend is already running on port $port."
        Write-Host "Health: http://127.0.0.1:$port/health"
        exit 0
    }
} catch {
    # The port may be free even when the health request cannot connect.
}

$listener = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
if ($listener) {
    Write-Host "Port $port is already in use by process $($listener.OwningProcess)."
    Write-Host "Stop that process or use the existing backend instead of starting another copy."
    exit 1
}

Set-Location $PSScriptRoot
& ".\.venv\Scripts\python.exe" -m uvicorn app.main:app --host 127.0.0.1 --port $port
