from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.error_error import ErrorError
from ..types import UNSET, Unset

T = TypeVar("T", bound="Error")


@attr.s(auto_attribs=True)
class Error:
    """Base type for most resource objects. It defines the common `type` element that identifies an object's type. It also
    identifies the element as Swagger's `discriminator`.

        Attributes:
            type (str):
            error (Union[Unset, ErrorError]):
    """

    type: str
    error: Union[Unset, ErrorError] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _error = d.pop("error", UNSET)
        error: Union[Unset, ErrorError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ErrorError.from_dict(_error)

        error = cls(
            type=type,
            error=error,
        )

        error.additional_properties = d
        return error

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
