from datetime import datetime
from pydantic import EmailStr, Field, BaseModel



class UserCreate(BaseModel):
    first_name : str = Field(min_length=3, max_length=50)
    last_name : str = Field(min_length=3, max_length=50)
    username : str = Field(min_length=3, max_length=50)
    email : EmailStr
    password : str = Field(min_length=3)


class UserResponse(BaseModel):
    id : int
    first_name : str
    last_name : str
    username : str
    email : EmailStr
    created_at : datetime
    is_active : bool

    model_config = {
        "from_attributes": True
    }



