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

# Import pickle for serializing Python objects.
import pickle

# Import vector store directory configuration.
from app.core.config import VECTORSTORE_DIR


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

        # Dimension of BAAI/bge-small-en-v1.5 embeddings.
        self.dimension = 384

        # Create an L2 (Euclidean distance) index. 
        # Creates empty faiss index
        self.index = faiss.IndexFlatL2(self.dimension)

        # Store original chunks.
        # creates empty list
        self.chunks: list[str] = []

        # Load previously saved vector store if it exists.
        self.load_index()
        self.load_chunks()

    def add_embeddings(self, embeddings: list[list[float]],chunks: list[str]) -> None:
       
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

        # Persist the updated vector store.
        self.save_index()
        self.save_chunks()

        # DEBUG: Remove after testing.
        print(f"Vectors in FAISS Index: {self.index.ntotal}")

    def search(self, query_embedding: list[float], top_k: int = 3) -> list[str]:
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

        # Collect retrieved chunks.
        retrieved_chunks = []

        for index in indices[0]:

            if index != -1:
                retrieved_chunks.append(
                    self.chunks[index]
                )

        print(f"Total vectors in FAISS: {self.index.ntotal}")
        
        return retrieved_chunks
    
    def save_index(self) -> None:
        """
        Save the FAISS index to disk.

        This method persists the current FAISS index so that it can be
        reloaded when the application restarts.
        """

        # Build the path for the FAISS index file.
        index_path = VECTORSTORE_DIR / "index.faiss"

        # Save the FAISS index.
        faiss.write_index(self.index, str(index_path))

        print(f"FAISS index saved to: {index_path}")

        '''The faiss.write_index() function is used because a FAISS index is a complex object implemented internally by the FAISS library. Unlike ordinary Python objects or text files, it cannot be saved correctly using Python's built-in open() function. The FAISS library provides write_index() to serialize and store the index in its native binary format. Additionally, index_path is a Path object created by the pathlib module, whereas faiss.write_index() expects a file path as a string. Therefore, we convert the Path object into a string using str(index_path) before passing it to the function.'''

        # Serialization
        '''Serialization in Python is the process of converting an in-memory Python object (such as a dictionary, list, or custom class instance) into a format that can be easily stored in a file, saved to a database, or transmitted over a network.'''
        
    def save_chunks(self) -> None:
        """
        Save the original document chunks to disk.

        This method serializes the list of document chunks
        using pickle so they can be restored when the
        application restarts.
        """

        # Build the path for the chunk file.
        chunks_path = VECTORSTORE_DIR / "chunks.pkl"

        # Open the file in binary write mode.
        with open(chunks_path, "wb") as file:

            # Serialize and save the chunks.
            pickle.dump(self.chunks, file)

        print(f"Chunks saved to: {chunks_path}")

        '''pickle.dump() is used because self.chunks is a Python list object, not plain text. The pickle module serializes the Python object into a binary format that can later be reconstructed exactly as it was. Since the serialized data is binary rather than text, the file must be opened in binary write mode ("wb"). The built-in file.write() method cannot directly write complex Python objects such as lists, dictionaries, or custom classes, whereas pickle.dump() handles both serialization and writing automatically.'''

    def load_index(self) -> None:
        """
        Load the FAISS index from disk.

        If the index file exists, it is loaded into memory.
        Otherwise, the empty index created during initialization
        will continue to be used.
        """

        # Build the path of the saved FAISS index.
        index_path = VECTORSTORE_DIR / "index.faiss"

        # Check whether the index file exists.
        if index_path.exists():

            # Load the saved FAISS index.
            self.index = faiss.read_index(str(index_path))

            print(f"FAISS index loaded from: {index_path}")

        else:
            print("No saved FAISS index found. Using empty index.")


    def load_chunks(self) -> None:
        """
        Load the document chunks from disk.

        If the chunk file exists, it is deserialized and loaded
        into memory. Otherwise, an empty chunk list is used.
        """

        # Build the path for the chunk file.
        chunks_path = VECTORSTORE_DIR / "chunks.pkl"

        # Check whether the chunk file exists.
        if chunks_path.exists():

            # Open the file in binary read mode.
            with open(chunks_path, "rb") as file:
                '''pickle.dump() stores serialized Python objects in binary format, therefore we must open the file in binary read mode ("rb") when using pickle.load().'''

                # Deserialize and load the chunks.
                self.chunks = pickle.load(file)

            print(f"Chunks loaded from: {chunks_path}")

        else:
            print("No saved chunks found. Using empty chunk list.")

# Create one shared instance for the application.
faiss_service = FAISSService()