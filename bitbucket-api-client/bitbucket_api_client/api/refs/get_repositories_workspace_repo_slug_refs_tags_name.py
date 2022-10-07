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
    url = "{}/repositories/{workspace}/{repo_slug}/refs/tags/{name}".format(
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
    """Get a tag

     Returns the specified tag.

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8 -G | jq .
    {
      \"name\": \"3.8\",
      \"links\": {
        \"commits\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commits/3.8\"
        },
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8\"
        },
        \"html\": {
          \"href\": \"https://bitbucket.org/seanfarley/hg/commits/tag/3.8\"
        }
      },
      \"tagger\": {
        \"raw\": \"Matt Mackall <mpm@selenic.com>\",
        \"type\": \"author\",
        \"user\": {
          \"username\": \"mpmselenic\",
          \"nickname\": \"mpmselenic\",
          \"display_name\": \"Matt Mackall\",
          \"type\": \"user\",
          \"uuid\": \"{a4934530-db4c-419c-a478-9ab4964c2ee7}\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/users/mpmselenic\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/mpmselenic/\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/account/mpmselenic/avatar/32/\"
            }
          }
        }
      },
      \"date\": \"2016-05-01T18:52:25+00:00\",
      \"message\": \"Added tag 3.8 for changeset f85de28eae32\",
      \"type\": \"tag\",
      \"target\": {
        \"hash\": \"f85de28eae32e7d3064b1a1321309071bbaaa069\",
        \"repository\": {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg/avatar/32/\"
            }
          },
          \"type\": \"repository\",
          \"name\": \"hg\",
          \"full_name\": \"seanfarley/hg\",
          \"uuid\": \"{c75687fb-e99d-4579-9087-190dbd406d30}\"
        },
        \"links\": {
          \"self\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069\"
          },
          \"comments\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/comments\"
          },
          \"patch\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/patch/f85de28eae32e7d30
    64b1a1321309071bbaaa069\"
          },
          \"html\": {
            \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/f85de28eae32e7d3064b1a1321309071bbaaa069\"
          },
          \"diff\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/diff/f85de28eae32e7d306
    4b1a1321309071bbaaa069\"
          },
          \"approve\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/approve\"
          },
          \"statuses\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/statuses\"
          }
        },
        \"author\": {
          \"raw\": \"Sean Farley <sean@farley.io>\",
          \"type\": \"author\",
          \"user\": {
            \"username\": \"seanfarley\",
            \"nickname\": \"seanfarley\",
            \"display_name\": \"Sean Farley\",
            \"type\": \"user\",
            \"uuid\": \"{a295f8a8-5876-4d43-89b5-3ad8c6c3c51d}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/seanfarley\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/seanfarley/\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket.org/account/seanfarley/avatar/32/\"
              }
            }
          }
        },
        \"parents\": [
          {
            \"hash\": \"9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\",
            \"type\": \"commit\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/9a98d0e5b07f
    c60887f9d3d34d9ac7d536f470d2\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\"
              }
            }
          }
        ],
        \"date\": \"2016-05-01T04:21:17+00:00\",
        \"message\": \"debian: alphabetize build deps\",
        \"type\": \"commit\"
      }
    }
    ```

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
    """Get a tag

     Returns the specified tag.

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8 -G | jq .
    {
      \"name\": \"3.8\",
      \"links\": {
        \"commits\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commits/3.8\"
        },
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8\"
        },
        \"html\": {
          \"href\": \"https://bitbucket.org/seanfarley/hg/commits/tag/3.8\"
        }
      },
      \"tagger\": {
        \"raw\": \"Matt Mackall <mpm@selenic.com>\",
        \"type\": \"author\",
        \"user\": {
          \"username\": \"mpmselenic\",
          \"nickname\": \"mpmselenic\",
          \"display_name\": \"Matt Mackall\",
          \"type\": \"user\",
          \"uuid\": \"{a4934530-db4c-419c-a478-9ab4964c2ee7}\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/users/mpmselenic\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/mpmselenic/\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/account/mpmselenic/avatar/32/\"
            }
          }
        }
      },
      \"date\": \"2016-05-01T18:52:25+00:00\",
      \"message\": \"Added tag 3.8 for changeset f85de28eae32\",
      \"type\": \"tag\",
      \"target\": {
        \"hash\": \"f85de28eae32e7d3064b1a1321309071bbaaa069\",
        \"repository\": {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg/avatar/32/\"
            }
          },
          \"type\": \"repository\",
          \"name\": \"hg\",
          \"full_name\": \"seanfarley/hg\",
          \"uuid\": \"{c75687fb-e99d-4579-9087-190dbd406d30}\"
        },
        \"links\": {
          \"self\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069\"
          },
          \"comments\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/comments\"
          },
          \"patch\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/patch/f85de28eae32e7d30
    64b1a1321309071bbaaa069\"
          },
          \"html\": {
            \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/f85de28eae32e7d3064b1a1321309071bbaaa069\"
          },
          \"diff\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/diff/f85de28eae32e7d306
    4b1a1321309071bbaaa069\"
          },
          \"approve\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/approve\"
          },
          \"statuses\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/statuses\"
          }
        },
        \"author\": {
          \"raw\": \"Sean Farley <sean@farley.io>\",
          \"type\": \"author\",
          \"user\": {
            \"username\": \"seanfarley\",
            \"nickname\": \"seanfarley\",
            \"display_name\": \"Sean Farley\",
            \"type\": \"user\",
            \"uuid\": \"{a295f8a8-5876-4d43-89b5-3ad8c6c3c51d}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/seanfarley\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/seanfarley/\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket.org/account/seanfarley/avatar/32/\"
              }
            }
          }
        },
        \"parents\": [
          {
            \"hash\": \"9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\",
            \"type\": \"commit\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/9a98d0e5b07f
    c60887f9d3d34d9ac7d536f470d2\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\"
              }
            }
          }
        ],
        \"date\": \"2016-05-01T04:21:17+00:00\",
        \"message\": \"debian: alphabetize build deps\",
        \"type\": \"commit\"
      }
    }
    ```

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
    """Get a tag

     Returns the specified tag.

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8 -G | jq .
    {
      \"name\": \"3.8\",
      \"links\": {
        \"commits\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commits/3.8\"
        },
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8\"
        },
        \"html\": {
          \"href\": \"https://bitbucket.org/seanfarley/hg/commits/tag/3.8\"
        }
      },
      \"tagger\": {
        \"raw\": \"Matt Mackall <mpm@selenic.com>\",
        \"type\": \"author\",
        \"user\": {
          \"username\": \"mpmselenic\",
          \"nickname\": \"mpmselenic\",
          \"display_name\": \"Matt Mackall\",
          \"type\": \"user\",
          \"uuid\": \"{a4934530-db4c-419c-a478-9ab4964c2ee7}\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/users/mpmselenic\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/mpmselenic/\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/account/mpmselenic/avatar/32/\"
            }
          }
        }
      },
      \"date\": \"2016-05-01T18:52:25+00:00\",
      \"message\": \"Added tag 3.8 for changeset f85de28eae32\",
      \"type\": \"tag\",
      \"target\": {
        \"hash\": \"f85de28eae32e7d3064b1a1321309071bbaaa069\",
        \"repository\": {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg/avatar/32/\"
            }
          },
          \"type\": \"repository\",
          \"name\": \"hg\",
          \"full_name\": \"seanfarley/hg\",
          \"uuid\": \"{c75687fb-e99d-4579-9087-190dbd406d30}\"
        },
        \"links\": {
          \"self\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069\"
          },
          \"comments\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/comments\"
          },
          \"patch\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/patch/f85de28eae32e7d30
    64b1a1321309071bbaaa069\"
          },
          \"html\": {
            \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/f85de28eae32e7d3064b1a1321309071bbaaa069\"
          },
          \"diff\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/diff/f85de28eae32e7d306
    4b1a1321309071bbaaa069\"
          },
          \"approve\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/approve\"
          },
          \"statuses\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/statuses\"
          }
        },
        \"author\": {
          \"raw\": \"Sean Farley <sean@farley.io>\",
          \"type\": \"author\",
          \"user\": {
            \"username\": \"seanfarley\",
            \"nickname\": \"seanfarley\",
            \"display_name\": \"Sean Farley\",
            \"type\": \"user\",
            \"uuid\": \"{a295f8a8-5876-4d43-89b5-3ad8c6c3c51d}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/seanfarley\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/seanfarley/\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket.org/account/seanfarley/avatar/32/\"
              }
            }
          }
        },
        \"parents\": [
          {
            \"hash\": \"9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\",
            \"type\": \"commit\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/9a98d0e5b07f
    c60887f9d3d34d9ac7d536f470d2\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\"
              }
            }
          }
        ],
        \"date\": \"2016-05-01T04:21:17+00:00\",
        \"message\": \"debian: alphabetize build deps\",
        \"type\": \"commit\"
      }
    }
    ```

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
    """Get a tag

     Returns the specified tag.

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8 -G | jq .
    {
      \"name\": \"3.8\",
      \"links\": {
        \"commits\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commits/3.8\"
        },
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8\"
        },
        \"html\": {
          \"href\": \"https://bitbucket.org/seanfarley/hg/commits/tag/3.8\"
        }
      },
      \"tagger\": {
        \"raw\": \"Matt Mackall <mpm@selenic.com>\",
        \"type\": \"author\",
        \"user\": {
          \"username\": \"mpmselenic\",
          \"nickname\": \"mpmselenic\",
          \"display_name\": \"Matt Mackall\",
          \"type\": \"user\",
          \"uuid\": \"{a4934530-db4c-419c-a478-9ab4964c2ee7}\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/users/mpmselenic\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/mpmselenic/\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/account/mpmselenic/avatar/32/\"
            }
          }
        }
      },
      \"date\": \"2016-05-01T18:52:25+00:00\",
      \"message\": \"Added tag 3.8 for changeset f85de28eae32\",
      \"type\": \"tag\",
      \"target\": {
        \"hash\": \"f85de28eae32e7d3064b1a1321309071bbaaa069\",
        \"repository\": {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg/avatar/32/\"
            }
          },
          \"type\": \"repository\",
          \"name\": \"hg\",
          \"full_name\": \"seanfarley/hg\",
          \"uuid\": \"{c75687fb-e99d-4579-9087-190dbd406d30}\"
        },
        \"links\": {
          \"self\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069\"
          },
          \"comments\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/comments\"
          },
          \"patch\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/patch/f85de28eae32e7d30
    64b1a1321309071bbaaa069\"
          },
          \"html\": {
            \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/f85de28eae32e7d3064b1a1321309071bbaaa069\"
          },
          \"diff\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/diff/f85de28eae32e7d306
    4b1a1321309071bbaaa069\"
          },
          \"approve\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/approve\"
          },
          \"statuses\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/statuses\"
          }
        },
        \"author\": {
          \"raw\": \"Sean Farley <sean@farley.io>\",
          \"type\": \"author\",
          \"user\": {
            \"username\": \"seanfarley\",
            \"nickname\": \"seanfarley\",
            \"display_name\": \"Sean Farley\",
            \"type\": \"user\",
            \"uuid\": \"{a295f8a8-5876-4d43-89b5-3ad8c6c3c51d}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/seanfarley\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/seanfarley/\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket.org/account/seanfarley/avatar/32/\"
              }
            }
          }
        },
        \"parents\": [
          {
            \"hash\": \"9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\",
            \"type\": \"commit\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/9a98d0e5b07f
    c60887f9d3d34d9ac7d536f470d2\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\"
              }
            }
          }
        ],
        \"date\": \"2016-05-01T04:21:17+00:00\",
        \"message\": \"debian: alphabetize build deps\",
        \"type\": \"commit\"
      }
    }
    ```

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
