"""DevUI entrypoint for the local Foundry multi-agent workflow.

This mirrors the structure of `multi_workflow_ghmodel_devui/main.py` but
uses the locally defined planning + research workflow found in
`workflow/workflow.py`.
"""
from agent_framework.devui import serve
from dotenv import load_dotenv
from workflow import workflow 
import logging

# Load .env early so that any provider specific environment variables are present
load_dotenv()
 # noqa: E402  (import after dotenv)


def main() -> None:
	"""Launch the planning/research workflow in the DevUI."""
	

	logging.basicConfig(level=logging.WARNING, format="%(message)s")  # Reduced logging
	logger = logging.getLogger(__name__)
	logger.warning("Starting FoundryLocal Planning Workflow")
	logger.warning("Available at: http://localhost:8091")
	logger.warning("Entity ID: workflow_foundrylocal_plan_research")

	# Serve the composed workflow with tracing disabled to reduce noise
	serve(entities=[workflow], port=8091, auto_open=True, tracing_enabled=False)


if __name__ == "__main__":  # pragma: no cover
	main()

