import asyncio
from swarms_client.client import SwarmsClient


async def main():
    async with SwarmsClient() as client:
        # Create an agent completion asynchronously
        response = await client.agent.acreate(
            agent_config={
                "agent_name": "Writer",
                "model_name": "gpt-4o-mini",
                "description": "A writer agent that writes short stories about an AI and human friendship",
                "system_prompt": "You are a writer agent that writes short stories about an AI and human friendship",
                "role": "writer",
                "max_loops": 1,
                "temperature": 0.7,
            },
            task="Write a short story about an AI and human friendship",
        )

        # print(f"Result: {response}")
        # print(json.dumps(response, indent=4))
        # print(type(response))
        print(response.model_dump_json(indent=4))


if __name__ == "__main__":
    asyncio.run(main())
