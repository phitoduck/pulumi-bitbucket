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
    url = "{}/repositories/{workspace}/{repo_slug}/effective-default-reviewers".format(
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
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """List effective default reviewers

     Returns the repository's effective default reviewers. This includes both default
    reviewers defined at the repository level as well as those inherited from its project.

    These are the users that are automatically added as reviewers on every
    new pull request that is created.

    ```
    $ curl https://bitbucket.org/!api/2.0/repositories/{workspace_slug}/{repo_slug}/effective-default-
    reviewers?page=1&pagelen=20
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"user\": {
                    \"display_name\": \"Patrick Wolf\",
                    \"uuid\": \"{9565301a-a3cf-4b5d-88f4-dd6af8078d7e}\"
                },
                \"reviewer_type\": \"project\",
                \"type\": \"default_reviewer\",
            },
            {
                \"user\": {
                    \"display_name\": \"Davis Lee\",
                    \"uuid\": \"{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\"
                },
                \"reviewer_type\": \"repository\",
                \"type\": \"default_reviewer\",
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
    """List effective default reviewers

     Returns the repository's effective default reviewers. This includes both default
    reviewers defined at the repository level as well as those inherited from its project.

    These are the users that are automatically added as reviewers on every
    new pull request that is created.

    ```
    $ curl https://bitbucket.org/!api/2.0/repositories/{workspace_slug}/{repo_slug}/effective-default-
    reviewers?page=1&pagelen=20
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"user\": {
                    \"display_name\": \"Patrick Wolf\",
                    \"uuid\": \"{9565301a-a3cf-4b5d-88f4-dd6af8078d7e}\"
                },
                \"reviewer_type\": \"project\",
                \"type\": \"default_reviewer\",
            },
            {
                \"user\": {
                    \"display_name\": \"Davis Lee\",
                    \"uuid\": \"{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\"
                },
                \"reviewer_type\": \"repository\",
                \"type\": \"default_reviewer\",
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
    """List effective default reviewers

     Returns the repository's effective default reviewers. This includes both default
    reviewers defined at the repository level as well as those inherited from its project.

    These are the users that are automatically added as reviewers on every
    new pull request that is created.

    ```
    $ curl https://bitbucket.org/!api/2.0/repositories/{workspace_slug}/{repo_slug}/effective-default-
    reviewers?page=1&pagelen=20
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"user\": {
                    \"display_name\": \"Patrick Wolf\",
                    \"uuid\": \"{9565301a-a3cf-4b5d-88f4-dd6af8078d7e}\"
                },
                \"reviewer_type\": \"project\",
                \"type\": \"default_reviewer\",
            },
            {
                \"user\": {
                    \"display_name\": \"Davis Lee\",
                    \"uuid\": \"{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\"
                },
                \"reviewer_type\": \"repository\",
                \"type\": \"default_reviewer\",
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
    """List effective default reviewers

     Returns the repository's effective default reviewers. This includes both default
    reviewers defined at the repository level as well as those inherited from its project.

    These are the users that are automatically added as reviewers on every
    new pull request that is created.

    ```
    $ curl https://bitbucket.org/!api/2.0/repositories/{workspace_slug}/{repo_slug}/effective-default-
    reviewers?page=1&pagelen=20
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"user\": {
                    \"display_name\": \"Patrick Wolf\",
                    \"uuid\": \"{9565301a-a3cf-4b5d-88f4-dd6af8078d7e}\"
                },
                \"reviewer_type\": \"project\",
                \"type\": \"default_reviewer\",
            },
            {
                \"user\": {
                    \"display_name\": \"Davis Lee\",
                    \"uuid\": \"{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}\"
                },
                \"reviewer_type\": \"repository\",
                \"type\": \"default_reviewer\",
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
