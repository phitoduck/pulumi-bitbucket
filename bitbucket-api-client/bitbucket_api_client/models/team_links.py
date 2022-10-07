from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.link import Link
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamLinks")


@attr.s(auto_attribs=True)
class TeamLinks:
    """
    Attributes:
        avatar (Union[Unset, Link]): A link to a resource related to this object.
        self_ (Union[Unset, Link]): A link to a resource related to this object.
        html (Union[Unset, Link]): A link to a resource related to this object.
        members (Union[Unset, Link]): A link to a resource related to this object.
        projects (Union[Unset, Link]): A link to a resource related to this object.
        repositories (Union[Unset, Link]): A link to a resource related to this object.
    """

    avatar: Union[Unset, Link] = UNSET
    self_: Union[Unset, Link] = UNSET
    html: Union[Unset, Link] = UNSET
    members: Union[Unset, Link] = UNSET
    projects: Union[Unset, Link] = UNSET
    repositories: Union[Unset, Link] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avatar: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        self_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        html: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.html, Unset):
            html = self.html.to_dict()

        members: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.members, Unset):
            members = self.members.to_dict()

        projects: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects.to_dict()

        repositories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = self.repositories.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if self_ is not UNSET:
            field_dict["self"] = self_
        if html is not UNSET:
            field_dict["html"] = html
        if members is not UNSET:
            field_dict["members"] = members
        if projects is not UNSET:
            field_dict["projects"] = projects
        if repositories is not UNSET:
            field_dict["repositories"] = repositories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, Link]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = Link.from_dict(_avatar)

        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, Link]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = Link.from_dict(_self_)

        _html = d.pop("html", UNSET)
        html: Union[Unset, Link]
        if isinstance(_html, Unset):
            html = UNSET
        else:
            html = Link.from_dict(_html)

        _members = d.pop("members", UNSET)
        members: Union[Unset, Link]
        if isinstance(_members, Unset):
            members = UNSET
        else:
            members = Link.from_dict(_members)

        _projects = d.pop("projects", UNSET)
        projects: Union[Unset, Link]
        if isinstance(_projects, Unset):
            projects = UNSET
        else:
            projects = Link.from_dict(_projects)

        _repositories = d.pop("repositories", UNSET)
        repositories: Union[Unset, Link]
        if isinstance(_repositories, Unset):
            repositories = UNSET
        else:
            repositories = Link.from_dict(_repositories)

        team_links = cls(
            avatar=avatar,
            self_=self_,
            html=html,
            members=members,
            projects=projects,
            repositories=repositories,
        )

        team_links.additional_properties = d
        return team_links

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
