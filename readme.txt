AI Document Intelligence System
A fully deployed AI-powered Document Intelligence platform that allows users to upload documents and ask natural language questions about them.

🔗 Live Demo:
https://huggingface.co/spaces/ssd64e57/ai-document-intelligence

🚀 Problem Statement
Organizations receive thousands of documents daily:
Resume
Invoices
Contracts
Certificates
Bank Statements
Manual review is:
Time-consuming
Error-prone
Expensive
This system automates document understanding using OCR + Transformer-based LLMs.

🧠 How It Works
User Upload
     ↓
OCR Text Extraction
     ↓
In-Memory Document Storage
     ↓
Transformer-based LLM (TinyLlama)
     ↓
Natural Language Answer

⚙️ Tech Stack
Python
Gradio (UI & Deployment)
Hugging Face Spaces (Free CPU Hosting)
Transformers (TinyLlama 1.1B)
PyTorch
pdfplumber (PDF OCR)
pytesseract (Image OCR)

✨ Features
Upload PDF or image documents
Automatic OCR extraction
Ask natural language questions
Context-aware responses
Fully serverless deployment
No external API dependency

🏗 Architecture Design
Modular service-based backend structure
Separate OCR and LLM services
Lazy model loading to optimize memory
Clean Git version control
Cloud deployment pipeline

⚡ Deployment
Hosted publicly using:
Hugging Face Spaces
Free CPU environment
Self-contained model (no external API cost)

📌 Example Questions
What is this document about?
What is the education completion year?
Who is the author?
What skills are mentioned?

🧑‍💻 Author

Shivang Singh Choudhary
AI/ML Undergraduate

GitHub: https://github.com/shivang1244

🎯 Why This Project Matters
This project demonstrates:
Real-world AI system design
End-to-end deployment capability
LLM integration without paid APIs
Production-ready modular architecture

📈 Future Improvements
Vector database integration (RAG)
Multi-document memory
Structured field extraction
Improved classification accuracy
UI enhancements
🏁 Status

✅ Fully deployed
✅ Publicly accessible
✅ Free hosting
✅ No API cost
