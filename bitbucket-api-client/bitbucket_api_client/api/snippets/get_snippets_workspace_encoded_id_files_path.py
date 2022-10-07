from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    encoded_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/snippets/{workspace}/{encoded_id}/files/{path}".format(
        client.base_url, workspace=workspace, encoded_id=encoded_id, path=path
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
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
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
    encoded_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """Get a snippet's raw file at HEAD

     Convenience resource for getting to a snippet's raw files without the
    need for first having to retrieve the snippet itself and having to pull
    out the versioned file links.

    Args:
        workspace (str):
        encoded_id (str):
        path (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
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
    encoded_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """Get a snippet's raw file at HEAD

     Convenience resource for getting to a snippet's raw files without the
    need for first having to retrieve the snippet itself and having to pull
    out the versioned file links.

    Args:
        workspace (str):
        encoded_id (str):
        path (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        workspace=workspace,
        encoded_id=encoded_id,
        path=path,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    encoded_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """Get a snippet's raw file at HEAD

     Convenience resource for getting to a snippet's raw files without the
    need for first having to retrieve the snippet itself and having to pull
    out the versioned file links.

    Args:
        workspace (str):
        encoded_id (str):
        path (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
        path=path,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    encoded_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """Get a snippet's raw file at HEAD

     Convenience resource for getting to a snippet's raw files without the
    need for first having to retrieve the snippet itself and having to pull
    out the versioned file links.

    Args:
        workspace (str):
        encoded_id (str):
        path (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            encoded_id=encoded_id,
            path=path,
            client=client,
        )
    ).parsed
