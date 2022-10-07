from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.pipeline_variable import PipelineVariable
from ...types import Response


def _get_kwargs(
    workspace: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/pipelines-config/variables".format(client.base_url, workspace=workspace)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, PipelineVariable]]:
    if response.status_code == 201:
        response_201 = PipelineVariable.from_dict(response.json())

        return response_201
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, PipelineVariable]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    *,
    client: Client,
) -> Response[Union[Error, PipelineVariable]]:
    """Create a variable for a workspace

     Create a workspace level variable.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, PipelineVariable]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    *,
    client: Client,
) -> Optional[Union[Error, PipelineVariable]]:
    """Create a variable for a workspace

     Create a workspace level variable.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, PipelineVariable]]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: Client,
) -> Response[Union[Error, PipelineVariable]]:
    """Create a variable for a workspace

     Create a workspace level variable.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, PipelineVariable]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    *,
    client: Client,
) -> Optional[Union[Error, PipelineVariable]]:
    """Create a variable for a workspace

     Create a workspace level variable.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, PipelineVariable]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
        )
    ).parsed
