from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...types import Response


def _get_kwargs(
    email: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/user/emails/{email}".format(client.base_url, email=email)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get an email address for current user

     Returns details about a specific one of the authenticated user's
    email addresses.

    Details describe whether the address has been confirmed by the user and
    whether it is the user's primary address or not.

    Args:
        email (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        email=email,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    email: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get an email address for current user

     Returns details about a specific one of the authenticated user's
    email addresses.

    Details describe whether the address has been confirmed by the user and
    whether it is the user's primary address or not.

    Args:
        email (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        email=email,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
