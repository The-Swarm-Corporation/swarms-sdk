"""
Cost calculation utility for Swarms API operations.

This module provides client-side cost calculation based on usage data,
model pricing, and service tiers. It calculates costs for individual
operations and aggregates costs for analytics.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from collections import Counter

from loguru import logger

# Type aliases for better readability
UsageData = Dict[str, Any]
ModelName = str
ServiceTier = str

@dataclass
class ModelPricing:
    """Pricing information for a specific model."""
    model_name: str
    input_cost_per_1k_tokens: float
    output_cost_per_1k_tokens: float
    description: str = ""

@dataclass
class ServiceTierMultiplier:
    """Service tier cost multipliers."""
    tier_name: str
    multiplier: float
    description: str = ""

class SwarmsCostCalculator:
    """
    Client-side cost calculator for Swarms API operations.
    
    This calculator uses usage data from API responses to calculate
    actual costs based on model pricing and service tiers.
    """
    
    def __init__(self):
        """Initialize the cost calculator with default pricing."""
        self._model_pricing = self._initialize_model_pricing()
        self._service_tiers = self._initialize_service_tiers()
        self._logger = logger.bind(name="SwarmsCostCalculator")
    
    def _initialize_model_pricing(self) -> Dict[ModelName, ModelPricing]:
        """Initialize default model pricing based on current market rates."""
        return {
            # OpenAI Models
            "gpt-4o": ModelPricing(
                model_name="gpt-4o",
                input_cost_per_1k_tokens=0.0025,
                output_cost_per_1k_tokens=0.01,
                description="GPT-4 Omni"
            ),
            "gpt-4o-mini": ModelPricing(
                model_name="gpt-4o-mini",
                input_cost_per_1k_tokens=0.00015,
                output_cost_per_1k_tokens=0.0006,
                description="GPT-4 Omni Mini"
            ),
            "gpt-4": ModelPricing(
                model_name="gpt-4",
                input_cost_per_1k_tokens=0.03,
                output_cost_per_1k_tokens=0.06,
                description="GPT-4"
            ),
            "gpt-4-turbo": ModelPricing(
                model_name="gpt-4-turbo",
                input_cost_per_1k_tokens=0.01,
                output_cost_per_1k_tokens=0.03,
                description="GPT-4 Turbo"
            ),
            "gpt-3.5-turbo": ModelPricing(
                model_name="gpt-3.5-turbo",
                input_cost_per_1k_tokens=0.0005,
                output_cost_per_1k_tokens=0.0015,
                description="GPT-3.5 Turbo"
            ),
            
            # Anthropic Models
            "claude-3-5-sonnet-20241022": ModelPricing(
                model_name="claude-3-5-sonnet-20241022",
                input_cost_per_1k_tokens=0.003,
                output_cost_per_1k_tokens=0.015,
                description="Claude 3.5 Sonnet"
            ),
            "claude-3-5-haiku-20241022": ModelPricing(
                model_name="claude-3-5-haiku-20241022",
                input_cost_per_1k_tokens=0.00025,
                output_cost_per_1k_tokens=0.00125,
                description="Claude 3.5 Haiku"
            ),
            "claude-3-opus-20240229": ModelPricing(
                model_name="claude-3-opus-20240229",
                input_cost_per_1k_tokens=0.015,
                output_cost_per_1k_tokens=0.075,
                description="Claude 3 Opus"
            ),
            "claude-3-sonnet-20240229": ModelPricing(
                model_name="claude-3-sonnet-20240229",
                input_cost_per_1k_tokens=0.003,
                output_cost_per_1k_tokens=0.015,
                description="Claude 3 Sonnet"
            ),
            "claude-3-haiku-20240307": ModelPricing(
                model_name="claude-3-haiku-20240307",
                input_cost_per_1k_tokens=0.00025,
                output_cost_per_1k_tokens=0.00125,
                description="Claude 3 Haiku"
            ),
            
            # Google Models
            "gemini-1.5-pro": ModelPricing(
                model_name="gemini-1.5-pro",
                input_cost_per_1k_tokens=0.0035,
                output_cost_per_1k_tokens=0.0105,
                description="Gemini 1.5 Pro"
            ),
            "gemini-1.5-flash": ModelPricing(
                model_name="gemini-1.5-flash",
                input_cost_per_1k_tokens=0.000075,
                output_cost_per_1k_tokens=0.0003,
                description="Gemini 1.5 Flash"
            ),
            
            # Default fallback
            "unknown": ModelPricing(
                model_name="unknown",
                input_cost_per_1k_tokens=0.001,
                output_cost_per_1k_tokens=0.002,
                description="Unknown model (using default pricing)"
            )
        }
    
    def _initialize_service_tiers(self) -> Dict[ServiceTier, ServiceTierMultiplier]:
        """Initialize service tier multipliers."""
        return {
            "standard": ServiceTierMultiplier(
                tier_name="standard",
                multiplier=1.0,
                description="Standard processing tier"
            ),
            "flex": ServiceTierMultiplier(
                tier_name="flex",
                multiplier=0.7,
                description="Lower cost but slower processing"
            ),
            "premium": ServiceTierMultiplier(
                tier_name="premium",
                multiplier=1.5,
                description="Higher cost but faster processing"
            )
        }
    
    def add_model_pricing(self, model_name: str, pricing: ModelPricing) -> None:
        """Add or update pricing for a specific model."""
        self._model_pricing[model_name] = pricing
        self._logger.info(f"Added pricing for model: {model_name}")
    
    def add_service_tier(self, tier_name: str, multiplier: ServiceTierMultiplier) -> None:
        """Add or update a service tier multiplier."""
        self._service_tiers[tier_name] = multiplier
        self._logger.info(f"Added service tier: {tier_name}")
    
    def get_model_pricing(self, model_name: str) -> ModelPricing:
        """Get pricing for a specific model, with fallback to default."""
        # Try exact match first
        if model_name in self._model_pricing:
            return self._model_pricing[model_name]
        
        # Try partial matches for model variants
        for key, pricing in self._model_pricing.items():
            if key in model_name or model_name in key:
                self._logger.warning(f"Using partial match for model '{model_name}' -> '{key}'")
                return pricing
        
        # Fallback to unknown model pricing
        self._logger.warning(f"Unknown model '{model_name}', using default pricing")
        return self._model_pricing["unknown"]
    
    def get_service_tier_multiplier(self, service_tier: Optional[str]) -> float:
        """Get the cost multiplier for a service tier."""
        if not service_tier:
            return self._service_tiers["standard"].multiplier
        
        return self._service_tiers.get(service_tier, self._service_tiers["standard"]).multiplier
    
    def calculate_operation_cost(
        self,
        usage_data: UsageData,
        model_name: Optional[str] = None,
        service_tier: Optional[str] = None,
        num_agents: Optional[int] = None
    ) -> float:
        """
        Calculate the cost for a single operation based on usage data.
        
        Args:
            usage_data: Dictionary containing usage information (tokens, requests, etc.)
            model_name: Name of the model used
            service_tier: Service tier used (standard, flex, premium)
            num_agents: Number of agents in the operation (for swarm operations)
            
        Returns:
            Calculated cost in USD
        """
        try:
            # Extract token usage
            prompt_tokens = usage_data.get("prompt_tokens", 0)
            completion_tokens = usage_data.get("completion_tokens", 0)
            total_tokens = usage_data.get("total_tokens", prompt_tokens + completion_tokens)
            
            # If we have total_tokens but not breakdown, estimate
            if total_tokens and not (prompt_tokens or completion_tokens):
                # Estimate 70% input, 30% output (typical ratio)
                prompt_tokens = int(total_tokens * 0.7)
                completion_tokens = total_tokens - prompt_tokens
            
            # Get model pricing
            pricing = self.get_model_pricing(model_name or "unknown")
            
            # Calculate base cost
            input_cost = (prompt_tokens / 1000) * pricing.input_cost_per_1k_tokens
            output_cost = (completion_tokens / 1000) * pricing.output_cost_per_1k_tokens
            base_cost = input_cost + output_cost
            
            # Apply service tier multiplier
            tier_multiplier = self.get_service_tier_multiplier(service_tier)
            adjusted_cost = base_cost * tier_multiplier
            
            # Apply agent multiplier if specified
            if num_agents and num_agents > 1:
                # Swarm operations may have additional overhead
                agent_multiplier = min(num_agents * 0.8, 5.0)  # Cap at 5x for very large swarms
                adjusted_cost *= agent_multiplier
            
            # Add base operation cost (API overhead)
            operation_overhead = 0.001  # $0.001 per operation
            final_cost = adjusted_cost + operation_overhead
            
            self._logger.debug(
                f"Cost calculation: model={model_name}, "
                f"tokens={total_tokens} (prompt={prompt_tokens}, completion={completion_tokens}), "
                f"tier={service_tier}, agents={num_agents}, "
                f"cost=${final_cost:.6f}"
            )
            
            return round(final_cost, 6)
            
        except Exception as e:
            self._logger.error(f"Error calculating cost: {e}")
            return 0.0
    
    def calculate_swarm_cost(
        self,
        usage_data: UsageData,
        agents: Optional[List[Dict[str, Any]]] = None,
        service_tier: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Calculate cost for a swarm operation.
        
        Args:
            usage_data: Usage data from the swarm response
            agents: List of agent configurations
            service_tier: Service tier used
            
        Returns:
            Dictionary with cost breakdown and most used model
        """
        try:
            # Calculate base cost
            base_cost = self.calculate_operation_cost(
                usage_data=usage_data,
                service_tier=service_tier,
                num_agents=len(agents) if agents else None
            )
            
            # Determine most used model
            most_used_model = self._determine_most_used_model(agents)
            
            # Calculate cost breakdown by agent if available
            agent_costs: List[Dict[str, str]] = []
            if agents:
                for agent in agents:
                    agent_model = agent.get("model_name", "unknown")
                    agent_pricing = self.get_model_pricing(agent_model)
                    agent_costs.append({
                        "agent_name": agent.get("agent_name", "Unknown"),
                        "model": agent_model,
                        "model_description": agent_pricing.description
                    })
            
            return {
                "total_cost": base_cost,
                "most_used_model": most_used_model,
                "cost_breakdown": {
                    "base_operation": base_cost,
                    "service_tier": service_tier or "standard",
                    "num_agents": len(agents) if agents else 1
                },
                "agent_details": agent_costs
            }
            
        except Exception as e:
            self._logger.error(f"Error calculating swarm cost: {e}")
            return {
                "total_cost": 0.0,
                "most_used_model": "unknown",
                "cost_breakdown": {},
                "agent_details": []
            }
    
    def calculate_batch_cost(
        self,
        results: List[Dict[str, Any]],
        usage_data: Optional[UsageData] = None
    ) -> Dict[str, Any]:
        """
        Calculate cost for a batch operation.
        
        Args:
            results: List of individual operation results
            usage_data: Overall batch usage data
            
        Returns:
            Dictionary with total cost and most used model
        """
        try:
            total_cost = 0.0
            model_usage: Counter[str] = Counter()
            
            # Calculate costs for individual operations
            for result in results:
                # Extract usage data from individual result
                result_usage = result.get("usage", {})
                result_model = result.get("model_name", "unknown")
                
                # Calculate individual cost
                individual_cost = self.calculate_operation_cost(
                    usage_data=result_usage,
                    model_name=result_model
                )
                total_cost += individual_cost
                
                # Track model usage
                model_usage[result_model] += 1
            
            # Determine most used model
            most_used_model = model_usage.most_common(1)[0][0] if model_usage else "unknown"
            
            return {
                "total_cost": total_cost,
                "most_used_model": most_used_model,
                "num_operations": len(results),
                "model_distribution": dict(model_usage)
            }
            
        except Exception as e:
            self._logger.error(f"Error calculating batch cost: {e}")
            return {
                "total_cost": 0.0,
                "most_used_model": "unknown",
                "num_operations": len(results),
                "model_distribution": {}
            }
    
    def calculate_logs_cost(
        self,
        logs: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Calculate total cost and most used model from logs.
        
        Args:
            logs: List of log entries
            
        Returns:
            Dictionary with total cost and most used model
        """
        try:
            total_cost = 0.0
            model_usage: Counter[str] = Counter()
            
            for log_entry in logs:
                # Extract usage data from log entry
                usage_data = log_entry.get("usage", {})
                model_name = log_entry.get("model_name", "unknown")
                
                # Calculate cost for this log entry
                entry_cost = self.calculate_operation_cost(
                    usage_data=usage_data,
                    model_name=model_name
                )
                total_cost += entry_cost
                
                # Track model usage
                model_usage[model_name] += 1
            
            # Determine most used model
            most_used_model = model_usage.most_common(1)[0][0] if model_usage else "unknown"
            
            return {
                "total_cost": total_cost,
                "most_used_model": most_used_model,
                "num_operations": len(logs),
                "model_distribution": dict(model_usage)
            }
            
        except Exception as e:
            self._logger.error(f"Error calculating logs cost: {e}")
            return {
                "total_cost": 0.0,
                "most_used_model": "unknown",
                "num_operations": len(logs),
                "model_distribution": {}
            }
    
    def _determine_most_used_model(self, agents: Optional[List[Dict[str, Any]]]) -> str:
        """Determine the most frequently used model from agent configurations."""
        if not agents:
            return "unknown"
        
        model_counts: Counter[str] = Counter()
        for agent in agents:
            model_name = agent.get("model_name", "unknown")
            model_counts[model_name] += 1
        
        return model_counts.most_common(1)[0][0] if model_counts else "unknown"
    
    def get_pricing_summary(self) -> Dict[str, Any]:
        """Get a summary of all available pricing information."""
        return {
            "models": {
                name: {
                    "input_cost_per_1k_tokens": pricing.input_cost_per_1k_tokens,
                    "output_cost_per_1k_tokens": pricing.output_cost_per_1k_tokens,
                    "description": pricing.description
                }
                for name, pricing in self._model_pricing.items()
            },
            "service_tiers": {
                name: {
                    "multiplier": tier.multiplier,
                    "description": tier.description
                }
                for name, tier in self._service_tiers.items()
            }
        }


# Global instance for easy access
_cost_calculator = SwarmsCostCalculator()


def get_cost_calculator() -> SwarmsCostCalculator:
    """Get the global cost calculator instance."""
    return _cost_calculator


def calculate_swarm_response_cost(
    response_data: Dict[str, Any],
    agents: Optional[List[Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """
    Calculate cost for a swarm response.
    
    This is a convenience function that extracts relevant data from a swarm response
    and calculates the cost using the global cost calculator.
    
    Args:
        response_data: Response data from a swarm operation
        agents: List of agent configurations used in the swarm
        
    Returns:
        Dictionary with cost information
    """
    calculator = get_cost_calculator()
    
    # Extract relevant data from response
    usage_data = response_data.get("usage", {})
    service_tier = response_data.get("service_tier")
    
    return calculator.calculate_swarm_cost(
        usage_data=usage_data,
        agents=agents,
        service_tier=service_tier
    )


def calculate_agent_response_cost(response_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate cost for an agent response.
    
    Args:
        response_data: Response data from an agent operation
        
    Returns:
        Dictionary with cost information
    """
    calculator = get_cost_calculator()
    
    # Extract relevant data from response
    usage_data = response_data.get("usage", {})
    model_name = response_data.get("model_name", "unknown")
    
    cost = calculator.calculate_operation_cost(
        usage_data=usage_data,
        model_name=model_name
    )
    
    return {
        "total_cost": cost,
        "most_used_model": model_name
    }


def calculate_batch_response_cost(response_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate cost for a batch response.
    
    Args:
        response_data: Response data from a batch operation
        
    Returns:
        Dictionary with cost information
    """
    calculator = get_cost_calculator()
    
    # Extract results from response
    results = response_data.get("results", [])
    usage_data = response_data.get("usage", {})
    
    return calculator.calculate_batch_cost(
        results=results,
        usage_data=usage_data
    )


def calculate_logs_response_cost(response_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate cost for a logs response.
    
    Args:
        response_data: Response data from a logs operation
        
    Returns:
        Dictionary with cost information
    """
    calculator = get_cost_calculator()
    
    # Extract logs from response
    logs = response_data.get("logs", [])
    
    return calculator.calculate_logs_cost(logs) 