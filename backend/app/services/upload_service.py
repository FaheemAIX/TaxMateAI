# Import UploadFile because the save() method receives uploaded files.
from fastapi import UploadFile

# Import the upload directory configuration.
from app.core.config import UPLOAD_DIR

# Import PDF parser service.
from app.services.pdf_parser import PDFParser

# Import the chunk service
from app.services.chunk_service import chunk_service

# Import the embedding service
from app.services.embedding_service import embedding_service

# Import the FAISS service
from app.services.faiss_service import faiss_service



# Create one parser object.
pdf_parser = PDFParser()

class UploadService:

    def save(self, file: UploadFile):

        file_path = UPLOAD_DIR / file.filename

        with open(file_path, "wb") as f:
            f.write(file.file.read())
            
        # Extract text from the saved PDF.
        text = pdf_parser.parse(file_path)

        # Split the extracted text into chunks.
        chunks = chunk_service.chunk_text(text)

        # Generate embeddings from chunks.
        embeddings = embedding_service.embed_chunks(chunks)

        # Store embeddings and their corresponding chunks in FAISS.
        faiss_service.add_embeddings(embeddings=embeddings,chunks=chunks)

        #print total number
        print(f"Total number of chunks {len(chunks)}")
        print(f"Total number of embeddings {len(embeddings)}")
        print(f"Embedding dimensions {len(embeddings[0])}")
       



        return file_path


upload_service = UploadService()