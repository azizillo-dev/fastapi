from database import Base
from sqlalchemy import String, Integer, Column, Text, ForeignKey
from sqlalchemy.orm import relationship




class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False)
    first_name = Column(String(30))
    comments = relationship("Comment", back_populates='users')




class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    comments = relationship("Comment", back_populates="book")


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    body = Column(Text, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship("Book")
    user = relationship("User", back_populates="comments")



