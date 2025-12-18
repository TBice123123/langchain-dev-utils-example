from .load import load_embeddings
from .register import register_all_embeddings_providers

register_all_embeddings_providers()

__all__ = ["load_embeddings"]
