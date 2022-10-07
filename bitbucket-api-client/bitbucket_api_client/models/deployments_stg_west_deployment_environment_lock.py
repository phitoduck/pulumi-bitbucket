from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentsStgWestDeploymentEnvironmentLock")


@attr.s(auto_attribs=True)
class DeploymentsStgWestDeploymentEnvironmentLock:
    """
    Attributes:
        type (str):
        environment_uuid (Union[Unset, str]): The UUID identifying the environment.
    """

    type: str
    environment_uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        environment_uuid = self.environment_uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if environment_uuid is not UNSET:
            field_dict["environmentUuid"] = environment_uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        environment_uuid = d.pop("environmentUuid", UNSET)

        deployments_stg_west_deployment_environment_lock = cls(
            type=type,
            environment_uuid=environment_uuid,
        )

        deployments_stg_west_deployment_environment_lock.additional_properties = d
        return deployments_stg_west_deployment_environment_lock

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
