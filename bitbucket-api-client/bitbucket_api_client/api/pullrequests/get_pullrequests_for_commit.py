from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    pagelen: Union[Unset, None, int] = 30,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/commit/{commit}/pullrequests".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, commit=commit
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pagelen"] = pagelen

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
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    pagelen: Union[Unset, None, int] = 30,
) -> Response[Error]:
    """List pull requests that contain a commit

     Returns a paginated list of all pull requests as part of which this commit was reviewed. Pull
    Request Commit Links app must be installed first before using this API; installation automatically
    occurs when 'Go to pull request' is clicked from the web interface for a commit's details.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        page (Union[Unset, None, int]):  Default: 1.
        pagelen (Union[Unset, None, int]):  Default: 30.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        client=client,
        page=page,
        pagelen=pagelen,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    pagelen: Union[Unset, None, int] = 30,
) -> Optional[Error]:
    """List pull requests that contain a commit

     Returns a paginated list of all pull requests as part of which this commit was reviewed. Pull
    Request Commit Links app must be installed first before using this API; installation automatically
    occurs when 'Go to pull request' is clicked from the web interface for a commit's details.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        page (Union[Unset, None, int]):  Default: 1.
        pagelen (Union[Unset, None, int]):  Default: 30.

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        client=client,
        page=page,
        pagelen=pagelen,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    pagelen: Union[Unset, None, int] = 30,
) -> Response[Error]:
    """List pull requests that contain a commit

     Returns a paginated list of all pull requests as part of which this commit was reviewed. Pull
    Request Commit Links app must be installed first before using this API; installation automatically
    occurs when 'Go to pull request' is clicked from the web interface for a commit's details.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        page (Union[Unset, None, int]):  Default: 1.
        pagelen (Union[Unset, None, int]):  Default: 30.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        client=client,
        page=page,
        pagelen=pagelen,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 1,
    pagelen: Union[Unset, None, int] = 30,
) -> Optional[Error]:
    """List pull requests that contain a commit

     Returns a paginated list of all pull requests as part of which this commit was reviewed. Pull
    Request Commit Links app must be installed first before using this API; installation automatically
    occurs when 'Go to pull request' is clicked from the web interface for a commit's details.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        page (Union[Unset, None, int]):  Default: 1.
        pagelen (Union[Unset, None, int]):  Default: 30.

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            client=client,
            page=page,
            pagelen=pagelen,
        )
    ).parsed
