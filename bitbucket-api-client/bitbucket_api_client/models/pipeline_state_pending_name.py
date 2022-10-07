from enum import Enum


class PipelineStatePendingName(str, Enum):
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
