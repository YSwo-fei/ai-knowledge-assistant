from fastapi import FastAPI

from datebase import init_db
from model import Document
from rounters.document import router as documents_router


init_db()

app = FastAPI(
    title="AI知识库助手",
    version="0.1.0",
)

app.include_router(documents_router)


@app.get("/")
def home():
    return {
        "app": "AI知识库助手",
        "version": "0.1.0",
        "framework": "FastAPI",
    }