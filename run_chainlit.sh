#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Starting Chainlit Multi-Agent Workflow Assistant..."
echo ""
echo "Make sure FoundryLocal is running before proceeding."
echo ""
read -p "Press Enter to continue..."
echo ""

echo "Activating virtual environment..."
if [ -f "foundrylocal/bin/activate" ]; then
    source foundrylocal/bin/activate
elif [ -f "foundrylocal/Scripts/activate" ]; then
    source foundrylocal/Scripts/activate
else
    echo "ERROR: Virtual environment not found"
    echo "Please ensure the foundrylocal virtual environment exists"
    exit 1
fi

echo ""
echo "Starting Chainlit app at http://localhost:8001..."
echo "Press Ctrl+C to stop the server"
echo ""

python -m chainlit run chainlit_app_simple.py --port 8001

echo ""
echo "Chainlit server stopped."