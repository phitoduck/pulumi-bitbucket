from enum import Enum


class PipelineStateCompletedName(str, Enum):
    COMPLETED = "COMPLETED"

    def __str__(self) -> str:
        return str(self.value)
