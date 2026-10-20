from fastapi import APIRouter, Depends, status
from crud import create_book, detail_book, books_list
from db import get_db
from schemas import BookCreateSchema
from sqlalchemy.orm import Session


router = APIRouter()

@router.post('/create', status_code=status.HTTP_201_CREATED)
def book_create(data: BookCreateSchema, db: Session = Depends(get_db)):
    return create_book(db, data)

@router.get('/{book_id}')
def book_detail(book_id: int, db: Session = Depends(get_db)):
    return detail_book(book_id, db)


@router.get('/')
def book_list(db: Session = Depends(get_db)):
    return books_list(db)


