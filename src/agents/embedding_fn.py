from src.utils.providers import load_embeddings


embeddings = load_embeddings("zai:embedding-3", dimensions=1024)


def embed(texts: list[str]) -> list[list[float]]:
    return embeddings.embed_documents(texts)
