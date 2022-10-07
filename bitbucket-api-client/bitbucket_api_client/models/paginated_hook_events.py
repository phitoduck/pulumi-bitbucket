from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.hook_event import HookEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginatedHookEvents")


@attr.s(auto_attribs=True)
class PaginatedHookEvents:
    """A paginated list of webhook types available to subscribe on.

    Attributes:
        size (Union[Unset, int]): Total number of objects in the response. This is an optional element that is not
            provided in all responses, as it can be expensive to compute.
        page (Union[Unset, int]): Page number of the current results. This is an optional element that is not provided
            in all responses.
        pagelen (Union[Unset, int]): Current number of objects on the existing page. The default value is 10 with 100
            being the maximum allowed value. Individual APIs may enforce different values.
        next_ (Union[Unset, str]): Link to the next page if it exists. The last page of a collection does not have this
            value. Use this link to navigate the result set and refrain from constructing your own URLs.
        previous (Union[Unset, str]): Link to previous page if it exists. A collections first page does not have this
            value. This is an optional element that is not provided in all responses. Some result sets strictly support
            forward navigation and never provide previous links. Clients must anticipate that backwards navigation is not
            always available. Use this link to navigate the result set and refrain from constructing your own URLs.
        values (Union[Unset, List[HookEvent]]):
    """

    size: Union[Unset, int] = UNSET
    page: Union[Unset, int] = UNSET
    pagelen: Union[Unset, int] = UNSET
    next_: Union[Unset, str] = UNSET
    previous: Union[Unset, str] = UNSET
    values: Union[Unset, List[HookEvent]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        size = self.size
        page = self.page
        pagelen = self.pagelen
        next_ = self.next_
        previous = self.previous
        values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()

                values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if page is not UNSET:
            field_dict["page"] = page
        if pagelen is not UNSET:
            field_dict["pagelen"] = pagelen
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        size = d.pop("size", UNSET)

        page = d.pop("page", UNSET)

        pagelen = d.pop("pagelen", UNSET)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = HookEvent.from_dict(values_item_data)

            values.append(values_item)

        paginated_hook_events = cls(
            size=size,
            page=page,
            pagelen=pagelen,
            next_=next_,
            previous=previous,
            values=values,
        )

        return paginated_hook_events
