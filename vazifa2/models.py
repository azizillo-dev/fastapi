from db import Base
from sqlalchemy import Column, String, Integer, DECIMAL, Text


class Student(Base):

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    bio = Column(Text)
    email = Column(String(200), unique=True)


