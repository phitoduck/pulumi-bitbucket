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
    url = "{}/repositories/{workspace}/{repo_slug}/permissions-config/users".format(
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
    """List explicit user permissions for a repository

     Returns a paginated list of explicit user permissions for the given repository.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/users

    {
      \"pagelen\": 10,
      \"values\": [
        {
            \"type\": \"repository_user_permission\",
            \"user\": {
                \"type\": \"user\",
                \"display_name\": \"Colin Cameron\",
                \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",
                \"account_id\": \"557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\"
            },
            \"permission\": \"admin\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/
                         permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\"
              }
            }
        },
        {
          \"type\": \"repository_user_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Sean Conaty\",
            \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\",
            \"account_id\": \"557058:ba8948b2-49da-43a9-9e8b-e7249b8e324c\"
          },
          \"permission\": \"write\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0//repositories/atlassian_tutorial/geordi/
                       permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324c\"
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
    """List explicit user permissions for a repository

     Returns a paginated list of explicit user permissions for the given repository.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/users

    {
      \"pagelen\": 10,
      \"values\": [
        {
            \"type\": \"repository_user_permission\",
            \"user\": {
                \"type\": \"user\",
                \"display_name\": \"Colin Cameron\",
                \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",
                \"account_id\": \"557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\"
            },
            \"permission\": \"admin\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/
                         permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\"
              }
            }
        },
        {
          \"type\": \"repository_user_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Sean Conaty\",
            \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\",
            \"account_id\": \"557058:ba8948b2-49da-43a9-9e8b-e7249b8e324c\"
          },
          \"permission\": \"write\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0//repositories/atlassian_tutorial/geordi/
                       permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324c\"
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
    """List explicit user permissions for a repository

     Returns a paginated list of explicit user permissions for the given repository.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/users

    {
      \"pagelen\": 10,
      \"values\": [
        {
            \"type\": \"repository_user_permission\",
            \"user\": {
                \"type\": \"user\",
                \"display_name\": \"Colin Cameron\",
                \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",
                \"account_id\": \"557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\"
            },
            \"permission\": \"admin\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/
                         permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\"
              }
            }
        },
        {
          \"type\": \"repository_user_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Sean Conaty\",
            \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\",
            \"account_id\": \"557058:ba8948b2-49da-43a9-9e8b-e7249b8e324c\"
          },
          \"permission\": \"write\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0//repositories/atlassian_tutorial/geordi/
                       permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324c\"
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
    """List explicit user permissions for a repository

     Returns a paginated list of explicit user permissions for the given repository.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/users

    {
      \"pagelen\": 10,
      \"values\": [
        {
            \"type\": \"repository_user_permission\",
            \"user\": {
                \"type\": \"user\",
                \"display_name\": \"Colin Cameron\",
                \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",
                \"account_id\": \"557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\"
            },
            \"permission\": \"admin\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/
                         permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a\"
              }
            }
        },
        {
          \"type\": \"repository_user_permission\",
          \"user\": {
            \"type\": \"user\",
            \"display_name\": \"Sean Conaty\",
            \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\",
            \"account_id\": \"557058:ba8948b2-49da-43a9-9e8b-e7249b8e324c\"
          },
          \"permission\": \"write\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0//repositories/atlassian_tutorial/geordi/
                       permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324c\"
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
