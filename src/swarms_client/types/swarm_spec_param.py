# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, TypedDict

from .agent_spec_param import AgentSpecParam

__all__ = ["SwarmSpecParam"]


class SwarmSpecParam(TypedDict, total=False):
    agents: Optional[Iterable[AgentSpecParam]]
    """
    A list of agents or specifications that define the agents participating in the
    swarm.
    """

    description: Optional[str]
    """
    A comprehensive description of the swarm's objectives, capabilities, and
    intended outcomes.
    """

    img: Optional[str]
    """
    An optional image URL that may be associated with the swarm's task or
    representation.
    """

    max_loops: Optional[int]
    """
    The maximum number of execution loops allowed for the swarm, enabling repeated
    processing if needed.
    """

    messages: Union[Iterable[Dict[str, object]], Dict[str, object], None]
    """A list of messages that the swarm should complete."""

    name: Optional[str]
    """
    The name of the swarm, which serves as an identifier for the group of agents and
    their collective task.
    """

    rearrange_flow: Optional[str]
    """Instructions on how to rearrange the flow of tasks among agents, if applicable."""

    return_history: Optional[bool]
    """
    A flag indicating whether the swarm should return its execution history along
    with the final output.
    """

    rules: Optional[str]
    """
    Guidelines or constraints that govern the behavior and interactions of the
    agents within the swarm.
    """

    service_tier: Optional[str]
    """The service tier to use for processing.

    Options: 'standard' (default) or 'flex' for lower cost but slower processing.
    """

    stream: Optional[bool]
    """A flag indicating whether the swarm should stream its output."""

    swarm_type: Optional[
        Literal[
            "AgentRearrange",
            "MixtureOfAgents",
            "SpreadSheetSwarm",
            "SequentialWorkflow",
            "ConcurrentWorkflow",
            "GroupChat",
            "MultiAgentRouter",
            "AutoSwarmBuilder",
            "HiearchicalSwarm",
            "auto",
            "MajorityVoting",
            "MALT",
            "DeepResearchSwarm",
            "CouncilAsAJudge",
            "InteractiveGroupChat",
        ]
    ]
    """
    The classification of the swarm, indicating its operational style and
    methodology.
    """

    task: Optional[str]
    """The specific task or objective that the swarm is designed to accomplish."""

    tasks: Optional[List[str]]
    """A list of tasks that the swarm should complete."""
