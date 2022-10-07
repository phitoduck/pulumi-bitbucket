from enum import Enum


class ParticipantState(str, Enum):
    APPROVED = "approved"
    CHANGES_REQUESTED = "changes_requested"

    def __str__(self) -> str:
        return str(self.value)
