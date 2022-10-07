from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MilestoneLinksLink")


@attr.s(auto_attribs=True)
class MilestoneLinksLink:
    """A link to a resource related to this object.

    Attributes:
        href (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    href: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        href = self.href
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href", UNSET)

        name = d.pop("name", UNSET)

        milestone_links_link = cls(
            href=href,
            name=name,
        )

        return milestone_links_link
