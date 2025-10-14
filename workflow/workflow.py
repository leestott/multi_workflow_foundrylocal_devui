"""Workflow wiring for FoundryLocal planning + research agents.

Structure mirrors the pattern used in the GitHub Models multi-step
workflow (`multi_workflow_ghmodel_devui/workflow/workflow.py`). We
compose two agent executors with a transformation executor between them
to map JSON model outputs into the next agent's user message.
"""

from agent_framework import (
	AgentExecutor,
	WorkflowBuilder,
)

from plan_agent import plan_agent
from researcher_agent import researcher_agent




# Create agent executors
planner_executor = AgentExecutor(plan_agent, id="plan_agent")  # type: ignore
research_executor = AgentExecutor(researcher_agent, id="researcher_agent")  # type: ignore


# Create a simple workflow using WorkflowBuilder for better DevUI compatibility
workflow = (
	WorkflowBuilder()
	.add_agent(planner_executor)
	.add_agent(research_executor)
	.add_edge(planner_executor, research_executor)
	.set_start_executor(planner_executor)
	.build()
)

    