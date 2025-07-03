from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_completion import AgentCompletion
from ...models.http_validation_error import HTTPValidationError
from ...models.run_agent_v1_agent_completions_post_response_run_agent_v1_agent_completions_post import (
    RunAgentV1AgentCompletionsPostResponseRunAgentV1AgentCompletionsPost,
)
from ...types import Response


def _get_kwargs(
    *,
    body: AgentCompletion,
    x_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-key"] = x_api_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/agent/completions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, RunAgentV1AgentCompletionsPostResponseRunAgentV1AgentCompletionsPost]]:
    if response.status_code == 200:
        response_200 = RunAgentV1AgentCompletionsPostResponseRunAgentV1AgentCompletionsPost.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, RunAgentV1AgentCompletionsPostResponseRunAgentV1AgentCompletionsPost]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AgentCompletion,
    x_api_key: str,
) -> Response[Union[HTTPValidationError, RunAgentV1AgentCompletionsPostResponseRunAgentV1AgentCompletionsPost]]:
    """Run Agent

     Run an agent with the specified task.

    Args:
        x_api_key (str):
        body (AgentCompletion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RunAgentV1AgentCompletionsPostResponseRunAgentV1AgentCompletionsPost]]
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
    body: AgentCompletion,
    x_api_key: str,
) -> Optional[Union[HTTPValidationError, RunAgentV1AgentCompletionsPostResponseRunAgentV1AgentCompletionsPost]]:
    """Run Agent

     Run an agent with the specified task.

    Args:
        x_api_key (str):
        body (AgentCompletion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, RunAgentV1AgentCompletionsPostResponseRunAgentV1AgentCompletionsPost]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: AgentCompletion,
    x_api_key: str,
) -> Response[Union[HTTPValidationError, RunAgentV1AgentCompletionsPostResponseRunAgentV1AgentCompletionsPost]]:
    """Run Agent

     Run an agent with the specified task.

    Args:
        x_api_key (str):
        body (AgentCompletion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, RunAgentV1AgentCompletionsPostResponseRunAgentV1AgentCompletionsPost]]
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
    body: AgentCompletion,
    x_api_key: str,
) -> Optional[Union[HTTPValidationError, RunAgentV1AgentCompletionsPostResponseRunAgentV1AgentCompletionsPost]]:
    """Run Agent

     Run an agent with the specified task.

    Args:
        x_api_key (str):
        body (AgentCompletion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, RunAgentV1AgentCompletionsPostResponseRunAgentV1AgentCompletionsPost]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_api_key=x_api_key,
        )
    ).parsed
