from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/projects/{project_key}/deploy-keys".format(
        client.base_url, workspace=workspace, project_key=project_key
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


def _parse_response(*, response: httpx.Response) -> Optional[Error]:
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
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
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Create a project deploy key

     Create a new deploy key in a project.

    Example:
    ```
    $ curl -XPOST \
    -H \"Authorization <auth header>\" \
    -H \"Content-type: application/json\" \
    https://api.bitbucket.org/!api/2.0/workspaces/jzeng/projects/JZ/deploy-keys/ -d \
    '{
        \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1
    fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU
    +qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZr
    CNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5
    mleu@C02W454JHTD8\",
        \"label\": \"mydeploykey\"
    }'

    Output:
    {
        \"comment\": \"mleu@C02W454JHTD8\",
        \"last_used\": null,
        \"links\": {
            \"self\": {
                \"href\":
    \"https://jzeng.devbucket.org/!api/2.0/workspaces/testadfsa/projects/ASDF/deploy-keys/5/\"
            }
        },
        \"label\": \"myprojectkey\",
        \"project\": {
            ...
        },
        \"created_on\": \"2021-08-10T05:28:00.570859+00:00\",
        \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1
    fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU
    +qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZr
    CNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\",
        \"type\": \"project_deploy_key\",
        \"id\": 5
    }
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Create a project deploy key

     Create a new deploy key in a project.

    Example:
    ```
    $ curl -XPOST \
    -H \"Authorization <auth header>\" \
    -H \"Content-type: application/json\" \
    https://api.bitbucket.org/!api/2.0/workspaces/jzeng/projects/JZ/deploy-keys/ -d \
    '{
        \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1
    fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU
    +qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZr
    CNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5
    mleu@C02W454JHTD8\",
        \"label\": \"mydeploykey\"
    }'

    Output:
    {
        \"comment\": \"mleu@C02W454JHTD8\",
        \"last_used\": null,
        \"links\": {
            \"self\": {
                \"href\":
    \"https://jzeng.devbucket.org/!api/2.0/workspaces/testadfsa/projects/ASDF/deploy-keys/5/\"
            }
        },
        \"label\": \"myprojectkey\",
        \"project\": {
            ...
        },
        \"created_on\": \"2021-08-10T05:28:00.570859+00:00\",
        \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1
    fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU
    +qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZr
    CNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\",
        \"type\": \"project_deploy_key\",
        \"id\": 5
    }
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        project_key=project_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Create a project deploy key

     Create a new deploy key in a project.

    Example:
    ```
    $ curl -XPOST \
    -H \"Authorization <auth header>\" \
    -H \"Content-type: application/json\" \
    https://api.bitbucket.org/!api/2.0/workspaces/jzeng/projects/JZ/deploy-keys/ -d \
    '{
        \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1
    fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU
    +qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZr
    CNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5
    mleu@C02W454JHTD8\",
        \"label\": \"mydeploykey\"
    }'

    Output:
    {
        \"comment\": \"mleu@C02W454JHTD8\",
        \"last_used\": null,
        \"links\": {
            \"self\": {
                \"href\":
    \"https://jzeng.devbucket.org/!api/2.0/workspaces/testadfsa/projects/ASDF/deploy-keys/5/\"
            }
        },
        \"label\": \"myprojectkey\",
        \"project\": {
            ...
        },
        \"created_on\": \"2021-08-10T05:28:00.570859+00:00\",
        \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1
    fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU
    +qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZr
    CNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\",
        \"type\": \"project_deploy_key\",
        \"id\": 5
    }
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Create a project deploy key

     Create a new deploy key in a project.

    Example:
    ```
    $ curl -XPOST \
    -H \"Authorization <auth header>\" \
    -H \"Content-type: application/json\" \
    https://api.bitbucket.org/!api/2.0/workspaces/jzeng/projects/JZ/deploy-keys/ -d \
    '{
        \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1
    fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU
    +qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZr
    CNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5
    mleu@C02W454JHTD8\",
        \"label\": \"mydeploykey\"
    }'

    Output:
    {
        \"comment\": \"mleu@C02W454JHTD8\",
        \"last_used\": null,
        \"links\": {
            \"self\": {
                \"href\":
    \"https://jzeng.devbucket.org/!api/2.0/workspaces/testadfsa/projects/ASDF/deploy-keys/5/\"
            }
        },
        \"label\": \"myprojectkey\",
        \"project\": {
            ...
        },
        \"created_on\": \"2021-08-10T05:28:00.570859+00:00\",
        \"key\": \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1
    fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU
    +qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZr
    CNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5\",
        \"type\": \"project_deploy_key\",
        \"id\": 5
    }
    ```

    Args:
        workspace (str):
        project_key (str):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            project_key=project_key,
            client=client,
        )
    ).parsed
