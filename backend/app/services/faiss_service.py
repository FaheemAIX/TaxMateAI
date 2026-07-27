"""
FAISS Service

This module manages the FAISS vector index used for semantic search.

Responsibilities:
- Create and manage the FAISS index.
- Store embedding vectors.
- Maintain the mapping between vectors and document chunks.
- Perform similarity search.

Author: Muhammad Faheem Ullah
Project: AI Knowledge Assistant for FBR
"""

# Import FAISS library.
import faiss

# Import NumPy because FAISS works with NumPy arrays.
import numpy as np

# Import vector store repository.
from app.repositories.vectorstore_repository import vectorstore_repository

# Import retrieval result from schemas
from app.schemas.retrieval import RetrievalResult

# Import document info from schemas
from app.schemas.document import DocumentInfo


class FAISSService:
    """
    Service responsible for storing and searching embedding vectors.

    This service creates a FAISS index and keeps a mapping between
    vector IDs and their corresponding text chunks.
    """

    def __init__(self):
        """
        Initialize the FAISS service.

        Attributes:
            index:
                The FAISS vector index.

            chunks:
                Stores the original text chunk for each vector.
        """


        # Store original chunks.
        # creates empty list
        self.chunks: list[str] = []

        # Store metadata for each chunk.
        self.metadata: list[dict] = []

        # Dimension of BAAI/bge-small-en-v1.5 embeddings.
        self.dimension = 384
        # Load previously saved index if it exists.
        loaded_index = vectorstore_repository.load_index()

        if loaded_index is not None:
            self.index = loaded_index
        else:
            # Create an L2 (Euclidean distance) index. 
            # Creates empty faiss index
            self.index = faiss.IndexFlatL2(self.dimension)

        # load chunks
        self.chunks = vectorstore_repository.load_chunks()

        # load metadata
        self.metadata = vectorstore_repository.load_metadata()

        # DEBUG: Remove after testing.
        print("\n===== VECTOR STORE STATUS =====")
        print(f"Vectors  : {self.index.ntotal}")
        print(f"Chunks   : {len(self.chunks)}")
        print(f"Metadata : {len(self.metadata)}")
        print("===============================\n")


    def add_embeddings(self, embeddings: list[list[float]],chunks: list[str], metadata: list[dict]) -> None:
       
        """
        Add embeddings and their corresponding text chunks to the FAISS index.

        Args:
            embeddings:
                List of embedding vectors generated from document chunks.

            chunks:
                Original text chunks corresponding to each embedding.

        Returns:
            None
        """

        # Convert Python list to a NumPy array with float32 datatype.
        vectors = np.array(embeddings, dtype=np.float32)

        # Add vectors to the FAISS index.
        self.index.add(vectors)


        # Store the original chunks.
        self.chunks.extend(chunks)

        # Store metadata.
        self.metadata.extend(metadata)

        # Persist the updated vector store.
        vectorstore_repository.save_index(self.index)
        vectorstore_repository.save_chunks(self.chunks)
        vectorstore_repository.save_metadata(self.metadata)


        # DEBUG: Remove after testing.
        print(f"Vectors in FAISS Index: {self.index.ntotal}")

    def search(self, query_embedding: list[float], top_k: int = 3) -> list[RetrievalResult]:
        """
        Search the FAISS index and return the most relevant text chunks.

        Args:
            query_embedding:
                Embedding vector of the user's question.

            top_k:
                Number of similar chunks to retrieve.

        Returns:
            List of retrieved text chunks.
        """

        # Convert the query embedding into a NumPy array.
        query_vector = np.array([query_embedding], dtype=np.float32)
    

        # Search the FAISS index.
        distances, indices = self.index.search(query_vector, top_k)

        print("Distances:", distances)
        print("Indices:", indices)
        print("Total vectors:", self.index.ntotal)
        print("Total chunks:", len(self.chunks))
        print("Total metadata:", len(self.metadata))

        # Collect retrieval result.
        retrieval_results = []

        for index in indices[0]:

            if index != -1:
                result = RetrievalResult(
                    chunk=self.chunks[index],
                    metadata=self.metadata[index]
                )
                retrieval_results.append(result)

        # DEBUG: Remove after testing.

        print(f"Total vectors in FAISS: {self.index.ntotal}")
        
        return retrieval_results
    
    


    def get_documents(self) -> list[DocumentInfo]:
        """
        Retrieve information about all indexed documents.

        This method scans the stored metadata, counts the number
        of chunks belonging to each document, and returns a list
        of document information objects.

        Returns:
            A list of DocumentInfo objects containing:

            - document:
                Name of the uploaded document.

            - chunks:
                Total number of indexed chunks belonging to
                the document.
        """

        # Dictionary used to count chunks for each document.
        documents: dict[str, int] = {}

        # Count the number of chunks for each document.
        for metadata in self.metadata:

            # Get the document name.
            document = metadata["document"]

            # Increment the chunk count if the document
            # has already been encountered.
            if document in documents:
                documents[document] += 1

            # Otherwise initialize the chunk count.
            else:
                documents[document] = 1

        # Convert the dictionary into a list of
        # DocumentInfo objects.
        document_infos: list[DocumentInfo] = []

        for document, chunks in documents.items():

            document_infos.append(
                DocumentInfo(
                    document=document,
                    chunks=chunks
                )
            )

        return document_infos



# Create one shared instance for the application.
faiss_service = FAISSService()

