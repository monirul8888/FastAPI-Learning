from fastapi import FastAPI
from . router import user, student, auth
app = FastAPI()

app.include_router(user.router)
app.include_router(student.router)
app.include_router(auth.router)




@app.get("/")
def view():

    # cursor.execute(""" SELECT * FROM STUDENT """)
    # data = cursor.fetchall()
    return {"message" : "Welcome To FastAPI"}
            # "Data": data}



# @app.get("/about")
# def about():
#     return {"about" : "This is About Page"}




# class Student(BaseModel):
#     name: str
#     id: int
#     dept: str
#     cgpa: float



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





