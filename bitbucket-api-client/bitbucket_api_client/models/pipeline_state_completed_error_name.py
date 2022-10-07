from enum import Enum


class PipelineStateCompletedErrorName(str, Enum):
    ERROR = "ERROR"

    def __str__(self) -> str:
        return str(self.value)
