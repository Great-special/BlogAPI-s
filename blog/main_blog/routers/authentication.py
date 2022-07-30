from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from main_blog import JWTtoken, database, models, schemas
from main_blog.hashing import Hash

router = APIRouter(
    # prefix=('/auth'),
    tags=['Authentication']
)


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    print(user.password, user.email)
    if not user:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Invalid Credentials")
        
    if not Hash.Verify(request.password, user.password):
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Invalid Credential")
    
    # Generate a jwt token and return
    access_token_expires = timedelta(minutes=30)
    access_token = JWTtoken.create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

