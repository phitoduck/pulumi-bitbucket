from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/refs/branches/{name}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, name=name
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
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Get a branch

     Returns a branch object within the specified repository.

            ```
            $ curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches/master | jq
    .
            {
              \"name\": \"master\",
              \"links\": {
                \"commits\": {
                  \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commits/master\"
                },
                \"self\": {
                  \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches/master\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/atlassian/aui/branch/master\"
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
                \"hash\": \"e7d158ff7ed5538c28f94cd97a9ad569680fc94e\",
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
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"comments\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e/comments\"
                  },
                  \"patch\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/patch/e7d158ff7
    ed5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"html\": {
                    \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/e7d158ff7ed5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"diff\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/diff/e7d158ff7e
    d5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"approve\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e/approve\"
                  },
                  \"statuses\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e/statuses\"
                  }
                },
                \"author\": {
                  \"raw\": \"psre-renovate-bot <psre-renovate-bot@atlassian.com>\",
                  \"type\": \"author\",
                  \"user\": {
                    \"display_name\": \"psre-renovate-bot\",
                    \"uuid\": \"{250a442a-3ab3-4fcb-87c3-3c8f3df65ec7}\",
                    \"links\": {
                      \"self\": {
                        \"href\":
    \"https://api.bitbucket.org/2.0/users/%7B250a442a-3ab3-4fcb-87c3-3c8f3df65ec7%7D\"
                      },
                      \"html\": {
                        \"href\": \"https://bitbucket.org/%7B250a442a-3ab3-4fcb-87c3-3c8f3df65ec7%7D/\"
                      },
                      \"avatar\": {
                        \"href\":
    \"https://secure.gravatar.com/avatar/6972ee037c9f36360170a86f544071a2?d=https%3A%2F%2Favatar-
    management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FP-3.png\"
                      }
                    },
                    \"nickname\": \"Renovate Bot\",
                    \"type\": \"user\",
                    \"account_id\": \"5d5355e8c6b9320d9ea5b28d\"
                  }
                },
                \"parents\": [
                  {
                    \"hash\": \"eab868a309e75733de80969a7bed1ec6d4651e06\",
                    \"type\": \"commit\",
                    \"links\": {
                      \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/eab8
    68a309e75733de80969a7bed1ec6d4651e06\"
                      },
                      \"html\": {
                        \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/eab868a309e75733de80969a7bed1ec6d4651e06\"
                      }
                    }
                  }
                ],
                \"date\": \"2021-04-12T06:44:38+00:00\",
                \"message\": \"Merged in issue/NONE-renovate-master-babel-monorepo (pull request #2883)

    chore(deps): update babel monorepo to v7.13.15 (master)

    Approved-by: Chris \"Daz\" Darroch
    \",
                \"type\": \"commit\"
              }
            }
            ```

            This call requires authentication. Private repositories require the
            caller to authenticate with an account that has appropriate
            authorization.

            For Git, the branch name should not include any prefixes (e.g.
            refs/heads).

    Args:
        workspace (str):
        repo_slug (str):
        name (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        name=name,
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
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Get a branch

     Returns a branch object within the specified repository.

            ```
            $ curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches/master | jq
    .
            {
              \"name\": \"master\",
              \"links\": {
                \"commits\": {
                  \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commits/master\"
                },
                \"self\": {
                  \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches/master\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/atlassian/aui/branch/master\"
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
                \"hash\": \"e7d158ff7ed5538c28f94cd97a9ad569680fc94e\",
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
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"comments\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e/comments\"
                  },
                  \"patch\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/patch/e7d158ff7
    ed5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"html\": {
                    \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/e7d158ff7ed5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"diff\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/diff/e7d158ff7e
    d5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"approve\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e/approve\"
                  },
                  \"statuses\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e/statuses\"
                  }
                },
                \"author\": {
                  \"raw\": \"psre-renovate-bot <psre-renovate-bot@atlassian.com>\",
                  \"type\": \"author\",
                  \"user\": {
                    \"display_name\": \"psre-renovate-bot\",
                    \"uuid\": \"{250a442a-3ab3-4fcb-87c3-3c8f3df65ec7}\",
                    \"links\": {
                      \"self\": {
                        \"href\":
    \"https://api.bitbucket.org/2.0/users/%7B250a442a-3ab3-4fcb-87c3-3c8f3df65ec7%7D\"
                      },
                      \"html\": {
                        \"href\": \"https://bitbucket.org/%7B250a442a-3ab3-4fcb-87c3-3c8f3df65ec7%7D/\"
                      },
                      \"avatar\": {
                        \"href\":
    \"https://secure.gravatar.com/avatar/6972ee037c9f36360170a86f544071a2?d=https%3A%2F%2Favatar-
    management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FP-3.png\"
                      }
                    },
                    \"nickname\": \"Renovate Bot\",
                    \"type\": \"user\",
                    \"account_id\": \"5d5355e8c6b9320d9ea5b28d\"
                  }
                },
                \"parents\": [
                  {
                    \"hash\": \"eab868a309e75733de80969a7bed1ec6d4651e06\",
                    \"type\": \"commit\",
                    \"links\": {
                      \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/eab8
    68a309e75733de80969a7bed1ec6d4651e06\"
                      },
                      \"html\": {
                        \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/eab868a309e75733de80969a7bed1ec6d4651e06\"
                      }
                    }
                  }
                ],
                \"date\": \"2021-04-12T06:44:38+00:00\",
                \"message\": \"Merged in issue/NONE-renovate-master-babel-monorepo (pull request #2883)

    chore(deps): update babel monorepo to v7.13.15 (master)

    Approved-by: Chris \"Daz\" Darroch
    \",
                \"type\": \"commit\"
              }
            }
            ```

            This call requires authentication. Private repositories require the
            caller to authenticate with an account that has appropriate
            authorization.

            For Git, the branch name should not include any prefixes (e.g.
            refs/heads).

    Args:
        workspace (str):
        repo_slug (str):
        name (str):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Get a branch

     Returns a branch object within the specified repository.

            ```
            $ curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches/master | jq
    .
            {
              \"name\": \"master\",
              \"links\": {
                \"commits\": {
                  \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commits/master\"
                },
                \"self\": {
                  \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches/master\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/atlassian/aui/branch/master\"
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
                \"hash\": \"e7d158ff7ed5538c28f94cd97a9ad569680fc94e\",
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
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"comments\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e/comments\"
                  },
                  \"patch\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/patch/e7d158ff7
    ed5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"html\": {
                    \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/e7d158ff7ed5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"diff\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/diff/e7d158ff7e
    d5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"approve\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e/approve\"
                  },
                  \"statuses\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e/statuses\"
                  }
                },
                \"author\": {
                  \"raw\": \"psre-renovate-bot <psre-renovate-bot@atlassian.com>\",
                  \"type\": \"author\",
                  \"user\": {
                    \"display_name\": \"psre-renovate-bot\",
                    \"uuid\": \"{250a442a-3ab3-4fcb-87c3-3c8f3df65ec7}\",
                    \"links\": {
                      \"self\": {
                        \"href\":
    \"https://api.bitbucket.org/2.0/users/%7B250a442a-3ab3-4fcb-87c3-3c8f3df65ec7%7D\"
                      },
                      \"html\": {
                        \"href\": \"https://bitbucket.org/%7B250a442a-3ab3-4fcb-87c3-3c8f3df65ec7%7D/\"
                      },
                      \"avatar\": {
                        \"href\":
    \"https://secure.gravatar.com/avatar/6972ee037c9f36360170a86f544071a2?d=https%3A%2F%2Favatar-
    management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FP-3.png\"
                      }
                    },
                    \"nickname\": \"Renovate Bot\",
                    \"type\": \"user\",
                    \"account_id\": \"5d5355e8c6b9320d9ea5b28d\"
                  }
                },
                \"parents\": [
                  {
                    \"hash\": \"eab868a309e75733de80969a7bed1ec6d4651e06\",
                    \"type\": \"commit\",
                    \"links\": {
                      \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/eab8
    68a309e75733de80969a7bed1ec6d4651e06\"
                      },
                      \"html\": {
                        \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/eab868a309e75733de80969a7bed1ec6d4651e06\"
                      }
                    }
                  }
                ],
                \"date\": \"2021-04-12T06:44:38+00:00\",
                \"message\": \"Merged in issue/NONE-renovate-master-babel-monorepo (pull request #2883)

    chore(deps): update babel monorepo to v7.13.15 (master)

    Approved-by: Chris \"Daz\" Darroch
    \",
                \"type\": \"commit\"
              }
            }
            ```

            This call requires authentication. Private repositories require the
            caller to authenticate with an account that has appropriate
            authorization.

            For Git, the branch name should not include any prefixes (e.g.
            refs/heads).

    Args:
        workspace (str):
        repo_slug (str):
        name (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        name=name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Get a branch

     Returns a branch object within the specified repository.

            ```
            $ curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches/master | jq
    .
            {
              \"name\": \"master\",
              \"links\": {
                \"commits\": {
                  \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commits/master\"
                },
                \"self\": {
                  \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches/master\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/atlassian/aui/branch/master\"
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
                \"hash\": \"e7d158ff7ed5538c28f94cd97a9ad569680fc94e\",
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
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"comments\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e/comments\"
                  },
                  \"patch\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/patch/e7d158ff7
    ed5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"html\": {
                    \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/e7d158ff7ed5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"diff\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/diff/e7d158ff7e
    d5538c28f94cd97a9ad569680fc94e\"
                  },
                  \"approve\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e/approve\"
                  },
                  \"statuses\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff
    7ed5538c28f94cd97a9ad569680fc94e/statuses\"
                  }
                },
                \"author\": {
                  \"raw\": \"psre-renovate-bot <psre-renovate-bot@atlassian.com>\",
                  \"type\": \"author\",
                  \"user\": {
                    \"display_name\": \"psre-renovate-bot\",
                    \"uuid\": \"{250a442a-3ab3-4fcb-87c3-3c8f3df65ec7}\",
                    \"links\": {
                      \"self\": {
                        \"href\":
    \"https://api.bitbucket.org/2.0/users/%7B250a442a-3ab3-4fcb-87c3-3c8f3df65ec7%7D\"
                      },
                      \"html\": {
                        \"href\": \"https://bitbucket.org/%7B250a442a-3ab3-4fcb-87c3-3c8f3df65ec7%7D/\"
                      },
                      \"avatar\": {
                        \"href\":
    \"https://secure.gravatar.com/avatar/6972ee037c9f36360170a86f544071a2?d=https%3A%2F%2Favatar-
    management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FP-3.png\"
                      }
                    },
                    \"nickname\": \"Renovate Bot\",
                    \"type\": \"user\",
                    \"account_id\": \"5d5355e8c6b9320d9ea5b28d\"
                  }
                },
                \"parents\": [
                  {
                    \"hash\": \"eab868a309e75733de80969a7bed1ec6d4651e06\",
                    \"type\": \"commit\",
                    \"links\": {
                      \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/eab8
    68a309e75733de80969a7bed1ec6d4651e06\"
                      },
                      \"html\": {
                        \"href\":
    \"https://bitbucket.org/atlassian/aui/commits/eab868a309e75733de80969a7bed1ec6d4651e06\"
                      }
                    }
                  }
                ],
                \"date\": \"2021-04-12T06:44:38+00:00\",
                \"message\": \"Merged in issue/NONE-renovate-master-babel-monorepo (pull request #2883)

    chore(deps): update babel monorepo to v7.13.15 (master)

    Approved-by: Chris \"Daz\" Darroch
    \",
                \"type\": \"commit\"
              }
            }
            ```

            This call requires authentication. Private repositories require the
            caller to authenticate with an account that has appropriate
            authorization.

            For Git, the branch name should not include any prefixes (e.g.
            refs/heads).

    Args:
        workspace (str):
        repo_slug (str):
        name (str):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            name=name,
            client=client,
        )
    ).parsed
