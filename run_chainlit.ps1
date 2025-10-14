# PowerShell script to run Chainlit Multi-Agent Workflow Assistant
param(
    [int]$Port = 8001
)

Write-Host "Starting Chainlit Multi-Agent Workflow Assistant..." -ForegroundColor Green
Write-Host ""
Write-Host "Make sure FoundryLocal is running before proceeding." -ForegroundColor Yellow
Write-Host ""
Read-Host "Press Enter to continue"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

Write-Host ""
Write-Host "Activating virtual environment..." -ForegroundColor Cyan

# Try to activate the virtual environment
$VenvPath = Join-Path $ScriptDir "foundrylocal\Scripts\Activate.ps1"
if (Test-Path $VenvPath) {
    try {
        & $VenvPath
        Write-Host "Virtual environment activated successfully." -ForegroundColor Green
    }
    catch {
        Write-Host "ERROR: Failed to activate virtual environment" -ForegroundColor Red
        Write-Host "Please ensure the foundrylocal virtual environment exists" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}
else {
    Write-Host "ERROR: Virtual environment not found at $VenvPath" -ForegroundColor Red
    Write-Host "Please ensure the foundrylocal virtual environment exists" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "Starting Chainlit app at http://localhost:$Port..." -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

$PythonPath = Join-Path $ScriptDir "foundrylocal\Scripts\python.exe"
$ChainlitApp = Join-Path $ScriptDir "chainlit_app_simple.py"

try {
    & $PythonPath -m chainlit run $ChainlitApp --port $Port
}
catch {
    Write-Host ""
    Write-Host "ERROR: Failed to start Chainlit" -ForegroundColor Red
    Write-Host "Error: $_" -ForegroundColor Red
}
finally {
    Write-Host ""
    Write-Host "Chainlit server stopped." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
}