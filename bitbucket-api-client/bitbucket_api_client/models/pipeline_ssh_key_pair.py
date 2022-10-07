from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineSshKeyPair")


@attr.s(auto_attribs=True)
class PipelineSshKeyPair:
    """
    Attributes:
        type (str):
        private_key (Union[Unset, str]): The SSH private key. This value will be empty when retrieving the SSH key pair.
        public_key (Union[Unset, str]): The SSH public key.
    """

    type: str
    private_key: Union[Unset, str] = UNSET
    public_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        private_key = self.private_key
        public_key = self.public_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if private_key is not UNSET:
            field_dict["private_key"] = private_key
        if public_key is not UNSET:
            field_dict["public_key"] = public_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        private_key = d.pop("private_key", UNSET)

        public_key = d.pop("public_key", UNSET)

        pipeline_ssh_key_pair = cls(
            type=type,
            private_key=private_key,
            public_key=public_key,
        )

        pipeline_ssh_key_pair.additional_properties = d
        return pipeline_ssh_key_pair

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
