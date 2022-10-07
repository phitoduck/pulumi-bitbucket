from enum import Enum


class ReportAnnotationAnnotationType(str, Enum):
    VULNERABILITY = "VULNERABILITY"
    CODE_SMELL = "CODE_SMELL"
    BUG = "BUG"

    def __str__(self) -> str:
        return str(self.value)
