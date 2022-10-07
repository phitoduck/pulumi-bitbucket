from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.account import Account
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    target_username: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, target_username=target_username
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Account, Error]]:
    if response.status_code == 200:
        response_200 = Account.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Account, Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    target_username: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Account, Error]]:
    """Get a default reviewer

     Returns the specified reviewer.

    This can be used to test whether a user is among the repository's
    default reviewers list. A 404 indicates that that specified user is not
    a default reviewer.

    Args:
        workspace (str):
        repo_slug (str):
        target_username (str):

    Returns:
        Response[Union[Account, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        target_username=target_username,
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
    target_username: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Account, Error]]:
    """Get a default reviewer

     Returns the specified reviewer.

    This can be used to test whether a user is among the repository's
    default reviewers list. A 404 indicates that that specified user is not
    a default reviewer.

    Args:
        workspace (str):
        repo_slug (str):
        target_username (str):

    Returns:
        Response[Union[Account, Error]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        target_username=target_username,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    target_username: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Account, Error]]:
    """Get a default reviewer

     Returns the specified reviewer.

    This can be used to test whether a user is among the repository's
    default reviewers list. A 404 indicates that that specified user is not
    a default reviewer.

    Args:
        workspace (str):
        repo_slug (str):
        target_username (str):

    Returns:
        Response[Union[Account, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        target_username=target_username,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    target_username: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Account, Error]]:
    """Get a default reviewer

     Returns the specified reviewer.

    This can be used to test whether a user is among the repository's
    default reviewers list. A 404 indicates that that specified user is not
    a default reviewer.

    Args:
        workspace (str):
        repo_slug (str):
        target_username (str):

    Returns:
        Response[Union[Account, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            target_username=target_username,
            client=client,
        )
    ).parsed
