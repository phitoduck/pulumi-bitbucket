from enum import Enum


class PipelineStateInProgressPausedName(str, Enum):
    PAUSED = "PAUSED"

    def __str__(self) -> str:
        return str(self.value)
