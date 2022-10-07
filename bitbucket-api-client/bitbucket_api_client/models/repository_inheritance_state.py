from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.repository_inheritance_state_override_settings import RepositoryInheritanceStateOverrideSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryInheritanceState")


@attr.s(auto_attribs=True)
class RepositoryInheritanceState:
    """A json object representing the repository's inheritance state values

    Attributes:
        type (str):
        override_settings (Union[Unset, RepositoryInheritanceStateOverrideSettings]):
    """

    type: str
    override_settings: Union[Unset, RepositoryInheritanceStateOverrideSettings] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        override_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.override_settings, Unset):
            override_settings = self.override_settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if override_settings is not UNSET:
            field_dict["override_settings"] = override_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _override_settings = d.pop("override_settings", UNSET)
        override_settings: Union[Unset, RepositoryInheritanceStateOverrideSettings]
        if isinstance(_override_settings, Unset):
            override_settings = UNSET
        else:
            override_settings = RepositoryInheritanceStateOverrideSettings.from_dict(_override_settings)

        repository_inheritance_state = cls(
            type=type,
            override_settings=override_settings,
        )

        repository_inheritance_state.additional_properties = d
        return repository_inheritance_state

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
