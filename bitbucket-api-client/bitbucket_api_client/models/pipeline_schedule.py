import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.pipeline_selector import PipelineSelector
from ..models.pipeline_target import PipelineTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineSchedule")


@attr.s(auto_attribs=True)
class PipelineSchedule:
    """
    Attributes:
        type (str):
        uuid (Union[Unset, str]): The UUID identifying the schedule.
        enabled (Union[Unset, bool]): Whether the schedule is enabled.
        target (Union[Unset, PipelineTarget]):
        selector (Union[Unset, PipelineSelector]):
        cron_pattern (Union[Unset, str]): The cron expression that the schedule applies.
        created_on (Union[Unset, datetime.datetime]): The timestamp when the schedule was created.
        updated_on (Union[Unset, datetime.datetime]): The timestamp when the schedule was updated.
    """

    type: str
    uuid: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    target: Union[Unset, PipelineTarget] = UNSET
    selector: Union[Unset, PipelineSelector] = UNSET
    cron_pattern: Union[Unset, str] = UNSET
    created_on: Union[Unset, datetime.datetime] = UNSET
    updated_on: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        uuid = self.uuid
        enabled = self.enabled
        target: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        selector: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector.to_dict()

        cron_pattern = self.cron_pattern
        created_on: Union[Unset, str] = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: Union[Unset, str] = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if target is not UNSET:
            field_dict["target"] = target
        if selector is not UNSET:
            field_dict["selector"] = selector
        if cron_pattern is not UNSET:
            field_dict["cron_pattern"] = cron_pattern
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        enabled = d.pop("enabled", UNSET)

        _target = d.pop("target", UNSET)
        target: Union[Unset, PipelineTarget]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = PipelineTarget.from_dict(_target)

        _selector = d.pop("selector", UNSET)
        selector: Union[Unset, PipelineSelector]
        if isinstance(_selector, Unset):
            selector = UNSET
        else:
            selector = PipelineSelector.from_dict(_selector)

        cron_pattern = d.pop("cron_pattern", UNSET)

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

        pipeline_schedule = cls(
            type=type,
            uuid=uuid,
            enabled=enabled,
            target=target,
            selector=selector,
            cron_pattern=cron_pattern,
            created_on=created_on,
            updated_on=updated_on,
        )

        pipeline_schedule.additional_properties = d
        return pipeline_schedule

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
