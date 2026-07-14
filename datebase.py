from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
DATEBASE_URL =os.getenv("DATEBASE_URL","sqlite:///data/app.db")

engine =create_engine(DATEBASE_URL,echo=False)
SessionLocal =sessionmaker(autoflush=False,autocommit=False,bind = engine)
Base =declarative_base()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    '''创建所有表'''
    
def init_db():

    os.makedirs("data", exist_ok=True)
    Base.metadata.create_all(bind=engine)