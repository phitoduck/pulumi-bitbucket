from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.webhook_subscription import WebhookSubscription
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    uid: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/hooks/{uid}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, uid=uid
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, WebhookSubscription]]:
    if response.status_code == 200:
        response_200 = WebhookSubscription.from_dict(response.json())

        return response_200
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
    repo_slug: str,
    uid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, WebhookSubscription]]:
    """Update a webhook for a repository

     Updates the specified webhook subscription.

    The following properties can be mutated:

    * `description`
    * `url`
    * `active`
    * `events`

    Args:
        workspace (str):
        repo_slug (str):
        uid (str):

    Returns:
        Response[Union[Error, WebhookSubscription]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        uid=uid,
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
    uid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, WebhookSubscription]]:
    """Update a webhook for a repository

     Updates the specified webhook subscription.

    The following properties can be mutated:

    * `description`
    * `url`
    * `active`
    * `events`

    Args:
        workspace (str):
        repo_slug (str):
        uid (str):

    Returns:
        Response[Union[Error, WebhookSubscription]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        uid=uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    uid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, WebhookSubscription]]:
    """Update a webhook for a repository

     Updates the specified webhook subscription.

    The following properties can be mutated:

    * `description`
    * `url`
    * `active`
    * `events`

    Args:
        workspace (str):
        repo_slug (str):
        uid (str):

    Returns:
        Response[Union[Error, WebhookSubscription]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        uid=uid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    uid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, WebhookSubscription]]:
    """Update a webhook for a repository

     Updates the specified webhook subscription.

    The following properties can be mutated:

    * `description`
    * `url`
    * `active`
    * `events`

    Args:
        workspace (str):
        repo_slug (str):
        uid (str):

    Returns:
        Response[Union[Error, WebhookSubscription]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            uid=uid,
            client=client,
        )
    ).parsed
