from typing import Any, Dict, List, Optional

import httpx

from ...client import Client
from ...models.report_annotation import ReportAnnotation
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    client: Client,
    json_body: List[ReportAnnotation],
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, commit=commit, reportId=report_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ReportAnnotation]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ReportAnnotation.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ReportAnnotation]]:
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
    report_id: str,
    *,
    client: Client,
    json_body: List[ReportAnnotation],
) -> Response[List[ReportAnnotation]]:
    """Bulk create or update annotations

     Bulk upload of annotations.
    Annotations are individual findings that have been identified as part of a report, for example, a
    line of code that represents a vulnerability. These annotations can be attached to a specific file
    and even a specific line in that file, however, that is optional. Annotations are not mandatory and
    a report can contain up to 1000 annotations.

    Add the annotations you want to upload as objects in a JSON array and make sure each annotation has
    the external_id field set to a unique value. If you want to use an existing id from your own system,
    we recommend prefixing it with your system's name to avoid collisions, for example, mySystem-
    annotation001. The external id can later be used to identify the report as an alternative to the
    generated [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). You
    can upload up to 100 annotations per POST request.

    ### Sample cURL request:
    ```
    curl --location 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001/annotations' \
    --header 'Content-Type: application/json' \
    --data-raw '[
      {
            \"external_id\": \"mysystem-annotation001\",
            \"title\": \"Security scan report\",
            \"annotation_type\": \"VULNERABILITY\",
            \"summary\": \"This line represents a security threat.\",
            \"severity\": \"HIGH\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\",
            \"line\": 42
      },
      {
            \"external_id\": \"mySystem-annotation002\",
            \"title\": \"Bug report\",
            \"annotation_type\": \"BUG\",
            \"result\": \"FAILED\",
            \"summary\": \"This line might introduce a bug.\",
            \"severity\": \"MEDIUM\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Helper.java\",
            \"line\": 13
      }
    ]'
    ```

    ### Possible field values:
    annotation_type: VULNERABILITY, CODE_SMELL, BUG
    result: PASSED, FAILED, IGNORED, SKIPPED
    severity: HIGH, MEDIUM, LOW, CRITICAL

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        json_body (List[ReportAnnotation]):

    Returns:
        Response[List[ReportAnnotation]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        client=client,
        json_body=json_body,
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
    report_id: str,
    *,
    client: Client,
    json_body: List[ReportAnnotation],
) -> Optional[List[ReportAnnotation]]:
    """Bulk create or update annotations

     Bulk upload of annotations.
    Annotations are individual findings that have been identified as part of a report, for example, a
    line of code that represents a vulnerability. These annotations can be attached to a specific file
    and even a specific line in that file, however, that is optional. Annotations are not mandatory and
    a report can contain up to 1000 annotations.

    Add the annotations you want to upload as objects in a JSON array and make sure each annotation has
    the external_id field set to a unique value. If you want to use an existing id from your own system,
    we recommend prefixing it with your system's name to avoid collisions, for example, mySystem-
    annotation001. The external id can later be used to identify the report as an alternative to the
    generated [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). You
    can upload up to 100 annotations per POST request.

    ### Sample cURL request:
    ```
    curl --location 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001/annotations' \
    --header 'Content-Type: application/json' \
    --data-raw '[
      {
            \"external_id\": \"mysystem-annotation001\",
            \"title\": \"Security scan report\",
            \"annotation_type\": \"VULNERABILITY\",
            \"summary\": \"This line represents a security threat.\",
            \"severity\": \"HIGH\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\",
            \"line\": 42
      },
      {
            \"external_id\": \"mySystem-annotation002\",
            \"title\": \"Bug report\",
            \"annotation_type\": \"BUG\",
            \"result\": \"FAILED\",
            \"summary\": \"This line might introduce a bug.\",
            \"severity\": \"MEDIUM\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Helper.java\",
            \"line\": 13
      }
    ]'
    ```

    ### Possible field values:
    annotation_type: VULNERABILITY, CODE_SMELL, BUG
    result: PASSED, FAILED, IGNORED, SKIPPED
    severity: HIGH, MEDIUM, LOW, CRITICAL

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        json_body (List[ReportAnnotation]):

    Returns:
        Response[List[ReportAnnotation]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    client: Client,
    json_body: List[ReportAnnotation],
) -> Response[List[ReportAnnotation]]:
    """Bulk create or update annotations

     Bulk upload of annotations.
    Annotations are individual findings that have been identified as part of a report, for example, a
    line of code that represents a vulnerability. These annotations can be attached to a specific file
    and even a specific line in that file, however, that is optional. Annotations are not mandatory and
    a report can contain up to 1000 annotations.

    Add the annotations you want to upload as objects in a JSON array and make sure each annotation has
    the external_id field set to a unique value. If you want to use an existing id from your own system,
    we recommend prefixing it with your system's name to avoid collisions, for example, mySystem-
    annotation001. The external id can later be used to identify the report as an alternative to the
    generated [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). You
    can upload up to 100 annotations per POST request.

    ### Sample cURL request:
    ```
    curl --location 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001/annotations' \
    --header 'Content-Type: application/json' \
    --data-raw '[
      {
            \"external_id\": \"mysystem-annotation001\",
            \"title\": \"Security scan report\",
            \"annotation_type\": \"VULNERABILITY\",
            \"summary\": \"This line represents a security threat.\",
            \"severity\": \"HIGH\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\",
            \"line\": 42
      },
      {
            \"external_id\": \"mySystem-annotation002\",
            \"title\": \"Bug report\",
            \"annotation_type\": \"BUG\",
            \"result\": \"FAILED\",
            \"summary\": \"This line might introduce a bug.\",
            \"severity\": \"MEDIUM\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Helper.java\",
            \"line\": 13
      }
    ]'
    ```

    ### Possible field values:
    annotation_type: VULNERABILITY, CODE_SMELL, BUG
    result: PASSED, FAILED, IGNORED, SKIPPED
    severity: HIGH, MEDIUM, LOW, CRITICAL

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        json_body (List[ReportAnnotation]):

    Returns:
        Response[List[ReportAnnotation]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    client: Client,
    json_body: List[ReportAnnotation],
) -> Optional[List[ReportAnnotation]]:
    """Bulk create or update annotations

     Bulk upload of annotations.
    Annotations are individual findings that have been identified as part of a report, for example, a
    line of code that represents a vulnerability. These annotations can be attached to a specific file
    and even a specific line in that file, however, that is optional. Annotations are not mandatory and
    a report can contain up to 1000 annotations.

    Add the annotations you want to upload as objects in a JSON array and make sure each annotation has
    the external_id field set to a unique value. If you want to use an existing id from your own system,
    we recommend prefixing it with your system's name to avoid collisions, for example, mySystem-
    annotation001. The external id can later be used to identify the report as an alternative to the
    generated [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). You
    can upload up to 100 annotations per POST request.

    ### Sample cURL request:
    ```
    curl --location 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001/annotations' \
    --header 'Content-Type: application/json' \
    --data-raw '[
      {
            \"external_id\": \"mysystem-annotation001\",
            \"title\": \"Security scan report\",
            \"annotation_type\": \"VULNERABILITY\",
            \"summary\": \"This line represents a security threat.\",
            \"severity\": \"HIGH\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\",
            \"line\": 42
      },
      {
            \"external_id\": \"mySystem-annotation002\",
            \"title\": \"Bug report\",
            \"annotation_type\": \"BUG\",
            \"result\": \"FAILED\",
            \"summary\": \"This line might introduce a bug.\",
            \"severity\": \"MEDIUM\",
          \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Helper.java\",
            \"line\": 13
      }
    ]'
    ```

    ### Possible field values:
    annotation_type: VULNERABILITY, CODE_SMELL, BUG
    result: PASSED, FAILED, IGNORED, SKIPPED
    severity: HIGH, MEDIUM, LOW, CRITICAL

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        json_body (List[ReportAnnotation]):

    Returns:
        Response[List[ReportAnnotation]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            report_id=report_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
