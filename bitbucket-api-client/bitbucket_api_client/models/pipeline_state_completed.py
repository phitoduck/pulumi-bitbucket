from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pipeline_state_completed_name import PipelineStateCompletedName
from ..models.pipeline_state_completed_result import PipelineStateCompletedResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineStateCompleted")


@attr.s(auto_attribs=True)
class PipelineStateCompleted:
    """
    Attributes:
        type (str):
        name (Union[Unset, PipelineStateCompletedName]): The name of pipeline state (COMPLETED).
        result (Union[Unset, PipelineStateCompletedResult]):
    """

    type: str
    name: Union[Unset, PipelineStateCompletedName] = UNSET
    result: Union[Unset, PipelineStateCompletedResult] = UNSET
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
        name: Union[Unset, PipelineStateCompletedName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = PipelineStateCompletedName(_name)

        _result = d.pop("result", UNSET)
        result: Union[Unset, PipelineStateCompletedResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = PipelineStateCompletedResult.from_dict(_result)

        pipeline_state_completed = cls(
            type=type,
            name=name,
            result=result,
        )

        pipeline_state_completed.additional_properties = d
        return pipeline_state_completed

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
