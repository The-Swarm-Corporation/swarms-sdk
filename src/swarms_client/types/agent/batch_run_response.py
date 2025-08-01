# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatchRunResponse"]


class BatchRunResponse(BaseModel):
    batch_id: Optional[str] = None
    """The unique identifier for the agent batch completion."""

    execution_time: Optional[float] = None
    """The execution time of the agent batch completion."""

    results: Optional[object] = None
    """The outputs generated by the agent."""

    timestamp: Optional[str] = None
    """The timestamp when the agent batch completion was created."""

    total_requests: Optional[int] = None
    """The total number of requests in the batch."""
