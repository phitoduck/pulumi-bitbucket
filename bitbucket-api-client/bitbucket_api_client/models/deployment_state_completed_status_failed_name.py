from enum import Enum


class DeploymentStateCompletedStatusFailedName(str, Enum):
    FAILED = "FAILED"

    def __str__(self) -> str:
        return str(self.value)
