from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/pipelines/".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: Client,
) -> Response[Any]:
    """List pipelines

     Find pipelines

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: Client,
) -> Response[Any]:
    """List pipelines

     Find pipelines

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
