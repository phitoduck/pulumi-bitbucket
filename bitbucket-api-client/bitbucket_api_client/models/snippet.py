import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.account import Account
from ..models.snippet_scm import SnippetScm
from ..types import UNSET, Unset

T = TypeVar("T", bound="Snippet")


@attr.s(auto_attribs=True)
class Snippet:
    """
    Attributes:
        type (str):
        id (Union[Unset, int]):
        title (Union[Unset, str]):
        scm (Union[Unset, SnippetScm]): The DVCS used to store the snippet.
        created_on (Union[Unset, datetime.datetime]):
        updated_on (Union[Unset, datetime.datetime]):
        owner (Union[Unset, Account]):
        creator (Union[Unset, Account]):
        is_private (Union[Unset, bool]):
    """

    type: str
    id: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    scm: Union[Unset, SnippetScm] = UNSET
    created_on: Union[Unset, datetime.datetime] = UNSET
    updated_on: Union[Unset, datetime.datetime] = UNSET
    owner: Union[Unset, Account] = UNSET
    creator: Union[Unset, Account] = UNSET
    is_private: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        id = self.id
        title = self.title
        scm: Union[Unset, str] = UNSET
        if not isinstance(self.scm, Unset):
            scm = self.scm.value

        created_on: Union[Unset, str] = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: Union[Unset, str] = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        creator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        is_private = self.is_private

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if scm is not UNSET:
            field_dict["scm"] = scm
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on
        if owner is not UNSET:
            field_dict["owner"] = owner
        if creator is not UNSET:
            field_dict["creator"] = creator
        if is_private is not UNSET:
            field_dict["is_private"] = is_private

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        _scm = d.pop("scm", UNSET)
        scm: Union[Unset, SnippetScm]
        if isinstance(_scm, Unset):
            scm = UNSET
        else:
            scm = SnippetScm(_scm)

        _created_on = d.pop("created_on", UNSET)
        created_on: Union[Unset, datetime.datetime]
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _updated_on = d.pop("updated_on", UNSET)
        updated_on: Union[Unset, datetime.datetime]
        if isinstance(_updated_on, Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, Account]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = Account.from_dict(_owner)

        _creator = d.pop("creator", UNSET)
        creator: Union[Unset, Account]
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = Account.from_dict(_creator)

        is_private = d.pop("is_private", UNSET)

        snippet = cls(
            type=type,
            id=id,
            title=title,
            scm=scm,
            created_on=created_on,
            updated_on=updated_on,
            owner=owner,
            creator=creator,
            is_private=is_private,
        )

        snippet.additional_properties = d
        return snippet

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
