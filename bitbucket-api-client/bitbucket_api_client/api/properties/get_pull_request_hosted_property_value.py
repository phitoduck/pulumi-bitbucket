from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.application_property import ApplicationProperty
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    pullrequest_id: str,
    app_key: str,
    property_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name}".format(
        client.base_url,
        workspace=workspace,
        repo_slug=repo_slug,
        pullrequest_id=pullrequest_id,
        app_key=app_key,
        property_name=property_name,
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


def _parse_response(*, response: httpx.Response) -> Optional[ApplicationProperty]:
    if response.status_code == 200:
        response_200 = ApplicationProperty.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ApplicationProperty]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    pullrequest_id: str,
    app_key: str,
    property_name: str,
    *,
    client: Client,
) -> Response[ApplicationProperty]:
    """Get a pull request application property

     Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a
    pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pullrequest_id (str):
        app_key (str):
        property_name (str):

    Returns:
        Response[ApplicationProperty]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pullrequest_id=pullrequest_id,
        app_key=app_key,
        property_name=property_name,
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
    pullrequest_id: str,
    app_key: str,
    property_name: str,
    *,
    client: Client,
) -> Optional[ApplicationProperty]:
    """Get a pull request application property

     Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a
    pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pullrequest_id (str):
        app_key (str):
        property_name (str):

    Returns:
        Response[ApplicationProperty]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        pullrequest_id=pullrequest_id,
        app_key=app_key,
        property_name=property_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    pullrequest_id: str,
    app_key: str,
    property_name: str,
    *,
    client: Client,
) -> Response[ApplicationProperty]:
    """Get a pull request application property

     Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a
    pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pullrequest_id (str):
        app_key (str):
        property_name (str):

    Returns:
        Response[ApplicationProperty]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pullrequest_id=pullrequest_id,
        app_key=app_key,
        property_name=property_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    pullrequest_id: str,
    app_key: str,
    property_name: str,
    *,
    client: Client,
) -> Optional[ApplicationProperty]:
    """Get a pull request application property

     Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a
    pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pullrequest_id (str):
        app_key (str):
        property_name (str):

    Returns:
        Response[ApplicationProperty]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            pullrequest_id=pullrequest_id,
            app_key=app_key,
            property_name=property_name,
            client=client,
        )
    ).parsed
