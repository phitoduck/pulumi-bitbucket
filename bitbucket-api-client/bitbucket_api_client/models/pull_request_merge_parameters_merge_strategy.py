from enum import Enum


class PullRequestMergeParametersMergeStrategy(str, Enum):
    MERGE_COMMIT = "merge_commit"
    SQUASH = "squash"
    FAST_FORWARD = "fast_forward"

    def __str__(self) -> str:
        return str(self.value)
