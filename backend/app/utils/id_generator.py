# Import Python's built-in module for generating universally unique identifiers.
import uuid


# This function generates a unique document ID.
# We use a function instead of a class because this is a single, reusable task.
def generate_id() -> str:
    # Generate a random UUID (version 4).
    # uuid4() returns a UUID object, not a string.
    document_id = uuid.uuid4()

    # Convert the UUID object into a string.
    # Strings are easier to store in JSON, databases, and API responses.
    return str(document_id)