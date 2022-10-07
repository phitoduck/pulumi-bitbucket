from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/decline".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, pull_request_id=pull_request_id
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
    if response.status_code == 555:
        response_555 = Error.from_dict(response.json())

        return response_555
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
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Decline a pull request

     Declines the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):

    Returns:
        Response[Error]
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


def sync(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Decline a pull request

     Declines the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Decline a pull request

     Declines the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):

    Returns:
        Response[Error]
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


async def asyncio(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Decline a pull request

     Declines the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            pull_request_id=pull_request_id,
            client=client,
        )
    ).parsed
