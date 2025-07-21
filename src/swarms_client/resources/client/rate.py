# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.client.rate_get_limits_response import RateGetLimitsResponse

__all__ = ["RateResource", "AsyncRateResource"]


class RateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#accessing-raw-response-data-eg-headers
        """
        return RateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#with_streaming_response
        """
        return RateResourceWithStreamingResponse(self)

    def get_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateGetLimitsResponse:
        """
        Get the rate limits and current usage for the user associated with the provided
        API key.
        """
        return self._get(
            "/v1/rate/limits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=RateGetLimitsResponse,
        )


class AsyncRateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#with_streaming_response
        """
        return AsyncRateResourceWithStreamingResponse(self)

    async def get_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateGetLimitsResponse:
        """
        Get the rate limits and current usage for the user associated with the provided
        API key.
        """
        return await self._get(
            "/v1/rate/limits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=RateGetLimitsResponse,
        )


class RateResourceWithRawResponse:
    def __init__(self, rate: RateResource) -> None:
        self._rate = rate

        self.get_limits = to_raw_response_wrapper(
            rate.get_limits,
        )


class AsyncRateResourceWithRawResponse:
    def __init__(self, rate: AsyncRateResource) -> None:
        self._rate = rate

        self.get_limits = async_to_raw_response_wrapper(
            rate.get_limits,
        )


class RateResourceWithStreamingResponse:
    def __init__(self, rate: RateResource) -> None:
        self._rate = rate

        self.get_limits = to_streamed_response_wrapper(
            rate.get_limits,
        )


class AsyncRateResourceWithStreamingResponse:
    def __init__(self, rate: AsyncRateResource) -> None:
        self._rate = rate

        self.get_limits = async_to_streamed_response_wrapper(
            rate.get_limits,
        )
