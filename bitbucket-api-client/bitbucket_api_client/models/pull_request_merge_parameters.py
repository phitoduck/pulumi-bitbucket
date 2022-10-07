from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pull_request_merge_parameters_merge_strategy import PullRequestMergeParametersMergeStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="PullRequestMergeParameters")


@attr.s(auto_attribs=True)
class PullRequestMergeParameters:
    """The metadata that describes a pull request merge.

    Attributes:
        type (str):
        message (Union[Unset, str]): The commit message that will be used on the resulting commit.
        close_source_branch (Union[Unset, bool]): Whether the source branch should be deleted. If this is not provided,
            we fallback to the value used when the pull request was created, which defaults to False
        merge_strategy (Union[Unset, PullRequestMergeParametersMergeStrategy]): The merge strategy that will be used to
            merge the pull request. Default: PullRequestMergeParametersMergeStrategy.MERGE_COMMIT.
    """

    type: str
    message: Union[Unset, str] = UNSET
    close_source_branch: Union[Unset, bool] = UNSET
    merge_strategy: Union[
        Unset, PullRequestMergeParametersMergeStrategy
    ] = PullRequestMergeParametersMergeStrategy.MERGE_COMMIT
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        message = self.message
        close_source_branch = self.close_source_branch
        merge_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.merge_strategy, Unset):
            merge_strategy = self.merge_strategy.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if close_source_branch is not UNSET:
            field_dict["close_source_branch"] = close_source_branch
        if merge_strategy is not UNSET:
            field_dict["merge_strategy"] = merge_strategy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        message = d.pop("message", UNSET)

        close_source_branch = d.pop("close_source_branch", UNSET)

        _merge_strategy = d.pop("merge_strategy", UNSET)
        merge_strategy: Union[Unset, PullRequestMergeParametersMergeStrategy]
        if isinstance(_merge_strategy, Unset):
            merge_strategy = UNSET
        else:
            merge_strategy = PullRequestMergeParametersMergeStrategy(_merge_strategy)

        pull_request_merge_parameters = cls(
            type=type,
            message=message,
            close_source_branch=close_source_branch,
            merge_strategy=merge_strategy,
        )

        pull_request_merge_parameters.additional_properties = d
        return pull_request_merge_parameters

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
