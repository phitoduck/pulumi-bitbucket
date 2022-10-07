from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, issue_id=issue_id, comment_id=comment_id
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
    issue_id: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get a comment on an issue

     Returns the specified issue comment object.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        comment_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        comment_id=comment_id,
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
    issue_id: str,
    comment_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get a comment on an issue

     Returns the specified issue comment object.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        comment_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        comment_id=comment_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
