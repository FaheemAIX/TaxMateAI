# This module contains helper functions related to filename generation.
# Keeping this logic here follows the DRY principle and Separation of Concerns.


# This function generates a unique filename for storing the uploaded document.
# It receives:
#   1. document_id       -> Generated UUID
#   2. original_filename -> Name uploaded by the user
#
# It returns:
#   document_id_originalFilename
#
# Example:
# a83c91_income_tax.pdf

def generate_stored_filename(document_id: str, original_filename: str) -> str:
    
    # replaces all spaces with underscore
    stored_filename = document_id + "_" + original_filename.replace(" ", "_")

    return stored_filename 
    