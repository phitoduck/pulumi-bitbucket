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
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/permissions".format(client.base_url, workspace=workspace)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["q"] = q

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
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List user permissions in a workspace

     Returns the list of members in a workspace
    and their permission levels.
    Permission can be:
    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Example:

    ```
    $ curl -X https://api.bitbucket.org/2.0/workspaces/bbworkspace1/permissions

    {
        \"pagelen\": 10,
        \"values\": [
            {
                \"permission\": \"owner\",
                \"type\": \"workspace_membership\",
                \"user\": {
                    \"type\": \"user\",
                    \"uuid\": \"{470c176d-3574-44ea-bb41-89e8638bcca4}\",
                    \"display_name\": \"Erik van Zijst\",
                },
                \"workspace\": {
                    \"type\": \"workspace\",
                    \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
                    \"slug\": \"bbworkspace1\",
                    \"name\": \"Atlassian Bitbucket\",
                }
            },
            {
                \"permission\": \"member\",
                \"type\": \"workspace_membership\",
                \"user\": {
                    \"type\": \"user\",
                    \"nickname\": \"seanaty\",
                    \"display_name\": \"Sean Conaty\",
                    \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"
                },
                \"workspace\": {
                    \"type\": \"workspace\",
                    \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
                    \"slug\": \"bbworkspace1\",
                    \"name\": \"Atlassian Bitbucket\",
                }
            }
        ],
        \"page\": 1,
        \"size\": 2
    }
    ```

    Results may be further [filtered](/cloud/bitbucket/rest/intro/#filtering) by
    permission by adding the following query string parameters:

    * `q=permission=\"owner\"`

    Args:
        workspace (str):
        q (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
        q=q,
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
) -> Optional[Error]:
    """List user permissions in a workspace

     Returns the list of members in a workspace
    and their permission levels.
    Permission can be:
    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Example:

    ```
    $ curl -X https://api.bitbucket.org/2.0/workspaces/bbworkspace1/permissions

    {
        \"pagelen\": 10,
        \"values\": [
            {
                \"permission\": \"owner\",
                \"type\": \"workspace_membership\",
                \"user\": {
                    \"type\": \"user\",
                    \"uuid\": \"{470c176d-3574-44ea-bb41-89e8638bcca4}\",
                    \"display_name\": \"Erik van Zijst\",
                },
                \"workspace\": {
                    \"type\": \"workspace\",
                    \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
                    \"slug\": \"bbworkspace1\",
                    \"name\": \"Atlassian Bitbucket\",
                }
            },
            {
                \"permission\": \"member\",
                \"type\": \"workspace_membership\",
                \"user\": {
                    \"type\": \"user\",
                    \"nickname\": \"seanaty\",
                    \"display_name\": \"Sean Conaty\",
                    \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"
                },
                \"workspace\": {
                    \"type\": \"workspace\",
                    \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
                    \"slug\": \"bbworkspace1\",
                    \"name\": \"Atlassian Bitbucket\",
                }
            }
        ],
        \"page\": 1,
        \"size\": 2
    }
    ```

    Results may be further [filtered](/cloud/bitbucket/rest/intro/#filtering) by
    permission by adding the following query string parameters:

    * `q=permission=\"owner\"`

    Args:
        workspace (str):
        q (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        q=q,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List user permissions in a workspace

     Returns the list of members in a workspace
    and their permission levels.
    Permission can be:
    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Example:

    ```
    $ curl -X https://api.bitbucket.org/2.0/workspaces/bbworkspace1/permissions

    {
        \"pagelen\": 10,
        \"values\": [
            {
                \"permission\": \"owner\",
                \"type\": \"workspace_membership\",
                \"user\": {
                    \"type\": \"user\",
                    \"uuid\": \"{470c176d-3574-44ea-bb41-89e8638bcca4}\",
                    \"display_name\": \"Erik van Zijst\",
                },
                \"workspace\": {
                    \"type\": \"workspace\",
                    \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
                    \"slug\": \"bbworkspace1\",
                    \"name\": \"Atlassian Bitbucket\",
                }
            },
            {
                \"permission\": \"member\",
                \"type\": \"workspace_membership\",
                \"user\": {
                    \"type\": \"user\",
                    \"nickname\": \"seanaty\",
                    \"display_name\": \"Sean Conaty\",
                    \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"
                },
                \"workspace\": {
                    \"type\": \"workspace\",
                    \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
                    \"slug\": \"bbworkspace1\",
                    \"name\": \"Atlassian Bitbucket\",
                }
            }
        ],
        \"page\": 1,
        \"size\": 2
    }
    ```

    Results may be further [filtered](/cloud/bitbucket/rest/intro/#filtering) by
    permission by adding the following query string parameters:

    * `q=permission=\"owner\"`

    Args:
        workspace (str):
        q (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
        q=q,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List user permissions in a workspace

     Returns the list of members in a workspace
    and their permission levels.
    Permission can be:
    * `owner`
    * `collaborator`
    * `member`

    **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information,
    see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**

    Example:

    ```
    $ curl -X https://api.bitbucket.org/2.0/workspaces/bbworkspace1/permissions

    {
        \"pagelen\": 10,
        \"values\": [
            {
                \"permission\": \"owner\",
                \"type\": \"workspace_membership\",
                \"user\": {
                    \"type\": \"user\",
                    \"uuid\": \"{470c176d-3574-44ea-bb41-89e8638bcca4}\",
                    \"display_name\": \"Erik van Zijst\",
                },
                \"workspace\": {
                    \"type\": \"workspace\",
                    \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
                    \"slug\": \"bbworkspace1\",
                    \"name\": \"Atlassian Bitbucket\",
                }
            },
            {
                \"permission\": \"member\",
                \"type\": \"workspace_membership\",
                \"user\": {
                    \"type\": \"user\",
                    \"nickname\": \"seanaty\",
                    \"display_name\": \"Sean Conaty\",
                    \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"
                },
                \"workspace\": {
                    \"type\": \"workspace\",
                    \"uuid\": \"{a15fb181-db1f-48f7-b41f-e1eff06929d6}\",
                    \"slug\": \"bbworkspace1\",
                    \"name\": \"Atlassian Bitbucket\",
                }
            }
        ],
        \"page\": 1,
        \"size\": 2
    }
    ```

    Results may be further [filtered](/cloud/bitbucket/rest/intro/#filtering) by
    permission by adding the following query string parameters:

    * `q=permission=\"owner\"`

    Args:
        workspace (str):
        q (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            q=q,
        )
    ).parsed
