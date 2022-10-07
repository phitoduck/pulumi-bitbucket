from enum import Enum


class BranchingModelSettingsBranchTypesItemKind(str, Enum):
    FEATURE = "feature"
    BUGFIX = "bugfix"
    RELEASE = "release"
    HOTFIX = "hotfix"

    def __str__(self) -> str:
        return str(self.value)
