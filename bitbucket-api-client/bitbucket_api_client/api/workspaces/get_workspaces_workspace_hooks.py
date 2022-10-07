from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.paginated_webhook_subscriptions import PaginatedWebhookSubscriptions
from ...types import Response


def _get_kwargs(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/hooks".format(client.base_url, workspace=workspace)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, PaginatedWebhookSubscriptions]]:
    if response.status_code == 200:
        response_200 = PaginatedWebhookSubscriptions.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, PaginatedWebhookSubscriptions]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, PaginatedWebhookSubscriptions]]:
    """List webhooks for a workspace

     Returns a paginated list of webhooks installed on this workspace.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, PaginatedWebhookSubscriptions]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, PaginatedWebhookSubscriptions]]:
    """List webhooks for a workspace

     Returns a paginated list of webhooks installed on this workspace.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, PaginatedWebhookSubscriptions]]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, PaginatedWebhookSubscriptions]]:
    """List webhooks for a workspace

     Returns a paginated list of webhooks installed on this workspace.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, PaginatedWebhookSubscriptions]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, PaginatedWebhookSubscriptions]]:
    """List webhooks for a workspace

     Returns a paginated list of webhooks installed on this workspace.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, PaginatedWebhookSubscriptions]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
        )
    ).parsed
