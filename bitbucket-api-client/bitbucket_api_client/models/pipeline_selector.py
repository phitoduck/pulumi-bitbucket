from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pipeline_selector_type import PipelineSelectorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineSelector")


@attr.s(auto_attribs=True)
class PipelineSelector:
    """
    Attributes:
        type (PipelineSelectorType): The type of selector.
        pattern (Union[Unset, str]): The name of the matching pipeline definition.
    """

    type: PipelineSelectorType
    pattern: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        pattern = self.pattern

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if pattern is not UNSET:
            field_dict["pattern"] = pattern

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PipelineSelectorType(d.pop("type"))

        pattern = d.pop("pattern", UNSET)

        pipeline_selector = cls(
            type=type,
            pattern=pattern,
        )

        pipeline_selector.additional_properties = d
        return pipeline_selector

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
