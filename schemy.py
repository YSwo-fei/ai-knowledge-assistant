from pydantic import BaseModel
class DocumentCreate(BaseModel):
    title: str
    content: str
    file_size: int = 0
    file_type: str="text"

class DocumentUpdate(BaseModel):
    title:str|None =None
    content:str|None =None
    file_size:int|None =None
    file_type:str|None =None
class DocumentOut(DocumentCreate):
    id: int
    class Config:
        from_attributes = True