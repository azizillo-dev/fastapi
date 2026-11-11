from users.schemas import UserCreate
from users.models import User
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session





def create_user(db: Session, user: UserCreate):
    user = User(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=user.password
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise
    db.refresh(user)
    return user


def get_users(db: Session):
    users = db.query(User).all()
    return users





