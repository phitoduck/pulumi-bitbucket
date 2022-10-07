import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.object_ import Object
from ..models.webhook_subscription_events_item import WebhookSubscriptionEventsItem
from ..models.webhook_subscription_subject_type import WebhookSubscriptionSubjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookSubscription")


@attr.s(auto_attribs=True)
class WebhookSubscription:
    """
    Attributes:
        type (str):
        uuid (Union[Unset, str]): The webhook's id
        url (Union[Unset, str]): The URL events get delivered to.
        description (Union[Unset, str]): A user-defined description of the webhook.
        subject_type (Union[Unset, WebhookSubscriptionSubjectType]): The type of entity. Set to either `repository` or
            `workspace` based on where the subscription is defined.
        subject (Union[Unset, Object]): Base type for most resource objects. It defines the common `type` element that
            identifies an object's type. It also identifies the element as Swagger's `discriminator`.
        active (Union[Unset, bool]):
        created_at (Union[Unset, datetime.datetime]):
        events (Union[Unset, List[WebhookSubscriptionEventsItem]]): The events this webhook is subscribed to.
    """

    type: str
    uuid: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    subject_type: Union[Unset, WebhookSubscriptionSubjectType] = UNSET
    subject: Union[Unset, Object] = UNSET
    active: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    events: Union[Unset, List[WebhookSubscriptionEventsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        uuid = self.uuid
        url = self.url
        description = self.description
        subject_type: Union[Unset, str] = UNSET
        if not isinstance(self.subject_type, Unset):
            subject_type = self.subject_type.value

        subject: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject.to_dict()

        active = self.active
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value

                events.append(events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description
        if subject_type is not UNSET:
            field_dict["subject_type"] = subject_type
        if subject is not UNSET:
            field_dict["subject"] = subject
        if active is not UNSET:
            field_dict["active"] = active
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        url = d.pop("url", UNSET)

        description = d.pop("description", UNSET)

        _subject_type = d.pop("subject_type", UNSET)
        subject_type: Union[Unset, WebhookSubscriptionSubjectType]
        if isinstance(_subject_type, Unset):
            subject_type = UNSET
        else:
            subject_type = WebhookSubscriptionSubjectType(_subject_type)

        _subject = d.pop("subject", UNSET)
        subject: Union[Unset, Object]
        if isinstance(_subject, Unset):
            subject = UNSET
        else:
            subject = Object.from_dict(_subject)

        active = d.pop("active", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = WebhookSubscriptionEventsItem(events_item_data)

            events.append(events_item)

        webhook_subscription = cls(
            type=type,
            uuid=uuid,
            url=url,
            description=description,
            subject_type=subject_type,
            subject=subject,
            active=active,
            created_at=created_at,
            events=events,
        )

        webhook_subscription.additional_properties = d
        return webhook_subscription

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
