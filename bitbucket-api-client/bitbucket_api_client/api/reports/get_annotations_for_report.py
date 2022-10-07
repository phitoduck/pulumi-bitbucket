from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.paginated_annotations import PaginatedAnnotations
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, commit=commit, reportId=report_id
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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedAnnotations]:
    if response.status_code == 200:
        response_200 = PaginatedAnnotations.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedAnnotations]:
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
    report_id: str,
    *,
    client: Client,
) -> Response[PaginatedAnnotations]:
    """List annotations

     Returns a paginated list of Annotations for a specified report.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):

    Returns:
        Response[PaginatedAnnotations]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
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
    report_id: str,
    *,
    client: Client,
) -> Optional[PaginatedAnnotations]:
    """List annotations

     Returns a paginated list of Annotations for a specified report.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):

    Returns:
        Response[PaginatedAnnotations]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    client: Client,
) -> Response[PaginatedAnnotations]:
    """List annotations

     Returns a paginated list of Annotations for a specified report.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):

    Returns:
        Response[PaginatedAnnotations]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    client: Client,
) -> Optional[PaginatedAnnotations]:
    """List annotations

     Returns a paginated list of Annotations for a specified report.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):

    Returns:
        Response[PaginatedAnnotations]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            report_id=report_id,
            client=client,
        )
    ).parsed
