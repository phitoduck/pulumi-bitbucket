from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.get_snippets_workspace_role import GetSnippetsWorkspaceRole
from ...models.paginated_snippets import PaginatedSnippets
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetSnippetsWorkspaceRole] = UNSET,
) -> Dict[str, Any]:
    url = "{}/snippets/{workspace}".format(client.base_url, workspace=workspace)

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
    workspace: str,
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetSnippetsWorkspaceRole] = UNSET,
) -> Response[Union[Error, PaginatedSnippets]]:
    """List snippets in a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-get), except that
    the result is further filtered
    by the snippet owner and only those that are owned by `{workspace}` are
    returned.

    Args:
        workspace (str):
        role (Union[Unset, None, GetSnippetsWorkspaceRole]):

    Returns:
        Response[Union[Error, PaginatedSnippets]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
        role=role,
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
    role: Union[Unset, None, GetSnippetsWorkspaceRole] = UNSET,
) -> Optional[Union[Error, PaginatedSnippets]]:
    """List snippets in a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-get), except that
    the result is further filtered
    by the snippet owner and only those that are owned by `{workspace}` are
    returned.

    Args:
        workspace (str):
        role (Union[Unset, None, GetSnippetsWorkspaceRole]):

    Returns:
        Response[Union[Error, PaginatedSnippets]]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        role=role,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetSnippetsWorkspaceRole] = UNSET,
) -> Response[Union[Error, PaginatedSnippets]]:
    """List snippets in a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-get), except that
    the result is further filtered
    by the snippet owner and only those that are owned by `{workspace}` are
    returned.

    Args:
        workspace (str):
        role (Union[Unset, None, GetSnippetsWorkspaceRole]):

    Returns:
        Response[Union[Error, PaginatedSnippets]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
        role=role,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetSnippetsWorkspaceRole] = UNSET,
) -> Optional[Union[Error, PaginatedSnippets]]:
    """List snippets in a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-get), except that
    the result is further filtered
    by the snippet owner and only those that are owned by `{workspace}` are
    returned.

    Args:
        workspace (str):
        role (Union[Unset, None, GetSnippetsWorkspaceRole]):

    Returns:
        Response[Union[Error, PaginatedSnippets]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            role=role,
        )
    ).parsed
