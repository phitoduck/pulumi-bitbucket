from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.subject_types_workspace_link import SubjectTypesWorkspaceLink
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubjectTypesWorkspace")


@attr.s(auto_attribs=True)
class SubjectTypesWorkspace:
    """
    Attributes:
        events (Union[Unset, SubjectTypesWorkspaceLink]): A link to a resource related to this object.
    """

    events: Union[Unset, SubjectTypesWorkspaceLink] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _events = d.pop("events", UNSET)
        events: Union[Unset, SubjectTypesWorkspaceLink]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = SubjectTypesWorkspaceLink.from_dict(_events)

        subject_types_workspace = cls(
            events=events,
        )

        return subject_types_workspace
