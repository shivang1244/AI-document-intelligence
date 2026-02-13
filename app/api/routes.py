# Import APIRouter to create modular API routes
from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import shutil
import os
import uuid

# Import OCR extraction service
from app.services.ocr_service import extract_text

# Import document storage
from app.services.vector_service import save_document, get_document

# Import LLM service
from app.services.llm_service import ask_llm


# Create router instance
router = APIRouter()


# Define folder where uploaded files will be stored
UPLOAD_FOLDER = "uploaded_files"

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# ---------------------------
# Upload Endpoint
# ---------------------------
@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload document and process it with OCR.
    """

    if not file.filename.endswith((".pdf", ".png", ".jpg", ".jpeg")):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and Image files are allowed"
        )

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        extracted_text = extract_text(file_path)

        document_id = str(uuid.uuid4())
        save_document(document_id, extracted_text)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Processing failed: {str(e)}"
        )

    return {
        "message": "Document processed successfully",
        "document_id": document_id,
        "status": "ready_for_questions"
    }


# ---------------------------
# Ask Endpoint
# ---------------------------
class QuestionRequest(BaseModel):
    document_id: str
    question: str


@router.post("/ask")
async def ask_question(request: QuestionRequest):
    """
    Ask a question about uploaded document.
    """

    document_text = get_document(request.document_id)

    if document_text is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found. Please upload again."
        )

    try:
        answer = ask_llm(document_text, request.question)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI processing failed: {str(e)}"
        )

    return {
        "document_id": request.document_id,
        "question": request.question,
        "answer": answer
    }
