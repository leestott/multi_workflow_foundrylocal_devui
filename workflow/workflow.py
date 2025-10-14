"""Workflow wiring for FoundryLocal planning + research + advisor agents.

Structure creates a sequential three-agent workflow:
1. Planning Agent: Analyzes user requests and creates detailed plans
2. Research Agent: Conducts thorough research based on the plan
3. Advisor Agent: Synthesizes findings and provides final recommendations

The workflow uses WorkflowBuilder for better DevUI compatibility and
to avoid serialization issues with ChatMessage types.
"""

from agent_framework import (
	AgentExecutor,
	WorkflowBuilder,
)

from plan_agent import plan_agent
from researcher_agent import researcher_agent
from advisor_agent import advisor_agent




# Create agent executors
planner_executor = AgentExecutor(plan_agent, id="plan_agent")  # type: ignore
research_executor = AgentExecutor(researcher_agent, id="researcher_agent")  # type: ignore
advisor_executor = AgentExecutor(advisor_agent, id="advisor_agent")  # type: ignore


# Create a simple workflow using WorkflowBuilder for better DevUI compatibility
# Flow: planner -> researcher -> advisor
workflow = (
	WorkflowBuilder()
	.add_agent(planner_executor)
	.add_agent(research_executor)
	.add_agent(advisor_executor)
	.add_edge(planner_executor, research_executor)
	.add_edge(research_executor, advisor_executor)
	.set_start_executor(planner_executor)
	.build()
)

    