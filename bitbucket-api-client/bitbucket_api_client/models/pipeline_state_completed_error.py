from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pipeline_error import PipelineError
from ..models.pipeline_state_completed_error_name import PipelineStateCompletedErrorName
from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineStateCompletedError")


@attr.s(auto_attribs=True)
class PipelineStateCompletedError:
    """
    Attributes:
        type (str):
        name (Union[Unset, PipelineStateCompletedErrorName]): The name of the result (ERROR)
        error (Union[Unset, PipelineError]):
    """

    type: str
    name: Union[Unset, PipelineStateCompletedErrorName] = UNSET
    error: Union[Unset, PipelineError] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

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
        if name is not UNSET:
            field_dict["name"] = name
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _name = d.pop("name", UNSET)
        name: Union[Unset, PipelineStateCompletedErrorName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = PipelineStateCompletedErrorName(_name)

        _error = d.pop("error", UNSET)
        error: Union[Unset, PipelineError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = PipelineError.from_dict(_error)

        pipeline_state_completed_error = cls(
            type=type,
            name=name,
            error=error,
        )

        pipeline_state_completed_error.additional_properties = d
        return pipeline_state_completed_error

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
