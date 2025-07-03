# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from swarms import Swarms, AsyncSwarms
from tests.utils import assert_matches_type
from swarms.types.swarms import BatchRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run(self, client: Swarms) -> None:
        batch = client.swarms.batch.run(
            body=[{}],
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchRunResponse, batch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run(self, client: Swarms) -> None:
        response = client.swarms.batch.with_raw_response.run(
            body=[{}],
            x_api_key="x-api-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchRunResponse, batch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run(self, client: Swarms) -> None:
        with client.swarms.batch.with_streaming_response.run(
            body=[{}],
            x_api_key="x-api-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchRunResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run(self, async_client: AsyncSwarms) -> None:
        batch = await async_client.swarms.batch.run(
            body=[{}],
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchRunResponse, batch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncSwarms) -> None:
        response = await async_client.swarms.batch.with_raw_response.run(
            body=[{}],
            x_api_key="x-api-key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchRunResponse, batch, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncSwarms) -> None:
        async with async_client.swarms.batch.with_streaming_response.run(
            body=[{}],
            x_api_key="x-api-key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchRunResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True
