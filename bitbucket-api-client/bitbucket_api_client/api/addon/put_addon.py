from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/addon".format(client.base_url)

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
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
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
    """Update an installed app

     Updates the application installation for the user.

    This endpoint is intended to be used by Bitbucket Connect apps
    and only supports JWT authentication -- that is how Bitbucket
    identifies the particular installation of the app. Developers
    with applications registered in the \"Develop Apps\" section
    of Bitbucket need not use this endpoint as updates for those
    applications can be sent out via the UI of that section.

    Passing an empty body will update the installation using the
    existing descriptor URL.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{}'
    ```

    The new `descriptor` for the installation can be also provided
    in the body directly.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor\": $NEW_DESCRIPTOR}'
    ```

    In both these modes the URL of the descriptor cannot be changed. To
    change the descriptor location and upgrade an installation
    the request must be made exclusively with a `descriptor_url`.

     ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor_url\": $NEW_URL}'
    ```

    The `descriptor_url` must exactly match the marketplace registration
    that Atlassian has for the application. Contact your Atlassian
    developer advocate to update this registration. Once the registration
    has been updated you may call this resource for each installation.

    Note that the scopes of the application cannot be increased
    in the new descriptor nor reduced to none.

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
    """Update an installed app

     Updates the application installation for the user.

    This endpoint is intended to be used by Bitbucket Connect apps
    and only supports JWT authentication -- that is how Bitbucket
    identifies the particular installation of the app. Developers
    with applications registered in the \"Develop Apps\" section
    of Bitbucket need not use this endpoint as updates for those
    applications can be sent out via the UI of that section.

    Passing an empty body will update the installation using the
    existing descriptor URL.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{}'
    ```

    The new `descriptor` for the installation can be also provided
    in the body directly.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor\": $NEW_DESCRIPTOR}'
    ```

    In both these modes the URL of the descriptor cannot be changed. To
    change the descriptor location and upgrade an installation
    the request must be made exclusively with a `descriptor_url`.

     ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor_url\": $NEW_URL}'
    ```

    The `descriptor_url` must exactly match the marketplace registration
    that Atlassian has for the application. Contact your Atlassian
    developer advocate to update this registration. Once the registration
    has been updated you may call this resource for each installation.

    Note that the scopes of the application cannot be increased
    in the new descriptor nor reduced to none.

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
    """Update an installed app

     Updates the application installation for the user.

    This endpoint is intended to be used by Bitbucket Connect apps
    and only supports JWT authentication -- that is how Bitbucket
    identifies the particular installation of the app. Developers
    with applications registered in the \"Develop Apps\" section
    of Bitbucket need not use this endpoint as updates for those
    applications can be sent out via the UI of that section.

    Passing an empty body will update the installation using the
    existing descriptor URL.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{}'
    ```

    The new `descriptor` for the installation can be also provided
    in the body directly.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor\": $NEW_DESCRIPTOR}'
    ```

    In both these modes the URL of the descriptor cannot be changed. To
    change the descriptor location and upgrade an installation
    the request must be made exclusively with a `descriptor_url`.

     ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor_url\": $NEW_URL}'
    ```

    The `descriptor_url` must exactly match the marketplace registration
    that Atlassian has for the application. Contact your Atlassian
    developer advocate to update this registration. Once the registration
    has been updated you may call this resource for each installation.

    Note that the scopes of the application cannot be increased
    in the new descriptor nor reduced to none.

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
    """Update an installed app

     Updates the application installation for the user.

    This endpoint is intended to be used by Bitbucket Connect apps
    and only supports JWT authentication -- that is how Bitbucket
    identifies the particular installation of the app. Developers
    with applications registered in the \"Develop Apps\" section
    of Bitbucket need not use this endpoint as updates for those
    applications can be sent out via the UI of that section.

    Passing an empty body will update the installation using the
    existing descriptor URL.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{}'
    ```

    The new `descriptor` for the installation can be also provided
    in the body directly.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor\": $NEW_DESCRIPTOR}'
    ```

    In both these modes the URL of the descriptor cannot be changed. To
    change the descriptor location and upgrade an installation
    the request must be made exclusively with a `descriptor_url`.

     ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor_url\": $NEW_URL}'
    ```

    The `descriptor_url` must exactly match the marketplace registration
    that Atlassian has for the application. Contact your Atlassian
    developer advocate to update this registration. Once the registration
    has been updated you may call this resource for each installation.

    Note that the scopes of the application cannot be increased
    in the new descriptor nor reduced to none.

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
