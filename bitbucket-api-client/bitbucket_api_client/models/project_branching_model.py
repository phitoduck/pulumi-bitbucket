from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.project_branching_model_branch_types_item import ProjectBranchingModelBranchTypesItem
from ..models.project_branching_model_development import ProjectBranchingModelDevelopment
from ..models.project_branching_model_production import ProjectBranchingModelProduction
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectBranchingModel")


@attr.s(auto_attribs=True)
class ProjectBranchingModel:
    """
    Attributes:
        type (str):
        branch_types (Union[Unset, List[ProjectBranchingModelBranchTypesItem]]): The active branch types.
        development (Union[Unset, ProjectBranchingModelDevelopment]):
        production (Union[Unset, ProjectBranchingModelProduction]):
    """

    type: str
    branch_types: Union[Unset, List[ProjectBranchingModelBranchTypesItem]] = UNSET
    development: Union[Unset, ProjectBranchingModelDevelopment] = UNSET
    production: Union[Unset, ProjectBranchingModelProduction] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        branch_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.branch_types, Unset):
            branch_types = []
            for branch_types_item_data in self.branch_types:
                branch_types_item = branch_types_item_data.to_dict()

                branch_types.append(branch_types_item)

        development: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.development, Unset):
            development = self.development.to_dict()

        production: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.production, Unset):
            production = self.production.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if branch_types is not UNSET:
            field_dict["branch_types"] = branch_types
        if development is not UNSET:
            field_dict["development"] = development
        if production is not UNSET:
            field_dict["production"] = production

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        branch_types = []
        _branch_types = d.pop("branch_types", UNSET)
        for branch_types_item_data in _branch_types or []:
            branch_types_item = ProjectBranchingModelBranchTypesItem.from_dict(branch_types_item_data)

            branch_types.append(branch_types_item)

        _development = d.pop("development", UNSET)
        development: Union[Unset, ProjectBranchingModelDevelopment]
        if isinstance(_development, Unset):
            development = UNSET
        else:
            development = ProjectBranchingModelDevelopment.from_dict(_development)

        _production = d.pop("production", UNSET)
        production: Union[Unset, ProjectBranchingModelProduction]
        if isinstance(_production, Unset):
            production = UNSET
        else:
            production = ProjectBranchingModelProduction.from_dict(_production)

        project_branching_model = cls(
            type=type,
            branch_types=branch_types,
            development=development,
            production=production,
        )

        project_branching_model.additional_properties = d
        return project_branching_model

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
