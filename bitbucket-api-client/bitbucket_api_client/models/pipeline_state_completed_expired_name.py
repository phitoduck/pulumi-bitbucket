from enum import Enum


class PipelineStateCompletedExpiredName(str, Enum):
    EXPIRED = "EXPIRED"

    def __str__(self) -> str:
        return str(self.value)
