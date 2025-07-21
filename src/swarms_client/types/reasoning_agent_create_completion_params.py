# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ReasoningAgentCreateCompletionParams"]


class ReasoningAgentCreateCompletionParams(TypedDict, total=False):
    agent_name: Optional[str]
    """The unique name assigned to the reasoning agent."""

    description: Optional[str]
    """A detailed explanation of the reasoning agent's purpose and capabilities."""

    max_loops: Optional[int]
    """The maximum number of times the reasoning agent is allowed to repeat its task."""

    memory_capacity: Optional[int]
    """The memory capacity for the reasoning agent."""

    model_name: Optional[str]
    """The name of the AI model that the reasoning agent will utilize."""

    num_knowledge_items: Optional[int]
    """The number of knowledge items to use for the reasoning agent."""

    num_samples: Optional[int]
    """The number of samples to generate for the reasoning agent."""

    output_type: Optional[
        Literal[
            "list",
            "dict",
            "dictionary",
            "string",
            "str",
            "final",
            "last",
            "json",
            "all",
            "yaml",
            "xml",
            "dict-all-except-first",
            "str-all-except-first",
            "basemodel",
            "dict-final",
            "list-final",
        ]
    ]
    """The type of output format for the reasoning agent."""

    swarm_type: Optional[
        Literal[
            "reasoning-duo",
            "self-consistency",
            "ire",
            "reasoning-agent",
            "consistency-agent",
            "ire-agent",
            "ReflexionAgent",
            "GKPAgent",
            "AgentJudge",
        ]
    ]
    """
    The type of reasoning swarm to use (e.g., reasoning duo, self-consistency, IRE).
    """

    system_prompt: Optional[str]
    """The initial instruction or context provided to the reasoning agent."""

    task: Optional[str]
    """The task to be completed by the reasoning agent."""
