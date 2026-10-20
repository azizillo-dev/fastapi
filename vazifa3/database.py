from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine



DATABASE_URL = "postgresql+psycopg://postgres:CEO517984@localhost:5432/vazifa3_db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


