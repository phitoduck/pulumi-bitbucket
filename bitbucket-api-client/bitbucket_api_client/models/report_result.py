from enum import Enum


class ReportResult(str, Enum):
    PASSED = "PASSED"
    FAILED = "FAILED"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
