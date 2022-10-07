from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pipeline_step_state_completed_name import PipelineStepStateCompletedName
from ..models.pipeline_step_state_completed_result import PipelineStepStateCompletedResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineStepStateCompleted")


@attr.s(auto_attribs=True)
class PipelineStepStateCompleted:
    """
    Attributes:
        type (str):
        name (Union[Unset, PipelineStepStateCompletedName]): The name of pipeline step state (COMPLETED).
        result (Union[Unset, PipelineStepStateCompletedResult]):
    """

    type: str
    name: Union[Unset, PipelineStepStateCompletedName] = UNSET
    result: Union[Unset, PipelineStepStateCompletedResult] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _name = d.pop("name", UNSET)
        name: Union[Unset, PipelineStepStateCompletedName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = PipelineStepStateCompletedName(_name)

        _result = d.pop("result", UNSET)
        result: Union[Unset, PipelineStepStateCompletedResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = PipelineStepStateCompletedResult.from_dict(_result)

        pipeline_step_state_completed = cls(
            type=type,
            name=name,
            result=result,
        )

        pipeline_step_state_completed.additional_properties = d
        return pipeline_step_state_completed

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
