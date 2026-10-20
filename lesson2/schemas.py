from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal



class BookCreateSchema(BaseModel):
    title: str = Field(max_length=100)
    description: Optional[str] = None
    price: Decimal = Field(gte=0, max_digits=10, decimal_places=2)
    




