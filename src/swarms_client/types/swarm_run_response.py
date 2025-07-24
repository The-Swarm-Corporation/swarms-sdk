# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["SwarmRunResponse"]


class SwarmRunResponse(BaseModel):
    description: Optional[str] = None
    """The description of the swarm."""

    execution_time: Optional[float] = None
    """The execution time of the swarm."""

    job_id: Optional[str] = None
    """The unique identifier for the swarm completion."""

    number_of_agents: Optional[int] = None
    """The number of agents in the swarm."""

    output: object
    """The output of the swarm."""

    service_tier: Optional[str] = None
    """The service tier of the swarm."""

    status: Optional[str] = None
    """The status of the swarm completion."""

    swarm_name: Optional[str] = None
    """The name of the swarm."""

    swarm_type: Optional[str] = None
    """The type of the swarm."""

    usage: Optional[Dict[str, object]] = None
    """The usage of the swarm."""

    cost: Optional[float] = None
    """The cost of the swarm execution."""

    most_used_model: Optional[str] = None
    """The most frequently used model during the swarm execution."""
