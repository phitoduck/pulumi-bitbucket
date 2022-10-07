from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.issue_attachment_links import IssueAttachmentLinks
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueAttachment")


@attr.s(auto_attribs=True)
class IssueAttachment:
    """
    Attributes:
        type (str):
        links (Union[Unset, IssueAttachmentLinks]):
        name (Union[Unset, str]):
    """

    type: str
    links: Union[Unset, IssueAttachmentLinks] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _links = d.pop("links", UNSET)
        links: Union[Unset, IssueAttachmentLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = IssueAttachmentLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        issue_attachment = cls(
            type=type,
            links=links,
            name=name,
        )

        issue_attachment.additional_properties = d
        return issue_attachment

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
