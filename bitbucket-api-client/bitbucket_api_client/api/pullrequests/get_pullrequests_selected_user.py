from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.get_pullrequests_selected_user_state import GetPullrequestsSelectedUserState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    selected_user: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, None, GetPullrequestsSelectedUserState] = UNSET,
) -> Dict[str, Any]:
    url = "{}/pullrequests/{selected_user}".format(client.base_url, selected_user=selected_user)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Error]:
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Error]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    selected_user: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, None, GetPullrequestsSelectedUserState] = UNSET,
) -> Response[Error]:
    """List pull requests for a user

     Returns all pull requests authored by the specified user.

    By default only open pull requests are returned. This can be controlled
    using the `state` query parameter. To retrieve pull requests that are
    in one of multiple states, repeat the `state` parameter for each
    individual state.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        selected_user (str):
        state (Union[Unset, None, GetPullrequestsSelectedUserState]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        client=client,
        state=state,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    selected_user: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, None, GetPullrequestsSelectedUserState] = UNSET,
) -> Optional[Error]:
    """List pull requests for a user

     Returns all pull requests authored by the specified user.

    By default only open pull requests are returned. This can be controlled
    using the `state` query parameter. To retrieve pull requests that are
    in one of multiple states, repeat the `state` parameter for each
    individual state.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        selected_user (str):
        state (Union[Unset, None, GetPullrequestsSelectedUserState]):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        selected_user=selected_user,
        client=client,
        state=state,
    ).parsed


async def asyncio_detailed(
    selected_user: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, None, GetPullrequestsSelectedUserState] = UNSET,
) -> Response[Error]:
    """List pull requests for a user

     Returns all pull requests authored by the specified user.

    By default only open pull requests are returned. This can be controlled
    using the `state` query parameter. To retrieve pull requests that are
    in one of multiple states, repeat the `state` parameter for each
    individual state.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        selected_user (str):
        state (Union[Unset, None, GetPullrequestsSelectedUserState]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        client=client,
        state=state,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    selected_user: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, None, GetPullrequestsSelectedUserState] = UNSET,
) -> Optional[Error]:
    """List pull requests for a user

     Returns all pull requests authored by the specified user.

    By default only open pull requests are returned. This can be controlled
    using the `state` query parameter. To retrieve pull requests that are
    in one of multiple states, repeat the `state` parameter for each
    individual state.

    This endpoint also supports filtering and sorting of the results. See
    [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        selected_user (str):
        state (Union[Unset, None, GetPullrequestsSelectedUserState]):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            selected_user=selected_user,
            client=client,
            state=state,
        )
    ).parsed
