from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from main_blog import Oauth2, database, models, schemas
from main_blog.repository import blog
from sqlalchemy.orm import Session

get_db = database.get_db
router = APIRouter(
    prefix = "/blog",
    tags=['Blogs']
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog]) # decorator
def get_blogs(db:Session = Depends(get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.getAll_blog(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.build(request, db)
    


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show_id(id, response: Response, db:Session = Depends(get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.getBlog_ById(id, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id,  db:Session = Depends(get_db),  current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.deleteBlog_id(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(Oauth2.get_current_user)):
    return blog.updateBlog_id(id, db)



