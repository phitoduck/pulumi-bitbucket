from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.report_annotation import ReportAnnotation
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    annotation_id: str,
    *,
    client: Client,
    json_body: ReportAnnotation,
) -> Dict[str, Any]:
    url = (
        "{}/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}".format(
            client.base_url,
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            reportId=report_id,
            annotationId=annotation_id,
        )
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, ReportAnnotation]]:
    if response.status_code == 200:
        response_200 = ReportAnnotation.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, ReportAnnotation]]:
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
    annotation_id: str,
    *,
    client: Client,
    json_body: ReportAnnotation,
) -> Response[Union[Error, ReportAnnotation]]:
    """Create or update an annotation

     Creates or updates an individual annotation for the specified report.
    Annotations are individual findings that have been identified as part of a report, for example, a
    line of code that represents a vulnerability. These annotations can be attached to a specific file
    and even a specific line in that file, however, that is optional. Annotations are not mandatory and
    a report can contain up to 1000 annotations.

    Just as reports, annotation needs to be uploaded with a unique ID that can later be used to identify
    the report as an alternative to the generated
    [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). If you want to
    use an existing id from your own system, we recommend prefixing it with your system's name to avoid
    collisions, for example, mySystem-annotation001.

    ### Sample cURL request:
    ```
    curl --request PUT 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mySystem-001/annotations/mysystem-annotation001' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        \"title\": \"Security scan report\",
        \"annotation_type\": \"VULNERABILITY\",
        \"summary\": \"This line represents a security thread.\",
        \"severity\": \"HIGH\",
        \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\",
        \"line\": 42
    }'
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
        annotation_id (str):
        json_body (ReportAnnotation):

    Returns:
        Response[Union[Error, ReportAnnotation]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        annotation_id=annotation_id,
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
    annotation_id: str,
    *,
    client: Client,
    json_body: ReportAnnotation,
) -> Optional[Union[Error, ReportAnnotation]]:
    """Create or update an annotation

     Creates or updates an individual annotation for the specified report.
    Annotations are individual findings that have been identified as part of a report, for example, a
    line of code that represents a vulnerability. These annotations can be attached to a specific file
    and even a specific line in that file, however, that is optional. Annotations are not mandatory and
    a report can contain up to 1000 annotations.

    Just as reports, annotation needs to be uploaded with a unique ID that can later be used to identify
    the report as an alternative to the generated
    [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). If you want to
    use an existing id from your own system, we recommend prefixing it with your system's name to avoid
    collisions, for example, mySystem-annotation001.

    ### Sample cURL request:
    ```
    curl --request PUT 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mySystem-001/annotations/mysystem-annotation001' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        \"title\": \"Security scan report\",
        \"annotation_type\": \"VULNERABILITY\",
        \"summary\": \"This line represents a security thread.\",
        \"severity\": \"HIGH\",
        \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\",
        \"line\": 42
    }'
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
        annotation_id (str):
        json_body (ReportAnnotation):

    Returns:
        Response[Union[Error, ReportAnnotation]]
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        annotation_id=annotation_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    annotation_id: str,
    *,
    client: Client,
    json_body: ReportAnnotation,
) -> Response[Union[Error, ReportAnnotation]]:
    """Create or update an annotation

     Creates or updates an individual annotation for the specified report.
    Annotations are individual findings that have been identified as part of a report, for example, a
    line of code that represents a vulnerability. These annotations can be attached to a specific file
    and even a specific line in that file, however, that is optional. Annotations are not mandatory and
    a report can contain up to 1000 annotations.

    Just as reports, annotation needs to be uploaded with a unique ID that can later be used to identify
    the report as an alternative to the generated
    [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). If you want to
    use an existing id from your own system, we recommend prefixing it with your system's name to avoid
    collisions, for example, mySystem-annotation001.

    ### Sample cURL request:
    ```
    curl --request PUT 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mySystem-001/annotations/mysystem-annotation001' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        \"title\": \"Security scan report\",
        \"annotation_type\": \"VULNERABILITY\",
        \"summary\": \"This line represents a security thread.\",
        \"severity\": \"HIGH\",
        \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\",
        \"line\": 42
    }'
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
        annotation_id (str):
        json_body (ReportAnnotation):

    Returns:
        Response[Union[Error, ReportAnnotation]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        report_id=report_id,
        annotation_id=annotation_id,
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
    annotation_id: str,
    *,
    client: Client,
    json_body: ReportAnnotation,
) -> Optional[Union[Error, ReportAnnotation]]:
    """Create or update an annotation

     Creates or updates an individual annotation for the specified report.
    Annotations are individual findings that have been identified as part of a report, for example, a
    line of code that represents a vulnerability. These annotations can be attached to a specific file
    and even a specific line in that file, however, that is optional. Annotations are not mandatory and
    a report can contain up to 1000 annotations.

    Just as reports, annotation needs to be uploaded with a unique ID that can later be used to identify
    the report as an alternative to the generated
    [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). If you want to
    use an existing id from your own system, we recommend prefixing it with your system's name to avoid
    collisions, for example, mySystem-annotation001.

    ### Sample cURL request:
    ```
    curl --request PUT 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mySystem-001/annotations/mysystem-annotation001' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        \"title\": \"Security scan report\",
        \"annotation_type\": \"VULNERABILITY\",
        \"summary\": \"This line represents a security thread.\",
        \"severity\": \"HIGH\",
        \"path\": \"my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\",
        \"line\": 42
    }'
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
        annotation_id (str):
        json_body (ReportAnnotation):

    Returns:
        Response[Union[Error, ReportAnnotation]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            report_id=report_id,
            annotation_id=annotation_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
