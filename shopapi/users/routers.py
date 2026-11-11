from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from db import get_db
from users.schemas import UserCreate, UserResponse
from users import crud


router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.post('/', response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = crud.create_user(db=db, user=user)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    return new_user


@router.get('/', response_model=list[UserResponse])
def get_users_all(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


