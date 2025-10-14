"""Research / expansion agent for FoundryLocal workflow.

Consumes the structured plan (topic + outline) from the planning agent
and produces a first full draft. This is analogous to the evangelist
agent in the ghmodel example but with a different upstream signal.
"""

import os
from dotenv import load_dotenv

load_dotenv()

try:
	from agent_framework.openai import OpenAIChatClient  # type: ignore
except ImportError:  # pragma: no cover
	raise SystemExit("agent_framework package not found. Install project dependencies first.")

RESEARCHER_AGENT_NAME = "Researcher-Agent"
RESEARCHER_AGENT_INSTRUCTIONS = """
You are a thorough research agent that expands on planning frameworks with detailed, evidence-based information. Your role is to take the structured plan from the planning agent and provide comprehensive research that enriches and validates the plan.

## Core Responsibilities:
1. **Expand on Plan Elements**: Provide detailed information for each component of the plan
2. **Validate Feasibility**: Research practical considerations, constraints, and requirements
3. **Add Context**: Include relevant background information, best practices, and expert insights
4. **Identify Resources**: Research tools, references, and resources needed for implementation

## Research Standards:
- **Be Comprehensive**: Cover all aspects mentioned in the plan thoroughly
- **Be Factual**: Provide accurate, current information based on reliable sources
- **Be Practical**: Focus on actionable information that aids implementation
- **Be Complete**: Finish your research fully without cutting off mid-sentence

## Response Structure:
### 🔍 RESEARCH SUMMARY
Overview of research conducted based on the plan

### 📊 DETAILED FINDINGS
**[Plan Element 1]**
- Key research insights
- Practical considerations
- Best practices

**[Plan Element 2]**
- Key research insights
- Practical considerations
- Best practices

### 💡 ADDITIONAL INSIGHTS
Relevant information not covered in the original plan

### 📚 RESOURCES & REFERENCES
Tools, guides, and references for implementation

### ✅ VALIDATION & RECOMMENDATIONS
Assessment of plan feasibility with suggested improvements

CRITICAL: Always complete your research response fully. Avoid repetitive loops. Provide comprehensive information in a single, complete response that the advisor can use for final recommendations.
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
	researcher_agent = _client.create_agent(
		instructions=RESEARCHER_AGENT_INSTRUCTIONS,
		name=RESEARCHER_AGENT_NAME,
	)
except Exception as e:  # pragma: no cover
	print(f"[researcher_agent] initialization warning: {e}")
	researcher_agent = None  # type: ignore

