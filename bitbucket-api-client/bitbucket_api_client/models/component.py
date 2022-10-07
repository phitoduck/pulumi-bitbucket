from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.component_links import ComponentLinks
from ..types import UNSET, Unset

T = TypeVar("T", bound="Component")


@attr.s(auto_attribs=True)
class Component:
    """
    Attributes:
        type (str):
        links (Union[Unset, ComponentLinks]):
        name (Union[Unset, str]):
        id (Union[Unset, int]):
    """

    type: str
    links: Union[Unset, ComponentLinks] = UNSET
    name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _links = d.pop("links", UNSET)
        links: Union[Unset, ComponentLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ComponentLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        component = cls(
            type=type,
            links=links,
            name=name,
            id=id,
        )

        component.additional_properties = d
        return component

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
