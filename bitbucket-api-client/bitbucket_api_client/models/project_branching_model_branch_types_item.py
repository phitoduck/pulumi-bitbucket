from typing import Any, Dict, Type, TypeVar

import attr

from ..models.project_branching_model_branch_types_item_kind import ProjectBranchingModelBranchTypesItemKind

T = TypeVar("T", bound="ProjectBranchingModelBranchTypesItem")


@attr.s(auto_attribs=True)
class ProjectBranchingModelBranchTypesItem:
    """
    Attributes:
        kind (ProjectBranchingModelBranchTypesItemKind): The kind of branch.
        prefix (str): The prefix for this branch type. A branch with this prefix will be classified as per `kind`. The
            prefix must be a valid prefix for a branch and must always exist. It cannot be blank, empty or `null`.
    """

    kind: ProjectBranchingModelBranchTypesItemKind
    prefix: str

    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind.value

        prefix = self.prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "kind": kind,
                "prefix": prefix,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kind = ProjectBranchingModelBranchTypesItemKind(d.pop("kind"))

        prefix = d.pop("prefix")

        project_branching_model_branch_types_item = cls(
            kind=kind,
            prefix=prefix,
        )

        return project_branching_model_branch_types_item
