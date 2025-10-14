"""Chainlit frontend for the FoundryLocal multi-agent workflow.

This provides an alternative web interface to the DevUI using Chainlit,
offering a more streamlined chat experience for the Plan → Research → Advisor workflow.
"""

import chainlit as cl
import asyncio
import logging
from dotenv import load_dotenv
from workflow import workflow

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@cl.on_chat_start
async def start():
    """Initialize the chat session with workflow information."""
    await cl.Message(
        content="🤖 **Multi-Agent Workflow Assistant**\n\n"
        "I'm powered by three specialized AI agents working together:\n"
        "- 📋 **Planning Agent**: Creates structured plans\n"
        "- 🔍 **Research Agent**: Conducts detailed research\n"
        "- 💡 **Advisor Agent**: Provides final recommendations\n\n"
        "Send me any request and I'll process it through all three agents to give you a comprehensive response!"
    ).send()


@cl.on_message
async def main(message: cl.Message):
    """Process user messages through the multi-agent workflow."""
    user_input = message.content
    
    # Show initial processing message
    processing_msg = cl.Message(content="🔄 Processing your request through the multi-agent workflow...")
    await processing_msg.send()
    
    try:
        # Execute the workflow using the run method
        result = await workflow.run(user_input)
        
        # Show agent progress
        await cl.Message(content="📋 **Planning Agent** is analyzing your request...").send()
        
        # Update processing message to show completion
        processing_msg.content = "✅ Workflow completed! Here are the results:"
        await processing_msg.update()
        
        # Display the final result from the advisor agent
        if isinstance(result, str):
            final_content = result
        else:
            final_content = str(result)
        
        # Send the comprehensive response
        await cl.Message(
            content=f"## 🎯 Multi-Agent Analysis Complete\n\n{final_content}"
        ).send()
        
    except Exception as e:
        logger.error(f"Workflow execution error: {e}")
        await cl.Message(
            content=f"❌ **Error occurred during workflow execution:**\n\n"
            f"```\n{str(e)}\n```\n\n"
            f"Please check that:\n"
            f"- FoundryLocal is running at the configured endpoint\n"
            f"- Your .env file is properly configured\n"
            f"- All required packages are installed"
        ).send()


@cl.on_stop
async def stop():
    """Clean up when chat session ends."""
    logger.info("Chat session ended")


if __name__ == "__main__":
    # Run the Chainlit app
    cl.run()