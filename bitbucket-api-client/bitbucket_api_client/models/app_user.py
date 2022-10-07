import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.account_links import AccountLinks
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppUser")


@attr.s(auto_attribs=True)
class AppUser:
    """
    Attributes:
        type (str):
        links (Union[Unset, AccountLinks]): Links related to an Account.
        created_on (Union[Unset, datetime.datetime]):
        display_name (Union[Unset, str]):
        username (Union[Unset, str]):
        uuid (Union[Unset, str]):
        account_id (Union[Unset, str]): The user's Atlassian account ID.
        account_status (Union[Unset, str]): The status of the account. Currently the only possible value is "active",
            but more values may be added in the future.
        kind (Union[Unset, str]): The kind of App User.
    """

    type: str
    links: Union[Unset, AccountLinks] = UNSET
    created_on: Union[Unset, datetime.datetime] = UNSET
    display_name: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    account_status: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        created_on: Union[Unset, str] = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        display_name = self.display_name
        username = self.username
        uuid = self.uuid
        account_id = self.account_id
        account_status = self.account_status
        kind = self.kind

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if username is not UNSET:
            field_dict["username"] = username
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if account_status is not UNSET:
            field_dict["account_status"] = account_status
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _links = d.pop("links", UNSET)
        links: Union[Unset, AccountLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AccountLinks.from_dict(_links)

        _created_on = d.pop("created_on", UNSET)
        created_on: Union[Unset, datetime.datetime]
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        display_name = d.pop("display_name", UNSET)

        username = d.pop("username", UNSET)

        uuid = d.pop("uuid", UNSET)

        account_id = d.pop("account_id", UNSET)

        account_status = d.pop("account_status", UNSET)

        kind = d.pop("kind", UNSET)

        app_user = cls(
            type=type,
            links=links,
            created_on=created_on,
            display_name=display_name,
            username=username,
            uuid=uuid,
            account_id=account_id,
            account_status=account_status,
            kind=kind,
        )

        app_user.additional_properties = d
        return app_user

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
