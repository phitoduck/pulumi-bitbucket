from enum import Enum


class GetRepositoriesWorkspaceRepoSlugSrcCommitPathFormat(str, Enum):
    META = "meta"
    RENDERED = "rendered"

    def __str__(self) -> str:
        return str(self.value)
