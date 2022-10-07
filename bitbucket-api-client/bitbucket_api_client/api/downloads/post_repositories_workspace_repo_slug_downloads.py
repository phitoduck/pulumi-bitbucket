from typing import Any, Dict, Optional, Union, cast

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
    url = "{}/repositories/{workspace}/{repo_slug}/downloads".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 406:
        response_406 = Error.from_dict(response.json())

        return response_406
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
) -> Response[Union[Any, Error]]:
    """Upload a download artifact

     Upload new download artifacts.

    To upload files, perform a `multipart/form-data` POST containing one
    or more `files` fields:

        $ echo Hello World > hello.txt
        $ curl -s -u evzijst -X POST https://api.bitbucket.org/2.0/repositories/evzijst/git-
    tests/downloads -F files=@hello.txt

    When a file is uploaded with the same name as an existing artifact,
    then the existing file will be replaced.

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[Any, Error]]
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
) -> Optional[Union[Any, Error]]:
    """Upload a download artifact

     Upload new download artifacts.

    To upload files, perform a `multipart/form-data` POST containing one
    or more `files` fields:

        $ echo Hello World > hello.txt
        $ curl -s -u evzijst -X POST https://api.bitbucket.org/2.0/repositories/evzijst/git-
    tests/downloads -F files=@hello.txt

    When a file is uploaded with the same name as an existing artifact,
    then the existing file will be replaced.

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[Any, Error]]
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
) -> Response[Union[Any, Error]]:
    """Upload a download artifact

     Upload new download artifacts.

    To upload files, perform a `multipart/form-data` POST containing one
    or more `files` fields:

        $ echo Hello World > hello.txt
        $ curl -s -u evzijst -X POST https://api.bitbucket.org/2.0/repositories/evzijst/git-
    tests/downloads -F files=@hello.txt

    When a file is uploaded with the same name as an existing artifact,
    then the existing file will be replaced.

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[Any, Error]]
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
) -> Optional[Union[Any, Error]]:
    """Upload a download artifact

     Upload new download artifacts.

    To upload files, perform a `multipart/form-data` POST containing one
    or more `files` fields:

        $ echo Hello World > hello.txt
        $ curl -s -u evzijst -X POST https://api.bitbucket.org/2.0/repositories/evzijst/git-
    tests/downloads -F files=@hello.txt

    When a file is uploaded with the same name as an existing artifact,
    then the existing file will be replaced.

    Args:
        workspace (str):
        repo_slug (str):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
        )
    ).parsed
