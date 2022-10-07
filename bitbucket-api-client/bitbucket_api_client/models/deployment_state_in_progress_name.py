from enum import Enum


class DeploymentStateInProgressName(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"

    def __str__(self) -> str:
        return str(self.value)
