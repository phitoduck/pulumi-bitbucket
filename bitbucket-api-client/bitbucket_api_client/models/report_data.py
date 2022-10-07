from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.report_data_type import ReportDataType
from ..models.report_data_value import ReportDataValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportData")


@attr.s(auto_attribs=True)
class ReportData:
    """A key-value element that will be displayed along with the report.

    Attributes:
        type (Union[Unset, ReportDataType]): The type of data contained in the value field. If not provided, then the
            value will be detected as a boolean, number or string.
        title (Union[Unset, str]): A string describing what this data field represents.
        value (Union[Unset, ReportDataValue]): The value of the data element.
    """

    type: Union[Unset, ReportDataType] = UNSET
    title: Union[Unset, str] = UNSET
    value: Union[Unset, ReportDataValue] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        title = self.title
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if title is not UNSET:
            field_dict["title"] = title
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, ReportDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ReportDataType(_type)

        title = d.pop("title", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, ReportDataValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = ReportDataValue.from_dict(_value)

        report_data = cls(
            type=type,
            title=title,
            value=value,
        )

        report_data.additional_properties = d
        return report_data

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
