# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from swarms_client import SwarmsClient, AsyncSwarmsClient
from swarms_client.types import AgentRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize(
        "client", [False, True], indirect=True, ids=["loose", "strict"]
    )

    @pytest.mark.skip()
    @parametrize
    def test_method_run(self, client: SwarmsClient) -> None:
        agent = client.agent.run()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params(self, client: SwarmsClient) -> None:
        agent = client.agent.run(
            agent_config={
                "agent_name": "agent_name",
                "auto_generate_prompt": True,
                "description": "description",
                "max_loops": 0,
                "max_tokens": 0,
                "mcp_url": "mcp_url",
                "model_name": "model_name",
                "role": "role",
                "streaming_on": True,
                "system_prompt": "system_prompt",
                "temperature": 0,
                "tools_list_dictionary": [{"foo": "bar"}],
            },
            history={"foo": "bar"},
            img="img",
            imgs=["string"],
            task="task",
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run(self, client: SwarmsClient) -> None:
        response = client.agent.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run(self, client: SwarmsClient) -> None:
        with client.agent.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRunResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run(self, async_client: AsyncSwarmsClient) -> None:
        agent = await async_client.agent.run()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params(
        self, async_client: AsyncSwarmsClient
    ) -> None:
        agent = await async_client.agent.run(
            agent_config={
                "agent_name": "agent_name",
                "auto_generate_prompt": True,
                "description": "description",
                "max_loops": 0,
                "max_tokens": 0,
                "mcp_url": "mcp_url",
                "model_name": "model_name",
                "role": "role",
                "streaming_on": True,
                "system_prompt": "system_prompt",
                "temperature": 0,
                "tools_list_dictionary": [{"foo": "bar"}],
            },
            history={"foo": "bar"},
            img="img",
            imgs=["string"],
            task="task",
        )
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncSwarmsClient) -> None:
        response = await async_client.agent.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRunResponse, agent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run(
        self, async_client: AsyncSwarmsClient
    ) -> None:
        async with async_client.agent.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRunResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
