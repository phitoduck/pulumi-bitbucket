from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineImage")


@attr.s(auto_attribs=True)
class PipelineImage:
    """The definition of a Docker image that can be used for a Bitbucket Pipelines step execution context.

    Attributes:
        name (Union[Unset, str]): The name of the image. If the image is hosted on DockerHub the short name can be used,
            otherwise the fully qualified name is required here.
        username (Union[Unset, str]): The username needed to authenticate with the Docker registry. Only required when
            using a private Docker image.
        password (Union[Unset, str]): The password needed to authenticate with the Docker registry. Only required when
            using a private Docker image.
        email (Union[Unset, str]): The email needed to authenticate with the Docker registry. Only required when using a
            private Docker image.
    """

    name: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        username = self.username
        password = self.password
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        email = d.pop("email", UNSET)

        pipeline_image = cls(
            name=name,
            username=username,
            password=password,
            email=email,
        )

        pipeline_image.additional_properties = d
        return pipeline_image

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
