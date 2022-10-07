from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    commit: str,
    path: str,
    *,
    client: AuthenticatedClient,
    renames: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, commit=commit, path=path
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["renames"] = renames

    params["q"] = q

    params["sort"] = sort

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
    path: str,
    *,
    client: AuthenticatedClient,
    renames: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List commits that modified a file

     Returns a paginated list of commits that modified the specified file.

    Commits are returned in reverse chronological order. This is roughly
    equivalent to the following commands:

        $ git log --follow --date-order <sha> <path>

    By default, Bitbucket will follow renames and the path name in the
    returned entries reflects that. This can be turned off using the
    `?renames=false` query parameter.

    Results are returned in descending chronological order by default, and
    like most endpoints you can
    [filter and sort](/cloud/bitbucket/rest/intro/#filtering) the response to
    only provide exactly the data you want.

    For example, if you wanted to find commits made before 2011-05-18
    against a file named `README.rst`, but you only wanted the path and
    date, your query would look like this:

    ```
    $ curl 'https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/filehistory/master/README.rst'\
      '?fields=values.next,values.path,values.commit.date&q=commit.date<=2011-05-18'
    {
      \"values\": [
        {
          \"commit\": {
            \"date\": \"2011-05-17T07:32:09+00:00\"
          },
          \"path\": \"README.rst\"
        },
        {
          \"commit\": {
            \"date\": \"2011-05-16T06:33:28+00:00\"
          },
          \"path\": \"README.txt\"
        },
        {
          \"commit\": {
            \"date\": \"2011-05-16T06:15:39+00:00\"
          },
          \"path\": \"README.txt\"
        }
      ]
    }
    ```

    In the response you can see that the file was renamed to `README.rst`
    by the commit made on 2011-05-16, and was previously named `README.txt`.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        path (str):
        renames (Union[Unset, None, str]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        path=path,
        client=client,
        renames=renames,
        q=q,
        sort=sort,
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
    path: str,
    *,
    client: AuthenticatedClient,
    renames: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List commits that modified a file

     Returns a paginated list of commits that modified the specified file.

    Commits are returned in reverse chronological order. This is roughly
    equivalent to the following commands:

        $ git log --follow --date-order <sha> <path>

    By default, Bitbucket will follow renames and the path name in the
    returned entries reflects that. This can be turned off using the
    `?renames=false` query parameter.

    Results are returned in descending chronological order by default, and
    like most endpoints you can
    [filter and sort](/cloud/bitbucket/rest/intro/#filtering) the response to
    only provide exactly the data you want.

    For example, if you wanted to find commits made before 2011-05-18
    against a file named `README.rst`, but you only wanted the path and
    date, your query would look like this:

    ```
    $ curl 'https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/filehistory/master/README.rst'\
      '?fields=values.next,values.path,values.commit.date&q=commit.date<=2011-05-18'
    {
      \"values\": [
        {
          \"commit\": {
            \"date\": \"2011-05-17T07:32:09+00:00\"
          },
          \"path\": \"README.rst\"
        },
        {
          \"commit\": {
            \"date\": \"2011-05-16T06:33:28+00:00\"
          },
          \"path\": \"README.txt\"
        },
        {
          \"commit\": {
            \"date\": \"2011-05-16T06:15:39+00:00\"
          },
          \"path\": \"README.txt\"
        }
      ]
    }
    ```

    In the response you can see that the file was renamed to `README.rst`
    by the commit made on 2011-05-16, and was previously named `README.txt`.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        path (str):
        renames (Union[Unset, None, str]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        path=path,
        client=client,
        renames=renames,
        q=q,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    path: str,
    *,
    client: AuthenticatedClient,
    renames: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List commits that modified a file

     Returns a paginated list of commits that modified the specified file.

    Commits are returned in reverse chronological order. This is roughly
    equivalent to the following commands:

        $ git log --follow --date-order <sha> <path>

    By default, Bitbucket will follow renames and the path name in the
    returned entries reflects that. This can be turned off using the
    `?renames=false` query parameter.

    Results are returned in descending chronological order by default, and
    like most endpoints you can
    [filter and sort](/cloud/bitbucket/rest/intro/#filtering) the response to
    only provide exactly the data you want.

    For example, if you wanted to find commits made before 2011-05-18
    against a file named `README.rst`, but you only wanted the path and
    date, your query would look like this:

    ```
    $ curl 'https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/filehistory/master/README.rst'\
      '?fields=values.next,values.path,values.commit.date&q=commit.date<=2011-05-18'
    {
      \"values\": [
        {
          \"commit\": {
            \"date\": \"2011-05-17T07:32:09+00:00\"
          },
          \"path\": \"README.rst\"
        },
        {
          \"commit\": {
            \"date\": \"2011-05-16T06:33:28+00:00\"
          },
          \"path\": \"README.txt\"
        },
        {
          \"commit\": {
            \"date\": \"2011-05-16T06:15:39+00:00\"
          },
          \"path\": \"README.txt\"
        }
      ]
    }
    ```

    In the response you can see that the file was renamed to `README.rst`
    by the commit made on 2011-05-16, and was previously named `README.txt`.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        path (str):
        renames (Union[Unset, None, str]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        path=path,
        client=client,
        renames=renames,
        q=q,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    commit: str,
    path: str,
    *,
    client: AuthenticatedClient,
    renames: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List commits that modified a file

     Returns a paginated list of commits that modified the specified file.

    Commits are returned in reverse chronological order. This is roughly
    equivalent to the following commands:

        $ git log --follow --date-order <sha> <path>

    By default, Bitbucket will follow renames and the path name in the
    returned entries reflects that. This can be turned off using the
    `?renames=false` query parameter.

    Results are returned in descending chronological order by default, and
    like most endpoints you can
    [filter and sort](/cloud/bitbucket/rest/intro/#filtering) the response to
    only provide exactly the data you want.

    For example, if you wanted to find commits made before 2011-05-18
    against a file named `README.rst`, but you only wanted the path and
    date, your query would look like this:

    ```
    $ curl 'https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/filehistory/master/README.rst'\
      '?fields=values.next,values.path,values.commit.date&q=commit.date<=2011-05-18'
    {
      \"values\": [
        {
          \"commit\": {
            \"date\": \"2011-05-17T07:32:09+00:00\"
          },
          \"path\": \"README.rst\"
        },
        {
          \"commit\": {
            \"date\": \"2011-05-16T06:33:28+00:00\"
          },
          \"path\": \"README.txt\"
        },
        {
          \"commit\": {
            \"date\": \"2011-05-16T06:15:39+00:00\"
          },
          \"path\": \"README.txt\"
        }
      ]
    }
    ```

    In the response you can see that the file was renamed to `README.rst`
    by the commit made on 2011-05-16, and was previously named `README.txt`.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        path (str):
        renames (Union[Unset, None, str]):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            path=path,
            client=client,
            renames=renames,
            q=q,
            sort=sort,
        )
    ).parsed
