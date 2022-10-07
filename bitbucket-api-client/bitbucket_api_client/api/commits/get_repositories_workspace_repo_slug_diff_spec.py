from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    client: AuthenticatedClient,
    context: Union[Unset, None, int] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    ignore_whitespace: Union[Unset, None, bool] = UNSET,
    binary: Union[Unset, None, bool] = UNSET,
    renames: Union[Unset, None, bool] = UNSET,
    merge: Union[Unset, None, bool] = UNSET,
    topic: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/diff/{spec}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, spec=spec
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["context"] = context

    params["path"] = path

    params["ignore_whitespace"] = ignore_whitespace

    params["binary"] = binary

    params["renames"] = renames

    params["merge"] = merge

    params["topic"] = topic

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
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
    context: Union[Unset, None, int] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    ignore_whitespace: Union[Unset, None, bool] = UNSET,
    binary: Union[Unset, None, bool] = UNSET,
    renames: Union[Unset, None, bool] = UNSET,
    merge: Union[Unset, None, bool] = UNSET,
    topic: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, Error]]:
    """Compare two commits

     Produces a raw git-style diff.

    #### Single commit spec

    If the `spec` argument to this API is a single commit, the diff is
    produced against the first parent of the specified commit.

    #### Two commit spec

    Two commits separated by `..` may be provided as the `spec`, e.g.,
    `3a8b42..9ff173`. When two commits are provided and the `topic` query
    parameter is true or absent, this API produces a 2-way three dot diff.
    This is the diff between source commit and the merge base of the source
    commit and the destination commit. When the `topic` query param is false,
    a simple git-style diff is produced.

    The two commits are interpreted as follows:

    * First commit: the commit containing the changes we wish to preview
    * Second commit: the commit representing the state to which we want to
      compare the first commit
    * **Note**: This is the opposite of the order used in `git diff`.

    #### Comparison to patches

    While similar to patches, diffs:

    * Don't have a commit header (username, commit message, etc)
    * Support the optional `path=foo/bar.py` query param to filter
      the diff to just that one file diff

    #### Response

    The raw diff is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):
        context (Union[Unset, None, int]):
        path (Union[Unset, None, str]):
        ignore_whitespace (Union[Unset, None, bool]):
        binary (Union[Unset, None, bool]):
        renames (Union[Unset, None, bool]):
        merge (Union[Unset, None, bool]):
        topic (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        spec=spec,
        client=client,
        context=context,
        path=path,
        ignore_whitespace=ignore_whitespace,
        binary=binary,
        renames=renames,
        merge=merge,
        topic=topic,
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
    context: Union[Unset, None, int] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    ignore_whitespace: Union[Unset, None, bool] = UNSET,
    binary: Union[Unset, None, bool] = UNSET,
    renames: Union[Unset, None, bool] = UNSET,
    merge: Union[Unset, None, bool] = UNSET,
    topic: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, Error]]:
    """Compare two commits

     Produces a raw git-style diff.

    #### Single commit spec

    If the `spec` argument to this API is a single commit, the diff is
    produced against the first parent of the specified commit.

    #### Two commit spec

    Two commits separated by `..` may be provided as the `spec`, e.g.,
    `3a8b42..9ff173`. When two commits are provided and the `topic` query
    parameter is true or absent, this API produces a 2-way three dot diff.
    This is the diff between source commit and the merge base of the source
    commit and the destination commit. When the `topic` query param is false,
    a simple git-style diff is produced.

    The two commits are interpreted as follows:

    * First commit: the commit containing the changes we wish to preview
    * Second commit: the commit representing the state to which we want to
      compare the first commit
    * **Note**: This is the opposite of the order used in `git diff`.

    #### Comparison to patches

    While similar to patches, diffs:

    * Don't have a commit header (username, commit message, etc)
    * Support the optional `path=foo/bar.py` query param to filter
      the diff to just that one file diff

    #### Response

    The raw diff is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):
        context (Union[Unset, None, int]):
        path (Union[Unset, None, str]):
        ignore_whitespace (Union[Unset, None, bool]):
        binary (Union[Unset, None, bool]):
        renames (Union[Unset, None, bool]):
        merge (Union[Unset, None, bool]):
        topic (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        spec=spec,
        client=client,
        context=context,
        path=path,
        ignore_whitespace=ignore_whitespace,
        binary=binary,
        renames=renames,
        merge=merge,
        topic=topic,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    client: AuthenticatedClient,
    context: Union[Unset, None, int] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    ignore_whitespace: Union[Unset, None, bool] = UNSET,
    binary: Union[Unset, None, bool] = UNSET,
    renames: Union[Unset, None, bool] = UNSET,
    merge: Union[Unset, None, bool] = UNSET,
    topic: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, Error]]:
    """Compare two commits

     Produces a raw git-style diff.

    #### Single commit spec

    If the `spec` argument to this API is a single commit, the diff is
    produced against the first parent of the specified commit.

    #### Two commit spec

    Two commits separated by `..` may be provided as the `spec`, e.g.,
    `3a8b42..9ff173`. When two commits are provided and the `topic` query
    parameter is true or absent, this API produces a 2-way three dot diff.
    This is the diff between source commit and the merge base of the source
    commit and the destination commit. When the `topic` query param is false,
    a simple git-style diff is produced.

    The two commits are interpreted as follows:

    * First commit: the commit containing the changes we wish to preview
    * Second commit: the commit representing the state to which we want to
      compare the first commit
    * **Note**: This is the opposite of the order used in `git diff`.

    #### Comparison to patches

    While similar to patches, diffs:

    * Don't have a commit header (username, commit message, etc)
    * Support the optional `path=foo/bar.py` query param to filter
      the diff to just that one file diff

    #### Response

    The raw diff is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):
        context (Union[Unset, None, int]):
        path (Union[Unset, None, str]):
        ignore_whitespace (Union[Unset, None, bool]):
        binary (Union[Unset, None, bool]):
        renames (Union[Unset, None, bool]):
        merge (Union[Unset, None, bool]):
        topic (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        spec=spec,
        client=client,
        context=context,
        path=path,
        ignore_whitespace=ignore_whitespace,
        binary=binary,
        renames=renames,
        merge=merge,
        topic=topic,
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
    context: Union[Unset, None, int] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    ignore_whitespace: Union[Unset, None, bool] = UNSET,
    binary: Union[Unset, None, bool] = UNSET,
    renames: Union[Unset, None, bool] = UNSET,
    merge: Union[Unset, None, bool] = UNSET,
    topic: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, Error]]:
    """Compare two commits

     Produces a raw git-style diff.

    #### Single commit spec

    If the `spec` argument to this API is a single commit, the diff is
    produced against the first parent of the specified commit.

    #### Two commit spec

    Two commits separated by `..` may be provided as the `spec`, e.g.,
    `3a8b42..9ff173`. When two commits are provided and the `topic` query
    parameter is true or absent, this API produces a 2-way three dot diff.
    This is the diff between source commit and the merge base of the source
    commit and the destination commit. When the `topic` query param is false,
    a simple git-style diff is produced.

    The two commits are interpreted as follows:

    * First commit: the commit containing the changes we wish to preview
    * Second commit: the commit representing the state to which we want to
      compare the first commit
    * **Note**: This is the opposite of the order used in `git diff`.

    #### Comparison to patches

    While similar to patches, diffs:

    * Don't have a commit header (username, commit message, etc)
    * Support the optional `path=foo/bar.py` query param to filter
      the diff to just that one file diff

    #### Response

    The raw diff is returned as-is, in whatever encoding the files in the
    repository use. It is not decoded into unicode. As such, the
    content-type is `text/plain`.

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):
        context (Union[Unset, None, int]):
        path (Union[Unset, None, str]):
        ignore_whitespace (Union[Unset, None, bool]):
        binary (Union[Unset, None, bool]):
        renames (Union[Unset, None, bool]):
        merge (Union[Unset, None, bool]):
        topic (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            spec=spec,
            client=client,
            context=context,
            path=path,
            ignore_whitespace=ignore_whitespace,
            binary=binary,
            renames=renames,
            merge=merge,
            topic=topic,
        )
    ).parsed
