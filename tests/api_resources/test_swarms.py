# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from swarms import Swarms, AsyncSwarms
from tests.utils import assert_matches_type
from swarms.types import SwarmRunResponse, SwarmGetLogsResponse, SwarmCheckAvailableResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSwarms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_check_available(self, client: Swarms) -> None:
        swarm = client.swarms.check_available(
            x_api_key="x-api-key",
        )
        assert_matches_type(SwarmCheckAvailableResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check_available(self, client: Swarms) -> None:
        response = client.swarms.with_raw_response.check_available(
            x_api_key="x-api-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swarm = response.parse()
        assert_matches_type(SwarmCheckAvailableResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check_available(self, client: Swarms) -> None:
        with client.swarms.with_streaming_response.check_available(
            x_api_key="x-api-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swarm = response.parse()
            assert_matches_type(SwarmCheckAvailableResponse, swarm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_logs(self, client: Swarms) -> None:
        swarm = client.swarms.get_logs(
            x_api_key="x-api-key",
        )
        assert_matches_type(SwarmGetLogsResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_logs(self, client: Swarms) -> None:
        response = client.swarms.with_raw_response.get_logs(
            x_api_key="x-api-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swarm = response.parse()
        assert_matches_type(SwarmGetLogsResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_logs(self, client: Swarms) -> None:
        with client.swarms.with_streaming_response.get_logs(
            x_api_key="x-api-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swarm = response.parse()
            assert_matches_type(SwarmGetLogsResponse, swarm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_run(self, client: Swarms) -> None:
        swarm = client.swarms.run(
            x_api_key="x-api-key",
        )
        assert_matches_type(SwarmRunResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params(self, client: Swarms) -> None:
        swarm = client.swarms.run(
            x_api_key="x-api-key",
            agents=[
                {
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
                }
            ],
            description="description",
            img="img",
            max_loops=0,
            messages=[{"foo": "bar"}],
            name="name",
            rearrange_flow="rearrange_flow",
            return_history=True,
            rules="rules",
            service_tier="service_tier",
            stream=True,
            swarm_type="AgentRearrange",
            task="task",
            tasks=["string"],
        )
        assert_matches_type(SwarmRunResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run(self, client: Swarms) -> None:
        response = client.swarms.with_raw_response.run(
            x_api_key="x-api-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swarm = response.parse()
        assert_matches_type(SwarmRunResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run(self, client: Swarms) -> None:
        with client.swarms.with_streaming_response.run(
            x_api_key="x-api-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swarm = response.parse()
            assert_matches_type(SwarmRunResponse, swarm, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSwarms:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_check_available(self, async_client: AsyncSwarms) -> None:
        swarm = await async_client.swarms.check_available(
            x_api_key="x-api-key",
        )
        assert_matches_type(SwarmCheckAvailableResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check_available(self, async_client: AsyncSwarms) -> None:
        response = await async_client.swarms.with_raw_response.check_available(
            x_api_key="x-api-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swarm = await response.parse()
        assert_matches_type(SwarmCheckAvailableResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check_available(self, async_client: AsyncSwarms) -> None:
        async with async_client.swarms.with_streaming_response.check_available(
            x_api_key="x-api-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swarm = await response.parse()
            assert_matches_type(SwarmCheckAvailableResponse, swarm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_logs(self, async_client: AsyncSwarms) -> None:
        swarm = await async_client.swarms.get_logs(
            x_api_key="x-api-key",
        )
        assert_matches_type(SwarmGetLogsResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_logs(self, async_client: AsyncSwarms) -> None:
        response = await async_client.swarms.with_raw_response.get_logs(
            x_api_key="x-api-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swarm = await response.parse()
        assert_matches_type(SwarmGetLogsResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_logs(self, async_client: AsyncSwarms) -> None:
        async with async_client.swarms.with_streaming_response.get_logs(
            x_api_key="x-api-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swarm = await response.parse()
            assert_matches_type(SwarmGetLogsResponse, swarm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_run(self, async_client: AsyncSwarms) -> None:
        swarm = await async_client.swarms.run(
            x_api_key="x-api-key",
        )
        assert_matches_type(SwarmRunResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncSwarms) -> None:
        swarm = await async_client.swarms.run(
            x_api_key="x-api-key",
            agents=[
                {
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
                }
            ],
            description="description",
            img="img",
            max_loops=0,
            messages=[{"foo": "bar"}],
            name="name",
            rearrange_flow="rearrange_flow",
            return_history=True,
            rules="rules",
            service_tier="service_tier",
            stream=True,
            swarm_type="AgentRearrange",
            task="task",
            tasks=["string"],
        )
        assert_matches_type(SwarmRunResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncSwarms) -> None:
        response = await async_client.swarms.with_raw_response.run(
            x_api_key="x-api-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        swarm = await response.parse()
        assert_matches_type(SwarmRunResponse, swarm, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncSwarms) -> None:
        async with async_client.swarms.with_streaming_response.run(
            x_api_key="x-api-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            swarm = await response.parse()
            assert_matches_type(SwarmRunResponse, swarm, path=["response"])

        assert cast(Any, response.is_closed) is True
