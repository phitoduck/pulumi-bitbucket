from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportOptions")


@attr.s(auto_attribs=True)
class ExportOptions:
    """Options for issue export.

    Attributes:
        type (str):
        project_key (Union[Unset, str]):
        project_name (Union[Unset, str]):
        send_email (Union[Unset, bool]):
        include_attachments (Union[Unset, bool]):
    """

    type: str
    project_key: Union[Unset, str] = UNSET
    project_name: Union[Unset, str] = UNSET
    send_email: Union[Unset, bool] = UNSET
    include_attachments: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        project_key = self.project_key
        project_name = self.project_name
        send_email = self.send_email
        include_attachments = self.include_attachments

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if project_key is not UNSET:
            field_dict["project_key"] = project_key
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if send_email is not UNSET:
            field_dict["send_email"] = send_email
        if include_attachments is not UNSET:
            field_dict["include_attachments"] = include_attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        project_key = d.pop("project_key", UNSET)

        project_name = d.pop("project_name", UNSET)

        send_email = d.pop("send_email", UNSET)

        include_attachments = d.pop("include_attachments", UNSET)

        export_options = cls(
            type=type,
            project_key=project_key,
            project_name=project_name,
            send_email=send_email,
            include_attachments=include_attachments,
        )

        export_options.additional_properties = d
        return export_options

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
