from enum import Enum


class GetRepositoriesWorkspaceRepoSlugSrcFormat(str, Enum):
    META = "meta"

    def __str__(self) -> str:
        return str(self.value)
