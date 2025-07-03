from swarms_client.client import SwarmsClient
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key with error handling
api_key = os.getenv("SWARMS_API_KEY")

# Initialize the client with explicit API key
client = SwarmsClient(api_key=api_key)


def run_agent_batch_example():
    """Example of running batch agent completions"""
    try:
        # Define multiple agent completion requests
        agent_completions = [
            {
                "agent_config": {
                    "agent_name": "Market Researcher",
                    "description": "Analyzes market trends and opportunities",
                    "model_name": "gpt-4o-mini",
                    "temperature": 0.7,
                },
                "task": "Analyze the current market trends in AI and ML",
            },
            {
                "agent_config": {
                    "agent_name": "Technical Writer",
                    "description": "Creates technical documentation and reports",
                    "model_name": "gpt-4o",
                    "temperature": 0.4,
                },
                "task": "Write a technical overview of transformer architecture",
            },
        ]

        # Execute batch agent completions
        responses = client.agent.create_batch(completions=agent_completions)

        # print(responses)
        print(responses.model_dump_json(indent=4))
        print(type(responses))

    except Exception as e:
        print(f"Error during batch processing: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    print("Running Agent Batch Example...")
    run_agent_batch_example()
