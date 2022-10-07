from enum import Enum


class GetRepositoriesWorkspaceRepoSlugPullrequestsState(str, Enum):
    OPEN = "OPEN"
    MERGED = "MERGED"
    DECLINED = "DECLINED"
    SUPERSEDED = "SUPERSEDED"

    def __str__(self) -> str:
        return str(self.value)
