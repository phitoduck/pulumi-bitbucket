from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/projects/{project_key}/default-reviewers".format(
        client.base_url, workspace=workspace, project_key=project_key
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
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """List the default reviewers in a project

     Return a list of all default reviewers for a project. This is a list of users that will be added as
    default
    reviewers to pull requests for any repository within the project.

    Example:
    ```
    $ curl https://bitbucket.org/!api/2.0/.../projects/.../default-reviewers | jq .
    {
        \"pagelen\": 10,
        \"values\": [
            {
                \"user\": {
                    \"display_name\": \"Davis Lee\",
                    \"uuid\": \"{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\"
                },
                \"reviewer_type\": \"project\",
                \"type\": \"default_reviewer\"
            },
            {
                \"user\": {
                    \"display_name\": \"Jorge Rodriguez\",
                    \"uuid\": \"{1aa43376-260d-4a0b-9660-f62672b9655d}\"
                },
                \"reviewer_type\": \"project\",
                \"type\": \"default_reviewer\"
            }
        ],
        \"page\": 1,
        \"size\": 2
    }
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """List the default reviewers in a project

     Return a list of all default reviewers for a project. This is a list of users that will be added as
    default
    reviewers to pull requests for any repository within the project.

    Example:
    ```
    $ curl https://bitbucket.org/!api/2.0/.../projects/.../default-reviewers | jq .
    {
        \"pagelen\": 10,
        \"values\": [
            {
                \"user\": {
                    \"display_name\": \"Davis Lee\",
                    \"uuid\": \"{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\"
                },
                \"reviewer_type\": \"project\",
                \"type\": \"default_reviewer\"
            },
            {
                \"user\": {
                    \"display_name\": \"Jorge Rodriguez\",
                    \"uuid\": \"{1aa43376-260d-4a0b-9660-f62672b9655d}\"
                },
                \"reviewer_type\": \"project\",
                \"type\": \"default_reviewer\"
            }
        ],
        \"page\": 1,
        \"size\": 2
    }
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        project_key=project_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """List the default reviewers in a project

     Return a list of all default reviewers for a project. This is a list of users that will be added as
    default
    reviewers to pull requests for any repository within the project.

    Example:
    ```
    $ curl https://bitbucket.org/!api/2.0/.../projects/.../default-reviewers | jq .
    {
        \"pagelen\": 10,
        \"values\": [
            {
                \"user\": {
                    \"display_name\": \"Davis Lee\",
                    \"uuid\": \"{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\"
                },
                \"reviewer_type\": \"project\",
                \"type\": \"default_reviewer\"
            },
            {
                \"user\": {
                    \"display_name\": \"Jorge Rodriguez\",
                    \"uuid\": \"{1aa43376-260d-4a0b-9660-f62672b9655d}\"
                },
                \"reviewer_type\": \"project\",
                \"type\": \"default_reviewer\"
            }
        ],
        \"page\": 1,
        \"size\": 2
    }
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """List the default reviewers in a project

     Return a list of all default reviewers for a project. This is a list of users that will be added as
    default
    reviewers to pull requests for any repository within the project.

    Example:
    ```
    $ curl https://bitbucket.org/!api/2.0/.../projects/.../default-reviewers | jq .
    {
        \"pagelen\": 10,
        \"values\": [
            {
                \"user\": {
                    \"display_name\": \"Davis Lee\",
                    \"uuid\": \"{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\"
                },
                \"reviewer_type\": \"project\",
                \"type\": \"default_reviewer\"
            },
            {
                \"user\": {
                    \"display_name\": \"Jorge Rodriguez\",
                    \"uuid\": \"{1aa43376-260d-4a0b-9660-f62672b9655d}\"
                },
                \"reviewer_type\": \"project\",
                \"type\": \"default_reviewer\"
            }
        ],
        \"page\": 1,
        \"size\": 2
    }
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            project_key=project_key,
            client=client,
        )
    ).parsed
