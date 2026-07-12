from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
DATEBASE_URL =os.getenv("DATEBASE_URL","sqlite:///data/app.db")

engine =create_engine(DATEBASE_URL,echo=False)
SessionLocal =sessionmaker(bind=engine)
Base =declarative_base()

def init_db():
    '''创建所有表'''
    os.makedirs("data",exist_ok=True)
    Base.metadata.create_all(bind=engine)