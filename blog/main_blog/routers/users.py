from fastapi import APIRouter, Depends, status, Response, HTTPException 
from typing import List
from sqlalchemy.orm import Session
from main_blog import schemas, models, database
from main_blog.repository import user

get_db = database.get_db
router = APIRouter(
    prefix="/user",
    tags=['User']
)


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.createUser(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session= Depends(get_db)):
    return user.getUser(id, db) 

