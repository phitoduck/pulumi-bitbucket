from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/permissions-config/groups".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Error]:
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
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
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """List explicit group permissions for a repository

     Returns a paginated list of explicit group permissions for the given repository.
    This endpoint does not support BBQL features.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-
    config/groups

    HTTP/1.1 200
    Location: https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-
    config/groups

    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"type\": \"repository_group_permission\",
          \"group\": {
            \"type\": \"group\",
            \"name\": \"Administrators\",
            \"slug\": \"administrators\"
          },
          \"permission\": \"admin\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/
                       geordi/permissions-config/groups/administrators\"
            }
          }
        },
        {
          \"type\": \"repository_group_permission\",
          \"group\": {
            \"type\": \"group\",
            \"name\": \"Developers\",
            \"slug\": \"developers\"
          },
          \"permission\": \"read\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/
                       geordi/permissions-config/groups/developers\"
            }
          }
        }
      ],
      \"page\": 1,
      \"size\": 2
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """List explicit group permissions for a repository

     Returns a paginated list of explicit group permissions for the given repository.
    This endpoint does not support BBQL features.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-
    config/groups

    HTTP/1.1 200
    Location: https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-
    config/groups

    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"type\": \"repository_group_permission\",
          \"group\": {
            \"type\": \"group\",
            \"name\": \"Administrators\",
            \"slug\": \"administrators\"
          },
          \"permission\": \"admin\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/
                       geordi/permissions-config/groups/administrators\"
            }
          }
        },
        {
          \"type\": \"repository_group_permission\",
          \"group\": {
            \"type\": \"group\",
            \"name\": \"Developers\",
            \"slug\": \"developers\"
          },
          \"permission\": \"read\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/
                       geordi/permissions-config/groups/developers\"
            }
          }
        }
      ],
      \"page\": 1,
      \"size\": 2
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """List explicit group permissions for a repository

     Returns a paginated list of explicit group permissions for the given repository.
    This endpoint does not support BBQL features.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-
    config/groups

    HTTP/1.1 200
    Location: https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-
    config/groups

    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"type\": \"repository_group_permission\",
          \"group\": {
            \"type\": \"group\",
            \"name\": \"Administrators\",
            \"slug\": \"administrators\"
          },
          \"permission\": \"admin\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/
                       geordi/permissions-config/groups/administrators\"
            }
          }
        },
        {
          \"type\": \"repository_group_permission\",
          \"group\": {
            \"type\": \"group\",
            \"name\": \"Developers\",
            \"slug\": \"developers\"
          },
          \"permission\": \"read\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/
                       geordi/permissions-config/groups/developers\"
            }
          }
        }
      ],
      \"page\": 1,
      \"size\": 2
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """List explicit group permissions for a repository

     Returns a paginated list of explicit group permissions for the given repository.
    This endpoint does not support BBQL features.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-
    config/groups

    HTTP/1.1 200
    Location: https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-
    config/groups

    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"type\": \"repository_group_permission\",
          \"group\": {
            \"type\": \"group\",
            \"name\": \"Administrators\",
            \"slug\": \"administrators\"
          },
          \"permission\": \"admin\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/
                       geordi/permissions-config/groups/administrators\"
            }
          }
        },
        {
          \"type\": \"repository_group_permission\",
          \"group\": {
            \"type\": \"group\",
            \"name\": \"Developers\",
            \"slug\": \"developers\"
          },
          \"permission\": \"read\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/
                       geordi/permissions-config/groups/developers\"
            }
          }
        }
      ],
      \"page\": 1,
      \"size\": 2
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
        )
    ).parsed
