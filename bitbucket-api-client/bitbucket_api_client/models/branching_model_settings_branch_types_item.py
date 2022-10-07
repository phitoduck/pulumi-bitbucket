from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.branching_model_settings_branch_types_item_kind import BranchingModelSettingsBranchTypesItemKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchingModelSettingsBranchTypesItem")


@attr.s(auto_attribs=True)
class BranchingModelSettingsBranchTypesItem:
    """
    Attributes:
        kind (BranchingModelSettingsBranchTypesItemKind): The kind of the branch type.
        enabled (Union[Unset, bool]): Whether the branch type is enabled or not. A disabled branch type may contain an
            invalid `prefix`.
        prefix (Union[Unset, str]): The prefix for this branch type. A branch with this prefix will be classified as per
            `kind`. The `prefix` of an enabled branch type must be a valid branch prefix.Additionally, it cannot be blank,
            empty or `null`. The `prefix` for a disabled branch type can be empty or invalid.
    """

    kind: BranchingModelSettingsBranchTypesItemKind
    enabled: Union[Unset, bool] = UNSET
    prefix: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind.value

        enabled = self.enabled
        prefix = self.prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "kind": kind,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kind = BranchingModelSettingsBranchTypesItemKind(d.pop("kind"))

        enabled = d.pop("enabled", UNSET)

        prefix = d.pop("prefix", UNSET)

        branching_model_settings_branch_types_item = cls(
            kind=kind,
            enabled=enabled,
            prefix=prefix,
        )

        return branching_model_settings_branch_types_item
