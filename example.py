import asyncio
from swarms_client.client import Swarms

async def main():
    async with Swarms() as client:
        # List available models asynchronously
        models = await client.models.alist()
        print(f"Available models: {models.models}")
        
        # Create an agent completion asynchronously
        response = await client.agent.acreate(
            agent_config={
                "agent_name": "Writer",
                "model_name": "gpt-4o-mini",
                "description": "A writer agent that writes short stories about an AI and human friendship",
                "system_prompt": "You are a writer agent that writes short stories about an AI and human friendship",
                "role": "writer",
                "max_loops": 1,
                "temperature": 0.7
            },
            task="Write a short story about an AI and human friendship"
        )
        
        print(f"Result: {response}")

asyncio.run(main())