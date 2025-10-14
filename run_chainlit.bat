@echo off
echo Starting Chainlit Multi-Agent Workflow Assistant...
echo.
echo Make sure FoundryLocal is running before proceeding.
echo.
echo Press any key to continue...
pause >nul
echo.
echo Activating virtual environment...
call "%~dp0foundrylocal\Scripts\activate.bat"
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    echo Please ensure the foundrylocal virtual environment exists
    pause
    exit /b 1
)
echo.
echo Starting Chainlit app at http://localhost:8001...
echo Press Ctrl+C to stop the server
echo.
"%~dp0foundrylocal\Scripts\python.exe" -m chainlit run "%~dp0chainlit_app_simple.py" --port 8001
echo.
echo Chainlit server stopped.
pause