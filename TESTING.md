# Testing Documentation

This document describes the testing suite for the multi-agent workflow system. The tests verify that the workflow functions correctly both with and without the DevUI interface.

## Overview

The testing suite consists of multiple test scripts designed to validate different aspects of the multi-agent workflow:

1. **Core functionality testing** - Verifies agents and workflow work independently of DevUI
2. **Integration testing** - Ensures proper communication between agents
3. **Environment validation** - Confirms Foundry Local setup and configuration

## Test Files

### 1. `test_simple.py` - Basic Diagnostics

**Purpose**: Basic system diagnostics and agent initialization testing.

**What it tests**:
- Agent initialization and availability
- Workflow component structure
- Basic agent method calls
- Environment setup validation

**How to run**:
```bash
python test_simple.py
```

**Expected output**:
- ✅ Agent initialization successful
- ✅ Workflow components available
- ✅ Simple agent call works
- Basic response from planning agent

**Use when**:
- First-time setup validation
- Troubleshooting initialization issues
- Quick health check of the system

---

### 2. `test_complete_workflow.py` - Full Workflow Testing

**Purpose**: Complete end-to-end workflow testing without DevUI.

**What it tests**:
- Individual agent functionality
- Complete multi-agent workflow execution
- Agent collaboration and communication
- Response streaming and completion
- Workflow orchestration

**How to run**:
```bash
python test_complete_workflow.py
```

**Expected output**:
- ✅ Individual agents test passed
- ✅ Complete workflow execution
- Detailed response logging (400+ responses)
- Workflow completion with supersteps
- Final success confirmation

**Use when**:
- Verifying core workflow functionality
- Testing before DevUI deployment
- Debugging workflow issues
- Performance validation

---

### 3. `test_workflow.py` - Advanced Workflow Testing

**Purpose**: Advanced workflow testing with detailed message handling.

**What it tests**:
- ChatMessage object handling
- Advanced workflow scenarios
- Error handling and recovery
- Detailed response analysis

**How to run**:
```bash
python test_workflow.py
```

**Note**: This test had some initial issues with ChatMessage format but demonstrates advanced testing patterns.

## Test Results Interpretation

### Successful Test Indicators

#### `test_simple.py` Success:
```
✅ Both agents initialized successfully
✅ Workflow has run_stream method
✅ All basic tests passed!
```

#### `test_complete_workflow.py` Success:
```
🎉 ALL TESTS PASSED!
The workflow works correctly without DevUI.
You can now run 'python main.py' to start with DevUI.
```

### Common Error Patterns

#### Agent Initialization Failures:
```
Plan agent: None
Research agent: None
```
**Solution**: Check `.env` file configuration and Foundry Local availability.

#### Model Not Found (400 Error):
```
Error code: 400 - BadRequestError
```
**Solution**: Verify model name in `.env` matches available models in Foundry Local.

#### Connection Issues:
```
Connection refused or timeout
```
**Solution**: Ensure Foundry Local is running on `http://127.0.0.1:58123`.

## Prerequisites for Testing

### 1. Environment Setup

Ensure your `.env` file contains:
```env
FOUNDRYLOCAL_ENDPOINT="http://127.0.0.1:58123/v1/"
FOUNDRYLOCAL_MODEL_DEPLOYMENT_NAME="Phi-3.5-mini-instruct-cuda-gpu:1"
OPENAI_CHAT_MODEL_ID="Phi-3.5-mini-instruct-cuda-gpu:1"
```

### 2. Foundry Local Running

Verify Foundry Local is accessible:
```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Alternative using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

### 3. Python Dependencies

Ensure required packages are installed:
```bash
pip install agent-framework
pip install python-dotenv
pip install openai
```

## Test Execution Workflow

### Recommended Testing Order:

1. **Start with basic diagnostics**:
   ```bash
   python test_simple.py
   ```

2. **Run complete workflow test**:
   ```bash
   python test_complete_workflow.py
   ```

3. **If tests pass, run full application**:
   ```bash
   python main.py
   ```

### Debugging Failed Tests:

1. **Check Foundry Local status** first
2. **Verify environment variables** in `.env`
3. **Confirm model availability** using models endpoint
4. **Review agent initialization** logs
5. **Test individual components** before full workflow

## Performance Expectations

### Normal Test Duration:
- `test_simple.py`: ~30 seconds
- `test_complete_workflow.py`: ~5-7 minutes

### Response Volume:
- Simple test: 1-5 responses
- Complete workflow: 400+ streaming responses
- Individual agents: 50-100 responses each

### Resource Usage:
- CPU: Moderate during model inference
- Memory: Depends on model size
- Network: Local traffic only (127.0.0.1)

## Troubleshooting Guide

### Issue: Tests hang or timeout

**Causes**:
- Foundry Local not responding
- Model taking too long to respond
- Network connectivity issues

**Solutions**:
- Restart Foundry Local
- Check model resource availability
- Verify endpoint accessibility

### Issue: Agent initialization fails

**Causes**:
- Incorrect environment variables
- Model name mismatch
- Missing API key (even though "nokey" is used)

**Solutions**:
- Verify `.env` file format and content
- Check available models list
- Ensure no extra spaces or quotes in env vars

### Issue: Workflow starts but doesn't complete

**Causes**:
- Agent communication issues
- Model context limits exceeded
- Framework configuration problems

**Solutions**:
- Check agent instructions for clarity
- Monitor response sizes
- Review workflow builder configuration

## Integration with Main Application

### Testing Before DevUI Launch:

Always run the complete workflow test before launching the DevUI:

```bash
# Test first
python test_complete_workflow.py

# If successful, launch DevUI
python main.py
```

### Continuous Validation:

Use tests for:
- **Environment validation** before deployment
- **Regression testing** after configuration changes
- **Performance baseline** establishment
- **Debugging isolation** when issues occur

## Test Data and Scenarios

### Default Test Scenarios:

1. **E-commerce website planning**: Tests complex project planning capabilities
2. **Security best practices research**: Tests knowledge synthesis and expansion
3. **Multi-step collaboration**: Tests agent handoff and coordination

### Custom Test Scenarios:

To test with custom prompts, modify the test files:

```python
# In test_complete_workflow.py, change this line:
test_prompt = "Your custom test scenario here"
```

## Maintenance and Updates

### Regular Test Maintenance:

1. **Update model names** when Foundry Local models change
2. **Adjust response expectations** as framework evolves
3. **Add new test scenarios** for additional features
4. **Update environment validation** for new requirements

### Version Compatibility:

- Tests are designed for **Agent Framework v1.x**
- Compatible with **Foundry Local standard deployment**
- Requires **Python 3.8+**

## Conclusion

This testing suite provides comprehensive validation of the multi-agent workflow system. By running these tests, you can confidently deploy and troubleshoot the application while ensuring all components work correctly in isolation and together.

The tests serve as both validation tools and documentation of expected system behavior, making them valuable for development, deployment, and maintenance activities.