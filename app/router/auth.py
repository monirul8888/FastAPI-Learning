from fastapi import FastAPI, status, HTTPException, Depends, Response, APIRouter
from sqlalchemy.orm import Session
from .. import database,models, utils, schemas

router = APIRouter(tags= ["Authentication"])

@router.post("/login")
def login(user_cred: schemas.UserLogin, db: Session= Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_cred.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credential")
    if not utils.verify_password(user_cred.password, user.password):
        raise HTTPException(status_code=404, detail="Invalid Credential")
    
    return {"token" : "Successfully Log In"}
