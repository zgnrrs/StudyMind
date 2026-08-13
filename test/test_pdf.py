from app.services.pdf_service import extract_text_from_pdf

pdf_path = "test.pdf"

text = extract_text_from_pdf(pdf_path)

print("PDF'den çıkarılan metin:")
print(text)