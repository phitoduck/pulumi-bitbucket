from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.issue_job_status_status import IssueJobStatusStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueJobStatus")


@attr.s(auto_attribs=True)
class IssueJobStatus:
    """The status of an import or export job

    Attributes:
        type (Union[Unset, str]):
        status (Union[Unset, IssueJobStatusStatus]): The status of the import/export job
        phase (Union[Unset, str]): The phase of the import/export job
        total (Union[Unset, int]): The total number of issues being imported/exported
        count (Union[Unset, int]): The total number of issues already imported/exported
        pct (Union[Unset, float]): The percentage of issues already imported/exported
    """

    type: Union[Unset, str] = UNSET
    status: Union[Unset, IssueJobStatusStatus] = UNSET
    phase: Union[Unset, str] = UNSET
    total: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    pct: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        phase = self.phase
        total = self.total
        count = self.count
        pct = self.pct

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if phase is not UNSET:
            field_dict["phase"] = phase
        if total is not UNSET:
            field_dict["total"] = total
        if count is not UNSET:
            field_dict["count"] = count
        if pct is not UNSET:
            field_dict["pct"] = pct

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, IssueJobStatusStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IssueJobStatusStatus(_status)

        phase = d.pop("phase", UNSET)

        total = d.pop("total", UNSET)

        count = d.pop("count", UNSET)

        pct = d.pop("pct", UNSET)

        issue_job_status = cls(
            type=type,
            status=status,
            phase=phase,
            total=total,
            count=count,
            pct=pct,
        )

        return issue_job_status
