"""
Chainlit frontend for the FoundryLocal multi-agent workflow.

This provides a clean chat interface for the Plan → Research → Advisor workflow.
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
    """Initialize the chat session."""
    welcome_msg = """
🤖 **Multi-Agent Workflow Assistant**

I'm powered by three specialized AI agents working in sequence:
- 📋 **Planning Agent**: Creates structured plans from your requests
- 🔍 **Research Agent**: Conducts detailed research and analysis  
- 💡 **Advisor Agent**: Synthesizes everything into actionable recommendations

Send me any request and I'll process it through all three agents!

**Example requests:**
- "Create a plan for building a web application"
- "Help me design a marketing strategy for a new product"
- "Plan a machine learning project for customer segmentation"
- "Develop a cybersecurity implementation roadmap"
"""
    await cl.Message(content=welcome_msg).send()


@cl.on_message
async def main(message: cl.Message):
    """Process user messages through the three-agent workflow."""
    user_input = message.content
    
    try:
        # Show initial processing message
        processing_msg = cl.Message(content="🔄 **Processing your request through the multi-agent workflow...**")
        await processing_msg.send()
        
        # Show agent progress
        await cl.Message(content="📋 **Planning Agent** is analyzing your request and creating a structured plan...").send()
        
        # Execute the workflow using the run method
        result = await workflow.run(user_input)
        
        # Update processing message
        processing_msg.content = "✅ **All three agents have completed their analysis!**"
        await processing_msg.update()
        
        # Extract the final result
        if isinstance(result, str):
            final_content = result
        else:
            final_content = str(result)
        
        # Send the comprehensive response from the advisor agent
        await cl.Message(
            content=f"## 🎯 **Complete Multi-Agent Analysis**\n\n{final_content}"
        ).send()
        
        # Send usage tip
        await cl.Message(
            content="💡 **Tip:** The response above is the final synthesis from all three agents. "
            "You can ask follow-up questions or request a new analysis on a different topic!"
        ).send()
        
    except Exception as e:
        logger.error(f"Workflow execution error: {e}")
        await cl.Message(
            content=f"❌ **Error occurred during workflow execution:**\n\n"
            f"```\n{str(e)}\n```\n\n"
            f"**Troubleshooting:**\n"
            f"• Ensure FoundryLocal is running at the configured endpoint\n"
            f"• Check that your .env file is properly configured\n"
            f"• Verify all required packages are installed\n"
            f"• Make sure the model specified in .env is available in FoundryLocal"
        ).send()


if __name__ == "__main__":
    cl.run()