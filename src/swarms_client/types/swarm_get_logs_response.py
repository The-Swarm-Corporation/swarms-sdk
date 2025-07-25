# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SwarmGetLogsResponse"]


class SwarmGetLogsResponse(BaseModel):
    count: Optional[int] = None

    logs: Optional[object] = None

    status: Optional[str] = None

    timestamp: Optional[str] = None
