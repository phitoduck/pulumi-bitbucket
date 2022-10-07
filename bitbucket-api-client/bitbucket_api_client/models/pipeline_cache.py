import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineCache")


@attr.s(auto_attribs=True)
class PipelineCache:
    """
    Attributes:
        type (str):
        uuid (Union[Unset, str]): The UUID identifying the pipeline cache.
        pipeline_uuid (Union[Unset, str]): The UUID of the pipeline that created the cache.
        step_uuid (Union[Unset, str]): The uuid of the step that created the cache.
        name (Union[Unset, str]): The name of the cache.
        path (Union[Unset, str]): The path where the cache contents were retrieved from.
        file_size_bytes (Union[Unset, int]): The size of the file containing the archive of the cache.
        created_on (Union[Unset, datetime.datetime]): The timestamp when the cache was created.
    """

    type: str
    uuid: Union[Unset, str] = UNSET
    pipeline_uuid: Union[Unset, str] = UNSET
    step_uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    file_size_bytes: Union[Unset, int] = UNSET
    created_on: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        uuid = self.uuid
        pipeline_uuid = self.pipeline_uuid
        step_uuid = self.step_uuid
        name = self.name
        path = self.path
        file_size_bytes = self.file_size_bytes
        created_on: Union[Unset, str] = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if pipeline_uuid is not UNSET:
            field_dict["pipeline_uuid"] = pipeline_uuid
        if step_uuid is not UNSET:
            field_dict["step_uuid"] = step_uuid
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if file_size_bytes is not UNSET:
            field_dict["file_size_bytes"] = file_size_bytes
        if created_on is not UNSET:
            field_dict["created_on"] = created_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        pipeline_uuid = d.pop("pipeline_uuid", UNSET)

        step_uuid = d.pop("step_uuid", UNSET)

        name = d.pop("name", UNSET)

        path = d.pop("path", UNSET)

        file_size_bytes = d.pop("file_size_bytes", UNSET)

        _created_on = d.pop("created_on", UNSET)
        created_on: Union[Unset, datetime.datetime]
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        pipeline_cache = cls(
            type=type,
            uuid=uuid,
            pipeline_uuid=pipeline_uuid,
            step_uuid=step_uuid,
            name=name,
            path=path,
            file_size_bytes=file_size_bytes,
            created_on=created_on,
        )

        pipeline_cache.additional_properties = d
        return pipeline_cache

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
