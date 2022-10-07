from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/branching-model".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug
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
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
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
) -> Response[Error]:
    """Get the branching model for a repository

     Return the branching model as applied to the repository. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-repositories-workspace-repo-slug-branching-model-settings-get) API.

    The returned object:

    1. Always has a `development` property. `development.branch` contains
       the actual repository branch object that is considered to be the
       `development` branch. `development.branch` will not be present
       if it does not exist.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.branch` contains the actual branch object that is
       considered to be the `production` branch. `production.branch` will
       not be present if it does not exist.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Example body:

    ```
    {
      \"development\": {
        \"name\": \"master\",
        \"branch\": {
          \"type\": \"branch\",
          \"name\": \"master\",
          \"target\": {
            \"hash\": \"16dffcb0de1b22e249db6799532074cf32efe80f\"
          }
        },
        \"use_mainbranch\": true
      },
      \"production\": {
        \"name\": \"production\",
        \"branch\": {
          \"type\": \"branch\",
          \"name\": \"production\",
          \"target\": {
            \"hash\": \"16dffcb0de1b22e249db6799532074cf32efe80f\"
          }
        },
        \"use_mainbranch\": false
      },
      \"branch_types\": [
        {
          \"kind\": \"release\",
          \"prefix\": \"release/\"
        },
        {
          \"kind\": \"hotfix\",
          \"prefix\": \"hotfix/\"
        },
        {
          \"kind\": \"feature\",
          \"prefix\": \"feature/\"
        },
        {
          \"kind\": \"bugfix\",
          \"prefix\": \"bugfix/\"
        }
      ],
      \"type\": \"branching_model\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/.../branching-model\"
        }
      }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
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
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Get the branching model for a repository

     Return the branching model as applied to the repository. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-repositories-workspace-repo-slug-branching-model-settings-get) API.

    The returned object:

    1. Always has a `development` property. `development.branch` contains
       the actual repository branch object that is considered to be the
       `development` branch. `development.branch` will not be present
       if it does not exist.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.branch` contains the actual branch object that is
       considered to be the `production` branch. `production.branch` will
       not be present if it does not exist.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Example body:

    ```
    {
      \"development\": {
        \"name\": \"master\",
        \"branch\": {
          \"type\": \"branch\",
          \"name\": \"master\",
          \"target\": {
            \"hash\": \"16dffcb0de1b22e249db6799532074cf32efe80f\"
          }
        },
        \"use_mainbranch\": true
      },
      \"production\": {
        \"name\": \"production\",
        \"branch\": {
          \"type\": \"branch\",
          \"name\": \"production\",
          \"target\": {
            \"hash\": \"16dffcb0de1b22e249db6799532074cf32efe80f\"
          }
        },
        \"use_mainbranch\": false
      },
      \"branch_types\": [
        {
          \"kind\": \"release\",
          \"prefix\": \"release/\"
        },
        {
          \"kind\": \"hotfix\",
          \"prefix\": \"hotfix/\"
        },
        {
          \"kind\": \"feature\",
          \"prefix\": \"feature/\"
        },
        {
          \"kind\": \"bugfix\",
          \"prefix\": \"bugfix/\"
        }
      ],
      \"type\": \"branching_model\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/.../branching-model\"
        }
      }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Get the branching model for a repository

     Return the branching model as applied to the repository. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-repositories-workspace-repo-slug-branching-model-settings-get) API.

    The returned object:

    1. Always has a `development` property. `development.branch` contains
       the actual repository branch object that is considered to be the
       `development` branch. `development.branch` will not be present
       if it does not exist.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.branch` contains the actual branch object that is
       considered to be the `production` branch. `production.branch` will
       not be present if it does not exist.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Example body:

    ```
    {
      \"development\": {
        \"name\": \"master\",
        \"branch\": {
          \"type\": \"branch\",
          \"name\": \"master\",
          \"target\": {
            \"hash\": \"16dffcb0de1b22e249db6799532074cf32efe80f\"
          }
        },
        \"use_mainbranch\": true
      },
      \"production\": {
        \"name\": \"production\",
        \"branch\": {
          \"type\": \"branch\",
          \"name\": \"production\",
          \"target\": {
            \"hash\": \"16dffcb0de1b22e249db6799532074cf32efe80f\"
          }
        },
        \"use_mainbranch\": false
      },
      \"branch_types\": [
        {
          \"kind\": \"release\",
          \"prefix\": \"release/\"
        },
        {
          \"kind\": \"hotfix\",
          \"prefix\": \"hotfix/\"
        },
        {
          \"kind\": \"feature\",
          \"prefix\": \"feature/\"
        },
        {
          \"kind\": \"bugfix\",
          \"prefix\": \"bugfix/\"
        }
      ],
      \"type\": \"branching_model\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/.../branching-model\"
        }
      }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Get the branching model for a repository

     Return the branching model as applied to the repository. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-repositories-workspace-repo-slug-branching-model-settings-get) API.

    The returned object:

    1. Always has a `development` property. `development.branch` contains
       the actual repository branch object that is considered to be the
       `development` branch. `development.branch` will not be present
       if it does not exist.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.branch` contains the actual branch object that is
       considered to be the `production` branch. `production.branch` will
       not be present if it does not exist.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Example body:

    ```
    {
      \"development\": {
        \"name\": \"master\",
        \"branch\": {
          \"type\": \"branch\",
          \"name\": \"master\",
          \"target\": {
            \"hash\": \"16dffcb0de1b22e249db6799532074cf32efe80f\"
          }
        },
        \"use_mainbranch\": true
      },
      \"production\": {
        \"name\": \"production\",
        \"branch\": {
          \"type\": \"branch\",
          \"name\": \"production\",
          \"target\": {
            \"hash\": \"16dffcb0de1b22e249db6799532074cf32efe80f\"
          }
        },
        \"use_mainbranch\": false
      },
      \"branch_types\": [
        {
          \"kind\": \"release\",
          \"prefix\": \"release/\"
        },
        {
          \"kind\": \"hotfix\",
          \"prefix\": \"hotfix/\"
        },
        {
          \"kind\": \"feature\",
          \"prefix\": \"feature/\"
        },
        {
          \"kind\": \"bugfix\",
          \"prefix\": \"bugfix/\"
        }
      ],
      \"type\": \"branching_model\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/.../branching-model\"
        }
      }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
        )
    ).parsed
