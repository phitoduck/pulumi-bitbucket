from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.ssh_key_links_link import SshKeyLinksLink
from ..types import UNSET, Unset

T = TypeVar("T", bound="SshKeyLinks")


@attr.s(auto_attribs=True)
class SshKeyLinks:
    """
    Attributes:
        self_ (Union[Unset, SshKeyLinksLink]): A link to a resource related to this object.
    """

    self_: Union[Unset, SshKeyLinksLink] = UNSET

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
        self_: Union[Unset, SshKeyLinksLink]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = SshKeyLinksLink.from_dict(_self_)

        ssh_key_links = cls(
            self_=self_,
        )

        return ssh_key_links
