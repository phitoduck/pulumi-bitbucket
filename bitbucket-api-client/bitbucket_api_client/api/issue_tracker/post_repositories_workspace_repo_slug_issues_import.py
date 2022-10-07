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
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, IssueJobStatus]]:
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
    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409
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
    """Import issues

     A POST request to this endpoint will import the zip file given by the archive parameter into the
    repository. All
    existing issues will be deleted and replaced by the contents of the imported zip file.

    Imports are done through a multipart/form-data POST. There is one valid and required form field,
    with the name
    \"archive,\" which needs to be a file field:

    ```
    $ curl -u <username> -X POST -F archive=@/path/to/file.zip
    https://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/issues/import
    ```

    When the import job is accepted, here is example output:

    ```
    < HTTP/1.1 202 Accepted

    {
        \"type\": \"issue_job_status\",
        \"status\": \"ACCEPTED\",
        \"phase\": \"Attachments\",
        \"total\": 15,
        \"count\": 0,
        \"percent\": 0
    }
    ```

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
    """Import issues

     A POST request to this endpoint will import the zip file given by the archive parameter into the
    repository. All
    existing issues will be deleted and replaced by the contents of the imported zip file.

    Imports are done through a multipart/form-data POST. There is one valid and required form field,
    with the name
    \"archive,\" which needs to be a file field:

    ```
    $ curl -u <username> -X POST -F archive=@/path/to/file.zip
    https://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/issues/import
    ```

    When the import job is accepted, here is example output:

    ```
    < HTTP/1.1 202 Accepted

    {
        \"type\": \"issue_job_status\",
        \"status\": \"ACCEPTED\",
        \"phase\": \"Attachments\",
        \"total\": 15,
        \"count\": 0,
        \"percent\": 0
    }
    ```

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
    """Import issues

     A POST request to this endpoint will import the zip file given by the archive parameter into the
    repository. All
    existing issues will be deleted and replaced by the contents of the imported zip file.

    Imports are done through a multipart/form-data POST. There is one valid and required form field,
    with the name
    \"archive,\" which needs to be a file field:

    ```
    $ curl -u <username> -X POST -F archive=@/path/to/file.zip
    https://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/issues/import
    ```

    When the import job is accepted, here is example output:

    ```
    < HTTP/1.1 202 Accepted

    {
        \"type\": \"issue_job_status\",
        \"status\": \"ACCEPTED\",
        \"phase\": \"Attachments\",
        \"total\": 15,
        \"count\": 0,
        \"percent\": 0
    }
    ```

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
    """Import issues

     A POST request to this endpoint will import the zip file given by the archive parameter into the
    repository. All
    existing issues will be deleted and replaced by the contents of the imported zip file.

    Imports are done through a multipart/form-data POST. There is one valid and required form field,
    with the name
    \"archive,\" which needs to be a file field:

    ```
    $ curl -u <username> -X POST -F archive=@/path/to/file.zip
    https://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/issues/import
    ```

    When the import job is accepted, here is example output:

    ```
    < HTTP/1.1 202 Accepted

    {
        \"type\": \"issue_job_status\",
        \"status\": \"ACCEPTED\",
        \"phase\": \"Attachments\",
        \"total\": 15,
        \"count\": 0,
        \"percent\": 0
    }
    ```

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
