from typing import Any, Dict, Optional, Union

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
    ignore_whitespace: Union[Unset, None, bool] = UNSET,
    merge: Union[Unset, None, bool] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    renames: Union[Unset, None, bool] = UNSET,
    topic: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/diffstat/{spec}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, spec=spec
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["ignore_whitespace"] = ignore_whitespace

    params["merge"] = merge

    params["path"] = path

    params["renames"] = renames

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


def _parse_response(*, response: httpx.Response) -> Optional[Error]:
    if response.status_code == 555:
        response_555 = Error.from_dict(response.json())

        return response_555
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
    spec: str,
    *,
    client: AuthenticatedClient,
    ignore_whitespace: Union[Unset, None, bool] = UNSET,
    merge: Union[Unset, None, bool] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    renames: Union[Unset, None, bool] = UNSET,
    topic: Union[Unset, None, bool] = UNSET,
) -> Response[Error]:
    """Compare two commit diff stats

     Produces a response in JSON format with a record for every path
    modified, including information on the type of the change and the
    number of lines added and removed.

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

    #### Sample output
    ```
    curl https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/diffstat/d222fa2..e174964
    {
        \"pagelen\": 500,
        \"values\": [
            {
                \"type\": \"diffstat\",
                \"status\": \"modified\",
                \"lines_removed\": 1,
                \"lines_added\": 2,
                \"old\": {
                    \"path\": \"setup.py\",
                    \"escaped_path\": \"setup.py\",
                    \"type\": \"commit_file\",
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/
    e1749643d655d7c7014001a6c0f58abaf42ad850/setup.py\"
                        }
                    }
                },
                \"new\": {
                    \"path\": \"setup.py\",
                    \"escaped_path\": \"setup.py\",
                    \"type\": \"commit_file\",
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/
    d222fa235229c55dad20b190b0b571adf737d5a6/setup.py\"
                        }
                    }
                }
            }
        ],
        \"page\": 1,
        \"size\": 1
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):
        ignore_whitespace (Union[Unset, None, bool]):
        merge (Union[Unset, None, bool]):
        path (Union[Unset, None, str]):
        renames (Union[Unset, None, bool]):
        topic (Union[Unset, None, bool]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        spec=spec,
        client=client,
        ignore_whitespace=ignore_whitespace,
        merge=merge,
        path=path,
        renames=renames,
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
    ignore_whitespace: Union[Unset, None, bool] = UNSET,
    merge: Union[Unset, None, bool] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    renames: Union[Unset, None, bool] = UNSET,
    topic: Union[Unset, None, bool] = UNSET,
) -> Optional[Error]:
    """Compare two commit diff stats

     Produces a response in JSON format with a record for every path
    modified, including information on the type of the change and the
    number of lines added and removed.

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

    #### Sample output
    ```
    curl https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/diffstat/d222fa2..e174964
    {
        \"pagelen\": 500,
        \"values\": [
            {
                \"type\": \"diffstat\",
                \"status\": \"modified\",
                \"lines_removed\": 1,
                \"lines_added\": 2,
                \"old\": {
                    \"path\": \"setup.py\",
                    \"escaped_path\": \"setup.py\",
                    \"type\": \"commit_file\",
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/
    e1749643d655d7c7014001a6c0f58abaf42ad850/setup.py\"
                        }
                    }
                },
                \"new\": {
                    \"path\": \"setup.py\",
                    \"escaped_path\": \"setup.py\",
                    \"type\": \"commit_file\",
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/
    d222fa235229c55dad20b190b0b571adf737d5a6/setup.py\"
                        }
                    }
                }
            }
        ],
        \"page\": 1,
        \"size\": 1
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):
        ignore_whitespace (Union[Unset, None, bool]):
        merge (Union[Unset, None, bool]):
        path (Union[Unset, None, str]):
        renames (Union[Unset, None, bool]):
        topic (Union[Unset, None, bool]):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        spec=spec,
        client=client,
        ignore_whitespace=ignore_whitespace,
        merge=merge,
        path=path,
        renames=renames,
        topic=topic,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    spec: str,
    *,
    client: AuthenticatedClient,
    ignore_whitespace: Union[Unset, None, bool] = UNSET,
    merge: Union[Unset, None, bool] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    renames: Union[Unset, None, bool] = UNSET,
    topic: Union[Unset, None, bool] = UNSET,
) -> Response[Error]:
    """Compare two commit diff stats

     Produces a response in JSON format with a record for every path
    modified, including information on the type of the change and the
    number of lines added and removed.

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

    #### Sample output
    ```
    curl https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/diffstat/d222fa2..e174964
    {
        \"pagelen\": 500,
        \"values\": [
            {
                \"type\": \"diffstat\",
                \"status\": \"modified\",
                \"lines_removed\": 1,
                \"lines_added\": 2,
                \"old\": {
                    \"path\": \"setup.py\",
                    \"escaped_path\": \"setup.py\",
                    \"type\": \"commit_file\",
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/
    e1749643d655d7c7014001a6c0f58abaf42ad850/setup.py\"
                        }
                    }
                },
                \"new\": {
                    \"path\": \"setup.py\",
                    \"escaped_path\": \"setup.py\",
                    \"type\": \"commit_file\",
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/
    d222fa235229c55dad20b190b0b571adf737d5a6/setup.py\"
                        }
                    }
                }
            }
        ],
        \"page\": 1,
        \"size\": 1
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):
        ignore_whitespace (Union[Unset, None, bool]):
        merge (Union[Unset, None, bool]):
        path (Union[Unset, None, str]):
        renames (Union[Unset, None, bool]):
        topic (Union[Unset, None, bool]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        spec=spec,
        client=client,
        ignore_whitespace=ignore_whitespace,
        merge=merge,
        path=path,
        renames=renames,
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
    ignore_whitespace: Union[Unset, None, bool] = UNSET,
    merge: Union[Unset, None, bool] = UNSET,
    path: Union[Unset, None, str] = UNSET,
    renames: Union[Unset, None, bool] = UNSET,
    topic: Union[Unset, None, bool] = UNSET,
) -> Optional[Error]:
    """Compare two commit diff stats

     Produces a response in JSON format with a record for every path
    modified, including information on the type of the change and the
    number of lines added and removed.

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

    #### Sample output
    ```
    curl https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/diffstat/d222fa2..e174964
    {
        \"pagelen\": 500,
        \"values\": [
            {
                \"type\": \"diffstat\",
                \"status\": \"modified\",
                \"lines_removed\": 1,
                \"lines_added\": 2,
                \"old\": {
                    \"path\": \"setup.py\",
                    \"escaped_path\": \"setup.py\",
                    \"type\": \"commit_file\",
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/
    e1749643d655d7c7014001a6c0f58abaf42ad850/setup.py\"
                        }
                    }
                },
                \"new\": {
                    \"path\": \"setup.py\",
                    \"escaped_path\": \"setup.py\",
                    \"type\": \"commit_file\",
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/
    d222fa235229c55dad20b190b0b571adf737d5a6/setup.py\"
                        }
                    }
                }
            }
        ],
        \"page\": 1,
        \"size\": 1
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        spec (str):
        ignore_whitespace (Union[Unset, None, bool]):
        merge (Union[Unset, None, bool]):
        path (Union[Unset, None, str]):
        renames (Union[Unset, None, bool]):
        topic (Union[Unset, None, bool]):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            spec=spec,
            client=client,
            ignore_whitespace=ignore_whitespace,
            merge=merge,
            path=path,
            renames=renames,
            topic=topic,
        )
    ).parsed
