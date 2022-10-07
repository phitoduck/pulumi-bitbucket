from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    project_key: str,
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}".format(
        client.base_url, workspace=workspace, project_key=project_key, selected_user=selected_user
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
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
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
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Get a default reviewer

     Returns the specified default reviewer.

    Example:
    ```
    $ curl https://bitbucket.org/!api/2.0/.../default-
    reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D
    {
        \"display_name\": \"Davis Lee\",
        \"type\": \"user\",
        \"uuid\": \"{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\"
    }
    ```

    Args:
        workspace (str):
        project_key (str):
        selected_user (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        selected_user=selected_user,
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
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Get a default reviewer

     Returns the specified default reviewer.

    Example:
    ```
    $ curl https://bitbucket.org/!api/2.0/.../default-
    reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D
    {
        \"display_name\": \"Davis Lee\",
        \"type\": \"user\",
        \"uuid\": \"{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\"
    }
    ```

    Args:
        workspace (str):
        project_key (str):
        selected_user (str):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        project_key=project_key,
        selected_user=selected_user,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    project_key: str,
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Get a default reviewer

     Returns the specified default reviewer.

    Example:
    ```
    $ curl https://bitbucket.org/!api/2.0/.../default-
    reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D
    {
        \"display_name\": \"Davis Lee\",
        \"type\": \"user\",
        \"uuid\": \"{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\"
    }
    ```

    Args:
        workspace (str):
        project_key (str):
        selected_user (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        selected_user=selected_user,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    project_key: str,
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Get a default reviewer

     Returns the specified default reviewer.

    Example:
    ```
    $ curl https://bitbucket.org/!api/2.0/.../default-
    reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D
    {
        \"display_name\": \"Davis Lee\",
        \"type\": \"user\",
        \"uuid\": \"{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\"
    }
    ```

    Args:
        workspace (str):
        project_key (str):
        selected_user (str):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            project_key=project_key,
            selected_user=selected_user,
            client=client,
        )
    ).parsed
