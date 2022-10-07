from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.export_options import ExportOptions
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    json_body: ExportOptions,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/issues/export".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 202:
        response_202 = cast(Any, None)
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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Error]]:
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
    json_body: ExportOptions,
) -> Response[Union[Any, Error]]:
    """Export issues

     A POST request to this endpoint initiates a new background celery task that archives the repo's
    issues.

    For example, you can run:

    curl -u <username> -X POST http://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/
    issues/export

    When the job has been accepted, it will return a 202 (Accepted) along with a unique url to this job
    in the
    'Location' response header. This url is the endpoint for where the user can obtain their zip
    files.\"

    Args:
        workspace (str):
        repo_slug (str):
        json_body (ExportOptions): Options for issue export.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        json_body=json_body,
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
    json_body: ExportOptions,
) -> Optional[Union[Any, Error]]:
    """Export issues

     A POST request to this endpoint initiates a new background celery task that archives the repo's
    issues.

    For example, you can run:

    curl -u <username> -X POST http://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/
    issues/export

    When the job has been accepted, it will return a 202 (Accepted) along with a unique url to this job
    in the
    'Location' response header. This url is the endpoint for where the user can obtain their zip
    files.\"

    Args:
        workspace (str):
        repo_slug (str):
        json_body (ExportOptions): Options for issue export.

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    json_body: ExportOptions,
) -> Response[Union[Any, Error]]:
    """Export issues

     A POST request to this endpoint initiates a new background celery task that archives the repo's
    issues.

    For example, you can run:

    curl -u <username> -X POST http://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/
    issues/export

    When the job has been accepted, it will return a 202 (Accepted) along with a unique url to this job
    in the
    'Location' response header. This url is the endpoint for where the user can obtain their zip
    files.\"

    Args:
        workspace (str):
        repo_slug (str):
        json_body (ExportOptions): Options for issue export.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    json_body: ExportOptions,
) -> Optional[Union[Any, Error]]:
    """Export issues

     A POST request to this endpoint initiates a new background celery task that archives the repo's
    issues.

    For example, you can run:

    curl -u <username> -X POST http://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/
    issues/export

    When the job has been accepted, it will return a 202 (Accepted) along with a unique url to this job
    in the
    'Location' response header. This url is the endpoint for where the user can obtain their zip
    files.\"

    Args:
        workspace (str):
        repo_slug (str):
        json_body (ExportOptions): Options for issue export.

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            json_body=json_body,
        )
    ).parsed
