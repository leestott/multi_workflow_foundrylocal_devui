# Multi-Agent Workflow with Foundry Local

A multi-agent workflow application that demonstrates how to build AI-powered planning and research agents using Azure AI Foundry Local and the Agent Framework.

## Overview

This solution implements a collaborative workflow between two specialized AI agents:
- **Planning Agent**: Generates structured plans based on user requirements
- **Research Agent**: Expands and analyzes topics based on the planner's output

The agents work together through a concurrent workflow pattern, enabling sophisticated AI-powered task automation.

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
1. **Initializes** both planning and research agents
2. **Creates** a concurrent workflow builder
3. **Starts** a web server on `http://localhost:8091`
4. **Opens** the interface automatically in your browser
5. **Enables** you to interact with the multi-agent workflow through a chat interface

The DevUI makes it easy to:
- Send messages to trigger the planning workflow
- Watch as the planning agent creates structured plans
- See how the research agent expands on those plans
- Debug any issues with agent communication or model responses
- Test different scenarios and use cases interactively

## Prerequisites

- Python 3.8 or higher
- Azure AI Foundry Local running locally
- Git (for cloning the repository)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd multi_workflow_foundrylocal_devui
```

### 2. Install Python Dependencies

Create a virtual environment (recommended):

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

Install required packages:

```bash
pip install agent-framework
pip install python-dotenv
pip install openai
```

**Note**: The exact package names may vary. If you encounter import errors, you may need to install additional packages or use different package names based on your specific agent framework distribution.

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

Once everything is configured, start the application:

```bash
python main.py
```

The application will:
1. Load environment variables from `.env`
2. Initialize the planning and research agents
3. Start the DevUI web interface
4. Open automatically in your browser at `http://localhost:8091`

## Project Structure

```
├── main.py                 # Application entry point
├── .env                   # Environment configuration
├── plan_agent/           # Planning agent implementation
│   ├── __init__.py
│   └── agent.py
├── researcher_agent/     # Research agent implementation
│   ├── __init__.py
│   └── agent.py
├── workflow/            # Workflow orchestration
│   ├── __init__.py
│   └── workflow.py
└── README.md           # This file
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all required packages are installed in your active Python environment
2. **Connection Errors**: Verify that Foundry Local is running and accessible at the configured endpoint
3. **Model Not Found (400 Error)**: Check that the model name in your `.env` file matches an available model in your Foundry Local instance
4. **Environment Variable Issues**: Ensure the `.env` file is properly formatted with no missing quotes

### Checking Foundry Local Status

Verify your Foundry Local instance is working:

```bash
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"
```

This should return a list of available models.

## Features

- **Multi-Agent Collaboration**: Coordinated workflow between specialized agents
- **Local AI Processing**: All AI operations run locally through Foundry Local
- **Web Interface**: Interactive DevUI for testing and monitoring workflows
- **Extensible Architecture**: Easy to add new agents or modify existing workflows
- **Tracing Support**: Built-in observability for debugging and monitoring

## Development Workflow

### Using the DevUI
1. **Start the application**: `python main.py`
2. **Open the web interface**: Navigate to `http://localhost:8091` (opens automatically)
3. **Interact with agents**: Send messages through the chat interface
4. **Monitor execution**: Watch the workflow execute in real-time
5. **Debug issues**: Use the built-in tracing and error reporting

### Example Interaction Flow
1. **User Input**: "Create a plan for building a web application"
2. **Planning Agent**: Generates a structured development plan
3. **Research Agent**: Expands on the plan with detailed implementation guidance
4. **User Feedback**: Review results and iterate on the plan

## Learn More

- [Edge AI for Beginners Course](https://aka.ms/edgeai-for-beginners) - Comprehensive guide to AI development
- [Azure AI Foundry Documentation](https://docs.microsoft.com/azure/ai-studio/) - Official documentation
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) - Framework-specific guides and API documentation
- [Agent Framework DevUI Documentation](https://github.com/microsoft/agent-framework/tree/main/docs/devui) - DevUI setup and usage guides
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference) - API reference for model interactions

## License


This project is licensed under the MIT License - see the LICENSE file for details.
