from langchain_dev_utils.embeddings import register_embeddings_provider


def register_all_embeddings_providers():
    register_embeddings_provider(
        provider_name="openrouter",
        embeddings_model="openai-compatible",
    )
