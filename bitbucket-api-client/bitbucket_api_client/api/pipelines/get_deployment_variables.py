from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.paginated_deployment_variables import PaginatedDeploymentVariables
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, environment_uuid=environment_uuid
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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedDeploymentVariables]:
    if response.status_code == 200:
        response_200 = PaginatedDeploymentVariables.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedDeploymentVariables]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    client: Client,
) -> Response[PaginatedDeploymentVariables]:
    """List variables for an environment

     Find deployment environment level variables.

    Args:
        workspace (str):
        repo_slug (str):
        environment_uuid (str):

    Returns:
        Response[PaginatedDeploymentVariables]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        environment_uuid=environment_uuid,
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
    environment_uuid: str,
    *,
    client: Client,
) -> Optional[PaginatedDeploymentVariables]:
    """List variables for an environment

     Find deployment environment level variables.

    Args:
        workspace (str):
        repo_slug (str):
        environment_uuid (str):

    Returns:
        Response[PaginatedDeploymentVariables]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        environment_uuid=environment_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    client: Client,
) -> Response[PaginatedDeploymentVariables]:
    """List variables for an environment

     Find deployment environment level variables.

    Args:
        workspace (str):
        repo_slug (str):
        environment_uuid (str):

    Returns:
        Response[PaginatedDeploymentVariables]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        environment_uuid=environment_uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    client: Client,
) -> Optional[PaginatedDeploymentVariables]:
    """List variables for an environment

     Find deployment environment level variables.

    Args:
        workspace (str):
        repo_slug (str):
        environment_uuid (str):

    Returns:
        Response[PaginatedDeploymentVariables]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            environment_uuid=environment_uuid,
            client=client,
        )
    ).parsed
