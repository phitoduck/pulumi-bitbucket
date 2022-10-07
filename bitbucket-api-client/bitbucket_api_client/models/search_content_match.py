from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.search_line import SearchLine
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchContentMatch")


@attr.s(auto_attribs=True)
class SearchContentMatch:
    """
    Attributes:
        lines (Union[Unset, List[SearchLine]]):
    """

    lines: Union[Unset, List[SearchLine]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()

                lines.append(lines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = SearchLine.from_dict(lines_item_data)

            lines.append(lines_item)

        search_content_match = cls(
            lines=lines,
        )

        search_content_match.additional_properties = d
        return search_content_match

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
