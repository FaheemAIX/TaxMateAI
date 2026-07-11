from fastapi import UploadFile


def validate_pdf(file: UploadFile) -> None:
    """
    Validate that the uploaded file is a PDF.

    Raises:
        ValueError: If the file extension or MIME type is invalid.
    """

    # Check that the filename ends with '.pdf' (case-insensitive).
    if not file.filename.lower().endswith(".pdf"):
        raise ValueError("Only PDF files are allowed.")

    # Check the MIME type reported by the upload.
    if file.content_type != "application/pdf":
        raise ValueError("Invalid PDF MIME type.")