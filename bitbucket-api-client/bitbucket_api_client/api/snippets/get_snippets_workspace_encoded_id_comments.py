from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/snippets/{workspace}/{encoded_id}/comments".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Error]:
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
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
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """List comments on a snippet

     Used to retrieve a paginated list of all comments for a specific
    snippet.

    This resource works identical to commit and pull request comments.

    The default sorting is oldest to newest and can be overridden with
    the `sort` query parameter.

    Args:
        workspace (str):
        encoded_id (str):

    Returns:
        Response[Error]
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
) -> Optional[Error]:
    """List comments on a snippet

     Used to retrieve a paginated list of all comments for a specific
    snippet.

    This resource works identical to commit and pull request comments.

    The default sorting is oldest to newest and can be overridden with
    the `sort` query parameter.

    Args:
        workspace (str):
        encoded_id (str):

    Returns:
        Response[Error]
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
) -> Response[Error]:
    """List comments on a snippet

     Used to retrieve a paginated list of all comments for a specific
    snippet.

    This resource works identical to commit and pull request comments.

    The default sorting is oldest to newest and can be overridden with
    the `sort` query parameter.

    Args:
        workspace (str):
        encoded_id (str):

    Returns:
        Response[Error]
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
) -> Optional[Error]:
    """List comments on a snippet

     Used to retrieve a paginated list of all comments for a specific
    snippet.

    This resource works identical to commit and pull request comments.

    The default sorting is oldest to newest and can be overridden with
    the `sort` query parameter.

    Args:
        workspace (str):
        encoded_id (str):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            encoded_id=encoded_id,
            client=client,
        )
    ).parsed
