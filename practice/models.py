from database import Base
from sqlalchemy import Integer, Column, String




class Student(Base):

    __tablename__ = 'students'

    id = Column(Integer, nullable=False, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

    




