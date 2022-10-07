from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.snippet import Snippet
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
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, Snippet]]:
    if response.status_code == 200:
        response_200 = Snippet.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, Snippet]]:
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
) -> Response[Union[Error, Snippet]]:
    """Get a previous revision of a snippet

     Identical to `GET /snippets/encoded_id`, except that this endpoint
    can be used to retrieve the contents of the snippet as it was at an
    older revision, while `/snippets/encoded_id` always returns the
    snippet's current revision.

    Note that only the snippet's file contents are versioned, not its
    meta data properties like the title.

    Other than that, the two endpoints are identical in behavior.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Returns:
        Response[Union[Error, Snippet]]
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
) -> Optional[Union[Error, Snippet]]:
    """Get a previous revision of a snippet

     Identical to `GET /snippets/encoded_id`, except that this endpoint
    can be used to retrieve the contents of the snippet as it was at an
    older revision, while `/snippets/encoded_id` always returns the
    snippet's current revision.

    Note that only the snippet's file contents are versioned, not its
    meta data properties like the title.

    Other than that, the two endpoints are identical in behavior.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Returns:
        Response[Union[Error, Snippet]]
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
) -> Response[Union[Error, Snippet]]:
    """Get a previous revision of a snippet

     Identical to `GET /snippets/encoded_id`, except that this endpoint
    can be used to retrieve the contents of the snippet as it was at an
    older revision, while `/snippets/encoded_id` always returns the
    snippet's current revision.

    Note that only the snippet's file contents are versioned, not its
    meta data properties like the title.

    Other than that, the two endpoints are identical in behavior.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Returns:
        Response[Union[Error, Snippet]]
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
) -> Optional[Union[Error, Snippet]]:
    """Get a previous revision of a snippet

     Identical to `GET /snippets/encoded_id`, except that this endpoint
    can be used to retrieve the contents of the snippet as it was at an
    older revision, while `/snippets/encoded_id` always returns the
    snippet's current revision.

    Note that only the snippet's file contents are versioned, not its
    meta data properties like the title.

    Other than that, the two endpoints are identical in behavior.

    Args:
        workspace (str):
        encoded_id (str):
        node_id (str):

    Returns:
        Response[Union[Error, Snippet]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            encoded_id=encoded_id,
            node_id=node_id,
            client=client,
        )
    ).parsed
