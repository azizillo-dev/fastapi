from db import Base
from sqlalchemy import Column, Integer, String, DECIMAL, Text


class Book(Base):

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    price = Column(DECIMAL, nullable=False)

    



