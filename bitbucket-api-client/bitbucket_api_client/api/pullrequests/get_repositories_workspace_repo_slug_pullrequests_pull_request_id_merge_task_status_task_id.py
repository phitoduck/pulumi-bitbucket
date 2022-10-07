from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, pull_request_id=pull_request_id, task_id=task_id
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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get the merge task status for a pull request

     When merging a pull request takes too long, the client receives a
    task ID along with a 202 status code. The task ID can be used in a call
    to this endpoint to check the status of a merge task.

    ```
    curl -X GET
    https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>
    ```

    If the merge task is not yet finished, a PENDING status will be returned.

    ```
    HTTP/2 200
    {
        \"task_status\": \"PENDING\",
        \"links\": {
            \"self\": {
                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>\"
            }
        }
    }
    ```

    If the merge was successful, a SUCCESS status will be returned.

    ```
    HTTP/2 200
    {
        \"task_status\": \"SUCCESS\",
        \"links\": {
            \"self\": {
                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>\"
            }
        },
        \"merge_result\": <the merged pull request object>
    }
    ```

    If the merge task failed, an error will be returned.

    ```
    {
        \"type\": \"error\",
        \"error\": {
            \"message\": \"<error message>\"
        }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        task_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        task_id=task_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get the merge task status for a pull request

     When merging a pull request takes too long, the client receives a
    task ID along with a 202 status code. The task ID can be used in a call
    to this endpoint to check the status of a merge task.

    ```
    curl -X GET
    https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>
    ```

    If the merge task is not yet finished, a PENDING status will be returned.

    ```
    HTTP/2 200
    {
        \"task_status\": \"PENDING\",
        \"links\": {
            \"self\": {
                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>\"
            }
        }
    }
    ```

    If the merge was successful, a SUCCESS status will be returned.

    ```
    HTTP/2 200
    {
        \"task_status\": \"SUCCESS\",
        \"links\": {
            \"self\": {
                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>\"
            }
        },
        \"merge_result\": <the merged pull request object>
    }
    ```

    If the merge task failed, an error will be returned.

    ```
    {
        \"type\": \"error\",
        \"error\": {
            \"message\": \"<error message>\"
        }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        task_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        task_id=task_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
