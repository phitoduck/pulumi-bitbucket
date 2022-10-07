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
    url = "{}/repositories/{workspace}/{repo_slug}/deploy-keys".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error]]:
    if response.status_code == 403:
        response_403 = cast(Any, None)
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
) -> Response[Union[Any, Error]]:
    """List repository deploy keys

     Returns all deploy-keys belonging to a repository.

    Example:
    ```
    $ curl -H \"Authorization <auth header>\" \
    https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys

    Output:
    {
        \"pagelen\": 10,
        \"values\": [
            {
                \"id\": 123,
                \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpE
    sYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGn
    fA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuI
    d93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhB
    dq5\",
                \"label\": \"mykey\",
                \"type\": \"deploy_key\",
                \"created_on\": \"2018-08-15T23:50:59.993890+00:00\",
                \"repository\": {
                    \"full_name\": \"mleu/test\",
                    \"name\": \"test\",
                    \"type\": \"repository\",
                    \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
                },
                \"links\":{
                    \"self\":{
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-
    keys/123\"
                    }
                }
                \"last_used\": null,
                \"comment\": \"mleu@C02W454JHTD8\"
            }
        ],
        \"page\": 1,
        \"size\": 1
    }
    ```

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
    """List repository deploy keys

     Returns all deploy-keys belonging to a repository.

    Example:
    ```
    $ curl -H \"Authorization <auth header>\" \
    https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys

    Output:
    {
        \"pagelen\": 10,
        \"values\": [
            {
                \"id\": 123,
                \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpE
    sYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGn
    fA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuI
    d93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhB
    dq5\",
                \"label\": \"mykey\",
                \"type\": \"deploy_key\",
                \"created_on\": \"2018-08-15T23:50:59.993890+00:00\",
                \"repository\": {
                    \"full_name\": \"mleu/test\",
                    \"name\": \"test\",
                    \"type\": \"repository\",
                    \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
                },
                \"links\":{
                    \"self\":{
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-
    keys/123\"
                    }
                }
                \"last_used\": null,
                \"comment\": \"mleu@C02W454JHTD8\"
            }
        ],
        \"page\": 1,
        \"size\": 1
    }
    ```

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
    """List repository deploy keys

     Returns all deploy-keys belonging to a repository.

    Example:
    ```
    $ curl -H \"Authorization <auth header>\" \
    https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys

    Output:
    {
        \"pagelen\": 10,
        \"values\": [
            {
                \"id\": 123,
                \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpE
    sYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGn
    fA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuI
    d93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhB
    dq5\",
                \"label\": \"mykey\",
                \"type\": \"deploy_key\",
                \"created_on\": \"2018-08-15T23:50:59.993890+00:00\",
                \"repository\": {
                    \"full_name\": \"mleu/test\",
                    \"name\": \"test\",
                    \"type\": \"repository\",
                    \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
                },
                \"links\":{
                    \"self\":{
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-
    keys/123\"
                    }
                }
                \"last_used\": null,
                \"comment\": \"mleu@C02W454JHTD8\"
            }
        ],
        \"page\": 1,
        \"size\": 1
    }
    ```

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
    """List repository deploy keys

     Returns all deploy-keys belonging to a repository.

    Example:
    ```
    $ curl -H \"Authorization <auth header>\" \
    https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys

    Output:
    {
        \"pagelen\": 10,
        \"values\": [
            {
                \"id\": 123,
                \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpE
    sYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGn
    fA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuI
    d93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhB
    dq5\",
                \"label\": \"mykey\",
                \"type\": \"deploy_key\",
                \"created_on\": \"2018-08-15T23:50:59.993890+00:00\",
                \"repository\": {
                    \"full_name\": \"mleu/test\",
                    \"name\": \"test\",
                    \"type\": \"repository\",
                    \"uuid\": \"{85d08b4e-571d-44e9-a507-fa476535aa98}\"
                },
                \"links\":{
                    \"self\":{
                        \"href\": \"https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-
    keys/123\"
                    }
                }
                \"last_used\": null,
                \"comment\": \"mleu@C02W454JHTD8\"
            }
        ],
        \"page\": 1,
        \"size\": 1
    }
    ```

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
