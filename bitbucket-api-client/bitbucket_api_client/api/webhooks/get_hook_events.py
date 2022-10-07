from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.subject_types import SubjectTypes
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/hook_events".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[SubjectTypes]:
    if response.status_code == 200:
        response_200 = SubjectTypes.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SubjectTypes]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[SubjectTypes]:
    """Get a webhook resource

     Returns the webhook resource or subject types on which webhooks can
    be registered.

    Each resource/subject type contains an `events` link that returns the
    paginated list of specific events each individual subject type can
    emit.

    This endpoint is publicly accessible and does not require
    authentication or scopes.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/hook_events

    {
        \"repository\": {
            \"links\": {
                \"events\": {
                    \"href\": \"https://api.bitbucket.org/2.0/hook_events/repository\"
                }
            }
        },
        \"workspace\": {
            \"links\": {
                \"events\": {
                    \"href\": \"https://api.bitbucket.org/2.0/hook_events/workspace\"
                }
            }
        }
    }
    ```

    Returns:
        Response[SubjectTypes]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[SubjectTypes]:
    """Get a webhook resource

     Returns the webhook resource or subject types on which webhooks can
    be registered.

    Each resource/subject type contains an `events` link that returns the
    paginated list of specific events each individual subject type can
    emit.

    This endpoint is publicly accessible and does not require
    authentication or scopes.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/hook_events

    {
        \"repository\": {
            \"links\": {
                \"events\": {
                    \"href\": \"https://api.bitbucket.org/2.0/hook_events/repository\"
                }
            }
        },
        \"workspace\": {
            \"links\": {
                \"events\": {
                    \"href\": \"https://api.bitbucket.org/2.0/hook_events/workspace\"
                }
            }
        }
    }
    ```

    Returns:
        Response[SubjectTypes]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[SubjectTypes]:
    """Get a webhook resource

     Returns the webhook resource or subject types on which webhooks can
    be registered.

    Each resource/subject type contains an `events` link that returns the
    paginated list of specific events each individual subject type can
    emit.

    This endpoint is publicly accessible and does not require
    authentication or scopes.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/hook_events

    {
        \"repository\": {
            \"links\": {
                \"events\": {
                    \"href\": \"https://api.bitbucket.org/2.0/hook_events/repository\"
                }
            }
        },
        \"workspace\": {
            \"links\": {
                \"events\": {
                    \"href\": \"https://api.bitbucket.org/2.0/hook_events/workspace\"
                }
            }
        }
    }
    ```

    Returns:
        Response[SubjectTypes]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[SubjectTypes]:
    """Get a webhook resource

     Returns the webhook resource or subject types on which webhooks can
    be registered.

    Each resource/subject type contains an `events` link that returns the
    paginated list of specific events each individual subject type can
    emit.

    This endpoint is publicly accessible and does not require
    authentication or scopes.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/hook_events

    {
        \"repository\": {
            \"links\": {
                \"events\": {
                    \"href\": \"https://api.bitbucket.org/2.0/hook_events/repository\"
                }
            }
        },
        \"workspace\": {
            \"links\": {
                \"events\": {
                    \"href\": \"https://api.bitbucket.org/2.0/hook_events/workspace\"
                }
            }
        }
    }
    ```

    Returns:
        Response[SubjectTypes]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
