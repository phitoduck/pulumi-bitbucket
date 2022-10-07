from enum import Enum


class PipelineStepStatePendingName(str, Enum):
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
