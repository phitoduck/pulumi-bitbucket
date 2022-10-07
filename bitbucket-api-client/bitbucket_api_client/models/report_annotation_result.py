from enum import Enum


class ReportAnnotationResult(str, Enum):
    PASSED = "PASSED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"
    IGNORED = "IGNORED"

    def __str__(self) -> str:
        return str(self.value)
