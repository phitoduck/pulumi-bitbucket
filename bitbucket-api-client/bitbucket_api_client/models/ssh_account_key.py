import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.account import Account
from ..models.ssh_key_links import SshKeyLinks
from ..types import UNSET, Unset

T = TypeVar("T", bound="SshAccountKey")


@attr.s(auto_attribs=True)
class SshAccountKey:
    """
    Attributes:
        type (str):
        uuid (Union[Unset, str]): The SSH key's immutable ID.
        key (Union[Unset, str]): The SSH public key value in OpenSSH format.
        comment (Union[Unset, str]): The comment parsed from the SSH key (if present)
        label (Union[Unset, str]): The user-defined label for the SSH key
        created_on (Union[Unset, datetime.datetime]):
        last_used (Union[Unset, datetime.datetime]):
        links (Union[Unset, SshKeyLinks]):
        owner (Union[Unset, Account]):
    """

    type: str
    uuid: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    created_on: Union[Unset, datetime.datetime] = UNSET
    last_used: Union[Unset, datetime.datetime] = UNSET
    links: Union[Unset, SshKeyLinks] = UNSET
    owner: Union[Unset, Account] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        uuid = self.uuid
        key = self.key
        comment = self.comment
        label = self.label
        created_on: Union[Unset, str] = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        last_used: Union[Unset, str] = UNSET
        if not isinstance(self.last_used, Unset):
            last_used = self.last_used.isoformat()

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

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
        if comment is not UNSET:
            field_dict["comment"] = comment
        if label is not UNSET:
            field_dict["label"] = label
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if links is not UNSET:
            field_dict["links"] = links
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        key = d.pop("key", UNSET)

        comment = d.pop("comment", UNSET)

        label = d.pop("label", UNSET)

        _created_on = d.pop("created_on", UNSET)
        created_on: Union[Unset, datetime.datetime]
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _last_used = d.pop("last_used", UNSET)
        last_used: Union[Unset, datetime.datetime]
        if isinstance(_last_used, Unset):
            last_used = UNSET
        else:
            last_used = isoparse(_last_used)

        _links = d.pop("links", UNSET)
        links: Union[Unset, SshKeyLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SshKeyLinks.from_dict(_links)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, Account]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = Account.from_dict(_owner)

        ssh_account_key = cls(
            type=type,
            uuid=uuid,
            key=key,
            comment=comment,
            label=label,
            created_on=created_on,
            last_used=last_used,
            links=links,
            owner=owner,
        )

        ssh_account_key.additional_properties = d
        return ssh_account_key

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
