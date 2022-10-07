from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.get_repositories_workspace_repo_slug_src_format import GetRepositoriesWorkspaceRepoSlugSrcFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, GetRepositoriesWorkspaceRepoSlugSrcFormat] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/src".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Error]:
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
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, GetRepositoriesWorkspaceRepoSlugSrcFormat] = UNSET,
) -> Response[Error]:
    """Get the root directory of the main branch

     This endpoint redirects the client to the directory listing of the
    root directory on the main branch.

    This is equivalent to directly hitting
    [/2.0/repositories/{username}/{repo_slug}/src/{commit}/{path}](src/%7Bcommit%7D/%7Bpath%7D)
    without having to know the name or SHA1 of the repo's main branch.

    To create new commits, [POST to this endpoint](#post)

    Args:
        workspace (str):
        repo_slug (str):
        format_ (Union[Unset, None, GetRepositoriesWorkspaceRepoSlugSrcFormat]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        format_=format_,
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
    client: AuthenticatedClient,
    format_: Union[Unset, None, GetRepositoriesWorkspaceRepoSlugSrcFormat] = UNSET,
) -> Optional[Error]:
    """Get the root directory of the main branch

     This endpoint redirects the client to the directory listing of the
    root directory on the main branch.

    This is equivalent to directly hitting
    [/2.0/repositories/{username}/{repo_slug}/src/{commit}/{path}](src/%7Bcommit%7D/%7Bpath%7D)
    without having to know the name or SHA1 of the repo's main branch.

    To create new commits, [POST to this endpoint](#post)

    Args:
        workspace (str):
        repo_slug (str):
        format_ (Union[Unset, None, GetRepositoriesWorkspaceRepoSlugSrcFormat]):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, GetRepositoriesWorkspaceRepoSlugSrcFormat] = UNSET,
) -> Response[Error]:
    """Get the root directory of the main branch

     This endpoint redirects the client to the directory listing of the
    root directory on the main branch.

    This is equivalent to directly hitting
    [/2.0/repositories/{username}/{repo_slug}/src/{commit}/{path}](src/%7Bcommit%7D/%7Bpath%7D)
    without having to know the name or SHA1 of the repo's main branch.

    To create new commits, [POST to this endpoint](#post)

    Args:
        workspace (str):
        repo_slug (str):
        format_ (Union[Unset, None, GetRepositoriesWorkspaceRepoSlugSrcFormat]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        format_=format_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, None, GetRepositoriesWorkspaceRepoSlugSrcFormat] = UNSET,
) -> Optional[Error]:
    """Get the root directory of the main branch

     This endpoint redirects the client to the directory listing of the
    root directory on the main branch.

    This is equivalent to directly hitting
    [/2.0/repositories/{username}/{repo_slug}/src/{commit}/{path}](src/%7Bcommit%7D/%7Bpath%7D)
    without having to know the name or SHA1 of the repo's main branch.

    To create new commits, [POST to this endpoint](#post)

    Args:
        workspace (str):
        repo_slug (str):
        format_ (Union[Unset, None, GetRepositoriesWorkspaceRepoSlugSrcFormat]):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            format_=format_,
        )
    ).parsed
