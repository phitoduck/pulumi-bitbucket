from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.account import Account
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/users/{selected_user}".format(client.base_url, selected_user=selected_user)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Account, Error]]:
    if response.status_code == 200:
        response_200 = Account.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Account, Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Account, Error]]:
    """Get a user

     Gets the public information associated with a user account.

    If the user's profile is private, `location`, `website` and
    `created_on` elements are omitted.

    Note that the user object returned by this operation is changing significantly, due to privacy
    changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-bitbucket-user-objects) for details.

    Args:
        selected_user (str):

    Returns:
        Response[Union[Account, Error]]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Account, Error]]:
    """Get a user

     Gets the public information associated with a user account.

    If the user's profile is private, `location`, `website` and
    `created_on` elements are omitted.

    Note that the user object returned by this operation is changing significantly, due to privacy
    changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-bitbucket-user-objects) for details.

    Args:
        selected_user (str):

    Returns:
        Response[Union[Account, Error]]
    """

    return sync_detailed(
        selected_user=selected_user,
        client=client,
    ).parsed


async def asyncio_detailed(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Account, Error]]:
    """Get a user

     Gets the public information associated with a user account.

    If the user's profile is private, `location`, `website` and
    `created_on` elements are omitted.

    Note that the user object returned by this operation is changing significantly, due to privacy
    changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-bitbucket-user-objects) for details.

    Args:
        selected_user (str):

    Returns:
        Response[Union[Account, Error]]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Account, Error]]:
    """Get a user

     Gets the public information associated with a user account.

    If the user's profile is private, `location`, `website` and
    `created_on` elements are omitted.

    Note that the user object returned by this operation is changing significantly, due to privacy
    changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-bitbucket-user-objects) for details.

    Args:
        selected_user (str):

    Returns:
        Response[Union[Account, Error]]
    """

    return (
        await asyncio_detailed(
            selected_user=selected_user,
            client=client,
        )
    ).parsed
