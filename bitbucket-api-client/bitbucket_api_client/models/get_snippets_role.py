from enum import Enum


class GetSnippetsRole(str, Enum):
    OWNER = "owner"
    CONTRIBUTOR = "contributor"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
