from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.report_annotation import ReportAnnotation
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    annotation_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = (
        "{}/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}".format(
            client.base_url,
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            reportId=report_id,
            annotationId=annotation_id,
        )
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, ReportAnnotation]]:
    if response.status_code == 200:
        response_200 = ReportAnnotation.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, ReportAnnotation]]:
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
    annotation_id: str,
    *,
    client: Client,
) -> Response[Union[Error, ReportAnnotation]]:
    """Get an annotation

     Returns a single Annotation matching the provided ID.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        annotation_id (str):

    Returns:
        Response[Union[Error, ReportAnnotation]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        annotation_id=annotation_id,
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
    annotation_id: str,
    *,
    client: Client,
) -> Optional[Union[Error, ReportAnnotation]]:
    """Get an annotation

     Returns a single Annotation matching the provided ID.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        annotation_id (str):

    Returns:
        Response[Union[Error, ReportAnnotation]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        annotation_id=annotation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    annotation_id: str,
    *,
    client: Client,
) -> Response[Union[Error, ReportAnnotation]]:
    """Get an annotation

     Returns a single Annotation matching the provided ID.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        annotation_id (str):

    Returns:
        Response[Union[Error, ReportAnnotation]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        annotation_id=annotation_id,
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
    annotation_id: str,
    *,
    client: Client,
) -> Optional[Union[Error, ReportAnnotation]]:
    """Get an annotation

     Returns a single Annotation matching the provided ID.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        annotation_id (str):

    Returns:
        Response[Union[Error, ReportAnnotation]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            report_id=report_id,
            annotation_id=annotation_id,
            client=client,
        )
    ).parsed
