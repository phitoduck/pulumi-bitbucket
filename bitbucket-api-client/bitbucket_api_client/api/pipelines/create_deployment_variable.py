from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.deployment_variable import DeploymentVariable
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    client: Client,
    json_body: DeploymentVariable,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, environment_uuid=environment_uuid
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[DeploymentVariable, Error]]:
    if response.status_code == 201:
        response_201 = DeploymentVariable.from_dict(response.json())

        return response_201
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DeploymentVariable, Error]]:
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
    json_body: DeploymentVariable,
) -> Response[Union[DeploymentVariable, Error]]:
    """Create a variable for an environment

     Create a deployment environment level variable.

    Args:
        workspace (str):
        repo_slug (str):
        environment_uuid (str):
        json_body (DeploymentVariable):

    Returns:
        Response[Union[DeploymentVariable, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        environment_uuid=environment_uuid,
        client=client,
        json_body=json_body,
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
    json_body: DeploymentVariable,
) -> Optional[Union[DeploymentVariable, Error]]:
    """Create a variable for an environment

     Create a deployment environment level variable.

    Args:
        workspace (str):
        repo_slug (str):
        environment_uuid (str):
        json_body (DeploymentVariable):

    Returns:
        Response[Union[DeploymentVariable, Error]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        environment_uuid=environment_uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    environment_uuid: str,
    *,
    client: Client,
    json_body: DeploymentVariable,
) -> Response[Union[DeploymentVariable, Error]]:
    """Create a variable for an environment

     Create a deployment environment level variable.

    Args:
        workspace (str):
        repo_slug (str):
        environment_uuid (str):
        json_body (DeploymentVariable):

    Returns:
        Response[Union[DeploymentVariable, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        environment_uuid=environment_uuid,
        client=client,
        json_body=json_body,
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
    json_body: DeploymentVariable,
) -> Optional[Union[DeploymentVariable, Error]]:
    """Create a variable for an environment

     Create a deployment environment level variable.

    Args:
        workspace (str):
        repo_slug (str):
        environment_uuid (str):
        json_body (DeploymentVariable):

    Returns:
        Response[Union[DeploymentVariable, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            environment_uuid=environment_uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
