from pydantic import BaseModel, Field, EmailStr, ConfigDict


class StudentCreateSchema(BaseModel):
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=12, le=60)
    bio: str | None = None
    email: EmailStr | None = None



class StudentUpdateSchema(BaseModel):
    first_name: str | None = Field(default=None, min_length=2, max_length=50)
    last_name: str | None = Field(default=None, min_length=2, max_length=50)
    age: int | None = Field(default=None, gt=12, le=60)
    bio: str | None = None
    email: EmailStr | None = None


class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    bio: str | None = None
    email: EmailStr | None = None

    model_config = ConfigDict(from_attributes=True)

    






