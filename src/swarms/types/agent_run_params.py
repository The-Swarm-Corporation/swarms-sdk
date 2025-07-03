# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .agent_spec_param import AgentSpecParam

__all__ = ["AgentRunParams"]


class AgentRunParams(TypedDict, total=False):
    x_api_key: Required[Annotated[str, PropertyInfo(alias="x-api-key")]]

    agent_config: Optional[AgentSpecParam]
    """The configuration of the agent to be completed."""

    history: Union[Dict[str, object], Iterable[Dict[str, str]], None]
    """The history of the agent's previous tasks and responses.

    Can be either a dictionary or a list of message objects.
    """

    img: Optional[str]
    """
    An optional image URL that may be associated with the agent's task or
    representation.
    """

    imgs: Optional[List[str]]
    """
    A list of image URLs that may be associated with the agent's task or
    representation.
    """

    task: Optional[str]
    """The task to be completed by the agent."""
