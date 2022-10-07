from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.hook_event_event import HookEventEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="HookEvent")


@attr.s(auto_attribs=True)
class HookEvent:
    """An event, associated with a resource or subject type.

    Attributes:
        event (Union[Unset, HookEventEvent]): The event identifier.
        category (Union[Unset, str]): The category this event belongs to.
        label (Union[Unset, str]): Summary of the webhook event type.
        description (Union[Unset, str]): More detailed description of the webhook event type.
    """

    event: Union[Unset, HookEventEvent] = UNSET
    category: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        event: Union[Unset, str] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.value

        category = self.category
        label = self.label
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event
        if category is not UNSET:
            field_dict["category"] = category
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _event = d.pop("event", UNSET)
        event: Union[Unset, HookEventEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = HookEventEvent(_event)

        category = d.pop("category", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        hook_event = cls(
            event=event,
            category=category,
            label=label,
            description=description,
        )

        return hook_event
