from typing import Any, Optional
from langchain_dev_utils.embeddings import load_embeddings as _load_embeddings


def load_embeddings(
    model: str,
    *,
    provider: Optional[str] = None,
    dimensions: Optional[int] = None,
    **kwargs: Any,
):
    """Load an embeddings model.

    A wrapper around langchain_dev_utils.load_embeddings that provides clearer type hints.

    Functionally identical to the original, but with more explicit parameter annotations to reduce the risk of naming or type errors.

    Additional parameters for specific embeddings providers can be added here to avoid subsequent type and parameter issues.

    Args:
        model (str): The name of the embeddings model to load
        provider (Optional[str], optional): The embeddings provider. Defaults to None.
        dimensions (Optional[int], optional): The number of dimensions. Defaults to None.
        **kwargs (Any): Additional keyword arguments passed to the embeddings model

    Returns:
        Embeddings: The loaded embeddings instance
    """
    if dimensions is not None:
        kwargs["dimensions"] = dimensions

    return _load_embeddings(
        model,
        provider=provider,
        **kwargs,
    )
