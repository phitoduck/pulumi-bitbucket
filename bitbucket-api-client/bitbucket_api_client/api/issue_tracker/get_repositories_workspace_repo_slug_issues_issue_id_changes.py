from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, issue_id=issue_id
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
    issue_id: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List changes on an issue

     Returns the list of all changes that have been made to the specified
    issue. Changes are returned in chronological order with the oldest
    change first.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Note that this operation is changing significantly, due to privacy changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-the-issue-changes-api)
    for details.

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes - | jq .

    {
      \"pagelen\": 20,
      \"values\": [
        {
          \"changes\": {
            \"priority\": {
              \"new\": \"trivial\",
              \"old\": \"major\"
            },
            \"assignee\": {
              \"new\": \"\",
              \"old\": \"evzijst\"
            },
            \"assignee_account_id\": {
              \"new\": \"\",
              \"old\": \"557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443\"
            },
            \"kind\": {
              \"new\": \"enhancement\",
              \"old\": \"bug\"
            }
          },
          \"links\": {
            \"self\": {
              \"href\":
    \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes/2\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/evzijst/dogslow/issues/1#comment-2\"
            }
          },
          \"issue\": {
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1\"
              }
            },
            \"type\": \"issue\",
            \"id\": 1,
            \"repository\": {
              \"links\": {
                \"self\": {
                  \"href\": \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/evzijst/dogslow\"
                },
                \"avatar\": {
                  \"href\": \"https://bitbucket.org/evzijst/dogslow/avatar/32/\"
                }
              },
              \"type\": \"repository\",
              \"name\": \"dogslow\",
              \"full_name\": \"evzijst/dogslow\",
              \"uuid\": \"{988b17c6-1a47-4e70-84ee-854d5f012bf6}\"
            },
            \"title\": \"Updated title\"
          },
          \"created_on\": \"2018-03-03T00:35:28.353630+00:00\",
          \"user\": {
            \"username\": \"evzijst\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"evzijst\",
            \"type\": \"user\",
            \"uuid\": \"{aaa7972b-38af-4fb1-802d-6e3854c95778}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/evzijst/\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket.org/account/evzijst/avatar/32/\"
              }
            }
          },
          \"message\": {
            \"raw\": \"Removed assignee, changed kind and priority.\",
            \"markup\": \"markdown\",
            \"html\": \"<p>Removed assignee, changed kind and priority.</p>\",
            \"type\": \"rendered\"
          },
          \"type\": \"issue_change\",
          \"id\": 2
        }
      ],
      \"page\": 1
    }
    ```

    Changes support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) that
    can be used to search for specific changes. For instance, to see
    when an issue transitioned to \"resolved\":

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/site/master/issues/1/changes \
       -G --data-urlencode='q=changes.state.new = \"resolved\"'
    ```

    This resource is only available on repositories that have the issue
    tracker enabled.

    N.B.

    The `changes.assignee` and `changes.assignee_account_id` fields are not
    a `user` object. Instead, they contain the raw `username` and
    `account_id` of the user. This is to protect the integrity of the audit
    log even after a user account gets deleted.

    The `changes.assignee` field is deprecated will disappear in the
    future. Use `changes.assignee_account_id` instead.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
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
    issue_id: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List changes on an issue

     Returns the list of all changes that have been made to the specified
    issue. Changes are returned in chronological order with the oldest
    change first.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Note that this operation is changing significantly, due to privacy changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-the-issue-changes-api)
    for details.

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes - | jq .

    {
      \"pagelen\": 20,
      \"values\": [
        {
          \"changes\": {
            \"priority\": {
              \"new\": \"trivial\",
              \"old\": \"major\"
            },
            \"assignee\": {
              \"new\": \"\",
              \"old\": \"evzijst\"
            },
            \"assignee_account_id\": {
              \"new\": \"\",
              \"old\": \"557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443\"
            },
            \"kind\": {
              \"new\": \"enhancement\",
              \"old\": \"bug\"
            }
          },
          \"links\": {
            \"self\": {
              \"href\":
    \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes/2\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/evzijst/dogslow/issues/1#comment-2\"
            }
          },
          \"issue\": {
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1\"
              }
            },
            \"type\": \"issue\",
            \"id\": 1,
            \"repository\": {
              \"links\": {
                \"self\": {
                  \"href\": \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/evzijst/dogslow\"
                },
                \"avatar\": {
                  \"href\": \"https://bitbucket.org/evzijst/dogslow/avatar/32/\"
                }
              },
              \"type\": \"repository\",
              \"name\": \"dogslow\",
              \"full_name\": \"evzijst/dogslow\",
              \"uuid\": \"{988b17c6-1a47-4e70-84ee-854d5f012bf6}\"
            },
            \"title\": \"Updated title\"
          },
          \"created_on\": \"2018-03-03T00:35:28.353630+00:00\",
          \"user\": {
            \"username\": \"evzijst\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"evzijst\",
            \"type\": \"user\",
            \"uuid\": \"{aaa7972b-38af-4fb1-802d-6e3854c95778}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/evzijst/\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket.org/account/evzijst/avatar/32/\"
              }
            }
          },
          \"message\": {
            \"raw\": \"Removed assignee, changed kind and priority.\",
            \"markup\": \"markdown\",
            \"html\": \"<p>Removed assignee, changed kind and priority.</p>\",
            \"type\": \"rendered\"
          },
          \"type\": \"issue_change\",
          \"id\": 2
        }
      ],
      \"page\": 1
    }
    ```

    Changes support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) that
    can be used to search for specific changes. For instance, to see
    when an issue transitioned to \"resolved\":

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/site/master/issues/1/changes \
       -G --data-urlencode='q=changes.state.new = \"resolved\"'
    ```

    This resource is only available on repositories that have the issue
    tracker enabled.

    N.B.

    The `changes.assignee` and `changes.assignee_account_id` fields are not
    a `user` object. Instead, they contain the raw `username` and
    `account_id` of the user. This is to protect the integrity of the audit
    log even after a user account gets deleted.

    The `changes.assignee` field is deprecated will disappear in the
    future. Use `changes.assignee_account_id` instead.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        client=client,
        q=q,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List changes on an issue

     Returns the list of all changes that have been made to the specified
    issue. Changes are returned in chronological order with the oldest
    change first.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Note that this operation is changing significantly, due to privacy changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-the-issue-changes-api)
    for details.

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes - | jq .

    {
      \"pagelen\": 20,
      \"values\": [
        {
          \"changes\": {
            \"priority\": {
              \"new\": \"trivial\",
              \"old\": \"major\"
            },
            \"assignee\": {
              \"new\": \"\",
              \"old\": \"evzijst\"
            },
            \"assignee_account_id\": {
              \"new\": \"\",
              \"old\": \"557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443\"
            },
            \"kind\": {
              \"new\": \"enhancement\",
              \"old\": \"bug\"
            }
          },
          \"links\": {
            \"self\": {
              \"href\":
    \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes/2\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/evzijst/dogslow/issues/1#comment-2\"
            }
          },
          \"issue\": {
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1\"
              }
            },
            \"type\": \"issue\",
            \"id\": 1,
            \"repository\": {
              \"links\": {
                \"self\": {
                  \"href\": \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/evzijst/dogslow\"
                },
                \"avatar\": {
                  \"href\": \"https://bitbucket.org/evzijst/dogslow/avatar/32/\"
                }
              },
              \"type\": \"repository\",
              \"name\": \"dogslow\",
              \"full_name\": \"evzijst/dogslow\",
              \"uuid\": \"{988b17c6-1a47-4e70-84ee-854d5f012bf6}\"
            },
            \"title\": \"Updated title\"
          },
          \"created_on\": \"2018-03-03T00:35:28.353630+00:00\",
          \"user\": {
            \"username\": \"evzijst\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"evzijst\",
            \"type\": \"user\",
            \"uuid\": \"{aaa7972b-38af-4fb1-802d-6e3854c95778}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/evzijst/\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket.org/account/evzijst/avatar/32/\"
              }
            }
          },
          \"message\": {
            \"raw\": \"Removed assignee, changed kind and priority.\",
            \"markup\": \"markdown\",
            \"html\": \"<p>Removed assignee, changed kind and priority.</p>\",
            \"type\": \"rendered\"
          },
          \"type\": \"issue_change\",
          \"id\": 2
        }
      ],
      \"page\": 1
    }
    ```

    Changes support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) that
    can be used to search for specific changes. For instance, to see
    when an issue transitioned to \"resolved\":

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/site/master/issues/1/changes \
       -G --data-urlencode='q=changes.state.new = \"resolved\"'
    ```

    This resource is only available on repositories that have the issue
    tracker enabled.

    N.B.

    The `changes.assignee` and `changes.assignee_account_id` fields are not
    a `user` object. Instead, they contain the raw `username` and
    `account_id` of the user. This is to protect the integrity of the audit
    log even after a user account gets deleted.

    The `changes.assignee` field is deprecated will disappear in the
    future. Use `changes.assignee_account_id` instead.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
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
    issue_id: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List changes on an issue

     Returns the list of all changes that have been made to the specified
    issue. Changes are returned in chronological order with the oldest
    change first.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Note that this operation is changing significantly, due to privacy changes.
    See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-
    gdpr/#changes-to-the-issue-changes-api)
    for details.

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes - | jq .

    {
      \"pagelen\": 20,
      \"values\": [
        {
          \"changes\": {
            \"priority\": {
              \"new\": \"trivial\",
              \"old\": \"major\"
            },
            \"assignee\": {
              \"new\": \"\",
              \"old\": \"evzijst\"
            },
            \"assignee_account_id\": {
              \"new\": \"\",
              \"old\": \"557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443\"
            },
            \"kind\": {
              \"new\": \"enhancement\",
              \"old\": \"bug\"
            }
          },
          \"links\": {
            \"self\": {
              \"href\":
    \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes/2\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/evzijst/dogslow/issues/1#comment-2\"
            }
          },
          \"issue\": {
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1\"
              }
            },
            \"type\": \"issue\",
            \"id\": 1,
            \"repository\": {
              \"links\": {
                \"self\": {
                  \"href\": \"https://api.bitbucket.org/2.0/repositories/evzijst/dogslow\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/evzijst/dogslow\"
                },
                \"avatar\": {
                  \"href\": \"https://bitbucket.org/evzijst/dogslow/avatar/32/\"
                }
              },
              \"type\": \"repository\",
              \"name\": \"dogslow\",
              \"full_name\": \"evzijst/dogslow\",
              \"uuid\": \"{988b17c6-1a47-4e70-84ee-854d5f012bf6}\"
            },
            \"title\": \"Updated title\"
          },
          \"created_on\": \"2018-03-03T00:35:28.353630+00:00\",
          \"user\": {
            \"username\": \"evzijst\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"evzijst\",
            \"type\": \"user\",
            \"uuid\": \"{aaa7972b-38af-4fb1-802d-6e3854c95778}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/evzijst/\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket.org/account/evzijst/avatar/32/\"
              }
            }
          },
          \"message\": {
            \"raw\": \"Removed assignee, changed kind and priority.\",
            \"markup\": \"markdown\",
            \"html\": \"<p>Removed assignee, changed kind and priority.</p>\",
            \"type\": \"rendered\"
          },
          \"type\": \"issue_change\",
          \"id\": 2
        }
      ],
      \"page\": 1
    }
    ```

    Changes support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) that
    can be used to search for specific changes. For instance, to see
    when an issue transitioned to \"resolved\":

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/site/master/issues/1/changes \
       -G --data-urlencode='q=changes.state.new = \"resolved\"'
    ```

    This resource is only available on repositories that have the issue
    tracker enabled.

    N.B.

    The `changes.assignee` and `changes.assignee_account_id` fields are not
    a `user` object. Instead, they contain the raw `username` and
    `account_id` of the user. This is to protect the integrity of the audit
    log even after a user account gets deleted.

    The `changes.assignee` field is deprecated will disappear in the
    future. Use `changes.assignee_account_id` instead.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            issue_id=issue_id,
            client=client,
            q=q,
            sort=sort,
        )
    ).parsed
