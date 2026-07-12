from pydantic import BaseModel
class DocumentCreate(BaseModel):
    title:str
    context:str
    file_size:int = 0
    file_type:str="text"

