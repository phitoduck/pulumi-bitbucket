from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.issue_job_status import IssueJobStatus
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/issues/import".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, IssueJobStatus]]:
    if response.status_code == 200:
        response_200 = IssueJobStatus.from_dict(response.json())

        return response_200
    if response.status_code == 202:
        response_202 = IssueJobStatus.from_dict(response.json())

        return response_202
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


def _build_response(*, response: httpx.Response) -> Response[Union[Error, IssueJobStatus]]:
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
) -> Response[Union[Error, IssueJobStatus]]:
    """Check issue import status

     When using GET, this endpoint reports the status of the current import task. Request example:

    ```
    $ curl -u <username> -X GET
    https://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/issues/import
    ```

    After the job has been scheduled, but before it starts executing, this endpoint's response is:

    ```
    < HTTP/1.1 202 Accepted
    {
        \"type\": \"issue_job_status\",
        \"status\": \"PENDING\",
        \"phase\": \"Attachments\",
        \"total\": 15,
        \"count\": 0,
        \"percent\": 0
    }
    ```

    Once it starts running, it is a 202 response with status STARTED and progress filled.

    After it is finished, it becomes a 200 response with status SUCCESS or FAILURE.

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[Error, IssueJobStatus]]
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
) -> Optional[Union[Error, IssueJobStatus]]:
    """Check issue import status

     When using GET, this endpoint reports the status of the current import task. Request example:

    ```
    $ curl -u <username> -X GET
    https://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/issues/import
    ```

    After the job has been scheduled, but before it starts executing, this endpoint's response is:

    ```
    < HTTP/1.1 202 Accepted
    {
        \"type\": \"issue_job_status\",
        \"status\": \"PENDING\",
        \"phase\": \"Attachments\",
        \"total\": 15,
        \"count\": 0,
        \"percent\": 0
    }
    ```

    Once it starts running, it is a 202 response with status STARTED and progress filled.

    After it is finished, it becomes a 200 response with status SUCCESS or FAILURE.

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[Error, IssueJobStatus]]
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
) -> Response[Union[Error, IssueJobStatus]]:
    """Check issue import status

     When using GET, this endpoint reports the status of the current import task. Request example:

    ```
    $ curl -u <username> -X GET
    https://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/issues/import
    ```

    After the job has been scheduled, but before it starts executing, this endpoint's response is:

    ```
    < HTTP/1.1 202 Accepted
    {
        \"type\": \"issue_job_status\",
        \"status\": \"PENDING\",
        \"phase\": \"Attachments\",
        \"total\": 15,
        \"count\": 0,
        \"percent\": 0
    }
    ```

    Once it starts running, it is a 202 response with status STARTED and progress filled.

    After it is finished, it becomes a 200 response with status SUCCESS or FAILURE.

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[Error, IssueJobStatus]]
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
) -> Optional[Union[Error, IssueJobStatus]]:
    """Check issue import status

     When using GET, this endpoint reports the status of the current import task. Request example:

    ```
    $ curl -u <username> -X GET
    https://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/issues/import
    ```

    After the job has been scheduled, but before it starts executing, this endpoint's response is:

    ```
    < HTTP/1.1 202 Accepted
    {
        \"type\": \"issue_job_status\",
        \"status\": \"PENDING\",
        \"phase\": \"Attachments\",
        \"total\": 15,
        \"count\": 0,
        \"percent\": 0
    }
    ```

    Once it starts running, it is a 202 response with status STARTED and progress filled.

    After it is finished, it becomes a 200 response with status SUCCESS or FAILURE.

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[Error, IssueJobStatus]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
        )
    ).parsed
