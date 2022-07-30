from pydantic import BaseModel
from typing import List, Union

# Schemas hold the data entered by the user

class User(BaseModel):
    fullname: str
    email: str
    phone: int
    password: str


class BlogBase(BaseModel):
    title: str
    body: str
    
class Blog(BlogBase):
    class Config:
        orm_mode = True
    
    
class ShowUser(BaseModel):
    fullname: str
    email: str
    phone: int
    blog: List[Blog] = []
    
    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title:str
    creator: ShowUser
    class Config:
        orm_mode = True
        

class Login(BaseModel):
    username:str
    password:str
    class Config:
        orm_mode = True 


class Token(BaseModel):
    access_token: str
    token_type: str

   
class TokenData(BaseModel):
    email: Union[str, None] = None