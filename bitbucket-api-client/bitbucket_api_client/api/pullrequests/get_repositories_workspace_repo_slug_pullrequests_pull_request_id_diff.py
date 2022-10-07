from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, pull_request_id=pull_request_id
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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """List changes in a pull request

     Redirects to the [repository diff](/cloud/bitbucket/rest/api-group-commits/#api-repositories-
    workspace-repo-slug-diff-spec-get)
    with the revspec that corresponds to the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """List changes in a pull request

     Redirects to the [repository diff](/cloud/bitbucket/rest/api-group-commits/#api-repositories-
    workspace-repo-slug-diff-spec-get)
    with the revspec that corresponds to the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
