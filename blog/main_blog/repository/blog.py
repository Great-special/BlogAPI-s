from fastapi import HTTPException
# from sqlalchemy.orm import Session
from .. import models, schemas


def getAll_blog(db ):
    blogs = db.query(models.Blogs).all()
    
    return blogs 



def build(request, db):
    new_blog = models.Blogs(title=request.title, body=request.body, user_id=1)
    print(type(new_blog))
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def getBlog_ById(id, db):
    blog = db.query(models.Blogs).filter(models.Blogs.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail":f"Blog with the id {id} is not available"}
    return blog


def deleteBlog_id(id, db):
    blog = db.query(models.Blogs).filter(models.Blogs.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Done !" 

def updateBlog_id(id, db):
    # updated_blog = models.Blogs(title=request.title, body=request.body)
    blog = db.query(models.Blogs).filter(models.Blogs.id == id)
    print(type(request))
    if not blog.first():
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    blog.update(dict(request))
    db.commit()
    return "Done!!!"