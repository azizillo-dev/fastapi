from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "postgresql+psycopg2://postgres:CEO517984@localhost:5432/practice_db"


engine = create_engine(DATABASE_URL, echo=True)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)




Base = declarative_base()

def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        





