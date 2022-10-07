from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    app_key: str,
    property_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, app_key=app_key, property_name=property_name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
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
    app_key: str,
    property_name: str,
    *,
    client: Client,
) -> Response[Any]:
    """Delete a repository application property

     Delete an [application property](/cloud/bitbucket/application-properties/) value stored against a
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        app_key (str):
        property_name (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        app_key=app_key,
        property_name=property_name,
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
    app_key: str,
    property_name: str,
    *,
    client: Client,
) -> Response[Any]:
    """Delete a repository application property

     Delete an [application property](/cloud/bitbucket/application-properties/) value stored against a
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        app_key (str):
        property_name (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        app_key=app_key,
        property_name=property_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
