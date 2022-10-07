from enum import Enum


class PipelineStateInProgressName(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"

    def __str__(self) -> str:
        return str(self.value)
