@echo off
REM Install script for Multi-Agent Workflow with Foundry Local (Windows)
REM This script handles Python 3.13 compatibility issues

echo Installing Multi-Agent Workflow dependencies for Python 3.13...

REM First, ensure we have the latest pip
python -m pip install --upgrade pip

REM Install core dependencies first to avoid conflicts
echo Installing core dependencies...
pip install openai==2.3.0
pip install python-dotenv==1.1.1
pip install pydantic==1.10.24

REM Install HTTP dependencies
echo Installing HTTP client dependencies...
pip install httpx==0.28.1
pip install httpcore==1.0.9
pip install anyio==4.11.0
pip install h11==0.16.0

REM Install utilities
echo Installing utility packages...
pip install typing_extensions==4.15.0
pip install tqdm==4.67.1
pip install certifi==2025.10.5
pip install idna==3.11
pip install sniffio==1.3.1
pip install distro==1.9.0
pip install colorama==0.4.6
pip install jiter==0.11.0

REM Try to install agent-framework last
echo Installing agent-framework...
pip install agent-framework --no-deps
if %errorlevel% neq 0 (
    echo Warning: agent-framework installation had issues, trying alternatives...
    pip install microsoft-agent-framework --no-deps
    if %errorlevel% neq 0 (
        pip install azure-agent-framework --no-deps
        if %errorlevel% neq 0 (
            echo ERROR: Could not install agent-framework or its alternatives.
            echo Please check the package name or install manually.
            pause
            exit /b 1
        )
    )
)

echo Installation complete!
echo You can now run: python main.py
pause