from datebase import get_db
from schemy import DocumentCreate,DocumentUpdate,DocumentOut
from model import Document
from sqlalchemy.orm import Session
from sqlalchemy import or_
def create_document(db:Session,data:DocumentCreate,):
    document = Document(
        title =data.title,
        content =data.content,
        file_size =data.file_size,
        file_type =data.file_type,
    )
    try:
        db.add(document)
        db.commit()
        db.refresh(document)
        return document
    except:
        db.rollback()
        raise

def get_documents(db:Session,keyword:str|None =None,page:int =1,page_size: int=20,):
    query =db.query(Document)
    if keyword:
             query = query.filter(
            or_(
                Document.title.contains(keyword),
                Document.content.contains(keyword),
            )
        )
    totle =query.count()
    documents =(
         query.order_by(Document.id.desc()).offset((page-1)*page_size).limit(page_size).all()
    )
    return totle,documents

def get_document_by_id(db:Session,document_id:int,):
     return (db.query(Document).filter(Document.id==document_id).first())

def update_document(db:Session,document:Document,data:DocumentUpdate):
    updata_data =data.model_dump(exclude_unset=True)
    for field,value in updata_data.items():
        setattr(document,field,value)
    try:
         db.commit()
         db.refresh(document)
         return document
    except:
         db.rollback()
         raise

def delete_document(
    db: Session,
    document: Document,
):
    """删除文档。"""

    try:
        db.delete(document)
        db.commit()

    except Exception:
        db.rollback()
        raise
    