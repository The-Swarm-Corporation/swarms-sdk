from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_spec_tools_list_dictionary_type_0_item import AgentSpecToolsListDictionaryType0Item


T = TypeVar("T", bound="AgentSpec")


@_attrs_define
class AgentSpec:
    """
    Attributes:
        agent_name (Union[None, str]): The unique name assigned to the agent, which identifies its role and
            functionality within the swarm.
        description (Union[None, Unset, str]): A detailed explanation of the agent's purpose, capabilities, and any
            specific tasks it is designed to perform.
        system_prompt (Union[None, Unset, str]): The initial instruction or context provided to the agent, guiding its
            behavior and responses during execution.
        model_name (Union[None, Unset, str]): The name of the AI model that the agent will utilize for processing tasks
            and generating outputs. For example: gpt-4o, gpt-4o-mini, openai/o3-mini Default: 'gpt-4o-mini'.
        auto_generate_prompt (Union[None, Unset, bool]): A flag indicating whether the agent should automatically create
            prompts based on the task requirements. Default: False.
        max_tokens (Union[None, Unset, int]): The maximum number of tokens that the agent is allowed to generate in its
            responses, limiting output length. Default: 8192.
        temperature (Union[None, Unset, float]): A parameter that controls the randomness of the agent's output; lower
            values result in more deterministic responses. Default: 0.5.
        role (Union[None, Unset, str]): The designated role of the agent within the swarm, which influences its behavior
            and interaction with other agents. Default: 'worker'.
        max_loops (Union[None, Unset, int]): The maximum number of times the agent is allowed to repeat its task,
            enabling iterative processing if necessary. Default: 1.
        tools_list_dictionary (Union[None, Unset, list['AgentSpecToolsListDictionaryType0Item']]): A dictionary of tools
            that the agent can use to complete its task.
        mcp_url (Union[None, Unset, str]): The URL of the MCP server that the agent can use to complete its task.
        streaming_on (Union[None, Unset, bool]): A flag indicating whether the agent should stream its output. Default:
            False.
    """

    agent_name: Union[None, str]
    description: Union[None, Unset, str] = UNSET
    system_prompt: Union[None, Unset, str] = UNSET
    model_name: Union[None, Unset, str] = "gpt-4o-mini"
    auto_generate_prompt: Union[None, Unset, bool] = False
    max_tokens: Union[None, Unset, int] = 8192
    temperature: Union[None, Unset, float] = 0.5
    role: Union[None, Unset, str] = "worker"
    max_loops: Union[None, Unset, int] = 1
    tools_list_dictionary: Union[None, Unset, list["AgentSpecToolsListDictionaryType0Item"]] = UNSET
    mcp_url: Union[None, Unset, str] = UNSET
    streaming_on: Union[None, Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_name: Union[None, str]
        agent_name = self.agent_name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        system_prompt: Union[None, Unset, str]
        if isinstance(self.system_prompt, Unset):
            system_prompt = UNSET
        else:
            system_prompt = self.system_prompt

        model_name: Union[None, Unset, str]
        if isinstance(self.model_name, Unset):
            model_name = UNSET
        else:
            model_name = self.model_name

        auto_generate_prompt: Union[None, Unset, bool]
        if isinstance(self.auto_generate_prompt, Unset):
            auto_generate_prompt = UNSET
        else:
            auto_generate_prompt = self.auto_generate_prompt

        max_tokens: Union[None, Unset, int]
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        temperature: Union[None, Unset, float]
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        role: Union[None, Unset, str]
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        max_loops: Union[None, Unset, int]
        if isinstance(self.max_loops, Unset):
            max_loops = UNSET
        else:
            max_loops = self.max_loops

        tools_list_dictionary: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.tools_list_dictionary, Unset):
            tools_list_dictionary = UNSET
        elif isinstance(self.tools_list_dictionary, list):
            tools_list_dictionary = []
            for tools_list_dictionary_type_0_item_data in self.tools_list_dictionary:
                tools_list_dictionary_type_0_item = tools_list_dictionary_type_0_item_data.to_dict()
                tools_list_dictionary.append(tools_list_dictionary_type_0_item)

        else:
            tools_list_dictionary = self.tools_list_dictionary

        mcp_url: Union[None, Unset, str]
        if isinstance(self.mcp_url, Unset):
            mcp_url = UNSET
        else:
            mcp_url = self.mcp_url

        streaming_on: Union[None, Unset, bool]
        if isinstance(self.streaming_on, Unset):
            streaming_on = UNSET
        else:
            streaming_on = self.streaming_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_name": agent_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if auto_generate_prompt is not UNSET:
            field_dict["auto_generate_prompt"] = auto_generate_prompt
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if role is not UNSET:
            field_dict["role"] = role
        if max_loops is not UNSET:
            field_dict["max_loops"] = max_loops
        if tools_list_dictionary is not UNSET:
            field_dict["tools_list_dictionary"] = tools_list_dictionary
        if mcp_url is not UNSET:
            field_dict["mcp_url"] = mcp_url
        if streaming_on is not UNSET:
            field_dict["streaming_on"] = streaming_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_spec_tools_list_dictionary_type_0_item import AgentSpecToolsListDictionaryType0Item

        d = dict(src_dict)

        def _parse_agent_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        agent_name = _parse_agent_name(d.pop("agent_name"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_system_prompt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        system_prompt = _parse_system_prompt(d.pop("system_prompt", UNSET))

        def _parse_model_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_name = _parse_model_name(d.pop("model_name", UNSET))

        def _parse_auto_generate_prompt(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        auto_generate_prompt = _parse_auto_generate_prompt(d.pop("auto_generate_prompt", UNSET))

        def _parse_max_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_tokens = _parse_max_tokens(d.pop("max_tokens", UNSET))

        def _parse_temperature(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_max_loops(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_loops = _parse_max_loops(d.pop("max_loops", UNSET))

        def _parse_tools_list_dictionary(
            data: object,
        ) -> Union[None, Unset, list["AgentSpecToolsListDictionaryType0Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tools_list_dictionary_type_0 = []
                _tools_list_dictionary_type_0 = data
                for tools_list_dictionary_type_0_item_data in _tools_list_dictionary_type_0:
                    tools_list_dictionary_type_0_item = AgentSpecToolsListDictionaryType0Item.from_dict(
                        tools_list_dictionary_type_0_item_data
                    )

                    tools_list_dictionary_type_0.append(tools_list_dictionary_type_0_item)

                return tools_list_dictionary_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AgentSpecToolsListDictionaryType0Item"]], data)

        tools_list_dictionary = _parse_tools_list_dictionary(d.pop("tools_list_dictionary", UNSET))

        def _parse_mcp_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mcp_url = _parse_mcp_url(d.pop("mcp_url", UNSET))

        def _parse_streaming_on(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        streaming_on = _parse_streaming_on(d.pop("streaming_on", UNSET))

        agent_spec = cls(
            agent_name=agent_name,
            description=description,
            system_prompt=system_prompt,
            model_name=model_name,
            auto_generate_prompt=auto_generate_prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            role=role,
            max_loops=max_loops,
            tools_list_dictionary=tools_list_dictionary,
            mcp_url=mcp_url,
            streaming_on=streaming_on,
        )

        agent_spec.additional_properties = d
        return agent_spec

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
