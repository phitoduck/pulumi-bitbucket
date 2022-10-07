from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.deployment_state_completed_status_stopped_name import DeploymentStateCompletedStatusStoppedName
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentStateCompletedStatusStopped")


@attr.s(auto_attribs=True)
class DeploymentStateCompletedStatusStopped:
    """
    Attributes:
        type (str):
        name (Union[Unset, DeploymentStateCompletedStatusStoppedName]): The name of the completed deployment status
            (STOPPED).
    """

    type: str
    name: Union[Unset, DeploymentStateCompletedStatusStoppedName] = UNSET
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
        name: Union[Unset, DeploymentStateCompletedStatusStoppedName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = DeploymentStateCompletedStatusStoppedName(_name)

        deployment_state_completed_status_stopped = cls(
            type=type,
            name=name,
        )

        deployment_state_completed_status_stopped.additional_properties = d
        return deployment_state_completed_status_stopped

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
