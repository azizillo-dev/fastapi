from schemas import *
from sqlalchemy.orm import Session
from models import Student
from fastapi.exceptions import HTTPException



def create_student(db: Session, data: StudentCreateSchema):
    student = Student(**data.model_dump())
    db.add(student)
    db.commit()
    db.refresh(student)
    return {
        "msg" : "Student added",
        "student" : StudentResponse(student)
    }


def student_list(db: Session):
    students = db.query(Student).all()
    return {
        "msg" : "Student list",
        "students" : students
    }



def student_detail(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id==student_id).first()
    if not student:
        raise HTTPException(detail="Student not found")
    return {
        "msg" : "student_detail",
        "student" : student 
    }


def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id==student_id).first()
    if not student:
        raise HTTPException(detail="Student not found")
    db.delete(student)
    db.commit()
    return {
        "msg": "Student deleted"
    }




