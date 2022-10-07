from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.paginated_accounts import PaginatedAccounts
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/default-reviewers".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, PaginatedAccounts]]:
    if response.status_code == 200:
        response_200 = PaginatedAccounts.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, PaginatedAccounts]]:
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
) -> Response[Union[Error, PaginatedAccounts]]:
    """List default reviewers

     Returns the repository's default reviewers.

    These are the users that are automatically added as reviewers on every
    new pull request that is created. To obtain the repository's default reviewers
    as well as the default reviewers inherited from the project, use the
    [effective-default-reveiwers](#api-repositories-workspace-repo-slug-effective-default-reviewers-get)
    endpoint.

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[Error, PaginatedAccounts]]
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
) -> Optional[Union[Error, PaginatedAccounts]]:
    """List default reviewers

     Returns the repository's default reviewers.

    These are the users that are automatically added as reviewers on every
    new pull request that is created. To obtain the repository's default reviewers
    as well as the default reviewers inherited from the project, use the
    [effective-default-reveiwers](#api-repositories-workspace-repo-slug-effective-default-reviewers-get)
    endpoint.

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[Error, PaginatedAccounts]]
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
) -> Response[Union[Error, PaginatedAccounts]]:
    """List default reviewers

     Returns the repository's default reviewers.

    These are the users that are automatically added as reviewers on every
    new pull request that is created. To obtain the repository's default reviewers
    as well as the default reviewers inherited from the project, use the
    [effective-default-reveiwers](#api-repositories-workspace-repo-slug-effective-default-reviewers-get)
    endpoint.

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[Error, PaginatedAccounts]]
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
) -> Optional[Union[Error, PaginatedAccounts]]:
    """List default reviewers

     Returns the repository's default reviewers.

    These are the users that are automatically added as reviewers on every
    new pull request that is created. To obtain the repository's default reviewers
    as well as the default reviewers inherited from the project, use the
    [effective-default-reveiwers](#api-repositories-workspace-repo-slug-effective-default-reviewers-get)
    endpoint.

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[Error, PaginatedAccounts]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
        )
    ).parsed
