from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pipeline_state_in_progress_name import PipelineStateInProgressName
from ..models.pipeline_state_in_progress_stage import PipelineStateInProgressStage
from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineStateInProgress")


@attr.s(auto_attribs=True)
class PipelineStateInProgress:
    """
    Attributes:
        type (str):
        name (Union[Unset, PipelineStateInProgressName]): The name of pipeline state (IN_PROGRESS).
        stage (Union[Unset, PipelineStateInProgressStage]):
    """

    type: str
    name: Union[Unset, PipelineStateInProgressName] = UNSET
    stage: Union[Unset, PipelineStateInProgressStage] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        stage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stage, Unset):
            stage = self.stage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if stage is not UNSET:
            field_dict["stage"] = stage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _name = d.pop("name", UNSET)
        name: Union[Unset, PipelineStateInProgressName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = PipelineStateInProgressName(_name)

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, PipelineStateInProgressStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = PipelineStateInProgressStage.from_dict(_stage)

        pipeline_state_in_progress = cls(
            type=type,
            name=name,
            stage=stage,
        )

        pipeline_state_in_progress.additional_properties = d
        return pipeline_state_in_progress

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
