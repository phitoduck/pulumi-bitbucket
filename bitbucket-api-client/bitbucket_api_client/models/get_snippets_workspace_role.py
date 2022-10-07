from enum import Enum


class GetSnippetsWorkspaceRole(str, Enum):
    OWNER = "owner"
    CONTRIBUTOR = "contributor"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
