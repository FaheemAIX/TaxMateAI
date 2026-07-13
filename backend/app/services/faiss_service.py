"""
FAISS Service

This module manages the FAISS vector index used for semantic search.

Responsibilities:
- Create and manage the FAISS index.
- Store embedding vectors.
- Maintain the mapping between vectors and document chunks.
- Perform similarity search.

Author: Muhammad Faheem Ullah
Project: AI Knowledge Assistant for FBR
"""

# Import FAISS library.
import faiss

# Import NumPy because FAISS works with NumPy arrays.
import numpy as np


class FAISSService:
    """
    Service responsible for storing and searching embedding vectors.

    This service creates a FAISS index and keeps a mapping between
    vector IDs and their corresponding text chunks.
    """

    def __init__(self):
        """
        Initialize the FAISS service.

        Attributes:
            index:
                The FAISS vector index.

            chunks:
                Stores the original text chunk for each vector.
        """

        # Dimension of BAAI/bge-small-en-v1.5 embeddings.
        self.dimension = 384

        # Create an L2 (Euclidean distance) index.
        self.index = faiss.IndexFlatL2(self.dimension)

        # Store original chunks.
        self.chunks: list[str] = []

    def add_embeddings(self, embeddings: list[list[float]],chunks: list[str]) -> None:
       
        """
        Add embeddings and their corresponding text chunks to the FAISS index.

        Args:
            embeddings:
                List of embedding vectors generated from document chunks.

            chunks:
                Original text chunks corresponding to each embedding.

        Returns:
            None
        """

        # Convert Python list to a NumPy array with float32 datatype.
        vectors = np.array(embeddings, dtype=np.float32)

        # Add vectors to the FAISS index.
        self.index.add(vectors)


        # Store the original chunks.
        self.chunks.extend(chunks)

        # DEBUG: Remove after testing.
        print(f"Vectors in FAISS Index: {self.index.ntotal}")

    def search(self, query_embedding: list[float], top_k: int = 3) -> list[str]:
        """
        Search the FAISS index and return the most relevant text chunks.

        Args:
            query_embedding:
                Embedding vector of the user's question.

            top_k:
                Number of similar chunks to retrieve.

        Returns:
            List of retrieved text chunks.
        """

        # Convert the query embedding into a NumPy array.
        query_vector = np.array([query_embedding], dtype=np.float32)

        # Search the FAISS index.
        distances, indices = self.index.search(query_vector, top_k)

        # Collect retrieved chunks.
        retrieved_chunks = []

        for index in indices[0]:

            if index != -1:
                retrieved_chunks.append(
                    self.chunks[index]
                )

        return retrieved_chunks


# Create one shared instance for the application.
faiss_service = FAISSService()