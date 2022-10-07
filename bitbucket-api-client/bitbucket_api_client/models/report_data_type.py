from enum import Enum


class ReportDataType(str, Enum):
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    DURATION = "DURATION"
    LINK = "LINK"
    NUMBER = "NUMBER"
    PERCENTAGE = "PERCENTAGE"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
