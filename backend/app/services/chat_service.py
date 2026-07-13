# import the embedding service
from app.services.embedding_service import embedding_service

# import the faiss service
from app.services.faiss_service import faiss_service




def retrieve_context(
    self,
    query: str,
    top_k: int = 3
) -> list[str]:
    """
    Retrieve the most relevant document chunks for a user's query.

    This method generates an embedding for the user's question,
    searches the FAISS index, and returns the top matching chunks.

    Args:
        query:
            User's question.

        top_k:
            Number of relevant chunks to retrieve.

    Returns:
        List of relevant document chunks.
    """

    # Generate embedding for the user's question.
    query_embedding = embedding_service.embed_query(query)

    # Search the FAISS index.
    retrieved_chunks = faiss_service.search(
        query_embedding=query_embedding,
        top_k=top_k
    )

    return retrieved_chunks