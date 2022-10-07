from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pipeline_step_state_ready_name import PipelineStepStateReadyName
from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineStepStateReady")


@attr.s(auto_attribs=True)
class PipelineStepStateReady:
    """
    Attributes:
        type (str):
        name (Union[Unset, PipelineStepStateReadyName]): The name of pipeline step state (READY).
    """

    type: str
    name: Union[Unset, PipelineStepStateReadyName] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _name = d.pop("name", UNSET)
        name: Union[Unset, PipelineStepStateReadyName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = PipelineStepStateReadyName(_name)

        pipeline_step_state_ready = cls(
            type=type,
            name=name,
        )

        pipeline_step_state_ready.additional_properties = d
        return pipeline_step_state_ready

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
