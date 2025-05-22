from swarms_client.client import SwarmsClient


def sync_example():
    """Example of synchronous client usage"""
    with SwarmsClient() as client:
        # List available models
        models_response = client.models.list()
        print(f"Available models: {models_response.models}")

        # List available swarm types
        swarm_types = client.swarm.list_types()
        print(f"Available swarm types: {swarm_types.swarm_types}")

        # Create a single agent completion
        agent_response = client.agent.create(
            agent_config={
                "agent_name": "Researcher",
                "description": "Conducts in-depth research",
                "model_name": "gpt-4o-mini",
                "temperature": 0.7,
                "max_loops": 1,
            },
            task="Research the latest developments in quantum computing",
        )
        print(f"Agent response: {agent_response}")

        # Create a swarm completion
        swarm_response = client.swarm.create(
            name="Research Swarm",
            description="A swarm for conducting research",
            swarm_type="SequentialWorkflow",
            task="Research and analyze the future of AI",
            agents=[
                {
                    "agent_name": "Researcher",
                    "description": "Conducts in-depth research",
                    "model_name": "gpt-4o-mini",
                    "temperature": 0.7,
                    "max_loops": 1,
                    "role": "researcher",
                },
                {
                    "agent_name": "Analyst",
                    "description": "Analyzes research findings",
                    "model_name": "gpt-4o-mini",
                    "temperature": 0.7,
                    "max_loops": 1,
                    "role": "analyst",
                },
            ],
            max_loops=1,
            service_tier="standard",
        )
        print(f"Swarm response: {swarm_response.output}")


def main():
    print("Running synchronous examples...")
    sync_example()
    print("Running asynchronous examples...")


if __name__ == "__main__":
    main()
