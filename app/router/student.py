from fastapi import FastAPI, HTTPException, Depends, APIRouter
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from .. import models, schemas, utils
from sqlalchemy.orm import Session
from .. database import engine, get_db

from typing import List

router = APIRouter()


@router.post("/student", response_model=schemas.StudentResponse)
def student(st: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_st = models.Student(**st.model_dump())
    db.add(new_st)
    db.commit()
    db.refresh(new_st)
    return  new_st

@router.get("/student", response_model=List[schemas.StudentResponse])
def student(db:Session = Depends(get_db)):

    st = db.query(models.Student).all()
    return st

    

@router.get("/student/{st_id}", response_model=schemas.StudentResponse)
def student(st_id: int, db:Session = Depends(get_db)):

    st = db.query(models.Student).filter(models.Student.id == st_id).first()

    return st


@router.put("/student/{st_id}", response_model=schemas.StudentResponse)
def student(st_id: int, update_st: schemas.StudentCreate, db:Session = Depends(get_db)):

    st = db.query(models.Student).filter(models.Student.id == st_id)
    st_data= st.first()
    st.update(update_st.model_dump(), synchronize_session=False )
    db.commit()
    db.refresh(st_data)
    return st_data


@router.delete("/student/{st_id}")
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



