from fastapi import APIRouter, UploadFile
from app.services.upload_service import upload_service

router = APIRouter()

@router.post("/upload")
def upload_document(file: UploadFile):

    saved_path = upload_service.save(file)

    return {
        "message": "File uploaded successfully",
        "saved_path": str(saved_path)
    }