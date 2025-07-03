# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..swarm_spec_param import SwarmSpecParam

__all__ = ["BatchRunParams"]


class BatchRunParams(TypedDict, total=False):
    body: Required[Iterable[SwarmSpecParam]]
