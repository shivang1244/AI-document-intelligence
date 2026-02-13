from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from typing import Any
import torch

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32
)

# Create generation pipeline
generator: Any = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)




def ask_llm(document_text: str, question: str) -> str:
    """
    Run local TinyLlama model for document Q&A.
    """

    truncated_doc = document_text[:3000]

    # Proper chat format for TinyLlama
    prompt = f"""<|system|>
    You are an AI document assistant.

    Follow these rules strictly:
    - Answer briefly.
    - Do NOT repeat the document.
    - If asked about document type, respond with only the type (e.g., Resume, Invoice, Contract).
    - If information is not found, say: Information not found in document.
    <|user|>
    Document:
    {truncated_doc}

    Question: {question}
    <|assistant|>
    """

    try:
        output = generator(
            prompt,
            max_new_tokens=200,
            temperature=0.1,
            do_sample=False,   # deterministic output
            pad_token_id=tokenizer.eos_token_id
        )

        generated_text = output[0]["generated_text"]

        # Extract only assistant response
        answer = generated_text.split("<|assistant|>")[-1].strip()

        return answer

    except Exception as e:
        raise Exception(f"Local LLM processing failed: {str(e)}")
