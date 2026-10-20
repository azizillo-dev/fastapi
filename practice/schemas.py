from pydantic import BaseModel, ConfigDict, Field



class StudentCreateSchema(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    age: int = Field()



class StudentResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    age: int


class StudentUpdateSchema(BaseModel):
    first_name: str | None=None
    last_name: str | None=None
    age: int | None=None


