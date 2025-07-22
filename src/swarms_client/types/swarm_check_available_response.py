# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SwarmCheckAvailableResponse"]


class SwarmCheckAvailableResponse(BaseModel):
    success: Optional[bool] = None

    swarm_types: Optional[object] = None
