# Requirements Setup Guide

This project has several requirements files to handle different installation scenarios and Python version compatibility issues.

## Python 3.13 Compatibility Notice

**Important**: If you're using Python 3.13, you may encounter dependency resolution issues due to some packages not being fully compatible yet. Use the step-by-step installation method below.

## Files Overview

### `requirements-minimal.txt` (Recommended for Python 3.13)
Minimal requirements with Python 3.13 compatible versions.

### `requirements.txt` 
The main requirements file with flexible version ranges for most use cases.

### `requirements-pinned.txt` 
Exact versions that are known to work together.

### Installation Scripts
- `install.bat` (Windows) - Handles Python 3.13 compatibility
- `install.sh` (Linux/macOS)

## Installation Options

### Option 1: Step-by-step (Recommended for Python 3.13)
```bash
# 1. Upgrade pip
python -m pip install --upgrade pip

# 2. Install core dependencies first
pip install openai==2.3.0
pip install python-dotenv==1.1.1
pip install pydantic==1.10.24

# 3. Install HTTP dependencies
pip install httpx==0.28.1 httpcore==1.0.9 anyio==4.11.0 h11==0.16.0

# 4. Install utilities
pip install typing_extensions==4.15.0 tqdm==4.67.1 certifi==2025.10.5
pip install idna==3.11 sniffio==1.3.1 distro==1.9.0 colorama==0.4.6 jiter==0.11.0

# 5. Install agent framework last (with --no-deps to avoid conflicts)
pip install agent-framework --no-deps
```

### Option 2: Use Installation Script (Windows)
```cmd
install.bat
```

### Option 3: Minimal Requirements
```bash
pip install -r requirements-minimal.txt
```

## Common Issues and Solutions

### Issue: Python 3.13 Dependency Resolution Errors
**Error**: `AttributeError: module 'collections' has no attribute 'MutableMapping'`

**Solution**: Use the step-by-step installation or the updated install.bat script. The issue is caused by older packages trying to resolve dependencies that are incompatible with Python 3.13.

### Issue: Long dependency resolution (backtracking)
**Error**: `INFO: This is taking longer than usual...`

**Solution**: 
1. Cancel the installation (Ctrl+C)
2. Use the step-by-step method above
3. Install agent-framework with `--no-deps` flag

### Issue: ImportError for agent_framework
**Solution**: Try alternative package names:
```bash
pip install microsoft-agent-framework --no-deps
# or
pip install azure-agent-framework --no-deps
```

### Issue: Pydantic compatibility errors
**Solution**: Ensure you're using Pydantic v1:
```bash
pip install pydantic==1.10.24
```

## Python Version Recommendations

- **Python 3.8-3.12**: Use any installation method
- **Python 3.13**: Use step-by-step installation or install.bat script
- **Python 3.14+**: May require additional compatibility updates

## Verification

After installation, test that everything works:
```bash
python test_simple.py
```

If the test passes, you can run the full application:
```bash
python main.py
```

## Environment Setup

Don't forget to configure your `.env` file:
```env
FOUNDRYLOCAL_ENDPOINT="http://127.0.0.1:58123/v1/"
FOUNDRYLOCAL_MODEL_DEPLOYMENT_NAME="Phi-3.5-mini-instruct-cuda-gpu:1"
OPENAI_CHAT_MODEL_ID="Phi-3.5-mini-instruct-cuda-gpu:1"
```

## Troubleshooting Specific Errors

### Error: "Getting requirements to build wheel did not run successfully"
This is a Python 3.13 compatibility issue. Use the step-by-step installation method.

### Error: "pip is looking at multiple versions"
This indicates dependency conflicts. Install packages individually in the order specified above.

### Error: Agent framework not found
The exact package name may vary. Try:
- `agent-framework`
- `microsoft-agent-framework` 
- `azure-agent-framework`