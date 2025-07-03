from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.swarm_spec_swarm_type_type_0 import SwarmSpecSwarmTypeType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_spec import AgentSpec
    from ..models.swarm_spec_messages_type_0_item import SwarmSpecMessagesType0Item
    from ..models.swarm_spec_messages_type_1 import SwarmSpecMessagesType1


T = TypeVar("T", bound="SwarmSpec")


@_attrs_define
class SwarmSpec:
    """
    Attributes:
        name (Union[None, Unset, str]): The name of the swarm, which serves as an identifier for the group of agents and
            their collective task.
        description (Union[None, Unset, str]): A comprehensive description of the swarm's objectives, capabilities, and
            intended outcomes.
        agents (Union[None, Unset, list['AgentSpec']]): A list of agents or specifications that define the agents
            participating in the swarm.
        max_loops (Union[None, Unset, int]): The maximum number of execution loops allowed for the swarm, enabling
            repeated processing if needed. Default: 1.
        swarm_type (Union[None, SwarmSpecSwarmTypeType0, Unset]): The classification of the swarm, indicating its
            operational style and methodology.
        rearrange_flow (Union[None, Unset, str]): Instructions on how to rearrange the flow of tasks among agents, if
            applicable.
        task (Union[None, Unset, str]): The specific task or objective that the swarm is designed to accomplish.
        img (Union[None, Unset, str]): An optional image URL that may be associated with the swarm's task or
            representation.
        return_history (Union[None, Unset, bool]): A flag indicating whether the swarm should return its execution
            history along with the final output. Default: True.
        rules (Union[None, Unset, str]): Guidelines or constraints that govern the behavior and interactions of the
            agents within the swarm.
        tasks (Union[None, Unset, list[str]]): A list of tasks that the swarm should complete.
        messages (Union['SwarmSpecMessagesType1', None, Unset, list['SwarmSpecMessagesType0Item']]): A list of messages
            that the swarm should complete.
        stream (Union[None, Unset, bool]): A flag indicating whether the swarm should stream its output. Default: False.
        service_tier (Union[None, Unset, str]): The service tier to use for processing. Options: 'standard' (default) or
            'flex' for lower cost but slower processing. Default: 'standard'.
    """

    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    agents: Union[None, Unset, list["AgentSpec"]] = UNSET
    max_loops: Union[None, Unset, int] = 1
    swarm_type: Union[None, SwarmSpecSwarmTypeType0, Unset] = UNSET
    rearrange_flow: Union[None, Unset, str] = UNSET
    task: Union[None, Unset, str] = UNSET
    img: Union[None, Unset, str] = UNSET
    return_history: Union[None, Unset, bool] = True
    rules: Union[None, Unset, str] = UNSET
    tasks: Union[None, Unset, list[str]] = UNSET
    messages: Union["SwarmSpecMessagesType1", None, Unset, list["SwarmSpecMessagesType0Item"]] = UNSET
    stream: Union[None, Unset, bool] = False
    service_tier: Union[None, Unset, str] = "standard"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.swarm_spec_messages_type_1 import SwarmSpecMessagesType1

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        agents: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.agents, Unset):
            agents = UNSET
        elif isinstance(self.agents, list):
            agents = []
            for agents_type_0_item_data in self.agents:
                agents_type_0_item = agents_type_0_item_data.to_dict()
                agents.append(agents_type_0_item)

        else:
            agents = self.agents

        max_loops: Union[None, Unset, int]
        if isinstance(self.max_loops, Unset):
            max_loops = UNSET
        else:
            max_loops = self.max_loops

        swarm_type: Union[None, Unset, str]
        if isinstance(self.swarm_type, Unset):
            swarm_type = UNSET
        elif isinstance(self.swarm_type, SwarmSpecSwarmTypeType0):
            swarm_type = self.swarm_type.value
        else:
            swarm_type = self.swarm_type

        rearrange_flow: Union[None, Unset, str]
        if isinstance(self.rearrange_flow, Unset):
            rearrange_flow = UNSET
        else:
            rearrange_flow = self.rearrange_flow

        task: Union[None, Unset, str]
        if isinstance(self.task, Unset):
            task = UNSET
        else:
            task = self.task

        img: Union[None, Unset, str]
        if isinstance(self.img, Unset):
            img = UNSET
        else:
            img = self.img

        return_history: Union[None, Unset, bool]
        if isinstance(self.return_history, Unset):
            return_history = UNSET
        else:
            return_history = self.return_history

        rules: Union[None, Unset, str]
        if isinstance(self.rules, Unset):
            rules = UNSET
        else:
            rules = self.rules

        tasks: Union[None, Unset, list[str]]
        if isinstance(self.tasks, Unset):
            tasks = UNSET
        elif isinstance(self.tasks, list):
            tasks = self.tasks

        else:
            tasks = self.tasks

        messages: Union[None, Unset, dict[str, Any], list[dict[str, Any]]]
        if isinstance(self.messages, Unset):
            messages = UNSET
        elif isinstance(self.messages, list):
            messages = []
            for messages_type_0_item_data in self.messages:
                messages_type_0_item = messages_type_0_item_data.to_dict()
                messages.append(messages_type_0_item)

        elif isinstance(self.messages, SwarmSpecMessagesType1):
            messages = self.messages.to_dict()
        else:
            messages = self.messages

        stream: Union[None, Unset, bool]
        if isinstance(self.stream, Unset):
            stream = UNSET
        else:
            stream = self.stream

        service_tier: Union[None, Unset, str]
        if isinstance(self.service_tier, Unset):
            service_tier = UNSET
        else:
            service_tier = self.service_tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if agents is not UNSET:
            field_dict["agents"] = agents
        if max_loops is not UNSET:
            field_dict["max_loops"] = max_loops
        if swarm_type is not UNSET:
            field_dict["swarm_type"] = swarm_type
        if rearrange_flow is not UNSET:
            field_dict["rearrange_flow"] = rearrange_flow
        if task is not UNSET:
            field_dict["task"] = task
        if img is not UNSET:
            field_dict["img"] = img
        if return_history is not UNSET:
            field_dict["return_history"] = return_history
        if rules is not UNSET:
            field_dict["rules"] = rules
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if messages is not UNSET:
            field_dict["messages"] = messages
        if stream is not UNSET:
            field_dict["stream"] = stream
        if service_tier is not UNSET:
            field_dict["service_tier"] = service_tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_spec import AgentSpec
        from ..models.swarm_spec_messages_type_0_item import SwarmSpecMessagesType0Item
        from ..models.swarm_spec_messages_type_1 import SwarmSpecMessagesType1

        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_agents(data: object) -> Union[None, Unset, list["AgentSpec"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                agents_type_0 = []
                _agents_type_0 = data
                for agents_type_0_item_data in _agents_type_0:
                    agents_type_0_item = AgentSpec.from_dict(agents_type_0_item_data)

                    agents_type_0.append(agents_type_0_item)

                return agents_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AgentSpec"]], data)

        agents = _parse_agents(d.pop("agents", UNSET))

        def _parse_max_loops(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_loops = _parse_max_loops(d.pop("max_loops", UNSET))

        def _parse_swarm_type(data: object) -> Union[None, SwarmSpecSwarmTypeType0, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                swarm_type_type_0 = SwarmSpecSwarmTypeType0(data)

                return swarm_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, SwarmSpecSwarmTypeType0, Unset], data)

        swarm_type = _parse_swarm_type(d.pop("swarm_type", UNSET))

        def _parse_rearrange_flow(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rearrange_flow = _parse_rearrange_flow(d.pop("rearrange_flow", UNSET))

        def _parse_task(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        task = _parse_task(d.pop("task", UNSET))

        def _parse_img(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        img = _parse_img(d.pop("img", UNSET))

        def _parse_return_history(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        return_history = _parse_return_history(d.pop("return_history", UNSET))

        def _parse_rules(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rules = _parse_rules(d.pop("rules", UNSET))

        def _parse_tasks(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tasks_type_0 = cast(list[str], data)

                return tasks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tasks = _parse_tasks(d.pop("tasks", UNSET))

        def _parse_messages(
            data: object,
        ) -> Union["SwarmSpecMessagesType1", None, Unset, list["SwarmSpecMessagesType0Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                messages_type_0 = []
                _messages_type_0 = data
                for messages_type_0_item_data in _messages_type_0:
                    messages_type_0_item = SwarmSpecMessagesType0Item.from_dict(messages_type_0_item_data)

                    messages_type_0.append(messages_type_0_item)

                return messages_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                messages_type_1 = SwarmSpecMessagesType1.from_dict(data)

                return messages_type_1
            except:  # noqa: E722
                pass
            return cast(Union["SwarmSpecMessagesType1", None, Unset, list["SwarmSpecMessagesType0Item"]], data)

        messages = _parse_messages(d.pop("messages", UNSET))

        def _parse_stream(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        stream = _parse_stream(d.pop("stream", UNSET))

        def _parse_service_tier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_tier = _parse_service_tier(d.pop("service_tier", UNSET))

        swarm_spec = cls(
            name=name,
            description=description,
            agents=agents,
            max_loops=max_loops,
            swarm_type=swarm_type,
            rearrange_flow=rearrange_flow,
            task=task,
            img=img,
            return_history=return_history,
            rules=rules,
            tasks=tasks,
            messages=messages,
            stream=stream,
            service_tier=service_tier,
        )

        swarm_spec.additional_properties = d
        return swarm_spec

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
