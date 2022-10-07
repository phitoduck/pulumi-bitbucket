import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.account import Account
from ..models.deployment_state_completed_name import DeploymentStateCompletedName
from ..models.deployment_state_completed_status import DeploymentStateCompletedStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentStateCompleted")


@attr.s(auto_attribs=True)
class DeploymentStateCompleted:
    """
    Attributes:
        type (str):
        name (Union[Unset, DeploymentStateCompletedName]): The name of deployment state (COMPLETED).
        url (Union[Unset, str]): Link to the deployment result.
        deployer (Union[Unset, Account]):
        status (Union[Unset, DeploymentStateCompletedStatus]):
        start_date (Union[Unset, datetime.datetime]): The timestamp when the deployment was started.
        completion_date (Union[Unset, datetime.datetime]): The timestamp when the deployment completed.
    """

    type: str
    name: Union[Unset, DeploymentStateCompletedName] = UNSET
    url: Union[Unset, str] = UNSET
    deployer: Union[Unset, Account] = UNSET
    status: Union[Unset, DeploymentStateCompletedStatus] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    completion_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        url = self.url
        deployer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deployer, Unset):
            deployer = self.deployer.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        completion_date: Union[Unset, str] = UNSET
        if not isinstance(self.completion_date, Unset):
            completion_date = self.completion_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if deployer is not UNSET:
            field_dict["deployer"] = deployer
        if status is not UNSET:
            field_dict["status"] = status
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if completion_date is not UNSET:
            field_dict["completion_date"] = completion_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _name = d.pop("name", UNSET)
        name: Union[Unset, DeploymentStateCompletedName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = DeploymentStateCompletedName(_name)

        url = d.pop("url", UNSET)

        _deployer = d.pop("deployer", UNSET)
        deployer: Union[Unset, Account]
        if isinstance(_deployer, Unset):
            deployer = UNSET
        else:
            deployer = Account.from_dict(_deployer)

        _status = d.pop("status", UNSET)
        status: Union[Unset, DeploymentStateCompletedStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DeploymentStateCompletedStatus.from_dict(_status)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _completion_date = d.pop("completion_date", UNSET)
        completion_date: Union[Unset, datetime.datetime]
        if isinstance(_completion_date, Unset):
            completion_date = UNSET
        else:
            completion_date = isoparse(_completion_date)

        deployment_state_completed = cls(
            type=type,
            name=name,
            url=url,
            deployer=deployer,
            status=status,
            start_date=start_date,
            completion_date=completion_date,
        )

        deployment_state_completed.additional_properties = d
        return deployment_state_completed

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
