from swarms_client import SwarmsClient
from swarms_client.client import AgentSpec

client = SwarmsClient()

response = client.agent.create(
    agent_config=AgentSpec(
        agent_name="financial_analyst",
        model_name="gpt-4o-mini",
        temperature=0.5,  # Lower temperature for more precise financial analysis
        description="A specialized financial analyst who can analyze market trends, financial data, and provide investment insights",
        system_prompt="""You are an expert financial analyst with deep knowledge of:
- Financial markets and trading
- Company financial analysis and valuation
- Economic indicators and their impact
- Investment strategies and portfolio management
- Risk assessment and management

Provide detailed, data-driven analysis and insights while maintaining professional financial accuracy.""",
    ).model_dump(),
    task="Please analyze the recent performance of major market indices and provide key insights.",
)

print(response.model_dump_json(indent=4))
