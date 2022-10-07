from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.deployment_state_undeployed_name import DeploymentStateUndeployedName
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentStateUndeployed")


@attr.s(auto_attribs=True)
class DeploymentStateUndeployed:
    """
    Attributes:
        type (str):
        name (Union[Unset, DeploymentStateUndeployedName]): The name of deployment state (UNDEPLOYED).
        trigger_url (Union[Unset, str]): Link to trigger the deployment.
    """

    type: str
    name: Union[Unset, DeploymentStateUndeployedName] = UNSET
    trigger_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        trigger_url = self.trigger_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if trigger_url is not UNSET:
            field_dict["trigger_url"] = trigger_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _name = d.pop("name", UNSET)
        name: Union[Unset, DeploymentStateUndeployedName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = DeploymentStateUndeployedName(_name)

        trigger_url = d.pop("trigger_url", UNSET)

        deployment_state_undeployed = cls(
            type=type,
            name=name,
            trigger_url=trigger_url,
        )

        deployment_state_undeployed.additional_properties = d
        return deployment_state_undeployed

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
