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
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/refs/branches".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List open branches

     Returns a list of all open branches within the specified repository.
            Results will be in the order the source control manager returns them.

            ```
            $ curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches?pagelen=1 |
    jq .
            {
              \"pagelen\": 1,
              \"size\": 187,
              \"values\": [
                {
                  \"name\": \"issue-9.3/AUI-5343-assistive-class\",
                  \"links\": {
                    \"commits\": {
                      \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commits/issue-9.3/AUI-5343-assistive-
    class\"
                    },
                    \"self\": {
                      \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches
    /issue-9.3/AUI-5343-assistive-class\"
                    },
                    \"html\": {
                      \"href\":
    \"https://bitbucket.org/atlassian/aui/branch/issue-9.3/AUI-5343-assistive-class\"
                    }
                  },
                  \"default_merge_strategy\": \"squash\",
                  \"merge_strategies\": [
                    \"merge_commit\",
                    \"squash\",
                    \"fast_forward\"
                  ],
                  \"type\": \"branch\",
                  \"target\": {
                    \"hash\": \"e5d1cde9069fcb9f0af90403a4de2150c125a148\",
                    \"repository\": {
                      \"links\": {
                        \"self\": {
                          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui\"
                        },
                        \"html\": {
                          \"href\": \"https://bitbucket.org/atlassian/aui\"
                        },
                        \"avatar\": {
                          \"href\":
    \"https://bytebucket.org/ravatar/%7B585074de-7b60-4fd1-81ed-e0bc7fafbda5%7D?ts=86317\"
                        }
                      },
                      \"type\": \"repository\",
                      \"name\": \"aui\",
                      \"full_name\": \"atlassian/aui\",
                      \"uuid\": \"{585074de-7b60-4fd1-81ed-e0bc7fafbda5}\"
                    },
                    \"links\": {
                      \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"comments\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148/comments\"
                      },
                      \"patch\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/patch/e5d1c
    de9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"html\": {
                        \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/e5d1cde9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"diff\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/diff/e5d1cd
    e9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"approve\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148/approve\"
                      },
                      \"statuses\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148/statuses\"
                      }
                    },
                    \"author\": {
                      \"raw\": \"Marcin Konopka <mkonopka@atlassian.com>\",
                      \"type\": \"author\",
                      \"user\": {
                        \"display_name\": \"Marcin Konopka\",
                        \"uuid\": \"{47cc24f4-2a05-4420-88fe-0417535a110a}\",
                        \"links\": {
                          \"self\": {
                            \"href\":
    \"https://api.bitbucket.org/2.0/users/%7B47cc24f4-2a05-4420-88fe-0417535a110a%7D\"
                          },
                          \"html\": {
                            \"href\":
    \"https://bitbucket.org/%7B47cc24f4-2a05-4420-88fe-0417535a110a%7D/\"
                          },
                          \"avatar\": {
                            \"href\": \"https://avatar-management--avatars.us-west-2.prod.public.atl-
    paas.net/initials/MK-1.png\"
                          }
                        },
                        \"nickname\": \"Marcin Konopka\",
                        \"type\": \"user\",
                        \"account_id\": \"60113d2b47a9540069f4de03\"
                      }
                    },
                    \"parents\": [
                      {
                        \"hash\": \"87f7fc92b00464ae47b13ef65c91884e4ac9be51\",
                        \"type\": \"commit\",
                        \"links\": {
                          \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/
    87f7fc92b00464ae47b13ef65c91884e4ac9be51\"
                          },
                          \"html\": {
                            \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/87f7fc92b00464ae47b13ef65c91884e4ac9be51\"
                          }
                        }
                      }
                    ],
                    \"date\": \"2021-04-13T13:44:49+00:00\",
                    \"message\": \"wip
    \",
                    \"type\": \"commit\"
                  }
                }
              ],
              \"page\": 1,
              \"next\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches?pagelen=1&page=2\"
            }
            ```

            Branches support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering)
            that can be used to search for specific branches. For instance, to find
            all branches that have \"stab\" in their name:

            ```
            curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches -G --data-
    urlencode 'q=name ~ \"stab\"'
            ```

            By default, results will be in the order the underlying source control system returns them
    and identical to
            the ordering one sees when running \"$ git branch --list\". Note that this follows simple
            lexical ordering of the ref names.

            This can be undesirable as it does apply any natural sorting semantics, meaning for instance
    that tags are
            sorted [\"v10\", \"v11\", \"v9\"] instead of [\"v9\", \"v10\", \"v11\"].

            Sorting can be changed using the ?q= query parameter. When using ?q=name to explicitly sort
    on ref name,
            Bitbucket will apply natural sorting and interpret numerical values as numbers instead of
    strings.

    Args:
        workspace (str):
        repo_slug (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
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
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List open branches

     Returns a list of all open branches within the specified repository.
            Results will be in the order the source control manager returns them.

            ```
            $ curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches?pagelen=1 |
    jq .
            {
              \"pagelen\": 1,
              \"size\": 187,
              \"values\": [
                {
                  \"name\": \"issue-9.3/AUI-5343-assistive-class\",
                  \"links\": {
                    \"commits\": {
                      \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commits/issue-9.3/AUI-5343-assistive-
    class\"
                    },
                    \"self\": {
                      \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches
    /issue-9.3/AUI-5343-assistive-class\"
                    },
                    \"html\": {
                      \"href\":
    \"https://bitbucket.org/atlassian/aui/branch/issue-9.3/AUI-5343-assistive-class\"
                    }
                  },
                  \"default_merge_strategy\": \"squash\",
                  \"merge_strategies\": [
                    \"merge_commit\",
                    \"squash\",
                    \"fast_forward\"
                  ],
                  \"type\": \"branch\",
                  \"target\": {
                    \"hash\": \"e5d1cde9069fcb9f0af90403a4de2150c125a148\",
                    \"repository\": {
                      \"links\": {
                        \"self\": {
                          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui\"
                        },
                        \"html\": {
                          \"href\": \"https://bitbucket.org/atlassian/aui\"
                        },
                        \"avatar\": {
                          \"href\":
    \"https://bytebucket.org/ravatar/%7B585074de-7b60-4fd1-81ed-e0bc7fafbda5%7D?ts=86317\"
                        }
                      },
                      \"type\": \"repository\",
                      \"name\": \"aui\",
                      \"full_name\": \"atlassian/aui\",
                      \"uuid\": \"{585074de-7b60-4fd1-81ed-e0bc7fafbda5}\"
                    },
                    \"links\": {
                      \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"comments\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148/comments\"
                      },
                      \"patch\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/patch/e5d1c
    de9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"html\": {
                        \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/e5d1cde9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"diff\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/diff/e5d1cd
    e9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"approve\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148/approve\"
                      },
                      \"statuses\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148/statuses\"
                      }
                    },
                    \"author\": {
                      \"raw\": \"Marcin Konopka <mkonopka@atlassian.com>\",
                      \"type\": \"author\",
                      \"user\": {
                        \"display_name\": \"Marcin Konopka\",
                        \"uuid\": \"{47cc24f4-2a05-4420-88fe-0417535a110a}\",
                        \"links\": {
                          \"self\": {
                            \"href\":
    \"https://api.bitbucket.org/2.0/users/%7B47cc24f4-2a05-4420-88fe-0417535a110a%7D\"
                          },
                          \"html\": {
                            \"href\":
    \"https://bitbucket.org/%7B47cc24f4-2a05-4420-88fe-0417535a110a%7D/\"
                          },
                          \"avatar\": {
                            \"href\": \"https://avatar-management--avatars.us-west-2.prod.public.atl-
    paas.net/initials/MK-1.png\"
                          }
                        },
                        \"nickname\": \"Marcin Konopka\",
                        \"type\": \"user\",
                        \"account_id\": \"60113d2b47a9540069f4de03\"
                      }
                    },
                    \"parents\": [
                      {
                        \"hash\": \"87f7fc92b00464ae47b13ef65c91884e4ac9be51\",
                        \"type\": \"commit\",
                        \"links\": {
                          \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/
    87f7fc92b00464ae47b13ef65c91884e4ac9be51\"
                          },
                          \"html\": {
                            \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/87f7fc92b00464ae47b13ef65c91884e4ac9be51\"
                          }
                        }
                      }
                    ],
                    \"date\": \"2021-04-13T13:44:49+00:00\",
                    \"message\": \"wip
    \",
                    \"type\": \"commit\"
                  }
                }
              ],
              \"page\": 1,
              \"next\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches?pagelen=1&page=2\"
            }
            ```

            Branches support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering)
            that can be used to search for specific branches. For instance, to find
            all branches that have \"stab\" in their name:

            ```
            curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches -G --data-
    urlencode 'q=name ~ \"stab\"'
            ```

            By default, results will be in the order the underlying source control system returns them
    and identical to
            the ordering one sees when running \"$ git branch --list\". Note that this follows simple
            lexical ordering of the ref names.

            This can be undesirable as it does apply any natural sorting semantics, meaning for instance
    that tags are
            sorted [\"v10\", \"v11\", \"v9\"] instead of [\"v9\", \"v10\", \"v11\"].

            Sorting can be changed using the ?q= query parameter. When using ?q=name to explicitly sort
    on ref name,
            Bitbucket will apply natural sorting and interpret numerical values as numbers instead of
    strings.

    Args:
        workspace (str):
        repo_slug (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        q=q,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List open branches

     Returns a list of all open branches within the specified repository.
            Results will be in the order the source control manager returns them.

            ```
            $ curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches?pagelen=1 |
    jq .
            {
              \"pagelen\": 1,
              \"size\": 187,
              \"values\": [
                {
                  \"name\": \"issue-9.3/AUI-5343-assistive-class\",
                  \"links\": {
                    \"commits\": {
                      \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commits/issue-9.3/AUI-5343-assistive-
    class\"
                    },
                    \"self\": {
                      \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches
    /issue-9.3/AUI-5343-assistive-class\"
                    },
                    \"html\": {
                      \"href\":
    \"https://bitbucket.org/atlassian/aui/branch/issue-9.3/AUI-5343-assistive-class\"
                    }
                  },
                  \"default_merge_strategy\": \"squash\",
                  \"merge_strategies\": [
                    \"merge_commit\",
                    \"squash\",
                    \"fast_forward\"
                  ],
                  \"type\": \"branch\",
                  \"target\": {
                    \"hash\": \"e5d1cde9069fcb9f0af90403a4de2150c125a148\",
                    \"repository\": {
                      \"links\": {
                        \"self\": {
                          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui\"
                        },
                        \"html\": {
                          \"href\": \"https://bitbucket.org/atlassian/aui\"
                        },
                        \"avatar\": {
                          \"href\":
    \"https://bytebucket.org/ravatar/%7B585074de-7b60-4fd1-81ed-e0bc7fafbda5%7D?ts=86317\"
                        }
                      },
                      \"type\": \"repository\",
                      \"name\": \"aui\",
                      \"full_name\": \"atlassian/aui\",
                      \"uuid\": \"{585074de-7b60-4fd1-81ed-e0bc7fafbda5}\"
                    },
                    \"links\": {
                      \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"comments\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148/comments\"
                      },
                      \"patch\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/patch/e5d1c
    de9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"html\": {
                        \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/e5d1cde9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"diff\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/diff/e5d1cd
    e9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"approve\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148/approve\"
                      },
                      \"statuses\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148/statuses\"
                      }
                    },
                    \"author\": {
                      \"raw\": \"Marcin Konopka <mkonopka@atlassian.com>\",
                      \"type\": \"author\",
                      \"user\": {
                        \"display_name\": \"Marcin Konopka\",
                        \"uuid\": \"{47cc24f4-2a05-4420-88fe-0417535a110a}\",
                        \"links\": {
                          \"self\": {
                            \"href\":
    \"https://api.bitbucket.org/2.0/users/%7B47cc24f4-2a05-4420-88fe-0417535a110a%7D\"
                          },
                          \"html\": {
                            \"href\":
    \"https://bitbucket.org/%7B47cc24f4-2a05-4420-88fe-0417535a110a%7D/\"
                          },
                          \"avatar\": {
                            \"href\": \"https://avatar-management--avatars.us-west-2.prod.public.atl-
    paas.net/initials/MK-1.png\"
                          }
                        },
                        \"nickname\": \"Marcin Konopka\",
                        \"type\": \"user\",
                        \"account_id\": \"60113d2b47a9540069f4de03\"
                      }
                    },
                    \"parents\": [
                      {
                        \"hash\": \"87f7fc92b00464ae47b13ef65c91884e4ac9be51\",
                        \"type\": \"commit\",
                        \"links\": {
                          \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/
    87f7fc92b00464ae47b13ef65c91884e4ac9be51\"
                          },
                          \"html\": {
                            \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/87f7fc92b00464ae47b13ef65c91884e4ac9be51\"
                          }
                        }
                      }
                    ],
                    \"date\": \"2021-04-13T13:44:49+00:00\",
                    \"message\": \"wip
    \",
                    \"type\": \"commit\"
                  }
                }
              ],
              \"page\": 1,
              \"next\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches?pagelen=1&page=2\"
            }
            ```

            Branches support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering)
            that can be used to search for specific branches. For instance, to find
            all branches that have \"stab\" in their name:

            ```
            curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches -G --data-
    urlencode 'q=name ~ \"stab\"'
            ```

            By default, results will be in the order the underlying source control system returns them
    and identical to
            the ordering one sees when running \"$ git branch --list\". Note that this follows simple
            lexical ordering of the ref names.

            This can be undesirable as it does apply any natural sorting semantics, meaning for instance
    that tags are
            sorted [\"v10\", \"v11\", \"v9\"] instead of [\"v9\", \"v10\", \"v11\"].

            Sorting can be changed using the ?q= query parameter. When using ?q=name to explicitly sort
    on ref name,
            Bitbucket will apply natural sorting and interpret numerical values as numbers instead of
    strings.

    Args:
        workspace (str):
        repo_slug (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        q=q,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List open branches

     Returns a list of all open branches within the specified repository.
            Results will be in the order the source control manager returns them.

            ```
            $ curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches?pagelen=1 |
    jq .
            {
              \"pagelen\": 1,
              \"size\": 187,
              \"values\": [
                {
                  \"name\": \"issue-9.3/AUI-5343-assistive-class\",
                  \"links\": {
                    \"commits\": {
                      \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commits/issue-9.3/AUI-5343-assistive-
    class\"
                    },
                    \"self\": {
                      \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches
    /issue-9.3/AUI-5343-assistive-class\"
                    },
                    \"html\": {
                      \"href\":
    \"https://bitbucket.org/atlassian/aui/branch/issue-9.3/AUI-5343-assistive-class\"
                    }
                  },
                  \"default_merge_strategy\": \"squash\",
                  \"merge_strategies\": [
                    \"merge_commit\",
                    \"squash\",
                    \"fast_forward\"
                  ],
                  \"type\": \"branch\",
                  \"target\": {
                    \"hash\": \"e5d1cde9069fcb9f0af90403a4de2150c125a148\",
                    \"repository\": {
                      \"links\": {
                        \"self\": {
                          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui\"
                        },
                        \"html\": {
                          \"href\": \"https://bitbucket.org/atlassian/aui\"
                        },
                        \"avatar\": {
                          \"href\":
    \"https://bytebucket.org/ravatar/%7B585074de-7b60-4fd1-81ed-e0bc7fafbda5%7D?ts=86317\"
                        }
                      },
                      \"type\": \"repository\",
                      \"name\": \"aui\",
                      \"full_name\": \"atlassian/aui\",
                      \"uuid\": \"{585074de-7b60-4fd1-81ed-e0bc7fafbda5}\"
                    },
                    \"links\": {
                      \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"comments\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148/comments\"
                      },
                      \"patch\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/patch/e5d1c
    de9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"html\": {
                        \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/e5d1cde9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"diff\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/diff/e5d1cd
    e9069fcb9f0af90403a4de2150c125a148\"
                      },
                      \"approve\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148/approve\"
                      },
                      \"statuses\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1
    cde9069fcb9f0af90403a4de2150c125a148/statuses\"
                      }
                    },
                    \"author\": {
                      \"raw\": \"Marcin Konopka <mkonopka@atlassian.com>\",
                      \"type\": \"author\",
                      \"user\": {
                        \"display_name\": \"Marcin Konopka\",
                        \"uuid\": \"{47cc24f4-2a05-4420-88fe-0417535a110a}\",
                        \"links\": {
                          \"self\": {
                            \"href\":
    \"https://api.bitbucket.org/2.0/users/%7B47cc24f4-2a05-4420-88fe-0417535a110a%7D\"
                          },
                          \"html\": {
                            \"href\":
    \"https://bitbucket.org/%7B47cc24f4-2a05-4420-88fe-0417535a110a%7D/\"
                          },
                          \"avatar\": {
                            \"href\": \"https://avatar-management--avatars.us-west-2.prod.public.atl-
    paas.net/initials/MK-1.png\"
                          }
                        },
                        \"nickname\": \"Marcin Konopka\",
                        \"type\": \"user\",
                        \"account_id\": \"60113d2b47a9540069f4de03\"
                      }
                    },
                    \"parents\": [
                      {
                        \"hash\": \"87f7fc92b00464ae47b13ef65c91884e4ac9be51\",
                        \"type\": \"commit\",
                        \"links\": {
                          \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/
    87f7fc92b00464ae47b13ef65c91884e4ac9be51\"
                          },
                          \"html\": {
                            \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/87f7fc92b00464ae47b13ef65c91884e4ac9be51\"
                          }
                        }
                      }
                    ],
                    \"date\": \"2021-04-13T13:44:49+00:00\",
                    \"message\": \"wip
    \",
                    \"type\": \"commit\"
                  }
                }
              ],
              \"page\": 1,
              \"next\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches?pagelen=1&page=2\"
            }
            ```

            Branches support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering)
            that can be used to search for specific branches. For instance, to find
            all branches that have \"stab\" in their name:

            ```
            curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches -G --data-
    urlencode 'q=name ~ \"stab\"'
            ```

            By default, results will be in the order the underlying source control system returns them
    and identical to
            the ordering one sees when running \"$ git branch --list\". Note that this follows simple
            lexical ordering of the ref names.

            This can be undesirable as it does apply any natural sorting semantics, meaning for instance
    that tags are
            sorted [\"v10\", \"v11\", \"v9\"] instead of [\"v9\", \"v10\", \"v11\"].

            Sorting can be changed using the ?q= query parameter. When using ?q=name to explicitly sort
    on ref name,
            Bitbucket will apply natural sorting and interpret numerical values as numbers instead of
    strings.

    Args:
        workspace (str):
        repo_slug (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            q=q,
            sort=sort,
        )
    ).parsed
