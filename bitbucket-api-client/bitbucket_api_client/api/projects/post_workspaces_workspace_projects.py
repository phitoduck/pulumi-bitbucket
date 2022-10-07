from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/projects".format(client.base_url, workspace=workspace)

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
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Create a project in a workspace

     Creates a new project.

    Note that the avatar has to be embedded as either a data-url
    or a URL to an external image as shown in the examples below:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\":
    \"data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/...\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/teams/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    or even:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\": \"http://i.imgur.com/72tRx4w.gif\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/teams/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    Args:
        workspace (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Create a project in a workspace

     Creates a new project.

    Note that the avatar has to be embedded as either a data-url
    or a URL to an external image as shown in the examples below:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\":
    \"data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/...\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/teams/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    or even:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\": \"http://i.imgur.com/72tRx4w.gif\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/teams/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    Args:
        workspace (str):

    Returns:
        Response[Error]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Create a project in a workspace

     Creates a new project.

    Note that the avatar has to be embedded as either a data-url
    or a URL to an external image as shown in the examples below:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\":
    \"data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/...\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/teams/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    or even:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\": \"http://i.imgur.com/72tRx4w.gif\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/teams/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    Args:
        workspace (str):

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Error]:
    """Create a project in a workspace

     Creates a new project.

    Note that the avatar has to be embedded as either a data-url
    or a URL to an external image as shown in the examples below:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\":
    \"data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/...\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/teams/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    or even:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\": \"http://i.imgur.com/72tRx4w.gif\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/teams/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    Args:
        workspace (str):

    Returns:
        Response[Error]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
        )
    ).parsed
