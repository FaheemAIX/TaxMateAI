# Import SentenceTransformer to generate embeddings.
from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """Generate embeddings from text."""

    def __init__(self):
        # Load the embedding model once.
        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    def embed_chunks(self, chunks: list[str]) -> list[list[float]]:
        """Convert text chunks into embeddings."""

        # Generate embeddings.
        embeddings = self.model.encode(chunks)

        # Convert NumPy array to normal Python list.
        return embeddings.tolist()
    
    def embed_query(self, query: str) -> list[float]:
        """
        Generate an embedding vector for a user's query.

        Args:
            query:
                The user's question in plain text.

        Returns:
            A single embedding vector representing the semantic meaning
            of the query.
        """

        # Generate embedding for the query.
        embedding = self.model.encode(query)

        # Convert NumPy array to Python list.
        return embedding.tolist()


# Create one object for the whole project.
embedding_service = EmbeddingService()