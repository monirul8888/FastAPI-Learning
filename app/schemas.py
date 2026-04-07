
from pydantic import BaseModel, EmailStr
from datetime import datetime

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

class UserResponse(BaseModel):
    id:int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


