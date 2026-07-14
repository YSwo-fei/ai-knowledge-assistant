from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
import crud
from datebase import get_db
from schemy import DocumentCreate, DocumentUpdate
router = APIRouter(
    prefix="/api/documents",
    tags=["文档管理"],
)
@router.post("/", status_code=201)
def create_document(
    data: DocumentCreate,
    db: Session = Depends(get_db),
):
    document = crud.create_document(db, data)

    return {
        "message": "文档创建成功",
        "document": document.to_dict(),
    }

@router.get("/")
def get_documents(
    keyword: str | None = None,
    page: int = 1,
    page_size: int = 20,
    db: Session = Depends(get_db),
):
    total, documents = crud.get_documents(
        db=db,
        keyword=keyword,
        page=page,
        page_size=page_size,
    )

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "documents": [
            document.to_dict()
            for document in documents
        ],
    }

@router.get("/{document_id}")
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    document = crud.get_document_by_id(
        db,
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="文档不存在",
        )

    return document.to_dict()

@router.patch("/{document_id}")
def update_document(
    document_id: int,
    data: DocumentUpdate,
    db: Session = Depends(get_db),
):
    document = crud.get_document_by_id(
        db,
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="文档不存在",
        )

    updated_document = crud.update_document(
        db,
        document,
        data,
    )

    return {
        "message": "文档更新成功",
        "document": updated_document.to_dict(),
    }

@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    document = crud.get_document_by_id(
        db,
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="文档不存在",
        )

    crud.delete_document(db, document)

    return {
        "message": "文档删除成功",
        "document_id": document_id,
    }