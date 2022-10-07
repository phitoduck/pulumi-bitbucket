from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/addon/linkers".format(client.base_url)

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
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """List linkers for an app

     Gets a list of all [linkers](/cloud/bitbucket/modules/linker/)
    for the authenticated application.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """List linkers for an app

     Gets a list of all [linkers](/cloud/bitbucket/modules/linker/)
    for the authenticated application.

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """List linkers for an app

     Gets a list of all [linkers](/cloud/bitbucket/modules/linker/)
    for the authenticated application.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """List linkers for an app

     Gets a list of all [linkers](/cloud/bitbucket/modules/linker/)
    for the authenticated application.

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
