from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.get_repositories_workspace_repo_slug_pullrequests_state import (
    GetRepositoriesWorkspaceRepoSlugPullrequestsState,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, None, GetRepositoriesWorkspaceRepoSlugPullrequestsState] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/pullrequests".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
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
    *,
    client: AuthenticatedClient,
    state: Union[Unset, None, GetRepositoriesWorkspaceRepoSlugPullrequestsState] = UNSET,
) -> Response[Union[Any, Error]]:
    """List pull requests

     Returns all pull requests on the specified repository.

    By default only open pull requests are returned. This can be controlled
    using the `state` query parameter. To retrieve pull requests that are
    in one of multiple states, repeat the `state` parameter for each
    individual state.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        repo_slug (str):
        state (Union[Unset, None, GetRepositoriesWorkspaceRepoSlugPullrequestsState]):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        state=state,
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
    state: Union[Unset, None, GetRepositoriesWorkspaceRepoSlugPullrequestsState] = UNSET,
) -> Optional[Union[Any, Error]]:
    """List pull requests

     Returns all pull requests on the specified repository.

    By default only open pull requests are returned. This can be controlled
    using the `state` query parameter. To retrieve pull requests that are
    in one of multiple states, repeat the `state` parameter for each
    individual state.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        repo_slug (str):
        state (Union[Unset, None, GetRepositoriesWorkspaceRepoSlugPullrequestsState]):

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        state=state,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, None, GetRepositoriesWorkspaceRepoSlugPullrequestsState] = UNSET,
) -> Response[Union[Any, Error]]:
    """List pull requests

     Returns all pull requests on the specified repository.

    By default only open pull requests are returned. This can be controlled
    using the `state` query parameter. To retrieve pull requests that are
    in one of multiple states, repeat the `state` parameter for each
    individual state.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        repo_slug (str):
        state (Union[Unset, None, GetRepositoriesWorkspaceRepoSlugPullrequestsState]):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        state=state,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, None, GetRepositoriesWorkspaceRepoSlugPullrequestsState] = UNSET,
) -> Optional[Union[Any, Error]]:
    """List pull requests

     Returns all pull requests on the specified repository.

    By default only open pull requests are returned. This can be controlled
    using the `state` query parameter. To retrieve pull requests that are
    in one of multiple states, repeat the `state` parameter for each
    individual state.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        repo_slug (str):
        state (Union[Unset, None, GetRepositoriesWorkspaceRepoSlugPullrequestsState]):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            state=state,
        )
    ).parsed
