from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.branching_model_settings import BranchingModelSettings
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/branching-model/settings".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[BranchingModelSettings, Error]]:
    if response.status_code == 200:
        response_200 = BranchingModelSettings.from_dict(response.json())

        return response_200
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


def _build_response(*, response: httpx.Response) -> Response[Union[BranchingModelSettings, Error]]:
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
) -> Response[Union[BranchingModelSettings, Error]]:
    """Get the branching model config for a repository

     Return the branching model configuration for a repository. The returned
    object:

    1. Always has a `development` property for the development branch.
    2. Always a `production` property for the production branch. The
       production branch can be disabled.
    3. The `branch_types` contains all the branch types.

    This is the raw configuration for the branching model. A client
    wishing to see the branching model with its actual current branches may
    find the [active model API](/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-
    workspace-repo-slug-branching-model-get) more useful.

    Example body:

    ```
    {
      \"development\": {
        \"is_valid\": true,
        \"name\": null,
        \"use_mainbranch\": true
      },
      \"production\": {
        \"is_valid\": true,
        \"name\": \"production\",
        \"use_mainbranch\": false,
        \"enabled\": false
      },
      \"branch_types\": [
        {
          \"kind\": \"release\",
          \"enabled\": true,
          \"prefix\": \"release/\"
        },
        {
          \"kind\": \"hotfix\",
          \"enabled\": true,
          \"prefix\": \"hotfix/\"
        },
        {
          \"kind\": \"feature\",
          \"enabled\": true,
          \"prefix\": \"feature/\"
        },
        {
          \"kind\": \"bugfix\",
          \"enabled\": false,
          \"prefix\": \"bugfix/\"
        }
      ],
      \"type\": \"branching_model_settings\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/.../branching-model/settings\"
        }
      }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[BranchingModelSettings, Error]]
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
) -> Optional[Union[BranchingModelSettings, Error]]:
    """Get the branching model config for a repository

     Return the branching model configuration for a repository. The returned
    object:

    1. Always has a `development` property for the development branch.
    2. Always a `production` property for the production branch. The
       production branch can be disabled.
    3. The `branch_types` contains all the branch types.

    This is the raw configuration for the branching model. A client
    wishing to see the branching model with its actual current branches may
    find the [active model API](/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-
    workspace-repo-slug-branching-model-get) more useful.

    Example body:

    ```
    {
      \"development\": {
        \"is_valid\": true,
        \"name\": null,
        \"use_mainbranch\": true
      },
      \"production\": {
        \"is_valid\": true,
        \"name\": \"production\",
        \"use_mainbranch\": false,
        \"enabled\": false
      },
      \"branch_types\": [
        {
          \"kind\": \"release\",
          \"enabled\": true,
          \"prefix\": \"release/\"
        },
        {
          \"kind\": \"hotfix\",
          \"enabled\": true,
          \"prefix\": \"hotfix/\"
        },
        {
          \"kind\": \"feature\",
          \"enabled\": true,
          \"prefix\": \"feature/\"
        },
        {
          \"kind\": \"bugfix\",
          \"enabled\": false,
          \"prefix\": \"bugfix/\"
        }
      ],
      \"type\": \"branching_model_settings\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/.../branching-model/settings\"
        }
      }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[BranchingModelSettings, Error]]
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
) -> Response[Union[BranchingModelSettings, Error]]:
    """Get the branching model config for a repository

     Return the branching model configuration for a repository. The returned
    object:

    1. Always has a `development` property for the development branch.
    2. Always a `production` property for the production branch. The
       production branch can be disabled.
    3. The `branch_types` contains all the branch types.

    This is the raw configuration for the branching model. A client
    wishing to see the branching model with its actual current branches may
    find the [active model API](/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-
    workspace-repo-slug-branching-model-get) more useful.

    Example body:

    ```
    {
      \"development\": {
        \"is_valid\": true,
        \"name\": null,
        \"use_mainbranch\": true
      },
      \"production\": {
        \"is_valid\": true,
        \"name\": \"production\",
        \"use_mainbranch\": false,
        \"enabled\": false
      },
      \"branch_types\": [
        {
          \"kind\": \"release\",
          \"enabled\": true,
          \"prefix\": \"release/\"
        },
        {
          \"kind\": \"hotfix\",
          \"enabled\": true,
          \"prefix\": \"hotfix/\"
        },
        {
          \"kind\": \"feature\",
          \"enabled\": true,
          \"prefix\": \"feature/\"
        },
        {
          \"kind\": \"bugfix\",
          \"enabled\": false,
          \"prefix\": \"bugfix/\"
        }
      ],
      \"type\": \"branching_model_settings\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/.../branching-model/settings\"
        }
      }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[BranchingModelSettings, Error]]
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
) -> Optional[Union[BranchingModelSettings, Error]]:
    """Get the branching model config for a repository

     Return the branching model configuration for a repository. The returned
    object:

    1. Always has a `development` property for the development branch.
    2. Always a `production` property for the production branch. The
       production branch can be disabled.
    3. The `branch_types` contains all the branch types.

    This is the raw configuration for the branching model. A client
    wishing to see the branching model with its actual current branches may
    find the [active model API](/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-
    workspace-repo-slug-branching-model-get) more useful.

    Example body:

    ```
    {
      \"development\": {
        \"is_valid\": true,
        \"name\": null,
        \"use_mainbranch\": true
      },
      \"production\": {
        \"is_valid\": true,
        \"name\": \"production\",
        \"use_mainbranch\": false,
        \"enabled\": false
      },
      \"branch_types\": [
        {
          \"kind\": \"release\",
          \"enabled\": true,
          \"prefix\": \"release/\"
        },
        {
          \"kind\": \"hotfix\",
          \"enabled\": true,
          \"prefix\": \"hotfix/\"
        },
        {
          \"kind\": \"feature\",
          \"enabled\": true,
          \"prefix\": \"feature/\"
        },
        {
          \"kind\": \"bugfix\",
          \"enabled\": false,
          \"prefix\": \"bugfix/\"
        }
      ],
      \"type\": \"branching_model_settings\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/.../branching-model/settings\"
        }
      }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[BranchingModelSettings, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
        )
    ).parsed
