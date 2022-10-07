from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.get_hook_events_subject_type_subject_type import GetHookEventsSubjectTypeSubjectType
from ...models.paginated_hook_events import PaginatedHookEvents
from ...types import Response


def _get_kwargs(
    subject_type: GetHookEventsSubjectTypeSubjectType,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/hook_events/{subject_type}".format(client.base_url, subject_type=subject_type)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, PaginatedHookEvents]]:
    if response.status_code == 200:
        response_200 = PaginatedHookEvents.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, PaginatedHookEvents]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    subject_type: GetHookEventsSubjectTypeSubjectType,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, PaginatedHookEvents]]:
    """List subscribable webhook types

     Returns a paginated list of all valid webhook events for the
    specified entity.
    **The team and user webhooks are deprecated, and you should use workspace instead.
    For more information, see [the
    announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).**

    This is public data that does not require any scopes or authentication.

    Example:

    NOTE: The following example is a truncated response object for the `workspace` `subject_type`.
    We return the same structure for the other `subject_type` objects.

    ```
    $ curl https://api.bitbucket.org/2.0/hook_events/workspace
    {
        \"page\": 1,
        \"pagelen\": 30,
        \"size\": 21,
        \"values\": [
            {
                \"category\": \"Repository\",
                \"description\": \"Whenever a repository push occurs\",
                \"event\": \"repo:push\",
                \"label\": \"Push\"
            },
            {
                \"category\": \"Repository\",
                \"description\": \"Whenever a repository fork occurs\",
                \"event\": \"repo:fork\",
                \"label\": \"Fork\"
            },
            {
                \"category\": \"Repository\",
                \"description\": \"Whenever a repository import occurs\",
                \"event\": \"repo:imported\",
                \"label\": \"Import\"
            },
            ...
            {
                \"category\":\"Pull Request\",
                \"label\":\"Approved\",
                \"description\":\"When someone has approved a pull request\",
                \"event\":\"pullrequest:approved\"
            },
        ]
    }
    ```

    Args:
        subject_type (GetHookEventsSubjectTypeSubjectType):

    Returns:
        Response[Union[Error, PaginatedHookEvents]]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    subject_type: GetHookEventsSubjectTypeSubjectType,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, PaginatedHookEvents]]:
    """List subscribable webhook types

     Returns a paginated list of all valid webhook events for the
    specified entity.
    **The team and user webhooks are deprecated, and you should use workspace instead.
    For more information, see [the
    announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).**

    This is public data that does not require any scopes or authentication.

    Example:

    NOTE: The following example is a truncated response object for the `workspace` `subject_type`.
    We return the same structure for the other `subject_type` objects.

    ```
    $ curl https://api.bitbucket.org/2.0/hook_events/workspace
    {
        \"page\": 1,
        \"pagelen\": 30,
        \"size\": 21,
        \"values\": [
            {
                \"category\": \"Repository\",
                \"description\": \"Whenever a repository push occurs\",
                \"event\": \"repo:push\",
                \"label\": \"Push\"
            },
            {
                \"category\": \"Repository\",
                \"description\": \"Whenever a repository fork occurs\",
                \"event\": \"repo:fork\",
                \"label\": \"Fork\"
            },
            {
                \"category\": \"Repository\",
                \"description\": \"Whenever a repository import occurs\",
                \"event\": \"repo:imported\",
                \"label\": \"Import\"
            },
            ...
            {
                \"category\":\"Pull Request\",
                \"label\":\"Approved\",
                \"description\":\"When someone has approved a pull request\",
                \"event\":\"pullrequest:approved\"
            },
        ]
    }
    ```

    Args:
        subject_type (GetHookEventsSubjectTypeSubjectType):

    Returns:
        Response[Union[Error, PaginatedHookEvents]]
    """

    return sync_detailed(
        subject_type=subject_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    subject_type: GetHookEventsSubjectTypeSubjectType,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, PaginatedHookEvents]]:
    """List subscribable webhook types

     Returns a paginated list of all valid webhook events for the
    specified entity.
    **The team and user webhooks are deprecated, and you should use workspace instead.
    For more information, see [the
    announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).**

    This is public data that does not require any scopes or authentication.

    Example:

    NOTE: The following example is a truncated response object for the `workspace` `subject_type`.
    We return the same structure for the other `subject_type` objects.

    ```
    $ curl https://api.bitbucket.org/2.0/hook_events/workspace
    {
        \"page\": 1,
        \"pagelen\": 30,
        \"size\": 21,
        \"values\": [
            {
                \"category\": \"Repository\",
                \"description\": \"Whenever a repository push occurs\",
                \"event\": \"repo:push\",
                \"label\": \"Push\"
            },
            {
                \"category\": \"Repository\",
                \"description\": \"Whenever a repository fork occurs\",
                \"event\": \"repo:fork\",
                \"label\": \"Fork\"
            },
            {
                \"category\": \"Repository\",
                \"description\": \"Whenever a repository import occurs\",
                \"event\": \"repo:imported\",
                \"label\": \"Import\"
            },
            ...
            {
                \"category\":\"Pull Request\",
                \"label\":\"Approved\",
                \"description\":\"When someone has approved a pull request\",
                \"event\":\"pullrequest:approved\"
            },
        ]
    }
    ```

    Args:
        subject_type (GetHookEventsSubjectTypeSubjectType):

    Returns:
        Response[Union[Error, PaginatedHookEvents]]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    subject_type: GetHookEventsSubjectTypeSubjectType,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, PaginatedHookEvents]]:
    """List subscribable webhook types

     Returns a paginated list of all valid webhook events for the
    specified entity.
    **The team and user webhooks are deprecated, and you should use workspace instead.
    For more information, see [the
    announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).**

    This is public data that does not require any scopes or authentication.

    Example:

    NOTE: The following example is a truncated response object for the `workspace` `subject_type`.
    We return the same structure for the other `subject_type` objects.

    ```
    $ curl https://api.bitbucket.org/2.0/hook_events/workspace
    {
        \"page\": 1,
        \"pagelen\": 30,
        \"size\": 21,
        \"values\": [
            {
                \"category\": \"Repository\",
                \"description\": \"Whenever a repository push occurs\",
                \"event\": \"repo:push\",
                \"label\": \"Push\"
            },
            {
                \"category\": \"Repository\",
                \"description\": \"Whenever a repository fork occurs\",
                \"event\": \"repo:fork\",
                \"label\": \"Fork\"
            },
            {
                \"category\": \"Repository\",
                \"description\": \"Whenever a repository import occurs\",
                \"event\": \"repo:imported\",
                \"label\": \"Import\"
            },
            ...
            {
                \"category\":\"Pull Request\",
                \"label\":\"Approved\",
                \"description\":\"When someone has approved a pull request\",
                \"event\":\"pullrequest:approved\"
            },
        ]
    }
    ```

    Args:
        subject_type (GetHookEventsSubjectTypeSubjectType):

    Returns:
        Response[Union[Error, PaginatedHookEvents]]
    """

    return (
        await asyncio_detailed(
            subject_type=subject_type,
            client=client,
        )
    ).parsed
