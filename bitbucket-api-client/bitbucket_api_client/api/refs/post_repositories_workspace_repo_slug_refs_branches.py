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
    url = "{}/repositories/{workspace}/{repo_slug}/refs/branches".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
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
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Create a branch

     Creates a new branch in the specified repository.

    The payload of the POST should consist of a JSON document that
    contains the name of the tag and the target hash.

    ```
    curl https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/branches \
    -s -u seanfarley -X POST -H \"Content-Type: application/json\" \
    -d '{
        \"name\" : \"smf/create-feature\",
        \"target\" : {
            \"hash\" : \"default\",
        }
    }'
    ```

    This call requires authentication. Private repositories require the
    caller to authenticate with an account that has appropriate
    authorization.

    The branch name should not include any prefixes (e.g.
    refs/heads). This endpoint does support using short hash prefixes for
    the commit hash, but it may return a 400 response if the provided
    prefix is ambiguous. Using a full commit hash is the preferred
    approach.

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
    """Create a branch

     Creates a new branch in the specified repository.

    The payload of the POST should consist of a JSON document that
    contains the name of the tag and the target hash.

    ```
    curl https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/branches \
    -s -u seanfarley -X POST -H \"Content-Type: application/json\" \
    -d '{
        \"name\" : \"smf/create-feature\",
        \"target\" : {
            \"hash\" : \"default\",
        }
    }'
    ```

    This call requires authentication. Private repositories require the
    caller to authenticate with an account that has appropriate
    authorization.

    The branch name should not include any prefixes (e.g.
    refs/heads). This endpoint does support using short hash prefixes for
    the commit hash, but it may return a 400 response if the provided
    prefix is ambiguous. Using a full commit hash is the preferred
    approach.

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
    """Create a branch

     Creates a new branch in the specified repository.

    The payload of the POST should consist of a JSON document that
    contains the name of the tag and the target hash.

    ```
    curl https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/branches \
    -s -u seanfarley -X POST -H \"Content-Type: application/json\" \
    -d '{
        \"name\" : \"smf/create-feature\",
        \"target\" : {
            \"hash\" : \"default\",
        }
    }'
    ```

    This call requires authentication. Private repositories require the
    caller to authenticate with an account that has appropriate
    authorization.

    The branch name should not include any prefixes (e.g.
    refs/heads). This endpoint does support using short hash prefixes for
    the commit hash, but it may return a 400 response if the provided
    prefix is ambiguous. Using a full commit hash is the preferred
    approach.

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
    """Create a branch

     Creates a new branch in the specified repository.

    The payload of the POST should consist of a JSON document that
    contains the name of the tag and the target hash.

    ```
    curl https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/branches \
    -s -u seanfarley -X POST -H \"Content-Type: application/json\" \
    -d '{
        \"name\" : \"smf/create-feature\",
        \"target\" : {
            \"hash\" : \"default\",
        }
    }'
    ```

    This call requires authentication. Private repositories require the
    caller to authenticate with an account that has appropriate
    authorization.

    The branch name should not include any prefixes (e.g.
    refs/heads). This endpoint does support using short hash prefixes for
    the commit hash, but it may return a 400 response if the provided
    prefix is ambiguous. Using a full commit hash is the preferred
    approach.

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
