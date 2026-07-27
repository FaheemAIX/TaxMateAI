"""
Document Schemas

This module defines the data models used for
document management operations.

Responsibilities:
- Represent uploaded documents.
- Represent document statistics.
- Transfer document information between the
  service and API layers.

Author: Muhammad Faheem Ullah
Project: AI Knowledge Assistant for FBR
"""

from pydantic import BaseModel


class DocumentInfo(BaseModel):
    """
    Represents an uploaded document stored in
    the vector database.

    Attributes:
        document:
            Name of the uploaded document.

        chunks:
            Total number of indexed chunks
            belonging to the document.
    """

    document: str
    chunks: int