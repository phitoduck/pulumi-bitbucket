from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.webhook_subscription import WebhookSubscription
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
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, WebhookSubscription]]:
    if response.status_code == 201:
        response_201 = WebhookSubscription.from_dict(response.json())

        return response_201
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, WebhookSubscription]]:
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
) -> Response[Union[Error, WebhookSubscription]]:
    """Create a webhook for a workspace

     Creates a new webhook on the specified workspace.

    Workspace webhooks are fired for events from all repositories contained
    by that workspace.

    Example:

    ```
    $ curl -X POST -u credentials -H 'Content-Type: application/json'
      https://api.bitbucket.org/2.0/workspaces/my-workspace/hooks
      -d '
        {
          \"description\": \"Webhook Description\",
          \"url\": \"https://example.com/\",
          \"active\": true,
          \"events\": [
            \"repo:push\",
            \"issue:created\",
            \"issue:updated\"
          ]
        }'
    ```

    This call requires the webhook scope, as well as any scope
    that applies to the events that the webhook subscribes to. In the
    example above that means: `webhook`, `repository` and `issue`.

    The `url` must properly resolve and cannot be an internal, non-routed address.

    Only workspace owners can install webhooks on workspaces.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, WebhookSubscription]]
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
) -> Optional[Union[Error, WebhookSubscription]]:
    """Create a webhook for a workspace

     Creates a new webhook on the specified workspace.

    Workspace webhooks are fired for events from all repositories contained
    by that workspace.

    Example:

    ```
    $ curl -X POST -u credentials -H 'Content-Type: application/json'
      https://api.bitbucket.org/2.0/workspaces/my-workspace/hooks
      -d '
        {
          \"description\": \"Webhook Description\",
          \"url\": \"https://example.com/\",
          \"active\": true,
          \"events\": [
            \"repo:push\",
            \"issue:created\",
            \"issue:updated\"
          ]
        }'
    ```

    This call requires the webhook scope, as well as any scope
    that applies to the events that the webhook subscribes to. In the
    example above that means: `webhook`, `repository` and `issue`.

    The `url` must properly resolve and cannot be an internal, non-routed address.

    Only workspace owners can install webhooks on workspaces.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, WebhookSubscription]]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, WebhookSubscription]]:
    """Create a webhook for a workspace

     Creates a new webhook on the specified workspace.

    Workspace webhooks are fired for events from all repositories contained
    by that workspace.

    Example:

    ```
    $ curl -X POST -u credentials -H 'Content-Type: application/json'
      https://api.bitbucket.org/2.0/workspaces/my-workspace/hooks
      -d '
        {
          \"description\": \"Webhook Description\",
          \"url\": \"https://example.com/\",
          \"active\": true,
          \"events\": [
            \"repo:push\",
            \"issue:created\",
            \"issue:updated\"
          ]
        }'
    ```

    This call requires the webhook scope, as well as any scope
    that applies to the events that the webhook subscribes to. In the
    example above that means: `webhook`, `repository` and `issue`.

    The `url` must properly resolve and cannot be an internal, non-routed address.

    Only workspace owners can install webhooks on workspaces.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, WebhookSubscription]]
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
) -> Optional[Union[Error, WebhookSubscription]]:
    """Create a webhook for a workspace

     Creates a new webhook on the specified workspace.

    Workspace webhooks are fired for events from all repositories contained
    by that workspace.

    Example:

    ```
    $ curl -X POST -u credentials -H 'Content-Type: application/json'
      https://api.bitbucket.org/2.0/workspaces/my-workspace/hooks
      -d '
        {
          \"description\": \"Webhook Description\",
          \"url\": \"https://example.com/\",
          \"active\": true,
          \"events\": [
            \"repo:push\",
            \"issue:created\",
            \"issue:updated\"
          ]
        }'
    ```

    This call requires the webhook scope, as well as any scope
    that applies to the events that the webhook subscribes to. In the
    example above that means: `webhook`, `repository` and `issue`.

    The `url` must properly resolve and cannot be an internal, non-routed address.

    Only workspace owners can install webhooks on workspaces.

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, WebhookSubscription]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
        )
    ).parsed
