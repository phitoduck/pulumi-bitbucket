from enum import Enum


class GetHookEventsSubjectTypeSubjectType(str, Enum):
    REPOSITORY = "repository"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
