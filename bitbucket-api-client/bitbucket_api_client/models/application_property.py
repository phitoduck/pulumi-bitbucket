from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.application_property_attributes_item import ApplicationPropertyAttributesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationProperty")


@attr.s(auto_attribs=True)
class ApplicationProperty:
    """An application property. It is a caller defined JSON object that Bitbucket will store and return.
    The `_attributes` field at its top level can be used to control who is allowed to read and update the property.
    The keys of the JSON object must match an allowed pattern. For details,
    see [Application properties](/cloud/bitbucket/application-properties/).

        Attributes:
            attributes (Union[Unset, List[ApplicationPropertyAttributesItem]]):
    """

    attributes: Union[Unset, List[ApplicationPropertyAttributesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.value

                attributes.append(attributes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["_attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attributes = []
        _attributes = d.pop("_attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = ApplicationPropertyAttributesItem(attributes_item_data)

            attributes.append(attributes_item)

        application_property = cls(
            attributes=attributes,
        )

        application_property.additional_properties = d
        return application_property

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
