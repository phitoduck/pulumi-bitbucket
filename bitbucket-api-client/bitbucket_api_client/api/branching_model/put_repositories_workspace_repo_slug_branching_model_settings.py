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
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[BranchingModelSettings, Error]]:
    if response.status_code == 200:
        response_200 = BranchingModelSettings.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
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
    """Update the branching model config for a repository

     Update the branching model configuration for a repository.

    The `development` branch can be configured to a specific branch or to
    track the main branch. When set to a specific branch it must
    currently exist. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `development` property will leave the development branch unchanged.

    It is possible for the `development` branch to be invalid. This
    happens when it points at a specific branch that has been
    deleted. This is indicated in the `is_valid` field for the branch. It is
    not possible to update the settings for `development` if that
    would leave the branch in an invalid state. Such a request will be
    rejected.

    The `production` branch can be a specific branch, the main
    branch or disabled. When set to a specific branch it must currently
    exist. The `enabled` property can be used to enable (`true`) or
    disable (`false`) it. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `production` property will leave the production branch unchanged.

    It is possible for the `production` branch to be invalid. This
    happens when it points at a specific branch that has been
    deleted. This is indicated in the `is_valid` field for the branch. A
    request that would leave `production` enabled and invalid will be
    rejected. It is possible to update `production` and make it invalid if
    it would also be left disabled.

    The `branch_types` property contains the branch types to be updated.
    Only the branch types passed will be updated. All updates will be
    rejected if it would leave the branching model in an invalid state.
    For branch types this means that:

    1. The prefixes for all enabled branch types are valid. For example,
       it is not possible to use '*' inside a Git prefix.
    2. A prefix of an enabled branch type must not be a prefix of another
       enabled branch type. This is to ensure that a branch can be easily
       classified by its prefix unambiguously.

    It is possible to store an invalid prefix if that branch type would be
    left disabled. Only the passed properties will be updated. The
    properties not passed will be left unchanged. Each branch type must
    have a `kind` property to identify it.

    Example Body:

    ```
        {
          \"development\": {
            \"use_mainbranch\": true
          },
          \"production\": {
            \"enabled\": true,
            \"use_mainbranch\": false,
            \"name\": \"production\"
          },
          \"branch_types\": [
            {
              \"kind\": \"bugfix\",
              \"enabled\": true,
              \"prefix\": \"bugfix/\"
            },
            {
              \"kind\": \"feature\",
              \"enabled\": true,
              \"prefix\": \"feature/\"
            },
            {
              \"kind\": \"hotfix\",
              \"prefix\": \"hotfix/\"
            },
            {
              \"kind\": \"release\",
              \"enabled\": false,
            }
          ]
        }
    ```

    There is currently a side effect when using this API endpoint. If the
    repository is inheriting branching model settings from its project,
    updating the branching model for this repository will disable the
    project setting inheritance.


    We have deprecated this side effect and will remove it on 1 August 2022.

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
    """Update the branching model config for a repository

     Update the branching model configuration for a repository.

    The `development` branch can be configured to a specific branch or to
    track the main branch. When set to a specific branch it must
    currently exist. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `development` property will leave the development branch unchanged.

    It is possible for the `development` branch to be invalid. This
    happens when it points at a specific branch that has been
    deleted. This is indicated in the `is_valid` field for the branch. It is
    not possible to update the settings for `development` if that
    would leave the branch in an invalid state. Such a request will be
    rejected.

    The `production` branch can be a specific branch, the main
    branch or disabled. When set to a specific branch it must currently
    exist. The `enabled` property can be used to enable (`true`) or
    disable (`false`) it. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `production` property will leave the production branch unchanged.

    It is possible for the `production` branch to be invalid. This
    happens when it points at a specific branch that has been
    deleted. This is indicated in the `is_valid` field for the branch. A
    request that would leave `production` enabled and invalid will be
    rejected. It is possible to update `production` and make it invalid if
    it would also be left disabled.

    The `branch_types` property contains the branch types to be updated.
    Only the branch types passed will be updated. All updates will be
    rejected if it would leave the branching model in an invalid state.
    For branch types this means that:

    1. The prefixes for all enabled branch types are valid. For example,
       it is not possible to use '*' inside a Git prefix.
    2. A prefix of an enabled branch type must not be a prefix of another
       enabled branch type. This is to ensure that a branch can be easily
       classified by its prefix unambiguously.

    It is possible to store an invalid prefix if that branch type would be
    left disabled. Only the passed properties will be updated. The
    properties not passed will be left unchanged. Each branch type must
    have a `kind` property to identify it.

    Example Body:

    ```
        {
          \"development\": {
            \"use_mainbranch\": true
          },
          \"production\": {
            \"enabled\": true,
            \"use_mainbranch\": false,
            \"name\": \"production\"
          },
          \"branch_types\": [
            {
              \"kind\": \"bugfix\",
              \"enabled\": true,
              \"prefix\": \"bugfix/\"
            },
            {
              \"kind\": \"feature\",
              \"enabled\": true,
              \"prefix\": \"feature/\"
            },
            {
              \"kind\": \"hotfix\",
              \"prefix\": \"hotfix/\"
            },
            {
              \"kind\": \"release\",
              \"enabled\": false,
            }
          ]
        }
    ```

    There is currently a side effect when using this API endpoint. If the
    repository is inheriting branching model settings from its project,
    updating the branching model for this repository will disable the
    project setting inheritance.


    We have deprecated this side effect and will remove it on 1 August 2022.

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
    """Update the branching model config for a repository

     Update the branching model configuration for a repository.

    The `development` branch can be configured to a specific branch or to
    track the main branch. When set to a specific branch it must
    currently exist. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `development` property will leave the development branch unchanged.

    It is possible for the `development` branch to be invalid. This
    happens when it points at a specific branch that has been
    deleted. This is indicated in the `is_valid` field for the branch. It is
    not possible to update the settings for `development` if that
    would leave the branch in an invalid state. Such a request will be
    rejected.

    The `production` branch can be a specific branch, the main
    branch or disabled. When set to a specific branch it must currently
    exist. The `enabled` property can be used to enable (`true`) or
    disable (`false`) it. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `production` property will leave the production branch unchanged.

    It is possible for the `production` branch to be invalid. This
    happens when it points at a specific branch that has been
    deleted. This is indicated in the `is_valid` field for the branch. A
    request that would leave `production` enabled and invalid will be
    rejected. It is possible to update `production` and make it invalid if
    it would also be left disabled.

    The `branch_types` property contains the branch types to be updated.
    Only the branch types passed will be updated. All updates will be
    rejected if it would leave the branching model in an invalid state.
    For branch types this means that:

    1. The prefixes for all enabled branch types are valid. For example,
       it is not possible to use '*' inside a Git prefix.
    2. A prefix of an enabled branch type must not be a prefix of another
       enabled branch type. This is to ensure that a branch can be easily
       classified by its prefix unambiguously.

    It is possible to store an invalid prefix if that branch type would be
    left disabled. Only the passed properties will be updated. The
    properties not passed will be left unchanged. Each branch type must
    have a `kind` property to identify it.

    Example Body:

    ```
        {
          \"development\": {
            \"use_mainbranch\": true
          },
          \"production\": {
            \"enabled\": true,
            \"use_mainbranch\": false,
            \"name\": \"production\"
          },
          \"branch_types\": [
            {
              \"kind\": \"bugfix\",
              \"enabled\": true,
              \"prefix\": \"bugfix/\"
            },
            {
              \"kind\": \"feature\",
              \"enabled\": true,
              \"prefix\": \"feature/\"
            },
            {
              \"kind\": \"hotfix\",
              \"prefix\": \"hotfix/\"
            },
            {
              \"kind\": \"release\",
              \"enabled\": false,
            }
          ]
        }
    ```

    There is currently a side effect when using this API endpoint. If the
    repository is inheriting branching model settings from its project,
    updating the branching model for this repository will disable the
    project setting inheritance.


    We have deprecated this side effect and will remove it on 1 August 2022.

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
    """Update the branching model config for a repository

     Update the branching model configuration for a repository.

    The `development` branch can be configured to a specific branch or to
    track the main branch. When set to a specific branch it must
    currently exist. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `development` property will leave the development branch unchanged.

    It is possible for the `development` branch to be invalid. This
    happens when it points at a specific branch that has been
    deleted. This is indicated in the `is_valid` field for the branch. It is
    not possible to update the settings for `development` if that
    would leave the branch in an invalid state. Such a request will be
    rejected.

    The `production` branch can be a specific branch, the main
    branch or disabled. When set to a specific branch it must currently
    exist. The `enabled` property can be used to enable (`true`) or
    disable (`false`) it. Only the passed properties will be updated. The
    properties not passed will be left unchanged. A request without a
    `production` property will leave the production branch unchanged.

    It is possible for the `production` branch to be invalid. This
    happens when it points at a specific branch that has been
    deleted. This is indicated in the `is_valid` field for the branch. A
    request that would leave `production` enabled and invalid will be
    rejected. It is possible to update `production` and make it invalid if
    it would also be left disabled.

    The `branch_types` property contains the branch types to be updated.
    Only the branch types passed will be updated. All updates will be
    rejected if it would leave the branching model in an invalid state.
    For branch types this means that:

    1. The prefixes for all enabled branch types are valid. For example,
       it is not possible to use '*' inside a Git prefix.
    2. A prefix of an enabled branch type must not be a prefix of another
       enabled branch type. This is to ensure that a branch can be easily
       classified by its prefix unambiguously.

    It is possible to store an invalid prefix if that branch type would be
    left disabled. Only the passed properties will be updated. The
    properties not passed will be left unchanged. Each branch type must
    have a `kind` property to identify it.

    Example Body:

    ```
        {
          \"development\": {
            \"use_mainbranch\": true
          },
          \"production\": {
            \"enabled\": true,
            \"use_mainbranch\": false,
            \"name\": \"production\"
          },
          \"branch_types\": [
            {
              \"kind\": \"bugfix\",
              \"enabled\": true,
              \"prefix\": \"bugfix/\"
            },
            {
              \"kind\": \"feature\",
              \"enabled\": true,
              \"prefix\": \"feature/\"
            },
            {
              \"kind\": \"hotfix\",
              \"prefix\": \"hotfix/\"
            },
            {
              \"kind\": \"release\",
              \"enabled\": false,
            }
          ]
        }
    ```

    There is currently a side effect when using this API endpoint. If the
    repository is inheriting branching model settings from its project,
    updating the branching model for this repository will disable the
    project setting inheritance.


    We have deprecated this side effect and will remove it on 1 August 2022.

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
