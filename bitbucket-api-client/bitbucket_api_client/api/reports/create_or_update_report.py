from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.report import Report
from ...types import Response


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    client: Client,
    json_body: Report,
) -> Dict[str, Any]:
    url = "{}/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}".format(
        client.base_url, workspace=workspace, repo_slug=repo_slug, commit=commit, reportId=report_id
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, Report]]:
    if response.status_code == 200:
        response_200 = Report.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, Report]]:
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
    json_body: Report,
) -> Response[Union[Error, Report]]:
    """Create or update a report

     Creates or updates a report for the specified commit.
    To upload a report, make sure to generate an ID that is unique across all reports for that commit.
    If you want to use an existing id from your own system, we recommend prefixing it with your system's
    name to avoid collisions, for example, mySystem-001.

    ### Sample cURL request:
    ```
    curl --request PUT 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        \"title\": \"Security scan report\",
        \"details\": \"This pull request introduces 10 new dependency vulnerabilities.\",
        \"report_type\": \"SECURITY\",
        \"reporter\": \"mySystem\",
        \"link\": \"http://www.mysystem.com/reports/001\",
        \"result\": \"FAILED\",
        \"data\": [
            {
                \"title\": \"Duration (seconds)\",
                \"type\": \"DURATION\",
                \"value\": 14
            },
            {
                \"title\": \"Safe to merge?\",
                \"type\": \"BOOLEAN\",
                \"value\": false
            }
        ]
    }'
    ```

    ### Possible field values:
    report_type: SECURITY, COVERAGE, TEST, BUG
    result: PASSED, FAILED, PENDING
    data.type: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE, TEXT

    #### Data field formats
    | Type  Field   | Value Field Type  | Value Field Display |
    |:--------------|:------------------|:--------------------|
    | None/ Omitted | Number, String or Boolean (not an array or object) | Plain text |
    | BOOLEAN	| Boolean | The value will be read as a JSON boolean and displayed as 'Yes' or 'No'. |
    | DATE  | Number | The value will be read as a JSON number in the form of a Unix timestamp
    (milliseconds) and will be displayed as a relative date if the date is less than one week ago,
    otherwise  it will be displayed as an absolute date. |
    | DURATION | Number | The value will be read as a JSON number in milliseconds and will be displayed
    in a human readable duration format. |
    | LINK | Object: `{\"text\": \"Link text here\", \"href\":
    \"https://link.to.annotation/in/external/tool\"}` | The value will be read as a JSON object
    containing the fields \"text\" and \"href\" and will be displayed as a clickable link on the report.
    |
    | NUMBER | Number | The value will be read as a JSON number and large numbers will be  displayed in
    a human readable format (e.g. 14.3k). |
    | PERCENTAGE | Number (between 0 and 100) | The value will be read as a JSON number between 0 and
    100 and will be displayed with a percentage sign. |
    | TEXT | String | The value will be read as a JSON string and will be displayed as-is |

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        json_body (Report):

    Returns:
        Response[Union[Error, Report]]
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
    json_body: Report,
) -> Optional[Union[Error, Report]]:
    """Create or update a report

     Creates or updates a report for the specified commit.
    To upload a report, make sure to generate an ID that is unique across all reports for that commit.
    If you want to use an existing id from your own system, we recommend prefixing it with your system's
    name to avoid collisions, for example, mySystem-001.

    ### Sample cURL request:
    ```
    curl --request PUT 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        \"title\": \"Security scan report\",
        \"details\": \"This pull request introduces 10 new dependency vulnerabilities.\",
        \"report_type\": \"SECURITY\",
        \"reporter\": \"mySystem\",
        \"link\": \"http://www.mysystem.com/reports/001\",
        \"result\": \"FAILED\",
        \"data\": [
            {
                \"title\": \"Duration (seconds)\",
                \"type\": \"DURATION\",
                \"value\": 14
            },
            {
                \"title\": \"Safe to merge?\",
                \"type\": \"BOOLEAN\",
                \"value\": false
            }
        ]
    }'
    ```

    ### Possible field values:
    report_type: SECURITY, COVERAGE, TEST, BUG
    result: PASSED, FAILED, PENDING
    data.type: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE, TEXT

    #### Data field formats
    | Type  Field   | Value Field Type  | Value Field Display |
    |:--------------|:------------------|:--------------------|
    | None/ Omitted | Number, String or Boolean (not an array or object) | Plain text |
    | BOOLEAN	| Boolean | The value will be read as a JSON boolean and displayed as 'Yes' or 'No'. |
    | DATE  | Number | The value will be read as a JSON number in the form of a Unix timestamp
    (milliseconds) and will be displayed as a relative date if the date is less than one week ago,
    otherwise  it will be displayed as an absolute date. |
    | DURATION | Number | The value will be read as a JSON number in milliseconds and will be displayed
    in a human readable duration format. |
    | LINK | Object: `{\"text\": \"Link text here\", \"href\":
    \"https://link.to.annotation/in/external/tool\"}` | The value will be read as a JSON object
    containing the fields \"text\" and \"href\" and will be displayed as a clickable link on the report.
    |
    | NUMBER | Number | The value will be read as a JSON number and large numbers will be  displayed in
    a human readable format (e.g. 14.3k). |
    | PERCENTAGE | Number (between 0 and 100) | The value will be read as a JSON number between 0 and
    100 and will be displayed with a percentage sign. |
    | TEXT | String | The value will be read as a JSON string and will be displayed as-is |

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        json_body (Report):

    Returns:
        Response[Union[Error, Report]]
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
    json_body: Report,
) -> Response[Union[Error, Report]]:
    """Create or update a report

     Creates or updates a report for the specified commit.
    To upload a report, make sure to generate an ID that is unique across all reports for that commit.
    If you want to use an existing id from your own system, we recommend prefixing it with your system's
    name to avoid collisions, for example, mySystem-001.

    ### Sample cURL request:
    ```
    curl --request PUT 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        \"title\": \"Security scan report\",
        \"details\": \"This pull request introduces 10 new dependency vulnerabilities.\",
        \"report_type\": \"SECURITY\",
        \"reporter\": \"mySystem\",
        \"link\": \"http://www.mysystem.com/reports/001\",
        \"result\": \"FAILED\",
        \"data\": [
            {
                \"title\": \"Duration (seconds)\",
                \"type\": \"DURATION\",
                \"value\": 14
            },
            {
                \"title\": \"Safe to merge?\",
                \"type\": \"BOOLEAN\",
                \"value\": false
            }
        ]
    }'
    ```

    ### Possible field values:
    report_type: SECURITY, COVERAGE, TEST, BUG
    result: PASSED, FAILED, PENDING
    data.type: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE, TEXT

    #### Data field formats
    | Type  Field   | Value Field Type  | Value Field Display |
    |:--------------|:------------------|:--------------------|
    | None/ Omitted | Number, String or Boolean (not an array or object) | Plain text |
    | BOOLEAN	| Boolean | The value will be read as a JSON boolean and displayed as 'Yes' or 'No'. |
    | DATE  | Number | The value will be read as a JSON number in the form of a Unix timestamp
    (milliseconds) and will be displayed as a relative date if the date is less than one week ago,
    otherwise  it will be displayed as an absolute date. |
    | DURATION | Number | The value will be read as a JSON number in milliseconds and will be displayed
    in a human readable duration format. |
    | LINK | Object: `{\"text\": \"Link text here\", \"href\":
    \"https://link.to.annotation/in/external/tool\"}` | The value will be read as a JSON object
    containing the fields \"text\" and \"href\" and will be displayed as a clickable link on the report.
    |
    | NUMBER | Number | The value will be read as a JSON number and large numbers will be  displayed in
    a human readable format (e.g. 14.3k). |
    | PERCENTAGE | Number (between 0 and 100) | The value will be read as a JSON number between 0 and
    100 and will be displayed with a percentage sign. |
    | TEXT | String | The value will be read as a JSON string and will be displayed as-is |

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        json_body (Report):

    Returns:
        Response[Union[Error, Report]]
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
    json_body: Report,
) -> Optional[Union[Error, Report]]:
    """Create or update a report

     Creates or updates a report for the specified commit.
    To upload a report, make sure to generate an ID that is unique across all reports for that commit.
    If you want to use an existing id from your own system, we recommend prefixing it with your system's
    name to avoid collisions, for example, mySystem-001.

    ### Sample cURL request:
    ```
    curl --request PUT 'https://api.bitbucket.org/2.0/repositories/<username>/<reposity-
    name>/commit/<commit-hash>/reports/mysystem-001' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        \"title\": \"Security scan report\",
        \"details\": \"This pull request introduces 10 new dependency vulnerabilities.\",
        \"report_type\": \"SECURITY\",
        \"reporter\": \"mySystem\",
        \"link\": \"http://www.mysystem.com/reports/001\",
        \"result\": \"FAILED\",
        \"data\": [
            {
                \"title\": \"Duration (seconds)\",
                \"type\": \"DURATION\",
                \"value\": 14
            },
            {
                \"title\": \"Safe to merge?\",
                \"type\": \"BOOLEAN\",
                \"value\": false
            }
        ]
    }'
    ```

    ### Possible field values:
    report_type: SECURITY, COVERAGE, TEST, BUG
    result: PASSED, FAILED, PENDING
    data.type: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE, TEXT

    #### Data field formats
    | Type  Field   | Value Field Type  | Value Field Display |
    |:--------------|:------------------|:--------------------|
    | None/ Omitted | Number, String or Boolean (not an array or object) | Plain text |
    | BOOLEAN	| Boolean | The value will be read as a JSON boolean and displayed as 'Yes' or 'No'. |
    | DATE  | Number | The value will be read as a JSON number in the form of a Unix timestamp
    (milliseconds) and will be displayed as a relative date if the date is less than one week ago,
    otherwise  it will be displayed as an absolute date. |
    | DURATION | Number | The value will be read as a JSON number in milliseconds and will be displayed
    in a human readable duration format. |
    | LINK | Object: `{\"text\": \"Link text here\", \"href\":
    \"https://link.to.annotation/in/external/tool\"}` | The value will be read as a JSON object
    containing the fields \"text\" and \"href\" and will be displayed as a clickable link on the report.
    |
    | NUMBER | Number | The value will be read as a JSON number and large numbers will be  displayed in
    a human readable format (e.g. 14.3k). |
    | PERCENTAGE | Number (between 0 and 100) | The value will be read as a JSON number between 0 and
    100 and will be displayed with a percentage sign. |
    | TEXT | String | The value will be read as a JSON string and will be displayed as-is |

    Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-
    insights-994316785.html) for more information.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        report_id (str):
        json_body (Report):

    Returns:
        Response[Union[Error, Report]]
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
