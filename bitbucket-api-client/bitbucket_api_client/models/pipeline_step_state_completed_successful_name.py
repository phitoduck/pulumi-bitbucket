from enum import Enum


class PipelineStepStateCompletedSuccessfulName(str, Enum):
    SUCCESSFUL = "SUCCESSFUL"

    def __str__(self) -> str:
        return str(self.value)
