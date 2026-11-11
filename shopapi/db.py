import os
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

load_dotenv()


DATABSE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABSE_URL, echo=True)


SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


