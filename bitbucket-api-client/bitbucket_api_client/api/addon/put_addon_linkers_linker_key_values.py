from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    linker_key: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/addon/linkers/{linker_key}/values".format(client.base_url, linker_key=linker_key)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
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
    linker_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """Update a linker value

     Bulk update [linker](/cloud/bitbucket/modules/linker/) values for the specified
    linker of the authenticated application.

    A linker value lets applications supply values to modify its regular expression.

    The base regular expression must use a Bitbucket-specific match group `(?K)`
    which will be translated to `([\w\-]+)`. A value must match this pattern.

    [Read more about linker values](/cloud/bitbucket/modules/linker/#usingthebitbucketapitosupplyvalues)

    Args:
        linker_key (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        linker_key=linker_key,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    linker_key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """Update a linker value

     Bulk update [linker](/cloud/bitbucket/modules/linker/) values for the specified
    linker of the authenticated application.

    A linker value lets applications supply values to modify its regular expression.

    The base regular expression must use a Bitbucket-specific match group `(?K)`
    which will be translated to `([\w\-]+)`. A value must match this pattern.

    [Read more about linker values](/cloud/bitbucket/modules/linker/#usingthebitbucketapitosupplyvalues)

    Args:
        linker_key (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        linker_key=linker_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    linker_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """Update a linker value

     Bulk update [linker](/cloud/bitbucket/modules/linker/) values for the specified
    linker of the authenticated application.

    A linker value lets applications supply values to modify its regular expression.

    The base regular expression must use a Bitbucket-specific match group `(?K)`
    which will be translated to `([\w\-]+)`. A value must match this pattern.

    [Read more about linker values](/cloud/bitbucket/modules/linker/#usingthebitbucketapitosupplyvalues)

    Args:
        linker_key (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        linker_key=linker_key,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    linker_key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """Update a linker value

     Bulk update [linker](/cloud/bitbucket/modules/linker/) values for the specified
    linker of the authenticated application.

    A linker value lets applications supply values to modify its regular expression.

    The base regular expression must use a Bitbucket-specific match group `(?K)`
    which will be translated to `([\w\-]+)`. A value must match this pattern.

    [Read more about linker values](/cloud/bitbucket/modules/linker/#usingthebitbucketapitosupplyvalues)

    Args:
        linker_key (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            linker_key=linker_key,
            client=client,
        )
    ).parsed
