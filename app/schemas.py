
from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    dept: str
    id: int

class StudentResponse(StudentCreate):
    id : int

    class Config:
        orm_model= True

class UserCreate(BaseModel):
    email: EmailStr
    password : str
