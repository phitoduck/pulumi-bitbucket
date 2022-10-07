from enum import Enum


class PipelineStateInProgressRunningName(str, Enum):
    RUNNING = "RUNNING"

    def __str__(self) -> str:
        return str(self.value)
