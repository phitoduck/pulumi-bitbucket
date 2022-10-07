from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/refs".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["q"] = q

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
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
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List branches and tags

     Returns the branches and tags in the repository.

    By default, results will be in the order the underlying source control system returns them and
    identical to
    the ordering one sees when running \"$ git show-ref\". Note that this follows simple
    lexical ordering of the ref names.

    This can be undesirable as it does apply any natural sorting semantics, meaning for instance that
    refs are
    sorted [\"branch1\", \"branch10\", \"branch2\", \"v10\", \"v11\", \"v9\"] instead of [\"branch1\",
    \"branch2\",
    \"branch10\", \"v9\", \"v10\", \"v11\"].

    Sorting can be changed using the ?sort= query parameter. When using ?sort=name to explicitly sort on
    ref name,
    Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.

    Args:
        workspace (str):
        repo_slug (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        q=q,
        sort=sort,
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
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List branches and tags

     Returns the branches and tags in the repository.

    By default, results will be in the order the underlying source control system returns them and
    identical to
    the ordering one sees when running \"$ git show-ref\". Note that this follows simple
    lexical ordering of the ref names.

    This can be undesirable as it does apply any natural sorting semantics, meaning for instance that
    refs are
    sorted [\"branch1\", \"branch10\", \"branch2\", \"v10\", \"v11\", \"v9\"] instead of [\"branch1\",
    \"branch2\",
    \"branch10\", \"v9\", \"v10\", \"v11\"].

    Sorting can be changed using the ?sort= query parameter. When using ?sort=name to explicitly sort on
    ref name,
    Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.

    Args:
        workspace (str):
        repo_slug (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        q=q,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[Error]:
    """List branches and tags

     Returns the branches and tags in the repository.

    By default, results will be in the order the underlying source control system returns them and
    identical to
    the ordering one sees when running \"$ git show-ref\". Note that this follows simple
    lexical ordering of the ref names.

    This can be undesirable as it does apply any natural sorting semantics, meaning for instance that
    refs are
    sorted [\"branch1\", \"branch10\", \"branch2\", \"v10\", \"v11\", \"v9\"] instead of [\"branch1\",
    \"branch2\",
    \"branch10\", \"v9\", \"v10\", \"v11\"].

    Sorting can be changed using the ?sort= query parameter. When using ?sort=name to explicitly sort on
    ref name,
    Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.

    Args:
        workspace (str):
        repo_slug (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        q=q,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    q: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[Error]:
    """List branches and tags

     Returns the branches and tags in the repository.

    By default, results will be in the order the underlying source control system returns them and
    identical to
    the ordering one sees when running \"$ git show-ref\". Note that this follows simple
    lexical ordering of the ref names.

    This can be undesirable as it does apply any natural sorting semantics, meaning for instance that
    refs are
    sorted [\"branch1\", \"branch10\", \"branch2\", \"v10\", \"v11\", \"v9\"] instead of [\"branch1\",
    \"branch2\",
    \"branch10\", \"v9\", \"v10\", \"v11\"].

    Sorting can be changed using the ?sort= query parameter. When using ?sort=name to explicitly sort on
    ref name,
    Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.

    Args:
        workspace (str):
        repo_slug (str):
        q (Union[Unset, None, str]):
        sort (Union[Unset, None, str]):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            q=q,
            sort=sort,
        )
    ).parsed
