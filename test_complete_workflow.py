"""Complete workflow test without DevUI.

This test verifies that the full workflow (planning + research agents)
works correctly without the DevUI interface.
"""

import asyncio
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def test_workflow_execution():
    """Test the complete workflow execution."""
    
    logger.info("Testing complete workflow execution...")
    
    try:
        from workflow import workflow
        
        # Create a test message for the workflow
        test_prompt = "Create a comprehensive plan for developing a secure e-commerce website"
        
        logger.info(f"Sending prompt to workflow: {test_prompt}")
        
        # Run the workflow and collect all responses
        responses = []
        
        logger.info("Starting workflow.run_stream()...")
        async for response in workflow.run_stream(test_prompt):
            responses.append(response)
            logger.info(f"Received response #{len(responses)}: {type(response).__name__}")
            
            # Log response details
            if hasattr(response, 'contents'):
                content = str(response.contents)[:200] + "..." if len(str(response.contents)) > 200 else str(response.contents)
                logger.info(f"  Content: {content}")
            elif hasattr(response, 'content'):
                content = str(response.content)[:200] + "..." if len(str(response.content)) > 200 else str(response.content)
                logger.info(f"  Content: {content}")
            else:
                logger.info(f"  Response: {str(response)[:200]}...")
        
        logger.info(f"✅ Workflow completed successfully! Received {len(responses)} responses.")
        
        # Analyze the responses
        if responses:
            logger.info("Response Summary:")
            for i, response in enumerate(responses, 1):
                logger.info(f"  Response {i}: {type(response).__name__}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Workflow execution failed: {e}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return False


async def test_individual_agents():
    """Test individual agents to ensure they work separately."""
    
    logger.info("Testing individual agents...")
    
    try:
        from plan_agent import plan_agent
        from researcher_agent import researcher_agent
        
        # Test planning agent
        logger.info("Testing planning agent...")
        plan_thread = plan_agent.get_new_thread()
        plan_response = await plan_agent.run(
            "Create a plan for building an e-commerce website",
            thread=plan_thread
        )
        logger.info("✅ Planning agent working correctly")
        logger.info(f"Plan response preview: {str(plan_response)[:100]}...")
        
        # Test research agent
        logger.info("Testing research agent...")
        research_thread = researcher_agent.get_new_thread()
        research_response = await researcher_agent.run(
            "Research best practices for e-commerce security",
            thread=research_thread
        )
        logger.info("✅ Research agent working correctly")
        logger.info(f"Research response preview: {str(research_response)[:100]}...")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Individual agent test failed: {e}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return False


async def main():
    """Main test function."""
    
    logger.info("=" * 70)
    logger.info("COMPLETE WORKFLOW TEST WITHOUT DEVUI")
    logger.info("=" * 70)
    
    # Test 1: Individual agents
    logger.info("\n" + "=" * 50)
    logger.info("STEP 1: Testing Individual Agents")
    logger.info("=" * 50)
    
    if not await test_individual_agents():
        logger.error("❌ Individual agents test failed. Cannot proceed with workflow test.")
        return
    
    # Test 2: Complete workflow
    logger.info("\n" + "=" * 50)
    logger.info("STEP 2: Testing Complete Workflow")
    logger.info("=" * 50)
    
    if not await test_workflow_execution():
        logger.error("❌ Workflow execution test failed.")
        return
    
    logger.info("\n" + "=" * 70)
    logger.info("🎉 ALL TESTS PASSED!")
    logger.info("The workflow works correctly without DevUI.")
    logger.info("You can now run 'python main.py' to start with DevUI.")
    logger.info("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())