# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AgentSpecParam"]


class AgentSpecParam(TypedDict, total=False):
    agent_name: Required[Optional[str]]
    """
    The unique name assigned to the agent, which identifies its role and
    functionality within the swarm.
    """

    auto_generate_prompt: Optional[bool]
    """
    A flag indicating whether the agent should automatically create prompts based on
    the task requirements.
    """

    description: Optional[str]
    """
    A detailed explanation of the agent's purpose, capabilities, and any specific
    tasks it is designed to perform.
    """

    max_loops: Optional[int]
    """
    The maximum number of times the agent is allowed to repeat its task, enabling
    iterative processing if necessary.
    """

    max_tokens: Optional[int]
    """
    The maximum number of tokens that the agent is allowed to generate in its
    responses, limiting output length.
    """

    mcp_url: Optional[str]
    """The URL of the MCP server that the agent can use to complete its task."""

    model_name: Optional[str]
    """
    The name of the AI model that the agent will utilize for processing tasks and
    generating outputs. For example: gpt-4o, gpt-4o-mini, openai/o3-mini
    """

    role: Optional[str]
    """
    The designated role of the agent within the swarm, which influences its behavior
    and interaction with other agents.
    """

    streaming_on: Optional[bool]
    """A flag indicating whether the agent should stream its output."""

    system_prompt: Optional[str]
    """
    The initial instruction or context provided to the agent, guiding its behavior
    and responses during execution.
    """

    temperature: Optional[float]
    """
    A parameter that controls the randomness of the agent's output; lower values
    result in more deterministic responses.
    """

    tools_list_dictionary: Optional[Iterable[Dict[str, object]]]
    """A dictionary of tools that the agent can use to complete its task."""
