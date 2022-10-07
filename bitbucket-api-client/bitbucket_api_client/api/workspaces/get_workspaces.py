from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.get_workspaces_role import GetWorkspacesRole
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetWorkspacesRole] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workspaces".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_role: Union[Unset, None, str] = UNSET
    if not isinstance(role, Unset):
        json_role = role.value if role else None

    params["role"] = json_role

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
    role: Union[Unset, None, GetWorkspacesRole] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List workspaces for user

     Returns a list of workspaces accessible by the authenticated user.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/workspaces

    {
      \"pagelen\": 10,
      \"page\": 1,
      \"size\": 1,
      \"values\": [
        {
            \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
            \"links\": {
                \"owners\": {
                    \"href\":
    \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1/members?q=permission%3D%22owner%22\"
                },
                \"self\": {
                    \"href\": \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1\"
                },
                \"repositories\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/bbworkspace1\"
                },
                \"snippets\": {
                    \"href\": \"https://api.bitbucket.org/2.0/snippets/bbworkspace1\"
                },
                \"html\": {
                    \"href\": \"https://bitbucket.org/bbworkspace1/\"
                },
                \"avatar\": {
                    \"href\": \"https://bitbucket.org/workspaces/bbworkspace1/avatar/?ts=1543465801\"
                },
                \"members\": {
                    \"href\": \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1/members\"
                },
                \"projects\": {
                    \"href\": \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1/projects\"
                }
            },
            \"created_on\": \"2018-11-14T19:15:05.058566+00:00\",
            \"type\": \"workspace\",
            \"slug\": \"bbworkspace1\",
            \"is_private\": true,
            \"name\": \"Atlassian Bitbucket\"
        }
      ]
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=slug=\"bbworkspace1\"` or `q=is_private=true`
    * `sort=created_on`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Args:
        role (Union[Unset, None, GetWorkspacesRole]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        client=client,
        role=role,
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
    role: Union[Unset, None, GetWorkspacesRole] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List workspaces for user

     Returns a list of workspaces accessible by the authenticated user.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/workspaces

    {
      \"pagelen\": 10,
      \"page\": 1,
      \"size\": 1,
      \"values\": [
        {
            \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
            \"links\": {
                \"owners\": {
                    \"href\":
    \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1/members?q=permission%3D%22owner%22\"
                },
                \"self\": {
                    \"href\": \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1\"
                },
                \"repositories\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/bbworkspace1\"
                },
                \"snippets\": {
                    \"href\": \"https://api.bitbucket.org/2.0/snippets/bbworkspace1\"
                },
                \"html\": {
                    \"href\": \"https://bitbucket.org/bbworkspace1/\"
                },
                \"avatar\": {
                    \"href\": \"https://bitbucket.org/workspaces/bbworkspace1/avatar/?ts=1543465801\"
                },
                \"members\": {
                    \"href\": \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1/members\"
                },
                \"projects\": {
                    \"href\": \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1/projects\"
                }
            },
            \"created_on\": \"2018-11-14T19:15:05.058566+00:00\",
            \"type\": \"workspace\",
            \"slug\": \"bbworkspace1\",
            \"is_private\": true,
            \"name\": \"Atlassian Bitbucket\"
        }
      ]
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=slug=\"bbworkspace1\"` or `q=is_private=true`
    * `sort=created_on`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Args:
        role (Union[Unset, None, GetWorkspacesRole]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        client=client,
        role=role,
        q=q,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetWorkspacesRole] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List workspaces for user

     Returns a list of workspaces accessible by the authenticated user.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/workspaces

    {
      \"pagelen\": 10,
      \"page\": 1,
      \"size\": 1,
      \"values\": [
        {
            \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
            \"links\": {
                \"owners\": {
                    \"href\":
    \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1/members?q=permission%3D%22owner%22\"
                },
                \"self\": {
                    \"href\": \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1\"
                },
                \"repositories\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/bbworkspace1\"
                },
                \"snippets\": {
                    \"href\": \"https://api.bitbucket.org/2.0/snippets/bbworkspace1\"
                },
                \"html\": {
                    \"href\": \"https://bitbucket.org/bbworkspace1/\"
                },
                \"avatar\": {
                    \"href\": \"https://bitbucket.org/workspaces/bbworkspace1/avatar/?ts=1543465801\"
                },
                \"members\": {
                    \"href\": \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1/members\"
                },
                \"projects\": {
                    \"href\": \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1/projects\"
                }
            },
            \"created_on\": \"2018-11-14T19:15:05.058566+00:00\",
            \"type\": \"workspace\",
            \"slug\": \"bbworkspace1\",
            \"is_private\": true,
            \"name\": \"Atlassian Bitbucket\"
        }
      ]
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=slug=\"bbworkspace1\"` or `q=is_private=true`
    * `sort=created_on`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Args:
        role (Union[Unset, None, GetWorkspacesRole]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        client=client,
        role=role,
        q=q,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    role: Union[Unset, None, GetWorkspacesRole] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List workspaces for user

     Returns a list of workspaces accessible by the authenticated user.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/workspaces

    {
      \"pagelen\": 10,
      \"page\": 1,
      \"size\": 1,
      \"values\": [
        {
            \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
            \"links\": {
                \"owners\": {
                    \"href\":
    \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1/members?q=permission%3D%22owner%22\"
                },
                \"self\": {
                    \"href\": \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1\"
                },
                \"repositories\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/bbworkspace1\"
                },
                \"snippets\": {
                    \"href\": \"https://api.bitbucket.org/2.0/snippets/bbworkspace1\"
                },
                \"html\": {
                    \"href\": \"https://bitbucket.org/bbworkspace1/\"
                },
                \"avatar\": {
                    \"href\": \"https://bitbucket.org/workspaces/bbworkspace1/avatar/?ts=1543465801\"
                },
                \"members\": {
                    \"href\": \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1/members\"
                },
                \"projects\": {
                    \"href\": \"https://api.bitbucket.org/2.0/workspaces/bbworkspace1/projects\"
                }
            },
            \"created_on\": \"2018-11-14T19:15:05.058566+00:00\",
            \"type\": \"workspace\",
            \"slug\": \"bbworkspace1\",
            \"is_private\": true,
            \"name\": \"Atlassian Bitbucket\"
        }
      ]
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    workspace or permission by adding the following query string parameters:

    * `q=slug=\"bbworkspace1\"` or `q=is_private=true`
    * `sort=created_on`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Args:
        role (Union[Unset, None, GetWorkspacesRole]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            role=role,
            q=q,
            sort=sort,
        )
    ).parsed
