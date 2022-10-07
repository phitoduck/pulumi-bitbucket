from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    kind: Union[Unset, None, str] = UNSET,
    pattern: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/branch-restrictions".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["kind"] = kind

    params["pattern"] = pattern

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
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
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
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    kind: Union[Unset, None, str] = UNSET,
    pattern: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List branch restrictions

     Returns a paginated list of all branch restrictions on the
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        kind (Union[Unset, None, str]):
        pattern (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        kind=kind,
        pattern=pattern,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    kind: Union[Unset, None, str] = UNSET,
    pattern: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List branch restrictions

     Returns a paginated list of all branch restrictions on the
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        kind (Union[Unset, None, str]):
        pattern (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        kind=kind,
        pattern=pattern,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    kind: Union[Unset, None, str] = UNSET,
    pattern: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List branch restrictions

     Returns a paginated list of all branch restrictions on the
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        kind (Union[Unset, None, str]):
        pattern (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        kind=kind,
        pattern=pattern,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    kind: Union[Unset, None, str] = UNSET,
    pattern: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List branch restrictions

     Returns a paginated list of all branch restrictions on the
    repository.

    Args:
        workspace (str):
        repo_slug (str):
        kind (Union[Unset, None, str]):
        pattern (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            kind=kind,
            pattern=pattern,
        )
    ).parsed
