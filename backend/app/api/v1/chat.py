from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.chat_service import chat_service
from app.schemas.chat import ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    return chat_service.answer_question(
        request.question
    )