"""
Chat Schemas

This module defines the request and response models
used by the chat API.

Responsibilities:
- Represent chat requests.
- Represent AI generated responses.
- Represent source information returned with each answer.

Author: Muhammad Faheem Ullah
Project: AI Knowledge Assistant for FBR
"""

from pydantic import BaseModel

from app.schemas.retrieval import ChunkMetadata


class ChatRequest(BaseModel):
    """
    Request model for a user question.

    Attributes:
        question:
            The question submitted by the user.
    """

    question: str


class ChatResponse(BaseModel):
    """
    Response model returned by the chat service.

    Attributes:
        answer:
            AI generated answer.

        sources:
            Metadata describing the document chunks
            used to generate the answer.
    """

    answer: str
    sources: list[ChunkMetadata]

