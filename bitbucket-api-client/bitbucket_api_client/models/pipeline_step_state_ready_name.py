from enum import Enum


class PipelineStepStateReadyName(str, Enum):
    READY = "READY"

    def __str__(self) -> str:
        return str(self.value)
