"""
Swarms API Client

A production-grade Python client for the Swarms API with both synchronous and asynchronous interfaces.
"""

from swarms_client.client import (
    # Main client
    Swarms,
    client,
    
    # Models
    SwarmsObject,
    AgentTool,
    AgentSpec,
    AgentCompletion,
    ScheduleSpec,
    SwarmSpec,
    Usage,
    AgentCompletionResponse,
    SwarmCompletionResponse,
    LogEntry,
    LogsResponse,
    SwarmTypesResponse,
    ModelsResponse,
    
    # Exceptions
    SwarmsError,
    AuthenticationError,
    RateLimitError,
    APIError,
    InvalidRequestError,
    InsufficientCreditsError,
    TimeoutError,
    NetworkError,
    
    # Resources
    BaseResource,
    AgentResource,
    SwarmResource,
    ModelsResource,
    LogsResource,
    
    # Types
    ModelNameType,
    AgentNameType,
    SwarmTypeType,
)


__all__ = [
    # Main client
    "Swarms",
    "client",
    
    # Models
    "SwarmsObject",
    "AgentTool",
    "AgentSpec",
    "AgentCompletion",
    "ScheduleSpec", 
    "SwarmSpec",
    "Usage",
    "AgentCompletionResponse",
    "SwarmCompletionResponse",
    "LogEntry",
    "LogsResponse",
    "SwarmTypesResponse",
    "ModelsResponse",
    
    # Exceptions
    "SwarmsError",
    "AuthenticationError",
    "RateLimitError",
    "APIError",
    "InvalidRequestError",
    "InsufficientCreditsError",
    "TimeoutError",
    "NetworkError",
    
    # Resources
    "BaseResource",
    "AgentResource",
    "SwarmResource",
    "ModelsResource",
    "LogsResource",
    
    # Types
    "ModelNameType",
    "AgentNameType",
    "SwarmTypeType",
]


