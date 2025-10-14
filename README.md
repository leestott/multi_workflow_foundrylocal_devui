# Multi-Agent Workflow with Foundry Local

A multi-agent workflow application that demonstrates how to build AI-powered planning, research, and advisor agents using Azure AI Foundry Local and the Agent Framework.

## Overview

This solution implements a collaborative workflow between three specialized AI agents:
- **Planning Agent**: Generates structured plans based on user requirements
- **Research Agent**: Expands and analyzes topics based on the planner's output
- **Advisor Agent**: Synthesizes the plan and research into a final, well-structured recommendation for the user

The agents work together through a sequential workflow pattern (Plan → Research → Advisor), enabling sophisticated AI-powered task automation and comprehensive recommendations.

## What is Foundry Local?

Azure AI Foundry Local is a containerized local development environment that allows you to run AI models locally on your machine. It provides:

- **Local Model Hosting**: Run popular open-source models like Phi-3.5, GPT models, and others locally
- **OpenAI-Compatible API**: Standard REST API that works with OpenAI client libraries
- **Development Environment**: Perfect for prototyping, testing, and development without cloud dependencies
- **Privacy & Control**: Keep your data local while developing AI applications

For a comprehensive guide to getting started with AI development, check out the [Edge AI for Beginners course](https://aka.ms/edgeai-for-beginners).

## Microsoft Agent Framework

The **Microsoft Agent Framework** is a powerful Python library designed to simplify the development of AI agents and multi-agent workflows. It provides:

### Core Features
- **Agent Creation**: Simple APIs to create AI agents with specific roles and capabilities
- **Multi-Agent Orchestration**: Built-in support for coordinating multiple agents in complex workflows
- **OpenAI Integration**: Seamless integration with OpenAI-compatible APIs (including Foundry Local)
- **Workflow Management**: Tools for creating sequential, parallel, and conditional agent interactions
- **Message Handling**: Robust message passing and state management between agents
- **Extensibility**: Plugin architecture for custom tools and integrations

### Key Components
- **AgentExecutor**: Manages the execution lifecycle of individual agents
- **WorkflowBuilder**: Creates complex multi-agent workflows with various execution patterns
- **ChatClient**: Handles communication with language models (OpenAI, Azure OpenAI, local models)
- **Message System**: Structured message passing with support for different roles and content types

## Agent Framework DevUI

The **Agent Framework DevUI** is an interactive web interface that provides a development and testing environment for your AI agents and workflows. It offers:

### Development Features
- **Interactive Chat Interface**: Test your agents through a user-friendly chat interface
- **Real-time Workflow Visualization**: See how messages flow between agents in your workflow
- **Agent Monitoring**: Monitor individual agent performance and responses
- **Debug Tools**: Built-in debugging capabilities for troubleshooting agent behavior
- **Live Configuration**: Modify agent parameters and see changes in real-time

### User Experience
- **Web-based Interface**: Access your agents through any modern web browser
- **Auto-opening**: Automatically launches in your default browser when started
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Updates**: See agent responses as they're generated (streaming support)

### Observability & Tracing
- **Execution Tracing**: Track the complete execution path of multi-agent workflows
- **Performance Metrics**: Monitor response times, token usage, and other key metrics
- **Error Handling**: Clear error reporting and debugging information
- **Workflow Analytics**: Understand how your agents interact and perform over time

### How It Works in This Solution
When you run `python main.py`, the DevUI:
1. **Initializes** the planning, research, and advisor agents
2. **Creates** a sequential workflow (Plan → Research → Advisor)
3. **Starts** a web server on `http://localhost:8093`
4. **Opens** the interface automatically in your browser
5. **Enables** you to interact with the multi-agent workflow through a chat interface

The DevUI makes it easy to:
- Send messages to trigger the planning workflow
- Watch as the planning agent creates structured plans
- See how the research agent expands on those plans
- Receive a final, well-structured recommendation from the advisor agent
- Debug any issues with agent communication or model responses
- Test different scenarios and use cases interactively

## Prerequisites

- Python 3.8 or higher
- Azure AI Foundry Local running locally
- Git (for cloning the repository)

## Setup Instructions

### Quick Setup (Recommended)

**Windows PowerShell (One Command Setup):**
```powershell
# Install everything including Chainlit
powershell -ExecutionPolicy Bypass -File setup.ps1

# Or install without Chainlit
powershell -ExecutionPolicy Bypass -File setup.ps1 -SkipChainlit
```

### Manual Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd multi_workflow_foundrylocal_devui
```

### 2. Install Python Dependencies

Create a virtual environment (recommended):

```bash
# Create virtual environment
python -m venv foundrylocal

# Activate virtual environment
# Windows:
foundrylocal\Scripts\activate
# macOS/Linux:
source foundrylocal/bin/activate
```

Install required packages:

```bash
# For Chainlit frontend (recommended)
pip install -r requirements-chainlit.txt

# Or for core functionality only
pip install -r requirements.txt
```

### 3. Set up Azure AI Foundry Local

Ensure Azure AI Foundry Local is running on your machine. 
The default configuration expects it to be available at `http://127.0.0.1:58123`. 
You can run foundry service status to confirm the port and update the .env file with the correct port ID.

### 4. Configure Environment Variables

Create or update the `.env` file in the project root with the following settings:

```env
FOUNDRYLOCAL_ENDPOINT="http://127.0.0.1:58123/v1/"
FOUNDRYLOCAL_MODEL_DEPLOYMENT_NAME="Phi-3.5-mini-instruct-cuda-gpu:1"
OPENAI_CHAT_MODEL_ID="Phi-3.5-mini-instruct-cuda-gpu:1"
```

## Environment Configuration

### `.env` Settings Explained

| Variable | Description | Example |
|----------|-------------|---------|
| `FOUNDRYLOCAL_ENDPOINT` | The base URL for your Foundry Local API endpoint | `"http://127.0.0.1:58123/v1/"` |
| `FOUNDRYLOCAL_MODEL_DEPLOYMENT_NAME` | The specific model deployment name available in your Foundry Local instance | `"Phi-3.5-mini-instruct-cuda-gpu:1"` |
| `OPENAI_CHAT_MODEL_ID` | The model ID used by the OpenAI client (should match the deployment name) | `"Phi-3.5-mini-instruct-cuda-gpu:1"` |

### Finding Available Models

To see which models are available in your Foundry Local instance, you can query the models endpoint:

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

Common available models include:
- `Phi-3.5-mini-instruct-cuda-gpu:1`
- `gpt-oss-20b-cuda-gpu:0`

## Running the Application

This project provides **two frontend options** for interacting with the multi-agent workflow:

### Option 1: DevUI (Agent Framework Default)

The **Agent Framework DevUI** provides a comprehensive development and testing environment:

```bash
# Start the DevUI
python main.py
```

**Features:**
- **Development-focused interface** with detailed workflow visualization
- **Real-time tracing** and debugging capabilities
- **Agent monitoring** and performance metrics
- **Automatic browser opening** at `http://localhost:8093`
- **Full workflow observability** for troubleshooting

**Best for:** Development, debugging, and detailed workflow analysis

### Option 2: Chainlit (Recommended for Users)

The **Chainlit frontend** provides a clean, modern chat interface:

#### Quick Start Commands

**Windows PowerShell (Recommended):**
```powershell
./run_chainlit.ps1
```

**Windows Command Prompt:**
```cmd
run_chainlit.bat
```

**Linux/macOS:**
```bash
./run_chainlit.sh
```

#### Manual Start
```bash
# With virtual environment activated
python -m chainlit run chainlit_app_simple.py --port 8001

# Or with full path (Windows)
foundrylocal\Scripts\python.exe -m chainlit run chainlit_app_simple.py --port 8001
```

**Features:**
- **Clean chat interface** optimized for conversations
- **Real-time agent progress** indicators
- **Mobile-responsive design** works on all devices
- **User-friendly error handling** with troubleshooting tips
- **Accessible at** `http://localhost:8001`

**Best for:** End users, interactive conversations, and production use

### Prerequisites for Both Options

Before running either frontend:

1. **Ensure FoundryLocal is running** at your configured endpoint
2. **Verify your `.env` file** is properly configured
3. **Check that all dependencies** are installed
4. **Confirm the virtual environment** is set up correctly

### Application Startup Process

Both applications will:
1. **Load environment variables** from `.env`
2. **Initialize the three agents** (Plan → Research → Advisor)
3. **Start the web interface** on their respective ports
4. **Display startup messages** with access URLs and troubleshooting tips

## Chainlit Frontend Details

### Launch Scripts Features

The provided launch scripts (`run_chainlit.ps1`, `run_chainlit.bat`, `run_chainlit.sh`) automatically:
- **Check prerequisites** and prompt for FoundryLocal status
- **Activate the virtual environment** (`foundrylocal/`)
- **Start the Chainlit server** on port 8001
- **Provide helpful status messages** and error handling
- **Wait for user confirmation** before starting

### Chainlit Interface Features

- **Clean Chat Interface**: Modern, user-friendly chat experience
- **Real-time Progress**: See each agent working on your request
- **Agent-Specific Responses**: Separate outputs from Plan, Research, and Advisor agents
- **Error Handling**: Clear error messages and troubleshooting guidance
- **Mobile Responsive**: Works on desktop and mobile devices
- **Workflow Execution**: Uses `await workflow.run(user_input)` for proper agent orchestration
- **Chainlit API Compliance**: Correctly handles message updates using `msg.content = new_content` followed by `await msg.update()`

### Example Usage Flow

1. **Start the app** using one of the launch scripts
2. **Open** `http://localhost:8001` in your browser
3. **Send a message** like "Create a plan for building a web application"
4. **Watch the progress** as each agent processes your request:
   - 📋 **Planning Agent** creates a structured plan
   - 🔍 **Research Agent** expands with detailed research
   - 💡 **Advisor Agent** provides final recommendations
5. **Receive a comprehensive response** with all three agent outputs

### Troubleshooting Chainlit

If you encounter issues:
- **Check FoundryLocal** is running at the configured endpoint
- **Verify your `.env` file** has correct settings
- **Ensure dependencies** are installed in the virtual environment
- **Check port availability** (8001 for Chainlit, 8093 for DevUI)
- **Review terminal output** for specific error messages

The Chainlit frontend provides the same three-agent workflow (Plan → Research → Advisor) but with a more focused chat experience ideal for interactive conversations.

## Quick Start Guide

### 1. Choose Your Frontend

**For Development & Debugging:**
```bash
python main.py
# Opens DevUI at http://localhost:8093
```

**For User Interactions:**
```bash
./run_chainlit.ps1    # Windows PowerShell
run_chainlit.bat      # Windows Command Prompt  
./run_chainlit.sh     # Linux/macOS
# Opens Chainlit at http://localhost:8001
```

### 2. Example Workflow

Try these sample requests to test the multi-agent workflow:

**Business Planning:**
> "Create a plan for launching a new SaaS product in the healthcare market"

**Technical Projects:**
> "Plan the development of a real-time chat application with user authentication"

**Marketing Strategy:**
> "Develop a digital marketing strategy for a small e-commerce business"

**Research Projects:**
> "Design a machine learning project for customer behavior analysis"

### 3. Understanding the Agent Flow

Each request goes through three specialized agents:

1. **📋 Planning Agent**: Analyzes your request and creates a structured, actionable plan
2. **🔍 Research Agent**: Conducts thorough research to expand and validate the plan
3. **💡 Advisor Agent**: Synthesizes findings into final recommendations with:
   - 🎯 Executive Summary
   - 📊 Key Findings & Analysis  
   - 🔥 Priority Recommendations
   - ⚠️ Risk Assessment & Mitigation
   - 📈 Success Metrics & Monitoring
   - 💡 Additional Considerations

## Advisor Agent Output Structure

The Advisor agent always provides a complete, well-structured final recommendation with the following sections:

1. **🎯 Executive Summary**: Concise overview and primary recommendation
2. **📊 Key Findings & Analysis**: Insights, patterns, and supporting evidence
3. **🔥 Priority Recommendations**: Immediate, short-term, and long-term actions
4. **⚠️ Risk Assessment & Mitigation**: Potential obstacles and contingency plans
5. **📈 Success Metrics & Monitoring**: KPIs, review checkpoints, and tracking methods
6. **💡 Additional Considerations**: Limitations, further research, and alternatives

This ensures users always receive a solid, actionable, and complete answer.

## Project Structure

```
├── main.py                 # Application entry point
├── .env                    # Environment configuration
├── plan_agent/             # Planning agent implementation
│   ├── __init__.py
│   └── agent.py
├── researcher_agent/       # Research agent implementation
│   ├── __init__.py
│   └── agent.py
├── advisor_agent/          # Advisor agent implementation (final recommendations)
│   ├── __init__.py
│   └── agent.py
├── workflow/               # Workflow orchestration
│   ├── __init__.py
│   └── workflow.py
└── README.md               # This file
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all required packages are installed in your active Python environment
2. **Connection Errors**: Verify that Foundry Local is running and accessible at the configured endpoint
3. **Model Not Found (400 Error)**: Check that the model name in your `.env` file matches an available model in your Foundry Local instance
4. **Environment Variable Issues**: Ensure the `.env` file is properly formatted with no missing quotes
5. **Output Truncation or Looping**: The advisor agent is designed to always provide a complete, well-structured response. If output appears cut off, refresh the browser or check the `.env` and agent instructions for completeness.
6. **DevUI Scroll/Visibility**: If you can't see the full output, try scrolling with your mouse wheel, arrow keys, or adjust browser zoom. The DevUI is optimized for large, structured responses.

### Checking Foundry Local Status

Verify your Foundry Local instance is working:

```bash
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"
```

This should return a list of available models.

## Features

- **Multi-Agent Collaboration**: Coordinated workflow between specialized agents (Plan, Research, Advisor)
- **Advisor Agent**: Provides a comprehensive, well-structured final recommendation synthesizing all prior outputs
- **Local AI Processing**: All AI operations run locally through Foundry Local
- **Web Interface**: Interactive DevUI for testing and monitoring workflows
- **Extensible Architecture**: Easy to add new agents or modify existing workflows
- **Tracing Support**: Built-in observability for debugging and monitoring

## Development Workflow

### Using the DevUI
1. **Start the application**: `python main.py`
2. **Open the web interface**: Navigate to `http://localhost:8093` (opens automatically)
3. **Interact with agents**: Send messages through the chat interface
4. **Monitor execution**: Watch the workflow execute in real-time
5. **Debug issues**: Use the built-in tracing and error reporting

### Example Interaction Flow
1. **User Input**: "Create a plan for building a web application"
2. **Planning Agent**: Generates a structured development plan
3. **Research Agent**: Expands on the plan with detailed implementation guidance
4. **Advisor Agent**: Synthesizes the plan and research into a final, actionable recommendation (with executive summary, key findings, prioritized actions, risk assessment, and success metrics)
5. **User Feedback**: Review results and iterate on the plan

## Learn More

- [Edge AI for Beginners Course](https://aka.ms/edgeai-for-beginners) - Comprehensive guide to AI development
- [Azure AI Foundry Documentation](https://docs.microsoft.com/azure/ai-studio/) - Official documentation
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) - Framework-specific guides and API documentation
- [Agent Framework DevUI Documentation](https://github.com/microsoft/agent-framework/tree/main/docs/devui) - DevUI setup and usage guides
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference) - API reference for model interactions

## License


This project is licensed under the MIT License - see the LICENSE file for details.
