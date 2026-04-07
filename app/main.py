from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from . import models
from sqlalchemy.orm import Session
from . database import engine, get_db


app = FastAPI()
models.Base.metadata.create_all(bind = engine)

class Student1(BaseModel):
    name: str
    dept: str
    id: int

@app.get("/student")
def student(db:Session = Depends(get_db)):

    st = db.query(models.Student).all()

    return{"status" : "SQL Alchemy Working",
           "Student Details": st}

@app.get("/student/{st_id}")
def student(st_id: int, db:Session = Depends(get_db)):

    st = db.query(models.Student).filter(models.Student.id == st_id).first()

    return{"status" : "SQL Alchemy Working",
           "Student Details": st}


@app.put("/student/{st_id}")
def student(st_id: int, update_st: Student1, db:Session = Depends(get_db)):

    st = db.query(models.Student).filter(models.Student.id == st_id)
    st_data= st.first()
    st.update(update_st.model_dump(), synchronize_session=False )
    db.commit()
    db.refresh(st_data)
    return{"status" : "SQL Alchemy Working",
           "Student Details": st_data}


@app.delete("/student/{st_id}")
def delete_student(st_id: int, db: Session = Depends(get_db)):

    st = db.query(models.Student).filter(models.Student.id == st_id).first()

    deleted_student = {
        "id": st.id,
        "name": st.name,
        "dept": st.dept,
    }
    db.delete(st)
    db.commit()
    return {
        "status": "Deleted Successfully",
        "Student Details": deleted_student
    }




# @app.get("/")
# def view():

#     cursor.execute(""" SELECT * FROM STUDENT """)
#     data = cursor.fetchall()
#     return {"message" : "Welcome To FastAPI",
#             "Data": data}



@app.get("/about")
def about():
    return {"about" : "This is About Page"}

@app.post("/student")
def student(st: Student1, db: Session = Depends(get_db)):
    new_st = models.Student(
        id = st.id,
        name = st.name,
        dept = st.dept
    )
    db.add(new_st)
    db.commit()
    db.refresh(new_st)
    return {"Student ": new_st}


class Student(BaseModel):
    name: str
    id: int
    dept: str
    cgpa: float



# @app.post("/post")
# def createStudent(st: Student):
#     cursor.execute(
#         "INSERT INTO STUDENT (NAME, ID, DEPT, CGPA) VALUES (%s, %s, %s, %s) RETURNING *",
#         (st.name, st.id, st.dept , st.cgpa)
#     )
#     new_post = cursor.fetchone()
#     conn.commit()
#     return {"data": new_post}  




# while True:
#     try:
#         conn = psycopg2.connect(
#             host = "localhost",
#             database = "university",
#             user = "postgres",
#             password = "1234",
#             cursor_factory = RealDictCursor
#         )

#         cursor = conn.cursor()
#         print("Successfully Connected To The Database")
#         break
#     except Exception as error:
#         print("Database Connection Failed")
#         print("Error : ", error)
#         time.sleep(2)


# @app.get("/student/{st_id}")
# def view_student(st_id: int):
#     cursor.execute("SELECT * FROM STUDENT WHERE id = %s", (st_id,))
#     st = cursor.fetchone()  
#     if not st:
#         raise HTTPException(
#             status_code=404,
#             detail=f"Student with ID {st_id} Not Found"
#         )
#     return {"Student Details": st}


# @app.delete("/student/delete/{st_id}")
# def delete (st_id : int):
#     cursor.execute(""" DELETE FROM STUDENT WHERE id = %s RETURNING * """,
#                    (st_id,))
#     st = cursor.fetchone()
#     conn.commit()

#     return {"Deleted Student : ":  st}


# @app.put("/student/update/{st_id}")
# def update_student(st_id : int, st: Student1):
#     cursor.execute(""" UPDATE STUDENT SET name = %s, dept = %s, cgpa = %s WHERE id = %s RETURNING * """,
#                    (st.name,  st.dept, st.cgpa, st_id))
    
#     update_st = cursor.fetchone()
#     conn.commit()
#     return {"Updated Student" : update_st}



