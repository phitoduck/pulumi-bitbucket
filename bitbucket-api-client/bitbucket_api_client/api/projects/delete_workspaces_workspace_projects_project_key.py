from typing import Any, Dict, Optional, Union, cast

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
    url = "{}/workspaces/{workspace}/projects/{project_key}".format(
        client.base_url, workspace=workspace, project_key=project_key
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Error]]:
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
) -> Response[Union[Any, Error]]:
    """Delete a project for a workspace

     Deletes this project. This is an irreversible operation.

    You cannot delete a project that still contains repositories.
    To delete the project, [delete](/cloud/bitbucket/rest/api-group-repositories/#api-repositories-
    workspace-repo-slug-delete)
    or transfer the repositories first.

    Example:
    ```
    $ curl -X DELETE https://api.bitbucket.org/2.0/bbworkspace1/PROJ
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Union[Any, Error]]
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
) -> Optional[Union[Any, Error]]:
    """Delete a project for a workspace

     Deletes this project. This is an irreversible operation.

    You cannot delete a project that still contains repositories.
    To delete the project, [delete](/cloud/bitbucket/rest/api-group-repositories/#api-repositories-
    workspace-repo-slug-delete)
    or transfer the repositories first.

    Example:
    ```
    $ curl -X DELETE https://api.bitbucket.org/2.0/bbworkspace1/PROJ
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Union[Any, Error]]
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
) -> Response[Union[Any, Error]]:
    """Delete a project for a workspace

     Deletes this project. This is an irreversible operation.

    You cannot delete a project that still contains repositories.
    To delete the project, [delete](/cloud/bitbucket/rest/api-group-repositories/#api-repositories-
    workspace-repo-slug-delete)
    or transfer the repositories first.

    Example:
    ```
    $ curl -X DELETE https://api.bitbucket.org/2.0/bbworkspace1/PROJ
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Union[Any, Error]]
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
) -> Optional[Union[Any, Error]]:
    """Delete a project for a workspace

     Deletes this project. This is an irreversible operation.

    You cannot delete a project that still contains repositories.
    To delete the project, [delete](/cloud/bitbucket/rest/api-group-repositories/#api-repositories-
    workspace-repo-slug-delete)
    or transfer the repositories first.

    Example:
    ```
    $ curl -X DELETE https://api.bitbucket.org/2.0/bbworkspace1/PROJ
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            project_key=project_key,
            client=client,
        )
    ).parsed
