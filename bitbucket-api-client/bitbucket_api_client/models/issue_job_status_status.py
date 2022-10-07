from enum import Enum


class IssueJobStatusStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    STARTED = "STARTED"
    RUNNING = "RUNNING"
    FAILURE = "FAILURE"

    def __str__(self) -> str:
        return str(self.value)
