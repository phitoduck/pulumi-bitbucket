from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.paginated_pipeline_schedule_executions import PaginatedPipelineScheduleExecutions
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    schedule_uuid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}/executions/".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, schedule_uuid=schedule_uuid
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, PaginatedPipelineScheduleExecutions]]:
    if response.status_code == 200:
        response_200 = PaginatedPipelineScheduleExecutions.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, PaginatedPipelineScheduleExecutions]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    schedule_uuid: str,
    *,
    client: Client,
) -> Response[Union[Error, PaginatedPipelineScheduleExecutions]]:
    """List executions of a schedule

     Retrieve the executions of a given schedule.

    Args:
        workspace (str):
        repo_slug (str):
        schedule_uuid (str):

    Returns:
        Response[Union[Error, PaginatedPipelineScheduleExecutions]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        schedule_uuid=schedule_uuid,
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
    schedule_uuid: str,
    *,
    client: Client,
) -> Optional[Union[Error, PaginatedPipelineScheduleExecutions]]:
    """List executions of a schedule

     Retrieve the executions of a given schedule.

    Args:
        workspace (str):
        repo_slug (str):
        schedule_uuid (str):

    Returns:
        Response[Union[Error, PaginatedPipelineScheduleExecutions]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        schedule_uuid=schedule_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    schedule_uuid: str,
    *,
    client: Client,
) -> Response[Union[Error, PaginatedPipelineScheduleExecutions]]:
    """List executions of a schedule

     Retrieve the executions of a given schedule.

    Args:
        workspace (str):
        repo_slug (str):
        schedule_uuid (str):

    Returns:
        Response[Union[Error, PaginatedPipelineScheduleExecutions]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        schedule_uuid=schedule_uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    schedule_uuid: str,
    *,
    client: Client,
) -> Optional[Union[Error, PaginatedPipelineScheduleExecutions]]:
    """List executions of a schedule

     Retrieve the executions of a given schedule.

    Args:
        workspace (str):
        repo_slug (str):
        schedule_uuid (str):

    Returns:
        Response[Union[Error, PaginatedPipelineScheduleExecutions]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            schedule_uuid=schedule_uuid,
            client=client,
        )
    ).parsed
