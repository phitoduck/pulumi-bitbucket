from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.link import Link
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountLinks")


@attr.s(auto_attribs=True)
class AccountLinks:
    """Links related to an Account.

    Attributes:
        avatar (Union[Unset, Link]): A link to a resource related to this object.
    """

    avatar: Union[Unset, Link] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avatar: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, Link]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = Link.from_dict(_avatar)

        account_links = cls(
            avatar=avatar,
        )

        account_links.additional_properties = d
        return account_links

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
