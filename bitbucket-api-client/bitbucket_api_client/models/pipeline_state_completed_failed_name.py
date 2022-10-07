from enum import Enum


class PipelineStateCompletedFailedName(str, Enum):
    FAILED = "FAILED"

    def __str__(self) -> str:
        return str(self.value)
