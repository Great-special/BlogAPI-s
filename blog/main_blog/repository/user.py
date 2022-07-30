from fastapi import HTTPException, status

from .. import models, schemas
from ..hashing import Hash


def createUser(request, db):
    new_user = models.User(fullname=request.fullname, email=request.email, phone=request.phone, 
                           password=Hash.Bcrypt(request.password))
    print(type(new_user))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def getUser(id, db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    
    return user


