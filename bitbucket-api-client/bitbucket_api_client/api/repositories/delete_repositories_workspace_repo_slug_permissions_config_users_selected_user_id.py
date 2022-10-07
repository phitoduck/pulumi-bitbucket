from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    selected_user_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, selected_user_id=selected_user_id
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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    selected_user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """Delete an explicit user permission for a repository

     Deletes the repository user permission between the requested repository and user, if one exists.

    Only users with admin permission for the repository may access this resource.

    The only authentication method for this endpoint is via app passwords.

    ```
    $ curl -X DELETE https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/
    permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a


    HTTP/1.1 204
    ```

    Args:
        workspace (str):
        repo_slug (str):
        selected_user_id (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        selected_user_id=selected_user_id,
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
    selected_user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """Delete an explicit user permission for a repository

     Deletes the repository user permission between the requested repository and user, if one exists.

    Only users with admin permission for the repository may access this resource.

    The only authentication method for this endpoint is via app passwords.

    ```
    $ curl -X DELETE https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/
    permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a


    HTTP/1.1 204
    ```

    Args:
        workspace (str):
        repo_slug (str):
        selected_user_id (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        selected_user_id=selected_user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    selected_user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """Delete an explicit user permission for a repository

     Deletes the repository user permission between the requested repository and user, if one exists.

    Only users with admin permission for the repository may access this resource.

    The only authentication method for this endpoint is via app passwords.

    ```
    $ curl -X DELETE https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/
    permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a


    HTTP/1.1 204
    ```

    Args:
        workspace (str):
        repo_slug (str):
        selected_user_id (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        selected_user_id=selected_user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    selected_user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """Delete an explicit user permission for a repository

     Deletes the repository user permission between the requested repository and user, if one exists.

    Only users with admin permission for the repository may access this resource.

    The only authentication method for this endpoint is via app passwords.

    ```
    $ curl -X DELETE https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/
    permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a


    HTTP/1.1 204
    ```

    Args:
        workspace (str):
        repo_slug (str):
        selected_user_id (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            selected_user_id=selected_user_id,
            client=client,
        )
    ).parsed
