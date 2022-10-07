from enum import Enum


class PipelineStateCompletedStoppedName(str, Enum):
    STOPPED = "STOPPED"

    def __str__(self) -> str:
        return str(self.value)
