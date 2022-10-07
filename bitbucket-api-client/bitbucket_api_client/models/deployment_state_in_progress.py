import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.account import Account
from ..models.deployment_state_in_progress_name import DeploymentStateInProgressName
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentStateInProgress")


@attr.s(auto_attribs=True)
class DeploymentStateInProgress:
    """
    Attributes:
        type (str):
        name (Union[Unset, DeploymentStateInProgressName]): The name of deployment state (IN_PROGRESS).
        url (Union[Unset, str]): Link to the deployment result.
        deployer (Union[Unset, Account]):
        start_date (Union[Unset, datetime.datetime]): The timestamp when the deployment was started.
    """

    type: str
    name: Union[Unset, DeploymentStateInProgressName] = UNSET
    url: Union[Unset, str] = UNSET
    deployer: Union[Unset, Account] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
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

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

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
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _name = d.pop("name", UNSET)
        name: Union[Unset, DeploymentStateInProgressName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = DeploymentStateInProgressName(_name)

        url = d.pop("url", UNSET)

        _deployer = d.pop("deployer", UNSET)
        deployer: Union[Unset, Account]
        if isinstance(_deployer, Unset):
            deployer = UNSET
        else:
            deployer = Account.from_dict(_deployer)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        deployment_state_in_progress = cls(
            type=type,
            name=name,
            url=url,
            deployer=deployer,
            start_date=start_date,
        )

        deployment_state_in_progress.additional_properties = d
        return deployment_state_in_progress

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
