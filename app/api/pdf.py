from fastapi import APIRouter, UploadFile, File
import tempfile
import os

from app.services.pdf_service import extract_text_from_pdf
from app.services.text_cleaner import clean_text
from app.services.ai_service import (
    generate_summary,
    generate_study_material
)

router = APIRouter()


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    file_content = await file.read()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(file_content)
        temp_path = temp_file.name

    try:

        # PDF'den metni çıkar
        text = extract_text_from_pdf(temp_path)

        # Metni temizle
        text = clean_text(text)

        # Kısa özet oluştur
        summary = generate_summary(text)

        # Ders notu oluştur
        study_material = generate_study_material(text)

        return {
            "filename": file.filename,
            "text": text,
            "summary": summary,
            "study_material": study_material
        }

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)