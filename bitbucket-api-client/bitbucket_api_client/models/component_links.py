from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.component_links_link import ComponentLinksLink
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentLinks")


@attr.s(auto_attribs=True)
class ComponentLinks:
    """
    Attributes:
        self_ (Union[Unset, ComponentLinksLink]): A link to a resource related to this object.
    """

    self_: Union[Unset, ComponentLinksLink] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        self_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, ComponentLinksLink]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = ComponentLinksLink.from_dict(_self_)

        component_links = cls(
            self_=self_,
        )

        return component_links
