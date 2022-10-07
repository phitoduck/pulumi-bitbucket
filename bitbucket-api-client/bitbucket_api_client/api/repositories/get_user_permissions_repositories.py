from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/user/permissions/repositories".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["q"] = q

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """List repository permissions for a user

     Returns an object for each repository the caller has explicit access
    to and their effective permission — the highest level of permission the
    caller has. This does not return public repositories that the user was
    not granted any specific permission in, and does not distinguish between
    explicit and implicit privileges.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/user/permissions/repositories

    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"geordi\",
            \"full_name\": \"bitbucket/geordi\",
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
          },
          \"permission\": \"admin\"
        }
      ],
      \"page\": 1,
      \"size\": 1
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    repository or permission by adding the following query string
    parameters:

    * `q=repository.name=\"geordi\"` or `q=permission>\"read\"`
    * `sort=repository.name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        q=q,
        sort=sort,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """List repository permissions for a user

     Returns an object for each repository the caller has explicit access
    to and their effective permission — the highest level of permission the
    caller has. This does not return public repositories that the user was
    not granted any specific permission in, and does not distinguish between
    explicit and implicit privileges.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/user/permissions/repositories

    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"geordi\",
            \"full_name\": \"bitbucket/geordi\",
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
          },
          \"permission\": \"admin\"
        }
      ],
      \"page\": 1,
      \"size\": 1
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    repository or permission by adding the following query string
    parameters:

    * `q=repository.name=\"geordi\"` or `q=permission>\"read\"`
    * `sort=repository.name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        q=q,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
