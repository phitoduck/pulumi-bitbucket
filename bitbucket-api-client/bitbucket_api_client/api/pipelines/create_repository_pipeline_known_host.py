from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.pipeline_known_host import PipelineKnownHost
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    client: Client,
    json_body: PipelineKnownHost,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, PipelineKnownHost]]:
    if response.status_code == 201:
        response_201 = PipelineKnownHost.from_dict(response.json())

        return response_201
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, PipelineKnownHost]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: Client,
    json_body: PipelineKnownHost,
) -> Response[Union[Error, PipelineKnownHost]]:
    """Create a known host

     Create a repository level known host.

    Args:
        workspace (str):
        repo_slug (str):
        json_body (PipelineKnownHost):

    Returns:
        Response[Union[Error, PipelineKnownHost]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    repo_slug: str,
    *,
    client: Client,
    json_body: PipelineKnownHost,
) -> Optional[Union[Error, PipelineKnownHost]]:
    """Create a known host

     Create a repository level known host.

    Args:
        workspace (str):
        repo_slug (str):
        json_body (PipelineKnownHost):

    Returns:
        Response[Union[Error, PipelineKnownHost]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: Client,
    json_body: PipelineKnownHost,
) -> Response[Union[Error, PipelineKnownHost]]:
    """Create a known host

     Create a repository level known host.

    Args:
        workspace (str):
        repo_slug (str):
        json_body (PipelineKnownHost):

    Returns:
        Response[Union[Error, PipelineKnownHost]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: Client,
    json_body: PipelineKnownHost,
) -> Optional[Union[Error, PipelineKnownHost]]:
    """Create a known host

     Create a repository level known host.

    Args:
        workspace (str):
        repo_slug (str):
        json_body (PipelineKnownHost):

    Returns:
        Response[Union[Error, PipelineKnownHost]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            json_body=json_body,
        )
    ).parsed
