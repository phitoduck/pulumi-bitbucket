import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.pipeline_command import PipelineCommand
from ..models.pipeline_image import PipelineImage
from ..models.pipeline_step_state import PipelineStepState
from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineStep")


@attr.s(auto_attribs=True)
class PipelineStep:
    """
    Attributes:
        type (str):
        uuid (Union[Unset, str]): The UUID identifying the step.
        started_on (Union[Unset, datetime.datetime]): The timestamp when the step execution was started. This is not set
            when the step hasn't executed yet.
        completed_on (Union[Unset, datetime.datetime]): The timestamp when the step execution was completed. This is not
            set if the step is still in progress.
        state (Union[Unset, PipelineStepState]):
        image (Union[Unset, PipelineImage]): The definition of a Docker image that can be used for a Bitbucket Pipelines
            step execution context.
        setup_commands (Union[Unset, List[PipelineCommand]]): The list of commands that are executed as part of the
            setup phase of the build. These commands are executed outside the build container.
        script_commands (Union[Unset, List[PipelineCommand]]): The list of build commands. These commands are executed
            in the build container.
    """

    type: str
    uuid: Union[Unset, str] = UNSET
    started_on: Union[Unset, datetime.datetime] = UNSET
    completed_on: Union[Unset, datetime.datetime] = UNSET
    state: Union[Unset, PipelineStepState] = UNSET
    image: Union[Unset, PipelineImage] = UNSET
    setup_commands: Union[Unset, List[PipelineCommand]] = UNSET
    script_commands: Union[Unset, List[PipelineCommand]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        uuid = self.uuid
        started_on: Union[Unset, str] = UNSET
        if not isinstance(self.started_on, Unset):
            started_on = self.started_on.isoformat()

        completed_on: Union[Unset, str] = UNSET
        if not isinstance(self.completed_on, Unset):
            completed_on = self.completed_on.isoformat()

        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        setup_commands: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.setup_commands, Unset):
            setup_commands = []
            for setup_commands_item_data in self.setup_commands:
                setup_commands_item = setup_commands_item_data.to_dict()

                setup_commands.append(setup_commands_item)

        script_commands: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.script_commands, Unset):
            script_commands = []
            for script_commands_item_data in self.script_commands:
                script_commands_item = script_commands_item_data.to_dict()

                script_commands.append(script_commands_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if started_on is not UNSET:
            field_dict["started_on"] = started_on
        if completed_on is not UNSET:
            field_dict["completed_on"] = completed_on
        if state is not UNSET:
            field_dict["state"] = state
        if image is not UNSET:
            field_dict["image"] = image
        if setup_commands is not UNSET:
            field_dict["setup_commands"] = setup_commands
        if script_commands is not UNSET:
            field_dict["script_commands"] = script_commands

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        _started_on = d.pop("started_on", UNSET)
        started_on: Union[Unset, datetime.datetime]
        if isinstance(_started_on, Unset):
            started_on = UNSET
        else:
            started_on = isoparse(_started_on)

        _completed_on = d.pop("completed_on", UNSET)
        completed_on: Union[Unset, datetime.datetime]
        if isinstance(_completed_on, Unset):
            completed_on = UNSET
        else:
            completed_on = isoparse(_completed_on)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PipelineStepState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PipelineStepState.from_dict(_state)

        _image = d.pop("image", UNSET)
        image: Union[Unset, PipelineImage]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = PipelineImage.from_dict(_image)

        setup_commands = []
        _setup_commands = d.pop("setup_commands", UNSET)
        for setup_commands_item_data in _setup_commands or []:
            setup_commands_item = PipelineCommand.from_dict(setup_commands_item_data)

            setup_commands.append(setup_commands_item)

        script_commands = []
        _script_commands = d.pop("script_commands", UNSET)
        for script_commands_item_data in _script_commands or []:
            script_commands_item = PipelineCommand.from_dict(script_commands_item_data)

            script_commands.append(script_commands_item)

        pipeline_step = cls(
            type=type,
            uuid=uuid,
            started_on=started_on,
            completed_on=completed_on,
            state=state,
            image=image,
            setup_commands=setup_commands,
            script_commands=script_commands,
        )

        pipeline_step.additional_properties = d
        return pipeline_step

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
