from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.subject_types_repository_link import SubjectTypesRepositoryLink
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubjectTypesRepository")


@attr.s(auto_attribs=True)
class SubjectTypesRepository:
    """
    Attributes:
        events (Union[Unset, SubjectTypesRepositoryLink]): A link to a resource related to this object.
    """

    events: Union[Unset, SubjectTypesRepositoryLink] = UNSET

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
        events: Union[Unset, SubjectTypesRepositoryLink]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = SubjectTypesRepositoryLink.from_dict(_events)

        subject_types_repository = cls(
            events=events,
        )

        return subject_types_repository
