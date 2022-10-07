from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.error_error_data import ErrorErrorData
from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorError")


@attr.s(auto_attribs=True)
class ErrorError:
    """
    Attributes:
        message (str):
        detail (Union[Unset, str]):
        data (Union[Unset, ErrorErrorData]): Optional structured data that is endpoint-specific.
    """

    message: str
    detail: Union[Unset, str] = UNSET
    data: Union[Unset, ErrorErrorData] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        detail = self.detail
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "message": message,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        detail = d.pop("detail", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ErrorErrorData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ErrorErrorData.from_dict(_data)

        error_error = cls(
            message=message,
            detail=detail,
            data=data,
        )

        return error_error
