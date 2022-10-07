from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineSshPublicKey")


@attr.s(auto_attribs=True)
class PipelineSshPublicKey:
    """
    Attributes:
        type (str):
        key_type (Union[Unset, str]): The type of the public key.
        key (Union[Unset, str]): The base64 encoded public key.
        md5_fingerprint (Union[Unset, str]): The MD5 fingerprint of the public key.
        sha256_fingerprint (Union[Unset, str]): The SHA-256 fingerprint of the public key.
    """

    type: str
    key_type: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    md5_fingerprint: Union[Unset, str] = UNSET
    sha256_fingerprint: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        key_type = self.key_type
        key = self.key
        md5_fingerprint = self.md5_fingerprint
        sha256_fingerprint = self.sha256_fingerprint

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if key_type is not UNSET:
            field_dict["key_type"] = key_type
        if key is not UNSET:
            field_dict["key"] = key
        if md5_fingerprint is not UNSET:
            field_dict["md5_fingerprint"] = md5_fingerprint
        if sha256_fingerprint is not UNSET:
            field_dict["sha256_fingerprint"] = sha256_fingerprint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        key_type = d.pop("key_type", UNSET)

        key = d.pop("key", UNSET)

        md5_fingerprint = d.pop("md5_fingerprint", UNSET)

        sha256_fingerprint = d.pop("sha256_fingerprint", UNSET)

        pipeline_ssh_public_key = cls(
            type=type,
            key_type=key_type,
            key=key,
            md5_fingerprint=md5_fingerprint,
            sha256_fingerprint=sha256_fingerprint,
        )

        pipeline_ssh_public_key.additional_properties = d
        return pipeline_ssh_public_key

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
