# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from swarms_client import SwarmsClient, AsyncSwarmsClient
from swarms_client.types.client import RateGetLimitsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRate:
    parametrize = pytest.mark.parametrize(
        "client", [False, True], indirect=True, ids=["loose", "strict"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_limits(self, client: SwarmsClient) -> None:
        rate = client.client.rate.get_limits()
        assert_matches_type(RateGetLimitsResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_limits(self, client: SwarmsClient) -> None:
        response = client.client.rate.with_raw_response.get_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = response.parse()
        assert_matches_type(RateGetLimitsResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_limits(self, client: SwarmsClient) -> None:
        with client.client.rate.with_streaming_response.get_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = response.parse()
            assert_matches_type(RateGetLimitsResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRate:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_limits(self, async_client: AsyncSwarmsClient) -> None:
        rate = await async_client.client.rate.get_limits()
        assert_matches_type(RateGetLimitsResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_limits(
        self, async_client: AsyncSwarmsClient
    ) -> None:
        response = await async_client.client.rate.with_raw_response.get_limits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate = await response.parse()
        assert_matches_type(RateGetLimitsResponse, rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_limits(
        self, async_client: AsyncSwarmsClient
    ) -> None:
        async with async_client.client.rate.with_streaming_response.get_limits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate = await response.parse()
            assert_matches_type(RateGetLimitsResponse, rate, path=["response"])

        assert cast(Any, response.is_closed) is True
