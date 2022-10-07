from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    project_key: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id}".format(
        client.base_url, workspace=workspace, project_key=project_key, key_id=key_id
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
    project_key: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Get a project deploy key

     Returns the deploy key belonging to a specific key ID.

    Example:
    ```
    $ curl -H \"Authorization <auth header>\" \
    https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys/1234

    Output:
    {
        \"pagelen\":10,
        \"values\":[
            {
                \"comment\":\"thakseth@C02W454JHTD8\",
                \"last_used\":null,
                \"links\":{
                    \"self\":{
    \"href\":\"https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-
    keys/1234\"
                    }
                },
                \"label\":\"test\",
                \"project\":{
                    \"links\":{
                        \"self\":{
    \"href\":\"https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT\"
                        }
                    },
                    \"type\":\"project\",
                    \"name\":\"cooperative standard\",
                    \"key\":\"TEST_PROJECT\",
                    \"uuid\":\"{3b3e510b-7f2b-414d-a2b7-76c4e405c1c0}\"
                },
                \"created_on\":\"2021-07-28T21:20:19.491721+00:00\",
                \"key\":\"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDX5yfMOEw6HG9jKTYTisbmDTJ4MCUTSVGr5e4OWv
    Y3UuI2A6F8SdzQqa2f5BABA/4g5Sk5awJrYHlNu3EzV1V2I44tR3A4fnZAG71ZKyDPi1wvdO7UYmFgxV/Vd18H9QZFFjICGDM7W0
    PT2mI0kON/jN3qNWi+GiB/xgaeQKSqynysdysDp8lnnI/8Sh3ikURP9UP83ShRCpAXszOUNaa+UUlcYQYBDLIGowsg51c4PCkC3D
    NhAMxppkNRKoSOWwyl+oRVXHSDylkiJSBHW3HH4Q6WHieD54kGrjbhWBKdnnxKX7QAAZBDseY+t01N36m6/ljvXSUEcBWtHxBYye
    0r\",
                \"type\":\"project_deploy_key\",
                \"id\":1234
            }
        ],
    }
    ```

    Args:
        workspace (str):
        project_key (str):
        key_id (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        key_id=key_id,
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
    key_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Get a project deploy key

     Returns the deploy key belonging to a specific key ID.

    Example:
    ```
    $ curl -H \"Authorization <auth header>\" \
    https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys/1234

    Output:
    {
        \"pagelen\":10,
        \"values\":[
            {
                \"comment\":\"thakseth@C02W454JHTD8\",
                \"last_used\":null,
                \"links\":{
                    \"self\":{
    \"href\":\"https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-
    keys/1234\"
                    }
                },
                \"label\":\"test\",
                \"project\":{
                    \"links\":{
                        \"self\":{
    \"href\":\"https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT\"
                        }
                    },
                    \"type\":\"project\",
                    \"name\":\"cooperative standard\",
                    \"key\":\"TEST_PROJECT\",
                    \"uuid\":\"{3b3e510b-7f2b-414d-a2b7-76c4e405c1c0}\"
                },
                \"created_on\":\"2021-07-28T21:20:19.491721+00:00\",
                \"key\":\"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDX5yfMOEw6HG9jKTYTisbmDTJ4MCUTSVGr5e4OWv
    Y3UuI2A6F8SdzQqa2f5BABA/4g5Sk5awJrYHlNu3EzV1V2I44tR3A4fnZAG71ZKyDPi1wvdO7UYmFgxV/Vd18H9QZFFjICGDM7W0
    PT2mI0kON/jN3qNWi+GiB/xgaeQKSqynysdysDp8lnnI/8Sh3ikURP9UP83ShRCpAXszOUNaa+UUlcYQYBDLIGowsg51c4PCkC3D
    NhAMxppkNRKoSOWwyl+oRVXHSDylkiJSBHW3HH4Q6WHieD54kGrjbhWBKdnnxKX7QAAZBDseY+t01N36m6/ljvXSUEcBWtHxBYye
    0r\",
                \"type\":\"project_deploy_key\",
                \"id\":1234
            }
        ],
    }
    ```

    Args:
        workspace (str):
        project_key (str):
        key_id (str):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        project_key=project_key,
        key_id=key_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    project_key: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Get a project deploy key

     Returns the deploy key belonging to a specific key ID.

    Example:
    ```
    $ curl -H \"Authorization <auth header>\" \
    https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys/1234

    Output:
    {
        \"pagelen\":10,
        \"values\":[
            {
                \"comment\":\"thakseth@C02W454JHTD8\",
                \"last_used\":null,
                \"links\":{
                    \"self\":{
    \"href\":\"https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-
    keys/1234\"
                    }
                },
                \"label\":\"test\",
                \"project\":{
                    \"links\":{
                        \"self\":{
    \"href\":\"https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT\"
                        }
                    },
                    \"type\":\"project\",
                    \"name\":\"cooperative standard\",
                    \"key\":\"TEST_PROJECT\",
                    \"uuid\":\"{3b3e510b-7f2b-414d-a2b7-76c4e405c1c0}\"
                },
                \"created_on\":\"2021-07-28T21:20:19.491721+00:00\",
                \"key\":\"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDX5yfMOEw6HG9jKTYTisbmDTJ4MCUTSVGr5e4OWv
    Y3UuI2A6F8SdzQqa2f5BABA/4g5Sk5awJrYHlNu3EzV1V2I44tR3A4fnZAG71ZKyDPi1wvdO7UYmFgxV/Vd18H9QZFFjICGDM7W0
    PT2mI0kON/jN3qNWi+GiB/xgaeQKSqynysdysDp8lnnI/8Sh3ikURP9UP83ShRCpAXszOUNaa+UUlcYQYBDLIGowsg51c4PCkC3D
    NhAMxppkNRKoSOWwyl+oRVXHSDylkiJSBHW3HH4Q6WHieD54kGrjbhWBKdnnxKX7QAAZBDseY+t01N36m6/ljvXSUEcBWtHxBYye
    0r\",
                \"type\":\"project_deploy_key\",
                \"id\":1234
            }
        ],
    }
    ```

    Args:
        workspace (str):
        project_key (str):
        key_id (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        key_id=key_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    project_key: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Get a project deploy key

     Returns the deploy key belonging to a specific key ID.

    Example:
    ```
    $ curl -H \"Authorization <auth header>\" \
    https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys/1234

    Output:
    {
        \"pagelen\":10,
        \"values\":[
            {
                \"comment\":\"thakseth@C02W454JHTD8\",
                \"last_used\":null,
                \"links\":{
                    \"self\":{
    \"href\":\"https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-
    keys/1234\"
                    }
                },
                \"label\":\"test\",
                \"project\":{
                    \"links\":{
                        \"self\":{
    \"href\":\"https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT\"
                        }
                    },
                    \"type\":\"project\",
                    \"name\":\"cooperative standard\",
                    \"key\":\"TEST_PROJECT\",
                    \"uuid\":\"{3b3e510b-7f2b-414d-a2b7-76c4e405c1c0}\"
                },
                \"created_on\":\"2021-07-28T21:20:19.491721+00:00\",
                \"key\":\"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDX5yfMOEw6HG9jKTYTisbmDTJ4MCUTSVGr5e4OWv
    Y3UuI2A6F8SdzQqa2f5BABA/4g5Sk5awJrYHlNu3EzV1V2I44tR3A4fnZAG71ZKyDPi1wvdO7UYmFgxV/Vd18H9QZFFjICGDM7W0
    PT2mI0kON/jN3qNWi+GiB/xgaeQKSqynysdysDp8lnnI/8Sh3ikURP9UP83ShRCpAXszOUNaa+UUlcYQYBDLIGowsg51c4PCkC3D
    NhAMxppkNRKoSOWwyl+oRVXHSDylkiJSBHW3HH4Q6WHieD54kGrjbhWBKdnnxKX7QAAZBDseY+t01N36m6/ljvXSUEcBWtHxBYye
    0r\",
                \"type\":\"project_deploy_key\",
                \"id\":1234
            }
        ],
    }
    ```

    Args:
        workspace (str):
        project_key (str):
        key_id (str):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            project_key=project_key,
            key_id=key_id,
            client=client,
        )
    ).parsed
