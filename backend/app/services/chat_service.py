# import the embedding service
from app.services.embedding_service import embedding_service

# import the faiss service
from app.services.faiss_service import faiss_service

# import the prompt
from app.prompts.rag_prompt import RAG_PROMPT

# import the LLM service
from app.services.llm_service import llm_service

# import the retrieval result
from app.schemas.retrieval import RetrievalResult

# import the chat response
from app.schemas.chat import ChatResponse

class ChatService:


    def retrieve_context(self, query: str, top_k: int = 3) -> list[RetrievalResult]:
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
        retrieval_results = faiss_service.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        return retrieval_results

    def answer_question(self, query: str) -> ChatResponse:
        """
        Retrieve relevant context and generate an answer.

        Args:
            query:
                User's question.

        Returns:
            AI generated answer.
        """

        retrieval_results = self.retrieve_context(query)
        print("\n===== RETRIEVAL RESULTS =====")
        print(retrieval_results)
        print(f"Count: {len(retrieval_results)}")

        context = "\n\n".join(
            result.chunk for result in retrieval_results
        )

        sources = [
            result.metadata for result in retrieval_results]

        prompt = RAG_PROMPT.format(
            context=context,
            question=query
        )

        response = llm_service.generate_response(prompt)

        print("\n========== RETRIEVED CHUNKS ==========\n")

        for i, result in enumerate(retrieval_results, start=1):
            print(f"Result {i}")
            print("-" * 40)
            print(f"Document : {result.metadata.document}")
            print(f"Chunk ID : {result.metadata.chunk_id}")
            print("\nChunk")
            print(result.chunk)


        print("\n========== AI RESPONSE ==========\n")
        print(response)

        return ChatResponse(
            answer=response,
            sources=sources
        )
    
chat_service = ChatService()