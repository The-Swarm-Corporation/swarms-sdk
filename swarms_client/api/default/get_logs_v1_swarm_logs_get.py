from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_logs_v1_swarm_logs_get_response_get_logs_v1_swarm_logs_get import (
    GetLogsV1SwarmLogsGetResponseGetLogsV1SwarmLogsGet,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    x_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-key"] = x_api_key

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/swarm/logs",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetLogsV1SwarmLogsGetResponseGetLogsV1SwarmLogsGet, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = GetLogsV1SwarmLogsGetResponseGetLogsV1SwarmLogsGet.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetLogsV1SwarmLogsGetResponseGetLogsV1SwarmLogsGet, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_key: str,
) -> Response[Union[GetLogsV1SwarmLogsGetResponseGetLogsV1SwarmLogsGet, HTTPValidationError]]:
    """Get Logs

     Get all API request logs for the user associated with the provided API key,
    excluding any logs that contain a client_ip field in their data.

    Args:
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetLogsV1SwarmLogsGetResponseGetLogsV1SwarmLogsGet, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        x_api_key=x_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_key: str,
) -> Optional[Union[GetLogsV1SwarmLogsGetResponseGetLogsV1SwarmLogsGet, HTTPValidationError]]:
    """Get Logs

     Get all API request logs for the user associated with the provided API key,
    excluding any logs that contain a client_ip field in their data.

    Args:
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetLogsV1SwarmLogsGetResponseGetLogsV1SwarmLogsGet, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_key: str,
) -> Response[Union[GetLogsV1SwarmLogsGetResponseGetLogsV1SwarmLogsGet, HTTPValidationError]]:
    """Get Logs

     Get all API request logs for the user associated with the provided API key,
    excluding any logs that contain a client_ip field in their data.

    Args:
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetLogsV1SwarmLogsGetResponseGetLogsV1SwarmLogsGet, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        x_api_key=x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_key: str,
) -> Optional[Union[GetLogsV1SwarmLogsGetResponseGetLogsV1SwarmLogsGet, HTTPValidationError]]:
    """Get Logs

     Get all API request logs for the user associated with the provided API key,
    excluding any logs that contain a client_ip field in their data.

    Args:
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetLogsV1SwarmLogsGetResponseGetLogsV1SwarmLogsGet, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_api_key=x_api_key,
        )
    ).parsed
