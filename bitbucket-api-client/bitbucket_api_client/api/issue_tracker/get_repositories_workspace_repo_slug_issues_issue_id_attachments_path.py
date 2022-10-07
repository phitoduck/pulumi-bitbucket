from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments/{path}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, issue_id=issue_id, path=path
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Error]]:
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
    path: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """Get attachment for an issue

     Returns the contents of the specified file attachment.

    Note that this endpoint does not return a JSON response, but instead
    returns a redirect pointing to the actual file that in turn will return
    the raw contents.

    The redirect URL contains a one-time token that has a limited lifetime.
    As a result, the link should not be persisted, stored, or shared.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        path (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        path=path,
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
    path: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """Get attachment for an issue

     Returns the contents of the specified file attachment.

    Note that this endpoint does not return a JSON response, but instead
    returns a redirect pointing to the actual file that in turn will return
    the raw contents.

    The redirect URL contains a one-time token that has a limited lifetime.
    As a result, the link should not be persisted, stored, or shared.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        path (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        path=path,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """Get attachment for an issue

     Returns the contents of the specified file attachment.

    Note that this endpoint does not return a JSON response, but instead
    returns a redirect pointing to the actual file that in turn will return
    the raw contents.

    The redirect URL contains a one-time token that has a limited lifetime.
    As a result, the link should not be persisted, stored, or shared.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        path (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        path=path,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """Get attachment for an issue

     Returns the contents of the specified file attachment.

    Note that this endpoint does not return a JSON response, but instead
    returns a redirect pointing to the actual file that in turn will return
    the raw contents.

    The redirect URL contains a one-time token that has a limited lifetime.
    As a result, the link should not be persisted, stored, or shared.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        path (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            issue_id=issue_id,
            path=path,
            client=client,
        )
    ).parsed
