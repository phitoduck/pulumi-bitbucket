from enum import Enum


class PipelineStepStateCompletedFailedName(str, Enum):
    FAILED = "FAILED"

    def __str__(self) -> str:
        return str(self.value)
