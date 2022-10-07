from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.snippet import Snippet
from ...types import Response


def _get_kwargs(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/snippets/{workspace}".format(client.base_url, workspace=workspace)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, Snippet]]:
    if response.status_code == 201:
        response_201 = Snippet.from_dict(response.json())

        return response_201
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
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
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, Snippet]]:
    """Create a snippet for a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-post), except that
    the new snippet will be
    created under the workspace specified in the path parameter
    `{workspace}`.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, Snippet]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
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
) -> Optional[Union[Error, Snippet]]:
    """Create a snippet for a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-post), except that
    the new snippet will be
    created under the workspace specified in the path parameter
    `{workspace}`.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, Snippet]]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, Snippet]]:
    """Create a snippet for a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-post), except that
    the new snippet will be
    created under the workspace specified in the path parameter
    `{workspace}`.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, Snippet]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, Snippet]]:
    """Create a snippet for a workspace

     Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-post), except that
    the new snippet will be
    created under the workspace specified in the path parameter
    `{workspace}`.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, Snippet]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
        )
    ).parsed
