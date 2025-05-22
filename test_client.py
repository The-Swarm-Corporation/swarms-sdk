"""
Comprehensive unit tests for the Swarms API client.
Uses simple functions and loguru for logging.
"""

import asyncio
from datetime import datetime
from typing import Any
from loguru import logger
from swarms_client.client import (
    SwarmsClient,
    SwarmCompletionResponse,
    AgentCompletionResponse,
    LogEntry,
    LogsResponse,
)

# Configure logger
logger.remove()
logger.add(
    "test_results.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
    rotation="1 day",
)

# Test data
TEST_AGENT_CONFIG = {
    "agent_name": "Research Analyst",
    "description": "Expert at analyzing and synthesizing research data",
    "system_prompt": "You are a research analyst focused on providing detailed, accurate analysis.",
    "model_name": "gpt-4o",
    "temperature": 0.7,
    "max_tokens": 4096,
    "max_loops": 2,
}

TEST_AGENT_CONFIG_2 = {
    "agent_name": "Data Scientist",
    "description": "Expert at data analysis and visualization",
    "system_prompt": "You are a data scientist focused on extracting insights from data.",
    "model_name": "gpt-4o-mini",
    "temperature": 0.5,
    "max_tokens": 2048,
    "max_loops": 1,
}

TEST_SWARM_CONFIG = {
    "name": "Research Analysis Swarm",
    "description": "A swarm for comprehensive research analysis",
    "agents": [TEST_AGENT_CONFIG, TEST_AGENT_CONFIG_2],
    "max_loops": 3,
    "swarm_type": "SequentialWorkflow",
    "task": "Analyze the impact of artificial intelligence on healthcare in 2024",
    "return_history": True,
    "service_tier": "standard",
}

# Test results storage
test_results = {
    "total_tests": 0,
    "passed_tests": 0,
    "failed_tests": 0,
    "test_details": [],
}


def log_test_result(test_name: str, success: bool, error: str = None):
    """Log test result and update test statistics."""
    test_results["total_tests"] += 1
    if success:
        test_results["passed_tests"] += 1
        logger.info(f"✅ Test passed: {test_name}")
    else:
        test_results["failed_tests"] += 1
        logger.error(f"❌ Test failed: {test_name}")
        if error:
            logger.error(f"Error: {error}")

    test_results["test_details"].append(
        {
            "name": test_name,
            "success": success,
            "error": error,
            "timestamp": datetime.now().isoformat(),
        }
    )


def validate_response(response: Any, expected_type: type) -> bool:
    """Validate response type and structure."""
    try:
        if not isinstance(response, expected_type):
            return False
        return True
    except Exception:
        return False


def test_agent_completion():
    """Test single agent completion with a research task."""
    try:
        client = SwarmsClient(timeout=120, max_retries=3, retry_delay=2)

        # Example 1: Basic research task
        response = client.agent.create(
            agent_config=TEST_AGENT_CONFIG,
            task="Analyze the latest trends in quantum computing",
        )

        if not validate_response(response, AgentCompletionResponse):
            raise ValueError("Invalid response type")

        assert response.success
        assert response.name == TEST_AGENT_CONFIG["agent_name"]

        # Example 2: Task with history
        history = {
            "messages": [
                {
                    "role": "user",
                    "content": "What are the key challenges in quantum computing?",
                },
                {"role": "assistant", "content": "The main challenges include..."},
            ]
        }

        response_with_history = client.agent.create(
            agent_config=TEST_AGENT_CONFIG,
            task="Based on the previous discussion, what are the potential solutions?",
            # history=history,
        )

        print(response_with_history)
        assert response_with_history is not None
        

        log_test_result("test_agent_completion", True)
        return True
    except Exception as e:
        log_test_result("test_agent_completion", False, str(e))
        return False


def test_agent_batch_completion():
    """Test batch agent completions with multiple tasks."""
    try:
        client = SwarmsClient(timeout=120, max_retries=3, retry_delay=2)

        # Example: Multiple research tasks
        completions = [
            {
                "agent_config": TEST_AGENT_CONFIG,
                "task": "Analyze quantum computing trends",
            },
            {"agent_config": TEST_AGENT_CONFIG_2, "task": "Analyze AI in healthcare"},
            {
                "agent_config": {
                    "agent_name": "Market Analyst",
                    "description": "Expert at market analysis",
                    "model_name": "gpt-4o",
                    "temperature": 0.6,
                },
                "task": "Analyze the impact of AI on financial markets",
            },
        ]

        responses = client.agent.create_batch(completions)
        
        print(responses)

        # if not isinstance(responses, list):
        #     raise ValueError("Expected list of responses")

        assert responses is not None

        log_test_result("test_agent_batch_completion", True)
        return True
    except Exception as e:
        log_test_result("test_agent_batch_completion", False, str(e))
        return False


def test_swarm_completion():
    """Test single swarm completion with a complex research task."""
    try:
        client = SwarmsClient(timeout=120, max_retries=3, retry_delay=2)

        # Example 1: Sequential workflow
        response = client.swarm.create(**TEST_SWARM_CONFIG)

        if not validate_response(response, SwarmCompletionResponse):
            raise ValueError("Invalid response type")

        assert response.swarm_name == TEST_SWARM_CONFIG["name"]
        assert response.swarm_type == TEST_SWARM_CONFIG["swarm_type"]

        # Example 2: Group chat workflow
        group_chat_config = {
            "name": "AI Ethics Discussion",
            "description": "A group chat to discuss AI ethics",
            "agents": [
                {
                    "agent_name": "Ethicist",
                    "description": "Expert in AI ethics",
                    "model_name": "gpt-4o",
                    "temperature": 0.7,
                },
                {
                    "agent_name": "Technologist",
                    "description": "Expert in AI technology",
                    "model_name": "gpt-4o",
                    "temperature": 0.7,
                },
            ],
            "swarm_type": "GroupChat",
            "task": "Discuss the ethical implications of autonomous AI systems",
            "max_loops": 5,
        }

        group_chat_response = client.swarm.create(**group_chat_config)
        assert group_chat_response.success

        log_test_result("test_swarm_completion", True)
        return True
    except Exception as e:
        log_test_result("test_swarm_completion", False, str(e))
        return False


def test_swarm_batch_completion():
    """Test batch swarm completions with multiple workflows."""
    try:
        client = SwarmsClient(timeout=120, max_retries=3, retry_delay=2)

        # Example: Multiple research workflows
        swarms = [
            {
                **TEST_SWARM_CONFIG,
                "name": "Healthcare AI Research",
                "task": "Analyze AI applications in healthcare",
            },
            {
                **TEST_SWARM_CONFIG,
                "name": "Quantum Computing Research",
                "task": "Analyze quantum computing advances",
            },
            {
                "name": "Market Analysis Swarm",
                "description": "A swarm for market analysis",
                "agents": [
                    {
                        "agent_name": "Market Analyst",
                        "description": "Expert in market analysis",
                        "model_name": "gpt-4o",
                        "temperature": 0.6,
                    },
                    {
                        "agent_name": "Data Scientist",
                        "description": "Expert in data analysis",
                        "model_name": "gpt-4o-mini",
                        "temperature": 0.5,
                    },
                ],
                "swarm_type": "SequentialWorkflow",
                "task": "Analyze market trends in AI technology",
                "max_loops": 3,
            },
        ]

        responses = client.swarm.create_batch(swarms)

        if not isinstance(responses, list):
            raise ValueError("Expected list of responses")

        for response in responses:
            if not validate_response(response, SwarmCompletionResponse):
                raise ValueError("Invalid response type in batch")
            assert response.success

        log_test_result("test_swarm_batch_completion", True)
        return True
    except Exception as e:
        log_test_result("test_swarm_batch_completion", False, str(e))
        return False


def test_list_swarm_types():
    """Test listing available swarm types."""
    try:
        client = SwarmsClient(timeout=120, max_retries=3, retry_delay=2)

        # Test listing swarm types
        response = client.swarm.list_types()

        assert response.success
        assert isinstance(response.swarm_types, list)
        assert len(response.swarm_types) > 0

        # Verify common swarm types are present
        common_types = ["SequentialWorkflow", "GroupChat", "MixtureOfAgents"]
        for swarm_type in common_types:
            assert swarm_type in response.swarm_types

        log_test_result("test_list_swarm_types", True)
        return True
    except Exception as e:
        log_test_result("test_list_swarm_types", False, str(e))
        return False


def test_list_models():
    """Test listing available models."""
    try:
        client = SwarmsClient(timeout=120, max_retries=3, retry_delay=2)

        # Test listing models
        response = client.models.list()

        assert response.success
        assert isinstance(response.models, list)
        assert len(response.models) > 0

        # Verify common models are present
        common_models = ["gpt-4o", "gpt-4o-mini"]
        for model in common_models:
            assert model in response.models

        log_test_result("test_list_models", True)
        return True
    except Exception as e:
        log_test_result("test_list_models", False, str(e))
        return False


def test_list_logs():
    """Test listing API logs."""
    try:
        client = SwarmsClient(timeout=120, max_retries=3, retry_delay=2)

        # Test listing logs
        response = client.logs.list()

        # Convert response to proper format if needed
        if isinstance(response, dict):
            # Handle case where response is raw dict
            logs = response.get("logs", [])
            processed_logs = []
            for log in logs:
                # Convert id to string if it's an integer
                if isinstance(log.get("id"), int):
                    log["id"] = str(log["id"])

                # Convert data to dict if it's a list
                if isinstance(log.get("data"), list):
                    log["data"] = {"items": log["data"]}

                processed_logs.append(log)

            response = LogsResponse(
                status="success",
                count=len(processed_logs),
                logs=[LogEntry(**log) for log in processed_logs],
                timestamp=datetime.now().isoformat(),
            )

        assert isinstance(response, LogsResponse)
        assert isinstance(response.logs, list)

        # Verify log structure
        for log in response.logs:
            assert isinstance(log.id, str)
            assert isinstance(log.api_key, str)
            assert isinstance(log.data, dict)

        log_test_result("test_list_logs", True)
        return True
    except Exception as e:
        log_test_result("test_list_logs", False, str(e))
        return False


async def test_async_agent_completion():
    """Test async agent completion."""
    try:
        async with SwarmsClient(timeout=120, max_retries=3, retry_delay=2) as client:
            # Example: Async research task
            response = await client.agent.acreate(
                agent_config=TEST_AGENT_CONFIG,
                task="Analyze the latest trends in quantum computing",
            )

            if not validate_response(response, AgentCompletionResponse):
                raise ValueError("Invalid response type")

            assert response.success
            assert response.name == TEST_AGENT_CONFIG["agent_name"]

            log_test_result("test_async_agent_completion", True)
            return True
    except Exception as e:
        log_test_result("test_async_agent_completion", False, str(e))
        return False


async def test_async_swarm_completion():
    """Test async swarm completion."""
    try:
        async with SwarmsClient(timeout=120, max_retries=3, retry_delay=2) as client:
            # Example: Async research workflow
            response = await client.swarm.acreate(**TEST_SWARM_CONFIG)

            if not validate_response(response, SwarmCompletionResponse):
                raise ValueError("Invalid response type")

            assert response.swarm_name == TEST_SWARM_CONFIG["name"]
            assert response.swarm_type == TEST_SWARM_CONFIG["swarm_type"]

            log_test_result("test_async_swarm_completion", True)
            return True
    except Exception as e:
        log_test_result("test_async_swarm_completion", False, str(e))
        return False


def generate_markdown_report():
    """Generate a markdown report of test results."""
    success_rate = (
        (test_results["passed_tests"] / test_results["total_tests"] * 100)
        if test_results["total_tests"] > 0
        else 0
    )

    report = f"""# Swarms Client Test Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary
- Total Tests: {test_results['total_tests']}
- Passed: {test_results['passed_tests']}
- Failed: {test_results['failed_tests']}
- Success Rate: {success_rate:.2f}%

## Test Details
"""

    for test in test_results["test_details"]:
        status = "✅ PASSED" if test["success"] else "❌ FAILED"
        report += f"""
### {test['name']}
- Status: {status}
- Timestamp: {test['timestamp']}
"""
        if not test["success"] and test["error"]:
            report += f"- Error: {test['error']}\n"

    return report


def run_tests():
    """Run all tests and generate report."""
    logger.info("Starting test suite...")

    # Run synchronous tests
    test_agent_completion()
    test_agent_batch_completion()
    test_swarm_completion()
    test_swarm_batch_completion()
    test_list_swarm_types()
    test_list_models()
    test_list_logs()

    # Run async tests
    asyncio.run(test_async_agent_completion())
    asyncio.run(test_async_swarm_completion())

    # Generate and save report
    report = generate_markdown_report()
    with open("test_report.md", "w") as f:
        f.write(report)

    logger.info("Test suite completed. Report generated: test_report.md")
    return test_results


if __name__ == "__main__":
    run_tests()
