
from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    dept: str
    id: int

class StudentResponse(StudentCreate):
    id : int

    class Config:
        orm_model= True