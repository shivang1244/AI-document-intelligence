# This dictionary will temporarily store document text in memory
# Key = document_id
# Value = full extracted text
document_store = {}


def save_document(document_id: str, text: str):
    """
    Store full document text in memory.
    """
    document_store[document_id] = text


def get_document(document_id: str) -> str:
    """
    Retrieve document text using document_id.
    """
    return document_store.get(document_id)
