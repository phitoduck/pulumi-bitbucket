from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/patch/{spec}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, spec=spec
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 555:
        response_555 = Error.from_dict(response.json())

        return response_555
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """Get a patch for two commits

     Produces a raw patch for a single commit (diffed against its first
    parent), or a patch-series for a revspec of 2 commits (e.g.
    `3a8b42..9ff173` where the first commit represents the source and the
    second commit the destination).

    In case of the latter (diffing a revspec), a patch series is returned
    for the commits on the source branch (`3a8b42` and its ancestors in
    our example).

    While similar to diffs, patches:

    * Have a commit header (username, commit message, etc)
    * Do not support the `path=foo/bar.py` query parameter

    The raw patch is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        spec=spec,
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
    spec: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """Get a patch for two commits

     Produces a raw patch for a single commit (diffed against its first
    parent), or a patch-series for a revspec of 2 commits (e.g.
    `3a8b42..9ff173` where the first commit represents the source and the
    second commit the destination).

    In case of the latter (diffing a revspec), a patch series is returned
    for the commits on the source branch (`3a8b42` and its ancestors in
    our example).

    While similar to diffs, patches:

    * Have a commit header (username, commit message, etc)
    * Do not support the `path=foo/bar.py` query parameter

    The raw patch is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        spec=spec,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """Get a patch for two commits

     Produces a raw patch for a single commit (diffed against its first
    parent), or a patch-series for a revspec of 2 commits (e.g.
    `3a8b42..9ff173` where the first commit represents the source and the
    second commit the destination).

    In case of the latter (diffing a revspec), a patch series is returned
    for the commits on the source branch (`3a8b42` and its ancestors in
    our example).

    While similar to diffs, patches:

    * Have a commit header (username, commit message, etc)
    * Do not support the `path=foo/bar.py` query parameter

    The raw patch is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        spec=spec,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error]]:
    """Get a patch for two commits

     Produces a raw patch for a single commit (diffed against its first
    parent), or a patch-series for a revspec of 2 commits (e.g.
    `3a8b42..9ff173` where the first commit represents the source and the
    second commit the destination).

    In case of the latter (diffing a revspec), a patch series is returned
    for the commits on the source branch (`3a8b42` and its ancestors in
    our example).

    While similar to diffs, patches:

    * Have a commit header (username, commit message, etc)
    * Do not support the `path=foo/bar.py` query parameter

    The raw patch is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            spec=spec,
            client=client,
        )
    ).parsed
