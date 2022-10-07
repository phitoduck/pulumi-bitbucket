from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    encoded_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/snippets/{workspace}/{encoded_id}/{node_id}".format(
        client.base_url, workspace=workspace, encoded_id=encoded_id, node_id=node_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 405:
        response_405 = Error.from_dict(response.json())

        return response_405
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
    node_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """Delete a previous revision of a snippet

     Deletes the snippet.

    Note that this only works for versioned URLs that point to the latest
    commit of the snippet. Pointing to an older commit results in a 405
    status code.

    To delete a snippet, regardless of whether or not concurrent changes
    are being made to it, use `DELETE /snippets/{encoded_id}` instead.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
        node_id=node_id,
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
    node_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """Delete a previous revision of a snippet

     Deletes the snippet.

    Note that this only works for versioned URLs that point to the latest
    commit of the snippet. Pointing to an older commit results in a 405
    status code.

    To delete a snippet, regardless of whether or not concurrent changes
    are being made to it, use `DELETE /snippets/{encoded_id}` instead.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        workspace=workspace,
        encoded_id=encoded_id,
        node_id=node_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    encoded_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """Delete a previous revision of a snippet

     Deletes the snippet.

    Note that this only works for versioned URLs that point to the latest
    commit of the snippet. Pointing to an older commit results in a 405
    status code.

    To delete a snippet, regardless of whether or not concurrent changes
    are being made to it, use `DELETE /snippets/{encoded_id}` instead.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
        node_id=node_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    encoded_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """Delete a previous revision of a snippet

     Deletes the snippet.

    Note that this only works for versioned URLs that point to the latest
    commit of the snippet. Pointing to an older commit results in a 405
    status code.

    To delete a snippet, regardless of whether or not concurrent changes
    are being made to it, use `DELETE /snippets/{encoded_id}` instead.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            encoded_id=encoded_id,
            node_id=node_id,
            client=client,
        )
    ).parsed
