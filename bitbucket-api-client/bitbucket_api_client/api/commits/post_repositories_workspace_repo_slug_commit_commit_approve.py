from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.participant import Participant
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/commit/{commit}/approve".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, commit=commit
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, Participant]]:
    if response.status_code == 200:
        response_200 = Participant.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, Participant]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, Participant]]:
    """Approve a commit

     Approve the specified commit as the authenticated user.

    This operation is only available to users that have explicit access to
    the repository. In contrast, just the fact that a repository is
    publicly accessible to users does not give them the ability to approve
    commits.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):

    Returns:
        Response[Union[Error, Participant]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
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
    commit: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, Participant]]:
    """Approve a commit

     Approve the specified commit as the authenticated user.

    This operation is only available to users that have explicit access to
    the repository. In contrast, just the fact that a repository is
    publicly accessible to users does not give them the ability to approve
    commits.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):

    Returns:
        Response[Union[Error, Participant]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, Participant]]:
    """Approve a commit

     Approve the specified commit as the authenticated user.

    This operation is only available to users that have explicit access to
    the repository. In contrast, just the fact that a repository is
    publicly accessible to users does not give them the ability to approve
    commits.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):

    Returns:
        Response[Union[Error, Participant]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, Participant]]:
    """Approve a commit

     Approve the specified commit as the authenticated user.

    This operation is only available to users that have explicit access to
    the repository. In contrast, just the fact that a repository is
    publicly accessible to users does not give them the ability to approve
    commits.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):

    Returns:
        Response[Union[Error, Participant]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            client=client,
        )
    ).parsed
