from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pipeline_ssh_public_key import PipelineSshPublicKey
from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineKnownHost")


@attr.s(auto_attribs=True)
class PipelineKnownHost:
    """
    Attributes:
        type (str):
        uuid (Union[Unset, str]): The UUID identifying the known host.
        hostname (Union[Unset, str]): The hostname of the known host.
        public_key (Union[Unset, PipelineSshPublicKey]):
    """

    type: str
    uuid: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    public_key: Union[Unset, PipelineSshPublicKey] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        uuid = self.uuid
        hostname = self.hostname
        public_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_key, Unset):
            public_key = self.public_key.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if public_key is not UNSET:
            field_dict["public_key"] = public_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        hostname = d.pop("hostname", UNSET)

        _public_key = d.pop("public_key", UNSET)
        public_key: Union[Unset, PipelineSshPublicKey]
        if isinstance(_public_key, Unset):
            public_key = UNSET
        else:
            public_key = PipelineSshPublicKey.from_dict(_public_key)

        pipeline_known_host = cls(
            type=type,
            uuid=uuid,
            hostname=hostname,
            public_key=public_key,
        )

        pipeline_known_host.additional_properties = d
        return pipeline_known_host

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
