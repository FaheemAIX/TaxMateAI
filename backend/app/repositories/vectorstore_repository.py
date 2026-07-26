import pickle

from app.core.config import VECTORSTORE_DIR

import faiss


"""
Vector Store Repository

This repository is responsible for persisting and retrieving
all vector store related data.

Responsibilities:
- Save and load FAISS index
- Save and load document chunks
- Save and load metadata
- Save and load embeddings

Author: Muhammad Faheem Ullah
Project: AI Knowledge Assistant for FBR
"""


class VectorStoreRepository:
    """
    Repository responsible for managing vector store persistence.
    """

    def save_chunks(self, chunks: list[str]) -> None:
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
            pickle.dump(chunks, file)

            '''pickle.dump() is used because self.chunks is a Python list object, not plain text. The pickle module serializes the Python object into a binary format that can later be reconstructed exactly as it was. Since the serialized data is binary rather than text, the file must be opened in binary write mode ("wb"). The built-in file.write() method cannot directly write complex Python objects such as lists, dictionaries, or custom classes, whereas pickle.dump() handles both serialization and writing automatically.'''
            print(f"Chunks saved to: {chunks_path}")

    def load_chunks(self) -> list[str]:
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

                print(f"Chunks loaded from: {chunks_path}")

                # Deserialize and load the chunks.
                return pickle.load(file)
        else:
            print("No saved chunks found. Using empty chunk list.")
            return []

    def save_metadata(self, metadata: list[dict]) -> None:
            """
            Save chunk metadata to disk.
    
            This method serializes the metadata associated with each
            document chunk using pickle so it can be restored when the
            application restarts.
            """
    
            # Build the path for the metadata file.
            metadata_path = VECTORSTORE_DIR / "metadata.pkl"
    
            # Open the file in binary write mode.
            with open(metadata_path, "wb") as file:
    
                # Serialize and save the metadata.
                pickle.dump(metadata, file)
    
                print(f"Metadata saved to: {metadata_path}")
    
    def load_metadata(self) -> list[dict]:
        """
        Load chunk metadata from disk.

        If metadata already exits then it loads the chunk metadata.
        """
        # path where we save chunk metadata
        metadata_path = VECTORSTORE_DIR / "metadata.pkl"

        # Check whether the metadata file exists.
        if metadata_path.exists():

            # Open the file in binary read mode.
            with open(metadata_path, "rb") as file:

                # load the file
                print(f"Metadata loaded from: {metadata_path}")
                return pickle.load(file)

        else:
            print("No saved metadata found. Using empty metadata.")
            return []

    def save_index(self, index: faiss.Index) -> None:
            """
            Save the FAISS index to disk.
    
            This method persists the current FAISS index so that it can be
            reloaded when the application restarts.
            """
    
            # Build the path for the FAISS index file.
            index_path = VECTORSTORE_DIR / "index.faiss"
    
            # Save the FAISS index.
            faiss.write_index(index, str(index_path))
    
            print(f"FAISS index saved to: {index_path}")
    
            '''The faiss.write_index() function is used because a FAISS index is a complex object implemented internally by the FAISS library. Unlike ordinary Python objects or text files, it cannot be saved correctly using Python's built-in open() function. The FAISS library provides write_index() to serialize and store the index in its native binary format. Additionally, index_path is a Path object created by the pathlib module, whereas faiss.write_index() expects a file path as a string. Therefore, we convert the Path object into a string using str(index_path) before passing it to the function.'''
    
            # Serialization
            '''Serialization in Python is the process of converting an in-memory Python object (such as a dictionary, list, or custom class instance) into a format that can be easily stored in a file, saved to a database, or transmitted over a network.'''
            
        
    def load_index(self) -> faiss.Index | None:
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

            print(f"FAISS index loaded from: {index_path}")
            # Load the saved FAISS index.
            return faiss.read_index(str(index_path))


        else:
            print("No saved FAISS index found. Using empty index.")
            return None

    

# Create one shared instance for the application.
vectorstore_repository = VectorStoreRepository()