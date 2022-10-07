from enum import Enum


class SnippetScm(str, Enum):
    GIT = "git"

    def __str__(self) -> str:
        return str(self.value)
