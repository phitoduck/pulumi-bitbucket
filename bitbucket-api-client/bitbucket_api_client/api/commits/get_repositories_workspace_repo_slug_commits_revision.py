from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    revision: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/commits/{revision}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, revision=revision
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
    revision: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """List commits for revision

     These are the repository's commits. They are paginated and returned
    in reverse chronological order, similar to the output of `git log`.
    Like these tools, the DAG can be filtered.

    #### GET /repositories/{workspace}/{repo_slug}/commits/master

    Returns all commits on rev `master` (similar to `git log master`).

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?include=foo&exclude=master

    Returns all commits on ref `dev` or `foo`, except those that are reachable on
    `master` (similar to `git log dev foo ^master`).

    An optional `path` parameter can be specified that will limit the
    results to commits that affect that path. `path` can either be a file
    or a directory. If a directory is specified, commits are returned that
    have modified any file in the directory tree rooted by `path`. It is
    important to note that if the `path` parameter is specified, the commits
    returned by this endpoint may no longer be a DAG, parent commits that
    do not modify the path will be omitted from the response.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=README.md&include=foo&include=bar&ex
    clude=master

    Returns all commits that are on refs `dev` or `foo` or `bar`, but not on `master`
    that changed the file README.md.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=src/&include=foo&exclude=master

    Returns all commits that are on refs `dev` or `foo`, but not on `master`
    that changed to a file in any file in the directory src or its children.

    Because the response could include a very large number of commits, it
    is paginated. Follow the 'next' link in the response to navigate to the
    next page of commits. As with other paginated resources, do not
    construct your own links.

    When the include and exclude parameters are more than can fit in a
    query string, clients can use a `x-www-form-urlencoded` POST instead.

    Args:
        workspace (str):
        repo_slug (str):
        revision (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        revision=revision,
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
    revision: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """List commits for revision

     These are the repository's commits. They are paginated and returned
    in reverse chronological order, similar to the output of `git log`.
    Like these tools, the DAG can be filtered.

    #### GET /repositories/{workspace}/{repo_slug}/commits/master

    Returns all commits on rev `master` (similar to `git log master`).

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?include=foo&exclude=master

    Returns all commits on ref `dev` or `foo`, except those that are reachable on
    `master` (similar to `git log dev foo ^master`).

    An optional `path` parameter can be specified that will limit the
    results to commits that affect that path. `path` can either be a file
    or a directory. If a directory is specified, commits are returned that
    have modified any file in the directory tree rooted by `path`. It is
    important to note that if the `path` parameter is specified, the commits
    returned by this endpoint may no longer be a DAG, parent commits that
    do not modify the path will be omitted from the response.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=README.md&include=foo&include=bar&ex
    clude=master

    Returns all commits that are on refs `dev` or `foo` or `bar`, but not on `master`
    that changed the file README.md.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=src/&include=foo&exclude=master

    Returns all commits that are on refs `dev` or `foo`, but not on `master`
    that changed to a file in any file in the directory src or its children.

    Because the response could include a very large number of commits, it
    is paginated. Follow the 'next' link in the response to navigate to the
    next page of commits. As with other paginated resources, do not
    construct your own links.

    When the include and exclude parameters are more than can fit in a
    query string, clients can use a `x-www-form-urlencoded` POST instead.

    Args:
        workspace (str):
        repo_slug (str):
        revision (str):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        revision=revision,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    revision: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """List commits for revision

     These are the repository's commits. They are paginated and returned
    in reverse chronological order, similar to the output of `git log`.
    Like these tools, the DAG can be filtered.

    #### GET /repositories/{workspace}/{repo_slug}/commits/master

    Returns all commits on rev `master` (similar to `git log master`).

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?include=foo&exclude=master

    Returns all commits on ref `dev` or `foo`, except those that are reachable on
    `master` (similar to `git log dev foo ^master`).

    An optional `path` parameter can be specified that will limit the
    results to commits that affect that path. `path` can either be a file
    or a directory. If a directory is specified, commits are returned that
    have modified any file in the directory tree rooted by `path`. It is
    important to note that if the `path` parameter is specified, the commits
    returned by this endpoint may no longer be a DAG, parent commits that
    do not modify the path will be omitted from the response.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=README.md&include=foo&include=bar&ex
    clude=master

    Returns all commits that are on refs `dev` or `foo` or `bar`, but not on `master`
    that changed the file README.md.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=src/&include=foo&exclude=master

    Returns all commits that are on refs `dev` or `foo`, but not on `master`
    that changed to a file in any file in the directory src or its children.

    Because the response could include a very large number of commits, it
    is paginated. Follow the 'next' link in the response to navigate to the
    next page of commits. As with other paginated resources, do not
    construct your own links.

    When the include and exclude parameters are more than can fit in a
    query string, clients can use a `x-www-form-urlencoded` POST instead.

    Args:
        workspace (str):
        repo_slug (str):
        revision (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        revision=revision,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    revision: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """List commits for revision

     These are the repository's commits. They are paginated and returned
    in reverse chronological order, similar to the output of `git log`.
    Like these tools, the DAG can be filtered.

    #### GET /repositories/{workspace}/{repo_slug}/commits/master

    Returns all commits on rev `master` (similar to `git log master`).

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?include=foo&exclude=master

    Returns all commits on ref `dev` or `foo`, except those that are reachable on
    `master` (similar to `git log dev foo ^master`).

    An optional `path` parameter can be specified that will limit the
    results to commits that affect that path. `path` can either be a file
    or a directory. If a directory is specified, commits are returned that
    have modified any file in the directory tree rooted by `path`. It is
    important to note that if the `path` parameter is specified, the commits
    returned by this endpoint may no longer be a DAG, parent commits that
    do not modify the path will be omitted from the response.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=README.md&include=foo&include=bar&ex
    clude=master

    Returns all commits that are on refs `dev` or `foo` or `bar`, but not on `master`
    that changed the file README.md.

    #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=src/&include=foo&exclude=master

    Returns all commits that are on refs `dev` or `foo`, but not on `master`
    that changed to a file in any file in the directory src or its children.

    Because the response could include a very large number of commits, it
    is paginated. Follow the 'next' link in the response to navigate to the
    next page of commits. As with other paginated resources, do not
    construct your own links.

    When the include and exclude parameters are more than can fit in a
    query string, clients can use a `x-www-form-urlencoded` POST instead.

    Args:
        workspace (str):
        repo_slug (str):
        revision (str):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            revision=revision,
            client=client,
        )
    ).parsed
