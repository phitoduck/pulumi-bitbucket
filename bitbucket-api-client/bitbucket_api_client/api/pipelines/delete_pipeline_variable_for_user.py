from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    selected_user: str,
    variable_uuid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{selected_user}/pipelines_config/variables/{variable_uuid}".format(
        client.base_url, selected_user=selected_user, variable_uuid=variable_uuid
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    selected_user: str,
    variable_uuid: str,
    *,
    client: Client,
) -> Response[Union[Any, Error]]:
    """Delete a variable for a user

     Delete an account level variable.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):
        variable_uuid (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        variable_uuid=variable_uuid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    selected_user: str,
    variable_uuid: str,
    *,
    client: Client,
) -> Optional[Union[Any, Error]]:
    """Delete a variable for a user

     Delete an account level variable.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):
        variable_uuid (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        selected_user=selected_user,
        variable_uuid=variable_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    selected_user: str,
    variable_uuid: str,
    *,
    client: Client,
) -> Response[Union[Any, Error]]:
    """Delete a variable for a user

     Delete an account level variable.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):
        variable_uuid (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        variable_uuid=variable_uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    selected_user: str,
    variable_uuid: str,
    *,
    client: Client,
) -> Optional[Union[Any, Error]]:
    """Delete a variable for a user

     Delete an account level variable.
    This endpoint has been deprecated, and you should use the new workspaces endpoint. For more
    information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-
    teams-deprecation/).

    Args:
        selected_user (str):
        variable_uuid (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            selected_user=selected_user,
            variable_uuid=variable_uuid,
            client=client,
        )
    ).parsed