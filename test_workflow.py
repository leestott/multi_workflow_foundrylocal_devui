"""Test script to verify workflow functionality without DevUI.

This script tests the core workflow functionality by directly calling
the workflow's run_stream method to isolate any non-DevUI issues.
"""

import asyncio
import logging
from dotenv import load_dotenv
from workflow import workflow
from agent_framework import ChatMessage, Role

# Load environment variables
load_dotenv()

# Set up logging to see what's happening
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def test_workflow_direct():
    """Test the workflow directly without DevUI."""
    
    logger.info("Starting direct workflow test...")
    
    # Test message to send to the workflow
    test_message = ChatMessage(
        role=Role.USER,
        contents="Create a plan for building a simple web application with user authentication"
    )
    
    logger.info(f"Sending test message: {test_message.contents}")
    
    try:
        # Test if we can call run_stream on the workflow
        logger.info("Calling workflow.run_stream()...")
        
        response_count = 0
        async for response in workflow.run_stream([test_message]):
            response_count += 1
            logger.info(f"Response #{response_count}: {type(response).__name__}")
            
            # Print response details
            if hasattr(response, 'messages') and response.messages:
                for msg in response.messages:
                    content = getattr(msg, 'contents', getattr(msg, 'content', str(msg)))
                    logger.info(f"  Message from {msg.role}: {str(content)[:100]}...")
            elif hasattr(response, 'contents'):
                logger.info(f"  Contents: {response.contents[:100]}...")
            elif hasattr(response, 'content'):
                logger.info(f"  Content: {response.content[:100]}...")
            else:
                logger.info(f"  Response: {str(response)[:100]}...")
        
        logger.info(f"Workflow completed successfully! Received {response_count} responses.")
        return True
        
    except Exception as e:
        logger.error(f"Workflow execution failed: {e}")
        logger.error(f"Error type: {type(e).__name__}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return False


async def test_agents_individually():
    """Test individual agents to isolate issues."""
    
    logger.info("Testing individual agents...")
    
    # Import agents directly
    from plan_agent import plan_agent
    from researcher_agent import researcher_agent
    
    # Test planning agent
    logger.info("Testing planning agent...")
    if plan_agent is None:
        logger.error("Planning agent is None - check agent initialization")
        return False
    
    try:
        plan_messages = [ChatMessage(
            role=Role.USER,
            contents="Create a plan for a simple web app"
        )]
        
        logger.info("Calling plan_agent.run_stream()...")
        async for update in plan_agent.run_stream(plan_messages):
            logger.info(f"Plan agent response: {str(update)[:100]}...")
            break  # Just test first response
            
        logger.info("Planning agent test successful!")
        
    except Exception as e:
        logger.error(f"Planning agent failed: {e}")
        return False
    
    # Test research agent
    logger.info("Testing research agent...")
    if researcher_agent is None:
        logger.error("Research agent is None - check agent initialization")
        return False
    
    try:
        research_messages = [ChatMessage(
            role=Role.USER,
            contents="Research best practices for web authentication"
        )]
        
        logger.info("Calling researcher_agent.run_stream()...")
        async for update in researcher_agent.run_stream(research_messages):
            logger.info(f"Research agent response: {str(update)[:100]}...")
            break  # Just test first response
            
        logger.info("Research agent test successful!")
        return True
        
    except Exception as e:
        logger.error(f"Research agent failed: {e}")
        return False


async def main():
    """Main test function."""
    
    logger.info("=" * 60)
    logger.info("WORKFLOW TEST WITHOUT DEVUI")
    logger.info("=" * 60)
    
    # Check if agents are properly initialized
    from plan_agent import plan_agent
    from researcher_agent import researcher_agent
    
    logger.info(f"Plan agent status: {'OK' if plan_agent else 'FAILED'}")
    logger.info(f"Research agent status: {'OK' if researcher_agent else 'FAILED'}")
    
    if not plan_agent or not researcher_agent:
        logger.error("Agents are not properly initialized. Check .env configuration.")
        return
    
    # Test individual agents first
    logger.info("\n" + "=" * 40)
    logger.info("TESTING INDIVIDUAL AGENTS")
    logger.info("=" * 40)
    
    agents_ok = await test_agents_individually()
    
    if not agents_ok:
        logger.error("Individual agent tests failed. Stopping workflow test.")
        return
    
    # Test full workflow
    logger.info("\n" + "=" * 40)
    logger.info("TESTING FULL WORKFLOW")
    logger.info("=" * 40)
    
    workflow_ok = await test_workflow_direct()
    
    if workflow_ok:
        logger.info("\n✅ All tests passed! Workflow is working correctly without DevUI.")
    else:
        logger.error("\n❌ Workflow test failed. Check the logs above for details.")


if __name__ == "__main__":
    asyncio.run(main())