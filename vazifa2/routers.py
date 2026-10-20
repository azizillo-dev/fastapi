from fastapi import APIRouter, Depends
from schemas import *
from crud import *
from db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/create', status_code=201)
def create__student(data: StudentCreateSchema, db: Session = Depends(get_db)):
    return create_student(db, data)

@router.get('/')
def get_students(db: Session = Depends(get_db)):
    return student_list(db)

@router.get('/{student_id}')
def get_student(student_id: int, db: Session = Depends(get_db)):
    return student_detail(db, student_id)

@router.delete('/{student_id}')
def delete_student_by_id(student_id: int, db: Session = Depends(get_db)):
    return delete_student(db, student_id)
