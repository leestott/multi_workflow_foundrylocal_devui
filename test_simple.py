"""Simple test to verify agent functionality without complex workflow calls.

This test focuses on basic agent initialization and simple interaction
to isolate the core issues.
"""

import asyncio
import logging
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def test_agent_initialization():
    """Test if agents initialize correctly."""
    
    logger.info("Testing agent initialization...")
    
    try:
        from plan_agent import plan_agent
        from researcher_agent import researcher_agent
        
        logger.info(f"Plan agent: {type(plan_agent) if plan_agent else 'None'}")
        logger.info(f"Research agent: {type(researcher_agent) if researcher_agent else 'None'}")
        
        if plan_agent is None:
            logger.error("Plan agent failed to initialize")
            return False
            
        if researcher_agent is None:
            logger.error("Research agent failed to initialize")
            return False
            
        logger.info("✅ Both agents initialized successfully")
        return True
        
    except Exception as e:
        logger.error(f"Agent initialization failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False


async def test_simple_agent_call():
    """Test a simple agent call to see what the exact error is."""
    
    logger.info("Testing simple agent call...")
    
    try:
        from plan_agent import plan_agent
        
        if plan_agent is None:
            logger.error("Plan agent is None")
            return False
        
        # Try to get a simple response - let's see what methods are available
        logger.info(f"Plan agent methods: {[method for method in dir(plan_agent) if not method.startswith('_')]}")
        
        # Try calling run_stream with a simple string first
        logger.info("Trying to call run_stream...")
        
        # Let's see what happens with just a thread
        if hasattr(plan_agent, 'get_new_thread'):
            thread = plan_agent.get_new_thread()
            logger.info(f"Got thread: {type(thread)}")
            
            # Try to run with the thread using the correct method
            logger.info("Calling plan_agent.run() method...")
            response = await plan_agent.run(
                "Create a simple plan",
                thread=thread
            )
            logger.info(f"Got response: {response}")
            return True
            
        else:
            logger.error("Agent doesn't have get_new_thread method")
            return False
            
    except Exception as e:
        logger.error(f"Simple agent call failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False


async def test_workflow_components():
    """Test the workflow components individually."""
    
    logger.info("Testing workflow components...")
    
    try:
        from workflow import workflow
        logger.info(f"Workflow type: {type(workflow)}")
        logger.info(f"Workflow methods: {[method for method in dir(workflow) if not method.startswith('_')]}")
        
        # Check if workflow has the expected methods
        if hasattr(workflow, 'run_stream'):
            logger.info("✅ Workflow has run_stream method")
        else:
            logger.error("❌ Workflow missing run_stream method")
            return False
            
        return True
        
    except Exception as e:
        logger.error(f"Workflow component test failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False


async def main():
    """Main test function."""
    
    logger.info("=" * 60)
    logger.info("SIMPLE WORKFLOW DIAGNOSTICS")
    logger.info("=" * 60)
    
    # Step 1: Test agent initialization
    if not test_agent_initialization():
        logger.error("❌ Agent initialization failed - check .env file and Foundry Local")
        return
    
    # Step 2: Test workflow components
    if not await test_workflow_components():
        logger.error("❌ Workflow components test failed")
        return
    
    # Step 3: Test simple agent call
    if not await test_simple_agent_call():
        logger.error("❌ Simple agent call failed")
        return
    
    logger.info("✅ All basic tests passed!")


if __name__ == "__main__":
    asyncio.run(main())