from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.account import Account
from ..types import UNSET, Unset

T = TypeVar("T", bound="Author")


@attr.s(auto_attribs=True)
class Author:
    """
    Attributes:
        type (str):
        raw (Union[Unset, str]): The raw author value from the repository. This may be the only value available if the
            author does not match a user in Bitbucket.
        user (Union[Unset, Account]):
    """

    type: str
    raw: Union[Unset, str] = UNSET
    user: Union[Unset, Account] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        raw = self.raw
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if raw is not UNSET:
            field_dict["raw"] = raw
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        raw = d.pop("raw", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, Account]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = Account.from_dict(_user)

        author = cls(
            type=type,
            raw=raw,
            user=user,
        )

        author.additional_properties = d
        return author

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
