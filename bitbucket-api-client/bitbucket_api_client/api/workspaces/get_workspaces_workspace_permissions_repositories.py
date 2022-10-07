from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/permissions/repositories".format(client.base_url, workspace=workspace)

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
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Error]:
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
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List all repository permissions for a workspace

     Returns an object for each repository permission for all of a
    workspace's repositories.

    Permissions returned are effective permissions: the highest level of
    permission the user has. This does not distinguish between direct and
    indirect (group) privileges.

    Only users with admin permission for the team may access this resource.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/workspaces/atlassian_tutorial/permissions/repositories

    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"geordi\",
            \"full_name\": \"atlassian_tutorial/geordi\",
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
          },
          \"permission\": \"admin\"
        },
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Sean Conaty\",
            \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"geordi\",
            \"full_name\": \"atlassian_tutorial/geordi\",
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
          },
          \"permission\": \"write\"
        },
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Jeff Zeng\",
            \"uuid\": \"{47f92a9a-c3a3-4d0b-bc4e-782a969c5c72}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"whee\",
            \"full_name\": \"atlassian_tutorial/whee\",
            \"uuid\": \"{30ba25e9-51ff-4555-8dd0-fc7ee2fa0895}\"
          },
          \"permission\": \"admin\"
        }
      ],
      \"page\": 1,
      \"size\": 3
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering)
    by repository, user, or permission by adding the following query string
    parameters:

    * `q=repository.name=\"geordi\"` or `q=permission>\"read\"`
    * `sort=user.display_name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        workspace (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
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
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List all repository permissions for a workspace

     Returns an object for each repository permission for all of a
    workspace's repositories.

    Permissions returned are effective permissions: the highest level of
    permission the user has. This does not distinguish between direct and
    indirect (group) privileges.

    Only users with admin permission for the team may access this resource.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/workspaces/atlassian_tutorial/permissions/repositories

    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"geordi\",
            \"full_name\": \"atlassian_tutorial/geordi\",
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
          },
          \"permission\": \"admin\"
        },
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Sean Conaty\",
            \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"geordi\",
            \"full_name\": \"atlassian_tutorial/geordi\",
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
          },
          \"permission\": \"write\"
        },
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Jeff Zeng\",
            \"uuid\": \"{47f92a9a-c3a3-4d0b-bc4e-782a969c5c72}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"whee\",
            \"full_name\": \"atlassian_tutorial/whee\",
            \"uuid\": \"{30ba25e9-51ff-4555-8dd0-fc7ee2fa0895}\"
          },
          \"permission\": \"admin\"
        }
      ],
      \"page\": 1,
      \"size\": 3
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering)
    by repository, user, or permission by adding the following query string
    parameters:

    * `q=repository.name=\"geordi\"` or `q=permission>\"read\"`
    * `sort=user.display_name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        workspace (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        q=q,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List all repository permissions for a workspace

     Returns an object for each repository permission for all of a
    workspace's repositories.

    Permissions returned are effective permissions: the highest level of
    permission the user has. This does not distinguish between direct and
    indirect (group) privileges.

    Only users with admin permission for the team may access this resource.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/workspaces/atlassian_tutorial/permissions/repositories

    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"geordi\",
            \"full_name\": \"atlassian_tutorial/geordi\",
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
          },
          \"permission\": \"admin\"
        },
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Sean Conaty\",
            \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"geordi\",
            \"full_name\": \"atlassian_tutorial/geordi\",
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
          },
          \"permission\": \"write\"
        },
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Jeff Zeng\",
            \"uuid\": \"{47f92a9a-c3a3-4d0b-bc4e-782a969c5c72}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"whee\",
            \"full_name\": \"atlassian_tutorial/whee\",
            \"uuid\": \"{30ba25e9-51ff-4555-8dd0-fc7ee2fa0895}\"
          },
          \"permission\": \"admin\"
        }
      ],
      \"page\": 1,
      \"size\": 3
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering)
    by repository, user, or permission by adding the following query string
    parameters:

    * `q=repository.name=\"geordi\"` or `q=permission>\"read\"`
    * `sort=user.display_name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        workspace (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
        q=q,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List all repository permissions for a workspace

     Returns an object for each repository permission for all of a
    workspace's repositories.

    Permissions returned are effective permissions: the highest level of
    permission the user has. This does not distinguish between direct and
    indirect (group) privileges.

    Only users with admin permission for the team may access this resource.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/workspaces/atlassian_tutorial/permissions/repositories

    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"geordi\",
            \"full_name\": \"atlassian_tutorial/geordi\",
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
          },
          \"permission\": \"admin\"
        },
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Sean Conaty\",
            \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"geordi\",
            \"full_name\": \"atlassian_tutorial/geordi\",
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
          },
          \"permission\": \"write\"
        },
        {
          \"type\": \"repository_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Jeff Zeng\",
            \"uuid\": \"{47f92a9a-c3a3-4d0b-bc4e-782a969c5c72}\"
          },
          \"repository\": {
            \"type\": \"repository\",
            \"name\": \"whee\",
            \"full_name\": \"atlassian_tutorial/whee\",
            \"uuid\": \"{30ba25e9-51ff-4555-8dd0-fc7ee2fa0895}\"
          },
          \"permission\": \"admin\"
        }
      ],
      \"page\": 1,
      \"size\": 3
    }
    ```

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering)
    by repository, user, or permission by adding the following query string
    parameters:

    * `q=repository.name=\"geordi\"` or `q=permission>\"read\"`
    * `sort=user.display_name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        workspace (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            q=q,
            sort=sort,
        )
    ).parsed
