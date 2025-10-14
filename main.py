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
	
	# Set logging to INFO to see more details about workflow execution
	logging.basicConfig(level=logging.INFO, format="%(message)s")
	logger = logging.getLogger(__name__)
	logger.warning("Starting FoundryLocal Planning Workflow")
	logger.warning("Available at: http://localhost:8093")
	logger.warning("Entity ID: workflow_foundrylocal_plan_research")
	logger.info("")
	logger.info("🔧 DevUI Troubleshooting Tips:")
	logger.info("• If output appears truncated, try refreshing the browser page")
	logger.info("• Use browser zoom (Ctrl+- or Ctrl++) to adjust text size")
	logger.info("• Check that the workflow completes all 3 agents: Plan → Research → Advisor")
	logger.info("• Try scrolling with mouse wheel or arrow keys in the response area")
	logger.info("")

	# Serve the composed workflow with tracing enabled for full output visibility
	serve(entities=[workflow], port=8093, auto_open=True, tracing_enabled=True)


if __name__ == "__main__":  # pragma: no cover
	main()

