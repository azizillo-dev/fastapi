from sqlalchemy import String, Integer, Text, Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base




class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    age = Column(Integer, nullable=False)

    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    likes = relationship("Like", back_populates="user")



class Post(Base):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)

    user = relationship("User", back_populates="posts")


class Comment(Base):

    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("Post.id"), nullable=False)

    user = relationship("User", back_populates='comments')
    post = relationship("Post", back_populates='comments')



class Like(Base):
    
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("Posts.id"), nullable=False)

    user = relationship("User", back_populates='likes')
    post = relationship("Post", back_populates='likes')


