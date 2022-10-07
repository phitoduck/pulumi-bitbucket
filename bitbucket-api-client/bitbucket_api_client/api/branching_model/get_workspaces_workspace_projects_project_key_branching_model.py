from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.project_branching_model import ProjectBranchingModel
from ...types import Response


def _get_kwargs(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/projects/{project_key}/branching-model".format(
        client.base_url, workspace=workspace, project_key=project_key
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, ProjectBranchingModel]]:
    if response.status_code == 200:
        response_200 = ProjectBranchingModel.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Error, ProjectBranchingModel]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, ProjectBranchingModel]]:
    """Get the branching model for a project

     Return the branching model set at the project level. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-workspaces-workspace-projects-project-key-branching-model-settings-get)
    API.

    The returned object:

    1. Always has a `development` property. `development.name` is
       the user-specified branch that can be inherited by an individual repository's
       branching model.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.name` is the user-specified branch that can be
       inherited by an individual repository's branching model.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Example body:

    ```
    {
      \"development\": {
        \"name\": \"master\",
        \"use_mainbranch\": true
      },
      \"production\": {
        \"name\": \"production\",
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
      \"type\": \"project_branching_model\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/.../branching-model\"
        }
      }
    }
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Union[Error, ProjectBranchingModel]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, ProjectBranchingModel]]:
    """Get the branching model for a project

     Return the branching model set at the project level. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-workspaces-workspace-projects-project-key-branching-model-settings-get)
    API.

    The returned object:

    1. Always has a `development` property. `development.name` is
       the user-specified branch that can be inherited by an individual repository's
       branching model.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.name` is the user-specified branch that can be
       inherited by an individual repository's branching model.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Example body:

    ```
    {
      \"development\": {
        \"name\": \"master\",
        \"use_mainbranch\": true
      },
      \"production\": {
        \"name\": \"production\",
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
      \"type\": \"project_branching_model\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/.../branching-model\"
        }
      }
    }
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Union[Error, ProjectBranchingModel]]
    """

    return sync_detailed(
        workspace=workspace,
        project_key=project_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, ProjectBranchingModel]]:
    """Get the branching model for a project

     Return the branching model set at the project level. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-workspaces-workspace-projects-project-key-branching-model-settings-get)
    API.

    The returned object:

    1. Always has a `development` property. `development.name` is
       the user-specified branch that can be inherited by an individual repository's
       branching model.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.name` is the user-specified branch that can be
       inherited by an individual repository's branching model.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Example body:

    ```
    {
      \"development\": {
        \"name\": \"master\",
        \"use_mainbranch\": true
      },
      \"production\": {
        \"name\": \"production\",
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
      \"type\": \"project_branching_model\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/.../branching-model\"
        }
      }
    }
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Union[Error, ProjectBranchingModel]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, ProjectBranchingModel]]:
    """Get the branching model for a project

     Return the branching model set at the project level. This view is
    read-only. The branching model settings can be changed using the
    [settings](#api-workspaces-workspace-projects-project-key-branching-model-settings-get)
    API.

    The returned object:

    1. Always has a `development` property. `development.name` is
       the user-specified branch that can be inherited by an individual repository's
       branching model.
    2. Might have a `production` property. `production` will not
       be present when `production` is disabled.
       `production.name` is the user-specified branch that can be
       inherited by an individual repository's branching model.
    3. Always has a `branch_types` array which contains all enabled branch
       types.

    Example body:

    ```
    {
      \"development\": {
        \"name\": \"master\",
        \"use_mainbranch\": true
      },
      \"production\": {
        \"name\": \"production\",
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
      \"type\": \"project_branching_model\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/.../branching-model\"
        }
      }
    }
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Union[Error, ProjectBranchingModel]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            project_key=project_key,
            client=client,
        )
    ).parsed
