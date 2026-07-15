from fastapi import APIRouter

from app.models.chat import ChatRequest
from app.services.chat_service import chat_service

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):

    answer = chat_service.answer_question(
        request.question
    )

    return {
        "question": request.question,
        "answer": answer,
        "user_id": request.user_id
    }