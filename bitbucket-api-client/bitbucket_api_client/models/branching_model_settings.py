from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.branching_model_settings_branch_types_item import BranchingModelSettingsBranchTypesItem
from ..models.branching_model_settings_development import BranchingModelSettingsDevelopment
from ..models.branching_model_settings_links import BranchingModelSettingsLinks
from ..models.branching_model_settings_production import BranchingModelSettingsProduction
from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchingModelSettings")


@attr.s(auto_attribs=True)
class BranchingModelSettings:
    """
    Attributes:
        type (str):
        links (Union[Unset, BranchingModelSettingsLinks]):
        branch_types (Union[Unset, List[BranchingModelSettingsBranchTypesItem]]):
        development (Union[Unset, BranchingModelSettingsDevelopment]):
        production (Union[Unset, BranchingModelSettingsProduction]):
    """

    type: str
    links: Union[Unset, BranchingModelSettingsLinks] = UNSET
    branch_types: Union[Unset, List[BranchingModelSettingsBranchTypesItem]] = UNSET
    development: Union[Unset, BranchingModelSettingsDevelopment] = UNSET
    production: Union[Unset, BranchingModelSettingsProduction] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

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
        if links is not UNSET:
            field_dict["links"] = links
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

        _links = d.pop("links", UNSET)
        links: Union[Unset, BranchingModelSettingsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = BranchingModelSettingsLinks.from_dict(_links)

        branch_types = []
        _branch_types = d.pop("branch_types", UNSET)
        for branch_types_item_data in _branch_types or []:
            branch_types_item = BranchingModelSettingsBranchTypesItem.from_dict(branch_types_item_data)

            branch_types.append(branch_types_item)

        _development = d.pop("development", UNSET)
        development: Union[Unset, BranchingModelSettingsDevelopment]
        if isinstance(_development, Unset):
            development = UNSET
        else:
            development = BranchingModelSettingsDevelopment.from_dict(_development)

        _production = d.pop("production", UNSET)
        production: Union[Unset, BranchingModelSettingsProduction]
        if isinstance(_production, Unset):
            production = UNSET
        else:
            production = BranchingModelSettingsProduction.from_dict(_production)

        branching_model_settings = cls(
            type=type,
            links=links,
            branch_types=branch_types,
            development=development,
            production=production,
        )

        branching_model_settings.additional_properties = d
        return branching_model_settings

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
