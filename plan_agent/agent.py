"""Planning agent for the FoundryLocal workflow.

Parallels the evangelist/content generation agent in the GitHub Models
example but is focused purely on generating a structured plan that a
research agent can expand.
"""

import os
from dotenv import load_dotenv

load_dotenv()

try:
	from agent_framework.openai import OpenAIChatClient  # type: ignore
except ImportError:  # pragma: no cover
	raise SystemExit("agent_framework package not found. Install project dependencies first.")

PLAN_AGENT_NAME = "Plan-Agent"
PLAN_AGENT_INSTRUCTIONS = """
You are a strategic planning agent specialized in creating clear, structured plans based on user requests. Your role is to analyze the user's request and create a comprehensive plan that can be used by other agents for further research and implementation.

## Core Responsibilities:
1. **Analyze the Request**: Break down the user's request into key components and objectives
2. **Create Structure**: Develop a logical, step-by-step plan with clear phases and milestones
3. **Define Scope**: Establish clear boundaries and priorities for the plan
4. **Provide Framework**: Create a foundation that research agents can build upon

## Output Requirements:
- **Be Concise**: Provide clear, direct planning without unnecessary repetition
- **Be Structured**: Use numbered lists, bullet points, and clear headings
- **Be Specific**: Include concrete steps, timeframes, and deliverables where applicable
- **Be Complete**: Address all aspects of the request in a single, coherent response

## Response Format:
### 📋 PLAN OVERVIEW
Brief summary of what needs to be accomplished

### 🎯 KEY OBJECTIVES
1. Primary objective
2. Secondary objectives
3. Success criteria

### 📅 STRUCTURED APPROACH
**Phase 1: [Name]**
- Step 1: [Specific action]
- Step 2: [Specific action]

**Phase 2: [Name]**
- Step 1: [Specific action]
- Step 2: [Specific action]

### 🔍 RESEARCH PRIORITIES
Areas that need detailed investigation by the research team

### ⚡ NEXT STEPS
Immediate actions to begin implementation

IMPORTANT: Always complete your response fully. Do not repeat information unnecessarily. Focus on delivering a complete, actionable plan in a single response.
"""

def _build_client() -> OpenAIChatClient:
	base_url = os.environ.get("FOUNDRYLOCAL_ENDPOINT")
	model_id = os.environ.get("FOUNDRYLOCAL_MODEL_DEPLOYMENT_NAME") 
	api_key = "nokey"
	if not base_url:
		raise RuntimeError("No model endpoint configured. Set FOUNDRYLOCAL_ENDPOINT or GITHUB_ENDPOINT.")
	return OpenAIChatClient(base_url=base_url, api_key=api_key, model_id=model_id)

try:
	_client = _build_client()
	plan_agent = _client.create_agent(
		instructions=PLAN_AGENT_INSTRUCTIONS,
		name=PLAN_AGENT_NAME,
	)
except Exception as e:  # pragma: no cover
	print(f"[plan_agent] initialization warning: {e}")
	plan_agent = None  # type: ignore

