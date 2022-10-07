from enum import Enum


class ApplicationPropertyAttributesItem(str, Enum):
    PUBLIC = "public"
    READ_ONLY = "read_only"

    def __str__(self) -> str:
        return str(self.value)
