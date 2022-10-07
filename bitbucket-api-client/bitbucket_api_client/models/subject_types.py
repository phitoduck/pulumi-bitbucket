from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.subject_types_repository import SubjectTypesRepository
from ..models.subject_types_workspace import SubjectTypesWorkspace
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubjectTypes")


@attr.s(auto_attribs=True)
class SubjectTypes:
    """The mapping of resource/subject types pointing to their individual event types.

    Attributes:
        repository (Union[Unset, SubjectTypesRepository]):
        workspace (Union[Unset, SubjectTypesWorkspace]):
    """

    repository: Union[Unset, SubjectTypesRepository] = UNSET
    workspace: Union[Unset, SubjectTypesWorkspace] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        repository: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        workspace: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workspace, Unset):
            workspace = self.workspace.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if repository is not UNSET:
            field_dict["repository"] = repository
        if workspace is not UNSET:
            field_dict["workspace"] = workspace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _repository = d.pop("repository", UNSET)
        repository: Union[Unset, SubjectTypesRepository]
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = SubjectTypesRepository.from_dict(_repository)

        _workspace = d.pop("workspace", UNSET)
        workspace: Union[Unset, SubjectTypesWorkspace]
        if isinstance(_workspace, Unset):
            workspace = UNSET
        else:
            workspace = SubjectTypesWorkspace.from_dict(_workspace)

        subject_types = cls(
            repository=repository,
            workspace=workspace,
        )

        return subject_types
