from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_completion_history_type_0 import AgentCompletionHistoryType0
    from ..models.agent_completion_history_type_1_item import AgentCompletionHistoryType1Item
    from ..models.agent_spec import AgentSpec


T = TypeVar("T", bound="AgentCompletion")


@_attrs_define
class AgentCompletion:
    """
    Attributes:
        agent_config (Union['AgentSpec', None, Unset]): The configuration of the agent to be completed.
        task (Union[None, Unset, str]): The task to be completed by the agent.
        history (Union['AgentCompletionHistoryType0', None, Unset, list['AgentCompletionHistoryType1Item']]): The
            history of the agent's previous tasks and responses. Can be either a dictionary or a list of message objects.
        img (Union[None, Unset, str]): An optional image URL that may be associated with the agent's task or
            representation.
        imgs (Union[None, Unset, list[str]]): A list of image URLs that may be associated with the agent's task or
            representation.
    """

    agent_config: Union["AgentSpec", None, Unset] = UNSET
    task: Union[None, Unset, str] = UNSET
    history: Union["AgentCompletionHistoryType0", None, Unset, list["AgentCompletionHistoryType1Item"]] = UNSET
    img: Union[None, Unset, str] = UNSET
    imgs: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_completion_history_type_0 import AgentCompletionHistoryType0
        from ..models.agent_spec import AgentSpec

        agent_config: Union[None, Unset, dict[str, Any]]
        if isinstance(self.agent_config, Unset):
            agent_config = UNSET
        elif isinstance(self.agent_config, AgentSpec):
            agent_config = self.agent_config.to_dict()
        else:
            agent_config = self.agent_config

        task: Union[None, Unset, str]
        if isinstance(self.task, Unset):
            task = UNSET
        else:
            task = self.task

        history: Union[None, Unset, dict[str, Any], list[dict[str, Any]]]
        if isinstance(self.history, Unset):
            history = UNSET
        elif isinstance(self.history, AgentCompletionHistoryType0):
            history = self.history.to_dict()
        elif isinstance(self.history, list):
            history = []
            for history_type_1_item_data in self.history:
                history_type_1_item = history_type_1_item_data.to_dict()
                history.append(history_type_1_item)

        else:
            history = self.history

        img: Union[None, Unset, str]
        if isinstance(self.img, Unset):
            img = UNSET
        else:
            img = self.img

        imgs: Union[None, Unset, list[str]]
        if isinstance(self.imgs, Unset):
            imgs = UNSET
        elif isinstance(self.imgs, list):
            imgs = self.imgs

        else:
            imgs = self.imgs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_config is not UNSET:
            field_dict["agent_config"] = agent_config
        if task is not UNSET:
            field_dict["task"] = task
        if history is not UNSET:
            field_dict["history"] = history
        if img is not UNSET:
            field_dict["img"] = img
        if imgs is not UNSET:
            field_dict["imgs"] = imgs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_completion_history_type_0 import AgentCompletionHistoryType0
        from ..models.agent_completion_history_type_1_item import AgentCompletionHistoryType1Item
        from ..models.agent_spec import AgentSpec

        d = dict(src_dict)

        def _parse_agent_config(data: object) -> Union["AgentSpec", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                agent_config_type_0 = AgentSpec.from_dict(data)

                return agent_config_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AgentSpec", None, Unset], data)

        agent_config = _parse_agent_config(d.pop("agent_config", UNSET))

        def _parse_task(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        task = _parse_task(d.pop("task", UNSET))

        def _parse_history(
            data: object,
        ) -> Union["AgentCompletionHistoryType0", None, Unset, list["AgentCompletionHistoryType1Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                history_type_0 = AgentCompletionHistoryType0.from_dict(data)

                return history_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                history_type_1 = []
                _history_type_1 = data
                for history_type_1_item_data in _history_type_1:
                    history_type_1_item = AgentCompletionHistoryType1Item.from_dict(history_type_1_item_data)

                    history_type_1.append(history_type_1_item)

                return history_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union["AgentCompletionHistoryType0", None, Unset, list["AgentCompletionHistoryType1Item"]], data
            )

        history = _parse_history(d.pop("history", UNSET))

        def _parse_img(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        img = _parse_img(d.pop("img", UNSET))

        def _parse_imgs(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                imgs_type_0 = cast(list[str], data)

                return imgs_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        imgs = _parse_imgs(d.pop("imgs", UNSET))

        agent_completion = cls(
            agent_config=agent_config,
            task=task,
            history=history,
            img=img,
            imgs=imgs,
        )

        agent_completion.additional_properties = d
        return agent_completion

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
