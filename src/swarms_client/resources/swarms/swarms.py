# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ...types import swarm_run_params
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
from ...types.swarm_run_response import SwarmRunResponse
from ...types.swarm_get_logs_response import SwarmGetLogsResponse
from ...types.swarm_check_available_response import SwarmCheckAvailableResponse

__all__ = ["SwarmsResource", "AsyncSwarmsResource"]


class SwarmsResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> SwarmsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#accessing-raw-response-data-eg-headers
        """
        return SwarmsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SwarmsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#with_streaming_response
        """
        return SwarmsResourceWithStreamingResponse(self)

    def check_available(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SwarmCheckAvailableResponse:
        """Check the available swarm types."""
        return self._get(
            "/v1/swarms/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=SwarmCheckAvailableResponse,
        )

    def get_logs(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SwarmGetLogsResponse:
        """
        Get all API request logs for the user associated with the provided API key,
        excluding any logs that contain a client_ip field in their data.
        """
        return self._get(
            "/v1/swarm/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=SwarmGetLogsResponse,
        )

    def run(
        self,
        *,
        agents: Optional[Iterable[AgentSpecParam]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        img: Optional[str] | NotGiven = NOT_GIVEN,
        max_loops: Optional[int] | NotGiven = NOT_GIVEN,
        messages: (
            Union[Iterable[Dict[str, object]], Dict[str, object], None] | NotGiven
        ) = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        rearrange_flow: Optional[str] | NotGiven = NOT_GIVEN,
        return_history: Optional[bool] | NotGiven = NOT_GIVEN,
        rules: Optional[str] | NotGiven = NOT_GIVEN,
        service_tier: Optional[str] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        swarm_type: (
            Optional[
                Literal[
                    "AgentRearrange",
                    "MixtureOfAgents",
                    "SpreadSheetSwarm",
                    "SequentialWorkflow",
                    "ConcurrentWorkflow",
                    "GroupChat",
                    "MultiAgentRouter",
                    "AutoSwarmBuilder",
                    "HiearchicalSwarm",
                    "auto",
                    "MajorityVoting",
                    "MALT",
                    "DeepResearchSwarm",
                    "CouncilAsAJudge",
                    "InteractiveGroupChat",
                ]
            ]
            | NotGiven
        ) = NOT_GIVEN,
        task: Optional[str] | NotGiven = NOT_GIVEN,
        tasks: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SwarmRunResponse:
        """
        Run a swarm with the specified task.

        Args:
          agents: A list of agents or specifications that define the agents participating in the
              swarm.

          description: A comprehensive description of the swarm's objectives, capabilities, and
              intended outcomes.

          img: An optional image URL that may be associated with the swarm's task or
              representation.

          max_loops: The maximum number of execution loops allowed for the swarm, enabling repeated
              processing if needed.

          messages: A list of messages that the swarm should complete.

          name: The name of the swarm, which serves as an identifier for the group of agents and
              their collective task.

          rearrange_flow: Instructions on how to rearrange the flow of tasks among agents, if applicable.

          return_history: A flag indicating whether the swarm should return its execution history along
              with the final output.

          rules: Guidelines or constraints that govern the behavior and interactions of the
              agents within the swarm.

          service_tier: The service tier to use for processing. Options: 'standard' (default) or 'flex'
              for lower cost but slower processing.

          stream: A flag indicating whether the swarm should stream its output.

          swarm_type: The classification of the swarm, indicating its operational style and
              methodology.

          task: The specific task or objective that the swarm is designed to accomplish.

          tasks: A list of tasks that the swarm should complete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/swarm/completions",
            body=maybe_transform(
                {
                    "agents": agents,
                    "description": description,
                    "img": img,
                    "max_loops": max_loops,
                    "messages": messages,
                    "name": name,
                    "rearrange_flow": rearrange_flow,
                    "return_history": return_history,
                    "rules": rules,
                    "service_tier": service_tier,
                    "stream": stream,
                    "swarm_type": swarm_type,
                    "task": task,
                    "tasks": tasks,
                },
                swarm_run_params.SwarmRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=SwarmRunResponse,
        )


class AsyncSwarmsResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSwarmsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSwarmsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSwarmsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#with_streaming_response
        """
        return AsyncSwarmsResourceWithStreamingResponse(self)

    async def check_available(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SwarmCheckAvailableResponse:
        """Check the available swarm types."""
        return await self._get(
            "/v1/swarms/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=SwarmCheckAvailableResponse,
        )

    async def get_logs(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SwarmGetLogsResponse:
        """
        Get all API request logs for the user associated with the provided API key,
        excluding any logs that contain a client_ip field in their data.
        """
        return await self._get(
            "/v1/swarm/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=SwarmGetLogsResponse,
        )

    async def run(
        self,
        *,
        agents: Optional[Iterable[AgentSpecParam]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        img: Optional[str] | NotGiven = NOT_GIVEN,
        max_loops: Optional[int] | NotGiven = NOT_GIVEN,
        messages: (
            Union[Iterable[Dict[str, object]], Dict[str, object], None] | NotGiven
        ) = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        rearrange_flow: Optional[str] | NotGiven = NOT_GIVEN,
        return_history: Optional[bool] | NotGiven = NOT_GIVEN,
        rules: Optional[str] | NotGiven = NOT_GIVEN,
        service_tier: Optional[str] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        swarm_type: (
            Optional[
                Literal[
                    "AgentRearrange",
                    "MixtureOfAgents",
                    "SpreadSheetSwarm",
                    "SequentialWorkflow",
                    "ConcurrentWorkflow",
                    "GroupChat",
                    "MultiAgentRouter",
                    "AutoSwarmBuilder",
                    "HiearchicalSwarm",
                    "auto",
                    "MajorityVoting",
                    "MALT",
                    "DeepResearchSwarm",
                    "CouncilAsAJudge",
                    "InteractiveGroupChat",
                ]
            ]
            | NotGiven
        ) = NOT_GIVEN,
        task: Optional[str] | NotGiven = NOT_GIVEN,
        tasks: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SwarmRunResponse:
        """
        Run a swarm with the specified task.

        Args:
          agents: A list of agents or specifications that define the agents participating in the
              swarm.

          description: A comprehensive description of the swarm's objectives, capabilities, and
              intended outcomes.

          img: An optional image URL that may be associated with the swarm's task or
              representation.

          max_loops: The maximum number of execution loops allowed for the swarm, enabling repeated
              processing if needed.

          messages: A list of messages that the swarm should complete.

          name: The name of the swarm, which serves as an identifier for the group of agents and
              their collective task.

          rearrange_flow: Instructions on how to rearrange the flow of tasks among agents, if applicable.

          return_history: A flag indicating whether the swarm should return its execution history along
              with the final output.

          rules: Guidelines or constraints that govern the behavior and interactions of the
              agents within the swarm.

          service_tier: The service tier to use for processing. Options: 'standard' (default) or 'flex'
              for lower cost but slower processing.

          stream: A flag indicating whether the swarm should stream its output.

          swarm_type: The classification of the swarm, indicating its operational style and
              methodology.

          task: The specific task or objective that the swarm is designed to accomplish.

          tasks: A list of tasks that the swarm should complete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/swarm/completions",
            body=await async_maybe_transform(
                {
                    "agents": agents,
                    "description": description,
                    "img": img,
                    "max_loops": max_loops,
                    "messages": messages,
                    "name": name,
                    "rearrange_flow": rearrange_flow,
                    "return_history": return_history,
                    "rules": rules,
                    "service_tier": service_tier,
                    "stream": stream,
                    "swarm_type": swarm_type,
                    "task": task,
                    "tasks": tasks,
                },
                swarm_run_params.SwarmRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=SwarmRunResponse,
        )


class SwarmsResourceWithRawResponse:
    def __init__(self, swarms: SwarmsResource) -> None:
        self._swarms = swarms

        self.check_available = to_raw_response_wrapper(
            swarms.check_available,
        )
        self.get_logs = to_raw_response_wrapper(
            swarms.get_logs,
        )
        self.run = to_raw_response_wrapper(
            swarms.run,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._swarms.batch)


class AsyncSwarmsResourceWithRawResponse:
    def __init__(self, swarms: AsyncSwarmsResource) -> None:
        self._swarms = swarms

        self.check_available = async_to_raw_response_wrapper(
            swarms.check_available,
        )
        self.get_logs = async_to_raw_response_wrapper(
            swarms.get_logs,
        )
        self.run = async_to_raw_response_wrapper(
            swarms.run,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._swarms.batch)


class SwarmsResourceWithStreamingResponse:
    def __init__(self, swarms: SwarmsResource) -> None:
        self._swarms = swarms

        self.check_available = to_streamed_response_wrapper(
            swarms.check_available,
        )
        self.get_logs = to_streamed_response_wrapper(
            swarms.get_logs,
        )
        self.run = to_streamed_response_wrapper(
            swarms.run,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._swarms.batch)


class AsyncSwarmsResourceWithStreamingResponse:
    def __init__(self, swarms: AsyncSwarmsResource) -> None:
        self._swarms = swarms

        self.check_available = async_to_streamed_response_wrapper(
            swarms.check_available,
        )
        self.get_logs = async_to_streamed_response_wrapper(
            swarms.get_logs,
        )
        self.run = async_to_streamed_response_wrapper(
            swarms.run,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._swarms.batch)
