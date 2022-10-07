from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.search_segment import SearchSegment
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchLine")


@attr.s(auto_attribs=True)
class SearchLine:
    """
    Attributes:
        line (Union[Unset, int]):
        segments (Union[Unset, List[SearchSegment]]):
    """

    line: Union[Unset, int] = UNSET
    segments: Union[Unset, List[SearchSegment]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line = self.line
        segments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()

                segments.append(segments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line is not UNSET:
            field_dict["line"] = line
        if segments is not UNSET:
            field_dict["segments"] = segments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line = d.pop("line", UNSET)

        segments = []
        _segments = d.pop("segments", UNSET)
        for segments_item_data in _segments or []:
            segments_item = SearchSegment.from_dict(segments_item_data)

            segments.append(segments_item)

        search_line = cls(
            line=line,
            segments=segments,
        )

        search_line.additional_properties = d
        return search_line

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
