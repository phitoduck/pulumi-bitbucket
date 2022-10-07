from enum import Enum


class PipelineStepStateCompletedExpiredName(str, Enum):
    EXPIRED = "EXPIRED"

    def __str__(self) -> str:
        return str(self.value)
