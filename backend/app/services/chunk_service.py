class ChunkService:
    """Split text into smaller chunks."""

    def chunk_text(
        self,
        text: str,
        chunk_size: int = 500
    ) -> list[str]:

        # Store all chunks.
        chunks = []

        # Move through the text.
        for i in range(0, len(text), chunk_size):

            # Take one chunk.
            chunk = text[i:i + chunk_size]

            # Save it.
            chunks.append(chunk)

        return chunks


# Create one object.
chunk_service = ChunkService()