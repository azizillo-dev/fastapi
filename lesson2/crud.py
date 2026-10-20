from sqlalchemy.orm import Session
from models import Book
from schemas import BookCreateSchema
from fastapi.exceptions import HTTPException



def create_book(db: Session, data: BookCreateSchema):
    # book = Book(title=data.title, price=data.price, description=data.description)
    # book = Book(**data.dict())
    book = Book(**data.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    return {
        "msg" : "Book created",
        "book" : book,
    }



def detail_book(book_id: int, db: Session):
    book = db.query(Book).filter(Book.id==book_id).first()
    if not book:
        raise HTTPException(detail="Bunday kitob topilmadi!", status_code=404)
    return {
        "book" : book
    }




def books_list(db: Session):
    books = db.query(Book).all()
    return {
        "books" : books,
        "count" : len(books)
    }



