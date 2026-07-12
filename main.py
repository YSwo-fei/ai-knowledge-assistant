from fastapi import FastAPI
from schemy import DocumentCreate

app =FastAPI(title="AI知识库助手",version="0.1.0")

@app.post("/api/documents")
def create_document(document: DocumentCreate):
    """接收用户发送的文档数据。"""

    return {
        "message": "文档接收成功",
        "document": {
            "title": document.title,
            "content": document.context,
            "file_type": document.file_type,
            "file_size": document.file_size,
        },
    }

@app.get("/")
def home():
    '''应用信息'''
    return {
        "app":"AI知识库助手",
        "version":"0.1.0",
        "framework":"FastAPI",
    }
 
@app.get("/api/info")
def info():
    return {"app":"AI助手",
            "status":"running",}
 