from enum import Enum


class GetWorkspacesRole(str, Enum):
    OWNER = "owner"
    COLLABORATOR = "collaborator"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
