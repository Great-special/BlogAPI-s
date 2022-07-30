from fastapi import FastAPI

from main_blog import models
from main_blog.database import SessionLocal, engine, get_db
from main_blog.routers import authentication, blogs, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(authentication.router)

