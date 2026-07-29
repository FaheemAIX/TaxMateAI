"""
Document Router

This module defines the API endpoints for
document management.

Responsibilities:
- Retrieve uploaded documents.
- Delete documents.
- Expose document management operations.

Author: Muhammad Faheem Ullah
Project: AI Knowledge Assistant for FBR
"""
from fastapi import APIRouter

from app.schemas.document import DocumentInfo

from app.services.document_service import document_service

from fastapi import HTTPException


router = APIRouter()

@router.get("/documents", response_model=list[DocumentInfo])
def get_documents():
    """
    Retrieve all uploaded documents.

    Returns:
        List of indexed documents with
        their chunk counts.
    """

    return document_service.get_documents()

@router.delete("/documents/{document_name}")
def delete_document(document_name: str):
    """
    Delete a document from the vector store.

    Returns:
        True:
            If the document was found and deleted.

        False:
            If the document does not exist.
    """
    deleted = document_service.delete_document(document_name)

    if not deleted:

        raise HTTPException(status_code=404,detail="Document not found.")

    return {
    "message": "Document deleted successfully."
    }