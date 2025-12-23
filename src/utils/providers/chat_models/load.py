from typing import Any, Literal, Optional

from langchain_dev_utils.chat_models import load_chat_model as _load_chat_model


def load_chat_model(
    model: str,
    *,
    model_provider: Optional[str] = None,
    thinking: Optional[bool] = None,
    reasoning_keep_policy: Optional[Literal["current", "all"]] = None,
    **kwargs: Any,
):
    """Load a chat model.

    A wrapper around langchain_dev_utils.load_chat_model that provides clearer type hints.

    Functionally identical to the original, but with more explicit parameter annotations to reduce the risk of naming or type errors.

    Additional parameters for specific model providers can be added here to avoid subsequent type and parameter issues.

    Args:
        model (str): The name of the model to load
        model_provider (Optional[str], optional): The model provider. Defaults to None.
        thinking (Optional[bool], optional): Whether to enable thinking mode. Defaults to None.
        **kwargs (Any): Additional keyword arguments passed to the chat model

    Returns:
        ChatModel: The loaded chat model instance
    """

    if thinking is not None and (model_provider == "zai" or model.startswith("zai")):
        kwargs["extra_body"] = {
            "thinking": {"type": "enabled" if thinking else "disabled"}
        }
    if reasoning_keep_policy is not None:
        kwargs["reasoning_keep_policy"] = reasoning_keep_policy

    return _load_chat_model(
        model,
        model_provider=model_provider,
        **kwargs,
    )
