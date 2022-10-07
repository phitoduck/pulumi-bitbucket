from enum import Enum


class PipelineSelectorType(str, Enum):
    BRANCHES = "branches"
    TAGS = "tags"
    BOOKMARKS = "bookmarks"
    DEFAULT = "default"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)
