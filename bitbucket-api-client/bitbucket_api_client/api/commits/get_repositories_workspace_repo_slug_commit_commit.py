from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/commit/{commit}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, commit=commit
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
    commit: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Get a commit

     Returns the specified commit.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a1
    {
        \"rendered\": {
            \"message\": {
            \"raw\": \"Add a GEORDI_OUTPUT_DIR setting\",
            \"markup\": \"markdown\",
            \"html\": \"<p>Add a GEORDI_OUTPUT_DIR setting</p>\",
            \"type\": \"rendered\"
            }
        },
        \"hash\": \"f7591a13eda445d9a9167f98eb870319f4b6c2d8\",
        \"repository\": {
            \"name\": \"geordi\",
            \"type\": \"repository\",
            \"full_name\": \"bitbucket/geordi\",
            \"links\": {
                \"self\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi\"
                },
                \"html\": {
                    \"href\": \"https://bitbucket.org/bitbucket/geordi\"
                },
                \"avatar\": {
                    \"href\":
    \"https://bytebucket.org/ravatar/%7B85d08b4e-571d-44e9-a507-fa476535aa98%7D?ts=1730260\"
                }
            },
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
        },
        \"links\": {
            \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8\"
            },
            \"comments\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8/comments\"
            },
            \"patch\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/patch/f7591a13ed
    a445d9a9167f98eb870319f4b6c2d8\"
            },
            \"html\": {
                \"href\":
    \"https://bitbucket.org/bitbucket/geordi/commits/f7591a13eda445d9a9167f98eb870319f4b6c2d8\"
            },
            \"diff\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/diff/f7591a13eda
    445d9a9167f98eb870319f4b6c2d8\"
            },
            \"approve\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8/approve\"
            },
            \"statuses\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8/statuses\"
            }
        },
        \"author\": {
            \"raw\": \"Brodie Rao <a@b.c>\",
            \"type\": \"author\",
            \"user\": {
                \"display_name\": \"Brodie Rao\",
                \"uuid\": \"{9484702e-c663-4afd-aefb-c93a8cd31c28}\",
                \"links\": {
                    \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/users/%7B9484702e-c663-4afd-
    aefb-c93a8cd31c28%7D\"
                    },
                    \"html\": {
                        \"href\": \"https://bitbucket.org/%7B9484702e-c663-4afd-aefb-c93a8cd31c28%7D/\"
                    },
                    \"avatar\": {
                        \"href\": \"https://avatar-management--avatars.us-west-2.prod.public.atl-
    paas.net/557058:3aae1e05-702a-41e5-81c8-f36f29afb6ca/613070db-28b0-421f-8dba-ae8a87e2a5c7/128\"
                    }
                },
                \"type\": \"user\",
                \"nickname\": \"brodie\",
                \"account_id\": \"557058:3aae1e05-702a-41e5-81c8-f36f29afb6ca\"
            }
        },
        \"summary\": {
            \"raw\": \"Add a GEORDI_OUTPUT_DIR setting\",
            \"markup\": \"markdown\",
            \"html\": \"<p>Add a GEORDI_OUTPUT_DIR setting</p>\",
            \"type\": \"rendered\"
        },
        \"participants\": [],
        \"parents\": [
            {
                \"type\": \"commit\",
                \"hash\": \"f06941fec4ef6bcb0c2456927a0cf258fa4f899b\",
                \"links\": {
                    \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f
    06941fec4ef6bcb0c2456927a0cf258fa4f899b\"
                    },
                    \"html\": {
                        \"href\":
    \"https://bitbucket.org/bitbucket/geordi/commits/f06941fec4ef6bcb0c2456927a0cf258fa4f899b\"
                    }
                }
            }
        ],
        \"date\": \"2012-07-16T19:37:54+00:00\",
        \"message\": \"Add a GEORDI_OUTPUT_DIR setting\",
        \"type\": \"commit\"
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
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
    commit: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Get a commit

     Returns the specified commit.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a1
    {
        \"rendered\": {
            \"message\": {
            \"raw\": \"Add a GEORDI_OUTPUT_DIR setting\",
            \"markup\": \"markdown\",
            \"html\": \"<p>Add a GEORDI_OUTPUT_DIR setting</p>\",
            \"type\": \"rendered\"
            }
        },
        \"hash\": \"f7591a13eda445d9a9167f98eb870319f4b6c2d8\",
        \"repository\": {
            \"name\": \"geordi\",
            \"type\": \"repository\",
            \"full_name\": \"bitbucket/geordi\",
            \"links\": {
                \"self\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi\"
                },
                \"html\": {
                    \"href\": \"https://bitbucket.org/bitbucket/geordi\"
                },
                \"avatar\": {
                    \"href\":
    \"https://bytebucket.org/ravatar/%7B85d08b4e-571d-44e9-a507-fa476535aa98%7D?ts=1730260\"
                }
            },
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
        },
        \"links\": {
            \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8\"
            },
            \"comments\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8/comments\"
            },
            \"patch\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/patch/f7591a13ed
    a445d9a9167f98eb870319f4b6c2d8\"
            },
            \"html\": {
                \"href\":
    \"https://bitbucket.org/bitbucket/geordi/commits/f7591a13eda445d9a9167f98eb870319f4b6c2d8\"
            },
            \"diff\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/diff/f7591a13eda
    445d9a9167f98eb870319f4b6c2d8\"
            },
            \"approve\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8/approve\"
            },
            \"statuses\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8/statuses\"
            }
        },
        \"author\": {
            \"raw\": \"Brodie Rao <a@b.c>\",
            \"type\": \"author\",
            \"user\": {
                \"display_name\": \"Brodie Rao\",
                \"uuid\": \"{9484702e-c663-4afd-aefb-c93a8cd31c28}\",
                \"links\": {
                    \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/users/%7B9484702e-c663-4afd-
    aefb-c93a8cd31c28%7D\"
                    },
                    \"html\": {
                        \"href\": \"https://bitbucket.org/%7B9484702e-c663-4afd-aefb-c93a8cd31c28%7D/\"
                    },
                    \"avatar\": {
                        \"href\": \"https://avatar-management--avatars.us-west-2.prod.public.atl-
    paas.net/557058:3aae1e05-702a-41e5-81c8-f36f29afb6ca/613070db-28b0-421f-8dba-ae8a87e2a5c7/128\"
                    }
                },
                \"type\": \"user\",
                \"nickname\": \"brodie\",
                \"account_id\": \"557058:3aae1e05-702a-41e5-81c8-f36f29afb6ca\"
            }
        },
        \"summary\": {
            \"raw\": \"Add a GEORDI_OUTPUT_DIR setting\",
            \"markup\": \"markdown\",
            \"html\": \"<p>Add a GEORDI_OUTPUT_DIR setting</p>\",
            \"type\": \"rendered\"
        },
        \"participants\": [],
        \"parents\": [
            {
                \"type\": \"commit\",
                \"hash\": \"f06941fec4ef6bcb0c2456927a0cf258fa4f899b\",
                \"links\": {
                    \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f
    06941fec4ef6bcb0c2456927a0cf258fa4f899b\"
                    },
                    \"html\": {
                        \"href\":
    \"https://bitbucket.org/bitbucket/geordi/commits/f06941fec4ef6bcb0c2456927a0cf258fa4f899b\"
                    }
                }
            }
        ],
        \"date\": \"2012-07-16T19:37:54+00:00\",
        \"message\": \"Add a GEORDI_OUTPUT_DIR setting\",
        \"type\": \"commit\"
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Get a commit

     Returns the specified commit.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a1
    {
        \"rendered\": {
            \"message\": {
            \"raw\": \"Add a GEORDI_OUTPUT_DIR setting\",
            \"markup\": \"markdown\",
            \"html\": \"<p>Add a GEORDI_OUTPUT_DIR setting</p>\",
            \"type\": \"rendered\"
            }
        },
        \"hash\": \"f7591a13eda445d9a9167f98eb870319f4b6c2d8\",
        \"repository\": {
            \"name\": \"geordi\",
            \"type\": \"repository\",
            \"full_name\": \"bitbucket/geordi\",
            \"links\": {
                \"self\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi\"
                },
                \"html\": {
                    \"href\": \"https://bitbucket.org/bitbucket/geordi\"
                },
                \"avatar\": {
                    \"href\":
    \"https://bytebucket.org/ravatar/%7B85d08b4e-571d-44e9-a507-fa476535aa98%7D?ts=1730260\"
                }
            },
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
        },
        \"links\": {
            \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8\"
            },
            \"comments\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8/comments\"
            },
            \"patch\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/patch/f7591a13ed
    a445d9a9167f98eb870319f4b6c2d8\"
            },
            \"html\": {
                \"href\":
    \"https://bitbucket.org/bitbucket/geordi/commits/f7591a13eda445d9a9167f98eb870319f4b6c2d8\"
            },
            \"diff\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/diff/f7591a13eda
    445d9a9167f98eb870319f4b6c2d8\"
            },
            \"approve\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8/approve\"
            },
            \"statuses\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8/statuses\"
            }
        },
        \"author\": {
            \"raw\": \"Brodie Rao <a@b.c>\",
            \"type\": \"author\",
            \"user\": {
                \"display_name\": \"Brodie Rao\",
                \"uuid\": \"{9484702e-c663-4afd-aefb-c93a8cd31c28}\",
                \"links\": {
                    \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/users/%7B9484702e-c663-4afd-
    aefb-c93a8cd31c28%7D\"
                    },
                    \"html\": {
                        \"href\": \"https://bitbucket.org/%7B9484702e-c663-4afd-aefb-c93a8cd31c28%7D/\"
                    },
                    \"avatar\": {
                        \"href\": \"https://avatar-management--avatars.us-west-2.prod.public.atl-
    paas.net/557058:3aae1e05-702a-41e5-81c8-f36f29afb6ca/613070db-28b0-421f-8dba-ae8a87e2a5c7/128\"
                    }
                },
                \"type\": \"user\",
                \"nickname\": \"brodie\",
                \"account_id\": \"557058:3aae1e05-702a-41e5-81c8-f36f29afb6ca\"
            }
        },
        \"summary\": {
            \"raw\": \"Add a GEORDI_OUTPUT_DIR setting\",
            \"markup\": \"markdown\",
            \"html\": \"<p>Add a GEORDI_OUTPUT_DIR setting</p>\",
            \"type\": \"rendered\"
        },
        \"participants\": [],
        \"parents\": [
            {
                \"type\": \"commit\",
                \"hash\": \"f06941fec4ef6bcb0c2456927a0cf258fa4f899b\",
                \"links\": {
                    \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f
    06941fec4ef6bcb0c2456927a0cf258fa4f899b\"
                    },
                    \"html\": {
                        \"href\":
    \"https://bitbucket.org/bitbucket/geordi/commits/f06941fec4ef6bcb0c2456927a0cf258fa4f899b\"
                    }
                }
            }
        ],
        \"date\": \"2012-07-16T19:37:54+00:00\",
        \"message\": \"Add a GEORDI_OUTPUT_DIR setting\",
        \"type\": \"commit\"
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Get a commit

     Returns the specified commit.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a1
    {
        \"rendered\": {
            \"message\": {
            \"raw\": \"Add a GEORDI_OUTPUT_DIR setting\",
            \"markup\": \"markdown\",
            \"html\": \"<p>Add a GEORDI_OUTPUT_DIR setting</p>\",
            \"type\": \"rendered\"
            }
        },
        \"hash\": \"f7591a13eda445d9a9167f98eb870319f4b6c2d8\",
        \"repository\": {
            \"name\": \"geordi\",
            \"type\": \"repository\",
            \"full_name\": \"bitbucket/geordi\",
            \"links\": {
                \"self\": {
                    \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi\"
                },
                \"html\": {
                    \"href\": \"https://bitbucket.org/bitbucket/geordi\"
                },
                \"avatar\": {
                    \"href\":
    \"https://bytebucket.org/ravatar/%7B85d08b4e-571d-44e9-a507-fa476535aa98%7D?ts=1730260\"
                }
            },
            \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
        },
        \"links\": {
            \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8\"
            },
            \"comments\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8/comments\"
            },
            \"patch\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/patch/f7591a13ed
    a445d9a9167f98eb870319f4b6c2d8\"
            },
            \"html\": {
                \"href\":
    \"https://bitbucket.org/bitbucket/geordi/commits/f7591a13eda445d9a9167f98eb870319f4b6c2d8\"
            },
            \"diff\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/diff/f7591a13eda
    445d9a9167f98eb870319f4b6c2d8\"
            },
            \"approve\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8/approve\"
            },
            \"statuses\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13e
    da445d9a9167f98eb870319f4b6c2d8/statuses\"
            }
        },
        \"author\": {
            \"raw\": \"Brodie Rao <a@b.c>\",
            \"type\": \"author\",
            \"user\": {
                \"display_name\": \"Brodie Rao\",
                \"uuid\": \"{9484702e-c663-4afd-aefb-c93a8cd31c28}\",
                \"links\": {
                    \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/users/%7B9484702e-c663-4afd-
    aefb-c93a8cd31c28%7D\"
                    },
                    \"html\": {
                        \"href\": \"https://bitbucket.org/%7B9484702e-c663-4afd-aefb-c93a8cd31c28%7D/\"
                    },
                    \"avatar\": {
                        \"href\": \"https://avatar-management--avatars.us-west-2.prod.public.atl-
    paas.net/557058:3aae1e05-702a-41e5-81c8-f36f29afb6ca/613070db-28b0-421f-8dba-ae8a87e2a5c7/128\"
                    }
                },
                \"type\": \"user\",
                \"nickname\": \"brodie\",
                \"account_id\": \"557058:3aae1e05-702a-41e5-81c8-f36f29afb6ca\"
            }
        },
        \"summary\": {
            \"raw\": \"Add a GEORDI_OUTPUT_DIR setting\",
            \"markup\": \"markdown\",
            \"html\": \"<p>Add a GEORDI_OUTPUT_DIR setting</p>\",
            \"type\": \"rendered\"
        },
        \"participants\": [],
        \"parents\": [
            {
                \"type\": \"commit\",
                \"hash\": \"f06941fec4ef6bcb0c2456927a0cf258fa4f899b\",
                \"links\": {
                    \"self\": {
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f
    06941fec4ef6bcb0c2456927a0cf258fa4f899b\"
                    },
                    \"html\": {
                        \"href\":
    \"https://bitbucket.org/bitbucket/geordi/commits/f06941fec4ef6bcb0c2456927a0cf258fa4f899b\"
                    }
                }
            }
        ],
        \"date\": \"2012-07-16T19:37:54+00:00\",
        \"message\": \"Add a GEORDI_OUTPUT_DIR setting\",
        \"type\": \"commit\"
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            client=client,
        )
    ).parsed
