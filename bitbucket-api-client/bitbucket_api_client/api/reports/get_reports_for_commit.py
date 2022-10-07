from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.paginated_reports import PaginatedReports
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/commit/{commit}/reports".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, commit=commit
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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedReports]:
    if response.status_code == 200:
        response_200 = PaginatedReports.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedReports]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: Client,
) -> Response[PaginatedReports]:
    """List reports

     Returns a paginated list of Reports linked to this commit.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):

    Returns:
        Response[PaginatedReports]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
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
    commit: str,
    *,
    client: Client,
) -> Optional[PaginatedReports]:
    """List reports

     Returns a paginated list of Reports linked to this commit.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):

    Returns:
        Response[PaginatedReports]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: Client,
) -> Response[PaginatedReports]:
    """List reports

     Returns a paginated list of Reports linked to this commit.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):

    Returns:
        Response[PaginatedReports]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: Client,
) -> Optional[PaginatedReports]:
    """List reports

     Returns a paginated list of Reports linked to this commit.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):

    Returns:
        Response[PaginatedReports]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            client=client,
        )
    ).parsed
