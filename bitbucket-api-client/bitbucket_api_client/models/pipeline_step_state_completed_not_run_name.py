from enum import Enum


class PipelineStepStateCompletedNotRunName(str, Enum):
    NOT_RUN = "NOT_RUN"

    def __str__(self) -> str:
        return str(self.value)
