from sqlalchemy import Column,Text,String,Integer,DateTime
from datetime import datetime,timezone
from datebase import Base
class Document(Base):
    __tablename__="document"
    id =Column(Integer,primary_key=True,autoincrement=True)
    title =Column(String(255),nullable=False)
    content =Column(Text,nullable=False)
    file_type =Column(String(20))
    file_size =Column(Integer)
    create_at =Column(DateTime,default=lambda:datetime.now(timezone.utc))

    def to_dict(self):
        return {
            "id":self.id,
            "title":self.title,
             "content": self.content[:200] + "..." if len(self.content) > 200 else self.content,
            "file_type": self.file_type,
            "file_size": self.file_size,
            "created_at": self.create_at.isoformat() if self.create_at else None,
        }