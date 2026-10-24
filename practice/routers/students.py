from fastapi import APIRouter, Depends
from schemas import StudentCreateSchema, StudentResponseSchema, StudentUpdateSchema
from database import get_db
from sqlalchemy.orm import Session
from models import Student
from fastapi.exceptions import HTTPException


router = APIRouter()


@router.post("/create", response_model=StudentResponseSchema)
def student_create(student: StudentCreateSchema, db: Session = Depends(get_db)):
    student = Student(**student.model_dump())
    db.add(student)
    db.commit()
    db.refresh(student)
    return StudentResponseSchema.model_validate(student)
    

@router.get('/', response_model=list[StudentResponseSchema])
def students_list(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students


@router.get('/{student_id}', response_model=StudentResponseSchema)
def student_detail(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id==student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student topilmadi!")
    return StudentResponseSchema.model_validate(student)


@router.put("/{student_id}", response_model=StudentResponseSchema)
def student_update(student_id: int, data: StudentUpdateSchema, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id==student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student topilmadi!")
    
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(student, key, value)
    db.commit()
    db.refresh(student)
    return StudentResponseSchema.model_validate(student)



@router.delete('/{student_id}')
def student_delete(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id==student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student topilmadi!")
    
    db.delete(student)
    db.commit()
    return {
        "msg" : "Student o'chirildi!"
    }

