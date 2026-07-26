from fastapi import APIRouter

from app.services.faiss_service import faiss_service


router = APIRouter()

@router.get("/documents")
def get_documents():

    documents = faiss_service.get_documents()

    return {
        "documents": documents
    }