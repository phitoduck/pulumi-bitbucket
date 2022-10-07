from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ProjectBranchingModelProduction")


@attr.s(auto_attribs=True)
class ProjectBranchingModelProduction:
    """
    Attributes:
        name (str): Name of the target branch. If inherited by a repository, it will default to the main branch if the
            specified branch does not exist.
        use_mainbranch (bool): Indicates if the setting points at an explicit branch (`false`) or tracks the main branch
            (`true`).
    """

    name: str
    use_mainbranch: bool

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        use_mainbranch = self.use_mainbranch

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "use_mainbranch": use_mainbranch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        use_mainbranch = d.pop("use_mainbranch")

        project_branching_model_production = cls(
            name=name,
            use_mainbranch=use_mainbranch,
        )

        return project_branching_model_production
