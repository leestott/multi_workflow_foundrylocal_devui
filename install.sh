#!/bin/bash
# Install script for Multi-Agent Workflow with Foundry Local
# This script helps resolve common dependency issues

echo "Installing Multi-Agent Workflow dependencies..."

# First, ensure we have the latest pip
python -m pip install --upgrade pip

# Install Pydantic v1 first to avoid conflicts
echo "Installing Pydantic v1 for compatibility..."
pip install "pydantic>=1.10.0,<2.0.0"

# Install core dependencies
echo "Installing core dependencies..."
pip install python-dotenv>=1.0.0
pip install "openai>=1.0.0,<3.0.0"

# Install HTTP dependencies
echo "Installing HTTP client dependencies..."
pip install httpx>=0.25.0
pip install httpcore>=1.0.0
pip install anyio>=4.0.0

# Try to install agent-framework
echo "Installing agent-framework..."
pip install agent-framework || {
    echo "Failed to install agent-framework, trying alternatives..."
    pip install microsoft-agent-framework || pip install azure-agent-framework || {
        echo "ERROR: Could not install agent-framework or its alternatives."
        echo "Please check the package name or install manually."
        exit 1
    }
}

# Install remaining dependencies
echo "Installing remaining dependencies..."
pip install -r requirements.txt

echo "Installation complete!"
echo "You can now run: python main.py"