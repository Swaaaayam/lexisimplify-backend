from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import os
from uuid import uuid4
from utils.pdf_extractor import extract_clauses_from_pdf

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

latest_uploaded_file = {"path": None}


@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    filename = f"{uuid4()}.pdf"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    latest_uploaded_file["path"] = file_path

    try:
        clauses = extract_clauses_from_pdf(file_path)
        return {"clauses": clauses}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@router.get("/clauses")
def get_clauses():
    file_path = latest_uploaded_file.get("path")
    if not file_path or not os.path.exists(file_path):
        return JSONResponse(status_code=404, content={"error": "No uploaded PDF found."})
    
    try:
        clauses = extract_clauses_from_pdf(file_path)
        return {"clauses": clauses}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
