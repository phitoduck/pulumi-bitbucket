from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    client: Client,
    search_query: str,
    page: Union[Unset, None, int] = 1,
    pagelen: Union[Unset, None, int] = 10,
) -> Dict[str, Any]:
    url = "{}/teams/{username}/search/code".format(client.base_url, username=username)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["search_query"] = search_query

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
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
    return None


def _build_response(*, response: httpx.Response) -> Response[Error]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: Client,
    search_query: str,
    page: Union[Unset, None, int] = 1,
    pagelen: Union[Unset, None, int] = 10,
) -> Response[Error]:
    """Search for code in a team's repositories

     Search for code in the repositories of the specified team.

    Searching across all repositories:

    ```
    curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query=foo'
    {
      \"size\": 1,
      \"page\": 1,
      \"pagelen\": 10,
      \"query_substituted\": false,
      \"values\": [
        {
          \"type\": \"code_search_result\",
          \"content_match_count\": 2,
          \"content_matches\": [
            {
              \"lines\": [
                {
                  \"line\": 2,
                  \"segments\": []
                },
                {
                  \"line\": 3,
                  \"segments\": [
                    {
                      \"text\": \"def \"
                    },
                    {
                      \"text\": \"foo\",
                      \"match\": true
                    },
                    {
                      \"text\": \"():\"
                    }
                  ]
                },
                {
                  \"line\": 4,
                  \"segments\": [
                    {
                      \"text\": \"    print(\\"snek\\")\"
                    }
                  ]
                },
                {
                  \"line\": 5,
                  \"segments\": []
                }
              ]
            }
          ],
          \"path_matches\": [
            {
              \"text\": \"src/\"
            },
            {
              \"text\": \"foo\",
              \"match\": true
            },
            {
              \"text\": \".py\"
            }
          ],
          \"file\": {
            \"path\": \"src/foo.py\",
            \"type\": \"commit_file\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/my-
    workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\"
              }
            }
          }
        }
      ]
    }
    ```

    Note that searches can match in the file's text (`content_matches`),
    the path (`path_matches`), or both as in the example above.

    You can use the same syntax for the search query as in the UI, e.g.
    to only search within a specific repository:

    ```
    curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query=foo+repo:demo'
    # results from the \"demo\" repository
    ```

    Similar to other APIs, you can request more fields using a
    `fields` query parameter. E.g. to get some more information about
    the repository of matched files (the `%2B` is a URL-encoded `+`):

    ```
    curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code'\
         '?search_query=foo&fields=%2Bvalues.file.commit.repository'
    {
      \"size\": 1,
      \"page\": 1,
      \"pagelen\": 10,
      \"query_substituted\": false,
      \"values\": [
        {
          \"type\": \"code_search_result\",
          \"content_match_count\": 1,
          \"content_matches\": [...],
          \"path_matches\": [...],
          \"file\": {
            \"commit\": {
              \"type\": \"commit\",
              \"hash\": \"ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\",
              \"links\": {
                \"self\": {
                  \"href\": \"https://api.bitbucket.org/2.0/repositories/my-
    workspace/demo/commit/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/my-
    workspace/demo/commits/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\"
                }
              },
              \"repository\": {
                \"name\": \"demo\",
                \"type\": \"repository\",
                \"full_name\": \"my-workspace/demo\",
                \"links\": {
                  \"self\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/my-workspace/demo\"
                  },
                  \"html\": {
                    \"href\": \"https://bitbucket.org/my-workspace/demo\"
                  },
                  \"avatar\": {
                    \"href\":
    \"https://bytebucket.org/ravatar/%7B850e1749-781a-4115-9316-df39d0600e7a%7D?ts=default\"
                  }
                },
                \"uuid\": \"{850e1749-781a-4115-9316-df39d0600e7a}\"
              }
            },
            \"type\": \"commit_file\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/my-
    workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\"
              }
            },
            \"path\": \"src/foo.py\"
          }
        }
      ]
    }
    ```

    Try `fields=%2Bvalues.*.*.*.*` to get an idea what's possible.

    Args:
        username (str):
        search_query (str):
        page (Union[Unset, None, int]):  Default: 1.
        pagelen (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        search_query=search_query,
        page=page,
        pagelen=pagelen,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    username: str,
    *,
    client: Client,
    search_query: str,
    page: Union[Unset, None, int] = 1,
    pagelen: Union[Unset, None, int] = 10,
) -> Optional[Error]:
    """Search for code in a team's repositories

     Search for code in the repositories of the specified team.

    Searching across all repositories:

    ```
    curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query=foo'
    {
      \"size\": 1,
      \"page\": 1,
      \"pagelen\": 10,
      \"query_substituted\": false,
      \"values\": [
        {
          \"type\": \"code_search_result\",
          \"content_match_count\": 2,
          \"content_matches\": [
            {
              \"lines\": [
                {
                  \"line\": 2,
                  \"segments\": []
                },
                {
                  \"line\": 3,
                  \"segments\": [
                    {
                      \"text\": \"def \"
                    },
                    {
                      \"text\": \"foo\",
                      \"match\": true
                    },
                    {
                      \"text\": \"():\"
                    }
                  ]
                },
                {
                  \"line\": 4,
                  \"segments\": [
                    {
                      \"text\": \"    print(\\"snek\\")\"
                    }
                  ]
                },
                {
                  \"line\": 5,
                  \"segments\": []
                }
              ]
            }
          ],
          \"path_matches\": [
            {
              \"text\": \"src/\"
            },
            {
              \"text\": \"foo\",
              \"match\": true
            },
            {
              \"text\": \".py\"
            }
          ],
          \"file\": {
            \"path\": \"src/foo.py\",
            \"type\": \"commit_file\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/my-
    workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\"
              }
            }
          }
        }
      ]
    }
    ```

    Note that searches can match in the file's text (`content_matches`),
    the path (`path_matches`), or both as in the example above.

    You can use the same syntax for the search query as in the UI, e.g.
    to only search within a specific repository:

    ```
    curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query=foo+repo:demo'
    # results from the \"demo\" repository
    ```

    Similar to other APIs, you can request more fields using a
    `fields` query parameter. E.g. to get some more information about
    the repository of matched files (the `%2B` is a URL-encoded `+`):

    ```
    curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code'\
         '?search_query=foo&fields=%2Bvalues.file.commit.repository'
    {
      \"size\": 1,
      \"page\": 1,
      \"pagelen\": 10,
      \"query_substituted\": false,
      \"values\": [
        {
          \"type\": \"code_search_result\",
          \"content_match_count\": 1,
          \"content_matches\": [...],
          \"path_matches\": [...],
          \"file\": {
            \"commit\": {
              \"type\": \"commit\",
              \"hash\": \"ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\",
              \"links\": {
                \"self\": {
                  \"href\": \"https://api.bitbucket.org/2.0/repositories/my-
    workspace/demo/commit/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/my-
    workspace/demo/commits/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\"
                }
              },
              \"repository\": {
                \"name\": \"demo\",
                \"type\": \"repository\",
                \"full_name\": \"my-workspace/demo\",
                \"links\": {
                  \"self\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/my-workspace/demo\"
                  },
                  \"html\": {
                    \"href\": \"https://bitbucket.org/my-workspace/demo\"
                  },
                  \"avatar\": {
                    \"href\":
    \"https://bytebucket.org/ravatar/%7B850e1749-781a-4115-9316-df39d0600e7a%7D?ts=default\"
                  }
                },
                \"uuid\": \"{850e1749-781a-4115-9316-df39d0600e7a}\"
              }
            },
            \"type\": \"commit_file\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/my-
    workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\"
              }
            },
            \"path\": \"src/foo.py\"
          }
        }
      ]
    }
    ```

    Try `fields=%2Bvalues.*.*.*.*` to get an idea what's possible.

    Args:
        username (str):
        search_query (str):
        page (Union[Unset, None, int]):  Default: 1.
        pagelen (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Error]
    """

    return sync_detailed(
        username=username,
        client=client,
        search_query=search_query,
        page=page,
        pagelen=pagelen,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Client,
    search_query: str,
    page: Union[Unset, None, int] = 1,
    pagelen: Union[Unset, None, int] = 10,
) -> Response[Error]:
    """Search for code in a team's repositories

     Search for code in the repositories of the specified team.

    Searching across all repositories:

    ```
    curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query=foo'
    {
      \"size\": 1,
      \"page\": 1,
      \"pagelen\": 10,
      \"query_substituted\": false,
      \"values\": [
        {
          \"type\": \"code_search_result\",
          \"content_match_count\": 2,
          \"content_matches\": [
            {
              \"lines\": [
                {
                  \"line\": 2,
                  \"segments\": []
                },
                {
                  \"line\": 3,
                  \"segments\": [
                    {
                      \"text\": \"def \"
                    },
                    {
                      \"text\": \"foo\",
                      \"match\": true
                    },
                    {
                      \"text\": \"():\"
                    }
                  ]
                },
                {
                  \"line\": 4,
                  \"segments\": [
                    {
                      \"text\": \"    print(\\"snek\\")\"
                    }
                  ]
                },
                {
                  \"line\": 5,
                  \"segments\": []
                }
              ]
            }
          ],
          \"path_matches\": [
            {
              \"text\": \"src/\"
            },
            {
              \"text\": \"foo\",
              \"match\": true
            },
            {
              \"text\": \".py\"
            }
          ],
          \"file\": {
            \"path\": \"src/foo.py\",
            \"type\": \"commit_file\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/my-
    workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\"
              }
            }
          }
        }
      ]
    }
    ```

    Note that searches can match in the file's text (`content_matches`),
    the path (`path_matches`), or both as in the example above.

    You can use the same syntax for the search query as in the UI, e.g.
    to only search within a specific repository:

    ```
    curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query=foo+repo:demo'
    # results from the \"demo\" repository
    ```

    Similar to other APIs, you can request more fields using a
    `fields` query parameter. E.g. to get some more information about
    the repository of matched files (the `%2B` is a URL-encoded `+`):

    ```
    curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code'\
         '?search_query=foo&fields=%2Bvalues.file.commit.repository'
    {
      \"size\": 1,
      \"page\": 1,
      \"pagelen\": 10,
      \"query_substituted\": false,
      \"values\": [
        {
          \"type\": \"code_search_result\",
          \"content_match_count\": 1,
          \"content_matches\": [...],
          \"path_matches\": [...],
          \"file\": {
            \"commit\": {
              \"type\": \"commit\",
              \"hash\": \"ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\",
              \"links\": {
                \"self\": {
                  \"href\": \"https://api.bitbucket.org/2.0/repositories/my-
    workspace/demo/commit/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/my-
    workspace/demo/commits/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\"
                }
              },
              \"repository\": {
                \"name\": \"demo\",
                \"type\": \"repository\",
                \"full_name\": \"my-workspace/demo\",
                \"links\": {
                  \"self\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/my-workspace/demo\"
                  },
                  \"html\": {
                    \"href\": \"https://bitbucket.org/my-workspace/demo\"
                  },
                  \"avatar\": {
                    \"href\":
    \"https://bytebucket.org/ravatar/%7B850e1749-781a-4115-9316-df39d0600e7a%7D?ts=default\"
                  }
                },
                \"uuid\": \"{850e1749-781a-4115-9316-df39d0600e7a}\"
              }
            },
            \"type\": \"commit_file\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/my-
    workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\"
              }
            },
            \"path\": \"src/foo.py\"
          }
        }
      ]
    }
    ```

    Try `fields=%2Bvalues.*.*.*.*` to get an idea what's possible.

    Args:
        username (str):
        search_query (str):
        page (Union[Unset, None, int]):  Default: 1.
        pagelen (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        search_query=search_query,
        page=page,
        pagelen=pagelen,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    username: str,
    *,
    client: Client,
    search_query: str,
    page: Union[Unset, None, int] = 1,
    pagelen: Union[Unset, None, int] = 10,
) -> Optional[Error]:
    """Search for code in a team's repositories

     Search for code in the repositories of the specified team.

    Searching across all repositories:

    ```
    curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query=foo'
    {
      \"size\": 1,
      \"page\": 1,
      \"pagelen\": 10,
      \"query_substituted\": false,
      \"values\": [
        {
          \"type\": \"code_search_result\",
          \"content_match_count\": 2,
          \"content_matches\": [
            {
              \"lines\": [
                {
                  \"line\": 2,
                  \"segments\": []
                },
                {
                  \"line\": 3,
                  \"segments\": [
                    {
                      \"text\": \"def \"
                    },
                    {
                      \"text\": \"foo\",
                      \"match\": true
                    },
                    {
                      \"text\": \"():\"
                    }
                  ]
                },
                {
                  \"line\": 4,
                  \"segments\": [
                    {
                      \"text\": \"    print(\\"snek\\")\"
                    }
                  ]
                },
                {
                  \"line\": 5,
                  \"segments\": []
                }
              ]
            }
          ],
          \"path_matches\": [
            {
              \"text\": \"src/\"
            },
            {
              \"text\": \"foo\",
              \"match\": true
            },
            {
              \"text\": \".py\"
            }
          ],
          \"file\": {
            \"path\": \"src/foo.py\",
            \"type\": \"commit_file\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/my-
    workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\"
              }
            }
          }
        }
      ]
    }
    ```

    Note that searches can match in the file's text (`content_matches`),
    the path (`path_matches`), or both as in the example above.

    You can use the same syntax for the search query as in the UI, e.g.
    to only search within a specific repository:

    ```
    curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query=foo+repo:demo'
    # results from the \"demo\" repository
    ```

    Similar to other APIs, you can request more fields using a
    `fields` query parameter. E.g. to get some more information about
    the repository of matched files (the `%2B` is a URL-encoded `+`):

    ```
    curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code'\
         '?search_query=foo&fields=%2Bvalues.file.commit.repository'
    {
      \"size\": 1,
      \"page\": 1,
      \"pagelen\": 10,
      \"query_substituted\": false,
      \"values\": [
        {
          \"type\": \"code_search_result\",
          \"content_match_count\": 1,
          \"content_matches\": [...],
          \"path_matches\": [...],
          \"file\": {
            \"commit\": {
              \"type\": \"commit\",
              \"hash\": \"ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\",
              \"links\": {
                \"self\": {
                  \"href\": \"https://api.bitbucket.org/2.0/repositories/my-
    workspace/demo/commit/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/my-
    workspace/demo/commits/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b\"
                }
              },
              \"repository\": {
                \"name\": \"demo\",
                \"type\": \"repository\",
                \"full_name\": \"my-workspace/demo\",
                \"links\": {
                  \"self\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/my-workspace/demo\"
                  },
                  \"html\": {
                    \"href\": \"https://bitbucket.org/my-workspace/demo\"
                  },
                  \"avatar\": {
                    \"href\":
    \"https://bytebucket.org/ravatar/%7B850e1749-781a-4115-9316-df39d0600e7a%7D?ts=default\"
                  }
                },
                \"uuid\": \"{850e1749-781a-4115-9316-df39d0600e7a}\"
              }
            },
            \"type\": \"commit_file\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/my-
    workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py\"
              }
            },
            \"path\": \"src/foo.py\"
          }
        }
      ]
    }
    ```

    Try `fields=%2Bvalues.*.*.*.*` to get an idea what's possible.

    Args:
        username (str):
        search_query (str):
        page (Union[Unset, None, int]):  Default: 1.
        pagelen (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            search_query=search_query,
            page=page,
            pagelen=pagelen,
        )
    ).parsed
