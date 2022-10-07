from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.get_repositories_workspace_role import GetRepositoriesWorkspaceRole
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetRepositoriesWorkspaceRole] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}".format(client.base_url, workspace=workspace)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_role: Union[Unset, None, str] = UNSET
    if not isinstance(role, Unset):
        json_role = role.value if role else None

    params["role"] = json_role

    params["q"] = q

    params["sort"] = sort

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
    if response.status_code == 410:
        response_410 = Error.from_dict(response.json())

        return response_410
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
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetRepositoriesWorkspaceRole] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List repositories in a workspace

     Returns a paginated list of all repositories owned by the specified
    workspace.

    The result can be narrowed down based on the authenticated user's role.

    E.g. with `?role=contributor`, only those repositories that the
    authenticated user has write access to are returned (this includes any
    repo the user is an admin on, as that implies write access).

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        role (Union[Unset, None, GetRepositoriesWorkspaceRole]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
        role=role,
        q=q,
        sort=sort,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetRepositoriesWorkspaceRole] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List repositories in a workspace

     Returns a paginated list of all repositories owned by the specified
    workspace.

    The result can be narrowed down based on the authenticated user's role.

    E.g. with `?role=contributor`, only those repositories that the
    authenticated user has write access to are returned (this includes any
    repo the user is an admin on, as that implies write access).

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        role (Union[Unset, None, GetRepositoriesWorkspaceRole]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        role=role,
        q=q,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetRepositoriesWorkspaceRole] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List repositories in a workspace

     Returns a paginated list of all repositories owned by the specified
    workspace.

    The result can be narrowed down based on the authenticated user's role.

    E.g. with `?role=contributor`, only those repositories that the
    authenticated user has write access to are returned (this includes any
    repo the user is an admin on, as that implies write access).

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        role (Union[Unset, None, GetRepositoriesWorkspaceRole]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
        role=role,
        q=q,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetRepositoriesWorkspaceRole] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List repositories in a workspace

     Returns a paginated list of all repositories owned by the specified
    workspace.

    The result can be narrowed down based on the authenticated user's role.

    E.g. with `?role=contributor`, only those repositories that the
    authenticated user has write access to are returned (this includes any
    repo the user is an admin on, as that implies write access).

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        role (Union[Unset, None, GetRepositoriesWorkspaceRole]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            role=role,
            q=q,
            sort=sort,
        )
    ).parsed
