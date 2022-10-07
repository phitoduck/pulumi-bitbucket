from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/issues/{issue_id}/watch".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, issue_id=issue_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Error]:
    if response.status_code == 204:
        response_204 = Error.from_dict(response.json())

        return response_204
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Error]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Watch an issue

     Start watching this issue.

    To start watching this issue, do an empty PUT. The 204 status code
    indicates that the operation was successful.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Watch an issue

     Start watching this issue.

    To start watching this issue, do an empty PUT. The 204 status code
    indicates that the operation was successful.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Watch an issue

     Start watching this issue.

    To start watching this issue, do an empty PUT. The 204 status code
    indicates that the operation was successful.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Watch an issue

     Start watching this issue.

    To start watching this issue, do an empty PUT. The 204 status code
    indicates that the operation was successful.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            issue_id=issue_id,
            client=client,
        )
    ).parsed
