from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchingModelSettingsProduction")


@attr.s(auto_attribs=True)
class BranchingModelSettingsProduction:
    """
    Attributes:
        is_valid (Union[Unset, bool]): Indicates if the configured branch is valid, that is, if the configured branch
            actually exists currently. Is always `true` when `use_mainbranch` is `true` (even if the main branch does not
            exist). This field is read-only. This field is ignored when updating/creating settings.
        name (Union[Unset, str]): The configured branch. It must be `null` when `use_mainbranch` is `true`. Otherwise it
            must be a non-empty value. It is possible for the configured branch to not exist (e.g. it was deleted after the
            settings are set). In this case `is_valid` will be `false`. The branch must exist when updating/setting the
            `name` or an error will occur.
        use_mainbranch (Union[Unset, bool]): Indicates if the setting points at an explicit branch (`false`) or tracks
            the main branch (`true`). When `true` the `name` must be `null` or not provided. When `false` the `name` must
            contain a non-empty branch name.
        enabled (Union[Unset, bool]): Indicates if branch is enabled or not.
    """

    is_valid: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    use_mainbranch: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        is_valid = self.is_valid
        name = self.name
        use_mainbranch = self.use_mainbranch
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if is_valid is not UNSET:
            field_dict["is_valid"] = is_valid
        if name is not UNSET:
            field_dict["name"] = name
        if use_mainbranch is not UNSET:
            field_dict["use_mainbranch"] = use_mainbranch
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_valid = d.pop("is_valid", UNSET)

        name = d.pop("name", UNSET)

        use_mainbranch = d.pop("use_mainbranch", UNSET)

        enabled = d.pop("enabled", UNSET)

        branching_model_settings_production = cls(
            is_valid=is_valid,
            name=name,
            use_mainbranch=use_mainbranch,
            enabled=enabled,
        )

        return branching_model_settings_production
