from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.paginated_pipeline_variables import PaginatedPipelineVariables
from ...types import Response


def _get_kwargs(
    selected_user: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{selected_user}/pipelines_config/variables/".format(client.base_url, selected_user=selected_user)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedPipelineVariables]:
    if response.status_code == 200:
        response_200 = PaginatedPipelineVariables.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedPipelineVariables]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    selected_user: str,
    *,
    client: Client,
) -> Response[PaginatedPipelineVariables]:
    """List variables for a user

     Find user level variables.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):

    Returns:
        Response[PaginatedPipelineVariables]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    selected_user: str,
    *,
    client: Client,
) -> Optional[PaginatedPipelineVariables]:
    """List variables for a user

     Find user level variables.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):

    Returns:
        Response[PaginatedPipelineVariables]
    """

    return sync_detailed(
        selected_user=selected_user,
        client=client,
    ).parsed


async def asyncio_detailed(
    selected_user: str,
    *,
    client: Client,
) -> Response[PaginatedPipelineVariables]:
    """List variables for a user

     Find user level variables.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):

    Returns:
        Response[PaginatedPipelineVariables]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    selected_user: str,
    *,
    client: Client,
) -> Optional[PaginatedPipelineVariables]:
    """List variables for a user

     Find user level variables.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):

    Returns:
        Response[PaginatedPipelineVariables]
    """

    return (
        await asyncio_detailed(
            selected_user=selected_user,
            client=client,
        )
    ).parsed
