"""
Retrieval Schemas

This module defines the data models used to represent
retrieval results returned from the vector store.

Responsibilities:
- Represent chunk metadata.
- Represent a retrieved chunk and its metadata.
- Provide strongly typed objects between the retrieval
  and chat layers.

Author: Muhammad Faheem Ullah
Project: AI Knowledge Assistant for FBR
"""

from pydantic import BaseModel


class ChunkMetadata(BaseModel):
    """
    Metadata associated with a retrieved document chunk.

    Attributes:
        document:
            Name of the source document from which
            the chunk was extracted.

        chunk_id:
            Sequential identifier of the chunk
            within the source document.
    """

    document: str
    chunk_id: int


class RetrievalResult(BaseModel):
    """
    Represents a single retrieval result returned
    by the vector store.

    Each retrieval result contains the retrieved
    document chunk along with its associated metadata.

    Attributes:
        chunk:
            The retrieved text chunk.

        metadata:
            Metadata describing the source of the
            retrieved chunk.
    """

    chunk: str
    metadata: ChunkMetadata