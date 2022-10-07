from enum import Enum


class ReportReportType(str, Enum):
    SECURITY = "SECURITY"
    COVERAGE = "COVERAGE"
    TEST = "TEST"
    BUG = "BUG"

    def __str__(self) -> str:
        return str(self.value)
