from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.paginated_ssh_user_keys import PaginatedSSHUserKeys
from ...types import Response


def _get_kwargs(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/users/{selected_user}/ssh-keys".format(client.base_url, selected_user=selected_user)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Error, PaginatedSSHUserKeys]]:
    if response.status_code == 200:
        response_200 = PaginatedSSHUserKeys.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Error, PaginatedSSHUserKeys]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error, PaginatedSSHUserKeys]]:
    """List SSH keys

     Returns a paginated list of the user's SSH public keys.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys
    {
        \"page\": 1,
        \"pagelen\": 10,
        \"size\": 1,
        \"values\": [
            {
                \"comment\": \"user@myhost\",
                \"created_on\": \"2018-03-14T13:17:05.196003+00:00\",
                \"key\": \"ssh-ed25519
    AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY\",
                \"label\": \"\",
                \"last_used\": \"2018-03-20T13:18:05.196003+00:00\",
                \"links\": {
                    \"self\": {
                        \"href\":
    \"https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-
    keys/b15b6026-9c02-4626-b4ad-b905f99f763a\"
                    }
                },
                \"owner\": {
                    \"display_name\": \"Mark Adams\",
                    \"links\": {
                        \"avatar\": {
                            \"href\": \"https://bitbucket.org/account/markadams-atl/avatar/32/\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/markadams-atl/\"
                        },
                        \"self\": {
                            \"href\":
    \"https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}\"
                        }
                    },
                    \"type\": \"user\",
                    \"username\": \"markadams-atl\",
                    \"nickname\": \"markadams-atl\",
                    \"uuid\": \"{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}\"
                },
                \"type\": \"ssh_key\",
                \"uuid\": \"{b15b6026-9c02-4626-b4ad-b905f99f763a}\"
            }
        ]
    }
    ```

    Args:
        selected_user (str):

    Returns:
        Response[Union[Any, Error, PaginatedSSHUserKeys]]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error, PaginatedSSHUserKeys]]:
    """List SSH keys

     Returns a paginated list of the user's SSH public keys.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys
    {
        \"page\": 1,
        \"pagelen\": 10,
        \"size\": 1,
        \"values\": [
            {
                \"comment\": \"user@myhost\",
                \"created_on\": \"2018-03-14T13:17:05.196003+00:00\",
                \"key\": \"ssh-ed25519
    AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY\",
                \"label\": \"\",
                \"last_used\": \"2018-03-20T13:18:05.196003+00:00\",
                \"links\": {
                    \"self\": {
                        \"href\":
    \"https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-
    keys/b15b6026-9c02-4626-b4ad-b905f99f763a\"
                    }
                },
                \"owner\": {
                    \"display_name\": \"Mark Adams\",
                    \"links\": {
                        \"avatar\": {
                            \"href\": \"https://bitbucket.org/account/markadams-atl/avatar/32/\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/markadams-atl/\"
                        },
                        \"self\": {
                            \"href\":
    \"https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}\"
                        }
                    },
                    \"type\": \"user\",
                    \"username\": \"markadams-atl\",
                    \"nickname\": \"markadams-atl\",
                    \"uuid\": \"{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}\"
                },
                \"type\": \"ssh_key\",
                \"uuid\": \"{b15b6026-9c02-4626-b4ad-b905f99f763a}\"
            }
        ]
    }
    ```

    Args:
        selected_user (str):

    Returns:
        Response[Union[Any, Error, PaginatedSSHUserKeys]]
    """

    return sync_detailed(
        selected_user=selected_user,
        client=client,
    ).parsed


async def asyncio_detailed(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Error, PaginatedSSHUserKeys]]:
    """List SSH keys

     Returns a paginated list of the user's SSH public keys.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys
    {
        \"page\": 1,
        \"pagelen\": 10,
        \"size\": 1,
        \"values\": [
            {
                \"comment\": \"user@myhost\",
                \"created_on\": \"2018-03-14T13:17:05.196003+00:00\",
                \"key\": \"ssh-ed25519
    AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY\",
                \"label\": \"\",
                \"last_used\": \"2018-03-20T13:18:05.196003+00:00\",
                \"links\": {
                    \"self\": {
                        \"href\":
    \"https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-
    keys/b15b6026-9c02-4626-b4ad-b905f99f763a\"
                    }
                },
                \"owner\": {
                    \"display_name\": \"Mark Adams\",
                    \"links\": {
                        \"avatar\": {
                            \"href\": \"https://bitbucket.org/account/markadams-atl/avatar/32/\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/markadams-atl/\"
                        },
                        \"self\": {
                            \"href\":
    \"https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}\"
                        }
                    },
                    \"type\": \"user\",
                    \"username\": \"markadams-atl\",
                    \"nickname\": \"markadams-atl\",
                    \"uuid\": \"{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}\"
                },
                \"type\": \"ssh_key\",
                \"uuid\": \"{b15b6026-9c02-4626-b4ad-b905f99f763a}\"
            }
        ]
    }
    ```

    Args:
        selected_user (str):

    Returns:
        Response[Union[Any, Error, PaginatedSSHUserKeys]]
    """

    kwargs = _get_kwargs(
        selected_user=selected_user,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Error, PaginatedSSHUserKeys]]:
    """List SSH keys

     Returns a paginated list of the user's SSH public keys.

    Example:

    ```
    $ curl https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys
    {
        \"page\": 1,
        \"pagelen\": 10,
        \"size\": 1,
        \"values\": [
            {
                \"comment\": \"user@myhost\",
                \"created_on\": \"2018-03-14T13:17:05.196003+00:00\",
                \"key\": \"ssh-ed25519
    AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY\",
                \"label\": \"\",
                \"last_used\": \"2018-03-20T13:18:05.196003+00:00\",
                \"links\": {
                    \"self\": {
                        \"href\":
    \"https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-
    keys/b15b6026-9c02-4626-b4ad-b905f99f763a\"
                    }
                },
                \"owner\": {
                    \"display_name\": \"Mark Adams\",
                    \"links\": {
                        \"avatar\": {
                            \"href\": \"https://bitbucket.org/account/markadams-atl/avatar/32/\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/markadams-atl/\"
                        },
                        \"self\": {
                            \"href\":
    \"https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}\"
                        }
                    },
                    \"type\": \"user\",
                    \"username\": \"markadams-atl\",
                    \"nickname\": \"markadams-atl\",
                    \"uuid\": \"{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}\"
                },
                \"type\": \"ssh_key\",
                \"uuid\": \"{b15b6026-9c02-4626-b4ad-b905f99f763a}\"
            }
        ]
    }
    ```

    Args:
        selected_user (str):

    Returns:
        Response[Union[Any, Error, PaginatedSSHUserKeys]]
    """

    return (
        await asyncio_detailed(
            selected_user=selected_user,
            client=client,
        )
    ).parsed
