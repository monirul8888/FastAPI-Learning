from fastapi import FastAPI, HTTPException
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
    cgpa: float


@app.post("/post")
def createStudent(st: Student):
    cursor.execute(
        "INSERT INTO STUDENT (NAME, ID, DEPT, CGPA) VALUES (%s, %s, %s, %s) RETURNING *",
        (st.name, st.id, st.dept , st.cgpa)
    )
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}  




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


@app.get("/student/{st_id}")
def view_student(st_id: int):
    cursor.execute("SELECT * FROM STUDENT WHERE id = %s", (st_id,))
    st = cursor.fetchone()  # fetch one row
    if not st:
        raise HTTPException(
            status_code=404,
            detail=f"Student with ID {st_id} Not Found"
        )
    return {"Student Details": st}
