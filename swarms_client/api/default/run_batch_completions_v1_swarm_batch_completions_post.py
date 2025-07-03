from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.run_batch_completions_v1_swarm_batch_completions_post_response_200_item import (
    RunBatchCompletionsV1SwarmBatchCompletionsPostResponse200Item,
)
from ...models.swarm_spec import SwarmSpec
from ...types import Response


def _get_kwargs(
    *,
    body: list["SwarmSpec"],
    x_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-key"] = x_api_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/swarm/batch/completions",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, list["RunBatchCompletionsV1SwarmBatchCompletionsPostResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RunBatchCompletionsV1SwarmBatchCompletionsPostResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
) -> Response[Union[HTTPValidationError, list["RunBatchCompletionsV1SwarmBatchCompletionsPostResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["SwarmSpec"],
    x_api_key: str,
) -> Response[Union[HTTPValidationError, list["RunBatchCompletionsV1SwarmBatchCompletionsPostResponse200Item"]]]:
    """Run Batch Completions

     Run a batch of swarms with the specified tasks using a thread pool.

    Args:
        x_api_key (str):
        body (list['SwarmSpec']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['RunBatchCompletionsV1SwarmBatchCompletionsPostResponse200Item']]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_api_key=x_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["SwarmSpec"],
    x_api_key: str,
) -> Optional[Union[HTTPValidationError, list["RunBatchCompletionsV1SwarmBatchCompletionsPostResponse200Item"]]]:
    """Run Batch Completions

     Run a batch of swarms with the specified tasks using a thread pool.

    Args:
        x_api_key (str):
        body (list['SwarmSpec']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['RunBatchCompletionsV1SwarmBatchCompletionsPostResponse200Item']]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["SwarmSpec"],
    x_api_key: str,
) -> Response[Union[HTTPValidationError, list["RunBatchCompletionsV1SwarmBatchCompletionsPostResponse200Item"]]]:
    """Run Batch Completions

     Run a batch of swarms with the specified tasks using a thread pool.

    Args:
        x_api_key (str):
        body (list['SwarmSpec']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['RunBatchCompletionsV1SwarmBatchCompletionsPostResponse200Item']]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_api_key=x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list["SwarmSpec"],
    x_api_key: str,
) -> Optional[Union[HTTPValidationError, list["RunBatchCompletionsV1SwarmBatchCompletionsPostResponse200Item"]]]:
    """Run Batch Completions

     Run a batch of swarms with the specified tasks using a thread pool.

    Args:
        x_api_key (str):
        body (list['SwarmSpec']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['RunBatchCompletionsV1SwarmBatchCompletionsPostResponse200Item']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_api_key=x_api_key,
        )
    ).parsed
