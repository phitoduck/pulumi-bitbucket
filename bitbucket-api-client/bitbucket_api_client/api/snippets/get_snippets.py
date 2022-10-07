from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.get_snippets_role import GetSnippetsRole
from ...models.paginated_snippets import PaginatedSnippets
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetSnippetsRole] = UNSET,
) -> Dict[str, Any]:
    url = "{}/snippets".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_role: Union[Unset, None, str] = UNSET
    if not isinstance(role, Unset):
        json_role = role.value if role else None

    params["role"] = json_role

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, PaginatedSnippets]]:
    if response.status_code == 200:
        response_200 = PaginatedSnippets.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, PaginatedSnippets]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetSnippetsRole] = UNSET,
) -> Response[Union[Error, PaginatedSnippets]]:
    """List snippets

     Returns all snippets. Like pull requests, repositories and workspaces, the
    full set of snippets is defined by what the current user has access to.

    This includes all snippets owned by any of the workspaces the user is a member of,
    or snippets by other users that the current user is either watching or has collaborated
    on (for instance by commenting on it).

    To limit the set of returned snippets, apply the
    `?role=[owner|contributor|member]` query parameter where the roles are
    defined as follows:

    * `owner`: all snippets owned by the current user
    * `contributor`: all snippets owned by, or watched by the current user
    * `member`: created in a workspaces or watched by the current user

    When no role is specified, all public snippets are returned, as well as all
    privately owned snippets watched or commented on.

    The returned response is a normal paginated JSON list. This endpoint
    only supports `application/json` responses and no
    `multipart/form-data` or `multipart/related`. As a result, it is not
    possible to include the file contents.

    Args:
        role (Union[Unset, None, GetSnippetsRole]):

    Returns:
        Response[Union[Error, PaginatedSnippets]]
    """

    kwargs = _get_kwargs(
        client=client,
        role=role,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetSnippetsRole] = UNSET,
) -> Optional[Union[Error, PaginatedSnippets]]:
    """List snippets

     Returns all snippets. Like pull requests, repositories and workspaces, the
    full set of snippets is defined by what the current user has access to.

    This includes all snippets owned by any of the workspaces the user is a member of,
    or snippets by other users that the current user is either watching or has collaborated
    on (for instance by commenting on it).

    To limit the set of returned snippets, apply the
    `?role=[owner|contributor|member]` query parameter where the roles are
    defined as follows:

    * `owner`: all snippets owned by the current user
    * `contributor`: all snippets owned by, or watched by the current user
    * `member`: created in a workspaces or watched by the current user

    When no role is specified, all public snippets are returned, as well as all
    privately owned snippets watched or commented on.

    The returned response is a normal paginated JSON list. This endpoint
    only supports `application/json` responses and no
    `multipart/form-data` or `multipart/related`. As a result, it is not
    possible to include the file contents.

    Args:
        role (Union[Unset, None, GetSnippetsRole]):

    Returns:
        Response[Union[Error, PaginatedSnippets]]
    """

    return sync_detailed(
        client=client,
        role=role,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetSnippetsRole] = UNSET,
) -> Response[Union[Error, PaginatedSnippets]]:
    """List snippets

     Returns all snippets. Like pull requests, repositories and workspaces, the
    full set of snippets is defined by what the current user has access to.

    This includes all snippets owned by any of the workspaces the user is a member of,
    or snippets by other users that the current user is either watching or has collaborated
    on (for instance by commenting on it).

    To limit the set of returned snippets, apply the
    `?role=[owner|contributor|member]` query parameter where the roles are
    defined as follows:

    * `owner`: all snippets owned by the current user
    * `contributor`: all snippets owned by, or watched by the current user
    * `member`: created in a workspaces or watched by the current user

    When no role is specified, all public snippets are returned, as well as all
    privately owned snippets watched or commented on.

    The returned response is a normal paginated JSON list. This endpoint
    only supports `application/json` responses and no
    `multipart/form-data` or `multipart/related`. As a result, it is not
    possible to include the file contents.

    Args:
        role (Union[Unset, None, GetSnippetsRole]):

    Returns:
        Response[Union[Error, PaginatedSnippets]]
    """

    kwargs = _get_kwargs(
        client=client,
        role=role,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetSnippetsRole] = UNSET,
) -> Optional[Union[Error, PaginatedSnippets]]:
    """List snippets

     Returns all snippets. Like pull requests, repositories and workspaces, the
    full set of snippets is defined by what the current user has access to.

    This includes all snippets owned by any of the workspaces the user is a member of,
    or snippets by other users that the current user is either watching or has collaborated
    on (for instance by commenting on it).

    To limit the set of returned snippets, apply the
    `?role=[owner|contributor|member]` query parameter where the roles are
    defined as follows:

    * `owner`: all snippets owned by the current user
    * `contributor`: all snippets owned by, or watched by the current user
    * `member`: created in a workspaces or watched by the current user

    When no role is specified, all public snippets are returned, as well as all
    privately owned snippets watched or commented on.

    The returned response is a normal paginated JSON list. This endpoint
    only supports `application/json` responses and no
    `multipart/form-data` or `multipart/related`. As a result, it is not
    possible to include the file contents.

    Args:
        role (Union[Unset, None, GetSnippetsRole]):

    Returns:
        Response[Union[Error, PaginatedSnippets]]
    """

    return (
        await asyncio_detailed(
            client=client,
            role=role,
        )
    ).parsed
