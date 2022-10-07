from enum import Enum


class DeploymentStateUndeployedName(str, Enum):
    UNDEPLOYED = "UNDEPLOYED"

    def __str__(self) -> str:
        return str(self.value)
