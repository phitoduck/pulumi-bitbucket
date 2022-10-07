import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.account import Account
from ..models.participant_role import ParticipantRole
from ..models.participant_state import ParticipantState
from ..types import UNSET, Unset

T = TypeVar("T", bound="Participant")


@attr.s(auto_attribs=True)
class Participant:
    """
    Attributes:
        type (str):
        user (Union[Unset, Account]):
        role (Union[Unset, ParticipantRole]):
        approved (Union[Unset, bool]):
        state (Union[Unset, None, ParticipantState]):
        participated_on (Union[Unset, datetime.datetime]): The ISO8601 timestamp of the participant's action. For
            approvers, this is the time of their approval. For commenters and pull request reviewers who are not approvers,
            this is the time they last commented, or null if they have not commented.
    """

    type: str
    user: Union[Unset, Account] = UNSET
    role: Union[Unset, ParticipantRole] = UNSET
    approved: Union[Unset, bool] = UNSET
    state: Union[Unset, None, ParticipantState] = UNSET
    participated_on: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        approved = self.approved
        state: Union[Unset, None, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value if self.state else None

        participated_on: Union[Unset, str] = UNSET
        if not isinstance(self.participated_on, Unset):
            participated_on = self.participated_on.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if role is not UNSET:
            field_dict["role"] = role
        if approved is not UNSET:
            field_dict["approved"] = approved
        if state is not UNSET:
            field_dict["state"] = state
        if participated_on is not UNSET:
            field_dict["participated_on"] = participated_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        _user = d.pop("user", UNSET)
        user: Union[Unset, Account]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = Account.from_dict(_user)

        _role = d.pop("role", UNSET)
        role: Union[Unset, ParticipantRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ParticipantRole(_role)

        approved = d.pop("approved", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, None, ParticipantState]
        if _state is None:
            state = None
        elif isinstance(_state, Unset):
            state = UNSET
        else:
            state = ParticipantState(_state)

        _participated_on = d.pop("participated_on", UNSET)
        participated_on: Union[Unset, datetime.datetime]
        if isinstance(_participated_on, Unset):
            participated_on = UNSET
        else:
            participated_on = isoparse(_participated_on)

        participant = cls(
            type=type,
            user=user,
            role=role,
            approved=approved,
            state=state,
            participated_on=participated_on,
        )

        participant.additional_properties = d
        return participant

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
