# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SwarmGetLogsResponse"]


class SwarmGetLogsResponse(BaseModel):
    count: Optional[int] = None

    logs: Optional[object] = None

    status: Optional[str] = None

    timestamp: Optional[str] = None

    cost: Optional[float] = None
    """The total cost of the swarm operations in the logs."""

    most_used_model: Optional[str] = None
    """The most frequently used model across all swarm operations in the logs."""
