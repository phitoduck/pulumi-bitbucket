from enum import Enum


class PipelineStepStateCompletedName(str, Enum):
    COMPLETED = "COMPLETED"

    def __str__(self) -> str:
        return str(self.value)
