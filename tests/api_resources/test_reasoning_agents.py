# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from swarms_client import SwarmsClient, AsyncSwarmsClient
from swarms_client.types import (
    ReasoningAgentListTypesResponse,
    ReasoningAgentCreateCompletionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReasoningAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_completion(self, client: SwarmsClient) -> None:
        reasoning_agent = client.reasoning_agents.create_completion()
        assert_matches_type(ReasoningAgentCreateCompletionResponse, reasoning_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_completion_with_all_params(self, client: SwarmsClient) -> None:
        reasoning_agent = client.reasoning_agents.create_completion(
            agent_name="agent_name",
            description="description",
            max_loops=0,
            memory_capacity=0,
            model_name="model_name",
            num_knowledge_items=0,
            num_samples=0,
            output_type="list",
            swarm_type="reasoning-duo",
            system_prompt="system_prompt",
            task="task",
        )
        assert_matches_type(ReasoningAgentCreateCompletionResponse, reasoning_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_completion(self, client: SwarmsClient) -> None:
        response = client.reasoning_agents.with_raw_response.create_completion()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reasoning_agent = response.parse()
        assert_matches_type(ReasoningAgentCreateCompletionResponse, reasoning_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_completion(self, client: SwarmsClient) -> None:
        with client.reasoning_agents.with_streaming_response.create_completion() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reasoning_agent = response.parse()
            assert_matches_type(ReasoningAgentCreateCompletionResponse, reasoning_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_types(self, client: SwarmsClient) -> None:
        reasoning_agent = client.reasoning_agents.list_types()
        assert_matches_type(ReasoningAgentListTypesResponse, reasoning_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_types(self, client: SwarmsClient) -> None:
        response = client.reasoning_agents.with_raw_response.list_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reasoning_agent = response.parse()
        assert_matches_type(ReasoningAgentListTypesResponse, reasoning_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_types(self, client: SwarmsClient) -> None:
        with client.reasoning_agents.with_streaming_response.list_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reasoning_agent = response.parse()
            assert_matches_type(ReasoningAgentListTypesResponse, reasoning_agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReasoningAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_completion(self, async_client: AsyncSwarmsClient) -> None:
        reasoning_agent = await async_client.reasoning_agents.create_completion()
        assert_matches_type(ReasoningAgentCreateCompletionResponse, reasoning_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_completion_with_all_params(self, async_client: AsyncSwarmsClient) -> None:
        reasoning_agent = await async_client.reasoning_agents.create_completion(
            agent_name="agent_name",
            description="description",
            max_loops=0,
            memory_capacity=0,
            model_name="model_name",
            num_knowledge_items=0,
            num_samples=0,
            output_type="list",
            swarm_type="reasoning-duo",
            system_prompt="system_prompt",
            task="task",
        )
        assert_matches_type(ReasoningAgentCreateCompletionResponse, reasoning_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncSwarmsClient) -> None:
        response = await async_client.reasoning_agents.with_raw_response.create_completion()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reasoning_agent = await response.parse()
        assert_matches_type(ReasoningAgentCreateCompletionResponse, reasoning_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncSwarmsClient) -> None:
        async with async_client.reasoning_agents.with_streaming_response.create_completion() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reasoning_agent = await response.parse()
            assert_matches_type(ReasoningAgentCreateCompletionResponse, reasoning_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_types(self, async_client: AsyncSwarmsClient) -> None:
        reasoning_agent = await async_client.reasoning_agents.list_types()
        assert_matches_type(ReasoningAgentListTypesResponse, reasoning_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_types(self, async_client: AsyncSwarmsClient) -> None:
        response = await async_client.reasoning_agents.with_raw_response.list_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reasoning_agent = await response.parse()
        assert_matches_type(ReasoningAgentListTypesResponse, reasoning_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_types(self, async_client: AsyncSwarmsClient) -> None:
        async with async_client.reasoning_agents.with_streaming_response.list_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reasoning_agent = await response.parse()
            assert_matches_type(ReasoningAgentListTypesResponse, reasoning_agent, path=["response"])

        assert cast(Any, response.is_closed) is True
