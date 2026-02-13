# Import FastAPI class to create our web application
from fastapi import FastAPI

# Import router from our routes file (API layer)
from app.api.routes import router


# Create FastAPI application instance
# This object represents our backend server
app = FastAPI(
    title="Document Intelligence API",  # API title shown in Swagger
    description="AI-powered document processing system",  # Short description
    version="1.0.0"  # API version
)


# Include all API routes from routes.py
# This keeps main.py clean and scalable
app.include_router(router)


# Health check endpoint
# Used to confirm server is running properly
@app.get("/")
def root():
    """
    Root endpoint to verify server is alive.
    """
    return {"status": "Document AI Backend Running"}
