from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error import Error
from ...models.snippet import Snippet
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/snippets".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, Snippet]]:
    if response.status_code == 201:
        response_201 = Snippet.from_dict(response.json())

        return response_201
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, Snippet]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, Snippet]]:
    """Create a snippet

     Creates a new snippet under the authenticated user's account.

    Snippets can contain multiple files. Both text and binary files are
    supported.

    The simplest way to create a new snippet from a local file:

        $ curl -u username:password -X POST https://api.bitbucket.org/2.0/snippets               -F
    file=@image.png

    Creating snippets through curl has a few limitations and so let's look
    at a more complicated scenario.

    Snippets are created with a multipart POST. Both `multipart/form-data`
    and `multipart/related` are supported. Both allow the creation of
    snippets with both meta data (title, etc), as well as multiple text
    and binary files.

    The main difference is that `multipart/related` can use rich encoding
    for the meta data (currently JSON).


    multipart/related (RFC-2387)
    ----------------------------

    This is the most advanced and efficient way to create a paste.

        POST /2.0/snippets/evzijst HTTP/1.1
        Content-Length: 1188
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"title\": \"My snippet\",
          \"is_private\": true,
          \"scm\": \"git\",
          \"files\": {
              \"foo.txt\": {},
              \"image.png\": {}
            }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"foo.txt\"
        Content-Disposition: attachment; filename=\"foo.txt\"

        foo

        --===============1438169132528273974==
        Content-Type: image/png
        MIME-Version: 1.0
        Content-Transfer-Encoding: base64
        Content-ID: \"image.png\"
        Content-Disposition: attachment; filename=\"image.png\"

        iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
        TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
        cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
        EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
        73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
        AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
        --===============1438169132528273974==--

    The request contains multiple parts and is structured as follows.

    The first part is the JSON document that describes the snippet's
    properties or meta data. It either has to be the first part, or the
    request's `Content-Type` header must contain the `start` parameter to
    point to it.

    The remaining parts are the files of which there can be zero or more.
    Each file part should contain the `Content-ID` MIME header through
    which the JSON meta data's `files` element addresses it. The value
    should be the name of the file.

    `Content-Disposition` is an optional MIME header. The header's
    optional `filename` parameter can be used to specify the file name
    that Bitbucket should use when writing the file to disk. When present,
    `filename` takes precedence over the value of `Content-ID`.

    When the JSON body omits the `files` element, the remaining parts are
    not ignored. Instead, each file is added to the new snippet as if its
    name was explicitly linked (the use of the `files` elements is
    mandatory for some operations like deleting or renaming files).


    multipart/form-data
    -------------------

    The use of JSON for the snippet's meta data is optional. Meta data can
    also be supplied as regular form fields in a more conventional
    `multipart/form-data` request:

        $ curl -X POST -u credentials https://api.bitbucket.org/2.0/snippets               -F title=\"My
    snippet\"               -F file=@foo.txt -F file=@image.png

        POST /2.0/snippets HTTP/1.1
        Content-Length: 951
        Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"file\"; filename=\"foo.txt\"
        Content-Type: text/plain

        foo

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"file\"; filename=\"image.png\"
        Content-Type: application/octet-stream

        ?PNG

        IHDR?1??I.....
        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"title\"

        My snippet
        ------------------------------63a4b224c59f--

    Here the meta data properties are included as flat, top-level form
    fields. The file attachments use the `file` field name. To attach
    multiple files, simply repeat the field.

    The advantage of `multipart/form-data` over `multipart/related` is
    that it can be easier to build clients.

    Essentially all properties are optional, `title` and `files` included.


    Sharing and Visibility
    ----------------------

    Snippets can be either public (visible to anyone on Bitbucket, as well
    as anonymous users), or private (visible only to members of the workspace).
    This is controlled through the snippet's `is_private` element:

    * **is_private=false** -- everyone, including anonymous users can view
      the snippet
    * **is_private=true** -- only workspace members can view the snippet

    To create the snippet under a workspace, just append the workspace ID
    to the URL. See [`/2.0/snippets/{workspace}`](/cloud/bitbucket/rest/api-group-snippets/#api-
    snippets-workspace-post).

    Returns:
        Response[Union[Error, Snippet]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, Snippet]]:
    """Create a snippet

     Creates a new snippet under the authenticated user's account.

    Snippets can contain multiple files. Both text and binary files are
    supported.

    The simplest way to create a new snippet from a local file:

        $ curl -u username:password -X POST https://api.bitbucket.org/2.0/snippets               -F
    file=@image.png

    Creating snippets through curl has a few limitations and so let's look
    at a more complicated scenario.

    Snippets are created with a multipart POST. Both `multipart/form-data`
    and `multipart/related` are supported. Both allow the creation of
    snippets with both meta data (title, etc), as well as multiple text
    and binary files.

    The main difference is that `multipart/related` can use rich encoding
    for the meta data (currently JSON).


    multipart/related (RFC-2387)
    ----------------------------

    This is the most advanced and efficient way to create a paste.

        POST /2.0/snippets/evzijst HTTP/1.1
        Content-Length: 1188
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"title\": \"My snippet\",
          \"is_private\": true,
          \"scm\": \"git\",
          \"files\": {
              \"foo.txt\": {},
              \"image.png\": {}
            }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"foo.txt\"
        Content-Disposition: attachment; filename=\"foo.txt\"

        foo

        --===============1438169132528273974==
        Content-Type: image/png
        MIME-Version: 1.0
        Content-Transfer-Encoding: base64
        Content-ID: \"image.png\"
        Content-Disposition: attachment; filename=\"image.png\"

        iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
        TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
        cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
        EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
        73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
        AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
        --===============1438169132528273974==--

    The request contains multiple parts and is structured as follows.

    The first part is the JSON document that describes the snippet's
    properties or meta data. It either has to be the first part, or the
    request's `Content-Type` header must contain the `start` parameter to
    point to it.

    The remaining parts are the files of which there can be zero or more.
    Each file part should contain the `Content-ID` MIME header through
    which the JSON meta data's `files` element addresses it. The value
    should be the name of the file.

    `Content-Disposition` is an optional MIME header. The header's
    optional `filename` parameter can be used to specify the file name
    that Bitbucket should use when writing the file to disk. When present,
    `filename` takes precedence over the value of `Content-ID`.

    When the JSON body omits the `files` element, the remaining parts are
    not ignored. Instead, each file is added to the new snippet as if its
    name was explicitly linked (the use of the `files` elements is
    mandatory for some operations like deleting or renaming files).


    multipart/form-data
    -------------------

    The use of JSON for the snippet's meta data is optional. Meta data can
    also be supplied as regular form fields in a more conventional
    `multipart/form-data` request:

        $ curl -X POST -u credentials https://api.bitbucket.org/2.0/snippets               -F title=\"My
    snippet\"               -F file=@foo.txt -F file=@image.png

        POST /2.0/snippets HTTP/1.1
        Content-Length: 951
        Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"file\"; filename=\"foo.txt\"
        Content-Type: text/plain

        foo

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"file\"; filename=\"image.png\"
        Content-Type: application/octet-stream

        ?PNG

        IHDR?1??I.....
        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"title\"

        My snippet
        ------------------------------63a4b224c59f--

    Here the meta data properties are included as flat, top-level form
    fields. The file attachments use the `file` field name. To attach
    multiple files, simply repeat the field.

    The advantage of `multipart/form-data` over `multipart/related` is
    that it can be easier to build clients.

    Essentially all properties are optional, `title` and `files` included.


    Sharing and Visibility
    ----------------------

    Snippets can be either public (visible to anyone on Bitbucket, as well
    as anonymous users), or private (visible only to members of the workspace).
    This is controlled through the snippet's `is_private` element:

    * **is_private=false** -- everyone, including anonymous users can view
      the snippet
    * **is_private=true** -- only workspace members can view the snippet

    To create the snippet under a workspace, just append the workspace ID
    to the URL. See [`/2.0/snippets/{workspace}`](/cloud/bitbucket/rest/api-group-snippets/#api-
    snippets-workspace-post).

    Returns:
        Response[Union[Error, Snippet]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, Snippet]]:
    """Create a snippet

     Creates a new snippet under the authenticated user's account.

    Snippets can contain multiple files. Both text and binary files are
    supported.

    The simplest way to create a new snippet from a local file:

        $ curl -u username:password -X POST https://api.bitbucket.org/2.0/snippets               -F
    file=@image.png

    Creating snippets through curl has a few limitations and so let's look
    at a more complicated scenario.

    Snippets are created with a multipart POST. Both `multipart/form-data`
    and `multipart/related` are supported. Both allow the creation of
    snippets with both meta data (title, etc), as well as multiple text
    and binary files.

    The main difference is that `multipart/related` can use rich encoding
    for the meta data (currently JSON).


    multipart/related (RFC-2387)
    ----------------------------

    This is the most advanced and efficient way to create a paste.

        POST /2.0/snippets/evzijst HTTP/1.1
        Content-Length: 1188
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"title\": \"My snippet\",
          \"is_private\": true,
          \"scm\": \"git\",
          \"files\": {
              \"foo.txt\": {},
              \"image.png\": {}
            }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"foo.txt\"
        Content-Disposition: attachment; filename=\"foo.txt\"

        foo

        --===============1438169132528273974==
        Content-Type: image/png
        MIME-Version: 1.0
        Content-Transfer-Encoding: base64
        Content-ID: \"image.png\"
        Content-Disposition: attachment; filename=\"image.png\"

        iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
        TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
        cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
        EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
        73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
        AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
        --===============1438169132528273974==--

    The request contains multiple parts and is structured as follows.

    The first part is the JSON document that describes the snippet's
    properties or meta data. It either has to be the first part, or the
    request's `Content-Type` header must contain the `start` parameter to
    point to it.

    The remaining parts are the files of which there can be zero or more.
    Each file part should contain the `Content-ID` MIME header through
    which the JSON meta data's `files` element addresses it. The value
    should be the name of the file.

    `Content-Disposition` is an optional MIME header. The header's
    optional `filename` parameter can be used to specify the file name
    that Bitbucket should use when writing the file to disk. When present,
    `filename` takes precedence over the value of `Content-ID`.

    When the JSON body omits the `files` element, the remaining parts are
    not ignored. Instead, each file is added to the new snippet as if its
    name was explicitly linked (the use of the `files` elements is
    mandatory for some operations like deleting or renaming files).


    multipart/form-data
    -------------------

    The use of JSON for the snippet's meta data is optional. Meta data can
    also be supplied as regular form fields in a more conventional
    `multipart/form-data` request:

        $ curl -X POST -u credentials https://api.bitbucket.org/2.0/snippets               -F title=\"My
    snippet\"               -F file=@foo.txt -F file=@image.png

        POST /2.0/snippets HTTP/1.1
        Content-Length: 951
        Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"file\"; filename=\"foo.txt\"
        Content-Type: text/plain

        foo

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"file\"; filename=\"image.png\"
        Content-Type: application/octet-stream

        ?PNG

        IHDR?1??I.....
        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"title\"

        My snippet
        ------------------------------63a4b224c59f--

    Here the meta data properties are included as flat, top-level form
    fields. The file attachments use the `file` field name. To attach
    multiple files, simply repeat the field.

    The advantage of `multipart/form-data` over `multipart/related` is
    that it can be easier to build clients.

    Essentially all properties are optional, `title` and `files` included.


    Sharing and Visibility
    ----------------------

    Snippets can be either public (visible to anyone on Bitbucket, as well
    as anonymous users), or private (visible only to members of the workspace).
    This is controlled through the snippet's `is_private` element:

    * **is_private=false** -- everyone, including anonymous users can view
      the snippet
    * **is_private=true** -- only workspace members can view the snippet

    To create the snippet under a workspace, just append the workspace ID
    to the URL. See [`/2.0/snippets/{workspace}`](/cloud/bitbucket/rest/api-group-snippets/#api-
    snippets-workspace-post).

    Returns:
        Response[Union[Error, Snippet]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, Snippet]]:
    """Create a snippet

     Creates a new snippet under the authenticated user's account.

    Snippets can contain multiple files. Both text and binary files are
    supported.

    The simplest way to create a new snippet from a local file:

        $ curl -u username:password -X POST https://api.bitbucket.org/2.0/snippets               -F
    file=@image.png

    Creating snippets through curl has a few limitations and so let's look
    at a more complicated scenario.

    Snippets are created with a multipart POST. Both `multipart/form-data`
    and `multipart/related` are supported. Both allow the creation of
    snippets with both meta data (title, etc), as well as multiple text
    and binary files.

    The main difference is that `multipart/related` can use rich encoding
    for the meta data (currently JSON).


    multipart/related (RFC-2387)
    ----------------------------

    This is the most advanced and efficient way to create a paste.

        POST /2.0/snippets/evzijst HTTP/1.1
        Content-Length: 1188
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"title\": \"My snippet\",
          \"is_private\": true,
          \"scm\": \"git\",
          \"files\": {
              \"foo.txt\": {},
              \"image.png\": {}
            }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"foo.txt\"
        Content-Disposition: attachment; filename=\"foo.txt\"

        foo

        --===============1438169132528273974==
        Content-Type: image/png
        MIME-Version: 1.0
        Content-Transfer-Encoding: base64
        Content-ID: \"image.png\"
        Content-Disposition: attachment; filename=\"image.png\"

        iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
        TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
        cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
        EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
        73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
        AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
        --===============1438169132528273974==--

    The request contains multiple parts and is structured as follows.

    The first part is the JSON document that describes the snippet's
    properties or meta data. It either has to be the first part, or the
    request's `Content-Type` header must contain the `start` parameter to
    point to it.

    The remaining parts are the files of which there can be zero or more.
    Each file part should contain the `Content-ID` MIME header through
    which the JSON meta data's `files` element addresses it. The value
    should be the name of the file.

    `Content-Disposition` is an optional MIME header. The header's
    optional `filename` parameter can be used to specify the file name
    that Bitbucket should use when writing the file to disk. When present,
    `filename` takes precedence over the value of `Content-ID`.

    When the JSON body omits the `files` element, the remaining parts are
    not ignored. Instead, each file is added to the new snippet as if its
    name was explicitly linked (the use of the `files` elements is
    mandatory for some operations like deleting or renaming files).


    multipart/form-data
    -------------------

    The use of JSON for the snippet's meta data is optional. Meta data can
    also be supplied as regular form fields in a more conventional
    `multipart/form-data` request:

        $ curl -X POST -u credentials https://api.bitbucket.org/2.0/snippets               -F title=\"My
    snippet\"               -F file=@foo.txt -F file=@image.png

        POST /2.0/snippets HTTP/1.1
        Content-Length: 951
        Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"file\"; filename=\"foo.txt\"
        Content-Type: text/plain

        foo

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"file\"; filename=\"image.png\"
        Content-Type: application/octet-stream

        ?PNG

        IHDR?1??I.....
        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"title\"

        My snippet
        ------------------------------63a4b224c59f--

    Here the meta data properties are included as flat, top-level form
    fields. The file attachments use the `file` field name. To attach
    multiple files, simply repeat the field.

    The advantage of `multipart/form-data` over `multipart/related` is
    that it can be easier to build clients.

    Essentially all properties are optional, `title` and `files` included.


    Sharing and Visibility
    ----------------------

    Snippets can be either public (visible to anyone on Bitbucket, as well
    as anonymous users), or private (visible only to members of the workspace).
    This is controlled through the snippet's `is_private` element:

    * **is_private=false** -- everyone, including anonymous users can view
      the snippet
    * **is_private=true** -- only workspace members can view the snippet

    To create the snippet under a workspace, just append the workspace ID
    to the URL. See [`/2.0/snippets/{workspace}`](/cloud/bitbucket/rest/api-group-snippets/#api-
    snippets-workspace-post).

    Returns:
        Response[Union[Error, Snippet]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
