from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.pull_request_merge_parameters import PullRequestMergeParameters
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
    json_body: PullRequestMergeParameters,
    async_: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, pull_request_id=pull_request_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["async"] = async_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202
    if response.status_code == 555:
        response_555 = Error.from_dict(response.json())

        return response_555
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
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
    json_body: PullRequestMergeParameters,
    async_: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, Error]]:
    """Merge a pull request

     Merges the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        async_ (Union[Unset, None, bool]):
        json_body (PullRequestMergeParameters): The metadata that describes a pull request merge.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        client=client,
        json_body=json_body,
        async_=async_,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
    json_body: PullRequestMergeParameters,
    async_: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, Error]]:
    """Merge a pull request

     Merges the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        async_ (Union[Unset, None, bool]):
        json_body (PullRequestMergeParameters): The metadata that describes a pull request merge.

    Returns:
        Response[Union[Any, Error]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        client=client,
        json_body=json_body,
        async_=async_,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
    json_body: PullRequestMergeParameters,
    async_: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, Error]]:
    """Merge a pull request

     Merges the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        async_ (Union[Unset, None, bool]):
        json_body (PullRequestMergeParameters): The metadata that describes a pull request merge.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        client=client,
        json_body=json_body,
        async_=async_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
    json_body: PullRequestMergeParameters,
    async_: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, Error]]:
    """Merge a pull request

     Merges the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        async_ (Union[Unset, None, bool]):
        json_body (PullRequestMergeParameters): The metadata that describes a pull request merge.

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            pull_request_id=pull_request_id,
            client=client,
            json_body=json_body,
            async_=async_,
        )
    ).parsed
