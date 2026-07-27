"""
Document Service

This module contains the business logic related
to document management.

Responsibilities:
- Retrieve uploaded documents.
- Delete documents.
- Manage document metadata.
- Coordinate document operations.

Author: Muhammad Faheem Ullah
Project: AI Knowledge Assistant for FBR
"""

from app.schemas.document import DocumentInfo
from app.services.faiss_service import faiss_service


class DocumentService:
    """
    Service responsible for document management.
    """

    def get_documents(self) -> list[DocumentInfo]:
        """
        Retrieve all indexed documents.

        Returns:
            List of uploaded documents with
            their chunk counts.
        """

        return faiss_service.get_documents()


document_service = DocumentService()