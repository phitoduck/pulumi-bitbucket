from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/issues/{issue_id}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, issue_id=issue_id
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
    issue_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Update an issue

     Modifies the issue.

    ```
    $ curl https://api.bitbucket.org/2.0/repostories/evzijst/dogslow/issues/123 \
      -u evzijst -s -X PUT -H 'Content-Type: application/json' \
      -d '{
      \"title\": \"Updated title\",
      \"assignee\": {
        \"account_id\": \"5d5355e8c6b9320d9ea5b28d\"
      },
      \"priority\": \"minor\",
      \"version\": {
        \"name\": \"1.0\"
      },
      \"component\": null
    }'
    ```

    This example changes the `title`, `assignee`, `priority` and the
    `version`. It also removes the value of the `component` from the issue
    by setting the field to `null`. Any field not present keeps its existing
    value.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
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
    issue_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Update an issue

     Modifies the issue.

    ```
    $ curl https://api.bitbucket.org/2.0/repostories/evzijst/dogslow/issues/123 \
      -u evzijst -s -X PUT -H 'Content-Type: application/json' \
      -d '{
      \"title\": \"Updated title\",
      \"assignee\": {
        \"account_id\": \"5d5355e8c6b9320d9ea5b28d\"
      },
      \"priority\": \"minor\",
      \"version\": {
        \"name\": \"1.0\"
      },
      \"component\": null
    }'
    ```

    This example changes the `title`, `assignee`, `priority` and the
    `version`. It also removes the value of the `component` from the issue
    by setting the field to `null`. Any field not present keeps its existing
    value.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    issue_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Update an issue

     Modifies the issue.

    ```
    $ curl https://api.bitbucket.org/2.0/repostories/evzijst/dogslow/issues/123 \
      -u evzijst -s -X PUT -H 'Content-Type: application/json' \
      -d '{
      \"title\": \"Updated title\",
      \"assignee\": {
        \"account_id\": \"5d5355e8c6b9320d9ea5b28d\"
      },
      \"priority\": \"minor\",
      \"version\": {
        \"name\": \"1.0\"
      },
      \"component\": null
    }'
    ```

    This example changes the `title`, `assignee`, `priority` and the
    `version`. It also removes the value of the `component` from the issue
    by setting the field to `null`. Any field not present keeps its existing
    value.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        issue_id=issue_id,
        client=client,
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
) -> Optional[Error]:
    """Update an issue

     Modifies the issue.

    ```
    $ curl https://api.bitbucket.org/2.0/repostories/evzijst/dogslow/issues/123 \
      -u evzijst -s -X PUT -H 'Content-Type: application/json' \
      -d '{
      \"title\": \"Updated title\",
      \"assignee\": {
        \"account_id\": \"5d5355e8c6b9320d9ea5b28d\"
      },
      \"priority\": \"minor\",
      \"version\": {
        \"name\": \"1.0\"
      },
      \"component\": null
    }'
    ```

    This example changes the `title`, `assignee`, `priority` and the
    `version`. It also removes the value of the `component` from the issue
    by setting the field to `null`. Any field not present keeps its existing
    value.

    Each time an issue is edited in the UI or through the API, an immutable
    change record is created under the `/issues/123/changes` endpoint. It
    also has a comment associated with the change.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            issue_id=issue_id,
            client=client,
        )
    ).parsed
