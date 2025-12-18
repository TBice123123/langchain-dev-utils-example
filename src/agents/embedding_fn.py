from src.utils.providers import load_embeddings


embeddings = load_embeddings("openrouter:qwen/qwen3-embedding-8b", dimensions=1024)


def embed(texts: list[str]) -> list[list[float]]:
    return embeddings.embed_documents(texts)
