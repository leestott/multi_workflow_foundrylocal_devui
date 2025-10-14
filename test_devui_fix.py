#!/usr/bin/env python3
"""
Test script to verify the DevUI workflow works without serialization errors.
"""

import asyncio
from workflow import workflow

async def test_workflow():
    """Test the workflow with a simple message."""
    
    print("Testing workflow...")
    
    try:
        # Test the workflow with a simple message
        test_message = "Create a plan for building a simple web application"
        
        print(f"Sending message: {test_message}")
        
        # Run the workflow
        responses = []
        async for response in workflow.run_stream(test_message):
            responses.append(response)
            print(f"Response {len(responses)}: {type(response).__name__}")
            
            # Print a preview of the response
            if hasattr(response, 'messages') and response.messages:
                for msg in response.messages[-1:]:  # Just show the last message
                    content = getattr(msg, 'contents', getattr(msg, 'content', str(msg)))
                    preview = str(content)[:200] + "..." if len(str(content)) > 200 else str(content)
                    print(f"  Preview: {preview}")
            elif hasattr(response, 'contents'):
                preview = str(response.contents)[:200] + "..." if len(str(response.contents)) > 200 else str(response.contents)
                print(f"  Preview: {preview}")
        
        print(f"\n✅ Workflow completed successfully! Received {len(responses)} responses.")
        return True
        
    except Exception as e:
        print(f"❌ Workflow test failed: {e}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        return False

if __name__ == "__main__":
    result = asyncio.run(test_workflow())
    if result:
        print("\n🎉 DevUI should now work without serialization errors!")
        print("You can run: python main.py")
    else:
        print("\n❌ There are still issues with the workflow.")