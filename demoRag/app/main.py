"""
main.py - Entry point for VerdictAI backend server

Author: justin.m
Date: 2025-07-23

This module initializes the FastAPI server for VerdictAI. 
Currently supports basic health check, document upload simulation,
and query handling with placeholder response.
"""

import os
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Create necessary directories
os.makedirs("data/raw", exist_ok=True)

# Initialize FastAPI app
app = FastAPI(
    title="VerdictAI",
    description="Backend API for VerdictAI — RAG-powered legal assistant",
    version="0.1.0"
)

# CORS middleware (in case frontend is added later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------
# Health Check Endpoint
# ------------------------------

@app.get("/ping")
def ping():
    """
    Health check endpoint.

    Returns:
        JSON response with 'pong'
    """
    return {"message": "pong"}


# ------------------------------
# Document Ingestion Endpoint
# ------------------------------

@app.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):
    """
    Accepts a PDF or DOCX file and stores it in 'data/raw/'.

    Args:
        file (UploadFile): The uploaded file.

    Returns:
        JSON response indicating success or error.
    """
    filename = file.filename
    file_path = os.path.join("data/raw", filename)

    try:
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        return {"message": f"File '{filename}' uploaded successfully."}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


# ------------------------------
# Query Endpoint (Simulated)
# ------------------------------

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
def query_rag(req: QueryRequest):
    """
    Accepts a user query and returns a simulated response.

    Args:
        req (QueryRequest): The input question.

    Returns:
        JSON response with a fake answer.
    """
    fake_response = (
        f"Simulated answer for: '{req.question}'. "
        "This will be replaced by actual model output once RAG is integrated."
    )
    return {"response": fake_response}


# ------------------------------
# Optional: Static Mount for Uploaded Files (Dev Only)
# ------------------------------

app.mount("/data", StaticFiles(directory="data/raw"), name="data")

