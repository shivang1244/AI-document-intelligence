# Import required libraries
import pytesseract  # Python wrapper for Tesseract OCR
from PIL import Image  # For opening image files
import pdfplumber  # For extracting text from PDFs
import os


# Optional: Explicitly define Tesseract path (safer for Windows)
# Uncomment if needed
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_image(file_path: str) -> str:
    """
    Extract text from image files using Tesseract OCR.
    """

    try:
        # Open image using Pillow
        image = Image.open(file_path)

        # Extract text using OCR engine
        text = pytesseract.image_to_string(image)

        return text.strip()

    except Exception as e:
        raise Exception(f"OCR extraction failed: {str(e)}")


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from PDF files.
    Works for text-based PDFs.
    """

    try:
        text_content = ""

        # Open PDF file
        with pdfplumber.open(file_path) as pdf:
            # Loop through all pages
            for page in pdf.pages:
                # Extract text from each page
                page_text = page.extract_text()

                if page_text:
                    text_content += page_text + "\n"

        return text_content.strip()

    except Exception as e:
        raise Exception(f"PDF extraction failed: {str(e)}")


def extract_text(file_path: str) -> str:
    """
    Master function to detect file type and extract text accordingly.
    """

    # Get file extension
    _, extension = os.path.splitext(file_path)

    extension = extension.lower()

    if extension in [".jpg", ".jpeg", ".png"]:
        return extract_text_from_image(file_path)

    elif extension == ".pdf":
        return extract_text_from_pdf(file_path)

    else:
        raise Exception("Unsupported file type for OCR")
