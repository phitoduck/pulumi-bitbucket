from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.paginated_accounts import PaginatedAccounts
from ...types import Response


def _get_kwargs(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/snippets/{workspace}/{encoded_id}/watchers".format(
        client.base_url, workspace=workspace, encoded_id=encoded_id
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, PaginatedAccounts]]:
    if response.status_code == 200:
        response_200 = PaginatedAccounts.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, PaginatedAccounts]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, PaginatedAccounts]]:
    """List users watching a snippet

     Returns a paginated list of all users watching a specific snippet.

    Args:
        workspace (str):
        encoded_id (str):

    Returns:
        Response[Union[Error, PaginatedAccounts]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, PaginatedAccounts]]:
    """List users watching a snippet

     Returns a paginated list of all users watching a specific snippet.

    Args:
        workspace (str):
        encoded_id (str):

    Returns:
        Response[Union[Error, PaginatedAccounts]]
    """

    return sync_detailed(
        workspace=workspace,
        encoded_id=encoded_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, PaginatedAccounts]]:
    """List users watching a snippet

     Returns a paginated list of all users watching a specific snippet.

    Args:
        workspace (str):
        encoded_id (str):

    Returns:
        Response[Union[Error, PaginatedAccounts]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, PaginatedAccounts]]:
    """List users watching a snippet

     Returns a paginated list of all users watching a specific snippet.

    Args:
        workspace (str):
        encoded_id (str):

    Returns:
        Response[Union[Error, PaginatedAccounts]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            encoded_id=encoded_id,
            client=client,
        )
    ).parsed
