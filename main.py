
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api.pdf import router as pdf_router 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pdf_router)

@app.get("/")
def home():
    return{"message": "Welcome to StudyMind!"}