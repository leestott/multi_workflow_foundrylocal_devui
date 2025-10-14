# Quick Setup Script for Multi-Agent Workflow with Chainlit
# This script sets up the virtual environment and installs all dependencies

param(
    [switch]$SkipChainlit,
    [switch]$Force
)

Write-Host "🚀 Multi-Agent Workflow Setup" -ForegroundColor Green
Write-Host "==============================" -ForegroundColor Green
Write-Host ""

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

# Check if virtual environment exists
$VenvPath = "foundrylocal"
if ((Test-Path $VenvPath) -and -not $Force) {
    Write-Host "✅ Virtual environment already exists at $VenvPath" -ForegroundColor Green
    Write-Host "   Use -Force to recreate it" -ForegroundColor Yellow
} else {
    Write-Host "📦 Creating virtual environment..." -ForegroundColor Cyan
    if (Test-Path $VenvPath) {
        Remove-Item -Path $VenvPath -Recurse -Force
    }
    python -m venv $VenvPath
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to create virtual environment" -ForegroundColor Red
        exit 1
    }
    Write-Host "✅ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "🔄 Activating virtual environment..." -ForegroundColor Cyan
$ActivateScript = Join-Path $VenvPath "Scripts\Activate.ps1"
if (Test-Path $ActivateScript) {
    & $ActivateScript
    Write-Host "✅ Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to find activation script" -ForegroundColor Red
    exit 1
}

# Upgrade pip
Write-Host "⬆️  Upgrading pip..." -ForegroundColor Cyan
& python -m pip install --upgrade pip

# Install requirements
if ($SkipChainlit) {
    Write-Host "📥 Installing core requirements..." -ForegroundColor Cyan
    $RequirementsFile = "requirements.txt"
} else {
    Write-Host "📥 Installing requirements with Chainlit..." -ForegroundColor Cyan
    $RequirementsFile = "requirements-chainlit.txt"
}

if (Test-Path $RequirementsFile) {
    & pip install -r $RequirementsFile
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Requirements installed successfully" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Some packages may have failed to install" -ForegroundColor Yellow
    }
} else {
    Write-Host "❌ Requirements file not found: $RequirementsFile" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "🎉 Setup Complete!" -ForegroundColor Green
Write-Host "==================" -ForegroundColor Green
Write-Host ""

if (-not $SkipChainlit) {
    Write-Host "📋 Available Commands:" -ForegroundColor Cyan
    Write-Host "   Chainlit UI:    powershell -ExecutionPolicy Bypass -File run_chainlit.ps1" -ForegroundColor White
    Write-Host "   DevUI:          python main.py" -ForegroundColor White
    Write-Host ""
    Write-Host "🌐 URLs:" -ForegroundColor Cyan
    Write-Host "   Chainlit:       http://localhost:8001" -ForegroundColor White
    Write-Host "   DevUI:          http://localhost:8093" -ForegroundColor White
} else {
    Write-Host "📋 Available Commands:" -ForegroundColor Cyan
    Write-Host "   DevUI:          python main.py" -ForegroundColor White
    Write-Host ""
    Write-Host "🌐 URLs:" -ForegroundColor Cyan
    Write-Host "   DevUI:          http://localhost:8093" -ForegroundColor White
}

Write-Host ""
Write-Host "⚙️  Next Steps:" -ForegroundColor Yellow
Write-Host "   1. Ensure FoundryLocal is running" -ForegroundColor White
Write-Host "   2. Check your .env file configuration" -ForegroundColor White
Write-Host "   3. Run one of the commands above" -ForegroundColor White
Write-Host ""