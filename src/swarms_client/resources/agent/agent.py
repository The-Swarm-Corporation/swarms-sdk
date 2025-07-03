# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ...types import agent_run_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agent_spec_param import AgentSpecParam
from ...types.agent_run_response import AgentRunResponse

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#accessing-raw-response-data-eg-headers
        """
        return AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#with_streaming_response
        """
        return AgentResourceWithStreamingResponse(self)

    def run(
        self,
        *,
        agent_config: Optional[AgentSpecParam] | NotGiven = NOT_GIVEN,
        history: (
            Union[Dict[str, object], Iterable[Dict[str, str]], None] | NotGiven
        ) = NOT_GIVEN,
        img: Optional[str] | NotGiven = NOT_GIVEN,
        imgs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        task: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentRunResponse:
        """
        Run an agent with the specified task.

        Args:
          agent_config: The configuration of the agent to be completed.

          history: The history of the agent's previous tasks and responses. Can be either a
              dictionary or a list of message objects.

          img: An optional image URL that may be associated with the agent's task or
              representation.

          imgs: A list of image URLs that may be associated with the agent's task or
              representation.

          task: The task to be completed by the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/agent/completions",
            body=maybe_transform(
                {
                    "agent_config": agent_config,
                    "history": history,
                    "img": img,
                    "imgs": imgs,
                    "task": task,
                },
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=AgentRunResponse,
        )


class AsyncAgentResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#with_streaming_response
        """
        return AsyncAgentResourceWithStreamingResponse(self)

    async def run(
        self,
        *,
        agent_config: Optional[AgentSpecParam] | NotGiven = NOT_GIVEN,
        history: (
            Union[Dict[str, object], Iterable[Dict[str, str]], None] | NotGiven
        ) = NOT_GIVEN,
        img: Optional[str] | NotGiven = NOT_GIVEN,
        imgs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        task: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentRunResponse:
        """
        Run an agent with the specified task.

        Args:
          agent_config: The configuration of the agent to be completed.

          history: The history of the agent's previous tasks and responses. Can be either a
              dictionary or a list of message objects.

          img: An optional image URL that may be associated with the agent's task or
              representation.

          imgs: A list of image URLs that may be associated with the agent's task or
              representation.

          task: The task to be completed by the agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/agent/completions",
            body=await async_maybe_transform(
                {
                    "agent_config": agent_config,
                    "history": history,
                    "img": img,
                    "imgs": imgs,
                    "task": task,
                },
                agent_run_params.AgentRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=AgentRunResponse,
        )


class AgentResourceWithRawResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.run = to_raw_response_wrapper(
            agent.run,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._agent.batch)


class AsyncAgentResourceWithRawResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.run = async_to_raw_response_wrapper(
            agent.run,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._agent.batch)


class AgentResourceWithStreamingResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.run = to_streamed_response_wrapper(
            agent.run,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._agent.batch)


class AsyncAgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.run = async_to_streamed_response_wrapper(
            agent.run,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._agent.batch)
