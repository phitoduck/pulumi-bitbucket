from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/user/permissions/workspaces".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Error]:
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Error]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List workspaces for the current user

     Returns an object for each workspace the caller is a member of, and
    their effective role - the highest level of privilege the caller has.
    If a user is a member of multiple groups with distinct roles, only the
    highest level is returned.

    Permissions can be:

    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/user/permissions/workspaces

    {
      \"pagelen\": 10,
      \"page\": 1,
      \"size\": 1,
      \"values\": [
        {
          \"type\": \"workspace_membership\",
          \"permission\": \"owner\",
          \"last_accessed\": \"2019-03-07T12:35:02.900024+00:00\",
          \"added_on\": \"2018-10-11T17:42:02.961424+00:00\",
          \"user\": {
            \"type\": \"user\",
            \"uuid\": \"{470c176d-3574-44ea-bb41-89e8638bcca4}\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
          },
          \"workspace\": {
            \"type\": \"workspace\",
            \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
            \"slug\": \"bbworkspace1\",
            \"name\": \"Atlassian Bitbucket\",
          }
        }
      ]
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=workspace.slug=\"bbworkspace1\"` or `q=permission=\"owner\"`
    * `sort=workspace.slug`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
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


def sync(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List workspaces for the current user

     Returns an object for each workspace the caller is a member of, and
    their effective role - the highest level of privilege the caller has.
    If a user is a member of multiple groups with distinct roles, only the
    highest level is returned.

    Permissions can be:

    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/user/permissions/workspaces

    {
      \"pagelen\": 10,
      \"page\": 1,
      \"size\": 1,
      \"values\": [
        {
          \"type\": \"workspace_membership\",
          \"permission\": \"owner\",
          \"last_accessed\": \"2019-03-07T12:35:02.900024+00:00\",
          \"added_on\": \"2018-10-11T17:42:02.961424+00:00\",
          \"user\": {
            \"type\": \"user\",
            \"uuid\": \"{470c176d-3574-44ea-bb41-89e8638bcca4}\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
          },
          \"workspace\": {
            \"type\": \"workspace\",
            \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
            \"slug\": \"bbworkspace1\",
            \"name\": \"Atlassian Bitbucket\",
          }
        }
      ]
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=workspace.slug=\"bbworkspace1\"` or `q=permission=\"owner\"`
    * `sort=workspace.slug`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        client=client,
        q=q,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List workspaces for the current user

     Returns an object for each workspace the caller is a member of, and
    their effective role - the highest level of privilege the caller has.
    If a user is a member of multiple groups with distinct roles, only the
    highest level is returned.

    Permissions can be:

    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/user/permissions/workspaces

    {
      \"pagelen\": 10,
      \"page\": 1,
      \"size\": 1,
      \"values\": [
        {
          \"type\": \"workspace_membership\",
          \"permission\": \"owner\",
          \"last_accessed\": \"2019-03-07T12:35:02.900024+00:00\",
          \"added_on\": \"2018-10-11T17:42:02.961424+00:00\",
          \"user\": {
            \"type\": \"user\",
            \"uuid\": \"{470c176d-3574-44ea-bb41-89e8638bcca4}\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
          },
          \"workspace\": {
            \"type\": \"workspace\",
            \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
            \"slug\": \"bbworkspace1\",
            \"name\": \"Atlassian Bitbucket\",
          }
        }
      ]
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=workspace.slug=\"bbworkspace1\"` or `q=permission=\"owner\"`
    * `sort=workspace.slug`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        client=client,
        q=q,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List workspaces for the current user

     Returns an object for each workspace the caller is a member of, and
    their effective role - the highest level of privilege the caller has.
    If a user is a member of multiple groups with distinct roles, only the
    highest level is returned.

    Permissions can be:

    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/user/permissions/workspaces

    {
      \"pagelen\": 10,
      \"page\": 1,
      \"size\": 1,
      \"values\": [
        {
          \"type\": \"workspace_membership\",
          \"permission\": \"owner\",
          \"last_accessed\": \"2019-03-07T12:35:02.900024+00:00\",
          \"added_on\": \"2018-10-11T17:42:02.961424+00:00\",
          \"user\": {
            \"type\": \"user\",
            \"uuid\": \"{470c176d-3574-44ea-bb41-89e8638bcca4}\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
          },
          \"workspace\": {
            \"type\": \"workspace\",
            \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
            \"slug\": \"bbworkspace1\",
            \"name\": \"Atlassian Bitbucket\",
          }
        }
      ]
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=workspace.slug=\"bbworkspace1\"` or `q=permission=\"owner\"`
    * `sort=workspace.slug`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            sort=sort,
        )
    ).parsed
