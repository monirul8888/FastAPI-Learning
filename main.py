from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time




app = FastAPI()

@app.get("/")
def view():

    cursor.execute(""" SELECT * FROM STUDENT """)
    data = cursor.fetchall()
    return {"message" : "Welcome To FastAPI",
            "Data": data}


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




while True:
    try:
        conn = psycopg2.connect(
            host = "localhost",
            database = "university",
            user = "postgres",
            password = "1234",
            cursor_factory = RealDictCursor
        )

        cursor = conn.cursor()
        print("Successfully Connected To The Database")
        break
    except Exception as error:
        print("Database Connection Failed")
        print("Error : ", error)
        time.sleep(2)

