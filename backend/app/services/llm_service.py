"""
LLM Service

Responsible for communicating with OpenAI models.
"""

from openai import OpenAI

from app.core.config import settings


class LLMService:
    """
    Service responsible for interacting with OpenAI.
    """

    def __init__(self):
        """
        Initialize the OpenAI client.
        """

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )


llm_service = LLMService()