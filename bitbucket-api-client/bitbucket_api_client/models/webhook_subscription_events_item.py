from enum import Enum


class WebhookSubscriptionEventsItem(str, Enum):
    PULLREQUESTUPDATED = "pullrequest:updated"
    REPOCOMMIT_STATUS_CREATED = "repo:commit_status_created"
    PULLREQUESTREJECTED = "pullrequest:rejected"
    ISSUECREATED = "issue:created"
    PULLREQUESTCOMMENT_UPDATED = "pullrequest:comment_updated"
    PROJECTUPDATED = "project:updated"
    REPOFORK = "repo:fork"
    REPODELETED = "repo:deleted"
    REPOCOMMIT_STATUS_UPDATED = "repo:commit_status_updated"
    ISSUEUPDATED = "issue:updated"
    REPOCREATED = "repo:created"
    PULLREQUESTAPPROVED = "pullrequest:approved"
    PULLREQUESTCOMMENT_DELETED = "pullrequest:comment_deleted"
    REPOIMPORTED = "repo:imported"
    REPOPUSH = "repo:push"
    REPOUPDATED = "repo:updated"
    PULLREQUESTCOMMENT_CREATED = "pullrequest:comment_created"
    PULLREQUESTCHANGES_REQUEST_CREATED = "pullrequest:changes_request_created"
    PULLREQUESTFULFILLED = "pullrequest:fulfilled"
    PULLREQUESTCREATED = "pullrequest:created"
    REPOCOMMIT_COMMENT_CREATED = "repo:commit_comment_created"
    REPOTRANSFER = "repo:transfer"
    ISSUECOMMENT_CREATED = "issue:comment_created"
    PULLREQUESTCHANGES_REQUEST_REMOVED = "pullrequest:changes_request_removed"
    PULLREQUESTUNAPPROVED = "pullrequest:unapproved"

    def __str__(self) -> str:
        return str(self.value)
