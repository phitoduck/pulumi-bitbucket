from typing import Any, Dict, Optional, Union, cast

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
    url = "{}/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, issue_id=issue_id
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
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
    issue_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error]]:
    """Upload an attachment to an issue

     Upload new issue attachments.

    To upload files, perform a `multipart/form-data` POST containing one
    or more file fields.

    When a file is uploaded with the same name as an existing attachment,
    then the existing file will be replaced.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Returns:
        Response[Union[Any, Error]]
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
) -> Optional[Union[Any, Error]]:
    """Upload an attachment to an issue

     Upload new issue attachments.

    To upload files, perform a `multipart/form-data` POST containing one
    or more file fields.

    When a file is uploaded with the same name as an existing attachment,
    then the existing file will be replaced.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Returns:
        Response[Union[Any, Error]]
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
) -> Response[Union[Any, Error]]:
    """Upload an attachment to an issue

     Upload new issue attachments.

    To upload files, perform a `multipart/form-data` POST containing one
    or more file fields.

    When a file is uploaded with the same name as an existing attachment,
    then the existing file will be replaced.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Returns:
        Response[Union[Any, Error]]
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
) -> Optional[Union[Any, Error]]:
    """Upload an attachment to an issue

     Upload new issue attachments.

    To upload files, perform a `multipart/form-data` POST containing one
    or more file fields.

    When a file is uploaded with the same name as an existing attachment,
    then the existing file will be replaced.

    Args:
        workspace (str):
        repo_slug (str):
        issue_id (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            issue_id=issue_id,
            client=client,
        )
    ).parsed
