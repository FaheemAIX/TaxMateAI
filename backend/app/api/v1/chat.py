from fastapi import APIRouter, UploadFile
from app.models.chat import ChatRequest

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    return {
        "question": request.question,
        "user_id": request.user_id
    }