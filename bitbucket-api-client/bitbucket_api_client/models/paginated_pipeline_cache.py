from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pipeline_cache import PipelineCache
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginatedPipelineCache")


@attr.s(auto_attribs=True)
class PaginatedPipelineCache:
    """A paged list of pipeline caches

    Attributes:
        page (Union[Unset, int]): Page number of the current results. This is an optional element that is not provided
            in all responses.
        values (Union[Unset, List[PipelineCache]]): The values of the current page.
        size (Union[Unset, int]): Total number of objects in the response. This is an optional element that is not
            provided in all responses, as it can be expensive to compute.
        pagelen (Union[Unset, int]): Current number of objects on the existing page. The default value is 10 with 100
            being the maximum allowed value. Individual APIs may enforce different values.
        next_ (Union[Unset, str]): Link to the next page if it exists. The last page of a collection does not have this
            value. Use this link to navigate the result set and refrain from constructing your own URLs.
        previous (Union[Unset, str]): Link to previous page if it exists. A collections first page does not have this
            value. This is an optional element that is not provided in all responses. Some result sets strictly support
            forward navigation and never provide previous links. Clients must anticipate that backwards navigation is not
            always available. Use this link to navigate the result set and refrain from constructing your own URLs.
    """

    page: Union[Unset, int] = UNSET
    values: Union[Unset, List[PipelineCache]] = UNSET
    size: Union[Unset, int] = UNSET
    pagelen: Union[Unset, int] = UNSET
    next_: Union[Unset, str] = UNSET
    previous: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page = self.page
        values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()

                values.append(values_item)

        size = self.size
        pagelen = self.pagelen
        next_ = self.next_
        previous = self.previous

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if values is not UNSET:
            field_dict["values"] = values
        if size is not UNSET:
            field_dict["size"] = size
        if pagelen is not UNSET:
            field_dict["pagelen"] = pagelen
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page = d.pop("page", UNSET)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = PipelineCache.from_dict(values_item_data)

            values.append(values_item)

        size = d.pop("size", UNSET)

        pagelen = d.pop("pagelen", UNSET)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        paginated_pipeline_cache = cls(
            page=page,
            values=values,
            size=size,
            pagelen=pagelen,
            next_=next_,
            previous=previous,
        )

        paginated_pipeline_cache.additional_properties = d
        return paginated_pipeline_cache

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
