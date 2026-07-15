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

    def generate_response(self, prompt: str) -> str:
        """
        Send a prompt to OpenAI and return the generated response.

        Args:
            prompt:
                The complete prompt to send to the language model.

        Returns:
            The generated response as plain text.
        """
        response = self.client.responses.create(
            model=settings.OPENAI_MODEL,
            input=prompt
        )

        return response.output_text





llm_service = LLMService()