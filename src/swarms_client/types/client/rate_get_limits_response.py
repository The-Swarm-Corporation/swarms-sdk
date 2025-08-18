# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RateGetLimitsResponse", "Limits", "RateLimits", "RateLimitsDay", "RateLimitsHour", "RateLimitsMinute"]


class Limits(BaseModel):
    maximum_requests_per_day: int
    """The maximum number of requests allowed per day."""

    maximum_requests_per_hour: int
    """The maximum number of requests allowed per hour."""

    maximum_requests_per_minute: int
    """The maximum number of requests allowed per minute."""

    tokens_per_agent: int
    """The maximum number of tokens allowed per agent."""


class RateLimitsDay(BaseModel):
    count: int
    """The number of requests made in this time window."""

    exceeded: bool
    """Whether the rate limit has been exceeded for this time window."""

    limit: int
    """The maximum number of requests allowed in this time window."""

    remaining: int
    """The number of requests remaining before hitting the limit."""

    reset_time: str
    """ISO timestamp when the rate limit will reset."""


class RateLimitsHour(BaseModel):
    count: int
    """The number of requests made in this time window."""

    exceeded: bool
    """Whether the rate limit has been exceeded for this time window."""

    limit: int
    """The maximum number of requests allowed in this time window."""

    remaining: int
    """The number of requests remaining before hitting the limit."""

    reset_time: str
    """ISO timestamp when the rate limit will reset."""


class RateLimitsMinute(BaseModel):
    count: int
    """The number of requests made in this time window."""

    exceeded: bool
    """Whether the rate limit has been exceeded for this time window."""

    limit: int
    """The maximum number of requests allowed in this time window."""

    remaining: int
    """The number of requests remaining before hitting the limit."""

    reset_time: str
    """ISO timestamp when the rate limit will reset."""


class RateLimits(BaseModel):
    day: RateLimitsDay
    """Rate limit information for the last day."""

    hour: RateLimitsHour
    """Rate limit information for the last hour."""

    minute: RateLimitsMinute
    """Rate limit information for the last minute."""


class RateGetLimitsResponse(BaseModel):
    limits: Optional[Limits] = None
    """The configured rate limits based on the user's subscription tier."""

    rate_limits: Optional[RateLimits] = None
    """Current rate limit usage information for different time windows."""

    tier: Optional[str] = None
    """The user's current subscription tier (free or premium)."""

    timestamp: Optional[str] = None
    """ISO timestamp when the rate limits information was retrieved."""

    success: Optional[bool] = None
    """Indicates whether the rate limits request was successful."""
