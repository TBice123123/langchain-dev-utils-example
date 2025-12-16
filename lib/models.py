from typing import Any, Optional
from langchain_core.language_models import ModelProfile
from langchain_dev_utils.chat_models import load_chat_model as _load_chat_model


def load_chat_model(
    model: str,
    *,
    model_provider: Optional[str] = None,
    temperature: Optional[float] = None,
    max_tokens: Optional[int] = None,
    profile: Optional[ModelProfile] = None,
    **kwargs: Any,
):
    """Load a chat model.

    A wrapper around langchain_dev_utils.load_chat_model that provides clearer type hints.

    Functionally identical to the original, but with more explicit parameter annotations to reduce the risk of naming or type errors.

    Additional parameters for specific model providers can be added here to avoid subsequent type and parameter issues.

    Args:
        model (str): The name of the model to load
        model_provider (Optional[str], optional): The model provider. Defaults to None.
        temperature (Optional[float], optional): Sampling temperature. Defaults to None.
        max_tokens (Optional[int], optional): Maximum number of tokens to generate. Defaults to None.
        profile (Optional[ModelProfile], optional): Override the model profile. Defaults to None.
        **kwargs (Any): Additional keyword arguments passed to the chat model

    Returns:
        ChatModel: The loaded chat model instance
    """
    if temperature is not None:
        kwargs["temperature"] = temperature
    if max_tokens is not None:
        kwargs["max_tokens"] = max_tokens
    if profile is not None:
        kwargs["profile"] = profile

    return _load_chat_model(
        model,
        model_provider=model_provider,
        temperature=temperature,
        **kwargs,
    )
