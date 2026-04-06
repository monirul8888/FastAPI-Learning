from fastapi import FastAPI
from pydantic import BaseModel





app = FastAPI()

@app.get("/")
def view():
    return {"message" : "Welcome To FastAPI"}

@app.get("/about")
def about():
    return {"about" : "This is About Page"}



class Student(BaseModel):
    name: str
    id: int
    dept: str

@app.post("/post")
def createStudent(st: Student):
    return {"data" : st}



