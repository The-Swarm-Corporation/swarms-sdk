from swarms_client.client import SwarmsClient


def main():
    # Initialize the Swarms client
    client = SwarmsClient()

    # Create a financial analysis swarm
    response = client.swarm.create(
        name="Financial Analysis Swarm",
        description="A sequential workflow for analyzing financial data and generating insights",
        swarm_type="SequentialWorkflow",
        task="Analyze the following financial data and provide investment recommendations: AAPL stock price: $175.04, Revenue: $394.3B, P/E Ratio: 28.5, Market Cap: $2.8T",
        agents=[
            {
                "agent_name": "Data Analyst",
                "description": "Analyzes financial metrics and market data",
                "model_name": "gpt-4o",
                "system_prompt": "You are a financial data analyst. Your role is to analyze financial metrics and market data to identify key trends and patterns. Focus on quantitative analysis and objective observations.",
                "temperature": 0.3,
            },
            {
                "agent_name": "Market Expert",
                "description": "Provides market context and industry insights",
                "model_name": "gpt-4o",
                "system_prompt": "You are a market expert with deep knowledge of the tech industry. Your role is to provide market context, industry trends, and competitive analysis. Consider macroeconomic factors and industry-specific dynamics.",
                "temperature": 0.4,
            },
            {
                "agent_name": "Investment Advisor",
                "description": "Generates investment recommendations",
                "model_name": "gpt-4o",
                "system_prompt": "You are an investment advisor. Your role is to synthesize the analysis and market insights to provide clear, actionable investment recommendations. Consider risk factors and investment time horizons.",
                "temperature": 0.5,
            },
        ],
        max_loops=1,
    )

    # Print the results
    print("\n=== Financial Analysis Results ===\n")
    print(f"Swarm Name: {response}")


if __name__ == "__main__":
    main()
