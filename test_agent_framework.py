#!/usr/bin/env python3
"""Simple test to diagnose agent framework issues."""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

def test_imports():
    print("Testing imports...")
    
    try:
        import agent_framework
        print("✅ agent_framework imported successfully")
        print(f"   Version: {getattr(agent_framework, '__version__', 'unknown')}")
    except Exception as e:
        print(f"❌ agent_framework import failed: {e}")
        return False
    
    try:
        from agent_framework.openai import OpenAIChatClient
        print("✅ OpenAIChatClient imported successfully")
    except Exception as e:
        print(f"❌ OpenAIChatClient import failed: {e}")
        return False
        
    try:
        from agent_framework.devui import serve
        print("✅ DevUI serve imported successfully")
    except Exception as e:
        print(f"❌ DevUI serve import failed: {e}")
        return False
        
    return True

def test_client_creation():
    print("\nTesting client creation...")
    
    try:
        from agent_framework.openai import OpenAIChatClient
        
        base_url = os.environ.get("FOUNDRYLOCAL_ENDPOINT")
        model_id = os.environ.get("FOUNDRYLOCAL_MODEL_DEPLOYMENT_NAME")
        api_key = "nokey"
        
        print(f"   Base URL: {base_url}")
        print(f"   Model ID: {model_id}")
        
        if not base_url:
            print("❌ No FOUNDRYLOCAL_ENDPOINT configured")
            return False
            
        client = OpenAIChatClient(base_url=base_url, api_key=api_key, model_id=model_id)
        print("✅ OpenAI client created successfully")
        return True
        
    except Exception as e:
        print(f"❌ Client creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_agent_creation():
    print("\nTesting agent creation...")
    
    try:
        from agent_framework.openai import OpenAIChatClient
        
        base_url = os.environ.get("FOUNDRYLOCAL_ENDPOINT")
        model_id = os.environ.get("FOUNDRYLOCAL_MODEL_DEPLOYMENT_NAME")
        api_key = "nokey"
        
        client = OpenAIChatClient(base_url=base_url, api_key=api_key, model_id=model_id)
        
        agent = client.create_agent(
            instructions="You are a test agent.",
            name="Test-Agent",
        )
        print("✅ Agent created successfully")
        return True
        
    except Exception as e:
        print(f"❌ Agent creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 50)
    print("AGENT FRAMEWORK DIAGNOSTIC TEST")
    print("=" * 50)
    
    if not test_imports():
        print("\n❌ Import tests failed")
        return
        
    if not test_client_creation():
        print("\n❌ Client creation tests failed")
        return
        
    if not test_agent_creation():
        print("\n❌ Agent creation tests failed")
        return
        
    print("\n✅ All tests passed! Agent framework is working correctly.")

if __name__ == "__main__":
    main()