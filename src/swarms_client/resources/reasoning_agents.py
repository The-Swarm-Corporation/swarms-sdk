# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import reasoning_agent_create_completion_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.reasoning_agent_list_types_response import ReasoningAgentListTypesResponse
from ..types.reasoning_agent_create_completion_response import ReasoningAgentCreateCompletionResponse

__all__ = ["ReasoningAgentsResource", "AsyncReasoningAgentsResource"]


class ReasoningAgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReasoningAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#accessing-raw-response-data-eg-headers
        """
        return ReasoningAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReasoningAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#with_streaming_response
        """
        return ReasoningAgentsResourceWithStreamingResponse(self)

    def create_completion(
        self,
        *,
        agent_name: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        max_loops: Optional[int] | NotGiven = NOT_GIVEN,
        memory_capacity: Optional[int] | NotGiven = NOT_GIVEN,
        model_name: Optional[str] | NotGiven = NOT_GIVEN,
        num_knowledge_items: Optional[int] | NotGiven = NOT_GIVEN,
        num_samples: Optional[int] | NotGiven = NOT_GIVEN,
        output_type: Optional[
            Literal[
                "list",
                "dict",
                "dictionary",
                "string",
                "str",
                "final",
                "last",
                "json",
                "all",
                "yaml",
                "xml",
                "dict-all-except-first",
                "str-all-except-first",
                "basemodel",
                "dict-final",
                "list-final",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        swarm_type: Optional[
            Literal[
                "reasoning-duo",
                "self-consistency",
                "ire",
                "reasoning-agent",
                "consistency-agent",
                "ire-agent",
                "ReflexionAgent",
                "GKPAgent",
                "AgentJudge",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        task: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReasoningAgentCreateCompletionResponse:
        """
        Run a reasoning agent with the specified task.

        Args:
          agent_name: The unique name assigned to the reasoning agent.

          description: A detailed explanation of the reasoning agent's purpose and capabilities.

          max_loops: The maximum number of times the reasoning agent is allowed to repeat its task.

          memory_capacity: The memory capacity for the reasoning agent.

          model_name: The name of the AI model that the reasoning agent will utilize.

          num_knowledge_items: The number of knowledge items to use for the reasoning agent.

          num_samples: The number of samples to generate for the reasoning agent.

          output_type: The type of output format for the reasoning agent.

          swarm_type: The type of reasoning swarm to use (e.g., reasoning duo, self-consistency, IRE).

          system_prompt: The initial instruction or context provided to the reasoning agent.

          task: The task to be completed by the reasoning agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/reasoning-agent/completions",
            body=maybe_transform(
                {
                    "agent_name": agent_name,
                    "description": description,
                    "max_loops": max_loops,
                    "memory_capacity": memory_capacity,
                    "model_name": model_name,
                    "num_knowledge_items": num_knowledge_items,
                    "num_samples": num_samples,
                    "output_type": output_type,
                    "swarm_type": swarm_type,
                    "system_prompt": system_prompt,
                    "task": task,
                },
                reasoning_agent_create_completion_params.ReasoningAgentCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReasoningAgentCreateCompletionResponse,
        )

    def list_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReasoningAgentListTypesResponse:
        """Get the types of reasoning agents available."""
        return self._get(
            "/v1/reasoning-agent/types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReasoningAgentListTypesResponse,
        )


class AsyncReasoningAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReasoningAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReasoningAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReasoningAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-sdk#with_streaming_response
        """
        return AsyncReasoningAgentsResourceWithStreamingResponse(self)

    async def create_completion(
        self,
        *,
        agent_name: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        max_loops: Optional[int] | NotGiven = NOT_GIVEN,
        memory_capacity: Optional[int] | NotGiven = NOT_GIVEN,
        model_name: Optional[str] | NotGiven = NOT_GIVEN,
        num_knowledge_items: Optional[int] | NotGiven = NOT_GIVEN,
        num_samples: Optional[int] | NotGiven = NOT_GIVEN,
        output_type: Optional[
            Literal[
                "list",
                "dict",
                "dictionary",
                "string",
                "str",
                "final",
                "last",
                "json",
                "all",
                "yaml",
                "xml",
                "dict-all-except-first",
                "str-all-except-first",
                "basemodel",
                "dict-final",
                "list-final",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        swarm_type: Optional[
            Literal[
                "reasoning-duo",
                "self-consistency",
                "ire",
                "reasoning-agent",
                "consistency-agent",
                "ire-agent",
                "ReflexionAgent",
                "GKPAgent",
                "AgentJudge",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        task: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReasoningAgentCreateCompletionResponse:
        """
        Run a reasoning agent with the specified task.

        Args:
          agent_name: The unique name assigned to the reasoning agent.

          description: A detailed explanation of the reasoning agent's purpose and capabilities.

          max_loops: The maximum number of times the reasoning agent is allowed to repeat its task.

          memory_capacity: The memory capacity for the reasoning agent.

          model_name: The name of the AI model that the reasoning agent will utilize.

          num_knowledge_items: The number of knowledge items to use for the reasoning agent.

          num_samples: The number of samples to generate for the reasoning agent.

          output_type: The type of output format for the reasoning agent.

          swarm_type: The type of reasoning swarm to use (e.g., reasoning duo, self-consistency, IRE).

          system_prompt: The initial instruction or context provided to the reasoning agent.

          task: The task to be completed by the reasoning agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/reasoning-agent/completions",
            body=await async_maybe_transform(
                {
                    "agent_name": agent_name,
                    "description": description,
                    "max_loops": max_loops,
                    "memory_capacity": memory_capacity,
                    "model_name": model_name,
                    "num_knowledge_items": num_knowledge_items,
                    "num_samples": num_samples,
                    "output_type": output_type,
                    "swarm_type": swarm_type,
                    "system_prompt": system_prompt,
                    "task": task,
                },
                reasoning_agent_create_completion_params.ReasoningAgentCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReasoningAgentCreateCompletionResponse,
        )

    async def list_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReasoningAgentListTypesResponse:
        """Get the types of reasoning agents available."""
        return await self._get(
            "/v1/reasoning-agent/types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReasoningAgentListTypesResponse,
        )


class ReasoningAgentsResourceWithRawResponse:
    def __init__(self, reasoning_agents: ReasoningAgentsResource) -> None:
        self._reasoning_agents = reasoning_agents

        self.create_completion = to_raw_response_wrapper(
            reasoning_agents.create_completion,
        )
        self.list_types = to_raw_response_wrapper(
            reasoning_agents.list_types,
        )


class AsyncReasoningAgentsResourceWithRawResponse:
    def __init__(self, reasoning_agents: AsyncReasoningAgentsResource) -> None:
        self._reasoning_agents = reasoning_agents

        self.create_completion = async_to_raw_response_wrapper(
            reasoning_agents.create_completion,
        )
        self.list_types = async_to_raw_response_wrapper(
            reasoning_agents.list_types,
        )


class ReasoningAgentsResourceWithStreamingResponse:
    def __init__(self, reasoning_agents: ReasoningAgentsResource) -> None:
        self._reasoning_agents = reasoning_agents

        self.create_completion = to_streamed_response_wrapper(
            reasoning_agents.create_completion,
        )
        self.list_types = to_streamed_response_wrapper(
            reasoning_agents.list_types,
        )


class AsyncReasoningAgentsResourceWithStreamingResponse:
    def __init__(self, reasoning_agents: AsyncReasoningAgentsResource) -> None:
        self._reasoning_agents = reasoning_agents

        self.create_completion = async_to_streamed_response_wrapper(
            reasoning_agents.create_completion,
        )
        self.list_types = async_to_streamed_response_wrapper(
            reasoning_agents.list_types,
        )
