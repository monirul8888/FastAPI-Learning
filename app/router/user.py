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


@router.post("/users", response_model=schemas.UserResponse)
def user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.email==user.email).first():
        raise HTTPException(status_code=400, detail=f"Email {user.email} already exists")
    hashedPassword = utils.hashPassword(user.password)
    user.password  = hashedPassword
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user