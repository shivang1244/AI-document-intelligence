import gradio as gr
import uuid
from app.services.ocr_service import extract_text
from app.services.llm_service import ask_llm

# In-memory document storage
document_store = {}


def upload_document(file):
    try:
        text = extract_text(file.name)

        document_id = str(uuid.uuid4())
        document_store[document_id] = text

        return f"Document uploaded successfully!\nDocument ID: {document_id}"

    except Exception as e:
        return f"Error processing document: {str(e)}"


def ask_question(document_id, question):
    if document_id not in document_store:
        return "Document not found. Please upload again."

    try:
        answer = ask_llm(document_store[document_id], question)
        return answer
    except Exception as e:
        return f"Error generating answer: {str(e)}"


with gr.Blocks() as demo:
    gr.Markdown("# 📄 AI Document Intelligence System")

    with gr.Tab("Upload Document"):
        file_input = gr.File(label="Upload PDF or Image")
        upload_output = gr.Textbox(label="Upload Status")
        upload_btn = gr.Button("Upload")

        upload_btn.click(upload_document, inputs=file_input, outputs=upload_output)

    with gr.Tab("Ask Question"):
        doc_id_input = gr.Textbox(label="Enter Document ID")
        question_input = gr.Textbox(label="Your Question")
        answer_output = gr.Textbox(label="Answer")
        ask_btn = gr.Button("Ask")

        ask_btn.click(
            ask_question,
            inputs=[doc_id_input, question_input],
            outputs=answer_output
        )

demo.launch()
