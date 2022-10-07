from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentVariable")


@attr.s(auto_attribs=True)
class DeploymentVariable:
    """
    Attributes:
        type (str):
        uuid (Union[Unset, str]): The UUID identifying the variable.
        key (Union[Unset, str]): The unique name of the variable.
        value (Union[Unset, str]): The value of the variable. If the variable is secured, this will be empty.
        secured (Union[Unset, bool]): If true, this variable will be treated as secured. The value will never be exposed
            in the logs or the REST API.
    """

    type: str
    uuid: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    secured: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        uuid = self.uuid
        key = self.key
        value = self.value
        secured = self.secured

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if secured is not UNSET:
            field_dict["secured"] = secured

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        secured = d.pop("secured", UNSET)

        deployment_variable = cls(
            type=type,
            uuid=uuid,
            key=key,
            value=value,
            secured=secured,
        )

        deployment_variable.additional_properties = d
        return deployment_variable

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
