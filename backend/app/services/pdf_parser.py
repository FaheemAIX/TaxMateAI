# Import PyMuPDF.
import fitz

# Import Path because the parser receives a file path.
from pathlib import Path


class PDFParser:
    """
    Service responsible for reading PDF documents.
    """

    def parse(self, file_path: Path) -> str:
        """
        Extract all text from a PDF.

        Args:
            file_path: Path to the PDF file.

        Returns:
            A single string containing the text from all pages.
        """

        # Open the PDF document.
        document = fitz.open(file_path)

        # Store text from each page.
        pages = []

        # Loop through every page in the PDF.
        for page in document:

            # Extract text from the current page.
            text = page.get_text()

            # Save the extracted text.
            pages.append(text)

        # Close the PDF to release system resources.
        document.close()

        # Combine all page text into one string.
        return "\n".join(pages)