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


router = APIRouter()

@router.get(
    "/documents",
    response_model=list[DocumentInfo]
)
def get_documents():
    """
    Retrieve all uploaded documents.

    Returns:
        List of indexed documents with
        their chunk counts.
    """

    return document_service.get_documents()