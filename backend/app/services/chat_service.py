# import the embedding service
from app.services.embedding_service import embedding_service

# import the faiss service
from app.services.faiss_service import faiss_service

# import the prompt
from app.prompts.rag_prompt import RAG_PROMPT

# import the LLM service
from app.services.llm_service import llm_service

class ChatService:


    def retrieve_context(self, query: str, top_k: int = 3) -> list[str]:
        """
        Retrieve the most relevant document chunks for a user's query.

        This method generates an embedding for the user's question,
        searches the FAISS index, and returns the top matching chunks.

        Args:
            query:
                User's question.

            top_k:
                Number of relevant chunks to retrieve.

        Returns:
            List of relevant document chunks.
        """

        # Generate embedding for the user's question.
        query_embedding = embedding_service.embed_query(query)

        # Search the FAISS index.
        retrieved_chunks = faiss_service.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        return retrieved_chunks

    def answer_question(self, query: str) -> str:
        """
        Retrieve relevant context and generate an answer.

        Args:
            query:
                User's question.

        Returns:
            AI generated answer.
        """

        retrieved_chunks = self.retrieve_context(query)

        context = "\n\n".join(retrieved_chunks)

        prompt = RAG_PROMPT.format(
            context=context,
            question=query
        )

        response = llm_service.generate_response(prompt)

        print("\n========== RETRIEVED CHUNKS ==========\n")

        for i, chunk in enumerate(retrieved_chunks, start=1):
            print(f"Chunk {i}")
            print("-" * 40)
            print(chunk)
            print()

        print("\n========== AI RESPONSE ==========\n")
        print(response)

        return response
    
chat_service = ChatService()